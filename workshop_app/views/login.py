from aiohttp import web
from .base import BaseView

routes = web.RouteTableDef()


@routes.view('/auth/login')
class LoginView(BaseView):
    async def post(self):
        return web.json_response({
            'token': '1'
        })
