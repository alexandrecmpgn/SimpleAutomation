from setuptools import setup, find_packages

setup(
    name="SimpleAutomation",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    author="Alexandre CMPGN",
    description="Un petit package pour automatiser rapidement des tâches sur son ordinateur sous forme de sessions.",
)