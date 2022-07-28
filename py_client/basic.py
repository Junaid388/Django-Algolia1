import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

# get_response = requests.get(endpoint)
# print(get_response.text)

get_response = requests.get(endpoint, json = {"query": "Hello World"})
print(get_response.json()) # see content type and check for data instead of json in request