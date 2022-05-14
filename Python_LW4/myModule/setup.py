from setuptools import setup, Extension

module = Extension("myModule", sources = ["main.c"])

setup(name="PackageName",
    version = "1.0",
    description = "my C module",
    ext_modules = [module])