import requests

def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'][to_currency]
    return rate

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    rate = get_exchange_rate(from_currency.upper(), to_currency.upper())
    return amount * rate
