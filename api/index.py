import os
import json

import redis        

r = redis.from_url(os.getenv("KV_URL").replace('redis://', 'rediss://'))

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        #self.wfile.write('Hello, world!'.encode('utf-8'))
        j = [] 
        keys = r.keys()
        for key in keys:
            print('Key:', key)
            print('Value:', r.get(key))
            j.append(r.get(key))
        print(j)
        json.dumps(j)
        self.wfile.write(json.dumps(j).encode('utf-8'))
        return
