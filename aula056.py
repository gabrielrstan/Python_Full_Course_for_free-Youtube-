store = [("camisa", 20.00),
         ("calça", 25.00),
         ("jaqueta", 50.00),
         ("meias", 10.00)]

to_euros = lambda data: (data[0], data[1] * 0.91)
to_dollars = lambda data: (data[0], data[1] / 0.91)

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))


for i in store_euros:
    print(i)

print()

for i in store_dollars:
    print(i)