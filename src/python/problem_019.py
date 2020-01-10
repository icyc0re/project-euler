# months go from 0 to 11
# days go from 0 to 6, 0=monday

months_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_month_length(month, year):
    if month == 1 and is_leap_year(year):
        return 29
    return months_length[month]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def euler_019():
    # day1 is end of 1901
    day1 = sum([get_month_length(m, 1900) for m in range(12)]) % 7

    # start
    cnt = 0
    for year in range(1901, 2001):
        for month in range(12):
            if day1 == 6:
                cnt += 1
            day1 = (day1 + get_month_length(month, year)) % 7
    return cnt

if __name__ == '__main__':
    print(euler_019())
