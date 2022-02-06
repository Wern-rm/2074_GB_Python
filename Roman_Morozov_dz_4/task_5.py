import utils
from datetime import date
import sys

kurs, date_value = utils.currency_rates_adv(sys.argv[1])

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)
