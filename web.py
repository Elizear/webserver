import http.server
from prometheus_client import start_http_server
from prometheus_client import Counter

REQUESTS = Counter('server_requests', 'Total number of requests to this webserver')

class ServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'KOCSISTEM')
if __name__ == "__main__":
    server = http.server.HTTPServer(('', 8080), ServerHandler)
    server.serve_forever()
