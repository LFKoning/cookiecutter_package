"""Module with pre-generation cookiecutter hooks."""
import re
import sys


user_input = {
    "project": {
        "value": "{{ cookiecutter.project }}",
        "pattern": r"^[a-zA-Z][a-zA-Z0-9\-_\s]+$",
    },
    "package_name": {
        "value": "{{ cookiecutter.package_name }}",
        "pattern": r"^[a-z][a-z0-9\-]+$",
    },
    "package_path": {
        "value": "{{ cookiecutter.package_path }}",
        "pattern": r"^[a-z][a-z0-9_]+$",
    },
    "azure_project": {
        "value": "{{ cookiecutter.azure_project }}",
        "pattern": r"^[a-zA-Z\-]+$",
    },
    "azure_repo": {
        "value": "{{ cookiecutter.azure_repo }}",
        "pattern": r"^[a-z][a-z0-9\-_]+$",
    },
    "azure_url": {
        "value": "{{ cookiecutter.azure_url }}",
        "pattern": r"^https://afm-spot-on@dev.azure.com/afm-spot-on/[a-zA-Z\-]+/_git/[a-z][a-z0-9\-_]+$",
    },
}

# Check sanity of the inputs
for field, check in user_input.items():
    if not re.match(check["pattern"], check["value"]):
        print(f"ERROR: Input {field!r} contains invalid characters: {check['value']!r}!")
        sys.exit(1)
