name = "bro Code!"

if(name[0].islower):
    name = name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_caracter = name[-1]

print(name)
print(first_name)
print(last_name)
print(last_caracter)