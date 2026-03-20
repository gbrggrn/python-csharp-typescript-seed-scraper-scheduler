using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.ModelBinding;
using Microsoft.EntityFrameworkCore;
using SeedScheduler.Api.Data;
using SeedScheduler.Api.Models;
using SeedScheduler.Api.Shared.DTOs;

namespace SeedScheduler.Api.Services;

public class PlantService
{
    private readonly ApplicationDbContext _dbContext;
    private readonly DbSet<Plant> _plants;

    public PlantService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
        _plants = _dbContext.Plants;
    }

    public async Task<List<PlantResponseDTO>> GetAllAsync()
    {
        return await _plants.Select(p => new PlantResponseDTO
        {
            Id = p.Id,
            Name = p.Name,
            SowDepth = p.SowDepth,
            MinGerminationDays = p.MinGerminationDays,
            MaxGerminationDays = p.MaxGerminationDays,
            RowSpacing = p.RowSpacing,
            PlantSpacing = p.PlantSpacing,
            MinSowMonth = p.MinSowMonth,
            MaxSowMonth = p.MaxSowMonth,
            MinHarvestMonth = p.MinHarvestMonth,
            MaxHarvestMonth = p.MaxHarvestMonth,
            IsPerennial = p.IsPerennial
        }).ToListAsync();
    }

    public async Task AddAsync(PlantCreateDTO dto)
    {
        var newPlant = new Plant
        {
            Name = dto.Name,
            SowDepth = dto.SowDepth,
            MinGerminationDays = dto.MinGerminationDays,
            MaxGerminationDays = dto.MaxGerminationDays,
            RowSpacing = dto.RowSpacing,
            PlantSpacing = dto.PlantSpacing,
            MinSowMonth = dto.MinSowMonth,
            MaxSowMonth = dto.MaxSowMonth,
            MinHarvestMonth = dto.MinHarvestMonth,
            MaxHarvestMonth = dto.MaxHarvestMonth,
            IsPerennial = dto.IsPerennial
        };

        await _plants.AddAsync(newPlant);
        await _dbContext.SaveChangesAsync();
    }

    public async Task AddBatchAsync(List<PlantCreateDTO> dtos)
    {
        var plants = new List<Plant>();
        for(int i = 0; i < dtos.Count; i++)
        {
            var newPlant = new Plant
            {
                Name = dtos[i].Name,
                SowDepth = dtos[i].SowDepth,
                MinGerminationDays = dtos[i].MinGerminationDays,
                MaxGerminationDays = dtos[i].MaxGerminationDays,
                RowSpacing = dtos[i].RowSpacing,
                PlantSpacing = dtos[i].PlantSpacing,
                MinSowMonth = dtos[i].MinSowMonth,
                MaxSowMonth = dtos[i].MaxSowMonth,
                MinHarvestMonth = dtos[i].MinHarvestMonth,
                MaxHarvestMonth = dtos[i].MaxHarvestMonth,
                IsPerennial = dtos[i].IsPerennial
            };

            plants.Add(newPlant);
        }

        _plants.AddRange(plants);
        await _dbContext.SaveChangesAsync();
    }

    public async Task<bool> UpdateAsync(PlantUpdateDTO dto, int id)
    {
        var existingPlant = await _plants.FindAsync(id);
        if(existingPlant == null)
            return false;
        
        existingPlant.Name = dto.Name;
        existingPlant.SowDepth = dto.SowDepth;
        existingPlant.MinGerminationDays = dto.MinGerminationDays;
        existingPlant.MaxGerminationDays = dto.MaxGerminationDays;
        existingPlant.RowSpacing = dto.RowSpacing;
        existingPlant.PlantSpacing = dto.PlantSpacing;
        existingPlant.MinSowMonth = dto.MinSowMonth;
        existingPlant.MaxSowMonth = dto.MaxSowMonth;
        existingPlant.MinHarvestMonth = dto.MinHarvestMonth;
        existingPlant.MaxHarvestMonth = dto.MaxHarvestMonth;
        existingPlant.IsPerennial = dto.IsPerennial;

        _plants.Update(existingPlant);
        await _dbContext.SaveChangesAsync();

        return true;
    }

    public async Task<bool> DeleteAsync(int id)
    {
        if (id <= 0)
            return false;

        var plant = await _plants.FindAsync(id);
        if (plant == null)
            return false;

        _plants.Remove(plant);
        await _dbContext.SaveChangesAsync();

        return true;
    }
}