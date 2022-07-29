from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product
# Create your views here.

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    
    return JsonResponse(data)

def api_home_old(request, *args, **kwargs):
    # request  -> HttpRequest  -> Django
    # request.body
    # print(request.GET)
    # print(request.POST)
    body = request.body # byte string of JSON data
    # print(body)
    data = {}
    try:
        data = json.loads(body)  # string of Json data -> Python Dict
    except:
        pass
    # print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)