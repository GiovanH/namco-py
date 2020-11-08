# <Scene {'id': 's_intro', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_intro:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_intro"
    $ renpy.pause(1)
    # <Scene {'id': 's_intro', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_intro_initialize:
        # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
        # <Events {} events ''>
        show i_bg_school_front as bg zorder 0:
            default
            alpha 0.0
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_cousin_default_neutral as cousin zorder 2:
            default
            xpos 0.5 
            alpha 0.0
        show i_cousin_default_neutral as alt1 zorder 3:
            default
            xpos 0.7 
            alpha 0.0
        show i_cousin_default_neutral as alt1_sil zorder 2:
            default
            xpos 0.7 
            alpha 0.0
        show i_cousin_default_neutral as alt2 zorder 3:
            default
            xpos 0.3 
            alpha 0.0
        show i_cousin_default_neutral as alt2_sil zorder 2:
            default
            xpos 0.3 
            alpha 0.0

    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bg_school_front as bg:
        # ShowWithAtl
        linear 1 alpha 1.0
    $ renpy.pause(1.0) # Text delay
    t_ch_tutorial "Welcome to Namco High, [slot_playerName]! Please click here or press Enter to progress through the game." # @t_tut00.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tutorial "Volume may be adjusted and the store may be accessed via the Options Menu in the bottom right." # @t_tut01.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tutorial "You can skip read text by pressing the Fast Forward button above that. It will light up when you can use it." # @t_tut02.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tutorial "Thanks for playing, and have fun!" # @t_tut03.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bg_school_front as bg:
        # ShowWithAtl
        linear 1 alpha 0.0
    extend "{w=1.0}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bg_classroom_a as bg
    t_ch_cousin "Here's the first thing you need to know." # @t_sintro0.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I'm just like you." # @t_sintro0.01 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # FadeEvent
        linear 1.0 alpha 1.0
    extend "{w=1.0}{nw}"
    extend " One hundred percent." # @t_sintro0.02 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "My Uncle is the King of all Cosmos..." # @t_sintro1.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    extend " Literally." # @t_sintro1.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "My cousin is the Prince. He's really good at rolling stuff up." # @t_sintro2.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Big stuff..." # @t_sintro2.01 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Little stuff..." # @t_sintro2.02 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Just..." # @t_sintro3.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Everything." # @t_sintro3.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If there's something you can think of, he's rolled it." # @t_sintro4.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He's kind of a big deal." # @t_sintro4.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "..." # @t_sintro5.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I really look up to him..." # @t_sintro6.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But I also kinda think of him as a rival." # @t_sintro6.01 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "It's a weird relationship." # @t_sintro7.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Anyway, I got to thinking... Maybe rolling runs in the family, if you know what I mean." # @t_sintro8.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "So I tried it out. Took a roll around school grounds." # @t_sintro9.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I even waited until lunch hour so I wasn't bothering anyone." # @t_sintro9.01 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I picked up a lot of stuff! Textbooks..." # @t_sintro10.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Some mix CDS (who has CDs anymore?!)..." # @t_sintro10.01 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Some games..." # @t_sintro10.02 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Lots of tasty food (our school is pretty international, y'know? Actually it's pretty intergalactic)..." # @t_sintro10.03 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " A Namco High varsity jacket (It was too big for me)..." # @t_sintro10.04 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Sports equipment, like wrestleballs and stuff…" # @t_sintro10.05 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Desks...{/cps}" # @t_sintro10.06 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Drums...{/cps}" # @t_sintro10.07 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    extend " {cps=*1.67}Drummers...{/cps}" # @t_sintro10.08 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Really it was the whole marching band...{/cps}" # @t_sintro10.09 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " {cps=*1.67}Everyone watching the marching band...{/cps}" # @t_sintro10.10 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Some cars in the parking lot...{/cps}" # @t_sintro10.11 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Principal Dig Dug's car...{/cps}" # @t_sintro10.12 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    extend " Principal Dig Dug …" # @t_sintro10.13 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I wasn't trying to cause a problem..." # @t_sintro11.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But maybe I got a little carried away." # @t_sintro11.01 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "ANYWAY, I'm exactly like you..." # @t_sintro12.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Minus all those incredibly specific details." # @t_sintro12.01 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "My point is: I just want to make it out of high school alive." # @t_sintro13.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bg_classroom_a as bg:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_cousin_default_sad as cousin
    extend "{w=0.5}{nw}"
    t_ch_cousin "But instead, I ended up here..." # @t_sintro14.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "...In detention." # @t_sintro15.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "This is where Namco High's most notorious..." # @t_sintro16.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Strangest..." # @t_sintro16.01 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Most dangerous..." # @t_sintro16.02 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Bizarre..." # @t_sintro16.03 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Bloodthirsty...." # @t_sintro16.04 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Delinquent students gather." # @t_sintro16.05 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Or so the legends say." # @t_sintro17.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I try not to look anyone in the eye. Who knows what these troublemakers will do?" # @t_sintro18.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "............" # @t_sintro19.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I just hope no one talks to me..." # @t_sintro20.00 self.block='Last'
    # <SilhouetteMacro {'actorName': '@t_ch_donko', 'actorScaleX': '0.75', 'actorScaleY': '0.75', 'actorY': '12.5%', 'appendSecond': 'true', 'cousinActor': 'cousin', 'cousinScaleX': '1', 'cousinX': '-20%', 'firstText': '@t_sintro21.00', 'name': '_u', 'realActor': 'alt1', 'realImage': '@i_donko_akimbo_wink', 'secondText': '@t_sintro21.01', 'silActor': 'alt1_sil', 'silImage': '@i_donko_akimbo_sil'} SilhouetteMacro ''>
    show i_donko_akimbo_sil as alt1_sil:
        default
        alpha 0.0
        xzoom 0.75 
        yzoom 0.75 
        ypos 0.62 
        xpos 0.7 
        linear 0.5 alpha 1.0
    t_ch_donko "WoooOOOOW! Check out THIS weirdo!" # @t_sintro21.00 self.block='NoAuto'
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom 1.0 
        linear 0.2 xpos 0.3 
    show i_donko_akimbo_sil as alt1_sil:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 0.0
    show i_donko_akimbo_wink as alt1:
        default
        alpha 0.0
        xzoom 0.75 
        yzoom 0.75 
        ypos 0.62 
        xpos 0.7 
        linear 0.5 alpha 1.0
    extend " You have your own special weirdness, don't you?" # @t_sintro21.01 self.block='NoAuto'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Um ..." # @t_sintro22.00 self.block='Last'
    # <SilhouetteMacro {'actorName': '@t_ch_mrdriller', 'appendSecond': 'false', 'cousinActor': 'cousin', 'cousinScaleX': '-1', 'cousinX': '20%', 'firstText': '@t_sintro23.00', 'lastActor': 'alt1', 'name': '_w', 'realActor': 'alt2', 'realImage': '@i_mrdriller_slumped_happy', 'secondText': '@t_sintro24.00', 'silActor': 'alt2_sil', 'silImage': '@i_mrdriller_slumped_smug_sil'} SilhouetteMacro ''>
    show i_donko_akimbo_wink as alt1:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_mrdriller_slumped_smug_sil as alt2_sil:
        default
        alpha 0.0
        xpos 0.3 
        linear 0.5 alpha 1.0
    t_ch_mrdriller "Hey!" # @t_sintro23.00 self.block='NoAuto'
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom -1.0 
        linear 0.2 xpos 0.7 
    show i_mrdriller_slumped_smug_sil as alt2_sil:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 0.0
    show i_mrdriller_slumped_happy as alt2:
        default
        alpha 0.0
        xpos 0.3 
        linear 0.5 alpha 1.0
    extend " Don't be so rude! To, uh, this weirdo ..." # @t_sintro24.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_taira', 'appendSecond': 'false', 'cousinActor': 'cousin', 'cousinScaleX': '1', 'cousinX': '-20%', 'firstText': '@t_sintro25.00', 'lastActor': 'alt2', 'name': '_x', 'realActor': 'alt1', 'realImage': '@i_taira_steveholt_happy', 'secondText': '@t_sintro26.00', 'silActor': 'alt1_sil', 'silImage': '@i_taira_steveholt_sil'} SilhouetteMacro ''>
    show i_mrdriller_slumped_happy as alt2:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_taira_steveholt_sil as alt1_sil:
        default
        alpha 0.0
        xpos 0.7 
        linear 0.5 alpha 1.0
    t_ch_taira "Oooh, you better not make the goody two-drills mad ..." # @t_sintro25.00 self.block='NoAuto'
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom 1.0 
        linear 0.2 xpos 0.3 
    show i_taira_steveholt_sil as alt1_sil:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 0.0
    show i_taira_steveholt_happy as alt1:
        default
        alpha 0.0
        xpos 0.7 
        linear 0.5 alpha 1.0
    extend " he'll sic his pops on you!" # @t_sintro26.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_aki', 'appendSecond': 'true', 'cousinActor': 'cousin', 'cousinScaleX': '-1', 'cousinX': '20%', 'firstText': '@t_sintro27.00', 'lastActor': 'alt1', 'name': '_y', 'realActor': 'alt2', 'realImage': '@i_aki_akimbo_focus', 'secondText': '@t_sintro27.01', 'silActor': 'alt2_sil', 'silImage': '@i_aki_akimbo_sil'} SilhouetteMacro ''>
    show i_taira_steveholt_happy as alt1:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_aki_akimbo_sil as alt2_sil:
        default
        alpha 0.0
        xpos 0.3 
        linear 0.5 alpha 1.0
    t_ch_aki "And just what, exactly, is wrong with being a goody two-shoes?" # @t_sintro27.00 self.block='NoAuto'
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom -1.0 
        linear 0.2 xpos 0.7 
    show i_aki_akimbo_sil as alt2_sil:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.5 alpha 0.0
    show i_aki_akimbo_focus as alt2:
        default
        alpha 0.0
        xpos 0.3 
        linear 0.5 alpha 1.0
    extend " A goody two-shoes has the makings of an exemplary student!" # @t_sintro27.01 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_max', 'cousinActor': 'cousin', 'cousinScaleX': '1', 'cousinX': '-20%', 'firstText': '@t_sintro28.00', 'lastActor': 'alt2', 'name': '_z', 'realActor': 'alt1', 'realImage': '@i_bluemax_cower_smile', 'silActor': 'alt1_sil', 'silImage': '@i_bluemax_cower_sil'} SilhouetteMacro ''>
    show i_aki_akimbo_focus as alt2:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_bluemax_cower_sil as alt1_sil:
        default
        alpha 0.0
        xpos 0.7 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom 1.0 
        linear 0.2 xpos 0.3 
    show i_bluemax_cower_smile as alt1:
        default
        alpha 0.0
        xpos 0.7 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_max "Y-yeah... ! D-don't be so mean! There’s nothing wrong with it!" # @t_sintro28.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_valkyrie', 'cousinActor': 'cousin', 'cousinScaleX': '-1', 'cousinX': '20%', 'firstText': '@t_sintro29.00', 'lastActor': 'alt1', 'name': '_10', 'realActor': 'alt2', 'realImage': '@i_valkyrie_akimbo_bored', 'silActor': 'alt2_sil', 'silImage': '@i_valkyrie_akimbo_sil'} SilhouetteMacro ''>
    show i_bluemax_cower_smile as alt1:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_valkyrie_akimbo_sil as alt2_sil:
        default
        alpha 0.0
        xpos 0.3 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom -1.0 
        linear 0.2 xpos 0.7 
    show i_valkyrie_akimbo_bored as alt2:
        default
        alpha 0.0
        xpos 0.3 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_valkyrie "What's wrong is that it's super BO-riiiiing! YAWN!" # @t_sintro29.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_meowkie', 'cousinActor': 'cousin', 'cousinScaleX': '1', 'cousinX': '-20%', 'firstText': '@t_sintro30.00', 'lastActor': 'alt2', 'name': '_11', 'realActor': 'alt1', 'realImage': '@i_meowkie_normal_forcedsmile_badge', 'silActor': 'alt1_sil', 'silImage': '@i_meowkie_normal_sil'} SilhouetteMacro ''>
    show i_valkyrie_akimbo_bored as alt2:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_meowkie_normal_sil as alt1_sil:
        default
        alpha 0.0
        xpos 0.7 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom 1.0 
        linear 0.2 xpos 0.3 
    show i_meowkie_normal_forcedsmile_badge as alt1:
        default
        alpha 0.0
        xpos 0.7 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_meowkie "HEY! I think it's brave to try to stick to the straight and narrow... Know what I mean, boss?" # @t_sintro30.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_antibravo', 'actorScaleX': '0.95', 'actorScaleY': '0.95', 'actorY': '2.5%', 'cousinActor': 'cousin', 'cousinScaleX': '-1', 'cousinX': '20%', 'firstText': '@t_sintro31.00', 'lastActor': 'alt1', 'name': '_12', 'realActor': 'alt2', 'realImage': '@i_abm_backturned_broody', 'silActor': 'alt2_sil', 'silImage': '@i_abm_backturned_sil'} SilhouetteMacro ''>
    show i_meowkie_normal_forcedsmile_badge as alt1:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_abm_backturned_sil as alt2_sil:
        default
        alpha 0.0
        xzoom 0.95 
        yzoom 0.95 
        ypos 0.53 
        xpos 0.3 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom -1.0 
        linear 0.2 xpos 0.7 
    show i_abm_backturned_broody as alt2:
        default
        alpha 0.0
        xzoom 0.95 
        yzoom 0.95 
        ypos 0.53 
        xpos 0.3 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_antibravo "The straight and narrow? Heh. Look around you. We're in detention. It's already too late. Too late for all of us..." # @t_sintro31.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_nidia', 'cousinActor': 'cousin', 'cousinScaleX': '1', 'cousinX': '-20%', 'firstText': '@t_sintro32.00', 'lastActor': 'alt2', 'name': '_13', 'realActor': 'alt1', 'realImage': '@i_nidia_akimbo_angry', 'silActor': 'alt1_sil', 'silImage': '@i_nidia_akimbo_sil'} SilhouetteMacro ''>
    show i_abm_backturned_broody as alt2:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_nidia_akimbo_sil as alt1_sil:
        default
        alpha 0.0
        xpos 0.7 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom 1.0 
        linear 0.2 xpos 0.3 
    show i_nidia_akimbo_angry as alt1:
        default
        alpha 0.0
        xpos 0.7 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_nidia "I don't think it's ever too late... But maybe it's a mistake to battle destiny..." # @t_sintro32.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_lolo', 'actorScaleX': '0.9', 'actorScaleY': '0.9', 'actorY': '5%', 'cousinActor': 'cousin', 'cousinScaleX': '-1', 'cousinX': '20%', 'firstText': '@t_sintro33.00', 'lastActor': 'alt1', 'name': '_14', 'realActor': 'alt2', 'realImage': '@i_lolo_crossed_frustrated', 'silActor': 'alt2_sil', 'silImage': '@i_lolo_crossed_sil'} SilhouetteMacro ''>
    show i_nidia_akimbo_angry as alt1:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_lolo_crossed_sil as alt2_sil:
        default
        alpha 0.0
        xzoom 0.9 
        yzoom 0.9 
        ypos 0.55 
        xpos 0.3 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom -1.0 
        linear 0.2 xpos 0.7 
    show i_lolo_crossed_frustrated as alt2:
        default
        alpha 0.0
        xzoom 0.9 
        yzoom 0.9 
        ypos 0.55 
        xpos 0.3 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_lolo "Yeah ... Like maybe we're all destined to be LOSERS." # @t_sintro33.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_tomari', 'actorScaleX': '0.95', 'actorScaleY': '0.95', 'actorY': '2.5%', 'cousinActor': 'cousin', 'cousinScaleX': '1', 'cousinX': '-20%', 'firstText': '@t_sintro34.00', 'lastActor': 'alt2', 'name': '_15', 'realActor': 'alt1', 'realImage': '@i_tomari_pondering_thinking', 'silActor': 'alt1_sil', 'silImage': '@i_tomari_pondering_sil'} SilhouetteMacro ''>
    show i_lolo_crossed_frustrated as alt2:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_tomari_pondering_sil as alt1_sil:
        default
        alpha 0.0
        xzoom 0.95 
        yzoom 0.95 
        ypos 0.53 
        xpos 0.7 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom 1.0 
        linear 0.2 xpos 0.3 
    show i_tomari_pondering_thinking as alt1:
        default
        alpha 0.0
        xzoom 0.95 
        yzoom 0.95 
        ypos 0.53 
        xpos 0.7 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_tomari "Given enough data, I COULD construct a mathematical model with a high level of predictive accuracy ... But the criteria for getting out of detention are unclear at best." # @t_sintro34.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_hiromi', 'cousinActor': 'cousin', 'cousinScaleX': '-1', 'cousinX': '20%', 'firstText': '@t_sintro35.00', 'lastActor': 'alt1', 'name': '_16', 'realActor': 'alt2', 'realImage': '@i_hiromi_akimbo_serious', 'silActor': 'alt2_sil', 'silImage': '@i_hiromi_akimbo_sil'} SilhouetteMacro ''>
    show i_tomari_pondering_thinking as alt1:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_hiromi_akimbo_sil as alt2_sil:
        default
        alpha 0.0
        xpos 0.3 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom -1.0 
        linear 0.2 xpos 0.7 
    show i_hiromi_akimbo_serious as alt2:
        default
        alpha 0.0
        xpos 0.3 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_hiromi "Tch. No thanks. I'd rather figure it out as I go." # @t_sintro35.00 self.block='NoAuto'
    # <SilhouetteMacro {'actorName': '@t_ch_albatros', 'cousinActor': 'cousin', 'cousinScaleX': '1', 'cousinX': '-20%', 'firstText': '@t_sintro36.00', 'lastActor': 'alt2', 'name': '_17', 'realActor': 'alt1', 'realImage': '@i_albatross_welcome_smirk_wink', 'silActor': 'alt1_sil', 'silImage': '@i_albatross_welcome_sil'} SilhouetteMacro ''>
    show i_hiromi_akimbo_serious as alt2:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_albatross_welcome_sil as alt1_sil:
        default
        alpha 0.0
        xpos 0.7 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xzoom 1.0 
        linear 0.2 xpos 0.3 
    show i_albatross_welcome_smirk_wink as alt1:
        default
        alpha 0.0
        xpos 0.7 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_albatros "Yes I agree, classmate! Let's all go on an unpredictable adventure likely to end in criminal activity!" # @t_sintro36.00 self.block='NoAuto'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_sil as alt2:
        # ShowWithAtl
        ypos 1.5 
        # ShowWithAtl
        alpha 1.0
        # ShowWithAtl
        linear 0.25 ypos 0.5 
    $ renpy.pause(0.25) # Image change
    show i_miller_aliens_serious as alt2
    with Dissolve(.75)
    show i_albatross_welcome_smirk_wink as alt1:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_cousin_default_surprised as cousin:
        linear 0 xzoom -1.0 
        # ShowWithAtl
        linear 0.25 xpos 0.7 
    extend "{w=0.5}{nw}"
    t_ch_miller "Did someone say ... Vast global conspiracy all around us every waking moment of every day?!" # @t_sintro37.00 self.block='Last'
    # <SilhouetteMacro {'actorName': '@t_ch_galaga', 'cousinActor': 'cousin', 'cousinScaleX': '1', 'cousinX': '-20%', 'firstText': '@t_sintro38.00', 'lastActor': 'alt2', 'name': '_19', 'realActor': 'alt1', 'realImage': '@i_galaga_default', 'silActor': 'alt1_sil', 'silImage': '@i_galaga_default_sil'} SilhouetteMacro ''>
    show i_miller_aliens_serious as alt2:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_galaga_default_sil as alt1_sil:
        default
        alpha 0.0
        xpos 0.7 
        linear 0.5 alpha 1.0
        # ActorEvent
        # ActorEvent (Transition only)
        pause 0.5
        linear 0.5 alpha 0.0
    show i_cousin_default_surprised as cousin:
        # ActorEvent
        xzoom 1.0 
        linear 0.2 xpos 0.3 
    show i_galaga_default as alt1:
        default
        alpha 0.0
        xpos 0.7 
        pause 0.5
        linear 0.5 alpha 1.0
    t_ch_galaga "{smallcaps}GALAGA DOES NOT THINK ANYBODY SAID THAT{/smallcaps}" # @t_sintro38.00 self.block='NoAuto'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    hide alt1_sil
    hide alt2_sil
    show i_galaga_default as alt1:
        # FadeEvent
        linear 0.333 alpha 0.0
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.5 
    extend "{w=0.333}{nw}"
    t_ch_cousin "(What an energetic group… !)" # @t_sintro39.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Um..." # @t_sintro40.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Guys...!!" # @t_sintro40.01 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(They're all arguing with each other. They've totally forgotten about me.)" # @t_sintro41.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I've gotta admit, they're not at all what I expected. Well ... Some of them.)" # @t_sintro42.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(You know ... Now that I think about it ... )" # @t_sintro43.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(It must take someone really scary to keep these students in line ... )" # @t_sintro44.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(REALLY scary ...)" # @t_sintro45.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar1.ogg"

    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "!!! Was that a ..." # @t_sintro46.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    extend " Roar?!" # @t_sintro46.01 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_angry as alt1:
        # ActorEvent
        xpos -0.3 
        alpha 1.0
        linear 0.333 xpos 0.2 
    extend "{w=0.333}{nw}"
    t_ch_taira "Oh no ... He's here!" # @t_sintro47.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(What could possibly scare this scary guy?!)" # @t_sintro48.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_shocked as alt2:
        # ActorEvent
        xpos 1.3 
        xzoom -1.0 
        alpha 1.0
        linear 0.333 xpos 0.8 
    extend "{w=0.333}{nw}"
    t_ch_aki "Everyone sit down! Quickly!" # @t_sintro49.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Y-yeah! What she said!" # @t_sintro50.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Weren't they just yelling at each other?!)" # @t_sintro51.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_angry as alt1:
        # FadeEvent
        linear 0.333 alpha 0.0
    show i_aki_default_shocked as alt2:
        # FadeEvent
        linear 0.333 alpha 0.0
    show i_cousin_default_surprised as cousin:
        # FadeEvent
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Hello... students." # @t_sintro52.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_right as digdug zorder 3:
        default
        alpha 0.0
        xpos 0.4 
        linear 1 alpha 1.0
    show i_king_confident as king zorder 2:
        default
        alpha 0.0
        xpos 0.3 
        linear 1 alpha 1.0
    extend "{w=1.0}{nw}"
    extend " So nice to see you." # @t_sintro52.01 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I recognize some of you." # @t_sintro53.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "And I see some new faces." # @t_sintro54.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Rest assured… I’m memorizing all of them." # @t_sintro55.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Allow me to introduce myself." # @t_sintro56.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I’m Dig Dug…. your principal." # @t_sintro57.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "My fellow faculty member here is King… called such because he is King of the ring." # @t_sintro58.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "But here..." # @t_sintro59.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Here…" # @t_sintro60.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Here he is the King of DETENTION!" # @t_sintro61.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Ahem. King has prepared a statement, which I am to read to you." # @t_sintro62.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king:
        # ShowWithAtl
        linear .333 xpos 0.4 
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear .20 xpos 0.55 
    extend "{w=0.333}{nw}"
    t_ch_digdug "\"I became a wrestler because I wanted to raise money for the children. Good children. Not like you miscreants.\"" # @t_sintro63.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king:
        # ShowWithAtl
        linear .333 xpos 0.5 
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear .20 xpos 0.65 
    extend "{w=0.333}{nw}"
    t_ch_digdug "\"It's the reason I've become a part-time teacher here at Namco High.\"" # @t_sintro64.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king:
        # ShowWithAtl
        linear .333 xpos 0.65 
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear .20 xpos 0.73 
    extend "{w=0.333}{nw}"
    t_ch_digdug "\"This place is like the orphanage where I grew up, only back home we were abandoned by our families.\"" # @t_sintro65.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_screaming as king
    play sound "sfx/kingroar2.ogg"
    show i_king_screaming as king:
        xzoom -1.0 
    show i_digdug_right as digdug:
        xzoom -1.0 
    t_ch_digdug "\"This room is an orphanage for people abandoned by their better judgement!!\"" # @t_sintro66.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What is Dig Dug even saying... This man, King... Is he even a man?)" # @t_sintro67.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_screaming as king:
        # ShowWithAtl
        linear .333 xpos 0.5 
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear .20 xpos 0.45 
    extend "{w=0.333}{nw}"
    t_ch_digdug "\"There was a time when I was forbidden from fighting students…\"" # @t_sintro68.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king:
        xzoom 1.0 
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear .5 xpos 0.35 
    extend "{w=0.5}{nw}"
    t_ch_digdug "\"So I defeated the principal.\"" # @t_sintro69.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "*cough*" # @t_sintro70.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar3.ogg"
    show i_king_screaming as king
    show i_digdug_right as digdug:
        # ShowWithAtl
        pause 0.25 
        linear 0.5 ypos 0.25 
        # ShowWithAtl
        pause 0.5 
        linear .25 xpos 0.2 
        pause 0.75
        xzoom 1.0 
        # ShowWithAtl
        pause 1.0 
        linear 0.5 ypos 0.5 
    $ renpy.pause(1.5) # TimedPause
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wait… is principal Dig Dug ALSO scared of this man?!)" # @t_sintro71.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king
    t_ch_digdug "\"Now I can do whatever I want!!\"" # @t_sintro72.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear 1 xpos 0.35 
    extend "{w=1.0}{nw}"
    t_ch_digdug "\"So let me know if you want to have a go. I'm ready!\"" # @t_sintro73.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(This man... Is crazy...!!)" # @t_sintro74.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear 0.25 xpos 0.8 
        pause 0.30
        xzoom -1.0 
    extend "{w=0.3}{nw}"
    t_ch_digdug "\"Lucky for you, I'm not a tyrant! We will work TOGETHER to mold you into better students. Students of TOMORROW.\"" # @t_sintro75.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "\"You will be like clay in my formidable paws.\"" # @t_sintro76.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " \"... Er, hands.\"" # @t_sintro76.01 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "\"Some of you seem to think that you have reached rock-bottom...\"" # @t_sintro77.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    extend " \"But I assure you... It could be much worse.\"" # @t_sintro77.01 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king:
        # ShowWithAtl
        linear 0.5 xpos 0.35 
    extend "{w=0.5}{nw}"
    t_ch_digdug "\"I grew up on the STREETS. I fought everyone... and everything. I was undisciplined... Raw... Angry... I ate RATS …\"" # @t_sintro78.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_digdug "\"One time I fought a kangaroo...\"" # @t_sintro79.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "\"And a panda...\"" # @t_sintro80.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " \"And a dinosaur...\"" # @t_sintro80.01 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_digdug "\"You have it easy. Or you would, if you weren't in here with me.\"" # @t_sintro81.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "...hmm." # @t_sintro82.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I don't know where he’s going with this. Let's take roll!" # @t_sintro83.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I'M GONNA DIE HERE...)" # @t_sintro84.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king:
        # FadeEvent
        linear 0.333 alpha 0.0
    show i_digdug_right as digdug:
        # FadeEvent
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Mr. Driller!" # @t_sintro85.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_mrdriller_slumped_smug as mrdriller:
        default
        # ActorEvent
        xpos 0.5 
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_mrdriller "Here!" # @t_sintro86.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    extend " When do we start our morning drills?" # @t_sintro86.01 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_smug as mrdriller:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Aki Matsuo!" # @t_sintro87.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_smile as aki:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_aki "Here." # @t_sintro88.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_distracted as aki
    play sound "sfx/sentaisignal.ogg"
    extend " But I may have to leave soon ... I have responsibilities to attend to." # @t_sintro88.01 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_distracted as aki:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "ALFONSO B. TROSS" # @t_sintro89.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk as albatros:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_albatros "THIS COMPLETELY NORMAL STUDENT IS HERE" # @t_sintro90.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk_wink as albatros
    extend " AND READY TO MAKE SOME TROUBLED FRIENDS" # @t_sintro90.01 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk_wink as albatros:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Yuichiro Tomari!" # @t_sintro91.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_thinking as tomari:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_tomari "Present, sir." # @t_sintro92.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I've been collecting some very interesting data..." # @t_sintro92.01 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_thinking as tomari:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Nidia!" # @t_sintro93.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_angry as nidia:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_nidia "I was destined to be here..." # @t_sintro94.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And so I am." # @t_sintro94.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_angry as nidia:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Richard Miller." # @t_sintro95.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_serious as miller:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_miller "SHHHH!" # @t_sintro96.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_shocked as miller
    extend " THEY will know I’m here!" # @t_sintro96.01 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_shocked as miller:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Hiromi Tengenji." # @t_sintro97.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_akimbo_serious as hiromi:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_hiromi "............." # @t_sintro98.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ......here in record time." # @t_sintro98.01 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_akimbo_serious as hiromi:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Blue Max!" # @t_sintro99.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_max "Squadron Leader Blue Max," # @t_sintro100.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " reporting for duty sir!" # @t_sintro100.01 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Donko!" # @t_sintro101.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_meloncholic as donko:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_donko "I'm, like, totally here, y'know?" # @t_sintro102.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    extend " Don!" # @t_sintro102.01 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Meowkie." # @t_sintro103.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_meowkie "Yep." # @t_sintro104.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Right here, boss!" # @t_sintro104.01 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Valkyrie." # @t_sintro105.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_akimbo_bored as valkyrie:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_valkyrie "Heeeeere!" # @t_sintro106.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_akimbo_wink as valkyrie
    extend " Have I ever told you I'm a cat person?" # @t_sintro106.01 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_akimbo_wink as valkyrie:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "G-Galaga!" # @t_sintro107.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_default as galaga:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_galaga "{smallcaps}GALAGA{/smallcaps}" # @t_sintro108.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}IS PRESENT.{/smallcaps}" # @t_sintro108.01 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_default as galaga:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Taira no Kagekiyo." # @t_sintro109.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused as taira:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_taira "Yeah yeah ... I'm here." # @t_sintro110.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_serious as taira
    extend " WRESTLEBALL RULES!" # @t_sintro110.01 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_serious as taira:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Lolo." # @t_sintro111.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_lolo "Uh-huh ... Yeah. Here." # @t_sintro112.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " For now, I guess." # @t_sintro112.01 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Anti-Bravoman!" # @t_sintro113.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_backturned_broody as antibravo:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_antibravo "Here..." # @t_sintro114.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " and so is my darkness..." # @t_sintro114.01 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_backturned_broody as antibravo:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Ah… and those weird transfer students…" # @t_sintro115.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Jane Crocker." # @t_sintro116.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_armscrossed_grin as jane:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_jane "HIIIIIII! :)" # @t_sintro117.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_armscrossed_smile as jane
    extend " Let’s all have fun, now." # @t_sintro117.01 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_armscrossed_smile as jane:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Terezi." # @t_sintro118.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_grin as terezi:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_terezi "H3H3H3… 1’M H3R3, P41NC1P4L." # @t_sintro119.00 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_laugh as terezi
    extend " 4ND 1’V3 GOT MY 3Y3 ON YOU! ;]" # @t_sintro119.01 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_laugh as terezi:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "Er… okay… where was I. Oh… Davesprite!" # @t_sintro120.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_davesprite_standing_disinterest as davesprite:
        default
        # ActorEvent
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_davesprite "sup" # @t_sintro121.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_davesprite_standing_disinterest as davesprite:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "And our newest face... [slot_playerName]!" # @t_sintro122.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ActorEvent
        xpos 0.5 
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_cousin "Y-yeah." # @t_sintro123.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I'm here.........." # @t_sintro123.01 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "...." # @t_sintro124.00 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king:
        # ShowWithAtl
        linear 0.333 alpha 1.0
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_digdug "I ... I can't believe it." # @t_sintro125.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_screaming as king
    play sound "sfx/kingroar2.ogg"
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear 0.5 ypos 0.25 
    extend "{w=0.5}{nw}"
    extend " Everyone's here!" # @t_sintro125.01 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear 0.5 ypos 0.5 
    extend "{w=0.5}{nw}"
    extend " There's hope for you lowlifes yet!" # @t_sintro125.02 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Since we have a new inmate ... Er, student ... I'm obligated to explain how detention works." # @t_sintro126.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "You did your crime, now you serve the time!" # @t_sintro127.00 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "BUT:" # @t_sintro128.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You can shorten your sentence in one of two ways." # @t_sintro128.01 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king
    t_ch_digdug "The first is to join a club to show your school spirit." # @t_sintro129.00 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "If we can see that you care and we are impressed by the amount of effort you put forth, your afternoons will be set free next week." # @t_sintro130.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "It's a lot of hard work, but you're sure to learn something about yourself!" # @t_sintro131.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "The second is to let King try his new wrestling move on you." # @t_sintro132.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He calls it the \"Student Body Reformer\"." # @t_sintro132.01 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_screaming as king
    play sound "sfx/kingroar1.ogg"
    extend " One time on the receiving end of it and you'll never want to cause trouble again!" # @t_sintro132.02 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Any takers?" # @t_sintro133.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(OF COURSE NOT! We all… want to live… !!)" # @t_sintro134.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "H-haha ... How about that old school spirit! Go Namco High ... !" # @t_sintro135.00 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king
    t_ch_digdug "Even in your youth, you have wisdom… don’t wrestle him. Not even for funsies." # @t_sintro136.00 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I wouldn’t dream of it…" # @t_sintro137.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Because it absolutely constitutes some kind of harassment!)" # @t_sintro138.00 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear 0.5 ypos 0.25 
    show i_king_screaming as king
    extend "{w=0.5}{nw}"
    t_ch_digdug "Eh? King? Oh, you think our new student has something to share? Do you have something to say, [slot_playerName]?" # @t_sintro139.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Nothing sir!!" # @t_sintro140.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear 0.5 ypos 0.5 
    show i_king_confident as king
    extend "{w=0.5}{nw}"
    t_ch_cousin "(Is he psychic?! Is it some kind of ... teacher power?!)" # @t_sintro141.00 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Hmmm. I think he likes you." # @t_sintro142.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_screaming as king
    t_ch_digdug "Orrrrr he hates you. Hard to tell." # @t_sintro143.00 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Stoicism does not suit you." # @t_sintro144.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I encourage you to make friends, [slot_playerName]!" # @t_sintro145.00 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king
    t_ch_digdug "Speak to your fellow students." # @t_sintro146.00 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They’re all enrolled in at least one of the school clubs.." # @t_sintro146.01 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar3.ogg"

    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "What’s that? Oh…" # @t_sintro147.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "King says: \"Friendship is very important! Sometimes the man you are about to kill in cold blood can become your greatest friend.\"" # @t_sintro148.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "You must look deep into their eyes to know this." # @t_sintro149.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I see friendship in your eyes, [slot_playerName]. Good luck!" # @t_sintro150.00 self.block='Last'
    # <NHSceneChange {'name': '_3V', 'scene': '@s_day0'} NHSceneChange ''>
    label s_intro__3V:
        # <NHSceneChange {'name': '_3V', 'scene': '@s_day0'} NHSceneChange ''>
        jump s_day0