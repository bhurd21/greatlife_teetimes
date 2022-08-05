from bs4 import BeautifulSoup
import requests
from generate_URL import get_URL

def gather_tee_times(m, d, y, start_t, end_t, p, h, c):
    URL = get_URL(m, d, y, start_t, end_t, p, h, c)
    soup = BeautifulSoup(requests.get(URL).text, features= 'lxml')
    try:
        lst = []
        job = soup.find('ul', class_="timeline-list timeline-hover").text
        for jobs in job.split():
            lst.append(jobs)
    except:
        lst = []
    return lst

def clean_tee_times(lst):
    ret = []
    for x in lst:
        if len(str(x)) > 2:
            if x.split()[0][-3] == ':':
                ret.append(x)
    return ret

def find_tee_times(month, day, year, start_time, end_time, people, holes):
    ret = {}
    course_list = [['C', 'Central Valley'], ['B', 'Bakkers Crossing'], ['R', 'Rocky Run'], ['W', 'Willow Run']]
    for x, name in course_list:
        ret[name] = clean_tee_times(gather_tee_times(month, day, year, start_time, end_time, people, holes, x))
    return ret

# print(find_tee_times(8, 8, 2022, 6, 8, 4, 18))