using Microsoft.AspNetCore.Mvc;
using SeedScheduler.Api.Models;
using SeedScheduler.Api.Services;
using SeedScheduler.Api.Shared.DTOs;

namespace SeedScheduler.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class GardenController : ControllerBase
{
        private readonly GardenService _gardenService;

    public GardenController(GardenService gardenService)
    {
        _gardenService = gardenService;
    }

    [HttpGet]
    public async Task<IActionResult> ReadAll()
    {
        var response = _gardenService.ReadAllAsync();

        if (response == null)
            return NotFound("Could not find any Gardens.");

        return Ok(response);
    }

    [HttpPost]
    public async Task<IActionResult> Add(GardenCreateDTO gardenCreateDTO)
    {
        if (gardenCreateDTO == null)
            return BadRequest("The request body was empty.");
        
        await _gardenService.AddAsync(gardenCreateDTO);

        return Ok($"The garden: {gardenCreateDTO.Name} was successfully added.");
    }

    [HttpPut("{id}")]
    public async Task<IActionResult> Update(GardenUpdateDTO gardenUpdateDTO, int id)
    {
        if (gardenUpdateDTO == null)
            return BadRequest("The request body was empty.");

        if (id <= 0)
            return BadRequest("The id was <= 0");

        await _gardenService.UpdateAsync(gardenUpdateDTO, id);

        return Ok($"The garden {gardenUpdateDTO.Name} was updated.");
    }

    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete (int id)
    {
        if (id <= 0)
            return BadRequest("The id was <= 0");

        await _gardenService.DeleteAsync(id);
        
        return Ok();
    }

}
