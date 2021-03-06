define slot_pick_count_albatros = 0
# <Scene scene {'id': 's_albatros6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_albatros6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_albatros6"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_albatros6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_albatros6_initialize:
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
        show i_battlepose_albatross_multi as albatros zorder 12:
            default
            xpos 0.9 
            ypos 0.38 
            xzoom 0.75 
            yzoom 0.75 
            alpha 0.0

    if slot_pick_count_albatros <= 1:
        # <IfLTE IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_albatros}', 'name': '_1', 'rvalue': '1', 'kind': 'IfLTE'} ''>
        label s_albatros6__1:
            # <IfLTE IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_albatros}', 'name': '_1', 'rvalue': '1', 'kind': 'IfLTE'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_battlepose_albatross_glitch as albatros
    # <BattleMacro BattleMacro {'name': '_2', 'partnerActor': 'albatros', 'kind': 'BattleMacro'} ''>
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
    show i_battlepose_albatross_glitch as albatros:
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
    show i_battlepose_albatross_glitch as albatros:
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
    show i_albatross_toocool_smirk as albatros zorder 2:
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
    if slot_pick_count_albatros <= 1:
        call BadEndMacro
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    if slot_pick_count_albatros == 2:
        # <IfEqual IfEqual {'lvalue': '${slot:pick_count_albatros}', 'name': '_5', 'rvalue': '2', 'kind': 'IfEqual'} ''>
        label s_albatros6__5:
            # <IfEqual IfEqual {'lvalue': '${slot:pick_count_albatros}', 'name': '_5', 'rvalue': '2', 'kind': 'IfEqual'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Albatross took the greatest risk of all by equipping the most powerful cheat code of them all. The infamous 30 Lives Code.)" # @t_salbatros639.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(The extra manpower helped us overcome the robotic horde of Evil Namco High.)" # @t_salbatros640.00 self.block='Last'
            show i_sw_black as curtain:
                # ShowWithAtl
                linear 1 alpha 1.0
            # Credits music -- NOT PLAYING (in screen)
            call CreditsEvent
            return
    if slot_pick_count_albatros >= 3:
        # <IfGTE IfGTE {'lvalue': '${slot:pick_count_albatros}', 'name': '_6', 'rvalue': '3', 'kind': 'IfGTE'} ''>
        label s_albatros6__6:
            # <IfGTE IfGTE {'lvalue': '${slot:pick_count_albatros}', 'name': '_6', 'rvalue': '3', 'kind': 'IfGTE'} ''>
            # <Events events {'kind': 'events'} ''>
            $ persistent.got_trueend_albatros = True
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            show i_albatross_welcome_smirk as albatros
            t_ch_albatross "...we hereby commend upon you the rank of World Crime Police Organization junior agent for gallantry in the line of duty…" # @t_salbatros641.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatross "And for helping me to learn that the world isn’t so black and white…" # @t_salbatros642.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_welcome_smirk_wink as albatros
            t_ch_albatross "And for, maybe, going out for that coffee later…?" # @t_salbatros643.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "It’s a date!" # @t_salbatros644.00 self.block='Last'
            show i_sw_black as curtain:
                # ShowWithAtl
                linear 1 alpha 1.0
            # Credits music -- NOT PLAYING (in screen)
            call CreditsEvent
            show i_event_albatross_ending as trueEnd zorder 23:
                default
                alpha 0.0
                linear 1 alpha 1.0
                # ShowWithAtl
                linear 1 alpha 0.0
            return