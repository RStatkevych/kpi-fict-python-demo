from aiohttp import web

import asyncio
from .app import init_app

app = init_app()

web.run_app(app)
