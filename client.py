import requests


def create_user():
    response = requests.post('http://127.0.0.1:8082/user', json={'username': 'kirill2', 'password': '1234', 'name': 'kirill2'})
    print(response.text)
    data = response.json()
    print(data)

def get_user():
    response = requests.get('http://127.0.0.1:8082/user/1')
    print(response.text)


def get_users():
    response = requests.get('http://127.0.0.1:8082/users')
    print(response.text)


get_user()