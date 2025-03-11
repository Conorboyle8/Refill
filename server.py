import json
import mysql.connector
from http.server import BaseHTTPRequestHandler, HTTPServer

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sarah1808!",  # Replace with your MySQL password
    database="refill_db"
)

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/users":
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            cursor.close()

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")  # Allow frontend to fetch
            self.end_headers()
            self.wfile.write(json.dumps(users).encode())

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

# Start Server
server_address = ("", 5000)
httpd = HTTPServer(server_address, MyHandler)
print("Server running on http://localhost:5000")
httpd.serve_forever()
