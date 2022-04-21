"""Package Setup File"""
import setuptools

#TODO: Fill in dependecies here
REQUIREMENTS = []

# Requirements for running unit tests
TEST_REQUIREMENTS = ["pytest", "pytest-cov"]

# Development requirements
EXTRAS_REQUIRE = {
    "dev": ["black", "pylint", "pre-commit"] + TEST_REQUIREMENTS,
}

def get_readme():
    """Returns contents of README.md."""
    try:
        with open("README.md", "r", encoding="utf-8") as readme_file:
            return readme_file.read()
    except OSError:
        return "Error: Cannot read from README.md!"

setuptools.setup(
    # Author info
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",

    # Package info
    name="{{cookiecutter.package_name}}",
    version="0.0.1",

    description="{{cookiecutter.package_description}}",
    long_description=get_readme(),
    keywords="{{cookiecutter.package_keywords}}",
    url="{{cookiecutter.azure_url}}",

    # See: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: {{cookiecutter.python_version}}",
    ],

    # Dependency specifications
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS_REQUIRE,
    tests_require=TEST_REQUIREMENTS,

    package_dir={"{{ cookiecutter.package_path }}": "src/{{ cookiecutter.package_path }}"},
    packages=setuptools.find_packages("src"),
    test_suite="tests",
    {% if cookiecutter.includes_data.startswith("y") %}include_package_data=True,
    package_data=["{{ cookiecutter.package_path }}", "package_data/*"],{% endif %}
    {% if cookiecutter.includes_cli.startswith("y") %}entry_points={"console_scripts": ["greeting = {{ cookiecutter.package_path }}.cli:main"]},{% endif %}
)
