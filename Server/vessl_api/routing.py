from channels import route

from vesslserver.vessl_api import VESSL_API_Consumer

channel_routing = [
	route('websocket.connect', VESSL_API_Consumer.connect),
	route('websocket.disconnect', VESSL_API_Consumer.disconnect),
	route('websocket.receive_json', VESSL_API_Consumer.receive_json),
]