define slot_pick_count_valk = 0
# <Scene {'id': 's_valk6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_valk6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_valk6"
    $ renpy.pause(1) # buffer
    # <Scene {'id': 's_valk6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_valk6_initialize:
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

    # <BattleMacro {'name': '_1', 'partnerActor': 'valkyrie'} BattleMacro ''>
    window hide None
    # <ParallelEvent {'auto': True} ParallelEvent ''>
    # <Events {'kind': 'RawRpy'} events ''>
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
    # <ParallelEvent {'delay': 0.5, 'auto': True} ParallelEvent ''>
    # <Events {'kind': 'events'} events ''>
    play sound "sfx/thunderclap.ogg" noloop
    show i_sw_white as white_swatch    # ActorEvent
    with flash
    $ renpy.pause(0.5) # ParallelEvent Delay
    # <ParallelEvent {'delay': 0.5} ParallelEvent ''>
    # <Events {'kind': 'Events'} events ''>
    show i_sw_white as white_swatch    # ActorEvent
    with flash


    $ renpy.pause(2) # ParallelEvent Delay
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
    $ renpy.pause(0.75) # ParallelEvent Delay
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
    show i_battlepose_valkyrie as valkyrie:
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
    show i_battlepose_valkyrie as valkyrie:
        # ActorEvent
        # ActorEvent (Transition only)
        ease 1.0 xpos 0.7 
    $ renpy.pause(1.0) # TimedPause
    # <ParallelEvent {'kind': 'Events'} ParallelEvent ''>
    # <Events {'kind': 'ParallelEvent'} events ''>
    show i_sw_white as white_swatch:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5) # TimedPause
    # = Battlemacro contents
    # <ParallelEvent {'kind': 'events'} ParallelEvent ''>
    # <Events {'kind': 'Annotation'} events ''>
    # <Events {} events ''>
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
    if slot_pick_count_valk <= 1:
        call BadEndMacro
    if slot_pick_count_valk == 2:
        # <IfEqual {'lvalue': '${slot:pick_count_valk}', 'name': '_3', 'rvalue': '2'} IfEqual ''>
        label s_valk6__3:
            # <IfEqual {'lvalue': '${slot:pick_count_valk}', 'name': '_3', 'rvalue': '2'} IfEqual ''>
            # <Events {} events ''>
            # Credits music -- NOT PLAYING (in screen)
            call CreditsEvent
            # <ParallelEvent {'auto': 'true', 'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_valkyrie_default_grin as valkyrie:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear 0.5 xpos 0.5 
            show i_sw_black as curtain:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "It's been a few months since Valkyrie left. I still think about her." # @t_svalk637.00 self.block='Last'
            # <ParallelEvent {'name': '_4'} ParallelEvent ''>
            # <Events {} events ''>
            extend " I wonder how she's doing out there." # @t_svalk637.01 self.block='Last'
            # <ParallelEvent {'name': '_5'} ParallelEvent ''>
            # <Events {} events ''>
            extend " I hope she saved her people." # @t_svalk637.02 self.block='Last'
            # <ParallelEvent {'name': '_6'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral_blush as cousin
            with Dissolve(0.5)
            extend " I definitely miss her. All I have left is my memories of her... And they become dimmer by the day." # @t_svalk637.03 self.block='Last'
            # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_7'} ParallelEvent ''>
            # <Events {} events ''>
            show i_sw_black as curtain zorder 22:
                # ShowWithAtl
                linear 1 alpha 1.0
            $ renpy.pause(1.0) # TimedPause
            return
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    $ persistent.got_trueend_valk = True
    show i_valkyrie_default_grin as valkyrie
    show i_cousin_default_neutral as cousin
    t_ch_cousin "What's this... ?" # @t_svalk622.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_forjustice_grin as valkyrie
    t_ch_valkyrie "Hahaha! That was so much fun! I haven't been in a good battle in a long time." # @t_svalk623.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Valkyrie..." # @t_svalk624.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    extend " I think I found it." # @t_svalk624.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_akimbo_grin as valkyrie
    t_ch_valkyrie "Found what?" # @t_svalk625.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I take the item out of my pocket and show it to her. It's an elaborately worked key.)" # @t_svalk626.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_akimbo_grinblush as valkyrie
    t_ch_valkyrie "O. M. G. This is..." # @t_svalk627.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    extend " It was kind of amazing.)" # @t_svalk628.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(She stuck it right into the face of the clock, and a keyhole appeared as thought it'd been there all along.)" # @t_svalk629.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(It all happened in broad daylight... Haha, that's just like her.)" # @t_svalk630.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(For a moment she went very still... I think she hesitated." # @t_svalk631.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    extend " Then she turned the key, once, hard.)" # @t_svalk631.01 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(The thundercrack was so loud, it shook all of campus." # @t_svalk632.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The light was yellow and soft and bright, like a hundred thousand fireflies flaring to life at once.)" # @t_svalk632.01 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_akimbo_sil as valkyrie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "(When I could see again... She was gone.)" # @t_svalk633.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "It's been a few months since Valkyrie left. I still think about her." # @t_svalk634.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " A lot has happened since then." # @t_svalk634.01 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    extend " Did I tell you? I'm dating someone now." # @t_svalk634.02 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It's something I would have been too shy to do on my own..." # @t_svalk635.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Turns out, I learned a lot from her." # @t_svalk635.01 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "She left me a beautiful gift." # @t_svalk636.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_prop_sword_good as sword:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    extend " A sword that she made with her own hands." # @t_svalk636.01 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Whenever I feel shy, I hold the sword and remember her." # @t_svalk636.02 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I hope, wherever she is... She's found someone too." # @t_svalk636.03 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain zorder 22:
        # ShowWithAtl
        linear 1 alpha 1.0
    $ renpy.pause(1.0) # TimedPause
    return