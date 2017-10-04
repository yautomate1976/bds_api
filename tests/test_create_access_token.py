import requests

url = "https://us-rqa3.api.concursolutions.com/oauth2/v0/token"

querystring = {"client_id":"ca97e0ca-82c4-415e-baca-72298730a09a","client_secret":"hush hush","grant_type":"password","username":"mlore@outtask.com","password":"outtask","scope":"user.read"}

headers = {
    'concur-correlationid': "1234567",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "29dc9805-e9fc-28e4-834f-98e22593f049"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.status_code)
print(response.text)