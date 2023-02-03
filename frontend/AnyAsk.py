from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from urllib.parse import urlparse
from urllib.request import urlopen

# Example of user's request
#   http://localhost:12345/?text=Oh!HiMark

answer_server_port = '12346'

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""

    def do_GET(self):
        query = urlparse(self.path).query
        query_components = dict({'text':None})

        if query != '':
            query_components = dict(qc.split("=") for qc in query.split("&"))
        
        self.send_response(200)

        if 'text' in query_components.keys():
            #Обработчик запроса пользователя

            with urlopen(f"http://backend:{answer_server_port}/?text={query_components['text']}") as response:
                #Обработчик ответа от второго сервиса

                result = response.read().decode()

                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write('<html><head><meta charset="utf-8">'.encode())
                self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
                self.wfile.write(f"<body>Вы ввели {query_components['text']}. <br>Ваш результат {result}</body></html>".encode())

        


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('', 12345)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()


print('Ready to listen')
run(handler_class=HttpGetHandler)