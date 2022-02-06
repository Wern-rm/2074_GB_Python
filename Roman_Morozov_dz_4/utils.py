from datetime import datetime

from requests import get


def currency_rates_adv(code: str):
    """возвращает курс валюты `code` по отношению к рублю"""
    response = get('https://www.cbr.ru/scripts/XML_daily.asp')
    data = response.text
    result_date = datetime.strptime(data[data.find('Date=') + 6:data.find('" name=')], "%d.%m.%Y").date()

    if code.upper() not in data:
        result_value = None
    else:
        nominal_value = data[data.find(code.upper()):].split('<Nominal>')[1].split('</Nominal>')[0]
        value = data[data.find(code.upper()):].split('<Value>')[1].split('</Value>')[0]
        result_value = float(value.replace(',', '.')) / int(nominal_value)
    return result_value, result_date