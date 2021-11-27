from aiohttp import web

from .views import ROUTES
from .model import pg_engine
from .auth import redis_cache

def init_app():
    app = web.Application(middlewares=[])

    for router in ROUTES:
        app.add_routes(router)

    return app
