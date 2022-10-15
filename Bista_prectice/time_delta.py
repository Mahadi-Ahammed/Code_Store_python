from datetime import datetime, timedelta

t=int(input())
for i in range(t):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    tDiff=t1-t2
    sec=int(tDiff.total_seconds())
    print(sec)
