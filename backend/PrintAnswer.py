from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse
from urllib.request import urlopen

ask_server_port = 12345


class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        query = urlparse(self.path).query
        query_components = dict({'text':None})

        if query != '':
            query_components = dict(qc.split("=") for qc in query.split("&"))

        if 'text' in query_components.keys():
            answer = query_components['text'] + ' ' + query_components['text']

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(answer.encode())


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('', 12346)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()


print('Ready to answer')
run(handler_class=HttpGetHandler)