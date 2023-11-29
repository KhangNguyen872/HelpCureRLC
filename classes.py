'''
class person:
    def introduce_self(self):
        print("Hello my name is",self.name)
    def favorite_color(self):
        print("My favorite color is",self.color)

sub1 = person()
sub1.name = "Soham"
sub1.color = "Blue"
sub1.weight = 107

sub2 = person()
sub2.name = "Joe"
sub2.color = "Red"
sub2.weight = 195

sub1.introduce_self()
sub2.introduce_self()
sub1.favorite_color()
sub2.favorite_color()
'''

class create_new_person:
    def define_name(self):
        print("Name: " + self.name)
    def define_age(self):
        print("Age: ",self.age)
    def define_height(self):
        print("Height:",self.height)
    def define_weight(self):
        print("Weight:",self.weight)

name = input("What is their name?: ")
age = int(input("What is their age?: "))
height = input("What is the height?: ")
weight = input("What is their weight?: ")

Person = create_new_person()
Person.name = name
Person.age = age
Person.height = height
Person.weight = weight

Person.define_name()
Person.define_age()
Person.define_height()
Person.define_weight()

repeat = input("Would you like to save another file? y/n: ")

while repeat == "y":
    name = input("What is their name?: ")
    age = int(input("What is their age?: "))
    height = input("What is the height?: ")
    weight = input("What is their weight?: ")

    Person = create_new_person()
    Person.name = name
    Person.age = age
    Person.height = height
    Person.weight = weight

    Person.define_name()
    Person.define_age()
    Person.define_height()
    Person.define_weight()

    repeat = input("Would you like to save another file? y/n: ")

if repeat != "y":
    print("Terminated")