import http.server
import os

class CustomHTTPServer(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        ctype = self.guess_type(path)
        try:
            if not os.path.exists(path):
                self.send_error(http.server.HTTPStatus.NOT_FOUND, "File not found")
                return None
            f = open(path, 'rb')
        except OSError:
            self.send_error(http.server.HTTPStatus.NOT_FOUND, "File not found")
            return None
        self.send_response(http.server.HTTPStatus.OK)
        self.send_header("Content-type", ctype)
        self.send_header("Content-Length", str(os.path.getsize(path)))
        self.end_headers()
        return f

if __name__ == "__main__":
    PORT = 8888
    os.chdir('public')
    server_address = ("", PORT)
    httpd = http.server.HTTPServer(server_address, CustomHTTPServer)
    print(f"Serving HTTP on port {PORT} (http://localhost:{PORT}/) ...")
    httpd.serve_forever()

