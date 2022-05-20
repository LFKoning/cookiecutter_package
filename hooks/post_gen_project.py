"""Module with pre-generation cookiecutter hooks."""
import os

print("\n\n")
print("Post-processing cookiecutter template.")


def is_yes(value):
    """Checks for a yes input."""
    if isinstance(value, str) and value.lower().startswith("y"):
        return True
    return False

# Create git repo
if is_yes("{{cookiecutter.create_conda}}"):
    print("Setting up the git repository.")
    os.system("git init")

    print("Adding remote: {{cookiecutter.azure_url}}.")
    os.system("git remote add origin {{cookiecutter.azure_url}}")

# Create Anaconda environment
if is_yes("{{cookiecutter.create_conda}}"):
    print("Creating Anaconda environment: {{cookiecutter.package_name}}.")
    os.system(
        "conda create --yes -n {{cookiecutter.package_name}} "
        + "python={{cookiecutter.python_version}}"
    )

    print("Installing development packages.")
    os.system(
        "conda activate {{cookiecutter.package_name}} "
        + "& python -m pip install black pylint pre-commit"
    )

    # Setup pre-commit
    if is_yes("{{cookiecutter.precommit}}"):
        print("Installing pre-commit hooks.")
        os.system("conda activate {{cookiecutter.package_name}} & pre-commit install")

print("All done!")
