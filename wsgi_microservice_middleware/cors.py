import urllib.parse
import logging
import wsgi_microservice_middleware


CORS_ALLOWED = wsgi_microservice_middleware.env.list("CORS_ALLOWED", tuple())


logger = logging.getLogger(__name__)


class CORSMiddleware(object):
    """
    Adds CORS headers to the responses of request that originate from domains inthe
    CORS_ALLOWED environment variable.  CORS_ALLOWED should reside in the environment as a
    comma-separated string of domain names.
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):

        def custom_start_response(status, headers, exc_info=None):
            # append whatever headers you need here
            origin = urllib.parse.urlparse(environ.get('HTTP_ORIGIN'))
            if origin.netloc in CORS_ALLOWED:
                logger.info("Cross-origin request approved for request origin {0}".format(origin))
                headers.append(('Access-Control-Allow-Origin', '*'))
                headers.append(
                    ('Access-Control-Allow-Headers', '*')
                )
                headers.append(('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, HEAD, OPTIONS'))
            return start_response(status, headers, exc_info)

        return self.app(environ, custom_start_response)