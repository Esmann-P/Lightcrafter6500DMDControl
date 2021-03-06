from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name = 'Hello world app',
    ext_modules = cythonize("dither_c.pyx"),
    include_dirs=[np.get_include()]
)