define slot_pick_count_valk = 0
# <Scene scene {'id': 's_valk6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_valk6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_valk6"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_valk6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_valk6_initialize:
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
        show i_battlepose_valkyrie as valkyrie zorder 12:
            default
            xpos 0.9 
            ypos 0.38 
            xzoom 0.75 
            yzoom 0.75 
            alpha 0.0
        show i_prop_sword_good as sword zorder 5:
            default
            xpos 0.7 
            ypos 0.38 
            xzoom 0.75 
            yzoom 0.75 
            alpha 0.0

    # <BattleMacro BattleMacro {'name': '_1', 'partnerActor': 'valkyrie', 'kind': 'BattleMacro'} ''>
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
    show i_battlepose_valkyrie as valkyrie:
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
    show i_battlepose_valkyrie as valkyrie:
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
    show i_valkyrie_default_grin as valkyrie zorder 2:
        # ActorEvent
        xzoom 1.0 
        yzoom 1.0 
        xpos 0.7 
        ypos 0.5 
    show i_cousin_default_neutral as cousin zorder 5:
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
    if slot_pick_count_valk <= 1:
        call BadEndMacro
    if slot_pick_count_valk == 2:
        # <IfEqual IfEqual {'lvalue': '${slot:pick_count_valk}', 'name': '_3', 'rvalue': '2', 'kind': 'IfEqual'} ''>
        label s_valk6__3:
            # <IfEqual IfEqual {'lvalue': '${slot:pick_count_valk}', 'name': '_3', 'rvalue': '2', 'kind': 'IfEqual'} ''>
            # <Events events {'kind': 'events'} ''>
            # Credits music -- NOT PLAYING (in screen)
            call CreditsEvent
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_default_grin as valkyrie:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear 0.5 xpos 0.5 
            show i_sw_black as curtain:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "It's been a few months since Valkyrie left. I still think about her." # @t_svalk637.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I wonder how she's doing out there." # @t_svalk637.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I hope she saved her people." # @t_svalk637.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            with Dissolve(0.5)
            extend " I definitely miss her. All I have left is my memories of her... And they become dimmer by the day." # @t_svalk637.03 self.block='Last'
            # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_sw_black as curtain zorder 22:
                # ShowWithAtl
                linear 1 alpha 1.0
            $ renpy.pause(1.0, hard=True) # TimedPause
            return
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    $ persistent.got_trueend_valk = True
    show i_valkyrie_default_grin as valkyrie
    show i_cousin_default_neutral as cousin
    t_ch_cousin "What's this... ?" # @t_svalk622.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie
    t_ch_valkyrie "Hahaha! That was so much fun! I haven't been in a good battle in a long time." # @t_svalk623.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Valkyrie..." # @t_svalk624.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    extend " I think I found it." # @t_svalk624.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie
    t_ch_valkyrie "Found what?" # @t_svalk625.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I take the item out of my pocket and show it to her. It's an elaborately worked key.)" # @t_svalk626.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grinblush as valkyrie
    t_ch_valkyrie "O. M. G. This is..." # @t_svalk627.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_sil as valkyrie
    with Dissolve(0.5)
    show i_sw_black as curtain zorder 4:
        # ShowWithAtl
        linear 0.5 alpha 0.5
    show i_cousin_default_sad_blush as cousin:
        # ShowWithAtl
        linear 1 xpos 0.5 
    extend "{w=1.0}{nw}"
    t_ch_cousin "(She was able to use the key." # @t_svalk628.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " It was kind of amazing.)" # @t_svalk628.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(She stuck it right into the face of the clock, and a keyhole appeared as thought it'd been there all along.)" # @t_svalk629.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It all happened in broad daylight... Haha, that's just like her.)" # @t_svalk630.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(For a moment she went very still... I think she hesitated." # @t_svalk631.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " Then she turned the key, once, hard.)" # @t_svalk631.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(The thundercrack was so loud, it shook all of campus." # @t_svalk632.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The light was yellow and soft and bright, like a hundred thousand fireflies flaring to life at once.)" # @t_svalk632.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_sil as valkyrie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "(When I could see again... She was gone.)" # @t_svalk633.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "It's been a few months since Valkyrie left. I still think about her." # @t_svalk634.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    extend " A lot has happened since then." # @t_svalk634.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    extend " Did I tell you? I'm dating someone now." # @t_svalk634.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It's something I would have been too shy to do on my own..." # @t_svalk635.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Turns out, I learned a lot from her." # @t_svalk635.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "She left me a beautiful gift." # @t_svalk636.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_prop_sword_good as sword:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    extend " A sword that she made with her own hands." # @t_svalk636.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Whenever I feel shy, I hold the sword and remember her." # @t_svalk636.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I hope, wherever she is... She's found someone too." # @t_svalk636.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain zorder 22:
        # ShowWithAtl
        linear 1 alpha 1.0
    $ renpy.pause(1.0, hard=True) # TimedPause
    return