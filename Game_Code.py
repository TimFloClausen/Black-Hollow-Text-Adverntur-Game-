print("Welcome to Black Hollow!")
print("A Text Adventure made by TimFloClausen")
input("Press Enter to continue... ")
print("""
══════════════════════════════════════
        BLACK HOLLOW - INTRO
══════════════════════════════════════
Welcome to Black Hollow.
A small town in the north of the United Kingdom.
Run-down, remote and rainy, surrounded by forests
and old stone houses.
Black Hollow has:
- an old elementary school, built after World War II
- abandoned bunkers from World War II
- an old atomic bunker renewed during the Cold War
- a grocery store
- four pubs
- a dilapidated cinema
- a gas station called "Gips"
You are Thomas Bruce.
Black Hollow is your hometown, and you are the
owner of "Gips".
You inherited the gas station from your father,
who died of cancer last year.
You once wanted to leave this town and move to
Birmingham.
But you could never bring yourself to close the
gas station.
So...
you stayed.
""")
input("Press Enter to start the story... ")
print("""Knock, knock — you wake up. Your head is pounding.
It feels like tiny creatures inside your skull are hitting it with hammers.
You know why you have such pain: a big hangover from last night at the pub.
Someone is knocking at the door.
The bell is broken, so the person has to knock on the old red door of the apartment you inherited from your father.
""")
task_1 = input("What do you want to do first? Open the door or take a pill? (door/pills): ").strip().lower()

if task_1 == "door":
    print("You open the door. Two police officers are standing in front of you.")
elif task_1 == "pills":
    print("You go to the bathroom, take a paracetamol, and then open the door.")
    print("Two police officers are still waiting outside.")
else:
    print("I didn't understand that. Please choose 'door' or 'pills'.")

input("""

Mr Potter, the local police officer, and his partner are standing in front of your door.
"Good morning, Mr Bruce. Sorry for the disturbance at this early hour.
We need to inform you that your brother is dead.
A woman found his body in the forest near the old atomic bunker. Can we come in and ask you some questions?"
""")
    
print("""

You are shocked. Your beloved brother James seems to be dead.
You haven't seen him since the burial of your father.
He left the town and went to Birmingham, like you wanted to do as well...
But why was he in Black Hollow?
And why did he die?
And how?
So many questions are going through your head.
""")

input("""

You let the police officer into your apartment. You point to the chairs in the kitchen and say that the both officers can take a seat.
Two small wooden chairs.
Your initials are carved into the backrest: T + J.
The paint is faded, but still visible. You and your brother painted them when you were children.
""")

print("""The police officer asks you some questions. You can't remember much after you answer them.
      After half an hour they are finished.
      Potter looks at you seriously in the eyes and asks: When we found the body of James,
        we saw something really strange. On his body was a photo of him, I could show you,
      but I want to tell you that it's really disturbing and it affects people in general if they see
      the dead body of their relatives or friends...
      So do you want to see the photo or just have it described?""")

task_2 = input("Do you want to see a picture or only a description? (photo/description) ")

if task_2 == "photo":
    print("""Potter silently hands you the photo.
At first you don't understand what you're seeing.
Then you realize it is James.
His skin has a strange color.
Not pale.
Not rotten.
Green.
A deep, unnatural green.
Like something inside his body had changed.""")

elif task_2 == "description":
     print("""Potter beginn to speak:
At first we didn't understand what we was seeing.
Then we realize it was James.
His skin had a strange color.
Not pale.
Not rotten.
Green.
A deep, unnatural green.
Like something inside his body had changed.""")
    
else:
    print("I didn't understand that. Please choose 'door' or 'pills'.")
