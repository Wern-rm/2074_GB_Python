def get_dict_address(log: str) -> dict:
    dict_adr = {}
    with open(log, 'r', encoding='utf-8') as f:
        for line in f:
            key = line[:line.find(' - - ')]
            dict_adr[key] = dict_adr.get(key, 0) + 1
    return dict_adr


def find_spam(dict_address: dict) -> str:
    return max(dict_address, key=dict_address.get)


spam_address = find_spam(get_dict_address('nginx.log'))
print(spam_address)