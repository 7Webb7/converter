import requests

def get_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data

conversion_rates = get_rates()
usd = conversion_rates['rates']['USD']
print(usd)
print(conversion_rates['rates'].keys())