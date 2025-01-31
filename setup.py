from setuptools import setup, find_packages

setup(
    name="PyDataLens",
    version="0.1",
    description="A Python package for automatic EDA, data cleaning, and visualization.",
    author='Gopalakrishn Arjunan',
    author_email='gopalakrishnana02@gmail.com',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
    ],
    python_requires=">=3.6",
)
