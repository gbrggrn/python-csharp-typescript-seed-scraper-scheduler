namespace SeedScheduler.Api.Services;

public class LLMClient
{
    private readonly HttpClient _httpClient;

    public LLMClient()
    {
        _httpClient = new HttpClient();
    }
}