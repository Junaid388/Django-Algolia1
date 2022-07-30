import requests


endpoint = "http://localhost:8000/api/products/1/" 
get_response = requests.get(endpoint, json={"title":"Hello World, again later"})
print(get_response.status_code)
print(get_response.json())