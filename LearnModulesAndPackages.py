# import the library
import urllib
import re


print (dir(urllib))

# use it
urlopen = urllib.urlopen("http://www.heise.de")
print (urllib)
print (urlopen.headers)
print urlopen.read()

l = dir(re)
print l
functions = []
for name in l:
    if "find" in name:
        functions.append(name)

print (sorted(functions))

