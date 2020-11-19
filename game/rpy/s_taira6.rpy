define slot_pick_count_taira = 0
# <Scene scene {'id': 's_taira6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_taira6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_taira6"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_taira6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_taira6_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        # Pass (VarEnsure)
        show i_pacman_left as pacman zorder 2:
            default
            xpos 0.92 
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
        show i_battlepose_cousin_normal as cousin zorder 13:
            default
            xpos 0.9 
            ypos 0.75 
            alpha 0.0
            xzoom 0.75 
            yzoom 0.75 
        show i_battlepose_taira as taira zorder 12:
            default
            xpos 0.9 
            ypos 0.38 
            xzoom 0.75 
            yzoom 0.75 
            alpha 0.0

    # <BattleMacro BattleMacro {'name': '_1', 'partnerActor': 'taira', 'kind': 'BattleMacro'} ''>
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
    show i_battlepose_taira as taira:
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
    show i_battlepose_taira as taira:
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
    show i_taira_akimbo_happy as taira zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.15 
        ypos 0.5 
    show i_cousin_default_neutral as cousin zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.45 
        ypos 0.5 
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 0.5 alpha 1.0

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
    if slot_pick_count_taira <= 1:
        call BadEndMacro
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Yo… we did it… we saved Pac-Man…" # @t_staira6107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_happy as taira
    extend " And we didn’t even have to do any revenge..." # @t_staira6107.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Yeah… I knew it…" # @t_staira6108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_laugh as cousin
    extend " The warrior heart and the delicate soul really are destined to work together…" # @t_staira6108.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_confused as taira
    t_ch_taira "Yeah…" # @t_staira6109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_confused as taira
    extend " Or the" # @t_staira6109.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_serious as taira
    extend " two" # @t_staira6109.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_serious as taira
    extend " totally rad warrior hearts…" # @t_staira6109.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "…" # @t_staira6110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Yeah, or that…" # @t_staira6111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Thank you for saving me!" # @t_staira6112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I knew you could do it if you could just be true to yourself." # @t_staira6112.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_happy as taira
    t_ch_taira "Thanks, Pac-bro!" # @t_staira6113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_serious_cry as taira
    t_ch_taira "I’m so glad you’re safe…" # @t_staira6114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_pleading_cry as taira
    extend " I TOTALLY LOVE YOU, MAN!" # @t_staira6114.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Er, yes, well…" # @t_staira6115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "You’re a very nice young man too…" # @t_staira6116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        pause 1.5 
        linear .333 xpos 0.7 
        pause 1.666
        linear .25 xzoom -1.0 
    show i_pacman_left as pacman:
        # ShowWithAtl
        pause 1.0 
        linear .5 alpha 0.0
    show i_taira_akimbo_pleading_cry as taira:
        # ShowWithAtl
        pause 1.5 
        linear .333 xpos 0.3 
    extend "{w=1.833}{nw}"
    t_ch_cousin "Don’t worry, Pac-Man. He’s like that about everything." # @t_staira6117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_confused as taira
    t_ch_taira "So, Cuz…" # @t_staira6118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_serious as taira
    t_ch_taira "what now?" # @t_staira6119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well, I don’t know about the future, but…" # @t_staira6120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " How about we get a sandwich?" # @t_staira6120.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m starving." # @t_staira6120.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_confused as taira
    t_ch_taira "Yo, I don’t eat food, remember?" # @t_staira6121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m mad undead." # @t_staira6121.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "You could just hang out with me while I eat a sandwich…" # @t_staira6122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_confused as taira
    t_ch_taira "Yeah, I’m down for that." # @t_staira6123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_serious as taira
    t_ch_taira "Doing anything with you sounds awesome right now…" # @t_staira6124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "Heh. You really are a big softie, aren’t you?" # @t_staira6127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_angry as taira
    t_ch_taira "WHAT?! NO WAY!" # @t_staira6128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_angry as taira
    extend " I’M AWESOME…" # @t_staira6128.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(So together, we went off to celebrate our victory." # @t_staira6129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Taira may be a meathead, and he’s made a lot of mistakes in his past." # @t_staira6130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "But I’m not interested in the past anymore, and neither is he." # @t_staira6131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Instead, we’re going to try to keep learning from each other, and face the future..." # @t_staira6132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    with Dissolve(.333)
    extend " ...Together." # @t_staira6132.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "After all, he helped me discover my warrior heart…" # @t_staira6133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " We’re bound together now, either by destiny or by choice." # @t_staira6133.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_laugh_blush as cousin
    t_ch_cousin "I can’t think of anything more awesome than that.)" # @t_staira6134.00 self.block='Last'
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 1 alpha 1.0
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    if slot_pick_count_taira >= 3:
        # <IfGTE IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_taira}', 'name': '_k', 'rvalue': '3', 'kind': 'IfGTE'} ''>
        label s_taira6__k:
            # <IfGTE IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_taira}', 'name': '_k', 'rvalue': '3', 'kind': 'IfGTE'} ''>
            # <Events events {'kind': 'events'} ''>
            $ persistent.got_trueend_taira = True
            show i_event_taira_ending as trueEnd zorder 23:
                default
                alpha 0.0
                linear 1 alpha 1.0
                # ShowWithAtl
                linear 1 alpha 0.0
    return