class Robot:
    def __init__(self, name: str, color: str, weight: int):
        if type(weight) != int:
            raise TypeError('Weight must be integer, found {}'.format(type(weight)))
        
        self.name = name
        self.color = color
        self.weight = weight

    def intreduce_self(self):
        print('Hello, my name is', self.name)

r1 = Robot(name='Anas', color='Blue', weight='4')

r1.intreduce_self()

r2 = Robot(name='Ahmed',color='Yellow',weight=20)

r2.intreduce_self()
