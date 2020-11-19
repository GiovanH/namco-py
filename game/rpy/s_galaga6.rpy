define slot_pick_count_galaga = 0
# <Scene scene {'id': 's_galaga6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_galaga6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_galaga6"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_galaga6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_galaga6_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        # Pass (VarEnsure)
        show i_bg_evil_namco_high as bg zorder 11 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_sw_black as curtain2 zorder 9:
            default
            alpha 0.0
        show i_sw_white as white_swatch zorder 16:
            default
            alpha 0.0
        show i_battlepose_robotarmy as robotarmy zorder 12:
            default
            xpos 0.1 
            alpha 0.0
        show i_battlepose_galaga as cousin zorder 13:
            default
            xpos 0.9 
            ypos 0.5 
            alpha 0.0
            xzoom 0.75 
            yzoom 0.75 
        show i_galaga_default as galaga zorder 12:
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

    if slot_pick_count_galaga <= 1:
        # <IfLTE IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_galaga}', 'name': '_1', 'rvalue': '1', 'kind': 'IfLTE'} ''>
        label s_galaga6__1:
            # <IfLTE IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_galaga}', 'name': '_1', 'rvalue': '1', 'kind': 'IfLTE'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_galaga_default as cousin
    # <BattleMacro BattleMacro {'name': '_2', 'kind': 'BattleMacro'} ''>
    window hide None
    # <ParallelEvent ParallelEvent {'auto': True, 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bg_evil_namco_high as bg:
        # ActorEvent
        xpos 0.5 
        ypos 0.65 
        xzoom 2.0 
        yzoom 2.0 
    show i_battlepose_robotarmy as robotarmy:
        # ActorEvent
        xpos 0.5 

    $ renpy.pause(0.5) # ParallelEvent Delay
    # <ParallelEvent ParallelEvent {'delay': 0.5, 'auto': True, 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/thunderclap.ogg" noloop
    show i_sw_white as white_swatch    # ActorEvent
    with flash
    $ renpy.pause(0.5) # ParallelEvent Delay
    # <ParallelEvent ParallelEvent {'delay': 0.5, 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_white as white_swatch    # ActorEvent
    with flash


    $ renpy.pause(2) # ParallelEvent Delay
    # <ParallelEvent ParallelEvent {'delay': 2, 'auto': True, 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bg_evil_namco_high as bg:
        # ActorEvent
        # ActorEvent (Transition only)
        easeout 0.75 xpos 0.5 ypos 0.5 xzoom 1.0 yzoom 1.0 
    $ renpy.pause(0.75, hard=True) # TimedPause
    show i_battlepose_robotarmy as robotarmy:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75, hard=True) # TimedPause
    $ renpy.pause(0.75) # ParallelEvent Delay
    # <ParallelEvent ParallelEvent {'delay': 0.75, 'auto': True, 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_battlepose_robotarmy as robotarmy:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 1 xpos 0.1 
    $ renpy.pause(1.0, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'auto': True, 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_white as white_swatch    # ActorEvent
    with flash
    show i_galaga_default as cousin:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_battlepose_robotarmy as robotarmy:
        # ActorEvent
        # ActorEvent (Transition only)
        ease 1.0 xpos 0.3 
    show i_galaga_default as cousin:
        # ActorEvent
        # ActorEvent (Transition only)
        ease 1.0 xpos 0.78 
    $ renpy.pause(1.0, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_white as white_swatch:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5, hard=True) # TimedPause
    # = Battlemacro contents
    # <ParallelEvent ParallelEvent {'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    # <Events events {'kind': 'events'} ''>
    hide robotarmy
    show i_bg_school_front as bg zorder 0    # ActorEvent
    show i_galaga_default as galaga zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        alpha 1.0
        xpos 0.8 
        ypos 0.5 
    show i_cousin_default_neutral as cousin zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.3 
        ypos 0.5 

    # - end battlemacro contents
    $ renpy.pause(2) # ParallelEvent Delay
    # <ParallelEvent ParallelEvent {'delay': 2, 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    stop sound
    show i_sw_black as curtain:
        # ActorEvent
        alpha 1.0
    show i_sw_white as white_swatch:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 2 alpha 0.0
    stop music fadeout 2.0
    $ renpy.pause(2.0, hard=True) # Text delay
    # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
    # End battlemacro
    if slot_pick_count_galaga <= 1:
        call BadEndMacro
    # <NormalEndMacro NormalEndMacro {'cousinX': '-5%', 'name': '_4', 'partnerActor': 'galaga', 'partnerImage': '@i_galaga_default', 'runCredits': 'true', 'kind': 'NormalEndMacro'} ''>
    # <ParallelEvent ParallelEvent {'auto': True, 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin zorder 3:
        # ActorEvent
        xpos 0.45 
    show i_galaga_default as galaga zorder 2:
        # ActorEvent
        xpos 0.15 
    show i_pacman_left as pacman zorder 2:
        # ActorEvent
        xpos 0.8 
        alpha 1.0
    t_ch_pacman "Thank you students for saving me! I thought I was a goner!" # @t_com00.00 self.block='Last'
    show i_sw_black as curtain:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 0.0
    t_ch_cousin "Thank: YOU: Pac-Man. We were only able to do it, because we were true to ourselves!" # @t_com01.00 self.block='NoAuto'
    show i_sw_black as curtain:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 1.0
    # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'auto': False, 'kind': 'TextEvent'} ''>
    $ AudioEvent('music', 1.0, 0.0)
    call CreditsEvent
    if slot_pick_count_galaga >= 3:
        # <IfGTE IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_galaga}', 'name': '_5', 'rvalue': '3', 'kind': 'IfGTE'} ''>
        label s_galaga6__5:
            # <IfGTE IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_galaga}', 'name': '_5', 'rvalue': '3', 'kind': 'IfGTE'} ''>
            # <Events events {'kind': 'events'} ''>
            $ persistent.got_trueend_galaga = True
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_pacman_left as pacman:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_digdug_left as digdug:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_galaga_default as galaga:
                # ShowWithAtl
                linear 0.5 xpos 0.8 
            show i_cousin_default_grin as cousin:
                # ShowWithAtl
                linear 0.5 xpos 0.3 
            show i_sw_black as curtain:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin_blush as cousin
            with Dissolve(0.5)
            t_ch_cousin "We make a great team!" # @t_sgalaga625.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin_blush as cousin:
                # ShowWithAtl
                linear 2 xpos 0.5 
            show i_galaga_default as galaga:
                # ShowWithAtl
                linear 2 xpos 0.5 
            show i_sw_black as curtain2:
                # ShowWithAtl
                linear 0.75 alpha 1.0
            play sound ["<silence .65>", "sfx/kiss2.ogg"]
            extend "{w=2.0}{nw}"
            t_ch_galaga "{smallcaps}Oh, [slot_playerName]. We sure do.{/smallcaps}" # @t_sgalaga626.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_sw_black as curtain zorder 22:
                # ShowWithAtl
                linear 1 alpha 1.0
            $ global_got_trueend_galaga = True
            $ renpy.pause(1.0, hard=True) # TimedPause
    return