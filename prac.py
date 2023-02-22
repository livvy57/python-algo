day, night, distance = map(int, input().split())
import math

if day >= distance:
    print(1)

else:
    cnt = (distance - day)/(day - night)
    print(math.ceil(cnt + 1))