using Microsoft.EntityFrameworkCore;
using SeedScheduler.Api.Data;
using SeedScheduler.Api.Models;
using SeedScheduler.Api.Shared.DTOs;

namespace SeedScheduler.Api.Services;

public class GardenService
{
    private readonly ApplicationDbContext _dbContext;
    private readonly DbSet<Garden> _gardens;

    public GardenService(ApplicationDbContext dbContext)
    {
        _dbContext = dbContext;
        _gardens = dbContext.Gardens;
    }

    public async Task<List<GardenResponseDTO>> ReadAllAsync()
    {
        
    }

    public async Task AddAsync(GardenCreateDTO dto)
    {
        
    }

    public async Task<bool> UpdateAsync(GardenUpdateDTO dto, int id)
    {
        
    }

    public async Task<bool> DeleteAsync(int id)
    {
        
    }
}
