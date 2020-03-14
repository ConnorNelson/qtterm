#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py3qterm", # Replace with your own username
    version="0.4",
    author="Michael Ramsey",
    author_email="mike@hackerdise.me",
    description="Simple terminal/console widget for PyQt5/Pyside2 with vt100 support based on pyqtermwidget(https://bitbucket.org/henning/pyqtermwidget) Original Author: Henning Schroeder ",
    url="https://gitlab.com/mikeramsey/py3qtermwidget",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
