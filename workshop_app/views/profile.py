from aiohttp import web
from .base import BaseView
from ..auth import auth_required
routes = web.RouteTableDef()


@routes.view('/profile/{id}')
class ProfileView(BaseView):

    @auth_required
    async def get(self):
        id_ = self.request.match_info.get('id')
        if id_ == 'me':
            id_ = self.auth.get_user_id()

        data = await self.db.get_user(id_)
        return web.json_response(data)
