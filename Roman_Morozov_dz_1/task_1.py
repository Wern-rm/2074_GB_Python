__author__ = 'Roman Morozov'


def convert_time(duration: int) -> str:
    """
    Converting time in seconds
    :param duration:
    :return:
    """
    if duration < 60:
        return f'{duration} сек'
    elif 60 <= duration < 3600:
        return f'{duration // 60} мин {duration % 60} сек'
    elif 3600 <= duration < 86400:
        hours = duration // 3600
        minutes = (duration - (3600 * hours)) // 60
        seconds = (duration - (3600 * hours)) - (60 * minutes)
        return f'{hours} час {minutes} мин {seconds} сек'
    else:
        days = duration // 86400
        hours = (duration - (86400 * days)) // 3600
        minutes = ((duration - (86400 * days)) - (3600 * hours)) // 60
        seconds = (duration - (86400 * days)) - (3600 * hours) - (60 * minutes)
        return f'{days} дней {hours} час {minutes} мин {seconds} сек'


if __name__ == '__main__':
    for i in [53, 153, 4153, 400153]:
        print(convert_time(duration=i))