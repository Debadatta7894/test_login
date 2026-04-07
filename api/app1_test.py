import requests

#get response post
'''base_url = "http://127.0.0.1:5000/api/users"

response = requests.get(base_url)

assert response.status_code == 200,f'Api Failed:- {response.status_code}'
data = response.json()

for i in data:
    print(i)'''

#token fetch -post of login

base_url = "http://127.0.0.1:5000/api/login"

payload = {"email":"bn@gmail.com","password":"Password@123"}
response = requests.post(base_url,json=payload)

assert response.status_code == 200,f'Api Failed:- {response.status_code}'

data = response.json()
for key,value in data.items():
    if key == "access_token":
        print(value)