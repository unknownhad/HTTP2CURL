import os
import unittest
from urllib.parse import quote

def http_to_curl(http_request: str) -> str:
    # Split the HTTP request into lines
    lines = http_request.strip().split('\n')

    # Extract the request method and URL
    request_line = lines[0]
    request_method, request_url, _ = request_line.split()

    # Encode the URL
    request_url = quote(request_url, safe="%/:=&?~#+!$,;'@()*[]")

    # Initialize the cURL command
    curl_command = f"curl -X {request_method}"

    # Add the URL to the cURL command
    curl_command += f" '{request_url}'"

    # Iterate through the remaining lines in the HTTP request
    for line in lines[1:]:
        # Split the line into key/value pairs
        key, value = map(str.strip, line.split(':', 1))

        # Add the key/value pair to the cURL command as a header
        curl_command += f" -H '{key}: {value}'"

    return curl_command


class TestHTTPToCURL(unittest.TestCase):
    def test_http_to_curl(self):
        # Test a simple HTTP request with no special characters
        http_request = """\
POST /api/users HTTP/1.1
Content-Type: application/json
User-Agent: curl/7.68.0
Accept: */*
Content-Length: 26

{"name": "Alice", "age": 30}"""
        expected_curl_command = """\
curl -X POST -H 'Content-Type: application/json' -H 'User-Agent: curl/7.68.0' -H 'Accept: */*' -H 'Content-Length: 26' 'http://example.com/api/users'"""
        self.assertEqual(http_to_curl(http_request), expected_curl_command)

        # Test an HTTP request with special characters in the URL
        http_request = """\
POST /api/users?id=' OR 1=1 HTTP/1.1
Content-Type: application/json
User-Agent: curl/7.68.0
Accept: */*
Content-Length: 26

{"name": "Alice", "age": 30}"""
        expected_curl_command = """\
curl -X POST -H 'Content-Type: application/json' -H 'User-Agent: curl/7.68.0' -H 'Accept: */*' -H 'Content-Length: 26' 'http://example.com/api/users?id=%27%20OR%201%3D1'"""
        self.assertEqual(http_to_curl(http_request), expected_curl_command)

        # Test an HTTP request with a ' character in the User-Agent header
        http_request = """\
POST /api/users HTTP/1.1
Content-Type: application/json
User-Agent: curl/7.
