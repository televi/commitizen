#!/usr/bin/env python

import io
import os

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "committer"
DESCRIPTION = "Commit to git using Convnetional Commits standard."
URL = "https://git.cic-nfv.com/Solutions/commiter"
EMAIL = "todd.levi@nokia.com"
AUTHOR = "Santiago Fraire, Todd Levi"
REQUIRED = [
    "delegator.py",
    "PyInquirer",
    "future",
    "prompt-toolkit>=1.0.15",
    'configparser; python_version < "3.5"',
]

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

about = {}
with open(os.path.join(here, NAME, "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    entry_points={"console_scripts": ["cz=commitizen.cli:main"]},
    keywords="commitizen conventional commits git",
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
