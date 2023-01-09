import os
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

# Read all the files with the .http extension in the /httpfiles directory
for filename in os.listdir('/httpfiles'):
    if filename.endswith('.http'):
        # Read the contents of the file
        with open(os.path.join('/httpfiles', filename), 'r') as f:
            http_request = f.read()

        # Convert the HTTP request to a cURL command
        curl_command = http_to_curl(http_request)

        # Print the cURL command
        print(curl_command)
