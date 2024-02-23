from vercel_kv import KV
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        kv = KV()
        self.wfile.write('<br>'.encode('utf-8'))
        self.wfile.write(str(kv.has_auth()).encode('utf-8'))
        self.wfile.write('<br>'.encode('utf-8'))
        self.wfile.write(str(kv.set(key="sss", value="asasd")).encode('utf-8'))
        self.wfile.write('<br>'.encode('utf-8'))
        self.wfile.write(str(kv.get("sss")).encode('utf-8'))        
        return
