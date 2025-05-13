import toml
from pathlib import Path

# Load TOML
pyproject_path = Path("pyproject.toml")
if not pyproject_path.exists():
    print("❌ pyproject.toml not found in current directory.")
    exit(1)

data = toml.load(pyproject_path)

# Adjusted to handle dependencies from the [project] section
# Extract dependencies
deps = data.get("project", {}).get("dependencies", [])
python_version = data.get("project", {}).get("requires-python", "3.10").lstrip(">=")

# Convert dependencies list to a dictionary
parsed_deps = {}
for dep in deps:
    if ">=" in dep:
        pkg, version = dep.split(">=")
        parsed_deps[pkg.strip()] = version.strip()
    else:
        parsed_deps[dep.strip()] = None

deps = parsed_deps

# Ask for output filename
output_name = input("Enter output filename [default: environment.yml]: ").strip()
if not output_name:
    output_name = "environment.yml"

# Generate YAML content
lines = [
    "name: myenv",
    "channels:",
    "  - conda-forge",
    "dependencies:",
    f"  - python={python_version}",
    "  - pip",
    "  - pip:"
]
for pkg, version in deps.items():
    if version:
        lines.append(f"      - {pkg}=={version}")  # Corrected to use '==' for version specification
    else:
        lines.append(f"      - {pkg}")

# Write to file
with open(output_name, "w") as f:
    f.write("\n".join(lines))

print(f"✅ Conda environment file written to '{output_name}'")
