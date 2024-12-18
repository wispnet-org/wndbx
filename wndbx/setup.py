from setuptools import setup, find_packages

setup(
    name="wndbx",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tkinter",  # Example of a package dependency
        "sqlite3",
    ],
)
