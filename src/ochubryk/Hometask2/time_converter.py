# exercise from https://py.checkio.org/
# Your task is to convert the time from the 24-h format into 12-h format
# by following the next rules:
# - the output format should be 'hh:mm a.m.' (for hours before midday)
# or 'hh:mm p.m.' (for hours after midday)
# - if hours is less than 10 - don't write
# a '0' before it. For example: '9:05 a.m.'


def time_converter(time):
    hours, minutes = [int(i) for i in time.split(':')]
    period = ''

    if hours == 0:
        hours = 12
        period = 'a.m.'
    elif hours == 12:
        period = 'p.m.'
    elif hours < 12:
        period = 'a.m.'
    elif hours > 12:
        hours = hours - 12
        period = 'p.m.'

    return "{}:{:02d} {}".format(hours, minutes, period)


if __name__ == '__main__':
    print("Example:")
    print(time_converter('00:00'))

    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
