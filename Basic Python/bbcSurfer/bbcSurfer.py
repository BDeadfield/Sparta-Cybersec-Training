import requests

request_bbc = requests.get("https://www.bbc.co.uk")

# Prints BBC.co.uk status code

print(request_bbc.status_code)
input()

# Prints BBC.co.uk content

print(request_bbc.content)
