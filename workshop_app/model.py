from contextvars import ContextVar
import aiopg
from aiohttp import web
from .errors import ApplicationException

DB_CURSOR = ContextVar('cursor', default=None)


class DBController:
    @property
    def cursor(self):
        return DB_CURSOR.get()

    async def insert_user(self, email, password, name):
        await self.cursor.execute(
            r"INSERT INTO users(email, password, name) "
            r"VALUES (%s, %s, %s) RETURNING id",
            (email, password, name)
        )
        new_id = await self.cursor.fetchone()
        return new_id

    async def get_user(self, uid):
        await self.cursor.execute(
            r"SELECT id, email, name FROM users WHERE id = %s", (uid,),
        )
        response = await self.cursor.fetchone()
        if not response:
            raise ApplicationException(
                f'User with id={uid} is not found',
                status_code=404
            )
        id, email, name = response
        return {
            'id': id,
            'email': email,
            'name': name
        }

    async def get_user_by_auth(self, email, password):
        await self.cursor.execute(
            r"SELECT id FROM users WHERE email = %s and password = %s",
            (email, password)
        )
        response = await self.cursor.fetchone()
        if not response:
            raise ApplicationException(
                f'Either email or password are incorrect',
                status_code=401
            )
        return response[0]

    async def search_users_by_name(self, name):
        await self.cursor.execute(
            r"SELECT id, email, name FROM users WHERE name LIKE %s", (f'%{name}%',),
        )
        response = await self.cursor.fetchall()
        results = []
        for entry in response:
            id, email, name = entry
            results.append({
                'id': id,
                'email': email,
                'name': name
            })
        return results


async def pg_engine(app):
    async with aiopg.connect(
        user='postgres', host='database', password='S0meP@ssw0rd',
        database='test',
        echo=True,
    ) as pg_engine:
        app['pg_engine'] = pg_engine
        yield


@web.middleware
async def db_cursor(request, handler):
    async with await request.app['pg_engine'].cursor() as cursor:
        DB_CURSOR.set(cursor)
        response = await handler(request)
        return response
