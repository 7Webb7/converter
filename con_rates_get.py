import requests
from datetime import datetime, timedelta
from api_key import exchange_rate_api_key
def get_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data

def get_historical_data(currency):
    end_date = datetime.now()
    start_date = end_date - timedelta(days = 30)
    year = start_date.strftime('%Y')
    month = start_date.strftime('%m')
    day = start_date.strftime('%d')
    url = f"https://v6.exchangerate-api.com/v6/{exchange_rate_api_key}/history/USD/{year}/{month}/{day}"
    #Этот api - платный, ищу альтернативу

    response = requests.get(url)

    if response == None:
        return "Error"
    data = response.json()

    return data

#Функция построения графика
#def build_graph():


conversion_rates = get_rates()
usd = conversion_rates['rates']['USD']
