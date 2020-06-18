import setuptools
from distutils.core import Extension

module1 = Extension(
    'engine', 
    sources=[
            './ctest/_lib/engine.c',
            './ctest/_lib/functions.c'
        ])

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="ctest",
    version="0.0.1",
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
    ext_modules = [module1],
)
