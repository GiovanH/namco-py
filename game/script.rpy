# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python in st_slot:
    pass

# The game starts here.

label start:

    # Enter name:

    $ st_slot.playerName = renpy.input("Enter name:", default='Cousin')

    menu:
        "You are enrolling as [st_slot.playerName]. Is that correct?"

        "Yes":
            jump s_intro

        "No":
            jump start

    # todo yes/no

    jump s_intro
