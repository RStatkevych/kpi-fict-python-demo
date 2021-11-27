from aiohttp import web

from .views import ROUTES
from .model import pg_engine, db_cursor
from .auth import redis_cache
from .errors import error_handler

def init_app():
    app = web.Application(middlewares=[db_cursor, error_handler,])

    for router in ROUTES:
        app.add_routes(router)

    app.cleanup_ctx.append(pg_engine)
    app.cleanup_ctx.append(redis_cache)
    return app
