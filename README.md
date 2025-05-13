# Toml_to_yml_convertor

## Overview
The `Toml_to_yml_convertor` is a Python script designed to convert dependencies specified in a `pyproject.toml` file into a Conda environment file (`environment.yml`). This tool is particularly useful for developers who want to seamlessly transition their Python project dependencies into a Conda environment.

## Features
- Extracts dependencies from the `[project]` section of `pyproject.toml`.
- Automatically detects the Python version specified in the `pyproject.toml` file.
- Generates a Conda-compatible `environment.yml` file with pip dependencies included.

## Requirements
- Python 3.6 or higher
- `toml` Python library

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd toml_to_yml_convertor
   ```
2. Install the required Python library:
   ```bash
   pip install toml
   ```

## Usage
1. Place your `pyproject.toml` file in the same directory as the script.
2. Run the script:
   ```bash
   python script.py
   ```
3. Enter the desired output filename when prompted (default: `environment.yml`).
4. The generated `environment.yml` file will include all dependencies from the `pyproject.toml` file.

## Example
Given the following `pyproject.toml`:
```toml
[project]
dependencies = [
    "django>=3.2",
    "pillow>=8.0"
]
requires-python = ">=3.8"
```
The script will generate the following `environment.yml`:
```yaml
name: myenv
channels:
  - conda-forge
dependencies:
  - python=3.8
  - pip
  - pip:
      - django==3.2
      - pillow==8.0
```
