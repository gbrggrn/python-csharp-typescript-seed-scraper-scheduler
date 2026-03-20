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
            Latitude = g.Latitude
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
}
