# setup.py

from setuptools import setup, find_packages

setup(
    name="pysecurity1024",
    version="0.1.0",
    author="Josemar Poubel L.",
    author_email="josemarpoubel@msn.com",
    description="Entropy engine and semantic dissolution for high-security systems",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/josemarpoubel/pysecurity1024",
    
    py_modules=["pysecurity1024"],
    
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "cryptography",
        "pycryptodome",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
    ],
)
