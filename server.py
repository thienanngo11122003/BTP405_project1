import http.server
import json
import mysql.connector
import cgi
import hashlib

# Establish connection to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Thienandeptrai123',
    port = 3306,
    database='thienan'
)
cursor = conn.cursor()

# Create users table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password_hashed VARCHAR(50) NOT NULL
    )
""")

# Create notes table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        note_id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        content TEXT NOT NULL
    )
""")

class PHRServer(http.server.BaseHTTPRequestHandler):
    def _set_response(self, content_type='application/json'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/notes':
            cursor.execute("SELECT * FROM notes")
            notes = cursor.fetchall()
            self._set_response()
            self.wfile.write(json.dumps(notes).encode())
        else:
            self._set_response()
            response = {
                'message': 'Welcome to Personal Health Record (PHR) system',
                'endpoints': [
                    {'login': 'Login endpoint'},
                    {'signup': 'Signup endpoint'},
                    {'notes': 'Get health notes'}
                ]
            }
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == '/notes':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_note = json.loads(post_data.decode())
            cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (new_note['title'], new_note['content']))
            conn.commit()
            self._set_response()
            self.wfile.write(json.dumps(new_note).encode())
        elif self.path == '/login':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            content_len = int(self.headers.get('content-length'))
            pdict['content-length'] = content_len

            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                username = fields.get('username')[0]
                password = fields.get('password')[0]
                password_hashed = hashlib.sha256(password.encode()).hexdigest()
                cursor.execute("SELECT * FROM users WHERE username = %s AND password_hashed = %s", (username, password_hashed))

                if cursor.fetchall():
                    self.send_response(301)
                    self.send_header('content-type', 'application/json')
                    self.send_header('Location', "/notes")
                    self.end_headers()
                else:
                    self.send_response(401)
                    self.send_header('content-type', 'application/json')
                    self.end_headers()
        elif self.path == '/signup':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            content_len = int(self.headers.get('content-length'))
            pdict['content-length'] = content_len

            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                username = fields.get('username')[0]
                password = fields.get('password')[0]
                password_hashed = hashlib.sha256(password.encode()).hexdigest()
                cursor.execute("INSERT INTO users (username, password_hashed) VALUES (%s, %s)", (username, password_hashed))
                conn.commit()

                self.send_response(301)
                self.send_header('content-type', 'application/json')
                self.send_header('Location', '/login')
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, PHRServer)
    print('Starting server...')
    httpd.serve_forever()

# Close database connection
cursor.close()
conn.close()
