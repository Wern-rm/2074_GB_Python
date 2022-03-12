import sys

with open('bakery.csv', 'a+', encoding='utf-8') as fa:
    if float(sys.argv[1].replace(',', '.')) or int(sys.argv[1]):
        fa.write(f'{sys.argv[1].ljust(20)}\n')
