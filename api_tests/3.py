
import hashlib
import requests
email = 'test2@gmail.com'
password = '123'
# password_hash = hashlib.sha256(password.encode()).hexdigest()
# print(email,password_hash)
api_url = 'https://abidali1999063.pythonanywhere.com/login_api'  # Replace with your actual API URL
data = {
'email': email,
'password': password
}
response = requests.post(api_url, json=data)

print(response.text)
print(response.status_code)