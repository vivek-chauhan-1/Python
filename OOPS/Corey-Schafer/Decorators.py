from functools import wraps

#Decorators
"""
def outer_fn(msg):
    #outer_fn_varibale = msg
    def inner_fn():
        print(msg)
    #return inner_fn() #executes function
    return inner_fn #waiting to be executes

hi_fn = outer_fn('Hi')
bye_fn = outer_fn('Bye')

hi_fn()
bye_fn()

hi_fn()
bye_fn()"""

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed this before {}'.format(original_function.__name__))
        original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_function():
    print('Display function ran')

@decorator_function
def display_info(name, age):
    print('{} is {} years old'.format(name, age))

#one way to run
"""disp=decorator_function(display_function)
disp()"""

#Another way after adding @decorator_function
#display_function()

#passing arhuments to wrapper function using *args and **kwargs
#display_info('John', 25)


#decorators functionality as above but using class
class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('Call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@decorator_class
def display_function():
    print('Display function ran')

@decorator_class
def display_info(name, age):
    print('{} is {} years old'.format(name, age))

#display_info('John', 25)

def my_logger(original_fn):
    import logging
    logging.basicConfig(filename = '{}.log'.format(original_fn.__name__), level = logging.INFO)

    @wraps(original_fn)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {} and kwargs: {}'.format(args, kwargs)
        )
        return original_fn(*args, **kwargs)

    return wrapper

@my_logger
def display_info(name, age):
    print('{} is {} years old'.format(name, age))

#display_info('Hank',23)

def my_timer(original_fn):
    import time

    @wraps(original_fn)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = original_fn(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} sec'.format(original_fn.__name__, t2))
        return result
    
    return wrapper

import time

#stacking docorators gives wrong results as wrapper is the output of first decorator 
#which acts as input to second decoratorr instaed of original function 
#the order of execution of decorators is @mytimer then @my_logger,
#  i.e decorator closer to function gets executed first

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('{} is {} years old'.format(name, age))

display_info('Tom',26)