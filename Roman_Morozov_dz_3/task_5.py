"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
"""

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count, repeat=True, **kwargs) -> list[str]:
    result: list[str] = []
    if repeat:
        for i in range(count):
            result.append(' '.join(random.choice(kwargs[j]) for j in kwargs.keys()))
    else:
        for i in range(count):
            noun, adverb, adjective = [random.choice(kwargs[j]) for j in kwargs.keys()]
            result.append(' '.join([noun, adverb, adjective]))
    return result


if __name__ == '__main__':
    print(get_jokes(count=1, repeat=True, nouns=nouns, adverbs=adverbs, adjectives=adjectives))
    print(get_jokes(count=3, repeat=False, nouns=nouns, adverbs=adverbs, adjectives=adjectives))
    print(get_jokes(count=5, repeat=True, nouns=nouns, adverbs=adverbs, adjectives=adjectives))