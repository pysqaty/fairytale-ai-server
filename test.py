import requests

# response = requests.post("http://localhost:8000/api/v1/accounts/", json={"email": "test@test.com", "password": "test"})
# print(response.json())

# GET
response = requests.get("http://0.0.0.0:8000/api/v1/accounts/")
print(response.json())

# DELETE
# response = requests.delete("http://0.0.0.0:8000/api/v1/accounts/1/")
# print(response.json())
