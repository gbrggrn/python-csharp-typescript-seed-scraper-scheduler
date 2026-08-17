using System.Reflection.Metadata.Ecma335;
using System.Runtime.CompilerServices;
using System.Text;
using System.Text.Json;
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

    public async Task<string> GetGeneralConditions(Garden garden)
    {
        var prompt = $"Garden data: name = {garden.Name}, avarage first day of frost = {garden.AverageFirstFrostDay}, avarage last day of frost = {garden.AverageLastFrostDay}, longitude = {garden.Longitude}, latitude = {garden.Latitude}";
        var model = "llama3.2";
        var system = @"You are a gardening expert and your job is to provide a summary of the general conditions for growing vegetables in a garden based on the data in the prompt. Maximum 200 words and no filler content. Be terse.";

        var body = new
        {
            model = model,
            prompt = prompt,
            system = system,
            stream = false
        };

        var requestBody = JsonSerializer.Serialize(body);
        var content = new StringContent(requestBody, Encoding.UTF8, "application/json");
        
        var response = await _httpClient.PostAsync("api/generate", content);
        response.EnsureSuccessStatusCode();
        var result = await response.Content.ReadAsStringAsync();

        using var doc = JsonDocument.Parse(result);
        if (doc.RootElement.TryGetProperty("response", out JsonElement responseProp))
        {
            string responseValue = responseProp.GetString();
            return responseValue;
        }
        else
        {
            return "fail";
        }
    }

    public async Task<string> GetWeatherSummary(JsonObject weatherPackage)
    {
        return "";
    }
}