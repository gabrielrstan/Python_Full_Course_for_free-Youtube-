import time

print(time.ctime(0))
print(time.ctime(1000000))
print(time.time())
print(time.ctime(time.time()))

time_object = time.localtime()
time_object2 = time.gmtime()

print(time_object)

local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
local_time2 = time.strftime("%B %d %Y %H:%M:%S", time_object2)

print(local_time)
print(local_time2)

time_string = "20 April, 2020"
time_object3 = time.strptime(time_string, "%d %B, %Y")

print(time_object3)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string2 = time.asctime(time_tuple)

print(time_string2)

time_tuple2 = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string3 = time.mktime(time_tuple2)

print(time_string3)
