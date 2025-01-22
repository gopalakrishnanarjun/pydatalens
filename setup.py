from setuptools import setup, find_packages

setup(
    name="PyDataLens",
    version="0.1",
    description="A Python package for automatic EDA, data cleaning, and visualization.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
    ],
    python_requires=">=3.6",
)
