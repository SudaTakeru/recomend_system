# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:41:31 2018

@author: buryu-
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rsys_by_suda",
    version="0.0.1",
    author="Takeru Suda",
    author_email="buryunogotoku@gmail.com",
    description="A recomend system package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SudaTakeru/recomend_system",
    packages=setuptools.find_packages(),
)