from pathlib import Path
from setuptools import setup

PATH_README = Path(__file__).resolve().parent / 'README.md'

setup(
    name="cz_legacy",
    version="0.0.1",
    py_modules=["cz_legacy"],
    license="MIT",
    long_description=PATH_README.read_text(),
    install_requires=["commitizen"],
)
