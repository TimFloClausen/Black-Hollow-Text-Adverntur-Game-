print("Welcome to Black Hollows!")
print("A Text Adventure made by TimFloClausen")
input("Press Enter to continue... ")
print("""
══════════════════════════════════════
        BLACK HOLLOWS - INTRO
══════════════════════════════════════
Welcome to Black Hollows.
A small town in the north of the United Kingdom.
Run-down, remote and rainy, surrounded by forests
and old stone houses.
Black Hollows has:
- an old elementary school, built after World War II
- abandoned bunkers from World War II
- an old atomic bunker renewed during the Cold War
- a grocery store
- four pubs
- a dilapidated cinema
- a gas station called "Gips"
You are Thomas Bruce.
Black Hollows is your hometown, and you are the
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
    exit()

input("""

      Mr Potter, the local police officer, and his partner are standing in front of your door.
"Good morning, Mr Bruce. Sorry for the disturbance at this early hour.
We need to inform you that your brother is dead.
A woman found his body in the forest near the old atomic bunker. Can we come in and ask you some questions?"
""" )
    
print("""

You are shocked. Your beloved brother James seems to be dead.
You haven't seen him since the burial of your father.
He left the town and went to Birmingham, like you wanted to do as well...
But why was he in Black Hollows?
And why did he die?
And how?
So many questions are going through your head.
""")