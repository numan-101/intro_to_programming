# method: function defined within the class
# instance mthods: functions which can be called on objects
# self: the first argument to all instance methods

class Flight:
    # instance method
    def number(self):
        return "SN06"

f = Flight()
print(f.number())

