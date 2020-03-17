# coding: utf-8

"""
WSGI Microservice Middleware

Simple middlewares to help move microservices into production
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "wsgi_microservice_middleware"
VERSION = "0.1.0"

REQUIRES = [
    "urllib3 >= 1.15",
    "environs >= 4.2.0",
]

with open("README.md", "r") as fh:
    long_description = fh.read()
    

setup(
    name=NAME,
    version=VERSION,
    description="WSGI Microservice Middleware",
    author_email="inquiries@presalytics.io",
    url="https://github.com/presalytics/WSGI-Microservice-Middleware",
    keywords=["WSGI", "middleware", "microservice"],
    install_requires=REQUIRES,
    packages=find_packages(),
    license="MIT",
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.5",
    project_urls = {
        "Issues": "https://github.com/presalytics/WSGI-Microservice-Middleware/issues"
    }
)
