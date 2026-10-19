"""
N++ Embedded Development Web Server
Serves N++ web applications locally with zero dependencies and auto-browser launch.
"""

import http.server
import socketserver
import webbrowser
import threading
import os
import sys


class NppHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Format clean, modern access log
        sys.stderr.write(f"  [N++ Web] {self.address_string()} - {format % args}\n")


def serve_directory(directory: str, port: int = 8080, open_browser: bool = True):
    """Start local HTTP server serving files from directory."""
    os.chdir(directory)

    # Find available port if specified is taken
    handler = NppHTTPHandler
    server = None
    current_port = port

    while server is None and current_port < port + 50:
        try:
            server = socketserver.TCPServer(("", current_port), handler)
        except OSError:
            current_port += 1

    if server is None:
        print(f"Error: Could not bind to port {port} or next 50 ports.")
        return

    url = f"http://localhost:{current_port}"
    print(f"""
    ========================================================
                 N++ DEVELOPMENT WEB SERVER
    ========================================================
      Serving directory: {directory}
      Local URL:         {url}
      Press Ctrl+C to stop the server.
    ========================================================
    """)

    if open_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping N++ web server. Goodbye!")
        server.server_close()
