from calendar import weekday
import email
from aiohttp import payload_type
from more_itertools import first, last


class Employee:

    company = "uwaterloo"
    hike = 4
    num_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = first + last + '@' + self.company +".com"

        Employee.num_emp += 1
    
    @property
    def email(self):
        return '{}{}@{}.com'.format(self.first, self.last, self.company)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('Deleted Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = self.pay * (1 + self.hike/100)

    @classmethod
    def raise_amt(cls, amount):
        cls.hike = amount

    #alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 

    def __repr__(self):
        return "Employee('{}' '{}' '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

class Developer(Employee):

    hike = 12
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print("Employee already exists")
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print("Employee does not exist")

    def print_emps(self):
        for emp in self.employees:
            print("-->",emp.fullname())


emp1 = Employee('vivek','chauhan',2500)
emp2 = Employee('test','user',3500)
emp3 = Employee('unknown','user',0)

#print(emp1.fullname())

#print(emp1.email)

#class variable "hike"
"""print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
"""
#Class as well as instances are able to access the aatributes
#Class Instances first check if they have that arribute in their instance, else they access the class attributes
"""print(Employee.hike)
print(emp1.hike)
print(emp2.hike)"""

#getting namespace associated with class instances
#class instances do not have class attributes
"""print(emp1.__dict__)
print(emp2.__dict__)"""

#getting namespace associated with class which contains class attributes
"""print(Employee.__dict__)"""

#Can set class attribute value instance wise as well
"""
Employee.hike = 5
print(Employee.hike)
print(emp1.hike)
print(emp2.pay)
emp2.hike = 7
emp2.apply_raise()
print(emp2.pay)
print(emp2.hike)
"""
#class attribute that makes more sense to be related to class as init method is called everytime an instance is created
#print(Employee.num_emp)

#Calling the class method to set the attribute value
"""Employee.raise_amt(9)
print(emp1.hike)"""

#using alternative constructor
"""emp4 = Employee.from_string('John-Doe-1100')
print(emp4.email)"""

import datetime

my_date = datetime.date(2022,8,4)
#print(Employee.is_workday(my_date))

#Developer class inheritance
dev1 = Developer('Jack','Daniel','2000','Python')

"""print(dev1.email)
print(dev1.prog_lang)"""

#Nice way to see all the inheritance path, i.e method resolution order, etc
#print(help(dev1))

#Manager class inheritance
mgr1 = Manager('Robert','Half','5000',[dev1])

"""print(mgr1.fullname())
print(mgr1.email)"""

mgr1.add_emp(emp1)
#print(mgr1.print_emps())

#print(isinstance(mgr1,Manager))
#print(issubclass(Manager,Employee))

#print(emp1)
"""print(repr(emp1))
print(str(emp1))

print(emp1.__repr__())
print(emp1.__str__())"""


#Operator overloading
"""print(emp1.pay)
print(emp2.pay)
print(emp1.__add__(emp2))"""

#Property Decorator
"""emp1.first = 'Vipul'
print(emp1.email) #able to access as attribute although defined as function: due to @property decorator
print(emp1.fullname())"""

#setter attribute
"""print(emp1.fullname)
emp1.fullname = 'Vicky Chauhan'
print(emp1.fullname)"""

#Deleter Attribute
"""del emp1.fullname"""