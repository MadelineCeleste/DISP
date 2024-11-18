from setuptools import find_packages
from setuptools import setup

setup(name='DISP',
      version='1.0',
      description='Data interpreter for Stelum and Pulse codes',
      author='Nathan Guyot',
      packages=find_packages('.'),
      packages_dir={'','.'},
     )