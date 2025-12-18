from setuptools import setup, find_packages

setup(
    name="azt-logging",
    version="0.0.1",
    description="Logging solution to store entries in Azure Data Tables.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="runway28R",
    url="https://github.com/runway28R/azt-logging",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.12",
    install_requires=[
        "azure-data-tables>=12.7.0"
    ],
    keywords=["logging", "azure data table"],
    classifiers=[
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
