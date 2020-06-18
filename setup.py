import setuptools
from setuptools import dist
from distutils.core import Extension

engine = Extension(
    'engine', 
    sources=[
            './ctest/_lib/engine.cpp',
            './ctest/_lib/functions.cpp',
            './ctest/_lib/utils.cpp'
        ],
    language='c++'
)

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="ctest",
    version="1.0.0",
    author="Debesh Mandal",
    description="Package for testing C implementations in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    ext_modules = [engine]
)
