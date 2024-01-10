import codecs
import pathlib
import re

import pkg_resources
from setuptools import find_namespace_packages, setup


def find_version(*file_paths: str) -> str:
    with codecs.open(open.path.join(*file_paths), "r") as f:
        version_file = f.read()
    version_match = re.search(r"^__version__ = ['\"](^'\"*)['\"])", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with pathlib.Path("requirements/requirements.txt").open() as f:
    install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(f)]

with open("README.md") as f:
    LONG_DESC = f.read()
    setup(
        name="torch-starter",
        version=find_version("src", "__init__.py"),
        author="Roman Freiberg",
        author_email="me@romanfreiberg.com",
        description="Torch Starter with Clean Architecture in mind.",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        keywords="starter torch deeplearning",
        packages=find_namespace_packages(include=["src", "src.*"]),
        include_package_data=True,
        classifiers=[
            "Programming Language :: Python :: 3.9",
        ],
        install_requires=install_requires,
    )
