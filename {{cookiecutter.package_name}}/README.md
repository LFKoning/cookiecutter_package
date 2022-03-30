# {{cookiecutter.project|title}}

## Goal

TODO: Briefly describe the goal of the project here...

## Installation

To install this project on the workbench, first create a new Anaconda environment:

```shell
conda create -n {{cookiecutter.package_name}} python={{cookiecutter.python_version}}
```

Activate the environment to start working with it:

```shell
conda activate {{cookiecutter.package_name}}
```

Then create a folder for the project and clone the repository from Azure DevOps:

```shell
git clone {{cookiecutter.azure_url}}
```

Finally, install the package using pip:

```shell
python -m pip install .
```

Or, if you want to contribute to the package, use this command instead:

```shell
python -m pip install -e .[dev]
```

## Usage

TODO: Describe how to use your project...


## Authors

This project is maintained by:

1. {{cookiecutter.author_name}} ({{cookiecutter.author_email}})
