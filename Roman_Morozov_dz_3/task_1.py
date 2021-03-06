'''
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
#>>> num_translate("one")
"один"
#>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
'''

numerals_eng = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
numerals_rus = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
numerals_dict = dict(zip(numerals_eng, numerals_rus))


def num_translate(key):
    print(numerals_dict.get(key))


if __name__ == '__main__':
    for i in numerals_eng:
        num_translate(key=i)