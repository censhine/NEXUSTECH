#!/usr/bin/env python3
"""
NEXUS TECH - Cross-border E-Commerce Local Development Server
"""

import http.server
import socketserver
import os
import sys

DEFAULT_PORT = 8080

class NexusHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and caching headers for local testing
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def run_server(port=DEFAULT_PORT):
    # Ensure working directory is the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    handler = NexusHTTPRequestHandler
    
    # Try preferred port, fallback to next ports if occupied
    current_port = port
    max_tries = 10
    httpd = None

    for i in range(max_tries):
        try:
            httpd = socketserver.TCPServer(("", current_port), handler)
            break
        except OSError:
            print(f"Port {current_port} is busy, trying {current_port + 1}...")
            current_port += 1

    if not httpd:
        print("Error: Could not bind to any free port.")
        sys.exit(1)

    print("=" * 60)
    print("🚀 NEXUS TECH Bilingual Store Server Running")
    print(f"📡 Local URL:    http://localhost:{current_port}")
    print(f"📡 Network URL:  http://127.0.0.1:{current_port}")
    print(f"📂 Serving Root: {script_dir}")
    print("=" * 60)
    print("Press Ctrl+C to terminate the server.\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()
        print("Server stopped cleanly.")

if __name__ == '__main__':
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run_server(port)
