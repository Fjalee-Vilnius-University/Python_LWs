import setuptools
from distutils.core import setup, Extension

def main():
    setup(name="checkPalindrome",
          version="1.0.0",
          description="Python interface for checkPalindrome function",
          author="Justas Vitkauskas",
          author_email="justas.vitkauskas@mif.stud.vu.lt",
          ext_modules=[Extension("checkPalindrome", ["checkPalindrome.c"])])

if __name__ == "__main__":
    main()