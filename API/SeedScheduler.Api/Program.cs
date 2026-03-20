using SeedScheduler.Api.Data;
using Microsoft.EntityFrameworkCore;
using SeedScheduler.Api.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddOpenApi();

builder.Services.AddScoped<PlantService>();
builder.Services.AddScoped<GardenService>();
builder.Services.AddScoped<ScheduleService>();

var connectionString = builder.Configuration.GetConnectionString("DefaultConnection") ?? throw new InvalidOperationException("Connection string 'DefaultConnection' not found.");
            builder.Services.AddDbContext<ApplicationDbContext>(options =>
                options.UseSqlite(connectionString));

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();
app.UseAuthorization();

app.MapControllers();

app.Run();