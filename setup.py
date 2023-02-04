
from setuptools import setup, find_packages
from typing import List

REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Descrition :  This function is going to return the list og requirement
    mentioned in requirements.txt file
    
    return: This is going to return list which contains name of the  required libraries.

    """

    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

        

#Declaring the variables for setup function

setup(
name="Housing-predictor",
version="0.0.2",
author="Sourav",
description="This is first end to end ML project",
packages=find_packages(), # ["housing"]
install_requires=get_requirements_list()
)