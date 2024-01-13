import pathlib

from setuptools import find_namespace_packages, setup


def parse_requirements_file(path):
    return [line.rstrip() for line in open(path, "r")]


reqs_main = parse_requirements_file("requirements/requirements.txt")
reqs_dev = parse_requirements_file("requirements/dev.txt")

with open("README.md", "r") as f:
    long_description = f.read()


init_str = pathlib.Path("src/__init__.py").read_text()
version = init_str.split("__version__ = ")[1].rstrip().strip('"')


with open("README.md") as f:
    LONG_DESC = f.read()
    setup(
        name="torch-starter",
        version=version,
        author="Roman Freiberg",
        author_email="me@romanfreiberg.com",
        description="Torch Starter with Clean Architecture in mind.",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        keywords="starter torch deeplearning",
        # rename the src directory to your project name and exchange the following
        # packages below
        packages=find_namespace_packages(include=["src", "src.*"]),
        include_package_data=True,
        classifiers=[
            "Programming Language :: Python :: 3.9",
        ],
        install_requires=reqs_main,
        extras_require={
            "dev": reqs_main + reqs_dev,
        },
    )
