'''This Animal class and examples of use are derived from Kirby Urner's work.
'''

class Animal:  
    '''Object structure:
       An Animal has a name and a gut (data fields of an Animal object).
       An Animal can greet, eat, and excrete (Animal method names).
    '''

    #PY In Python, the object acted on must always be explicitly named.
    #PY By convention, in a class definition, the current object is called self,
    #PY    so self is the first formal parameter name for *each* object method
    #PY Object methods are function definitions inside the class.
    def __init__(self, aName): #PY construct new Animal, initialize data fields
        '''Create Animal with name aName.''' #PY documentation string
        self.name = aName      #PY Object notation:  object.attribute
                               #PY   Here the self object's name is set to aName
        self.gut = []          # gut initially is an empty list of contents

    def greet(self):
        print("Hello, my name is", self.name) #PY print: item1 item2 ...

    def eat(self, food):
        self.gut.append(food) # append food to the end of the gut list

    def excrete(self):
        print(self.gut.pop(0)) # take oldest list item, at position 0

    ######## Conversion to String  ########

    def __str__(self): #PY for conversion to str (string type) and printing
        return 'Animal: ' + self.name
        #PY + sign used with strings for concatenation

    def __repr__(self): #PY for conversion to formal string representation
        return 'Animal(' + repr(self.name) + ')' #PY repr quotes a string
        
#PY indentaton ends, so end of class definition

#PY outside class definition - plain Python function definition
def testAnimal():   #PY not need parameters; can do stuff and return nothing
    mouse = Animal('Squeeky') #PY object created using class name, not __init__
    mouse.greet()             #PY mouse, before the period is self in definition
    print('Eat grass and leaf.')
    mouse.eat('grass')        #PY same use of self, but list further parameter
    mouse.eat('leaf')
    print('Gut contains', mouse.gut)  #PY can reference method or data element
    print('Now excrete:')
    mouse.excrete()
    print('Gut contains', mouse.gut)
    snake = Animal('Hissy')
    snake.greet()
    print('Eat Squeeky.')
    snake.eat(mouse)
    print('Gut contains', snake.gut)
    