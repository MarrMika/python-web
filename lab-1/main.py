from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()

print("Set-cookie: name=value; expires=Wed Oct 12 11:59:00 2020; path=/cgi-bin/; httponly")

print("Content-type: text/html\n")
print("Cookies!!!")