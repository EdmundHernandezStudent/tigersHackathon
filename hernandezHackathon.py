import random

nouns =["tiger", "pirate", "Batman", "knight", "Weird Al", "Arnold", "Cheddar Cheese", "Sherlock Holmes"]
transport = ["plane", "boat", "car", "train", "spaceship", "airship", "Flintstone car", "Helicopter"]
places = ["superstore", "ocean", "backrooms", "End of the Universe", "DMV", "Atlantis", "Castle Frankenstein", "mansion"]


print("Welcome to Edmund Hernandez's Crazy Libs!")

def crazyFunc():
    randomo = int(random.uniform(0,len(nouns)))
    
    answers=["The " + nouns[randomo] + " ate a donut on an airplane",
         "You have fallen down a void with a " + nouns[randomo] + " going to the " + places[randomo],
         "The " + nouns[randomo] + " went to the " + transport[randomo],
         "The " + nouns[randomo] + " went to the " + places[randomo],
         "Somehow, " + nouns[randomo] + " destroyed a brand-new " + transport[randomo] + " at the " + places[randomo],
         "The speeding cars crashed into a strange " + transport[randomo] + " that looked like a confused " + nouns[randomo],
         "The " + transport[randomo] + " is going to " + places[randomo] + " at a super sonic speed!",
         "The " + places[randomo] + " is packed with clones of " + nouns[randomo]]

    print("")
    print(answers[randomo])
    
    #the repeater
    boolLoop = input("Would you like to make another?: y, Or exit?: n - Choose(y/n)")
    if (boolLoop == "y"):
        crazyFunc()
    else:
        exit()

crazyFunc()
