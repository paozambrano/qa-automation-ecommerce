import requests
from jsonschema import validate

BASE = 'https://fakestoreapi.com'

def test_get_products():
    req = requests.get(f'{BASE}/products')
    assert req.status_code == 200
    data = req.json()
    assert isinstance (data, list)

def test_product_schema():
    req = requests.get(f'{BASE}/products/1')
    schema = {
        'type':'object',
        'properties':{
            'id': {'type': 'number'},
            'title': {'type': 'string'},
            'price': {'type': ['number','string']},
        },
        'required': ['id', 'title', 'price']
    }
    validate(instance=req.json(), schema=schema)