rom random import randint
import time
print("Welcome to.. \n EEEEEE    LL        IIII    ZZZZZZZ    AAAAAA\n EE        LL         II         ZZ    AA    AA\n EEEEE     LL         II       ZZZ     AAAAAAAA\n EE        LL         II      ZZ       AA    AA\n EEEEEE    LLLLLL    IIII    ZZZZZZZ   AA    AA")
print("What is your name?")
name = input()
print("okay", name, "how can i help you?","do you want to? (respond in number)","1. play rock paper scissors (not added yet)", "2. flip a coin", "3. calculate the fibonnaci system")
thingy = int(input())
if thingy == 3:
    nterms = int(input("how many terms?"))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
elif thingy == 2:
    yon=randint(1 ,2)
    if yon == 1:
        print("heads")
    else:
        print("tails")
    time.sleep(1)
elif thingy == 1:
    print("remember to use scissors not scissor")
    print("3 points to win")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    score = 0
    time.sleep(1)
    while score != 3:
        computer = randint(1 ,3)
        if computer == 1:
            computertake = "rock"
        elif computer == 2:
            computertake = "paper"
        elif computer == 3:
            computertake = "scissors"
        print("rock paper scissors!")
        usertake = input()
        if usertake == "rock":
            if computertake == "paper":
                 print("paper")
                 print("you lose")
            elif computertake == "scissors":
                print("scissor")
                print("you win")
                score = score + 1
                print(score)
            elif computertake == "rock":
                print("rock")
                print("draw")
        if usertake == "paper":
            if computertake == "paper":
                print("paper")
                print("draw")
            elif computertake == "scissors":
                print("scissors")
                print("you lose")
            elif computertake == "rock":
                print("rock")
                print("you win")
                score = score + 1
                print(score)
        if usertake == "scissors":
            if computertake == "paper":
                print("paper")
                print("you win")
                score = score + 1
                print(score)
            elif computertake == "scissors":
                print("scissors")
                print("draw")
            elif computertake == "rock":
                print("rock")
                print("you lose")
    print("congrats you win")
    time.sleep(1)
    print("please note the code works by picking a random number from 1 to 3 and converts it to words i set. this means the same number/choice has the option of happening in a chain or sequence its all just probability")
