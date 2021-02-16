# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povName]")
define shelly = Character("Shelly")
define child = Character("Child")
define oldPerson = Character("Old Person")
define app = Character("App")
define phone = Character("Phone")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    app "Congratulations! Shelly likes you back!"

    shelly "Heyyy. What's your name?"

    python:
        povName = renpy.input("My name is...", length=32)
        povName = povName.strip()

        if not povName:
            povName = "Spencer"
        
    pov "My name is [povName]!"

    pov "(Why is she asking for my name? It's in my profile!)"

    shelly "Nice to meet you [povName]!"

    shelly "My name is Shelly!"

    pov "(I know)"

    pov "Nice to meet you Shelly! So what brings you to my profile?"

    shelly "Your dog! She's so cute!"

    shelly "Also could you tell me about the novel you're writing?"

    pov "Aw thank you! And sure!"

    pov "(And so we would continue talking for weeks, and finally on Valentines Day...)"

    shelly "Wanna meet up?"

    pov "Sure when?"

    shelly "Right now!"

    pov "(thanks for the notice)"

    shelly "Come meet me at the beach, go to there street and I'll tell you where to go next"

    pov "Where is that?"

    shelly "Just past the highway 200 feet away from your house. See you there!"

    shelly "(hangs up)"

    pov "(and so I drove over to that highway)"

    pov "(and just as I got there... the highway closed)"

    pov "(and there was a drunk driver behind me, I had to get away, so I drove into a path that led to the woods.)"

    pov "Why is this happening to me..."

    oldPerson "Hello there!"

    menu:
        "I respond:"

        "Who are you?":
            jump oldPersonContinue
        "General Kenobi!":
            jump oldPersonSWFan

label oldPersonSWFan:
    oldPerson "Hahaha! I see you're a man of culture!"

label oldPersonContinue:
    oldPerson "I'm just your usual old hiker"
    oldPerson "So are you lost?"
    menu:
        "I respond:"

        "Yes":
            jump lost
        "No":
            jump followedByDrunkDriver

label followedByDrunkDriver:
    pov "Nah, I just hid my car here because a drunk driver was following me."
    pov "But, I need to get somewhere past the bridge."
    oldPerson "Oh, I see"
    
label lost:
    oldPerson "Where are you trying to go?"
    menu:
        "I respond:"

        "There street":
            jump lostContinued
        "Their street":
            jump lostContinued
            
label lostContinued:
    oldPerson "Oh! I was just there!"

    oldPerson "I'll bring you there"

    menu:
        "What should I do?"

        "Go with him":
            jump deathRouteBeginning
        "Nah":
            jump streetSigns

label deathRouteBeginning:
    pov "Placeholder"
    return

label streetSigns:
    pov "(I leave the woods, and I walk to where the highway is, and take the walking path.)"
    pov "(And I come across two street signs)"
    pov "(Couldn't she have been more specific??)"
    menu:
        "Where should I go?"

        "There street":
            jump sirenRouteBeginning
        "Their street":
            jump trueRouteBeginning
        "Call Shelly":
            jump callShelly

label callShelly:
    phone "**Rings**"
    shelly "[povName]! What's taking you so long?!"
    pov "Hey I'm so sorry, could you just tell me which street..."
    shelly "I already told you which street!! You didn't listen to me!"
    shelly "I'm done with you. Goodbye!"
    phone "**beeps**"
    pov "Welp... Game Over"
    return

label sirenRouteBeginning:
    pov "Well, this looks like the right place!"
    pov "There are a lot of beach houses here!"
    pov "I should call Shelly."
    phone "**Rings**"
    shelly "[povName]! What's taking you so long?!"
    pov "I'm at there street!"
    shelly "Oh good! Now look for the red house and tell me when you get there!"
    phone "**beeps**"

label sirenRoute0_1:
    menu:
        "Which way should I go?"

        "Forward":
            jump sirenRoute1_1
        "Left":
            jump sirenRoute0_0
        "Right":
            jump sirenRoute0_2

label sirenRoute0_0:
    menu:
        "Which way should I go?"

        "Forward":
            jump sirenRoute1_0
        "Right":
            jump sirenRoute0_1

label sirenRoute0_2:
    menu:
        "Which way should I go?"

        "Forward":
            jump sirenRoute1_2
        "Left":
            jump sirenRoute0_1

label sirenRoute1_2:
    menu:
        "Which way should I go?"

        "Backward":
            jump sirenRoute0_2
        "Left":
            jump sirenRoute1_1

label sirenRoute1_1:
    menu:
        "Which way should I go?"

        "Backward":
            jump sirenRoute0_1
        "Left":
            jump sirenRoute1_0
        "Right":
            jump sirenRoute1_2

label sirenRoute1_0:
    pov "Placeholder"
    return

label trueRouteBeginning:
    pov "Placeholder"
    return

        