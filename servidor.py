import http.server
import socketserver
import os

# Configurações do servidor
PORT = 8000
DIRECTORY = "/home/rap/alcateia/bond_dos_vilão"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def run_server():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Servidor rodando em http://localhost:{PORT}")
        print("Pressione Ctrl+C para encerrar")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor encerrado")

if __name__ == "__main__":
    run_server()