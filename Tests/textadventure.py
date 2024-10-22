Bond_With_Man = 0   # The bond you will have with a character in the game which will influence how the game ends 

def Start_Adventure():  # Back round information to give context behind the story
    print("Your name is Bob and you have randomly come across a very suspicious looking facility with a dark mist around it")
    print("1. Turn back around being too scared to enter the scary place")
    print("2. Enter through the door which is mysteriously covered in a thick fog, so you can't see inside")

    choice_1 = input("> ")  # First choice in the story 

    if choice_1 == "1":
        Go_Home()

    elif choice_1 == "2":
        Enter_Building()
            
    else:
        Start_Adventure()

def Go_Home():
    print("You're a scaredy cat and decide not to have a totatlly fun adventure")
    print("You walk through the forest the facility still on your mind and are suddenly attacked by a shadowy figure")
    print("Your screams echo between the trees and you are never seen again")
    print("Game Over")  # First ending in the game

def Enter_Building():
    print("You enter through the door which loudly creaks and are greated with a dimly lighted front office")
    print("The lights shutter and in the corner of your eye you see two doors, one with danger written on it in red and the other saying safe")
    print("1. Enter though the door that says Danger on it nervous to see what you will find inside")
    print("2. Enter though the door that says Safe on it feeling confident in your choice")

    choice_2 = input("> ")  # Second choice in the story

    if choice_2 == "1":
        Inside_Creepy_Door()

    elif choice_2 == "2":
        Inside_Safe_Door()

    else:
        Enter_Building()

def Inside_Creepy_Door():
    print("Inside the door way you see a very bright blinding light")
    print("1. walk slowly toward the light")
    print("2. run very fast at the light")
    
    choice_3 = input("> ")  # Third choice in the story 
    
    if choice_3 == "1":
        Talk_With_Man()

    elif choice_3 == "2":
        print("The person behind the blinding light shoots you out of fear")
        print("You can feel the pellets go through your body and your vision turns to black")
        print("Game Over")  # Second ending to the game

    else:
        Inside_Creepy_Door()


def Talk_With_Man():
    print("You see a man holding a flashlight at your face and he is also holding a shotgun")
    print("Still standing there he says, Omg I thought you were a monster, almost shot you there")
    print("What looks like to be an old man greets you and says, My name is Joe")
    print("1. Greet him back saying your name is Bob")
    print("2. Don't say anything to the stranger and look at him with an uneasy feeling in your eye")

    choice_4 = input("> ")  # Fourth choice in the story 

    if choice_4 == "1":
        Bond_With_Man + 1
        Monster_Encounter()

    elif choice_4 == "2":
        Monster_Encounter()

def Monster_Encounter():
    print("You have no more time to talk becuase a monster bursts through the door you just came through a moment ago")
    print("The old man tells you to run but not sure of what is the best option are frozen in place")
    print("1. You see a metal pipe on the gound and think to wack the monster with it")
    print("2. You follow the old mans direction to run")

    choice_5 = input("> ")

    if choice_5 == "1":
        Bond_With_Man + 1
        Through_The_Door()

    elif choice_5 == "2":
        Through_The_Door()

    else:
        Monster_Encounter()

def Through_The_Door():
    print("After either running or hitting the monster you go to the end of the hallways becuase")
    print("more monsters are crashing through the door")


def Inside_Safe_Door():
    print("As you creek open the door you see a monster at the end of a long hallway")

Start_Adventure()