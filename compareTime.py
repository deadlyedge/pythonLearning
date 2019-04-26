import time
def compare_time(time1,time2):
    s_time = time.mktime(time.strptime(time1,'%Y-%m-%d %H:%M'))
    e_time = time.mktime(time.strptime(time2,'%Y-%m-%d %H:%M'))
    print('time1 is:',s_time)
    print('time2 is:',e_time)
    return int(s_time) - int(e_time)

result = compare_time('2019-04-27 06:00','2019-04-29 05:00')
print('the compare result is:',result)
