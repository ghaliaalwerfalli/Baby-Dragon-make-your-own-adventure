## BUG in line 147: if statment isnt recognizing any input and only else is working to break the loop.

import time

still_working = True 
while still_working:
    print('''
    *******************************************************************************
               ____ __
              { --.\  |          .)%%%)%%
               '-._\\ | (\___   %)%%(%%(%%%
                   `\\|{/ ^ _)-%(%%%%)%%;%%%
               .'^^^^^^^  /`    %%)%%%%)%%%'
              //\   ) ,  /       '%%%%(%%'
        ,  _.'/  `\<-- \<
         `^^^`     ^^   ^^

    *******************************************************************************
    ''')
    print(
        "You are a newly hatched dragon.\nExplore the world around you and live your life until your inevitable death."
    )
    print(
        "\"To progress further in the story, make your selection by pressing on number 1,number 2, number 3 or number 4 on your keyboard.\""
    )
    print("")
    print(
        "You wake up... you feel cramped. Your knees are pushed to your stomach and your head is hitting the ceiling. Panic begins to sink in. What do you do?"
    )
    yell_stretch = int(input("1) Stretch..\n2) Yell!\nYour choice is: "))
    print("")
    if yell_stretch == 1:
        print(
            "You stretch all your limbs outward. You feel the walls begin to break and finally it gives way. You look back at the egg that encased you. Congratulations! You have been born."
        )
        print("")
        print(
            "You take in your surroundings. You see the rest of the eggs in the nest.\nThe nest is in a cave which has three entrances to the caverns surrounding the nest. What do you do?"
        )
        investigate_adventure = int(
            input(
                "1) Investigate the nest?\n2) Go on an adventure.\nYour choice is: "
            ))
        print("")
        if investigate_adventure == 1:
            print(
                "While walking around the other eggs in the nest, you hear a \"thud\" from inside one of the eggs. What do you do?"
            )
            help_ignore = int(
                input("1) Help out.\n2) Ignore the sound.\nYour choice is: "))
            print("")
            if help_ignore == 1:
                print(
                    "You franticly look around for something to aid your brethren with. You spot a rock, but it doesn't seem to have much weight to it. What do you do?"
                )
                charge_rock = int(
                    input("1) Charge!\n2) Throw rock.\nYour choice is: "))
                print("")
                if charge_rock == 1:
                    print(
                        "You smash your hard skull into the side of the egg and cause a crack to appear. A foot is thrust out through the crack you made, then another. The next thing you know the egg shatters and out comes a dragon. It immediately takes flight with you and both of you fly through the right tunnel to freedom.\nLet's go on an adventure."
                    )
                else:
                    print(
                        "The rock glances off the surface of the egg and does nothing. You sit there unable to help your sibling out, starving, thirsty and can't do a thing to help.\n You died of starvation.\nGame Over."
                    )
            else:
                print(
                    "You ignored your siblings and kept going through the dark narrow nest, hoping to leave for freedom. But due to your bad judgment, you misstep and hit your head hardly on the floor.\n You died of being lonely and clumsy.\nGame Over."
                )
        else:
            print(
                "You look down each hallway trying to discern something in the darkness. The floor of the tunnel on the left appears to descend into a lower level. The one on the right seems to have a slight incline. The middle tunnel has no gradient. What do you do?"
            )
            left_right = int(
                input("1) Take left.\n2) Go to the right.\nYour choice is: "))
            print("")
            if left_right == 1:
                print(
                    "You descend into the left hallway. The air thickens with humidity and it gets cold. As you turn a corner, you see a strange green creature with pointy ears brandishing a bronze spear. What do you do?"
                )
                announce_run = int(
                    input(
                        "1) Run Away.\n2) Announce your arrival.\nYour choice is: "
                    ))
                print("")
                if announce_run == 1:
                    print(
                        "You ran away successfully and back to the fork to select your way to the right."
                    )
                else:
                    print(
                        "The strange creature jumps at your voice and yells for help. In an instant you are surrounded by ten of them. The one you figure to be the leader steps forward and says \"You DARE enter the realm of the goblins?! This is our land!\" As he finishes, he plunges his spear into your hide.\nYou died of being ambushed and killed by a goblin.\nGame Over."
                    )
            else:
                print(
                    "You see the valley bellow you. You stand on the ledge that leads to your nest wondering what to do. You see a farm in the distance. You see a caravan coming through the mountain pass that connects to the valley. The path from the pass leads to a village. What do you do?"
                )
                caravan_farm_village_valley = int(
                    input(
                        "1) Attack the caravan!\n2) Head to the farm.\n3) Go to the village.\n4) Take the path towards the valley.\nYour choice is: "
                    ))
                print("")
                if caravan_farm_village_valley == 1:
                    print(
                        "As you fly in over the caravan, you see one of the men make a small movement grabbing at his waist. The next thing you know, you hear a loud crack and a pain in your chest.\You died from a sowrd attack.\nGame Over."
                    )
                elif caravan_farm_village_valley == 2:
                    print(
                        "You settle in to eat a few cows and maybe a few pigs. You are about to eat your first one when a farmer comes running out of the nearest building holding a pitchfork towards you. You tried to take off and fly away but the farmer was faster than you.\nYou died from a pitchfork attack.\nGame Over."
                    )
                elif caravan_farm_village_valley == 3:
                    print(
                        "You arrive at the village. You land on the roof of a small building with a cross on it... weird architectural choice... A man wearing robes carrying a book comes out of the building and looks at you. What do you do?"
                    )
                    eat_watch = int(
                        input("1) Eat him!\n2) Watch him..\nYour choice is: "))
                    print("")
                    if eat_watch == 1:
                        print(
                            "You swoop down and eat him quick and easy, but the commotion (namingly the man's screams of terror) causes the rest of the village to become aware of your arrival. Everyone picks up the nearest item that could be conceivably used as a weapon and charges at you. You tried to flee away from the village but a gaurd with a bow shows up.\nYou died taking an arrow in the knee.\nGame Over."
                        )
                    else:
                        print(
                            "You just look down at the man as he fumbles through his small book. He begins to speak in a language you do not understand. You begin to feel odd. He completes a few more stanzas. Your skin begins to burn. He keeps reading. Your entire body at this point writhes in pain. He completes the last of the stanzas and you realize why there was no mother waiting for you to hatch.\nYou died of religious reasons.\nGame Over."
                        )
                else:
                    print(
                        "You fly out of the valley through the pass. You come out into a desert. You can see a small outcrop of rocks to your left and a forest in the distance. What do you do?"
                    )
                    rocks_forest = int(
                        input(
                            "1) Try the rocks.\n2) Forset looks like an interesting option.\nYour choice is: "
                        ))
                    print("")
                    if rocks_forest == 1:
                        print(
                            "You settle in and make the small rock outcrop your home. You live peacefully for many years until a drought dries up your water supply and you die of thirst\nGame Over."
                        )
                    else:
                        print(
                            "You spend several long years in the forest. You live a happy, simple life away from the hazardous human species and die of old age in your sleep.\nOld, Fat and Happy little dragon boy.\nGame Over."
                        )
    else:
        print(
            "You open your mouth to yell. As soon as you do so, however, your lungs are filled with an ungodly fluid which only accelerates your spiral into insanity.\nYou died of losing your mind.\nGame Over."
        )

    game_exit_choice = input("Do you want to continue playing? [Y/n] ").lower 
    if game_exit_choice == 'y': 
        print("starting over in 4 seconds...")
        time.sleep(4)
    else:
        print("Thank you for playing the game :)")
        still_working = False

