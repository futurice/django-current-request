from django.conf import settings
from django.middleware.csrf import get_token

import threading
_thread_locals = threading.local()

def get_current_request():
    return getattr(_thread_locals, 'request', None)

def reset_current_request():
    setattr(_thread_locals, 'request', None)

class RequestMiddleware(object):

    def process_request(self, request):
        get_token(request) # force CSRFTOKEN setup
        _thread_locals.request = request

    def process_response(self, request, response):
        reset_current_request()
        return response
