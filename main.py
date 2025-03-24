import requests


response = requests.get("https://petstore.swagger.io/v2/pet/1")

print(response.status_code)
print(response.text)

print("1___________")

url = 'https://petstore.swagger.io/v2/pet'
data =  {
    "id": 26790,
    "category": {
        "id": 1,
        "name": "string"
    },
    "name": "Lilcat",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 1,
            "name": "string"
        }
    ],
    "status": "available"
}
response = requests.post(url, json=data)
print(response.status_code)
print(response.text)

print("___________")

response = requests.get('https://petstore.swagger.io/v2/pet/26790')

print(response.status_code)
print(response.text)


