import requests


endpoint = "http://localhost:8000/api/products/1/update/" 

data ={
    "title" : "Hello Updated World",
    "price" : 11.1
}
get_response = requests.put(endpoint, json=data)
# print(get_response.status_code)
print(get_response.json())