# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define slot = renpy.python.StoreModule({})

# The game starts here.

label start:

    # Enter name.

    $ slot.playerName = renpy.input("prompt", default='Cousin')

    # You are enrolling as Name. Is that correct?

    jump s_intro
