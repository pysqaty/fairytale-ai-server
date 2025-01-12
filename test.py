import requests
from pprint import pprint

def register_user():
    response = requests.post("http://localhost:8000/api/v1/accounts/auth/register/", json={
        "email": "test@test.com",
        "password": "testpassword"
    })
    pprint(response.json())
    return response.json()['refresh']


def login_user():
    response = requests.post("http://localhost:8000/api/v1/accounts/auth/login/", json={
        "email": "test@test.com",
        "password": "testpassword"
    })
    pprint(response.json())

def list_users(token):
    response = requests.get("http://localhost:8000/api/v1/accounts/", headers={
        "Authorization": f"Bearer {token}"
    })
    pprint(response.json())
    return response.json()

def delete_user(id, token):
    response = requests.delete(f"http://localhost:8000/api/v1/accounts/{id}/", headers={
        "Authorization": f"Bearer {token}"
    })
    pprint(response.status_code)

def refresh_token(refresh_token):
    response = requests.post("http://localhost:8000/api/v1/accounts/token/refresh/", json={
        "refresh": refresh_token
    })
    pprint(response.json())
    return response.json()['access']

if __name__ == "__main__":
    ref_token = register_user()
    print("")
    access_token = refresh_token(ref_token)
    print("")
    list_users("avx")
    print("")
    users = list_users(access_token)
    delete_user(users[0]['id'], access_token)
    print("")
    list_users(access_token)
