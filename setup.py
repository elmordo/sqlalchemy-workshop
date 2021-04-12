# -*- coding: utf-8 -*-
"""

"""

from __future__ import absolute_import

from os.path import dirname, join
from setuptools import setup, find_namespace_packages

__copyright__ = "Copyright (c) 2015-2019 Ing. Petr Jindra. All Rights Reserved."


SRC_DIR = "src"

requirements_path = join(dirname(__file__), "requirements.txt")


def get_requirements():
    with open(requirements_path, "r") as fd:
        return [r for r in fd]


def main():
    setup(
        version="1.0.0",
        name="saw",
        package_dir={"": SRC_DIR},
        packages=find_namespace_packages(SRC_DIR),
        install_requires=get_requirements(),
        data_files=[("", ["requirements.txt"])]
    )


if __name__ == "__main__":
    main()
