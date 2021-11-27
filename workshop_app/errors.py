from aiohttp import web

class ApplicationException(Exception):
    def __init__(self, *args, status_code=400, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.status_code = status_code


@web.middleware
async def error_handler(request,handler):
    try:
        return await handler(request)
    except ApplicationException as e:
        return web.json_response({'error': str(e)}, status=e.status_code)
