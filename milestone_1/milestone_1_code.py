
# This is a simple program that asks the user for their name and calculates their age, before printing a message using that information.

name=input("Hello, what is your name? ")
print("Hello, " + name + "! That's a nice name!")
birth=input("What year were you born? ")
year=input("And what year is it now? ")
age=int(year)-int(birth)
print("So you are {} years old, you were born during {}, and your name is {}?".format(age, birth, name))
print("It is nice to meet you, {}." .format(name))
