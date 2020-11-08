define slot_pick_count_richard = 0
# <Scene {'id': 's_richard6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_richard6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_richard6"
    $ renpy.pause(1)
    # <Scene {'id': 's_richard6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_richard6_initialize:
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
        show i_battlepose_cousin_normal as cousin zorder 13:
            default
            xpos 0.9 
            ypos 0.75 
            alpha 0.0
            xzoom 0.75 
            yzoom 0.75 
        show i_battlepose_miller as miller zorder 12:
            default
            xpos 0.9 
            ypos 0.38 
            xzoom 0.75 
            yzoom 0.75 
            alpha 0.0
        show i_pacman_left as pacman zorder 2:
            default
            xpos 0.95 
            alpha 0.0
        show i_digdug_left as digdug zorder 3:
            default
            xpos 0.9 
            alpha 0.0

    # <BattleMacro {'name': '_1', 'partnerActor': 'miller'} BattleMacro ''>
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
    show i_battlepose_miller as miller:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # TimedPause
    # <ParallelEvent {'auto': True} ParallelEvent ''>
    # <Events {'kind': 'events'} events ''>
    show i_sw_white as white_swatch    # ActorEvent
    with flash
    show i_battlepose_cousin_normal as cousin:
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
    show i_battlepose_cousin_normal as cousin:
        # ActorEvent
        # ActorEvent (Transition only)
        ease 1.0 xpos 0.78 
    show i_battlepose_miller as miller:
        # ActorEvent
        # ActorEvent (Transition only)
        ease 1.0 xpos 0.7 
    $ renpy.pause(1.0) # TimedPause
    show i_sw_white as white_swatch:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 1.0
    # = Battlemacro contents
    # <ParallelEvent {'kind': 'events'} ParallelEvent ''>
    # <Events {'kind': 'Annotation'} events ''>
    # <Events {} events ''>
    hide robotarmy
    show i_bg_school_front as bg zorder 0    # ActorEvent
    show i_miller_aliens_serious as miller zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.7 
        ypos 0.5 
    show i_cousin_default_neutral as cousin zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.3 
        ypos 0.5 

    # - end battlemacro contents
    $ renpy.pause(2)
    # <ParallelEvent {'delay': 2} ParallelEvent ''>
    # <Events {'kind': 'Annotation'} events ''>
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
    if slot_pick_count_richard <= 1:
        call BadEndMacro
    # <NormalEndMacro {'cousinX': '-5%', 'name': '_3', 'partnerActor': 'miller', 'partnerImage': '@i_miller_standing_laugh'} NormalEndMacro ''>
    # <ParallelEvent {'auto': True} ParallelEvent ''>
    # <Events {'kind': 'events'} events ''>
    show i_cousin_energetic_grin as cousin zorder 3:
        # ActorEvent
        xpos 0.45 
    show i_miller_standing_laugh as miller zorder 2:
        # ActorEvent
        xpos 0.15 
    show i_pacman_left as pacman zorder 2:
        # ActorEvent
        xpos 0.8 
        alpha 1.0
    t_ch_pacman "Thank you students for saving me! I thought I was a goner!" # @t_com00.00 self.block='Last'
    show i_sw_black as curtain    # ActorEvent
    t_ch_cousin "Thank: YOU: Pac-Man. We were only able to do it, because we were true to ourselves!" # @t_com01.00 self.block='NoAuto'
    show i_sw_black as curtain    # ActorEvent
    # Blank text event <TextEvent {'char': '', 'text': '', 'auto': False} TextEvent ''>
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    if slot_pick_count_richard >= 3:
        # <IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_richard}', 'name': '_6', 'rvalue': '3'} IfGTE ''>
        label s_richard6__6:
            # <IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_richard}', 'name': '_6', 'rvalue': '3'} IfGTE ''>
            # <Events {} events ''>
            $ persistent.got_trueend_richard = True
            show i_event_miller_ending as trueEnd zorder 18:
                default
                alpha 0.0
                linear 1 alpha 1.0
            # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_sw_black as curtain:
                # ShowWithAtl
                linear 0.5 alpha 0.0
                # ShowWithAtl
                linear 1 alpha 1.0
            $ renpy.pause(1.0) # TimedPause
    return