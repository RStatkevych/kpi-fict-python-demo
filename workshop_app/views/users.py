from aiohttp import web
from .base import BaseView

routes = web.RouteTableDef()



@routes.view('/users')
class UsersView(BaseView):
    async def get(self):
        users = [{'id': 2, 'name': 'John Doe', 'email': 'jon@doe.com'},
                 {'id': 1, 'name': 'Linus Torvalds', 'email': 'ihate@windows.com'}]
        return web.json_response({'users': users})
