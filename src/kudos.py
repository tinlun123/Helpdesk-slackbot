from listener import Listener 

class Kudos:
    def __init__(self, client):
        self.client = client
        Listener.register(self.on_message, "on_message")
        pass

    def on_message(self, ctx):
        pass
