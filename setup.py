import logging
from setuptools import setup, find_packages

install_requires = []

try:
    with open('requirements.txt', 'r', encoding='utf-8') as requirements_file:
        install_requires = requirements_file.readlines()
except Exception:
    logging.warning("Exception raised when attempting to read the requirements.txt using utf-8 encoding.")
    logging.warning("Retry reading requirements.txt using utf-16 encoding")
    with open('requirements.txt', 'r', encoding='utf-16') as requirements_file:
        install_requires = requirements_file.readlines()
    

setup(
    name='autocore',
    version='1.0.13',
    packages=find_packages(),
    install_requires=install_requires
)