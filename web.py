from wsgiref.simple_server import make_server

if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 8080, python)
    httpd.serve_forever()
