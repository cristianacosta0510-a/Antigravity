import http.server
import socketserver
import threading
import subprocess
import time

PORT = 8080
DIRECTORY = r"c:\Recorrido II VR"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Wait for server to start
    time.sleep(2)
    
    # Run Edge
    edge_cmd = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "--headless",
        "--disable-gpu",
        "--print-to-pdf=C:\\Users\\Dell 5490\\Downloads\\CAcosta_U3_Act2_Curriculum_Vitae.pdf",
        "http://localhost:8080/cv_template.html"
    ]
    
    print("Running Edge...")
    subprocess.run(edge_cmd)
    print("Edge finished PDF generation.")
    
    httpd.shutdown()
    print("Server shut down.")
