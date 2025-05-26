
#This is a program that asks the user to create a username and password, before helping make sure that the password is strong.

userid=input("Please enter your preferred username: ")
useridyn=input("Are you sure you want your username to be {}? (y/n) ".format(userid))
if useridyn == "y":
    print("Okay, your username is: " + userid)
if useridyn == "n":
    userid=input("Please enter your new username: ")
    userid=input("Okay, your username is now {}, is that correct? (y/n) ".format(userid))

passw=input("Now, please create a password: ")
len(passw)
if len(passw) < 6:
    print("Your password is kinda weak...")
    retrypassyn=input("Do you wnat to change it? (y/n) ")
    if retrypassyn == "yes":
        startpass=input("Please redo your password: ")
    else:
        print("Okay, your password is: " + passw)
if len(passw) > 12:
    print("Wow, that's a very strong password!")
else: 
    if len(passw) > 6:
        print("Ok, that's a decent password.")
