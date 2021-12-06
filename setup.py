from setuptools import setup, find_packages
from canibalize.__version__ import __version__

setup(
    name='canibalize', 
    version=__version__,
    packages=find_packages(),
    author='0xffox',
    author_email='dancing.0xffox@yandex.ru',
    description='Allows you to canibalize methods from classes effectively implementing trait-oriented programming'
)
    

