food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

print(food)
print(food[4])

food[0] = "sushi"

print(food[0])

food.append("ice cream")
food.remove("hotdog")
food.pop(3)
food.insert(0,"cake")
food.sort()
#food.clear()
for x in food:
    print(x)
