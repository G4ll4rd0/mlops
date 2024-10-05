'''Demo for API'''
import requests

data = list(range(23))

response = requests.post('http://127.0.0.1:1234/predict', json=data, timeout = 30)
print(response)

prediction = response.json()

print(prediction)
