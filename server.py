from http.server import HTTPServer, BaseHTTPRequestHandler

class StaticServer(BaseHTTPRequestHandler):

    def do_GET(self):
        root = 'html'
        #print(self.path)
        if self.path == '/':
            filename = root + '/index.html'
        else:
            filename = root + self.path

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename) as fh:
            html = fh.read()
            html = bytes(html, 'utf8')
            self.wfile.write(html)

def run(server_class=HTTPServer, handler_class=StaticServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()

run()
