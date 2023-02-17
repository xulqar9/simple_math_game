import time

print("\nmath game!!\n")

name = input("please enter your name?\n")
score = 0
score2 = 0
total_questions = 3
points1 = (score / total_questions) * 100

print("\nwelcome", name)
answer = input("\nAre you ready to play this small math game? (yes/no) : \n")
while points1 <= 80:
    if answer == "yes":
        question_loop = True
        while question_loop == True:
            answer = input("\nQuestion 1: What is 2 + 2 - 1 =\n")
            if answer == "3":
                score += 1
                print("\ncorrect!!")
            else:
                print("\nWrong Answer :(m")
                print("wanna try again?")
                choice = input("ENTER YES OR NO: ")
                if choice == "YES":
                    question_loop = False
                    continue
                else:
                    print("Aight then")
            answer = input("\nQuestion 2: what is 99 - 23 =\n")
            if answer == "76":
                score += 1
                print("\ncorrect!!!\n")
            else:
                print("Wrong Answer :(\n")

            answer = input("\nQuestion 3: What is 30 / 3 =\n")
            if answer == "10":
                score += 1
                print("\ncorrect!!\n")
            else:
                print("\nWrong Answer :(")
    elif answer == "no":
        time.sleep(2)
        exit(print("bye..."))
    points1 = (score / total_questions) * 100

else:
    print("congrats!! you passed level 1")
    print("\npoints obtained:", points1)
    if points1 >= 80:
        print("\nyou passed level 1, you attempted",
              score, "questions correctly!\n")
        answer = input("Are you ready to proceed to level 2? (yes/no):\n")
        if answer == "no":
            time.sleep(2.4)
            exit(print("bye..."))
        if answer == "yes":
            answer = input("\nQuestion 1: What is x if x(3+2)=25 \n")
            if answer == "5":
                score2 += 1
                print("\ncorrect!!")
            else:
                print("\nWrong Answer :(")

            answer = input("\nQuestion 2: what is x if x2+4=10\n")
            if answer == "3":
                score2 += 1
                print("\ncorrect!!!\n")
            else:
                print("Wrong Answer :(\n")

            answer = input(
                "\nQuestion 3: what is the approximate value of pi 'π' in math?=\n")
            if answer == "3.14":
                score2 += 1
                print("\ncorrect!!")
            else:
                print("\nWrong Answer :(")

            points2 = (score2 / total_questions) * 100
            print("points obtained:", points2+points1)
            time.sleep(2)
            exit(print("perfect!!"))