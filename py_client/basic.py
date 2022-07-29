import requests

endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" # "http://127.0.0.1:8000/"

# get_response = requests.get(endpoint)
# print(get_response.text)

get_response = requests.post(endpoint, json={"title":"Hello World, again later"})  #, json={"query": "Hello World"})
# get_response = requests.get(endpoint, params={"abc":123}, json={"query": "Hello World"})
# print(get_response.json()) # see content type and check for data instead of json in request
# print(get_response.text)
print(get_response.status_code)
print(get_response.json())