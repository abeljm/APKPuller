import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="apkpuller",
    version="1.0.1",
    description="Tool extract APKs from device to desktop directories",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abeljm/APKPuller",
    author="Avelino Navarro",
    author_email="abeljm2017@gmail.com",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    packages=["apkpuller"],
    include_package_data=True,
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "apkpuller=apkpuller.apkpuller:main",
        ]
    },
)