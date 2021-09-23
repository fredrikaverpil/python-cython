from setuptools import setup
from Cython.Build import cythonize

setup(name="primes", version="0.0.1", ext_modules=cythonize("primes.pyx"))
