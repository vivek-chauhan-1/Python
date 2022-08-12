#first class functions

from sympy import Id


def square_function(x):
    return x*x

""""
f = square_function(5)
print(f)

#first class functions
#assigning function to a variable is different that passing function with argument
fn = square_function
print(fn(5))
print(square_function)"""

def my_map(func, arg_list):
    result = []
    for a in arg_list:
        result.append(func(a))
    return result

res=my_map(square_function, [1,2,3,4])
#print(res)

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

"""h1 = html_tag('h1')
h1("Headline 1")
h2 = html_tag("p")
h2("paragraph")"""

#Mutable/Immutable
#when we say string as an immutable type : it does not mean we cannot set the same variable 
# but it is not the same variable modifies but a new one
#Different memmory addresses
"""a = "John Mayers"
print(a)
print("Address of a is : {}".format(id(a)))

a = "John Travolta"
print(a)
print("Address of a is : {}".format(id(a)))"""


#creating a new string varibale for every concatenation operation, could be fatal for long strings
"""employees = ['Jon', 'John', 'Jack', 'Tom', 'Carl', 'Steve', 'Sam']

output = "<ul>\n"

for employee in employees:
    output += "\t<li>{}</li>\n".format(employee)
    print("Address of output is: {}".format(id(output)))

output += "</ul>\n"
print(output)"""


"""#memoization
import time

ef_cache = {}
def expensive_function(num):
    if num in ef_cache:
        return ef_cache[num]

    print("Calculating for {}".format(num))
    time.sleep(1)
    res = num*num
    ef_cache[num] = res
    return res

result=expensive_function(4)
print(result)

result=expensive_function(10)
print(result)

result=expensive_function(4)
print(result)

result=expensive_function(10)
print(result)"""

#permutation and combination
import itertools

"""my_list = [1,2,3]

print("\n combinations: \n ")
combinations = itertools.combinations(my_list,2)
for c in combinations:
    print(c)

print("\n permutations: ")
permutations = itertools.permutations(my_list,2)
for p in permutations:
    print(p)"""

my_list = [1,2,3,4,5,6]
combinations = itertools.combinations(my_list,3)
result =[i for i in combinations if sum(i)==10]
print(result)

word ="sample"
letters = "elamps"
permutations = itertools.permutations(letters, 6)
for p in permutations:
    if ''.join(p) == word:
        print('Match!')
        break
    else:
        print("No match found")
