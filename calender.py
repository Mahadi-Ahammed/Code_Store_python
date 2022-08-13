import calendar

mon_num,day_num,year_num= map(int,input().split())
 
obj = calendar.Calendar()
for day in obj.monthdays2calendar(year_num, mon_num):
    for i in day:
        if i[0]==day_num:
            nam=calendar.day_name[i[1]]
            print(nam.upper())