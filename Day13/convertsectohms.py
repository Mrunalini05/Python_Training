#convert the given seconds to hourminutesecond (hms)

#ip:7262 sec
#op: 2h:1m:2s

#ip: 500
#op:0h:8m:20s

def hms(sec):
    hours = sec // 3600
    remaining_sec = sec % 3600
    minutes = remaining_sec // 60
    remaining_sec = remaining_sec % 60
    formatted_time = f"{hours}h:{minutes}m:{remaining_sec}s"
    return formatted_time

sec=int(input())
print(hms(sec))