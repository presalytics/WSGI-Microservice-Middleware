# WSGI Microservice Middleware

This little library contains middlewares to help quickly turn wsgi apps (e.g., flask, django, bottle, tornado, pyramid) into production-ready microservices for integration into a kubernetes cluster.  These middelewares set up to be configurable warfrom environment variables in accordance with the twelve-factor app methodology.

Middlewares in this package include:
* [CORS](#cors)
* [Request Id](#request-id)


This project spun out of development for the Presalytics as way to quickly port code across various microserivces built on wsgi-supported frameworks.

[View on Github](https://github.com/presalytics/WSGI-Microservice-Middleware)

### Installation

This project requires python 3.5+. It is best installed fromt he pypi package repository via pip.

~~~~bash
pip install wsgi_microservice_middleware
~~~~

The latest branch of this package can also be installed from git:
~~~~bash
pip install git+https://github.com/presalytics/WSGI-Microservice-Middleware
~~~~

### Configuration

Package configuration is best done by adding configuration values via environment varialble.  This package uses the [environs](https://pypi.org/project/environs/) package to load the following values from the system environment or a `.env` file in the the working directory:

* `CORS_ALLOWED`: Comma-separated string of domain names that will from which CORS requests can be made.  Is empty by default

* `REQUEST_ID_HEADER`: The http request header containing a the request-id to including in logs. If not supplied, defaults to `X-Request-Id`.

### Usage 

These middleware are applied by wrapping the wsgi application object in you code by the middleware class. Examples below:

* **Flask:**
    ~~~~python
    # app.py
    from flask import Flask
    from wsgi_microservice_middleware.cors import CORSMiddleware

    app = Flask(__name__)
    app.wsgi_app = CORSMiddleware(app.wsgi_app) # Middleware applied here
    app.run(...) 
    ~~~~

* **Django:**
    ~~~~python
    # wsgi.py
    from django.core.wsgi import get_wsgi_application
    from wsgi_microservice_middleware.request_id import RequestIdMiddleware

    application = get_wsgi_application()
    application = RequestIdMiddleware(application) # Middleware applied here
    ~~~~


# Modules

### CORS

Adds CORS headers to the responses of request that originate from domains in the
CORS_ALLOWED environment variable.  CORS_ALLOWED should reside in the environment as a
comma-separated string of domain names.

### Request Id

Implements Request Id handling for requests that need to be tracked accross multiple microservices and searched in log records.
The `RequestIdMiddleware` class.

To extend the request Id to your application logs, incorporate the `RequestIdFilter` into your logging configuration. the best way to do this
is to use `logging.config.dictConfig` to apply the filter to all of your handlers:

~~~~python
# log_config.py
from logging.config import dictConfig
from wsgi_microservice_middleware.request_id import RequestIdFilter


dictConfig({
    'version': 1,
    'filters': {
        'request_id_filter' : {
            '()': RequestIdFilter,  # RequestIdFilter.filter(self, record) called with each log entry
        }

    },
    'formatters': {'default': {
        'format': '%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(request_id)s -  %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['request_id_filter']  # add this filter to each handler
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})
~~~~

If your microservice makes requests to other microservices, you can call the `current_request_id()` method to get the current request id and 
incorporate it into your request headers.

# Contributing

We'd love your help! Open an issue at the [github repo](https://github.com/presalytics/WSGI-Microservice-Middleware/issues).  Or even better, you can fork the repo and we'll merge your improvements.
