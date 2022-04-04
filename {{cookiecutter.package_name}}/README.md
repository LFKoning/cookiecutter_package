# {{cookiecutter.project|title}}

## Goal

TODO: Briefly describe the goal of the project here...

## Installation

### For regular users

If you just want to use this project, you can simply install it with:

```shell
python -m pip install git+{{cookiecutter.azure_url}}
```

This will install the package and all of its dependencies into your current Anaconda
environment.

### For developers

If you want to help develop this project, please follow the following steps to get
started.

First, create a new Anaconda environment for the project:

```shell
conda create -n {{cookiecutter.package_name}} python={{cookiecutter.python_version}}
```

Next, activate the environment to start working with it:

```shell
conda activate {{cookiecutter.package_name}}
```

Then clone the repository from Azure DevOps to your personal folder on Workbench:

```shell
git clone {{cookiecutter.azure_url}}
```

Finally, install the package and its dependencies using pip:

```shell
python -m pip install -e .[dev]
```

## Usage

TODO: Describe how people should use your project...

## Contributing

If you want to contribute to this project, feel free to clone the code, make
improvements and open a pull request!

If you have suggestions or remarks not directly related to the project's code or
documentation, feel free to e-mail the authors.

## Authors

This project is maintained by:

1. {{cookiecutter.author_name}} ({{cookiecutter.author_email}})
