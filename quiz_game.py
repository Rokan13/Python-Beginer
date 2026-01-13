
questions=("how many element in periodic table?:",
          "whis animal lays the largest eggs?:",
          "what is the  most abundnat gas in earth>:",
          "how many bones are in human?:")
options=(("A. 116","B. 117","C. 118","D. 119"),
         ("A. whale","B. crocodile","C. elephant","D. ostrich"),
         ("A. nitrogen","B. oxygen","C. carbon di oxide","D. hydrogen"),
         ("A. 206","B. 207","C. 208","D. 209"))
answers=("C","D","A","A")
gusses=[]
score=0
question_num=0

for question in questions:
    print("--------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess=input("Enter (A,B,C,D):").upper()
    gusses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1
