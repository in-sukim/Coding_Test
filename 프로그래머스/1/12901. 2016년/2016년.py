import datetime
def solution(a, b):
    week_list = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    day = datetime.date(2016,a,b)
    return week_list[day.isoweekday()-1]
    