namespace SeedScheduler.Api.Shared.DTOs;

public class GardenCreateDTO
{
    // Identifiers
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;

    // Location
    public float Longitude { get; set; }
    public float Latitude { get; set; }
}
