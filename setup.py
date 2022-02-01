from setuptools import setup, find_packages

setup(
    name="k4pg",
    version="1.0.8",
    author="KeyFr4me",
    description="Pygame utilities used by KeyFr4me",
    packages=find_packages(),
    install_requires=["pygame>=2.0.1", "colorama"]
)
