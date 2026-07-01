using System.Text.Json.Nodes;
using Microsoft.EntityFrameworkCore;
using SeedScheduler.Api.Data;
using SeedScheduler.Api.Models;
using SeedScheduler.Api.Shared.DTOs;

namespace SeedScheduler.Api.Services;

public class GardenService
{
    private readonly ApplicationDbContext _dbContext;
    private readonly DbSet<Garden> _gardens;

    public GardenService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
        _gardens = dbContext.Gardens;
    }

    public async Task<List<GardenResponseDTO>> ReadAllAsync()
    {
        return await _gardens.Select(g => new GardenResponseDTO
        {
            Id = g.Id,
            Name = g.Name,
            Longitude = g.Longitude,
            Latitude = g.Latitude,
            AverageLastFrostDay = g.AverageLastFrostDay,
            AverageFirstFrostDay = g.AverageFirstFrostDay
        }).ToListAsync();
    }

    public async Task AddAsync(GardenCreateDTO dto)
    {
        var newGarden = new Garden
        {
            Name = dto.Name,
            Longitude = dto.Longitude,
            Latitude = dto.Latitude
        };

        await _gardens.AddAsync(newGarden);
        await _dbContext.SaveChangesAsync();
    }

    public async Task<bool> UpdateAsync(GardenUpdateDTO dto, int id)
    {
        var existingGarden = await _gardens.FindAsync(id);
        if (existingGarden == null)
            return false;

        existingGarden.Id = dto.Id;
        existingGarden.Name = dto.Name;
        existingGarden.Longitude = dto.Longitude;
        existingGarden.Latitude = dto.Latitude;

        _gardens.Update(existingGarden);
        await _dbContext.SaveChangesAsync();

        return true;
    }

    public async Task<bool> DeleteAsync(int id)
    {
        if (id <= 0)
            return false;

        var garden = await _gardens.FindAsync(id);
        if (garden == null)
            return false;

        _gardens.Remove(garden);
        await _dbContext.SaveChangesAsync();

        return true;
    }

    public async Task<int> GetClosestStationId(float targetLat, float targetLon)
    {
        using var client = new HttpClient();

        client.DefaultRequestHeaders.Add("User-Agent", "SeedSchedulerApp");

        var url = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1.json";
        var jsonRoot = await client.GetFromJsonAsync<JsonNode>(url);

        var stationArray = jsonRoot?["station"]?.AsArray();

        if (stationArray == null)
            throw new Exception("Failed to parse SMHI stations");

        int closestStationId = 0;
        float shortestDistance = float.MaxValue;

        foreach (var node in stationArray)
        {
            if (node == null)
                continue;
            
            if (node["active"]?.GetValue<bool>() == false)
                continue;

            float stationLat = node["latitude"]?.GetValue<float>() ?? 0;
            float stationLon = node["longitude"]?.GetValue<float>() ?? 0;

            float dLat = targetLat - stationLat;
            float dLon = targetLon - stationLon;
            float distanceSquared = (dLat * dLat) + (dLon * dLon);

            if (distanceSquared < shortestDistance)
            {
                shortestDistance = distanceSquared;
                closestStationId = node["id"]?.GetValue<int>() ?? 0;
            }
        }

        return closestStationId;
    }

    public async Task<JsonArray> GetFrostData(int stationId)
    {
        using var client = new HttpClient();
        client.DefaultRequestHeaders.Add("User-Agent", "SeedSchedulerApp");

        var url = $"https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/19/station/{stationId}.json";
        var jsonRoot = await client.GetFromJsonAsync<JsonNode>(url);

        var minTempArray = jsonRoot?["value"]?.AsArray() ?? new JsonArray();

        return minTempArray;
    }

    public void CalculateAvgFrost(JsonArray minTempArray, Garden garden)
    {
        var recordsByYear = minTempArray
            .Where(node => node != null)
            .Select(node =>
            {
                float temp = float.Parse(node["value"]?.GetValue<string>() ?? "0");
                long unixMillis = node["date"]?.GetValue<long>() ?? 0;
                var date = DateTimeOffset.FromUnixTimeMilliseconds(unixMillis).DateTime;
                return new { Date = date, Temp = temp};
            })
            .GroupBy(r => r.Date.Year);

        List<int> lastSpringFrostDays = [];
        List<int> firstFallFrostDays = [];

        foreach (var yearGroup in recordsByYear)
        {
            var lastSpringFrost = yearGroup
                .Where(r => r.Date.DayOfYear < 180 && r.Temp <= 0)
                .OrderByDescending(r => r.Date.DayOfYear)
                .FirstOrDefault();

            var firstFallFrost = yearGroup
                .Where(r => r.Date.DayOfYear > 180 && r.Temp >= 0)
                .OrderByDescending(r => r.Date.DayOfYear)
                .FirstOrDefault();

            if (lastSpringFrost != null)
                lastSpringFrostDays.Add(lastSpringFrost.Date.DayOfYear);

            if (firstFallFrost != null)
                firstFallFrostDays.Add(firstFallFrost.Date.DayOfYear);
        }

        if (lastSpringFrostDays.Any())
            garden.AverageLastFrostDay = (int)lastSpringFrostDays.Average();

        if (firstFallFrostDays.Any())
            garden.AverageFirstFrostDay = (int)firstFallFrostDays.Average();
    }

    /*
    public async Task<bool> GetGenWeatherData(int stationId)
    {
        
    }

    public async Task<bool> GenerateWeatherSummary(JsonObject weatherPayload)
    {
        
    } */
}