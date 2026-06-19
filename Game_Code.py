# importet moduls
import time
import pygame

# lode music and link them
music1 = "music/black_by_pearl_jam.ogg"
pygame.init()
pygame.mixer.init()


# lode textfiles and link them

with open("story_txt/intro.txt", "r", encoding="utf-8") as file:
    intro = file.read()

with open("story_txt/knock.txt", "r", encoding="utf-8") as file:
    knock = file.read()

with open("story_txt/door_police.txt", "r", encoding="utf-8") as file:
    door_police = file.read()

with open("story_txt/chairs.txt", "r", encoding="utf-8") as file:
    chairs = file.read()

with open("story_txt/shocked.txt", "r", encoding="utf-8") as file:
    shocked = file.read()

with open("story_txt/photo_ordescription.txt", "r", encoding="utf-8") as file:
    photo_ordescription = file.read()

with open("story_txt/photo.txt", "r", encoding="utf-8") as file:
    photo  = file.read()

with open("story_txt/description.txt", "r", encoding="utf-8") as file:
    description  = file.read()

with open("story_txt/left.txt", "r", encoding="utf-8") as file:
    left  = file.read()


with open("story_txt/go_or_bed.txt", "r", encoding="utf-8") as file:
    go_or_bed  = file.read()


with open("story_txt/walk.txt", "r", encoding="utf-8") as file:
    walk  = file.read()

with open("story_txt/walkpart2.txt", "r", encoding="utf-8") as file:
    walkpart2  = file.read()

with open("story_txt/walkpart3.txt", "r", encoding="utf-8") as file:
    walkpart3  = file.read()

with open("story_txt/walkpart4.txt", "r", encoding="utf-8") as file:
    walkpart4  = file.read()


with open("story_txt/walkpart5.txt", "r", encoding="utf-8") as file:
    walkpart5  = file.read()


    
with open("story_txt/dream.txt", "r", encoding="utf-8") as file:
    dream  = file.read()

with open("story_txt/dream2.txt", "r", encoding="utf-8") as file:
    dream2  = file.read()
with open("story_txt/dream3.txt", "r", encoding="utf-8") as file:
    dream3  = file.read()


with open("story_txt/waup.txt", "r", encoding="utf-8") as file:
    waup  = file.read()


with open("story_txt/waup2.txt", "r", encoding="utf-8") as file:
    waup2  = file.read()

with open("story_txt/pc1.txt", "r", encoding="utf-8") as file:
    pc1  = file.read()

with open("story_txt/messeag1.txt", "r", encoding="utf-8") as file:
    messeag1  = file.read()


with open("story_txt/messeag2.txt", "r", encoding="utf-8") as file:
    messeag2  = file.read()


with open("story_txt/messeag3.txt", "r", encoding="utf-8") as file:
    messeag3 = file.read()




with open("story_txt/game_over.txt", "r", encoding="utf-8") as file:
    game_over = file.read()


# def function that make that the player need to press "enter" to to continue with the story

def wait():
    input()


# extremely epic intro (I should get GOTY award for this /s)

print("Welcome to Black Hollow!")
print("A Text Adventure made by TimFloClausen")
input("Press enter to start the game: ")
print(intro)
input("Press Enter to continue! ")

# game starts

print("Knock...")
time.sleep(1)

print("Knock...")
time.sleep(1)

print("Knock...") 
time.sleep(1)

print(knock)

wait()

task_1 = input("What do you want to do first? Open the door or take a pill? (door/pills): ").strip().lower()
 
while task_1 not in ["door", "pills"]:
    print("I didn't understand that.")

    task_1 = input(
        "Please choose: door or pills: "
    ).strip().lower()

    
if task_1 == "door":
    print(" You chose door! You open the door. Two police officers are standing in front of you.")
elif task_1 == "pills":
    print("You chose pills! You go to the bathroom, take a paracetamol, and then open the door.")
    print("Two police officers are still waiting outside.")
    wait()


print(door_police)

wait() 
    
print(shocked)

wait()


print(chairs)


wait()

print(photo_ordescription)

wait()

task_2 = input("Do you want to see a picture or only a description? (photo/description) ").strip().lower()

while task_2 not in ["photo", "description"]:
    print("I didn't understand that.")

    task_2 = input(
        "Please choose: photo or description: "
    ).strip().lower()




if task_2 == "photo":
    print("You chose photo!")
    print(photo)

elif task_2 == "description":
     print("You chose description!")
     print(description)


wait()

print(left)

wait()

print(go_or_bed)

wait()

task_3 = input("Do you want to go out for a walk, or go to bed again? (walk/bed) ").strip().lower()

while task_3 not in ["walk", "bed"]:
    print("I didn't understand that.")

    task_3 = input(
        "Please choose: walk or bed: "
    ).strip().lower()


if task_3 == "walk":
    print("You chose walk!")
    print(walk)
    wait()
    print(walkpart2)
    wait()
    print(walkpart3)
    wait()
    print(walkpart4)
    wait()
    print(walkpart5)

elif task_3 == "bed":
    print("You chose bed!")
    print(dream)
    wait()
    print(dream2)
    wait()
    print(dream3)
    wait()
    print(waup)
    wait()
    print(waup2)

print(pc1)

password = "pizza"
while True:
    task_4 = input("Tippe in the password: ").strip().lower()
    if task_4 == password:
        print("You unlocked the Pc!")
        break
    print("Wrong password. Please try again")


task_5 = input("Which folder do you want to open? photos/music/messages/top_secret/documents: ").strip().lower()

if task_5 == "photos":
    print("The folder contains some old photos of you and James, but there is nothing else that interests you.")

elif task_5 == "music":
    print("You open the folder containing the old music that you and James used to listen to. You click on a song and listen to it...")
    pygame.mixer.music.load(music1)
    pygame.mixer.music.play()

elif task_5 == "top_secret":
    print("Oh no! You click on a file containing a virus. The PC is now broken!")
    print(game_over)
    quit()

elif task_5 == "documents":
    print("You open a folder filled with boring documents. Nothing special here...")

elif task_5 == "messages":
    print("You are in the right folder.")
    wait()
    print(messeag1)
    wait()
    print(messeag2)
    wait()
    print("What could that message mean? You ask yourself...")
    wait()

    meaning = "the bunker"

    while True:
        task_4 = input("Enter the password: ").strip().lower()

        if task_4 == meaning:
            print(messeag3)
            quit()

        print("No, that isn't the correct meaning of the message. Try again!")