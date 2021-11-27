import pytest

pytestmark = pytest.mark.asyncio


async def test_post_register(aio_client):
    test_password = 'p@ssw0rd'
    test_email = 'test@example.com'
    name = 'test-user'

    async with aio_client.post(
        '/auth/register',
        json={'email': test_email, 'password': test_password,
              'confirm': test_password, 'name': name}
    ) as response:
        resp_data = await response.json()
        uid = resp_data['id']

    async with aio_client.post(
        '/auth/login',
        json={
            'password': test_password,
            'email': test_email
        }
    ) as response:
        data = await response.json()
        assert 'token' in data
        token = data['token']

    async with aio_client.get(
        f'/profile/me',
        headers={'Token': token}
    ) as response:
        resp_data = await response.json()
        assert resp_data['email'] == 'test@example.com'

    wrong_id = -1
    async with aio_client.get(
        f'/profile/{wrong_id}',
        headers={'Token': token}
    ) as response:
        resp_data = await response.json()
        assert resp_data['error'] == f'User with id={wrong_id} is not found'
        assert response.status == 404


async def test_register_wrong_password(aio_client):
    test_password = 'p@ssw0rd'
    test_email = 'test@example.com'

    async with aio_client.post(
        '/auth/register',
        json={'email': test_email, 'password': test_password,
              'confirm': 'iamwrong'}
    ) as response:
        resp_data = await response.json()
        assert resp_data['error'] == 'Password mismatch'


async def test_wrong_login(aio_client):
    test_password = 'p@ssw0rd'
    test_email = 'bad@example.com'

    async with aio_client.post(
        '/auth/login',
        json={
            'password': test_password,
            'email': test_email
        }
    ) as response:
        data = await response.json()
        assert data['error'] == 'Either email or password are incorrect'
        assert response.status == 401


async def test_unathorised(aio_client):

    async with aio_client.get(
        f'/profile/me',
        # headers={'Token': token}
    ) as response:
        resp_data = await response.json()
        assert resp_data['error'] == 'Token is not provided'

    async with aio_client.get(
        f'/profile/me',
        headers={'Token': 'dummy_token'}
    ) as response:
        resp_data = await response.json()
        assert resp_data['error'] == 'Token is expired, or invalid'


async def test_users_by_name(aio_client, pg_connection):
    email, password = 'test3@example.com', 'password'
    await pg_connection.execute(
        "INSERT INTO users(name, email) VALUES ('user1', 'test1@example.com')"
    )
    await pg_connection.execute(
        "INSERT INTO users(name, email) VALUES ('user2', 'test2@example.com')"
    )
    await pg_connection.execute(
        "INSERT INTO users(name, email, password)"
        " VALUES ('user23', 'test3@example.com', 'password')"
    )

    async with aio_client.post(
        '/auth/login',
        json={
            'password': password,
            'email': email
        }
    ) as response:
        data = await response.json()
        assert 'token' in data
        token = data['token']

    async with aio_client.get(
        f'/users',
        params={'name': 'user2'},
        headers={'Token': token}
    ) as response:
        resp_data = await response.json()
        assert len(resp_data['users']) == 2
        val_set = set(['user2', 'user23'])
        assert all(u['name'] in val_set for u in resp_data['users'])
