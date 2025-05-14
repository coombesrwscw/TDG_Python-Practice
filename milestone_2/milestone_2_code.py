
#This is a program that asks the user to create a username and password, before helping make sure that the password is strong.

userid=input("Please enter your username: ")
useridyn=input("Are you sure you want your password to be {}? (yes/no)".format(userid))
if useridyn == "yes":
    print("Okay, your username is: " + userid)
if useridyn == "no":
    userid=input("Please enter your new username: ")
    print("Okay, your username is now " + userid)    
passw=input("Now, please create a password: ")
len(passw)
if len(passw) < 6:
    print("Your password is kinda weak...")
    retrypassyn=input("Do you wnat to change it? (yes/no)")
    if retrypassyn == "yes":
        startpass=input("Please redo your password: ")
    else:
        print("Okay, your password is: " + passw)
if len(passw) > 12:
    print("Wow, that's a very strong password!")
else: 
    if len(passw) > 6:
        print("Ok, that's a decent password.")
