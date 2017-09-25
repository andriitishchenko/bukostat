#! /usr/bin/python
from os import curdir
from os.path import join as pjoin

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urlparse, json
import cgi
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
            post_data = self.rfile.read(int(length))
            json_data = json.loads(post_data)
                        
            with open(self.store_path,'a') as fh:
                fh.write((json_data['date']+"\t"+
                    json_data['time']+"\t"+
                    json_data['temperature']+"\t"+
                    json_data['humidity']+"\t"+
                    json_data['atm_presh']+"\t"+
                    json_data['wind']+"\t"+
                    json_data['wind_direction']+"\t"+
                    json_data['descr']+"\n").encode('utf-8'))
            # length = self.headers['content-length']
            # post_data = self.rfile.read(int(length))
            # with open(self.store_path,'a') as fh:
            #     fh.write(post_data+"\n")
            
            self.send_response(200,"OK")
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.send_header('Content-type', 'application/json; charset=utf-8')            
            self.end_headers()


    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


server = HTTPServer(('', 8080), StoreHandler)
server.serve_forever()

# curl -X POST --data "one two three four" localhost:8080/store.json
# curl -X POST --data "one two three four" https://localhost:4443/store.json -k

# curl -X GET localhost:8080/store.json    
# one two three four%