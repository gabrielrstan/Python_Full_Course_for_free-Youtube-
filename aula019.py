capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

print(capitals['Russia'])
#print(capitals['Germany'])
print(capitals.get('Germany'))

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
#capitals.clear()

print(capitals.keys())
print(capitals.values())
print(capitals.items)
print("\n")

for key, value in capitals.items():
    print(key,value)
