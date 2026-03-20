using Microsoft.AspNetCore.Mvc;
using SeedScheduler.Api.Services;

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
        return Ok();
    }

    [HttpPost]
    public async Task<IActionResult> Add(GardenCreateDTO gardenCreateDTO)
    {
        return Ok();
    }

    [HttpPost("batch")]
    public async Task<IActionResult> AddBatch(List<GardenCreateDTO> gardenCreateDTOs)
    {
        return Ok();
    }

    [HttpPut("{id}")]
    public async Task<IActionResult> Update(GardenUpdateDTO gardenUpdateDTO, int id)
    {
        return Ok();
    }

    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete (int id)
    {
        return Ok();
    }

}
