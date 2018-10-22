from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync

class ApplicationConsumer(JsonWebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'events',
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print("Closed websocket with code: ", close_code)
        async_to_sync(self.channel_layer.group_discard)(
            'events',
            self.channel_name
        )
        self.close()

    def receive_json(self, event):
        print("Received event: {}".format(event))
        self.send_json(event)

    # ------------------------------------------------------------------------------------------------------------------
    # Handler definitions! handlers will accept their corresponding message types. A message with type event.alarm
    # has to have a function event_alarm
    # ------------------------------------------------------------------------------------------------------------------

    def events_alarm(self, event):
        self.send_json(
            {
                'type': 'events.alarm',
                'content': event['content']
            }
        )
