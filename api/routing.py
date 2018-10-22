from channels.routing import ProtocolTypeRouter
from api import consumers

application = ProtocolTypeRouter({
    'websocket': consumers.ApplicationConsumer,
})
