using Microsoft.AspNetCore.Mvc;
using SeedScheduler.Api.Models;
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
        var response = await _plantService.GetAllAsync();
        if (response == null || response.Count <= 0)
            return NotFound("No plants found.");

        return Ok(response);
    }

    [HttpPost]
    public async Task<IActionResult> Add(PlantCreateDTO plantCreateDTO)
    {
        if (plantCreateDTO == null)
            return BadRequest("The request body was empty.");

        await _plantService.AddAsync(plantCreateDTO);

        return Ok($"The plant: {plantCreateDTO.Name} was added.");
    }

    [HttpPost("batch")]
    public async Task<IActionResult> AddBatch(List<PlantCreateDTO> plantCreateDTOs)
    {
        if (plantCreateDTOs == null || plantCreateDTOs.Count <= 0)
            return BadRequest("The request body was empty.");

        await _plantService.AddBatchAsync(plantCreateDTOs);

        return Ok("Batch of plants added.");
    }

    [HttpPut("{id}")]
    public async Task<IActionResult> Update(PlantUpdateDTO plantUpdateDTO, int id)
    {
        if (plantUpdateDTO == null)
            return BadRequest("The request body was empty.");

        if (id <= 0)
            return BadRequest("The id was <= 0");

        await _plantService.UpdateAsync(plantUpdateDTO, id);

        return Ok($"The plant: {plantUpdateDTO.Name} was updated.");
    }

    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete (int id)
    {
        if (id <= 0)
            return BadRequest("The id was <= 0");

        await _plantService.DeleteAsync(id);

        return Ok("Delete successful.");
    }
}