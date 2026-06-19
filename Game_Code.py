# importet moduls
import time
import pygame

# lode music and link them
music1 = "music/black_by_pearl_jam.ogg"
pygame.init()
audio_available = True
try:
    pygame.mixer.init()
except Exception:
    print("Warning: audio device not available; music will be disabled.")
    audio_available = False


# load text files safely
def read_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: required file '{path}' not found.")
        raise SystemExit(1)

intro = read_text("story_txt/intro.txt")
knock = read_text("story_txt/knock.txt")
door_police = read_text("story_txt/door_police.txt")
chairs = read_text("story_txt/chairs.txt")
shocked = read_text("story_txt/shocked.txt")
photo_ordescription = read_text("story_txt/photo_ordescription.txt")
photo = read_text("story_txt/photo.txt")
description = read_text("story_txt/description.txt")
left = read_text("story_txt/left.txt")
go_or_bed = read_text("story_txt/go_or_bed.txt")
walk = read_text("story_txt/walk.txt")
walkpart2 = read_text("story_txt/walkpart2.txt")
walkpart3 = read_text("story_txt/walkpart3.txt")
walkpart4 = read_text("story_txt/walkpart4.txt")
walkpart5 = read_text("story_txt/walkpart5.txt")
dream = read_text("story_txt/dream.txt")
dream2 = read_text("story_txt/dream2.txt")
dream3 = read_text("story_txt/dream3.txt")
waup = read_text("story_txt/waup.txt")
waup2 = read_text("story_txt/waup2.txt")
pc1 = read_text("story_txt/pc1.txt")
messeag1 = read_text("story_txt/messeag1.txt")
messeag2 = read_text("story_txt/messeag2.txt")
messeag3 = read_text("story_txt/messeag3.txt")
game_over = read_text("story_txt/game_over.txt")


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

while task_5 not in ["photos", "music", "top_secret", "documents", "messeages"]:
    print("That folder dont exist.")

    task_5 = input(
        "Please choose: photos/music/messages/top_secret/documents:: "
    ).strip().lower()

if task_5 == "photos":
    print("The folder contains some old photos of you and James, but there is nothing else that interests you.")

elif task_5 == "music":
    print("You open the folder containing the old music that you and James used to listen to. You click on a song and listen to it...")
    task_5 = input(
        "Please choose: photos/music/messages/top_secret/documents:: "
    ).strip().lower()

    if audio_available:
        try:
            pygame.mixer.music.load(music1)
            pygame.mixer.music.play()
        except Exception:
            print(f"Could not play audio file: {music1}")


    else:
        print(f"(Audio disabled) would play: {music1}")

elif task_5 == "top_secret":
    print("Oh no! You click on a file containing a virus. The PC is now broken!")
    print(game_over)
    quit()

elif task_5 == "documents":
    print("You open a folder filled with boring documents. Nothing special here...")
    task_5 = input(
        "Please choose: photos/music/messages/top_secret/documents:: "
    ).strip().lower()




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
        task_4 = input("Enter the meaning og the messeag: ").strip().lower()

        if task_4 == meaning:
            print(messeag3)
            quit()

        print("No, that isn't the correct meaning of the message. Try again!")
        task_4 = input("Enter the meaning og the messeag: ").strip().lower()


    
