"""Module with pre-generation cookiecutter hooks."""
import re
import sys


def check_sanity(value):
    """Check whether user input is sane."""
    return re.match(r"[a-z0-9\-_]+", value, re.IGNORECASE)


# Check sanity of the inputs
user_input = {
    "project": "{{cookiecutter.project}}",
    "package_name": "{{cookiecutter.package_name}}",
    "package_path": "{{cookiecutter.package_path}}",
    "azure_project": "{{cookiecutter.azure_project}}",
    "azure_repo": "{{cookiecutter.azure_repo}}",
}

for item, value in user_input.items():
    if not check_sanity(value):
        print(f"ERROR: Input {item} contains invalid characters!")
        sys.exit(1)
