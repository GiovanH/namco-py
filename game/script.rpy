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
