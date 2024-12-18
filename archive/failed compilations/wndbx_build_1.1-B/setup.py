from setuptools import setup, find_packages
import webbrowser

setup(
    name="wndbx",
    version="1.1-B",
    description="Your project description here",
    author="William S. Popovici",
    packages=find_packages(),
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'wndbx=wndbx.main:main',  # Adjust this to match your `main.py`
        ],
    },
)
