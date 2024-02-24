import os
import json
import time
from datetime import datetime

import redis        

r = redis.from_url(os.getenv("KV_URL").replace('redis://', 'rediss://'))

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()    

    def do_GET(self):
        self._set_headers()
        #self.wfile.write('Hello, world!'.encode('utf-8'))
        j = [] 
        keys = r.keys()
        for key in keys:
            v = r.get(key).decode('utf-8')
            if len(v) > 0:
                self.wfile.write('V: '+v.encode('utf-8'))
                j.append(json.loads(v))
        self.wfile.write(json.dumps(j).encode('utf-8'))
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        j = json.loads(post_data)
        j["date"] = datetime.now().strftime("%Y-%m-%d/%H:%M")
        k = str(round(time.time() * 1000))
        r.set(k, json.dumps(j))
        self._set_headers()
        self.wfile.write(json.dumps(j).encode('utf-8')) 
        if r.exists(k):
            self.wfile.write(json.dumps({"response":"success"}).encode('utf-8'))        
        else:
            self.wfile.write(json.dumps({"response":"error"}).encode('utf-8'))        
        return
