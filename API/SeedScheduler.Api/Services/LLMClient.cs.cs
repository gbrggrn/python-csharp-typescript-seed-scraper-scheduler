using System.Reflection.Metadata.Ecma335;
using System.Runtime.CompilerServices;
using System.Text.Json.Nodes;
using Microsoft.AspNetCore.SignalR;
using SeedScheduler.Api.Models;

namespace SeedScheduler.Api.Services;

public class LLMClient
{
    private readonly HttpClient _httpClient;
    private readonly string baseAddress = "http://192.168.39.179:11434";

    public LLMClient()
    {
        _httpClient = new HttpClient()
        {
            BaseAddress = new Uri(baseAddress)
        };
    }

    public async string GetGeneralConditions(Garden garden)
    {
        string prompt = $"Restrictions: 1. Maximum 200 words 2. No filler content. | Instructions: Generate a summary of the general conditions for growing vegetables in a garden based on provided data. | Data: name = {garden.Name}, avarage first day of frost = {garden.AverageFirstFrostDay}, avarage last day of frost = {garden.AverageLastFrostDay}, longitude = {garden.Longitude}, latitude = {garden.Latitude}";

        
    }

    public async string GetWeatherSummary(JsonObject weatherPackage)
    {
        
    }
}