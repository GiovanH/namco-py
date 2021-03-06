define slot_pick_count_nidia = 0
# <Scene scene {'id': 's_nidia6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_nidia6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_nidia6"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_nidia6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_nidia6_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
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
        show i_battlepose_nidia as cousin zorder 13:
            default
            xpos 0.9 
            ypos 0.5 
            alpha 0.0
            xzoom 1.0 
            yzoom 1.0 
        show i_nidia_akimbo_happy as nidia zorder 12:
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

    if slot_pick_count_nidia <= 1:
        # <IfLTE IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_nidia}', 'name': '_1', 'rvalue': '1', 'kind': 'IfLTE'} ''>
        label s_nidia6__1:
            # <IfLTE IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_nidia}', 'name': '_1', 'rvalue': '1', 'kind': 'IfLTE'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_battlepose_cousin_normal as cousin:
                # ShowWithAtl
                linear 0.5 xzoom 0.75 
                linear 0.5 yzoom 0.75 
                # ShowWithAtl
                linear 0.5 xpos 0.9 
                linear 0.5 ypos 0.75 
            $ renpy.pause(1.0, hard=True) # TimedPause
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
    show i_battlepose_cousin_normal as cousin:
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
    show i_battlepose_cousin_normal as cousin:
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
    show i_nidia_akimbo_happy as nidia zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.7 
        ypos 0.5 
        alpha 1.0
    show i_cousin_energetic_grin as cousin zorder 2:
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
    if slot_pick_count_nidia <= 1:
        call BadEndMacro
    # <NormalEndMacro NormalEndMacro {'comparison': '${slot:pick_count_nidia} == 2', 'name': '_4', 'partnerActor': 'nidia', 'partnerImage': '@i_nidia_resolute_happy', 'runCredits': 'true', 'kind': 'NormalEndMacro'} ''>
    # <ParallelEvent ParallelEvent {'auto': True, 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin zorder 3:
        # ActorEvent
        xpos 0.35 
    show i_nidia_resolute_happy as nidia zorder 2:
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
    if slot_pick_count_nidia >= 3:
        # <IfGTE IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_nidia}', 'name': '_5', 'rvalue': '3', 'kind': 'IfGTE'} ''>
        label s_nidia6__5:
            # <IfGTE IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_nidia}', 'name': '_5', 'rvalue': '3', 'kind': 'IfGTE'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_resolute_happy as nidia:
                # ShowWithAtl
                linear 0.5 xpos 0.7 
                linear 0.5 ypos 0.5 
            show i_cousin_energetic_grin as cousin:
                # ShowWithAtl
                linear 0.5 xpos 0.3 
                linear 0.5 ypos 0.5 
            $ renpy.pause(1.0, hard=True) # TimedPause
            show i_sw_black as curtain:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_akimbo_happy as nidia
            show i_cousin_energetic_grin as cousin
            t_ch_cousin "WE DID IT!" # @t_snidia637.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_surprise as cousin
            extend " You were amazing, Nidia!" # @t_snidia637.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_akimbo_happy as nidia
            t_ch_nidia "Thanks [slot_playerName]... It was all thanks to you." # @t_snidia638.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "I watched you during the fight... Thinking about your words." # @t_snidia639.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_resolute_happy as nidia:
                xzoom -1.0 
            show i_cousin_energetic_neutral as cousin
            t_ch_nidia "I AM free to choose. I want to throw off the chains of destiny... But I don't want to make choices because I'm afraid of destiny either." # @t_snidia640.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            t_ch_cousin "Nidia... What are you saying?" # @t_snidia641.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_resolute_happy_blush as nidia:
                # ShowWithAtl
                linear 0.5 xpos 0.6 
            extend "{w=0.5}{nw}"
            t_ch_nidia "Take my hand, [slot_playerName]..." # @t_snidia642.00 self.block='Last'
            show i_sw_black as curtain:
                # ShowWithAtl
                linear 0.5 alpha 1.0
            # Credits music -- NOT PLAYING (in screen)
            call CreditsEvent
            show i_event_nidia_ending as trueEnd zorder 18:
                default
                alpha 0.0
                linear 1 alpha 1.0
            # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            $ persistent.got_trueend_nidia = True
            show i_event_nidia_ending as trueEnd:
                # ShowWithAtl
                linear 1 alpha 0.0
            $ renpy.pause(1.0, hard=True) # TimedPause
    return