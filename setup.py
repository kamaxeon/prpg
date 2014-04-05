import os
from setuptools import setup



base_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name = "prpg",
    version = "0.0.1",
    description = "A library to generate strong and random password",
    #long_description="\n\n".join([
    #    open(os.path.join(base_dir, "README.rst"), "r").read(),
    #    open(os.path.join(base_dir, "CHANGELOG.rst"), "r").read()
    #]),
    url = "https://github.com/kamaxeon/prpg",
    author = "Israel Santana",
    author_email = "isra@miscorreos.org",
    packages = ["prpg"],
    zip_safe = False,
    #install_requires = install_requires,
    #tests_require = tests_require,
    test_suite = "tests.get_tests",
)