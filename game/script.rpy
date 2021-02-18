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
define support = Character("")
define redHouseFound = False
define musiciansFound = False
define childSpokenTo = False
define flowersGiven = False

#characters

image shelly_happy = "Shelly_Sprites/shelly_happy.png"
image shelly_excited = "Shelly_Sprites/shelly_excited.png"
image shelly_disappointed = "Shelly_Sprites/shelly_disappointed.png"
image shelly_shame = "Shelly_Sprites/shelly_shame.png"

image mermaid_curious = "Not_Shelly_Sprites/not_shelly_curious.png"
image mermaid_sinister = "Not_Shelly_Sprites/not_shelly_sinister.png"

image florist_impressed = "Florist_Sprites/florist_impressed.png"
image florist_smile = "Florist_Sprites/florist_smile.png"

image sad_boy = "Sad_Boy_Sprites/sad_boy_idle.png"
image sad_boy_thankful = "Sad_Boy_Sprites/sad_boy_thankful.png"

image old_man = "Old_Man_Sprites/old_man_idle.png"

#backgrounds
image bg black = "bg black.jpg"
image bg road = "bg road.jpg"
image bg their_st = "bg their_st.png"
image bg wood0_0 = "bg wood0_0.png"
image bg wood0_1 = "bg wood0_1.png"
image bg wood0_2 = "bg wood0_2.png"
image bg wood1_0 = "bg wood1_0.png"
image bg wood1_1 = "bg wood1_1.png"
image bg wood1_2 = "bg wood1_2.png"
image bg beach0_1 = "bg beach0_1.png"
image bg beach0_0 = "bg beach0_0.png"
image bg beach0_2 = "bg beach0_2.png"
image bg beach1_0 = "bg beach1_0.png"
image bg beach1_1 = "bg beach1_1.png"
image bg beach1_2 = "bg beach1_2.png"
image bg city0_1 = "bg city0_1.png"
image bg city0_0 = "bg city0_0.png"
image bg city0_2 = "bg city0_2.png"
image bg city1_0 = "bg city1_0.png"
image bg city1_1 = "bg city1_1.png"
image bg city1_2 = "bg city1_2.png"
image bg cityFlowers = "bg cityFlowers.png"
image bg cityMusicians = "bg cityMusicians.png"
image bg cityRedHouse = "bg cityRedHouse.png"
image bg citySurfboardHouse = "bg citySurfboard.png"
image bg beach = "bg beach.png"

label start:

    show bg black

    support "Please turn on your audio for this game. Thank you."

    python:
        povName = renpy.input("My name is...", length=32)
        povName = povName.strip()

        if not povName:
            povName = "Spencer"
    
    pov "(It's almost Valentines Days, and I am single.)"

    pov "(I was desperate, so I downloaded a dating app called Saucer.)"

    pov "(And after weeks of swiping...)"

    app "Congratulations! Shelly likes you back!"

    pov "(Now my finger can finally take a break, and aparently someone unfortuante enough likes me back.)"

    pov "(In fact, she was unfortunate enough to text me first.)"

    show shelly_happy

    play sound "/audio/Happy_hey.mp3"

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

    hide shelly_happy

    pov "(At first, I thought it was a dream.)"

    pov "(But... it was real! I knew because my dog bit me and I felt the pain!)"

    pov "(And so we would continue talking for weeks, and finally on Valentines Day...)"

    show shelly_excited

    shelly "So... think it's time to meet up now?"

    pov "Sure, when?"

    shelly "Right now!"

    pov "(Thanks for the notice...)"

    shelly "Come meet me at the beach, ... uh I'll just speak it"

    play sound "audio/There_Street.mp3"
    shelly ""
    
    shelly "and I'll tell you where to go next"

    pov "Where is that?"

    shelly "Just past the road 200 feet away from your house. See you there!"

    hide shelly_excited

    pov "(and so I drove over to that road)"

    show bg road

    play music "/audio/city.mp3"

    pov "(Just as I got there... the road closed!)"

    pov "(and there was a drunk driver behind me, I had to get away, so I drove into a path that led to the woods.)"

    pov "Why is this happening to me..."

    stop music 

    show old_man

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
            jump woodRouteBeginning
        "Nah":
            jump streetSigns

