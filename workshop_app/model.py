from contextvars import ContextVar
import aiopg
from aiohttp import web
from .errors import ApplicationException


class DBController:

    async def insert_user(self, email, password, name):
        pass
    async def get_user(self, uid):
        pass
    async def get_user_by_auth(self, email, password):
        pass
    async def search_users_by_name(self, name):
        pass


async def pg_engine(app):
    async with aiopg.connect(
        user='postgres', host='database', password='test',
        database='test',
        echo=True,
    ) as pg_engine:
        app['pg_engine'] = pg_engine
        yield
