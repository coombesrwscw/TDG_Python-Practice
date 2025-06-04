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

#question 3
q3=input("Third question: What is the purpose of putting text after a hashtag in Python? \n a) To save data to the repository \n b) To define a variable's syntax \n c) To give info about sections of the code to future editors and comment on details of the code \n d) To help the device know what to do with certain peices of code \n Please enter your answer (a/b/c/d): ")
if q3.lower() == "c":
    print("Correct! Text after a hashtag is called a comment, which helps explain the code to others, or yourself if you're worried about being forgetful.")
else:
    retry3=input("Incorrect. Would you like to know the correct answer? ")
    if retry3.lower() in ["yes", "y", "okay""ok", "go ahead", "sure"]:
        print("The correct answer is c) To give info about sections of the code to future editors and comment on details of the code.")
    else:
        print("OK. I can't be bothered writing more questions, so thats the end of my quiz!")
#end of quiz
score = 3
if q1.lower() == ["b", "c", "d"] or q2.lower() == ["a", "b", "d"] or q3.lower() == ["a", "b", "d"]:
    print("You didn't get all the questions right, but that's okay! Keep practicing and you'll improve.")
if q1.lower() == "a" and q2.lower() == "c" and q3.lower() == "c":
    print("Congratulations! You got all the questions right!")
if q1.lower() == ["b", "c", "d"]:
    score = score - 1
if q2.lower() == ["a", "b", "d"]:
    score = score - 1  
if q3.lower() == ["a", "b", "d"]:
    score = score - 1
print("Your score is {} out of 3." .format(score))
print("Thank you for taking the quiz! I hope you learned something new about Python basics. Goodbye!")
