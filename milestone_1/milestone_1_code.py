
# This is a simple program that asks the user for their name and calculates their age, before printing a message using that information.

userid=input("Please enter your name: ")
print("Hello, " + userid + "! That's a nice name!")
birth=input("What year were you born? ")
year=input("And what year is it now? ")
age=int(year)-int(birth)
print("So you are {} years old, you were born during {}, and your name is {}?".format(age, birth, userid))
print("It is nice to meet you, {}." .format(userid))
