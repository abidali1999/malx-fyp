import requests,hashlib


api_url = 'https://abidali1999063.pythonanywhere.com/signup_api'  # Replace with your actual API URL
ps='123'
password_hash = hashlib.sha256(ps.encode()).hexdigest()
data = {
    'name': 'test',
    'email': 'test2@gmail.com',
    'password': password_hash,
    'phone': '123'
}
response = requests.post(api_url, data=data)
print(response.text)
print(response.status_code)