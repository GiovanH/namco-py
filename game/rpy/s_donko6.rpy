define slot_pick_count_donko = 0
# <Scene {'id': 's_donko6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_donko6:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_donko6"
    $ renpy.pause(1)
    # <Scene {'id': 's_donko6', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_donko6_initialize:
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
        show i_battlepose_donko as donko zorder 12:
            default
            xpos 0.9 
            ypos 0.0 
            xzoom 0.75 
            yzoom 0.75 
            alpha 0.0
        show i_taira_steveholt_confused as taira zorder 2:
            default
            alpha 0.0
            xpos 0.3 
        show i_aki_default_laughter as aki zorder 2:
            default
            alpha 1.0
            xpos 0.3 
        show i_galaga_default as galaga zorder 2:
            default
            alpha 0.0
            xpos 0.3 

    # <BattleMacro {'name': '_1', 'partnerActor': 'donko'} BattleMacro ''>
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
    show i_battlepose_donko as donko:
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
    show i_battlepose_donko as donko:
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
    show i_donko_akimbo_grin as donko zorder 2:
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
        alpha 0.0

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
    if slot_pick_count_donko <= 1:
        call BadEndMacro
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_laughter as aki
    show i_donko_akimbo_grin as donko
    t_ch_aki "Donko! You did it!" # @t_sdonko682.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_smile as aki
    extend " You saved Pac-Man, AND the school!" # @t_sdonko682.01 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_laughter as aki
    extend " That’ll be amazing on your resume! I’m SO JEALOUS..." # @t_sdonko682.02 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    t_ch_donko "Oh! Well, [slot_playerName] helped too-" # @t_sdonko683.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_laughter as aki:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_taira_steveholt_happy as taira:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_taira "YEAHHH! Donko, you’re good at EVERYTHING!" # @t_sdonko684.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic as donko
    t_ch_donko "Well, but it was really, like, a joint effort-" # @t_sdonko685.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_galaga_default as galaga:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}WELL DONE DONKO.{/smallcaps}" # @t_sdonko686.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}GALAGA IS PLEASED!{/smallcaps}" # @t_sdonko686.01 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic as donko
    t_ch_donko "...Everyone’s giving me all the credit!" # @t_sdonko687.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic_blush as donko
    with Dissolve(0.5)
    extend " It’s like, totally unfair!" # @t_sdonko687.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_default as galaga:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_cousin_default_grin_scarf as cousin:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "Heh… I don’t mind." # @t_sdonko688.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_grin as donko
    extend " After all… everybody knows you here." # @t_sdonko688.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh_scarf as cousin
    t_ch_cousin "I’m not as popular as you, so they don’t notice me as much…" # @t_sdonko689.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_scarf as cousin
    extend " But I don’t really care." # @t_sdonko689.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_scarf_blush as cousin
    with Dissolve(0.5)
    extend " The only person I care about being popular with is you." # @t_sdonko689.02 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_grin_blush as donko
    with Dissolve(0.5)
    t_ch_donko "OMG, [slot_playerName]..." # @t_sdonko690.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If you keep saying corny stuff like that around me..." # @t_sdonko690.01 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink_blush as donko
    show i_cousin_default_laugh_scarf_blush as cousin
    extend " You’re gonna like, totally ruin my reputation!" # @t_sdonko690.02 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_scarf as cousin
    t_ch_cousin "(I don’t care about popularity…" # @t_sdonko691.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or fashion…" # @t_sdonko691.01 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or even about music. I just listen to what’s on the radio!" # @t_sdonko691.02 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    t_ch_cousin "But I do care about Donko… I care about her a lot." # @t_sdonko692.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_scarf_blush as cousin
    extend " And if those things are important to her, I know they really matter." # @t_sdonko692.01 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "From here on out, I’ll take her feelings seriously." # @t_sdonko693.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She deserves it." # @t_sdonko693.01 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad_scarf_blush as cousin
    t_ch_cousin "...Darn, I wish I could’ve thought of a drum pun to sneak in there…" # @t_sdonko694.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That would have been perfect." # @t_sdonko694.01 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_scarf as cousin
    extend " Per(cussion)fect?!" # @t_sdonko694.02 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_laugh_scarf_blush as cousin
    t_ch_cousin "...Nailed it.)" # @t_sdonko695.00 self.block='Last'
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 1 alpha 1.0
    # Credits music -- NOT PLAYING (in screen)
    call CreditsEvent
    if slot_pick_count_donko >= 3:
        # <IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_donko}', 'name': '_a', 'rvalue': '3'} IfGTE ''>
        label s_donko6__a:
            # <IfGTE {'auto': 'true', 'lvalue': '${slot:pick_count_donko}', 'name': '_a', 'rvalue': '3'} IfGTE ''>
            # <Events {} events ''>
            $ persistent.got_trueend_donko = True
            show i_event_donko_ending as trueEnd zorder 23:
                default
                alpha 0.0
                linear 1 alpha 1.0
                # ShowWithAtl
                linear 1 alpha 0.0
    return