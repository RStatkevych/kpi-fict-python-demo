from aiohttp import web
from .base import BaseView

routes = web.RouteTableDef()


@routes.view('/auth/login')
class LoginView(BaseView):
    async def post(self):
        data = await self.request.json()
        uid = await self.db.get_user_by_auth(data['email'], data['password'])
        token = await self.auth.authenticate(uid)
        return web.json_response({
            'token': token
        })
