from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path : str) -> List[str]:
    '''
    Returns a list of requirements for running the source code to obtain a deployable application
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [rep.replace("\n", "") for rep in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements

setup(
    author = "Sohbat Infostride",
    version = "0.0.1",
    name = "Fraud Detection using Simulated Data",
    author_email = "sohbat.sandhu@infostride.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)