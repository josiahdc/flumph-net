from setuptools import setup, find_packages

installation_requirements = [
    "loguru==0.5.3",
    "ujson==4.0.1",
    "SLPP==1.2.3",
    "psycopg2==2.8.6",
    "yoyo-migrations==7.2.1",
]

setup(
    name="flumphnet",
    description="Command and control server for managing Opencomputers robots",
    version="0.0.1",
    author="Josiah Chapman",
    packages=find_packages(include=["src"]),
    tests_require=installation_requirements
)
