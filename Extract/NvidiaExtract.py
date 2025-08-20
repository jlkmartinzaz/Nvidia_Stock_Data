import requests

URL="https://ipinfo.io/190.60.194.114/json"
try:
    response = requests.get(URL)
    data= response.json()
    print(data)

except:
    print("Hubo un error")
    