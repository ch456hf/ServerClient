import SocketServer
import SimpleHTTPServer

HOST = '127.0.0.1'
PORT = 8000

server = SocketServer.TCPServer((HOST, PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

server.serve_forever()
