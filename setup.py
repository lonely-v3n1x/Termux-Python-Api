# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('LICENSE') as lic_file:
    license_text = lic_file.read()

setup(
    name="Termux-API",
    version="0.0.1",
    description="Python script to provide access to termux api",
    long_description=readme,
    author="lonely-v3n1x",
    author_email="",
    license=license_text,
    packages=find_packages(exclude=('tests', 'docs'))
)
