using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace SeedScheduler.Api.Migrations
{
    /// <inheritdoc />
    public partial class GardensFrostMigration : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<int>(
                name: "AverageFirstFrostDay",
                table: "Gardens",
                type: "INTEGER",
                nullable: false,
                defaultValue: 0);

            migrationBuilder.AddColumn<int>(
                name: "AverageLastFrostDay",
                table: "Gardens",
                type: "INTEGER",
                nullable: false,
                defaultValue: 0);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "AverageFirstFrostDay",
                table: "Gardens");

            migrationBuilder.DropColumn(
                name: "AverageLastFrostDay",
                table: "Gardens");
        }
    }
}
