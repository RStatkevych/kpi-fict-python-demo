import aioredis
import uuid
from contextvars import ContextVar
from aiohttp import web


class AuthProvider:
    def __init__(self, view):
        self.view_instance = view

    async def authenticate(self, uid):
        pass


async def redis_cache(app):
    redis = aioredis.from_url(
        "redis://redis", encoding="utf-8", decode_responses=True
    )
    async with redis.client() as conn:
        app['redis'] = conn
        yield conn
