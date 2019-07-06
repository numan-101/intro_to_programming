# scopes
# contexts in which name references can be looked up

# local: defined inside the current function
# Enclosing: defined inside any enclosing functions
# Global: defined as the top level of the module
# built-in: provided by builtins modules

count = 0

def show_count():
    print('count =', count)

def set_count(c):
    # this count is different, not the global one
    # called a shadow variable
    count = c

def set_count2(c):
    global count
    count = c

show_count()
set_count(5)
show_count()
set_count2(5)
show_count()