# exercise from https://py.checkio.org/
# Your task is to find the angle of the sun
# above the horizon knowing the time of the day.
# Input data: the sun rises in the East at 6:00 AM,
# which corresponds to the angle of 0 degrees.
# At 12:00 PM the sun reaches its zenith, which
# means that the angle equals 90 degrees.
# 6:00 PM is the time of the sunset so the angle
# is 180 degrees. If the input will be the time of
# the night (before 6:00 AM or after 6:00 PM),
# your function should return - "I don't see the sun!".


def sun_angle(time):
    hours, minutes = [int(i) for i in time.split(':')]
    degreeInMinute = 0.25
    degrees = (hours * 60 + minutes) * degreeInMinute - 90
    if 0 <= degrees <= 180:
        time = degrees
    else:
        time = "I don't see the sun!"
    return time


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
