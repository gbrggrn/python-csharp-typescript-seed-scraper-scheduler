using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace SeedScheduler.Api.Migrations
{
    /// <inheritdoc />
    public partial class UpdateSchemaForDescriptionUrlUid : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "IsPerennial",
                table: "Plants");

            migrationBuilder.AddColumn<string>(
                name: "Description",
                table: "Plants",
                type: "TEXT",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "Uid",
                table: "Plants",
                type: "TEXT",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddColumn<string>(
                name: "Url",
                table: "Plants",
                type: "TEXT",
                nullable: false,
                defaultValue: "");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "Description",
                table: "Plants");

            migrationBuilder.DropColumn(
                name: "Uid",
                table: "Plants");

            migrationBuilder.DropColumn(
                name: "Url",
                table: "Plants");

            migrationBuilder.AddColumn<bool>(
                name: "IsPerennial",
                table: "Plants",
                type: "INTEGER",
                nullable: false,
                defaultValue: false);
        }
    }
}
