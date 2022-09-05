from urllib import response
import requests
url = 'http://127.0.0.1:8000/card/'
headers =  {'Authorization': 'Token f533fc9f84810f4df662f2f3c67ee7a54af2b80a'}
response = requests.get(url,headers = headers)

print(response)
print(response.text)