import requests


endpoint = "http://localhost:8000/api/products/" 
get_response = requests.post(endpoint, json={"title":"This field is done", "price":3.49})
print(get_response.json())