from Lab5 import Time

t1 = Time(10, 14, 30)
print("t1 = ", t1)
print("t1 hours = ", t1.getHours())
print("t1 minutes = ", t1.getMinutes())
print("t1 seconds = ", t1.getSeconds())

t2 = Time(17, 30, 10)
print("t2 = ", t2)
print("t2 hours = ", t2.getHours())
print("t2 minutes = ", t2.getMinutes())
print("t2 seconds = ", t2.getSeconds())

print("t1 time in seconds = ", t1.timeInSeconds())
print("t2 time in seconds = ", t2.timeInSeconds())

t1.changeTheTime(9, 17, 45)
print("t1 = ", t1)

print("t2 twelve hour clock = ", t2.twelveHourClock())

print("t1 what time is it = ", t1.whatTimeIsIt())

print("t1 compare to t2 = ", t1.compareTo(t2))
print("t2 compare to t1 = ", t2.compareTo(t1))

print("t1 time till t2 = ", t1.timeTill(t2))


