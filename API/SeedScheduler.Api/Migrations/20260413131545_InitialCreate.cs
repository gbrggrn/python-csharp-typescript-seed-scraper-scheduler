using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace SeedScheduler.Api.Migrations
{
    /// <inheritdoc />
    public partial class InitialCreate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Gardens",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Name = table.Column<string>(type: "TEXT", nullable: false),
                    Longitude = table.Column<float>(type: "REAL", nullable: false),
                    Latitude = table.Column<float>(type: "REAL", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Gardens", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Plants",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Name = table.Column<string>(type: "TEXT", nullable: false),
                    SowDepth = table.Column<int>(type: "INTEGER", nullable: false),
                    MinGerminationDays = table.Column<int>(type: "INTEGER", nullable: false),
                    MaxGerminationDays = table.Column<int>(type: "INTEGER", nullable: false),
                    RowSpacing = table.Column<int>(type: "INTEGER", nullable: false),
                    PlantSpacing = table.Column<int>(type: "INTEGER", nullable: false),
                    MinSowMonth = table.Column<int>(type: "INTEGER", nullable: false),
                    MaxSowMonth = table.Column<int>(type: "INTEGER", nullable: false),
                    MinHarvestMonth = table.Column<int>(type: "INTEGER", nullable: false),
                    MaxHarvestMonth = table.Column<int>(type: "INTEGER", nullable: false),
                    IsPerennial = table.Column<bool>(type: "INTEGER", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Plants", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Schedules",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Schedules", x => x.Id);
                });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Gardens");

            migrationBuilder.DropTable(
                name: "Plants");

            migrationBuilder.DropTable(
                name: "Schedules");
        }
    }
}
