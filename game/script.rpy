# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define slot_playerName = "Cousin"

# The game starts here.

label start:

    # Enter name:

    $ slot_playerName = renpy.input("Enter name:", default='Cousin')

    menu:
        "You are enrolling as [slot_playerName]. Is that correct?"

        "Yes":
            jump s_intro

        "No":
            jump start

    # todo yes/no

    jump s_intro

label credits:
    "CREDITS"
    return

label SuperSecretMacro:
    $ throw NotImplementedError()
    # if you have the true ending for all characters:
    jump s_supersecret
    return
    
label BadEndMacro:
    $ throw NotImplementedError()
        # curtainactor == curtain (???)
        # imageevent actor badEnd with image i_event_badend 1sec fadein
        # imageevent actor badEndText with image i_event_badend_gameover 1sec fadein

        # bgm a_bgm_namcotheme then fadeout .5 secs
    return

label BattleMacro:
    $ throw NotImplementedError()



    #     # Zoom in on evil namco
    #     self.children.append(ActorEvent("ActorEvent", attrs={
    #         "target": cousin_id,
    #         "duration": 0.5,
    #     }, children=[
    #         Styles("styles", attrs={"scaleX": scalex}),
    #         Transitions("transitions", attrs={"x": cousinx})
    #     ]))

    # pass

    # Thunderclap!
    # ease out

    # Fade in evil namco robots
    # evil linear move left

    # on thunderclaps:
    # Fade in partner, right top
    # Fade in cousin, right bottom

    # Move together, fade to white
    # Fade to black
    return