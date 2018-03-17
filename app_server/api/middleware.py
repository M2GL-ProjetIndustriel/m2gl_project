import threading

from threading import current_thread

_thread_locals = threading.local()

def get_request():
    return getattr(_thread_locals, 'request', None)

class CurrentUserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        _thread_locals.request=request