label woodRouteBeginning:
    stop music
    play music "/audio/outside.mp3"
    show bg wood0_1:
        zoom 0.3
    oldPerson "Well, here we are!"
    pov "Thank you sir! How can I repay you?"
    oldPerson "Oh ho ho, no need"
    hide old_man
    
    pov "I should tell Shelly that I'm here."
    phone "**Rings**"
    stop music
    play sound "audio/Angry-annoyed_hey.mp3"
    show shelly_shame
    shelly "[povName]! What's taking you so long?!"
    pov "I'm at there street!"
    hide shelly_shame
    show shelly_happy
    shelly "Oh good! Now look for the red house and tell me when you get there!"
    hide shelly_happy
    phone "**beeps**"
    play music "/audio/outside.mp3"

label woodRoute0_1:
    show bg wood0_1:
        zoom 0.3
    if redHouseFound:
        pov "Theres no music anywhere!"
        show old_man
        oldPerson "Hey there, you look lost."
        pov "Are you sure this is there street?"
        oldPerson "There street? I thought you said Bear street."
        pov "..."
        hide old_man
        show bg black
        pov "(I walk back to the road.)"
        pov "(It was a long walk. I call Shelly.)"
        phone "**Rings**"
        stop music
        play sound "audio/Angry-annoyed_hey.mp3"
        show shelly_disappointed
        shelly "[povName] What do you want?"
        pov "Hey I'm really sorry, I got lost."
        shelly "Well now you can stay lost. You dumped me on our first date. Goodbye!"
        hide shelly_disappointed
        phone "**beeps**"
        pov "Well..."
        pov "Game Over"
        return
    menu:
        "Which way should I go?"

        "Forward":
            jump woodRoute1_1
        "Left":
            jump woodRoute0_0
        "Right":
            jump woodRoute0_2

label woodRoute0_0:
    show bg wood0_0:
        zoom 0.3
    menu:
        "Which way should I go?"

        "Forward":
            jump woodRoute1_0
        "Right":
            jump woodRoute0_1

label woodRoute0_2:
    show bg wood0_2
    menu:
        "Which way should I go?"

        "Forward":
            jump woodRoute1_2
        "Left":
            jump woodRoute0_1

label woodRoute1_2:
    show bg wood1_2:
        zoom 0.3
    menu:
        "Which way should I go?"

        "Backward":
            jump woodRoute0_2
        "Left":
            jump woodRoute1_1

label woodRoute1_1:
    show bg wood1_1:
        zoom 0.3
    if not redHouseFound:
        python:
            redHouseFound = True
        pov "Well here's a... red house..."
        phone "**Rings**"
        stop music
        play sound "/audio/Happy_hey.mp3"
        show shelly_happy
        shelly "Hello?"
        pov "Hey, I found the red house!"
        shelly "Nice!"
        shelly "Now listen for the music!"
        phone "**beeps**"
        hide shelly_happy
        play music "/audio/outside.mp3"

    menu:
        "Which way should I go?"

        "Backward":
            jump woodRoute0_1
        "Left":
            jump woodRoute1_0
        "Right":
            jump woodRoute1_2

label woodRoute1_0:
    show bg wood1_0:
        zoom 0.3
    menu:
        "What should I do?"

        "Go backward":
            jump woodRoute0_0
        "Go right":
            jump woodRoute1_1

label streetSigns:
    hide old_man
    pov "(I leave the woods, and I walk to where the road is, and take the walking path.)"
    pov "(And I come across two street signs)"
    show bg their_st
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
    stop music
    show shelly_shame
    play sound "audio/Angry-annoyed_hey.mp3"
    shelly "[povName]! What's taking you so long?!"
    pov "Hey I'm so sorry, could you just tell me which street..."
    hide shelly_shame
    show shelly_disappointed
    shelly "I already told you which street!! You didn't listen to me!"
    shelly "I'm done with you. Goodbye!"
    phone "**beeps**"
    hide shelly_disappointed
    pov "Welp... Game Over"
    return

