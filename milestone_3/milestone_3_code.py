
#this is a simple quiz to test knowledge of Python basics

#intro
print("Hello! This is a quiz on extremely basic Python code. Enjoy!")

#username stuff
userid=input("Please enter your preferred username: ")
useridyn=input("Are you sure you want your username to be {}? (y/n) ".format(userid))
if useridyn == "y":
    print("Okay, your username is: " + userid)
if useridyn == "n":
    userid=input("Please enter your new username: ")
    userid=input("Okay, your username is now {}, is that correct? (y/n) ".format(userid))
    if useridyn == "y":
        print("Okay, your username is: " + userid)
    if useridyn == "n":
        userid=input("Please enter your new username: ")
        useridyn=input("Okay, your username is now {}, is that correct? (y/n) ".format(userid))    
    if useridyn == "y":
                print("Okay, your username is: " + userid)
    elif useridyn == "n":
                print("You're annoying, goodbye.")
                exit()
#password stuff
passw=input("Now, please create a password: ")

#question 1
