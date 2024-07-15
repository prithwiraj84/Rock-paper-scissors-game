import random
computer_choice = ["rock", "paper", "scissor"]
user_point = 0
computer_point = 0
while True:
    user_choice = input("enter your choice {rock, paper, scissor}: ")
    a = random.choice(computer_choice)
    if user_choice == a:
        print("both choice are same TIE!")
    elif user_choice == "rock" and a == "paper":
        computer_point +=1
        print("user loses")
    elif user_choice == "paper" and a == "scissor":
        computer_point += 1
        print("user loses")
    elif user_choice == "scissor" and a == "rock":
        computer_point +=1
        print("user loses")
    else:
        user_point +=1
        print("user win")
    print("computer choice = ",a)
    print("user choice = ",user_choice)
    print("computer point =",computer_point)
    print("user point = ",user_point)
    choice = input("enter do you want to continue playing? (y/n): ")
    if choice == "n":
        break

