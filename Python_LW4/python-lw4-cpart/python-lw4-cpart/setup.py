from setuptools import setup, Extension

module = Extension("main", sources = ["main.cpp"])

setup(name="PackageName",
    version = "1.0",
    description = "my C module",
    ext_modules = [module])