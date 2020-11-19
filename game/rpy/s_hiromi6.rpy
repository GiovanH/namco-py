define slot_pick_count_hiromi = 0
# <Scene scene {'id': 's_hiromi6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_hiromi6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_hiromi6"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_hiromi6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_hiromi6_initialize:
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
        show i_battlepose_cousin_normal as cousin zorder 13:
            default
            xpos 0.9 
            ypos 0.75 
            alpha 0.0
            xzoom 0.75 
            yzoom 0.75 
        show i_battlepose_hiromi as hiromi zorder 12:
            default
            xpos 0.9 
            ypos 0.38 
            xzoom 0.65 
            yzoom 0.65 
            alpha 0.0
        show i_tobi_stand_grin as toby zorder 2:
            default
            xpos 0.9 
            alpha 0.0

    if slot_pick_count_hiromi <= 1:
        # <IfLTE IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_hiromi}', 'name': '_1', 'rvalue': '1', 'kind': 'IfLTE'} ''>
        label s_hiromi6__1:
            # <IfLTE IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_hiromi}', 'name': '_1', 'rvalue': '1', 'kind': 'IfLTE'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_battlepose_hiromi_notoby as hiromi
    # <BattleMacro BattleMacro {'name': '_2', 'partnerActor': 'hiromi', 'kind': 'BattleMacro'} ''>
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
    show i_battlepose_hiromi_notoby as hiromi:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75, hard=True) # TimedPause
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
    show i_battlepose_hiromi_notoby as hiromi:
        # ActorEvent
        # ActorEvent (Transition only)
        ease 1.0 xpos 0.7 
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
    show i_hiromi_crossed_serious as hiromi zorder 3:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        alpha 1.0
        xpos 0.7 
        ypos 0.5 
    show i_cousin_default_neutral as cousin zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.3 
        ypos 0.5 
    show i_tobi_stand_grin as toby zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.9 
        ypos 0.5 
        alpha 1.0

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
    if slot_pick_count_hiromi <= 1:
        call BadEndMacro
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    if slot_pick_count_hiromi == 2:
        # <IfEqual IfEqual {'lvalue': '${slot:pick_count_hiromi}', 'name': '_5', 'rvalue': '2', 'kind': 'IfEqual'} ''>
        label s_hiromi6__5:
            # <IfEqual IfEqual {'lvalue': '${slot:pick_count_hiromi}', 'name': '_5', 'rvalue': '2', 'kind': 'IfEqual'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_crossed_serious as hiromi
            show i_cousin_default_neutral as cousin
            show i_tobi_stand_grin as toby
            t_ch_hiromi "We’re taking off, [slot_playerName]." # @t_shiromi660.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Thanks for everything, Hiromi…" # @t_shiromi661.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_hiromi "……………." # @t_shiromi662.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_akimbo_smile as hiromi
            t_ch_hiromi "………….. no, thank you, [slot_playerName]." # @t_shiromi663.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Will you write?" # @t_shiromi664.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_stand_smile as hiromi
            t_ch_hiromi "……………." # @t_shiromi665.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_hiromi "I’m not much for words……." # @t_shiromi666.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_laugh as cousin
            t_ch_cousin "Hah….." # @t_shiromi667.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_crossed_smile as hiromi
            t_ch_cousin "Hahahahaha!" # @t_shiromi668.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "That’s true." # @t_shiromi669.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_akimbo_smile as hiromi
            t_ch_hiromi "……………. but for you, I’ll make an exception." # @t_shiromi6610.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear 1 xpos 0.5 
            show i_hiromi_akimbo_smile as hiromi:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_tobi_stand_grin as toby:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            extend "{w=1.0}{nw}"
            t_ch_cousin "(I’ve never had a friend like Hiromi before…." # @t_shiromi6611.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "I’ll see her again some day. I’m sure of it.)" # @t_shiromi6612.00 self.block='Last'
            show i_sw_black as curtain:
                # ShowWithAtl
                linear 1 alpha 1.0
            # Credits music -- NOT PLAYING (in screen)
            call CreditsEvent
            return
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    $ persistent.got_trueend_hiromi = True
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
        # ShowWithAtl
        linear 0.5 alpha 1.0
    show i_tobi_stand_grin as toby:
        # ShowWithAtl
        linear 0.5 xpos 0.9 
        # ShowWithAtl
        linear 0.5 alpha 1.0
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    extend "{w=0.5}{nw}"
    t_ch_hiromi "We’re taking off, [slot_playerName]." # @t_shiromi6614.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Thanks for everything, Hiromi…" # @t_shiromi6615.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "……………." # @t_shiromi6616.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_akimbo_smile as hiromi
    t_ch_hiromi "………….. no, thank you, [slot_playerName]." # @t_shiromi6617.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Will you write?" # @t_shiromi6618.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_stand_smile as hiromi
    t_ch_hiromi "……………." # @t_shiromi6619.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I’m not much for words……." # @t_shiromi6620.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "Hah….." # @t_shiromi6621.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_smile as hiromi
    t_ch_cousin "Hahahahaha!" # @t_shiromi6622.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "That’s true." # @t_shiromi6623.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "………………………….." # @t_shiromi6624.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I wish I could come with you…" # @t_shiromi6625.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_stand_serious as hiromi
    t_ch_hiromi "………………………….." # @t_shiromi6626.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_akimbo_smile_blush as hiromi
    t_ch_hiromi "Maybe you can." # @t_shiromi6627.00 self.block='Last'
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 1 alpha 1.0
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    show i_event_hiromi_ending as trueEnd zorder 23:
        default
        alpha 0.0
        linear 1 alpha 1.0
        # ShowWithAtl
        linear 1 alpha 0.0
    return