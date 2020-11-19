define slot_pick_count_davesprite = 0
# <Scene scene {'id': 's_davesprite6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_davesprite6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_davesprite6"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_davesprite6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_davesprite6_initialize:
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
        show i_pacman_left as pacman zorder 2:
            default
            xpos 0.7 
            alpha 0.0
        show i_battlepose_davesprite as davesprite zorder 12:
            default
            xpos 0.9 
            ypos 0.38 
            xzoom 0.75 
            yzoom 0.75 
            alpha 0.0

    # <BattleMacro BattleMacro {'name': '_1', 'partnerActor': 'davesprite', 'kind': 'BattleMacro'} ''>
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
    show i_battlepose_davesprite as davesprite:
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
    show i_battlepose_davesprite as davesprite:
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
    show i_davesprite_standing_disinterest as davesprite zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.35 
        ypos 0.5 
    show i_cousin_default_neutral as cousin zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.1 
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
    if slot_pick_count_davesprite <= 1:
        call BadEndMacro
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite:
        # ShowWithAtl
        linear 0.5 xpos 0.35 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.1 
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear 0.5 xpos 0.9 
    $ renpy.pause(0.5, hard=True) # Text delay
    t_ch_pacman "You saved me!" # @t_sdavesprite696.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        pause 0.25 
        linear .5 alpha 0.0
    show i_davesprite_standing_disinterest as davesprite:
        # ShowWithAtl
        pause 1.0 
        linear .333 xpos 0.7 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        pause 1.0 
        linear .333 xpos 0.3 
    extend "{w=1.333}{nw}"
    t_ch_pacman "Thank you so much!" # @t_sdavesprite697.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "We did it…" # @t_sdavesprite698.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " We beat Evil Namco High…" # @t_sdavesprite698.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I know I seemed pretty self confident, but…" # @t_sdavesprite699.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " I was worried for a moment." # @t_sdavesprite699.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "...Thank you, Davesprite." # @t_sdavesprite6100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "huh" # @t_sdavesprite6101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    t_ch_davesprite "so this is the ending of the game huh" # @t_sdavesprite6102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i think we got the good one" # @t_sdavesprite6103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "thats cool" # @t_sdavesprite6104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Davesprite…" # @t_sdavesprite6105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " If it really is the end of the game…" # @t_sdavesprite6105.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What’s gonna happen to us after this?" # @t_sdavesprite6106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "i was thinking about that too" # @t_sdavesprite6107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i was hoping it didnt occur to you" # @t_sdavesprite6108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "because" # @t_sdavesprite6109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_sad as davesprite
    t_ch_davesprite "i actually have no idea" # @t_sdavesprite6110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_sad as davesprite
    t_ch_davesprite "and i didnt want you to be scared" # @t_sdavesprite6111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Heh. Finally something you don’t have an answer for…" # @t_sdavesprite6112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " Somehow it doesn’t feel as good as I thought it would." # @t_sdavesprite6112.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "i wonder" # @t_sdavesprite6113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "are we just gonna disappear?" # @t_sdavesprite6114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "or maybe you will" # @t_sdavesprite6115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "and i will just restart" # @t_sdavesprite6116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "youll be in a new game and wont remember" # @t_sdavesprite6117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "but i will" # @t_sdavesprite6118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "leaving me even more alone than before" # @t_sdavesprite6119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_defeated_sad as davesprite
    t_ch_davesprite "that would seem about par for the course with how my life has gone so far" # @t_sdavesprite6120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I’m not saying I believe you when you say it’s all a video game…" # @t_sdavesprite6121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I mean, that’s totally crazy." # @t_sdavesprite6121.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "But… if it is…" # @t_sdavesprite6122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And this really is the end..." # @t_sdavesprite6122.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "There’s nothing we can do but wait and find out what happens next." # @t_sdavesprite6123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "yeah" # @t_sdavesprite6124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "i guess so" # @t_sdavesprite6125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Davesprite…" # @t_sdavesprite6126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    show i_sw_white as white_swatch:
        # ShowWithAtl
        linear .666 alpha 0.2
    extend "{w=0.666}{nw}"
    extend " I’m glad I picked you, and…" # @t_sdavesprite6126.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_laugh as cousin
    show i_sw_white as white_swatch:
        # ShowWithAtl
        linear .666 alpha 0.4
    extend "{w=0.666}{nw}"
    t_ch_cousin "Whatever happens, I’m glad you came with me." # @t_sdavesprite6127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    show i_sw_white as white_swatch:
        # ShowWithAtl
        linear .666 alpha 0.6
    extend "{w=0.666}{nw}"
    t_ch_davesprite "yeah" # @t_sdavesprite6128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile_blush as davesprite
    with Dissolve(.333)
    show i_sw_white as white_swatch:
        # ShowWithAtl
        linear .666 alpha 0.8
    extend "{w=0.666}{nw}"
    t_ch_davesprite "me too." # @t_sdavesprite6129.00 self.block='Last'
    show i_sw_white as white_swatch:
        # ShowWithAtl
        linear .666 alpha 1.0
    $ renpy.pause(1) # ParallelEvent Delay
    # <ParallelEvent ParallelEvent {'auto': 'true', 'delay': '1', 'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain zorder 18:
        # ShowWithAtl
        linear 1 alpha 1.0
    $ renpy.pause(1.0, hard=True) # TimedPause
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    if slot_pick_count_davesprite >= 3:
        # <IfGTE IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_davesprite}', 'name': '_n', 'rvalue': '3', 'kind': 'IfGTE'} ''>
        label s_davesprite6__n:
            # <IfGTE IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_davesprite}', 'name': '_n', 'rvalue': '3', 'kind': 'IfGTE'} ''>
            # <Events events {'kind': 'events'} ''>
            $ persistent.got_trueend_davesprite = True
            show i_event_davesprite_ending as trueEnd zorder 23:
                default
                alpha 0.0
                linear 1 alpha 1.0
                # ShowWithAtl
                linear 1 alpha 0.0
    return