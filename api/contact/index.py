
import os
import json
import time

import redis

r = redis.from_url(os.getenv("KV_URL").replace('redis://', 'rediss://'))

def json_loads_safe(data):
    try:
        return json.loads(data)
    except (ValueError, TypeError):
        return None

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def dump_data(self):
        j = []
        keys = r.keys()
        for key in keys:
            v = r.get(key).decode('utf-8')
            v = json_loads_safe(v)
            if v:
                j.append(v)
        self.wfile.write(json.dumps(j).encode('utf-8'))

    def do_GET(self):
        self.set_headers()
        self.dump_data()
        return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        j = json.loads(post_data)
        k = str(round(time.time() * 1000))
        r.set(k, json.dumps(j))
        self.set_headers()
        self.dump_data()
        return
