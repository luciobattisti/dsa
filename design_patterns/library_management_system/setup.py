from setuptools import setup, find_packages

setup(
    name="libs",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[],
    author="Alessandro Lusci",
    author_email="alelusci1@gmail.com",
    description="SOLID Principles Exercise",
    long_description_content_type="text/markdown",
    url="http://alusci.test.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
)