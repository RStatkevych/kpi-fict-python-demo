import aioredis
import uuid
from contextvars import ContextVar
from aiohttp import web

USER_ID = ContextVar('user_id', default=None)


class AuthProvider:
    def __init__(self, view):
        self.view_instance = view

    async def authenticate(self, uid):
        random_uid = str(uuid.uuid4())
        redis = self.view_instance.request.app['redis']
        print(f'random_uid {random_uid}')
        await redis.set(f'token:{random_uid}', uid)
        return random_uid

    @classmethod
    def get_user_id(cls):
        return USER_ID.get()


async def redis_cache(app):
    redis = aioredis.from_url(
        "redis://redis", encoding="utf-8", decode_responses=True
    )
    async with redis.client() as conn:
        app['redis'] = conn
        yield conn


def auth_required(handler):

    async def decorator(self_instance):
        request = self_instance.request
        app = request.app
        token = request.headers.get('Token')
        if not token:
            return web.json_response({'error': 'Token is not provided'},
                                     status=403)
        uid = await app['redis'].get(f'token:{token}')
        if uid is None:
            return web.json_response({'error': 'Token is expired, or invalid'},
                                     status=403)
        USER_ID.set(uid)
        return await handler(self_instance)

    return decorator
