

class Timeslots():
    maxhours = 24*7
    maxhalfhours = maxhours*2
    def __init__(self):
        self.times = []

    def addtime(self,n):
        self.times.append(n)

    timedef = list(range(maxhalfhours)[0:30])
class Person:
    def __init__(self):
        self.schedule = Timeslots()

