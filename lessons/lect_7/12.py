'''Summary:
* All types in python have a class
* Classes define the structure and behavior of an object
* Class is determined when a n object is created
    - normally fixed for the lifetime
* classes are the key support for object oriented programming in Python
* classes defined using the class keyword followed by CamelCase name
* class instances are created by calling the class if it were a function
* instance methods are functions defined inside the class
    - should accept an object instance called self as the first parameter
* methods are called using the instance.method()
    - syntactic sugar for passing self instance to method
* the optional __init__() method initialized new instances
    - if present the constructor calls __init__()
    - __init__() is not the constuctor
* arguments passed to the constructor are forwarded to the initializer
* instance attributes are created simply by assigning to them
* implementation details are denoted by a leading underscore
    - there are no public, protected or private access modifires in Python
* accessing implementation details can be very useful
    - especially during development and debugging
* class invariants should be established in the intializer
    - if the variants can't be established raise exceptions to signal failure
* methods can have docstrings, just like regular functions
* classes can have docstrings
* Even within an object method calls must be preceded with self
* You can have as many classes and functions in a module as you wish
    - related classes and global functions are usually grouped together this way
* Polymorphism in Python is achived through duck typing
* Polymorphism in Python does not use shared base classes or interfaces
* class inheritance in primarily useful for sharing implementation
* all methods are inherited, including special methods like the initializer
* strings support slicing, because they implement the sequence protocol
* following the law of Demeter can reduce coupling
* we can nest comprehensions
* it can sometimes be useful to discard the current item in comprehension
* when dealing with one-based collections it's often easier just to waste one list entry
* don't feel compelled to use classes when a simple function will suffice
* comprehinsions or generator expression can be split over multiple lines
* statements can be split over multiple lines using backslash
    - only use to improve readability
* use tell don't ask to avoid tight coupling between objects '''
