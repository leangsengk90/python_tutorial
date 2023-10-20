import requests


url = "http://localhost:8200/v1/kv_test/data/test/file"
headers = {
    "X-Vault-Token": "hvs.t0TaY7ytqXPWsy0OQXuJChWM",
    "accept": "application/json",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Process the retrieved data
    print(data.data)
else:
    print("Request failed with status code:", response.status_code)
