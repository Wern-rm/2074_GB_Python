import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(?!.*([-._])\1)^[^_.-][a-zA-Z0-9_.-]{3,}[^_.-]@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]{2,})+$')

    dict_address = {}
    if not RE_MAIL.match(email):
        raise ValueError(f'wrong email: {email}')
    else:
        dict_address['username'], dict_address['domain'] = email.split('@')
    return dict_address


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print('-----')
    print(email_parse('someone@geekbrainsru'))