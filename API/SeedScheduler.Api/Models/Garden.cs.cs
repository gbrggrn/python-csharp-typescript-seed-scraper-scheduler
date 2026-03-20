namespace SeedScheduler.Api.Models;

public class Garden
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;

    public float Longitude { get; set; }
    public float Latitude { get; set; }
}
