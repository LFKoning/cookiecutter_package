"""Module with pre-generation cookiecutter hooks."""
import os

print("\n\n")
print("Post-processing cookiecutter template.")

# Create git repo
print("Setting up the git repository.")
os.system("git init")

print("Adding remote: {{cookiecutter.azure_url}}.")
os.system("git remote add origin {{cookiecutter.azure_url}}")

# Setup pre-commit
print("Installing pre-commit hooks.")
os.system("pre-commit install")

print("All done!")
