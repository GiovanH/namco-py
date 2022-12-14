# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define slot_playerName = "Cousin"

image titlecard nbgi = "credits/titlecard_nbgi_half.png"
image titlecard whatpumpkin = "credits/titlecard_whatpumpkin.png"
image titlecard shiftylook = "credits/titlecard_shiftylook.png"
image titlecard datenighto = "credits/titlecard_datenighto.png"

define slot_day_name = "Intro"

define titledissolve = Dissolve(0.9)

label splashscreen:

    # $ titlepause = 0.2
    $ titlepause = 1.2

    scene i_sw_white

    show titlecard datenighto  # with titledissolve
    $ renpy.pause(titlepause)
    hide titlecard datenighto  # with titledissolve

    show titlecard nbgi  # with titledissolve
    $ renpy.pause(titlepause)
    hide titlecard nbgi  # with titledissolve

    show titlecard shiftylook  # with titledissolve
    play sound "sfx/pacman.ogg" noloop
    $ renpy.pause(titlepause)
    hide titlecard shiftylook  # with titledissolve

    show titlecard whatpumpkin  # with titledissolve
    $ renpy.pause(titlepause)
    hide titlecard whatpumpkin  # with titledissolve

    return


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

label CreditsEvent:
    window hide
    $ renpy.pause(1.0)

    call _credits

    window show
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
    if not unlockedAll():
        return
    call s_supersecret from _call_s_supersecret
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
    $ persistent.got_truend_badend = True
    $ renpy.pause(5)
    $ renpy.pause()
        # imageevent actor badEnd with image i_event_badend 1sec fadein
        # imageevent actor badEndText with image i_event_badend_gameover 1sec fadein

        # bgm a_bgm_namcotheme then fadeout .5 secs
    return
