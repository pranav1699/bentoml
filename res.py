import requests
data =requests.post(
    "http://127.0.0.1:5000/classify",
    headers={"content-type": "application/json"},
    data="[5,4,3,2]").text

print(data)