label sirenRouteBeginning:
    play music "/audio/outside.mp3"
    show bg beach0_1:
        zoom 0.3
    pov "Well, this looks like the right place!"
    pov "There are a lot of beach houses here!"
    pov "I should call Shelly."
    phone "**Rings**"
    stop music
    play sound "audio/Angry-annoyed_hey.mp3"
    show shelly_shame
    shelly "[povName]! What's taking you so long?!"
    pov "I'm at there street!"
    hide shelly_shame
    show shelly_happy
    shelly "Oh good! Now look for the red house and tell me when you get there!"
    hide shelly_happy
    phone "**beeps**"
    play music "/audio/outside.mp3"

label sirenRoute0_1:
    show bg beach0_1:
        zoom 0.3
    menu:
        "Which way should I go?"

        "Forward":
            jump sirenRoute1_1
        "Left":
            jump sirenRoute0_0
        "Right":
            jump sirenRoute0_2

label sirenRoute0_0:
    show bg beach0_0:
        zoom 0.3
    menu:
        "Which way should I go?"

        "Forward":
            jump sirenRoute1_0
        "Right":
            jump sirenRoute0_1

label sirenRoute0_2:
    show bg beach0_2:
        zoom 0.3
    menu:
        "Which way should I go?"

        "Forward":
            jump sirenRoute1_2
        "Left":
            jump sirenRoute0_1

label sirenRoute1_2:
    show bg beach1_2:
        zoom 0.3
    menu:
        "Which way should I go?"

        "Backward":
            jump sirenRoute0_2
        "Left":
            jump sirenRoute1_1

label sirenRoute1_1:
    show bg beach1_1:
        zoom 0.3
    menu:
        "Which way should I go?"

        "Backward":
            jump sirenRoute0_1
        "Left":
            jump sirenRoute1_0
        "Right":
            jump sirenRoute1_2

label sirenRoute1_0:
    show bg beach1_0:
        zoom 0.3
    if not redHouseFound:
        python:
            redHouseFound = True
        pov "Well, here is the red house!"
        phone "**Rings**"
        stop music
        play sound "audio/Happy_hey.mp3"
        show shelly_happy
        shelly "Hello?"
        pov "Hey, I found the red house!"
        shelly "Nice!"
        shelly "Now listen for the music!"
        hide shelly_happy
        phone "**beeps**"
        stop music
        play music "/audio/mermaid_song.mp3"
        pov "Hey! The beach is right there!"
        pov "And I hear music coming from there!"
    else:
        play music "/audio/mermaid_song.mp3"
        pov "Well, I haven't heard music anywhere else..."
    menu:
        "What should I do?"

        "Go to the beach":
            jump sirenRouteEnding
        "Go backward":
            stop music
            jump sirenRoute0_0
        "Go right":
            stop music
            jump sirenRoute1_1

label sirenRouteEnding:
    stop music
    play music "/audio/beach.mp3"
    show bg beach
    pov "Is that her?!?!"
    stop music
    play sound "/audio/evil_hey.mp3"
    show mermaid_curious
    shelly "Hey there!"
    pov "You're a mermaid???"
    shelly "Well yes, I am. I hope that's okay with you."
    pov "No, totally fine!"
    pov "You look beautiful!"
    shelly "Thank you!"
    hide mermaid_curious
    show mermaid_sinister
    shelly "You look nice yourself."
    pov "Thank you"
    shelly "Lets go swimming!"
    
    hide mermaid_sinister
    play music "/audio/beach.mp3"
    pov "(We head into the ocean, she leads me into a very far deep end.)"
    stop music
    show bg black
    pov "(And then... the pushes me down into the water)"
    pov "(I manage to escape and swim upwards)"

    pov "Shelly! What was that?!?!"
    play music "/audio/mermaid_song.mp3"
    shelly "I'm not Shelly. Goodbye."

    pov "(And that's how I died)"
    pov "(Game Over)"
    return

label trueRouteBeginning:
    play music "/audio/city.mp3"
    show bg city0_1:
        zoom 0.3
    pov "A city?"
    pov "Sure doesn't look like a place to find a beach."
    menu:
        "What should I do?"

        "Go to there street":
            jump sirenRouteBeginning
        "Keep going":
            pov "Well, if this is it, I should tell Shelly that I'm here."
            phone "**Rings**"
            stop music
            play sound "audio/Angry-annoyed_hey.mp3"
            show shelly_shame
            shelly "[povName]! What's taking you so long?!"
            pov "I'm at there street!"
            hide shelly_shame
            show shelly_happy
            shelly "Oh good! Now look for the red house and tell me when you get there!"
            hide shelly_happy
            phone "**beeps**"
            play music "/audio/city.mp3"

