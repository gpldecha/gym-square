from setuptools import setup
from setuptools import find_packages

setup(name='gym_square',
      version='0.0.1',
      author='Guillaume de Chambrier',
      author_email='chambrierg@gmail.com',
      description='A simple square world environment for openai/gym',
      packages=find_packages(),
      url='https://github.com/gpldecha/gym-square',
      license='MIT',
      install_requires=['gym']
)


