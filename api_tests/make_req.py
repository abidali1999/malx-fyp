import requests

api_url = 'https://abidali1999063.pythonanywhere.com/predict'
file_path = 'projekt_fyp\malxV2\signup.py'  # Replace with the path to your file
files = {'file': ('file.py', open(file_path, 'rb'))}

r = requests.post(api_url, files=files)
print(r.status_code)
print(r.text)

