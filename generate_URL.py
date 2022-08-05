def get_roundtype(num):
    if int(num) == 9:
        return '2'
    if int(num) == 18:
        return '1'
    else:
        return None

def get_course(c):
    if c == 'C':
        return '380'
    if c == 'B':
        return '361'
    if c == 'R':
        return '382'
    if c == 'W':
        return '381'
    else:
        return None

def get_URL(m, d, y, start_t, end_t, p, h, c):
    preamble = 'https://greatlife.clubautomation.com/golf/online-reservation?date='
    f1 = '%2F'
    f2 = '&startTimeRange%5B0%5D='
    f3 = '&startTimeRange%5B1%5D='
    f4 = '&playersNum='
    f5 = '&roundType='
    f6 = '&courses%5B%5D='
    month = m
    day = d
    year = str(y)
    start_time = str(start_t)
    end_time = str(end_t)
    player_count = str(p)
    holes = get_roundtype(h)
    course = get_course(c)
    return preamble + str(month) + f1 + str(day) + f1 + year + f2 + start_time + f3 + end_time + f4 + player_count + f5 + holes + f6 + course

# print(get_URL('08', 10, 2022, 8, 10, 4, 18, 'R'))