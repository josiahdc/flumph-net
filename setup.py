from setuptools import setup, find_packages

setup(
    name="Flumphnet",
    version="0.0.1",
    author="Josiah Chapman",
    packages=find_packages("src"),
    tests_require=[
        "pytest",
    ]
)
