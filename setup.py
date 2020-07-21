# coding: utf-8

"""
WSGI Microservice Middleware

Simple middlewares to help move microservices into production
"""


from setuptools import setup, find_packages, Extension  # noqa: H301

NAME = "wsgi_microservice_middleware"
VERSION = "0.1.6"

REQUIRES = [
    "urllib3 >= 1.15",
    "environs >= 4.2.0",
    "python-json-logger >=0.1.11"
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
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Natural Language :: English", 
        "Development Status :: 4 - Beta"
    ]
)
