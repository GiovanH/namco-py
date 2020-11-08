define slot_pick_count_meowkie = 0
# <Scene {'id': 's_meowkie6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_meowkie6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_meowkie6"
    $ renpy.pause(1)
    # <Scene {'id': 's_meowkie6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_meowkie6_initialize:
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
        show i_battlepose_meowkie as meowkie zorder 12:
            default
            xpos 0.9 
            ypos 0.38 
            xzoom -0.75 
            yzoom 0.75 
            alpha 0.0
        show i_nidia_akimbo_happy as nidia zorder 3:
            default
            xpos 0.3 
            alpha 0.0
        show i_pacman_left as pacman zorder 2:
            default
            xpos 0.9 
            alpha 0.0
        show i_bluemax_stand_smile as bluemax zorder 2:
            default
            xpos 0.3 
            alpha 0.0

    # <BattleMacro {'name': '_1', 'partnerActor': 'meowkie'} BattleMacro ''>
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
    show i_battlepose_meowkie as meowkie:
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
    show i_battlepose_meowkie as meowkie:
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
    show i_meowkie_normal_normal_badge as meowkie zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.35 
        ypos 0.5 
    show i_cousin_default_grin as cousin zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.1 
        ypos 0.5 
    show i_pacman_left as pacman:
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
    if slot_pick_count_meowkie <= 1:
        call BadEndMacro
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "You saved me! Thank you so much!" # @t_smeowkie6102.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_grin_badge as meowkie
    t_ch_meowkie "All in a day’s work… for a Hall Monitor!" # @t_smeowkie6103.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "We did it, Meowkie!" # @t_smeowkie6104.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie:
        linear .25 xzoom -1.0 
    t_ch_meowkie "Nya… I hope I wasn’t holdin’ you back too much, Boss…" # @t_smeowkie6105.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Are you kidding?!" # @t_smeowkie6106.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "That righteous fury you unleashed on the battlefield…" # @t_smeowkie6107.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ve never seen anything like it!" # @t_smeowkie6107.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "Meowkie… you’re amazing." # @t_smeowkie6108.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_grin_badge as meowkie
    t_ch_meowkie "Haha… I gotta admit, it felt pretty good…" # @t_smeowkie6109.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It was cathartic, you know?" # @t_smeowkie6109.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    t_ch_meowkie "But… I’m still not sure the other students will like it…" # @t_smeowkie6110.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_meowkie_normal_alert_badge as meowkie:
        pause .25
        linear .25 xzoom 1.0 
    extend "{w=0.25}{nw}"
    t_ch_cousin "(As if on cue, the other students at Namco High swarm Meowkie." # @t_smeowkie6110.00a self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They’re all so happy and proud of what she did… They’re hugging her and congratulating her…" # @t_smeowkie6110.01 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Meowkie looks totally stunned!)" # @t_smeowkie6111.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_happy as nidia:
        # ShowWithAtl
        linear .333 alpha 1.0
        # ShowWithAtl
        linear 0.5 xpos 0.68 
    extend "{w=0.5}{nw}"
    t_ch_nidia "You did it, Meowkie! That was amazing… it must’ve been your destiny all along!" # @t_smeowkie6112.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_smile as bluemax:
        # ShowWithAtl
        linear 0.5 xpos 0.65 
        # ShowWithAtl
        linear .333 alpha 1.0
    show i_nidia_akimbo_happy as nidia:
        # ShowWithAtl
        linear .25 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_max "I’m sorry I ever doubted you, Meowkie! I want an amazing fighter like you on my side anytime!" # @t_smeowkie6113.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_smile as bluemax:
        # ShowWithAtl
        linear .333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_pacman "Come on everyone! Let’s celebrate!" # @t_smeowkie6114.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear .333 alpha 0.0
    show i_meowkie_normal_alert_badge as meowkie:
        # ShowWithAtl
        pause 0.25 
        linear .333 xpos 0.7 
        pause .333
        linear .333 xzoom -1.0 
    show i_cousin_default_grin as cousin:
        # ShowWithAtl
        pause 0.25 
        linear .25 xpos 0.3 
    extend "{w=0.583}{nw}"
    t_ch_cousin "(And at Pac-Man’s words, they all rush off to party and celebrate our win…" # @t_smeowkie6115.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Meowkie and I are alone again.)" # @t_smeowkie6115.01 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "...Wow…" # @t_smeowkie6116.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "See, Meowkie? They know now what a sweet person you are…" # @t_smeowkie6117.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I have a feeling you won’t have any trouble here from now on." # @t_smeowkie6117.01 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But… you don’t have to forgive them right away, you know!" # @t_smeowkie6118.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean, you shouldn’t have had to prove anything, to anyone." # @t_smeowkie6118.01 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You’re not bad, and they should never have treated you like you were." # @t_smeowkie6119.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "...It’s alright, [slot_playerName]." # @t_smeowkie6120.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What’s done is done, ya know?" # @t_smeowkie6120.01 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_normal_badge as meowkie
    extend " I’d rather just move on…" # @t_smeowkie6120.02 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_grin_badge as meowkie
    t_ch_meowkie "Thank you. For everything." # @t_smeowkie6121.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Thank you, Meowkie." # @t_smeowkie6122.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(She’s such a sweet person…" # @t_smeowkie6123.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Of course she’d forgive them right away." # @t_smeowkie6123.01 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And I’ll go along with what she wants, of course." # @t_smeowkie6123.02 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    t_ch_cousin "But still, the jerks who were mean to Meowkie better watch their steps from now on…" # @t_smeowkie6124.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_angry as cousin
    extend " Because as the new Hall Monitor at Namco High, I’ll be keeping a VERY close eye on them." # @t_smeowkie6124.01 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Heh heh heh!)" # @t_smeowkie6125.00 self.block='Last'
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 1 alpha 1.0
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    if slot_pick_count_meowkie >= 3:
        # <IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_meowkie}', 'name': '_h', 'rvalue': '3'} IfGTE ''>
        label s_meowkie6__h:
            # <IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_meowkie}', 'name': '_h', 'rvalue': '3'} IfGTE ''>
            # <Events {} events ''>
            $ persistent.got_trueend_meowkie = True
            show i_event_meowkie_ending as trueEnd zorder 23:
                default
                alpha 0.0
                linear 1 alpha 1.0
                # ShowWithAtl
                linear 1 alpha 0.0
    return