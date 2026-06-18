namespace SeedScheduler.Api.Models;

public class Garden
{
    public string Name { get; set; } = string.Empty;

    public float Longitude { get; set; }
    public float Latitude { get; set; }

    public int AverageFirstFrostDay { get; set; } // (1-365)
    public int AverageLastFrostDay { get; set; } // (1-365)
}
