from aiohttp import web
from ..model import DBController
from ..auth import AuthProvider


class BaseView(web.View):

    def __init__(self, *args, **kwargs):
        web.View.__init__(self, *args, **kwargs)
        self.db = DBController()
        self.auth = AuthProvider(self)
