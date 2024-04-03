
import json

from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def set_headers(self, type):
        self.send_response(200)
        self.send_header('Content-type', type)
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        j = json.loads(post_data)
        url = j['url']
        if 'data' in j:
        data = json.dumps(j['data']).encode('utf-8')
        else:
        data = None
        if 'headers' in j:
        headers = j['headers']
        else:
        headers = {'User-Agent':'curl/8.5.0'}
        req = Request(url, data, headers)
        self.set_headers(urlopen(req).info()["content-type"])
        self.wfile.write(urlopen(req).read())
        return
