astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])


print(astring[::-1])

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print (afewwords)

print (afewwords.__class__)