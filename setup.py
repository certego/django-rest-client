from pathlib import Path
from setuptools import setup, find_packages

# constants
GITHUB_URL = "https://github.com/certego/django-rest-client"

# The directory containing this file
HERE = Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()
# Define requirements
requirements = ["requests", "typing_extensions"]
requirements_cli = ["click"]
requirements_dev = (HERE / "requirements.dev.txt").read_text().split("\n")
# read version
version_contents = {}
with open((HERE / "django_rest_client" / "version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

# This call to setup() does all the work
setup(
    name="django_rest_client",
    version=version_contents["VERSION"],
    description="An abstract and extensible framework for building python SDK and CLI for APIs built with django-rest-framework and other such general frameworks.",
    long_description=README,
    long_description_content_type="text/markdown",
    url=GITHUB_URL,
    author="Certego S.R.L",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=requirements,
    project_urls={
        "Documentation": GITHUB_URL,
        "Source": GITHUB_URL,
        "Tracker": f"{GITHUB_URL}/issues",
    },
    keywords="sdk python command line django rest framework api client coreapi",
    extras_require={
        "cli": requirements + requirements_cli,
        "dev": requirements + requirements_cli + requirements_dev,
    },
    entry_points="""
        [console_scripts]
        django_rest_client_example=example_project.cli:cli
    """,
)
