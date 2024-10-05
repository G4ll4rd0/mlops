'''Demo for API'''
import requests


def test_api_request(data: list[float]) -> dict[str, int]:
    response = requests.post('http://127.0.0.1:1234/predict', json=data, timeout = 30)
    # print(response)

    prediction = response.json()

    return prediction

if __name__ == "__main__":
    data = list(range(23))
    test_api_request(data)
