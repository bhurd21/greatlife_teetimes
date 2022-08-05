from generate_tee_times import find_tee_times


MONTH = 8
DAY = 10 # must be no more than a week in advance
YEAR = 2022
START_TIME = 12 # military time, > 6
END_TIME = 14 # military time, < 20
PLAYERS = 4 # 1 through 4
HOLES = 18 # 9 or 18


def get_poss_times(s, e):
    poss_times = {}
    for x in range(s - 1, e + 2):
        if x > 12:
            x = x - 12
        for y in range(0, 6):
            poss_times[str(x) + ':' + str(y) + '0'] = []
    return poss_times

def final(m, d, y, s, e, p, h):
    dic = find_tee_times(m, d, y, s, e, p, h)
    poss_times = get_poss_times(s, e)
    for key, value in dic.items():
        for v in value:
            poss_times[v].append(key)
    temp_check = True
    ret = {}
    for key, value in poss_times.items():
        if len(value) != 0:
            ret[key] = value
            temp_check = False
    if temp_check:
        return 'No avaliable times'
    else:
        return ret

# final(MONTH, DAY, YEAR, START_TIME, END_TIME, PLAYERS, HOLES)