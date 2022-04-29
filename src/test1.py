import datetime
import time


def string_time_to_unix_time(input_str):
    ymd_s, hms_s = tuple(input_str.split(" "))
    year, month, day = tuple(ymd_s.split('-'))
    hms_s = hms_s.split(".")[0]
    hour, minute, second = tuple(hms_s.split(':'))
    date_time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
    print("unix_timestamp => ",(time.mktime(date_time.timetuple())))



ST = '2018-09-12 07:22:40.080409'
ET = '2018-09-13 21:51:21.865953'

Year = ST[0:4]
Mon = ST[5:7]
Day = ST[8:10]
Hour = ST[11:13]
Min = ST[14:16]
Sec = ST[17:19]

#date_time = datetime.datetime(int(Year), int(Mon), int(Day), int(Hour), int(Min), int(Sec))
#print("unix_timestamp => ",(time.mktime(date_time.timetuple())))


string_time_to_unix_time(ET)