label city0_1:
    if redHouseFound and musiciansFound:
        show bg cityFlowers:
            zoom 0.3
        if not childSpokenTo:
            python:
                childSpokenTo = True
            show sad_boy_idle
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
    else:
        show bg city0_1:
            zoom 0.3
    menu:
        "Which way should I go?"

        "Forward":
            jump city1_1
        "Left":
            jump city0_0
        "Right":
            jump city0_2

label city0_0:
    show bg city0_0:
        zoom 0.3
    if redHouseFound and musiciansFound and childSpokenTo:
        show bg citySurfboardHouse:
            zoom 0.3

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
        show bg cityRedHouse:
            zoom 0.3
        python:
            redHouseFound = True
        pov "Well, here is the red house!"
        stop music
        phone "**Rings**"
        play sound "audio/Happy_hey.mp3"
        show shelly_happy
        shelly "Hello?"
        pov "Hey, I found the red house!"
        shelly "Nice!"
        shelly "Now listen for the music!"
        phone "**beeps**"
        hide shelly_happy
        play music "/audio/city.mp3"
        jump city0_1
        
    show bg city0_2:
        zoom 0.3

    menu:
        "Which way should I go?"

        "Forward":
            jump city1_2
        "Left":
            jump city0_1

label city1_2:
    show bg city1_2:
        zoom 0.3
    menu:
        "Which way should I go?"

        "Backward":
            jump city0_2
        "Left":
            jump city1_1

label city1_1:
    if redHouseFound and not musiciansFound:
        show bg cityMusicians:
            zoom 0.3
        python:
            musiciansFound = True
        play music "/audio/jazz.mp3"
        
        pov "Wow! Street musicians!"
        phone "**Rings**"
        stop music
        play sound "audio/Happy_hey.mp3"
        show shelly_happy
        shelly "Hello?"
        pov "Hey, I found some street musicians, that must be where the music is coming from!"
        shelly "Yup! Thats it!"
        shelly "Now go forward and look for a house with a surfboard!"
        hide shelly_happy
        phone "**beeps**"
        jump city0_1
    show bg city1_1:
        zoom 0.3
    menu:
        "Which way should I go?"

        "Backward":
            jump city0_1
        "Left":
            jump city1_0
        "Right":
            jump city1_2

label city1_0:
    show bg city1_0:
        zoom 0.3
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
    hide sad_boy_idle
    show sad_boy_thankful
    kid "...I-I can have these? Thank you! Thank you so much!"
    hide sad_boy_thankful

    show florist_impressed
    florist "That was... very nice of you."
    florist "Don't tell my boss but... take these."

    pov "(I recieved purple flowers from the florist.)"
    hide florist_impressed
    show florist_smile

    florist "I hope you have a good day!"
    hide florist_smile
    jump flowers

label dontGiveFlowers:
    pov "Well... it's the thought that counts... I’m sorry to hear that."
    kid "..."
    hide sad_boy_idle

label flowers:
    stop music
    play sound "audio/Happy_hey.mp3"
    show shelly_excited
    phone "Hey! I can't wait for the flowers, I hope they’re purple."
    hide shelly_excited
    phone "**clicks**"
    if not flowersGiven:
        pov "Oh boy..."
    jump city0_1
    
label beach:
    show bg beach
    stop music
    play music "/audio/beach.mp3"
    pov "..."
    stop music
    play sound "audio/Happy_hey.mp3"
    show shelly_happy
    shelly "Heyyy!"
    pov "Hey!"
    pov "I brought you some flowers."
    shelly "Aw, thank you!"

    hide shelly_happy

    if not flowersGiven:
        show shelly_disappointed
        shelly "Ohh... I guess you forgot my favorite color."
        pov "Shoot..."
        pov "Game Over"
        return

    show shelly_excited

    shelly "OH! I love them! They're so pretty!"

    pov "(It was a rough journey to get here, but I made it. Our first date was a success!)"

    pov "(Apparently we hit it off pretty well after that. Many more days pass, with me spending most of them on Shelly.)"

    pov "(Well, would you look at that. This was probably the best Valentine’s Day I ever had.)"

    return


        