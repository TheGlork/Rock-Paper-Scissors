import random


ftp = int(input("How many rounds do you want to play? "))
x = random.randint(1,3)
i = 1
comp_g = ""

user_p = 0
comp_p = 0



while i <= ftp:
    x = random.randint(1,3)

    if x == 1:
        comp_g = "rock"
    elif x == 2:
        comp_g = "paper"
    elif x == 3:
        comp_g = "scissor"
    user_g = input("Enter rock, paper or scissor: ")

    if comp_g == user_g:
        print("Its a draw, no one gets points")
        print("The computers points are: ", comp_p)
        print("Your points are: ", user_p)
    elif comp_g == "rock" and user_g == "scissor":
        comp_p = comp_p + 1
        print("Computer said rock, It gets a point")
        print("The computers points are: ", comp_p)
        print("Your points are: ", user_p)
    elif comp_g == "paper" and user_g == "rock":
        comp_p = comp_p + 1
        print("Computer said paper, It gets a point")
        print("The computers points are: ", comp_p)
        print("Your points are: ", user_p)
    elif comp_g == "scissor" and user_g == "paper":
        comp_p = comp_p + 1
        print("Computer said scissor, It gets a point")
        print("The computers points are: ", comp_p)
        print("Your points are: ", user_p)

    elif comp_g == "rock" and user_g == "paper":
        user_p = user_p + 1
        print("Computer said rock, you get a point")
        print("The computers points are: ", comp_p)
        print("Your points are: ", user_p)
    elif comp_g == "paper" and user_g == "scissor":
        user_p = user_p + 1
        print("Computer said paper, Iyou get a point")
        print("The computers points are: ", comp_p)
        print("Your points are: ", user_p)
    elif comp_g == "scissor" and user_g == "rock":
        user_p = user_p + 1
        print("Computer said scissor, you get a point")
        print("The computers points are: ", comp_p)
        print("Your points are: ", user_p)

    i = i + 1

if comp_p > user_p:
    print("The Computer has won, better luck next time!")
elif comp_p < user_p:
    print("You won!! Congratulations")
elif comp_p == user_p:
    print("Its a draw!")