from setuptools import setup, find_packages

# read the requirements file and use it to install the dependencies
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

# setup the package - This information will be used to create the package
# and upload it to PyPI
setup(
    name="blkpy-package",
    description="A python CLI tool for listing block devices and files",
    packages=find_packages(),
    author="Rashid Rasul",
    author_email="rashid.rasul@me.com",
    entry_points={
        "console_scripts": [
            "blkpy=blkpy.main:cli"
        ]
    },
    install_requires=install_requires,
    version="0.1.0",
    url="https://github.com/rstrategist/python-cli",
)
# To install the package in editable mode, run the following command:
# pip install -e .