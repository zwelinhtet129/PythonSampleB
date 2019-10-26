#class Person:
#    pass

#p = Person()
#print(p)

#Method

#class Person:
#        def say_hi(self):
#            print('Hello, how are you')

#p = Person()
#p.say_hi()

#init method

#class Person:
#    def __init__(self,name):
#        self.name=name
#
#    def say_hi(self):
#        print('Hello, my name is ',self.name)
#
#p = Person('Zwe Lin Htet)')
#p.say_hi()

# class dog:
#     def __init__(self,name):
#         self.name = name
#
#     def __init__(self, eat):
#         self.eat = eat
#
#     def __init__(self,sleep):
#         self.sleep = sleep
#
#     def __init__(self, bark):
#         self.bark = bark
#
#     def say_hi(self):
#         print((self.name, self.eat , ', ', self.sleep), ', ' , self.bark)
#
# d = dog('Dog')
# d = dog("eat")
# d = dog("sleep")
# d = dog("bark")
#
# d.say_hi()


# class dog:
#
#     def __init__(self,name):
#         self.name = name
#
#     def say_hi(self):
#         print('hello, my name is ', self.name)

# # p = Person('Swaroop')#
# p.say_hi()
#
# d = dog('Name')
# d.color('BLACK')
# d.owner('U KAUNG')
#
# d.function() - bark
#             - eat
#             - sleep

# class Robot:
#
#     population = 0
#
#     def __init__(self,name):
#
#         self.name = name
#         print("(Initializing{})".format(self.name))
#
#         Robot.population +=  1
#
#     def die(self):
#
#         print("{} is being destroyed.".format(self.name))
#
#         Robot.population -=  1
#
#         if Robot.population == 0:
#             print("{} was the last one.".format(self.name))
#         else:
#             print("There are still {:d} robots working.".format(Robot.population))
#     def say_hi(self):
#             print("Greeting, my sisters call me {}.".format(self.name))
#
#     @classmethod
#     def how_many(cls):
#
#             print("We have {:d} robots.".format(cls.population))
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()
#
# droid3 = Robot('Q-35')
# droid3.say_hi()
# Robot.how_many()
#
# print("\nRobots can do some work here.\n")
#
# print("Robots have finished their work.Let's destroy them")
#
# droid1.die()
# droid2.die()
# droid3.die()
#
# Robot.how_many()

# class Robot:
#
#     population = 0
#
#     def __init__(self,name):
#
#         self.name = name
#         print("(Initializing{})".format(self.name))
#
#         Robot.population +=  1
#
#     def die(self):
#
#         print("{} is being destroyed.".format(self.name))
#
#         Robot.population -=  1
#
#         if Robot.population == 0:
#             print("{} was the last one.".format(self.name))
#         else:
#             print("There are still {:d} robots working.".format(Robot.population))
#     def say_hi(self):
#             print("Greeting, my sisters call me {}.".format(self.name))
#
#     @classmethod
#     def how_many(cls):
#
#             print("We have {:d} robots.".format(cls.population))
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()
#
# droid3 = Robot('Q-35')
# droid3.say_hi()
# Robot.how_many()
#
# print("\nRobots can do some work here.\n")
#
# print("Robots have finished their work.Let's destroy them")
#
# droid1.die()
# droid2.die()
# droid3.die()
#
# Robot.how_many()

class Dog:

    population = 0

    def __init__(self,name):

        self.name = name
        print("Catch dog".format(self.name))

        Dog.population +=  1

    def die(self):

        print("Dog {} is being fed.".format(self.name))

        Dog.population -=  1

        if Dog.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} dog waiting to be fed.".format(Dog.population))
    def say_hi(self):
            print("Dog {}.".format(self.name))

    @classmethod
    def how_many(cls):

            print("We have {:d} dogs.".format(cls.population))

d1 = Dog("1")
d1.say_hi()
Dog.how_many()

d2 = Dog("2")
d2.say_hi()
Dog.how_many()

d3 = Dog('3')
d3.say_hi()
Dog.how_many()

print("\nDogs are hungry.\n")

print("let's feed and release them.")

d1.die()
d2.die()
d3.die()

Dog.how_many()