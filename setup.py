from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    requirements = []
    
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements] 
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
setup(name='ML_Pipeline_project',
      version='0.0.1',
      description='Machine Learning Pipeline project',
      author= 'Thanmayi Vempala',
      author_email='vempalathanmayi@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements("requirements.txt")
      )    