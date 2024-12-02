from setuptools import setup, find_packages

setup(
    # basic info
    name="api-detection-tool",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # metadata
    author="Granth Agarwal",
    author_email="heygranth@gmail.com",
    description="A tool to detect API keys in code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # install dependencies
    install_requires=["typing"],
    # entry point for the CLI
    entry_points={
        "console_scripts": [
            "api-detection-tool=core:main",
        ],
    },
    # classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
