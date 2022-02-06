import utils
from datetime import date

kurs, date_value = utils.currency_rates_adv("BYN")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)

'''
потыкала разные варианты:
/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 /Users/wern/Documents/GB_Python/Roman_Morozov_dz_4/task_4.py
87.1163 2022-02-05

/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 /Users/wern/Documents/GB_Python/Roman_Morozov_dz_4/task_4.py
76.0509 2022-02-05

/Library/Frameworks/Python.framework/Versions/3.10/bin/python3 /Users/wern/Documents/GB_Python/Roman_Morozov_dz_4/task_4.py
29.5194 2022-02-05
'''