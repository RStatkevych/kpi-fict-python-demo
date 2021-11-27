import pytest
import aiohttp
import aiopg


@pytest.fixture
async def aio_client(event_loop):
    async with aiohttp.ClientSession(base_url='http://application:8080') as session:
        yield session


@pytest.fixture(autouse=True)
async def pg_connection(event_loop):
    async with aiopg.connect(user='postgres', host='database',
                             password='test',
                             database='test',
                             echo=True,) as conn:
        async with conn.cursor() as cursor:
            yield cursor
            await cursor.execute('TRUNCATE users;')
