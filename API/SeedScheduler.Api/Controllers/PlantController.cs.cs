using Microsoft.AspNetCore.Mvc;
using SeedScheduler.Api.Services;
using SeedScheduler.Api.Shared.DTOs;

namespace SeedScheduler.Api.Controllers;

[Route("api/[controller]")]
[ApiController]
public class PlantController : ControllerBase
{
    private readonly PlantService _plantService;

    public PlantController(PlantService plantService)
    {
        _plantService = plantService;
    }

    [HttpGet]
    public async Task<IActionResult> ReadAll()
    {
        return Ok();
    }

    [HttpPost]
    public async Task<IActionResult> Add(PlantCreateDTO plantCreateDTO)
    {
        return Ok();
    }

    [HttpPost("batch")]
    public async Task<IActionResult> AddBatch(List<PlantCreateDTO> plantCreateDTOs)
    {
        return Ok();
    }

    [HttpPut("{id}")]
    public async Task<IActionResult> Update(PlantUpdateDTO plantUpdateDTO, int id)
    {
        return Ok();
    }

    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete (int id)
    {
        return Ok();
    }
}