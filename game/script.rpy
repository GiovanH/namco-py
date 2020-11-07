# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define slot_playerName = "Cousin"

# The game starts here.

label start:

    window show
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
    show i_sw_black as curtain zorder 15:
        alpha 0.0
        linear 1.0 alpha 1.0
    "CREDITS"
    return

define char_name_to_id = {
    "Aki Matsuo": "amazona",
    "Albatross": "albatros",
    "Anti-Bravoman": "antibravo",
    "Blue Max": "bluemax",
    "Davesprite": "davesprite",
    "Donko": "donko",
    "Galaga": "galaga",
    "Hiromi": "hiromi",
    # "Kame Crocker": "jane",
    "Jane Crocker": "jane",
    "Lolo": "lolo",
    "Meowkie": "meowkie",
    "Mr. Driller": "mrdriller",
    "Nidia": "nidia",
    "Richard Miller": "richard",
    "Taira": "taira",
    "Terezi Pyrope": "terezi",
    "Tomari": "tomari",
    "Valkyrie": "valk"
}

label SuperSecretMacro:
    $ renpy.pause()
    # if you have the true ending for all characters:
    if not persistent.got_trueend_amazona:
        return
    if not persistent.got_trueend_albatros:
        return
    if not persistent.got_trueend_antibravo:
        return
    if not persistent.got_trueend_bluemax:
        return
    if not persistent.got_trueend_davesprite:
        return
    if not persistent.got_trueend_donko:
        return
    if not persistent.got_trueend_galaga:
        return
    if not persistent.got_trueend_hiromi:
        return
    if not persistent.got_trueend_jane:
        return
    if not persistent.got_trueend_lolo:
        return
    if not persistent.got_trueend_meowkie:
        return
    if not persistent.got_trueend_mrdriller:
        return
    if not persistent.got_trueend_nidia:
        return
    if not persistent.got_trueend_richard:
        return
    if not persistent.got_trueend_taira:
        return
    if not persistent.got_trueend_terezi:
        return
    if not persistent.got_trueend_tomari:
        return
    if not persistent.got_trueend_valk:
        return
    call s_supersecret
    return
    


label BadEndMacro:
    $ renpy.pause()
    # $ raise NotImplementedError
        # curtainactor == curtain (???)
    show i_sw_black as curtain zorder 15:
        alpha 0.0
        linear 1.0 alpha 1.0

    show i_event_badend zorder 16:
        alpha 0.0
        time 1.0
        linear 1.0 alpha 1.0
    show i_event_badend_gameover zorder 17:
        alpha 0.0
        time 2.0
        linear 1.0 alpha 1.0
    $ renpy.pause(5)
    $ renpy.pause()
        # imageevent actor badEnd with image i_event_badend 1sec fadein
        # imageevent actor badEndText with image i_event_badend_gameover 1sec fadein

        # bgm a_bgm_namcotheme then fadeout .5 secs
    return
