from aiohttp import web
from .base import BaseView

routes = web.RouteTableDef()


@routes.view('/auth/register')
class RegisterView(BaseView):
    async def post(self):
        data = await self.request.json()
        password = data.get('password')
        confirm_password = data.get('confirm')
        username = data.get('name')

        if password != confirm_password:
            return web.json_response({'error': 'Password mismatch'}, status=401)
        uid = await self.db.insert_user(
            email=data.get('email'),
            name=username,
            password=password
        )
        return web.json_response({'id': uid[0]})
