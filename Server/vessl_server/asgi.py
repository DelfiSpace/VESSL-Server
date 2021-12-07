"""
ASGI config for vessl_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os, sys

# JOHAN Question: Why is SessionMiddlewareStack used, and not AuthMiddlewareStack, as 
#   in https://channels.readthedocs.io/en/stable/topics/routing.html ?
from channels.sessions import SessionMiddlewareStack
# Import ProtocolTypeRouter (the recommended default root router application)
# 	and URLRouter
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
from django.conf.urls import url


# The imports need this as it imports from a sibling directory
#from vesslserver.vessl_api import VESSL_API_Consumer
sys.path.append(os.path.abspath("../vessl_api"))
from vessl_api.vessl_api import VESSL_API_Consumer

# Setting the OS environment variable `DJANGO_SETTINGS_MODULE` to `vessl_server.settings`, 
#   so that Django knows where to look for the server settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vessl_server.settings')

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": get_asgi_application(),

    # Specifying that the VESSL_API_Consumer app uses websockets
    "websocket": SessionMiddlewareStack(
        URLRouter([
            url("api", VESSL_API_Consumer.as_asgi())
        ])
    )
})