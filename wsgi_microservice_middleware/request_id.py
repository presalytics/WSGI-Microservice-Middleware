"""
Middleware and logging filter to add request ids to logs and forward request Ids in downstream requests
"""
import logging
import traceback
import wsgi_microservice_middleware


logger = logging.getLogger(__name__)


REQUEST_ID_HEADER_NAME = wsgi_microservice_middleware.env.str("REQUEST_ID_HEADER", "X-Request-Id")


def make_wsgi_header_key(header: str):
    wsgi_header = "HTTP_" + REQUEST_ID_HEADER_NAME.replace("-","_").upper()
    return wsgi_header

class RequestIdMiddleware(object):
    """
    This middleware add access log-style record with a request id and includes
    the request Id in int he response headers
    """
    def __init__(self, app, header_name: str = None):
        self.header_name = header_name
        if not self.header_name:
            self.header_name = REQUEST_ID_HEADER_NAME
        self.wsgi_header_key = make_wsgi_header_key(self.header_name)
        self.app = app

    def __call__(self, environ, start_response):

        def custom_start_response(status, headers, exc_info=None):
            # append whatever headers you need here
            FACTS = [
                environ.get("HTTP_HOST", ""),
                environ.get("REQUEST_METHOD", ""),
                environ.get("RAW_URI", ""),
                environ.get("SERVER_PROTOCOL", ""),
                status
            ]
            message = " | ".join(FACTS)
            request_id = environ.get(self.wsgi_header_key, 'No Request Id')
            adpater = logging.LoggerAdapter(logger, extra={"request_id": request_id})
            adpater.info(message)


            headers.append((self.header_name, request_id,))

            return start_response(status, headers, exc_info)

        return self.app(environ, custom_start_response)



def current_request_id():
    """
    Retrives the current request id from the wsgi `environ` buried in the call stack
    """
    _req = None
    wsgi_header = "HTTP_" + REQUEST_ID_HEADER_NAME.replace("-","_").upper()
    try:
        for frame in traceback.walk_stack(None):
            if getattr(frame[0], 'f_globals', None) and getattr(frame[0], 'f_locals', None):
                if frame[0].f_globals.get('__name__', None) == __name__ and 'environ' in frame[0].f_locals:
                    environ = frame[0].f_locals['environ']
                    _req = environ.get(wsgi_header, None)
                    break
    except Exception:
        pass
    return _req


class RequestIdFilter(logging.Filter):
    """
    Logger filter to add a `{request_id}` logger variable tot he logging context
    """
    def __init__(self, header_name=REQUEST_ID_HEADER_NAME, *args, **kwargs):
        self.header_name = header_name
        self.wsgi_header_key = "HTTP_" + self.header_name.replace("-","_").upper()
        super().__init__(*args, **kwargs)

    def filter(self, record):
        record.request_id = self.get_current_request_id()
        return True

    def get_current_request_id(self):
        _req = current_request_id()
        if _req:
            request_id = _req
        else: 
            request_id = "No Request Id"
        return request_id


