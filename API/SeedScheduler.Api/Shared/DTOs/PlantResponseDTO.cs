namespace SeedScheduler.Api.Shared.DTOs;

public class PlantResponseDTO
{
    // Identifiers
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;

    // Description
    public string Description { get; set; } = string.Empty;
    public string Url { get; set; } = string.Empty;

    // Growth properties
    public float SowDepth { get; set; }
    public float MinGerminationDays { get; set; }
    public float MaxGerminationDays { get; set; }
    public float MinHeight { get; set; }
    public float MaxHeight { get; set; }
    public float RowSpacing { get; set; }
    public float PlantSpacing { get; set; }
    public float MinSowMonth { get; set; }
    public float MaxSowMonth { get; set; }
    public float MinHarvestMonth { get; set; }
    public float MaxHarvestMonth { get; set; }
}
