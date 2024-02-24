import os
import json
import time

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
            #print('Key:', key)
            #print('Value:', r.get(key))
            j.append(str(r.get(key)))
        self.wfile.write(json.dumps(j).encode('utf-8'))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.wfile.write(post_data.encode('utf-8'))
        k = str(round(time.time() * 1000))
        r.set(k, post_data)
        return
