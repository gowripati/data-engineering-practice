from setuptools import setup, find_packages

setup(
    name='data_tools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    description='Custom data engineering utilities package',
    author='Your Name',
)
