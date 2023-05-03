import requests
import json
status = 'available'

resget = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
                       headers = {'accept': 'application/json'})

print(resget.status_code)
print(resget.text)
print(resget.json())
print(type(resget.json()))


headers = {'accept' : 'application/json', 'Content-Type' : 'application/json'}
data = {
  "id": 0,
  "username": "kosar",
  "firstName": "ko",
  "lastName": "sar",
  "email": "nenre@yandex.ru",
  "password": "127562",
  "phone": "88005550044",
  "userStatus": 0
}


respost = requests.post(f"https://petstore.swagger.io/v2/user",
                    headers = headers, data = json.dumps(data))
print(respost.status_code)
print(respost.json())

resput = requests.put(f'https://petstore.swagger.io/v2/user/kosar',
                    headers = headers, data = json.dumps(data))
print(resput.status_code)
print(resput.json())

resdelete = requests.delete(f'https://petstore.swagger.io/v2/user/kosar',
                            headers = headers, data = json.dumps(data))
print(resdelete.status_code)
print(resdelete.json())