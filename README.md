# HTTP2CURL
This python code converts raw HTTP to Curl request

#Added 2 files both does the exact same thing, one is just the function another one accepts .HTTP files and conver it to cURL

# Example usage
http_request = """\
POST /api/users HTTP/1.1
Content-Type: application/json
User-Agent: curl/7.68.0'
Accept: */*
Content-Length: 26

{"name": "Alice", "age": 30}"""
print(http_to_curl(http_request))


curl -X POST -H 'Content-Type: application/json' -H 'User-Agent: curl/7.68.0%27' -H 'Accept: */*' -H 'Content-Length: 26' 'http://example.com/api/users'


#Known issues 
Directory treversal attack are normalized by curl, right now please manually add `--path-as-is` flag to send it.

#Feel free to raise bug if something is incorrect


