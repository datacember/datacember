from setuptools import setup, find_packages

setup(
    name="datacember",
    version="0.1.1",
    description="A package for queryeing the datacember server",
    author="Alexander",
    author_email="wingfooted3@gmail.com",
    url="https://github.com/datacember/datacember",
    packages=find_packages(),
    install_requires=[
        "requests>=2.27.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
