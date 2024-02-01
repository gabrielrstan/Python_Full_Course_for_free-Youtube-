usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

users = zip(usernames, passwords)

print(type(users))
'''for j in users:
    print(j)'''

users2 = list(users)

print()

print(type(users2))

for i in users2:
    print(i)

users3 = dict(users2)

print()

print(type(users3))

for key, value in users3.items():
    print(key + " " + value)

login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users4 = zip(usernames, passwords, login_date)
print()

for k in users4:
    print(k)
    