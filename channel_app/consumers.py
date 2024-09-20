from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        self.send({
            'type': 'websocket.accept',
        })
       
    def websocket_receive(self, event):
        message = event['text']
        self.send({
            'type': 'websocket.send',
            'text': f'You said: {message}',
        })
    
    def websocket_disconnect(self, event):
        self.send({
            'type': 'websocket.close',
        })