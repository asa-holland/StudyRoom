# Code taken from HowCode.org: https://github.com/howCodeORG/Simple-Python-Web-Server
# Comments added for clarity

# Imports the built in http library to create the server and handle HTTP requests
from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
    """
    Class that holds our server (inherits from BaseHTTPRequestHandler)
    """

    def do_GET(self):
        """
        This function runs whenever we send a Get request to a webpage.
        Anytime we are entering a website into a browser and hitting enter, we are sending a Get request to a server.

        :return:
        """

        # First, check if the path provided by the user is a forward slash.
        # If it does, that means the user is attempting to access the index page and that is where we should send them.
        if self.path == '/':
            self.path = '/index.html'

        # Next, try to read the file that the user is attempting to access.
        # If the user attempts to access a legal page that is added to our server,
        # Read the file and load it for the user.
        # return the code 200 (the generic code for a successful HTTP request.)
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)

        # If the user has entered an invalid link (any link not associated with our server) return the 404 code.
        # 404 is the generic code for an unsuccessful HTTP request.
        # This will also display the text "File not found" to the user.
        except:
            file_to_open = "File not found"
            self.send_response(404)

        # End the headers (this is required by the BaseHTTPRequestHandler class)
        # Convert the file from utf-8 to bytes using the bytes method (allows the server to read the files sent)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


# create a HTTP variable (HTTPD for HTTP Demon, a term for a program that runs in the background - a web server)
# Set to address to host the server on, and the port, and the serv class.
httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
