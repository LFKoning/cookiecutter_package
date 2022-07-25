"""Module with pre-generation cookiecutter hooks."""
import os
import shutil


def is_yes(value):
    """Checks for a yes input."""
    if isinstance(value, str) and value.lower().startswith("y"):
        return True
    return False


print("\n\n")
print("Post-processing cookiecutter template.")

# Copy README.md to docs/index.md
shutil.copy("README.md", "docs/index.md")

# Remove unnecessary CLI example files
if not is_yes("{{ cookiecutter.includes_cli }}"):
    print("Cleaning up CLI example files.")
    os.remove("src/{{ cookiecutter.package_path }}/cli.py")

# Remove unnecessary data example files
if not is_yes("{{ cookiecutter.includes_data }}"):
    print("Cleaning up package data example files.")
    os.remove("MANIFEST.in")
    os.remove("src/{{ cookiecutter.package_path }}/read_data.py")
    shutil.rmtree("src/{{ cookiecutter.package_path }}/package_data")

# Create git repo
if is_yes("{{ cookiecutter.create_git }}"):
    print("Setting up the git repository.")
    os.system("git init")

    print("Adding remote: {{ cookiecutter.azure_url }}.")
    os.system("git remote add origin {{ cookiecutter.azure_url }}")

# Create Anaconda environment
if is_yes("{{ cookiecutter.create_conda }}"):
    print("Creating Anaconda environment: {{ cookiecutter.package_name }}.")
    os.system(
        "conda create --yes --quiet --name {{ cookiecutter.package_name }} "
        + "python={{ cookiecutter.python_version }}"
    )

    print("Installing package with development dependencies.")
    os.system(
        "conda activate {{ cookiecutter.package_name }} "
        + "& python -m pip install -e .[dev]"
    )

    # Pre-commit setup
    if is_yes("{{ cookiecutter.precommit }}"):
        # Install pre-commit hooks
        # Note: Requires a git repository to be initialized!
        if is_yes("{{ cookiecutter.create_git }}"):
            print("Installing pre-commit hooks.")
            os.system(
                "conda activate {{ cookiecutter.package_name }} "
                + "& python -m pre-commit install"
            )
        else:
            print("Cannot install pre-commit hooks; no git repository!")
            print("Type `pre-commit install` in the package folder to install manually.")

    else:
        # Remove pre-commmit config
        os.remove(".pre-commit-config.yaml")

print("All done!")
