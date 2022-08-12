#duck typing and easier to ask forgiveness than permissions
#if we expect less exceptions, 
# than data is scanned once but if we are checking on conditions, we scan data multiple times
#also avoids race condition

class Duck:
    def quack(self):
        print("Ducks can quack")

    def flap(self):
        print("Ducks flap")

class Person:
    def quack(self):
        print("I can quack like duck")

    def flap(self):
        print("I can flap my arms like duck")

#not duck typed
"""def quack_and_flap(thing):
    if isinstance(thing, Duck):
        thing.quack()
        thing.flap()
    else:
        print("Not a Duck")"""

"""#duck typed but dangerous
def quack_and_flap(thing):
    thing.quack()
    thing.flap()"""

"""def quack_and_flap(thing):
    #LBYL(Non-Pythonic)
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'flap'):
        if callable(thing.flap):
            thing.flap()"""

#EAPF(Pythonic way)
def quack_and_flap(thing):
    try:
        thing.quack()
        thing.flap()
        thing.bark()
    except AttributeError as e:
        print(e) 


d = Duck()
quack_and_flap(d)

p = Person()
quack_and_flap(p)


data1 = {'name':'John', 'age':23, 'pay':2500, 'job':'programmer'}
data2 = {'name':'Jacob', 'age':18}

#Non-pythonic way
if 'name' in data1 and 'age' in data1 and 'job' in data1:
    print('{name} is {age} years old and works as {job}'.format(**data1))
else:
    print("Missing some attributes")

#pythonic way
try:
    print('{name} is {age} years old and works as {job}'.format(**data2))
except KeyError as e:
    print("Missing {} key".format(e))

#race condition
import os

filename = r'C:\Users\hp\Desktop\Books\Corey_Schafer\display_info.log'

if os.access(filename, os.R_OK):
    with open(filename) as f:
        print(f.read())
else:
    print("File cannot be accessed")

try :
    f = open(filename)
    print(f.read())
except IOError as e:
    print(e)
else:
    with f:
        print(f.read())