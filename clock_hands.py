"""
Create a function called "find_smallest_angle" (snake-case) that,
 when given a time, will return the smallest angle of the clock's hands.
 Save the file as "clock_hands.py"

 The input is a string with hours, a colon, and minutes


 The output is a float of the smallest angle of the hands

 12-hour time

 BONUS: return None on invalid input
"""


def find_smallest_angle(clock: str) -> float or None:
    try:
        [hours, minutes] = map(int, clock.split(":"))
    except AttributeError:
        return
    except ValueError:
        return
    if hours > 12 or hours < 1 or minutes > 60 or minutes < 0:
        return
    hours += minutes / 60  # Add fractional hour to hours
    hours_angle = hours * 30  # 360/12 = 30 degrees/hour
    minutes_angle = minutes * 6  # 360/60 = 6 degrees/minute
    smallest_angle = abs(hours_angle - minutes_angle)
    return smallest_angle if smallest_angle < 180 else 360 - smallest_angle
