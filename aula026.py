def add(*stuff): #convenção usar *args
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,6,8,7,4,2,1,5))