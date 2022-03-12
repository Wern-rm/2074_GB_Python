import re


def parse_log(str_info: str) -> list:
    request_data = re.compile(r'(?P<addr>(?:\d{1,3}\.){3}\d{1,3})\s-\s-\s\['
                              r'(?P<date>\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}\s+[+]\d{4})\]\s"'
                              r'(?P<request_type>\w+)\s(?P<requested_resource>/\w+/\w+_\d{1})\sHTTP/1.1" '
                              r'(?P<response_code>\d{3})\s(?P<response_size>\d+)\s"-"')
    return request_data.findall(str_info)


if __name__ == '__main__':
    with open('nginx.log', 'r', encoding='utf-8') as fr:
        for line in fr:
            print(*parse_log(line))