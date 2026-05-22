import time
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
STORY_PATH = BASE_PATH / "story_txt"

with open(STORY_PATH / "intro.txt", "r", encoding="utf-8") as file:
    intro = file.read()

with open(STORY_PATH / "knock.txt", "r", encoding="utf-8") as file:
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






    


    
    







    


def wait():
    input()



print("Welcome to Black Hollow!")
print("A Text Adventure made by TimFloClausen")
input("Press enter to start the game: ")
print(intro)

input("Press Enter to continue! ")

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

    
