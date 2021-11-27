from . import login
from . import profile
from . import register
from . import users

ROUTES = [
    login.routes,
    profile.routes,
    register.routes,
    users.routes
]
