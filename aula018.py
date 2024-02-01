utensils = {"garfo", "colher", "faca", "faca", "faca"}
dishes = {"pote", "prato", "copo"}

utensils.add("guardanapo")
utensils.remove("garfo")
#utensils.clear()
#utensils.update(dishes)
dinner_table = utensils.union(dishes)

for x in utensils:
    print(x)

print("\n")
for y in dinner_table:
    print(y)

print("\n")
print(dinner_table.difference(dishes))
print("\n")
print(dinner_table.intersection(dishes))