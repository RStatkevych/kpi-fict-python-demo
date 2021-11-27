from aiohttp import web
from .base import BaseView
from ..auth import auth_required

routes = web.RouteTableDef()



@routes.view('/users')
class UsersView(BaseView):
    @auth_required
    async def get(self):
        query_params = self.request.query
        name = query_params.get('name')
        print(name, 'query')
        if not name:
            return web.json_response({'users': []})
        users = await self.db.search_users_by_name(name)
        return web.json_response({'users': users})
