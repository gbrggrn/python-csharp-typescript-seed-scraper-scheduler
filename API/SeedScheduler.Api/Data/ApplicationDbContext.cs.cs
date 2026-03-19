using Microsoft.EntityFrameworkCore;
using SeedScheduler.Api.Models;

namespace SeedScheduler.Api.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public DbSet<Plant> Plants { get; set; }
        public DbSet<Garden> Gardens { get; set; }
		}
}