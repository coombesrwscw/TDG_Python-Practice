
#this is a simple quiz to test knowledge of Python basics

#intro
print("Hello! This is a quiz on extremely basic Python code. Enjoy!")

#question 1
q1=input("First question: What is the purpose of the 'print' function in Python? \n a) To display output to the console \n b) To take input from the user \n c) To define a variable \n d) To create a loop \n Please enter your answer (a/b/c/d): ")
if q1.lower() == "a":
    print("Correct! The 'print' function is used to display output to the console.")
else:
    retry1=input("Incorrect. Would you like to know the correct answer? ")
    if retry1.lower() in ["yes", "y", "okay""ok", "go ahead", "sure"]:
        print("The correct answer is a) To display output to the console.")
    else:
        print("OK. Let's continue!")

#question 2
q2=input("Second question: What is the difference between a string and list? \n a) Strings contain multiple variables, but lists only have one. \n b) There is no difference. \n c) Lists contain multiple variables, but strings only have one. \n d) None of the above. \n Please enter your answer (a/b/c/d): ")
if q2.lower() == "c":
    print("Correct! Lists can contain multiple items, while strings are a single sequence of characters.")
else:
    retry2=input("Incorrect. Would you like to know the correct answer? ")
    if retry2.lower() in ["yes", "y", "okay""ok", "go ahead", "sure"]:
        print("The correct answer is c) Lists contain multiple variables, but strings only have one.")
    else:
        print("OK. Let's continue!")