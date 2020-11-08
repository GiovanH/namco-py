define slot_pick_count_mrdriller = 0
# <Scene {'id': 's_mrdriller6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_mrdriller6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_mrdriller6"
    $ renpy.pause(1)
    # <Scene {'id': 's_mrdriller6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_mrdriller6_initialize:
        # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
        # <Events {} events ''>
        # Pass (VarEnsure)
        show i_digdug_left as digdug zorder 3:
            default
            xpos 0.8 
            alpha 0.0
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
        show i_digdug_left as cousin zorder 13:
            default
            xpos 0.9 
            ypos 0.75 
            alpha 0.0
            xzoom 0.75 
            yzoom 0.75 
        show i_battlepose_mrdriller as mrdriller zorder 12:
            default
            xpos 0.9 
            ypos 0.38 
            xzoom 0.75 
            yzoom 0.75 
            alpha 0.0

    if slot_pick_count_mrdriller <= 1:
        # <IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_mrdriller}', 'name': '_1', 'rvalue': '1'} IfLTE ''>
        label s_mrdriller6__1:
            # <IfLTE {'auto': 'true', 'lvalue': '${slot:pick_count_mrdriller}', 'name': '_1', 'rvalue': '1'} IfLTE ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_battlepose_mrdriller_nodrill as mrdriller
            show i_battlepose_cousin_normal as cousin

    # <BattleMacro {'name': '_2', 'partnerActor': 'mrdriller'} BattleMacro ''>
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
    show i_battlepose_mrdriller_nodrill as mrdriller:
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
    show i_battlepose_mrdriller_nodrill as mrdriller:
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
    show i_mrdriller_drillup_excited as mrdriller zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.53 
        ypos 0.5 
    show i_cousin_default_grin as cousin zorder 3:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.1 
        ypos 0.5 
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.5 alpha 1.0

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
    if slot_pick_count_mrdriller <= 1:
        call BadEndMacro
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "We did it! We saved Pac-Man!" # @t_smrdriller691.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "YEAH! It feels so good to dig again!" # @t_smrdriller692.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_drillup_shock as mrdriller
    t_ch_mrdriller "Dad… you really mean that?" # @t_smrdriller693.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I do. Thank you, son." # @t_smrdriller694.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_laugh as cousin:
        # ShowWithAtl
        pause 0.666 
        linear .5 xpos 0.25 
    extend "{w=1.166}{nw}"
    t_ch_cousin "Mr. Driller, you were amazing! I’m so proud of-" # @t_smrdriller695.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        pause 0.25 
        linear .25 xpos 0.08 
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear .25 xpos 0.58 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(But before I could give him a hug, Dig Dug pushed me away.)" # @t_smrdriller696.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "No way, [slot_playerName]." # @t_smrdriller697.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin zorder 2
    extend " You two are gonna stick to a hearty handshake until you’re the same age as me." # @t_smrdriller697.01 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_drillup_sad as mrdriller
    t_ch_mrdriller "Dad, come on! It’s just a hug." # @t_smrdriller698.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 1.5 xpos 0.8 
    extend "{w=1.5}{nw}"
    t_ch_digdug "...Alright! Make it quick." # @t_smrdriller699.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_laugh_blush as cousin:
        # ShowWithAtl
        linear .5 xpos 0.2 
    show i_mrdriller_drillup_excited as mrdriller:
        # ShowWithAtl
        linear .5 xpos 0.4 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(As I pull Mr. Driller into my embrace, I can see Principal Dig Dug is gonna watch us like a hawk…" # @t_smrdriller6100.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I guess an overprotective parent is always gonna be an overprotective parent." # @t_smrdriller6100.01 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Still, I’m glad that Mr. Driller knows now that his dad cares about him." # @t_smrdriller6101.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And… he knows I care about him, too.)" # @t_smrdriller6101.01 self.block='Last'
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 1 alpha 1.0
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    if slot_pick_count_mrdriller >= 3:
        # <IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_mrdriller}', 'name': '_M', 'rvalue': '3'} IfGTE ''>
        label s_mrdriller6__M:
            # <IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_mrdriller}', 'name': '_M', 'rvalue': '3'} IfGTE ''>
            # <Events {} events ''>
            $ persistent.got_trueend_mrdriller = True
            show i_event_mrdriller_ending as trueEnd zorder 23:
                default
                alpha 0.0
                linear 1 alpha 1.0
                # ShowWithAtl
                linear 1 alpha 0.0
    return