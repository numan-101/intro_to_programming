def example1():
    def f(d):
        return d

    c = [1, 2, 3]

    e = f(c)

    print(c is e)

#####################################

def example2():
    def modify(l):
        l[0] = -1

    list = [1, 2, 3]

    print(list)

    modify(list)

    print(list)

#####################################

def example3():
    def reasign(l):
        l = [4, 5, 6]
        # rebind
        # l and list refered to the same object
        # however, the reference have been overwritten to point to another list
    
    list = [1, 2, 3]

    print(list)

    reasign(list)

    print(list)

# Function arguments are passed by object reference
# the value of the refernce is copied not the value of the object

#####################################

def example4():
    def banner(message, border='-'):
        line = border * len(message)
        print(f'{line}\n{message}\n{line}\n')

    banner('Hello World')
    banner('Hello from python', '*')
    banner('Hawdy', border='#')
    banner(border='@', message='Good day')

#####################################

import time

def example5():
    print(time.ctime())

    def show_time(t=time.ctime()):
        print(t)
    
    show_time()
    show_time()
    show_time()

# Def argument evaluation
# default argument values are evaluated when def is evaluated

#####################################

def example6():
    def add_spam(menu=[]):
        menu.append('spam')
        return menu
    
    breakfast = ['bacon', 'eggs']
    add_spam(breakfast)
    print(breakfast)
    
    lunch = ['fish']
    add_spam(lunch)
    print(lunch)

    print(add_spam())
    print(add_spam())
    print(add_spam())

    # Always use immutable objects such as integers or
    # strings for default value

    def add_eggs(menu=None):
        if menu is None:
            menu = []
        menu.append('eggs')
        return menu
    
    print(add_eggs())
    print(add_eggs())
    print(add_eggs())

#####################################

def example7():
    # python has dynamic and strong type system
    # dynamic: object types are only resolved at runtime
    def add(a, b):
        return a + b
    
    print(add(1, 5))
    print(add(1.2, 1.5))
    print(add('news', 'paper'))
    print(add([1, 6], [7, 8]))

    # strong: no implicit type conversion

    print(add('this is', 99))

#####################################

example7()