import requests

# endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api"

get_response = requests.get(endpoint, params={"abs": 123}, json={"query": "Hello discord mates"})


# print(get_response.text)
print(get_response.json() ["message"])
# print(get_response.status_code)