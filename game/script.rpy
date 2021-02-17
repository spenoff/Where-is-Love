# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povName]")
define shelly = Character("Shelly")
define kid = Character("Child")
define oldPerson = Character("Old Person")
define florist = Character("Florist")
define app = Character("App")
define phone = Character("Phone")
define redHouseFound = False
define musiciansFound = False
define childSpokenTo = False
define flowersGiven = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    python:
        povName = renpy.input("My name is...", length=32)
        povName = povName.strip()

        if not povName:
            povName = "Spencer"
    
    pov "(It's almost Valentines Days, and I am single.)"

    pov "(I was desparate, so I downloaded a dating app called Saucer.)"

    pov "(And after weeks of swiping...)"

    app "Congratulations! Shelly likes you back!"

    pov "(Now my finger can finally take a break, and aparently someone unfortuante enough likes me back.)"

    pov "(In fact, she was unfortunate enough to text me first.)"

    shelly "Heyyy. What's your name?"
        
    pov "My name is [povName]!"

    pov "(Why is she asking for my name? It's in my profile!)"

    shelly "Nice to meet you [povName]!"

    shelly "My name is Shelly!"

    pov "(I know.)"

    pov "Nice to meet you Shelly!"

    shelly "Your dog is so cute!"

    pov "Aw thank you!"

    pov "(She's probably just interested in my dog, but lets see how this goes.)"

    shelly "Also could you tell me about the novel you're writing?"

    pov "Sure!"

    pov "(So she isn't just interested in my dog... nice to know.)"

    pov "(At first, I thought it was a dream.)"

    pov "(But... it was real! I knew because my dog bit me and I felt the pain!)"

    pov "(And so we would continue talking for weeks, and finally on Valentines Day...)"

    shelly "So... think it's time to meet up now?"

    pov "Sure, when?"

    shelly "Right now!"

    pov "(Thanks for the notice...)"

    shelly "Come meet me at the beach, go to there street and I'll tell you where to go next"

    pov "Where is that?"

    shelly "Just past the highway 200 feet away from your house. See you there!"

    pov "(and so I drove over to that highway)"

    pov "(and just as I got there... the highway closed!)"

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
    if not redHouseFound:
        python:
            redHouseFound = True
        pov "Well, here is the red house!"
        phone "**Rings**"
        shelly "Hello?"
        pov "Hey, I found the red house!"
        shelly "Nice!"
        shelly "Now listen for the music!"
        phone "**beeps**"
        pov "Hey! The beach is right there!"
        pov "And I hear music coming from there!"
    else:
        pov "Well, I haven't heard music anywhere else..."
    menu:
        "What should I do?"

        "Go to the beach":
            jump sirenRouteEnding
        "Go backward":
            jump sirenRoute0_0
        "Go right":
            jump sirenRoute1_1

label sirenRouteEnding:
    pov "Is that her?!?!"
    shelly "Hey there!"
    pov "You're a mermaid???"
    shelly "Well yes, I am. I hope that's okay with you."
    pov "No, totally fine!"
    pov "You look beautiful!"
    shelly "Thank you!"
    shelly "You look nice yourself."
    pov "Thank you"
    shelly "Lets go swimming!"

    pov "(We head into the ocean, she leads me into a very far deep end.)"
    pov "(And then... the pushes me down into the water)"
    pov "(I manage to escape and swim upwards)"

    pov "Shelly! What was that?!?!"
    shelly "I'm not Shelly. Goodbye."

    pov "(And that's how I died)"
    pov "(Game Over)"
    return

label trueRouteBeginning:
    pov "A city?"
    pov "Sure doesn't look like a place to find a beach."
    menu:
        "What should I do?"

        "Go to there street":
            jump sirenRouteBeginning
        "Keep going":
            pov "Well, if this is it, I should tell Shelly that I'm here."
            phone "**Rings**"
            phone "**Rings**"
            shelly "[povName]! What's taking you so long?!"
            pov "I'm at there street!"
            shelly "Oh good! Now look for the red house and tell me when you get there!"
            phone "**beeps**"

label city0_1:
    if redHouseFound and musiciansFound and not childSpokenTo:
        python:
            childSpokenTo = True
        kid "..."
        pov "Hey there... are you okay."
        kid "My dad shot my dog... we had to bury him by our cabin..."
        kid "I was going to give flowers to him but... I have no money"
        pov "I was going to give these flowers to Shelly but..."

        menu:
            "What should I do?"

            "Give the poor kid the flowers":
                jump giveFlowers
            "These are for Shelly":
                jump dontGiveFlowers
    menu:
        "Which way should I go?"

        "Forward":
            jump city1_1
        "Left":
            jump city0_0
        "Right":
            jump city0_2

label city0_0:
    if redHouseFound and musiciansFound and childSpokenTo:
        pov "Well, heres the house with the surfboard!"
        pov "The beach is right behind it? Weird."
        pov "Well here we go. [povName], you got this."
        jump beach

    menu:
        "Which way should I go?"

        "Forward":
            jump city1_0
        "Right":
            jump city0_1

label city0_2:
    if not redHouseFound:
        python:
            redHouseFound = True
        pov "Well, here is the red house!"
        phone "**Rings**"
        shelly "Hello?"
        pov "Hey, I found the red house!"
        shelly "Nice!"
        shelly "Now listen for the music!"
        phone "**beeps**"
        jump city0_1
        

    menu:
        "Which way should I go?"

        "Forward":
            jump city1_2
        "Left":
            jump city0_1

label city1_2:
    menu:
        "Which way should I go?"

        "Backward":
            jump city0_2
        "Left":
            jump city1_1

label city1_1:
    if redHouseFound and not musiciansFound:
        python:
            musiciansFound = True
        pov "Wow! Street musicians!"
        phone "**Rings**"
        shelly "Hello?"
        pov "Hey, I found some street musicians, that must be where the music is coming from!"
        shelly "Yup! Thats it!"
        shelly "Now go forward and look for a house with a surfboard!"
        phone "**beeps**"
        jump city0_1
    menu:
        "Which way should I go?"

        "Backward":
            jump city0_1
        "Left":
            jump city1_0
        "Right":
            jump city1_2

label city1_0:
    menu:
        "Which way should I go?"

        "Backward":
            jump city0_1
        "Right":
            jump city1_1

label giveFlowers:
    python:
        flowersGiven = True
    pov "(I offer him the flowers.)"
    kid "...THANK YOU THANK YOU THANK YOU"

    florist "That was... very nice of you."
    florist "Don't tell my boss but... take these."

    pov "(I recieved purple flowers from the florist.)"

    florist "I hope you have a good day!"
    jump flowers

label dontGiveFlowers:
    pov "Well... its the thought that counts..."
    kid "..."

label flowers:
    phone "Hey! I can't wait for the flowers, I hope they’re purple."
    phone "**clicks**"
    if not flowersGiven:
        pov "Oh boy..."
    jump city0_1
    
label beach:
    shelly "Heyyy"
    pov "Hey!"
    pov "I brought you some flowers."
    shelly "aw thank you!"

    if not flowersGiven:
        shelly "ohh... I guess you forgot my favorite color."
        pov "shoot..."
        pov "Game Over"
        return

    shelly "OH! I love them!"

    pov "And we went on to have a good date."

    pov "And we had many more, and we lived a happy life together"

    return


        