from distutils.core import setup
from Cython.Build import cythonize

setup(name='fib_cython',
      ext_modules=cythonize("fib_cython.pyx"))