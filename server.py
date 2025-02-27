import http.server
import socketserver
import webbrowser
import os

# Set the port
PORT = 8000

# Change directory to where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create the handler
Handler = http.server.SimpleHTTPRequestHandler

# Create the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server")
    
    # Open the browser automatically
    webbrowser.open(f"http://localhost:{PORT}")
    
    # Keep the server running
    httpd.serve_forever() 