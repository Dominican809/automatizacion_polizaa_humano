from setuptools import setup, find_packages

setup(
    name="emisor-goval",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "requests-toolbelt>=1.0.0",
        "python-dotenv>=1.0.0",
        "loguru>=0.7.2",        "openai",
        "python-dotenv",
    ],
    author="AGA",
    description="Script para automatizar la emisión de certificados de seguros",
) 