import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_clowns, get_all_completions, get_all_requests, create_clown, create_completion, create_requests, delete_clown, delete_completion, delete_request, get_single_clown, get_single_completion, get_single_request, update_clown, update_completion, update_request


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple
    
    def do_GET(self):
        
        response = {}  # Default response

        # Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)
        
        if resource == "completions":
                if id is not None:
                    self._set_headers(200)
                    response = get_single_completion(id)

                else:
                    self._set_headers(200)
                    response = get_all_completions()
        if resource == "clowns":
                if id is not None:
                    self._set_headers(200)
                    response = get_single_clown(id)

                else:
                    self._set_headers(200)
                    response = get_all_clowns()
        if resource == "requests":
                if id is not None:
                    self._set_headers(200)
                    response = get_single_request(id)

                else:
                    self._set_headers(200)
                    response = get_all_requests()

            
        self.wfile.write(json.dumps(response).encode())
        
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)
        
        new_completion = None
        new_clown = None
        new_request = None
        
        if resource == "completions":
            new_completion = create_completion()

            # Encode the new completion and send in response
            self.wfile.write(json.dumps(new_completion).encode())
        if resource == "clowns":
            new_clown = create_clown()

            # Encode the new completion and send in response
            self.wfile.write(json.dumps(new_clown).encode())
        if resource == "requests":
            new_request = create_requests()

            # Encode the new request and send in response
            self.wfile.write(json.dumps(new_request).encode())
            
    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "completions":
            delete_completion()
            
        if resource == "clowns":
            delete_clown()
            
        if resource == "requests":
            delete_request()
            
        # Encode the new animal and send in response
        self.wfile.write("".encode())
        
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "completions":
            update_completion()           
        if resource == "clowns":
            update_clown()           
        if resource == "requests":
            update_request()            

        # Encode the new animal and send in response
        self.wfile.write("".encode())
        
    def _set_headers(self, status):
        # Notice this Docstring also includes information about the arguments passed to the function
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()
        
# This function is not inside the class. It is the starting
# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """


HOST = ''
PORT = 8088
HTTPServer((HOST, PORT), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
