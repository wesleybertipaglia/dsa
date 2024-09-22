# platform: HackerRank
# kit: Week Preparation Kit
# title: Time Conversion
# url: https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/

# description:
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def time_conversion(s):
    hour = int(s[:2])
    minute_second = s[2:8]
    time_format = s[-2:]

    if time_format == "PM":
        if hour != 12:
            hour += 12
    else:
        if hour == 12:
            hour = 0   
    
    return f"{hour:02}{minute_second}"