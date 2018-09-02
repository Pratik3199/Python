#Pratik Singh

print("Welcome you in this game!")
game = True
while game:
    name1=input("Enter your name: - ")
    name2=input("Enter your name: - ")
    name1 = input(name1+ " Choose from Rock, Paper and Scissors?" )
    name2 = input(name2+ " Choose from Rock, Paper and Scissors?" )
    if name1 == name2:
        print("Match tied!")
    elif name1 == "Rock":
        if name2 == "Paper":
            print("Sorry!",name2, "covers", name1)
        else:
            print("Congrats! You win!", name1, "smashes", name2)
    elif name1 == "Paper":
        if name2 == "Scissors":
            print("Sorry!", name2, "cut", name1)
        else:
            print("Congrats! You win!", name1, "covers",name2)
    elif name1 == "Scissors":
        if name2 == "Rock":
            print("Sorry!", name2, "smashes", name1)
        else:
            print("Congrats! You win!", name1, "cut", name2)
    else:
        print("Wrong Input. Please Check your input!")

