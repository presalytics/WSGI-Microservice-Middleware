# coding: utf-8

"""
WSGI Microservice Middleware

Simple middlewares to help move microservices into production
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "wsgi_microservice_middleware"
VERSION = "0.1.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.15",
    "environs >= 7.3.0",
]

with open("readme.md", "r") as fh:
    long_description = fh.read()
    

setup(
    name=NAME,
    version=VERSION,
    description="WSGI Microservice Middleware",
    author_email="inquiries@presalytics.io",
    url="https://github.com/presalytics/wsgi_microserice_middleware",
    keywords=["WSGI", "middleware", "microservice"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=long_description
)
