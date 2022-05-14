import setuptools
from distutils.core import setup, Extension

def main():
    setup(name="checkPalindrome",
          version="1.0.0",
          description="module for finding fibonacci nth number",
          author="Rytis Cepulis",
          author_email="rytis.cepulis@mif.stud.vu.lt",
          ext_modules=[Extension("checkPalindrome", ["checkPalindrome.c"])])

if __name__ == "__main__":
    main()