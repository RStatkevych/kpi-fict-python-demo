from aiohttp import web

class ApplicationException(Exception):
    def __init__(self, *args, status_code=400, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status_code
