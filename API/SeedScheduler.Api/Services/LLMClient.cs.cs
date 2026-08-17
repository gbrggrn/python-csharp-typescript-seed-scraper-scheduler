using System.Reflection.Metadata.Ecma335;
using System.Text.Json.Nodes;
using Microsoft.AspNetCore.SignalR;

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

    public async string GetGeneralConditions(float lat, float lon)
    {
        
    }

    public async string GetWeatherSummary(JsonObject weatherPackage)
    {
        
    }
}