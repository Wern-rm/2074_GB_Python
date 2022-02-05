'''
*(вместо задачи 1) Перепишите функцию из задания 1 изменив название на num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
'''

numerals_eng = ['One', 'Two', 'Three', 'Four', 'Five', 'six', 'seven', 'eight', 'nine', 'ten']
numerals_rus = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
numerals_dict = dict(zip(numerals_eng, numerals_rus))


def num_translate_adv(key):
    if key[:1].isupper():
        print(str(numerals_dict.get(key)).title())
    else:
        print(numerals_dict.get(key))


if __name__ == '__main__':
    for i in numerals_eng:
        num_translate_adv(key=i)