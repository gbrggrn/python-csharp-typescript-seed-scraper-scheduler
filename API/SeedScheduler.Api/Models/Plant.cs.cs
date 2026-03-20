namespace SeedScheduler.Api.Models;

public class Plant
{
    // Identifiers
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;

    // Growth properties
    public int SowDepth { get; set; }
    public int MinGerminationDays { get; set; }
    public int MaxGerminationDays { get; set; }
    public int RowSpacing { get; set; }
    public int PlantSpacing { get; set; }
    public int MinSowMonth { get; set; }
    public int MaxSowMonth { get; set; }
    public int MinHarvestMonth { get; set; }
    public int MaxHarvestMonth { get; set; }
    public bool IsPerennial { get; set; }
}
