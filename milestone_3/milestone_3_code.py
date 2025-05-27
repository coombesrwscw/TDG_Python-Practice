
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
