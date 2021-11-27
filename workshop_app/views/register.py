from aiohttp import web
from .base import BaseView

routes = web.RouteTableDef()


@routes.view('/auth/register')
class RegisterView(BaseView):
    async def post(self):
        return web.json_response({'id': '1'})
