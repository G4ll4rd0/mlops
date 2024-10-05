import requests

data = list(range(23))

response = requests.post('http://127.0.0.1:1234/predict', json=data)
print(response)

prediction = response.json()['prediction']

print(prediction)