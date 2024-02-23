from vercel_kv import KV

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        kv = KV()
        self.wfile.write(kv.has_auth())
        self.wfile.write(kv.set(key="sss", value="asasd"))
        self.wfile.write(kv.get("sss"))        
        return
