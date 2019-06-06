from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from chatbot import get_response


class ChatServer(WebSocket):

    def handleMessage(self):
        message = self.data
        response = get_response(message)
        print(response)
        self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')


server = SimpleWebSocketServer('localhost', 3000, ChatServer)
print("server connected")
server.serveforever()
