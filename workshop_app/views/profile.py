from aiohttp import web
from .base import BaseView
routes = web.RouteTableDef()


@routes.view('/profile/{id}')
class ProfileView(BaseView):

    async def get(self):
        return web.json_response({'id': 1, 'name': 'Linus Torvalds', 'email': 'ihate@windows.com'})
