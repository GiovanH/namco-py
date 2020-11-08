define slot_pick_count_cousin = 0
# <Scene {'id': 's_cousin6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_cousin6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_cousin6"
    $ renpy.pause(1)
    # <Scene {'id': 's_cousin6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_cousin6_initialize:
        # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
        # <Events {} events ''>
        # Pass (VarEnsure)
        show i_bg_evil_namco_high as bg zorder 11 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_sw_white as white_swatch zorder 16:
            default
            alpha 0.0
        show i_battlepose_robotarmy as robotarmy zorder 12:
            default
            xpos 0.1 
            alpha 0.0
        show i_battlepose_cousin_evil as cousin zorder 13:
            default
            xpos 0.9 
            ypos 0.5 
            alpha 0.0
            xzoom 0.85 
            yzoom 0.85 

    # <BattleMacro {'name': '_1'} BattleMacro ''>
    # <ParallelEvent {'auto': True} ParallelEvent ''>
    # <Events {'kind': 'Transitions'} events ''>
    show i_bg_evil_namco_high as bg:
        # ActorEvent
        xpos 0.5 
        ypos 0.65 
        xzoom 2.0 
        yzoom 2.0 
    show i_battlepose_robotarmy as robotarmy:
        # ActorEvent
        xpos 0.5 

    $ renpy.pause(0.5)
    # <ParallelEvent {'delay': 0.5, 'auto': True} ParallelEvent ''>
    # <Events {'kind': 'events'} events ''>
    play sound "sfx/thunderclap.ogg" noloop
    show i_sw_white as white_swatch    # ActorEvent
    with flash
    $ renpy.pause(0.5)
    # <ParallelEvent {'delay': 0.5} ParallelEvent ''>
    # <Events {'kind': 'Events'} events ''>
    show i_sw_white as white_swatch    # ActorEvent
    with flash


    $ renpy.pause(2)
    # <ParallelEvent {'delay': 2, 'auto': True} ParallelEvent ''>
    # <Events {'kind': 'events'} events ''>
    show i_bg_evil_namco_high as bg:
        # ActorEvent
        # ActorEvent (Transition only)
        easeout 0.75 xpos 0.5 ypos 0.5 xzoom 1.0 yzoom 1.0 
    $ renpy.pause(0.75) # TimedPause
    show i_battlepose_robotarmy as robotarmy:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # TimedPause
    $ renpy.pause(0.75)
    # <ParallelEvent {'delay': 0.75, 'auto': True} ParallelEvent ''>
    # <Events {'kind': 'events'} events ''>
    show i_battlepose_robotarmy as robotarmy:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 1 xpos 0.1 
    $ renpy.pause(1.0) # TimedPause
    # <ParallelEvent {'auto': True} ParallelEvent ''>
    # <Events {'kind': 'events'} events ''>
    show i_sw_white as white_swatch    # ActorEvent
    with flash
    show i_battlepose_cousin_evil as cousin:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # TimedPause
    # <ParallelEvent {'kind': 'events'} ParallelEvent ''>
    # <Events {'kind': 'events'} events ''>
    show i_battlepose_robotarmy as robotarmy:
        # ActorEvent
        # ActorEvent (Transition only)
        ease 1.0 xpos 0.3 
    show i_battlepose_cousin_evil as cousin:
        # ActorEvent
        # ActorEvent (Transition only)
        ease 1.0 xpos 0.78 
    $ renpy.pause(1.0) # TimedPause
    show i_sw_white as white_swatch:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 1.0
    $ renpy.pause(2)
    # <ParallelEvent {'delay': 2} ParallelEvent ''>
    # <Events {'kind': 'ParallelEvent'} events ''>
    stop sound
    show i_sw_black as curtain:
        # ActorEvent
        alpha 1.0
    show i_sw_white as white_swatch:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 2 alpha 0.0
    stop music fadeout 2.0
    $ renpy.pause(2.0) # Text delay
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    # End battlemacro
    $ persistent.got_trueend_cousin = True
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    show i_event_cousin_badend as trueEnd zorder 23:
        default
        alpha 0.0
        linear 1 alpha 1.0
        # ShowWithAtl
        linear 1 alpha 0.0
    call SuperSecretMacro
    return