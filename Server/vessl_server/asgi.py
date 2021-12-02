"""
ASGI config for vessl_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os, sys

from channels.sessions import SessionMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application
from django.conf.urls import url

# The imports need this as it imports from a sibling directory
#from vesslserver.vessl_api import VESSL_API_Consumer
sys.path.append(os.path.abspath("../vessl_api"))
from vessl_api.vessl_api import VESSL_API_Consumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vessl_server.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": SessionMiddlewareStack(
        URLRouter([
            url("api", VESSL_API_Consumer.as_asgi())
        ])
    )
})