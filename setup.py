#!/usr/bin/env python3
"""
Setup script for Aeroget
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aeroget",
    version="1.0.0",
    author="BeeKitchen7-hash",
    description="Nettoyeur de données personnelles avec interface Frutiger Aero",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BeeKitchen7-hash/aeroget",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Systems Administration",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyQt6>=6.6.0",
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.2",
        "selenium>=4.13.0",
        "Pillow>=10.0.1",
        "psutil>=5.9.5",
        "lxml>=4.9.3",
    ],
    entry_points={
        "console_scripts": [
            "aeroget=main:main",
            "aeroget-cli=cli:main",
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/BeeKitchen7-hash/aeroget/issues",
        "Documentation": "https://github.com/BeeKitchen7-hash/aeroget/wiki",
        "Source Code": "https://github.com/BeeKitchen7-hash/aeroget",
    },
)
