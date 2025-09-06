# A setup.py file in Python is a script used to configure and manage the packaging 
# and distribution of Python projects. 
# It traditionally uses the setuptools library to define various aspects of a Python package, 
# enabling it to be easily installed and used by others.

# Key functions and contents of a setup.py file:

# Metadata Definition:It contains essential metadata about the package, such as:
# name: The name of the package (must be unique if published on PyPI).
# version: The version number of the package.
# author: and author_email: Information about the package's creator.
# description: and long_description: A brief and detailed description of the package's purpose.
# license: The license under which the package is distributed.
# classifiers: Categories that help users find the package on PyPI.

# Package Inclusion:
# It specifies which files and directories constitute the package's source code, 
# often using find_packages() or find_namespace_packages() from setuptools.

# Dependency Management:
# It lists the external libraries or packages that your project depends on 
# using the install_requires argument, ensuring they are installed 
# when your package is installed.
from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = 'Machine Learning Project'
VERSION = "0.0.1"
DESCRIPTION = " This is our Machine Learning Project in modular coding"
AUTHOR_NAME = " HARISH S"
AUTHOR_EMAIL = "harish.s.140597@gmail.com"

REQUIREMENTS_FILE_NAME = "requirement.txt"
HYPHEN_E_DOT = "-e ."
# Requirement.txt file open
# read
# replace \n with "" empty

def get_requirement_list()  -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list ]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list
    pass

setup(name= PROJECT_NAME ,
      version= VERSION,
      description= DESCRIPTION,
      author= AUTHOR_NAME,
      author_email= AUTHOR_EMAIL,
    #   url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_requires = get_requirement_list()
     )