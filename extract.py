import requests
def extract_products():
    url = "https://fakestoreapi.com/products" #api link
    response = requests.get(url)
    return response.json()