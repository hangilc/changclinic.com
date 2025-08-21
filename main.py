import http.server
import socketserver
import os

def main():
    PORT = 8000
    DIRECTORY = "docs"
    
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
