#! /usr/bin/python
# generate server.xml with the following command:
#    openssl req -new -x509 -keyout server.pem -out server.pem -days 365 -nodes
# run as follows:
#    python https.py
# then in your browser, visit:
#    https://localhost:4443

# curl -X POST --data "one two three four" localhost:8080/store.json
# curl -X POST --data "one two three four" https://localhost:4443/store.json -k

# curl -X GET localhost:8080/store.json    
# one two three four%


import ssl
from os import curdir
from os.path import join as pjoin

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class StoreHandler(BaseHTTPRequestHandler):
    store_path = pjoin(curdir, 'store.json')

    def do_GET(self):
        if self.path == '/store.json':
            with open(self.store_path) as fh:
                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.end_headers()
                self.wfile.write(fh.read().encode())

    def do_POST(self):
        if self.path == '/store.json':
            length = self.headers['content-length']
            data = self.rfile.read(int(length))

            with open(self.store_path, 'a') as fh:
                fh.write(data.decode())

            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.send_header('Content-type', 'application/json; charset=utf-8')
            self.send_response(200,"OK")
            self.end_headers()


server = HTTPServer(('localhost', 4443), StoreHandler)
server.socket = ssl.wrap_socket (server.socket, certfile='./server.pem', server_side=True)
server.serve_forever()
