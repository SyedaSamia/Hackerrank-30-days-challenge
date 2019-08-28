class Person:
    def __init__(self,initialage):
        if initialage >= 0:
            self.age = initialage
        else:
            print("Age is not valid, setting age to 0")
            self.age = 0

    def yearPasses(self):
        self.age += 1


    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age >=13 and self.age <18 :
            print("You are teenager.")
        else :
            print("You are old.")


t = int(input())
for i in range(0,t):
    age = int(input())
    x = Person(age)
    x.amIOld()
    for j in range(0,3):
        x.yearPasses()
    x.amIOld()


