define scene_picked_once_amazona = False
define scene_picked_once_albatros = False
define scene_picked_once_antibravo = False
define scene_picked_once_bluemax = False
define scene_picked_once_davesprite = False
define scene_picked_once_donko = False
define scene_picked_once_galaga = False
define scene_picked_once_hiromi = False
define scene_picked_once_jane = False
define scene_picked_once_lolo = False
define scene_picked_once_meowkie = False
define scene_picked_once_mrdriller = False
define scene_picked_once_nidia = False
define scene_picked_once_richard = False
define scene_picked_once_taira = False
define scene_picked_once_terezi = False
define scene_picked_once_tomari = False
define scene_picked_once_valk = False
define slot_picked_amazona_day1 = False
define slot_picked_albatros_day1 = False
define slot_picked_antibravo_day1 = False
define slot_picked_bluemax_day1 = False
define slot_picked_davesprite_day1 = False
define slot_picked_donko_day1 = False
define slot_picked_galaga_day1 = False
define slot_picked_hiromi_day1 = False
define slot_picked_jane_day1 = False
define slot_picked_lolo_day1 = False
define slot_picked_meowkie_day1 = False
define slot_picked_mrdriller_day1 = False
define slot_picked_nidia_day1 = False
define slot_picked_richard_day1 = False
define slot_picked_taira_day1 = False
define slot_picked_terezi_day1 = False
define slot_picked_tomari_day1 = False
define slot_picked_valk_day1 = False
define slot_pick_count_amazona = 0
define slot_pick_count_albatros = 0
define slot_pick_count_antibravo = 0
define slot_pick_count_bluemax = 0
define slot_pick_count_davesprite = 0
define slot_pick_count_donko = 0
define slot_pick_count_galaga = 0
define slot_pick_count_hiromi = 0
define slot_pick_count_jane = 0
define slot_pick_count_lolo = 0
define slot_pick_count_meowkie = 0
define slot_pick_count_mrdriller = 0
define slot_pick_count_nidia = 0
define slot_pick_count_richard = 0
define slot_pick_count_taira = 0
define slot_pick_count_terezi = 0
define slot_pick_count_tomari = 0
define slot_pick_count_valk = 0
# <Scene {'id': 's_day2.5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_day2p5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_day2p5"
    $ renpy.pause(1)
    # <Scene {'id': 's_day2.5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'day2.5initialize'} ParallelEvent ''>
    label s_day2p5_day2p5initialize:
        # <ParallelEvent {'auto': 'true', 'name': 'day2.5initialize'} ParallelEvent ''>
        # <Events {} events ''>
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        # Pass (VarEnsure)
        show i_bg_school_front as school zorder 9 at default
        show i_bg_classroom_a as bg zorder 1 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_sw_white as white_swatch zorder 15:
            default
            alpha 0.0
        show i_cousin_default_neutral as cousin zorder 2:
            default
            xpos 0.25 
        show i_king_confident as king zorder 2:
            default
            xpos 0.7 
            xzoom -1.0 
        show i_digdug_left as digdug zorder 3:
            default
            xpos 0.7 

    # <ParallelEvent {'auto': 'true', 'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bg_school_front as school:
        # ShowWithAtl
        pause 8.0 
        linear 1 alpha 0.0
    play sound "sfx/westminster.ogg"
    narrator "The next day ...{nw}" # @t_ui_nextday self.block=False
    extend "{w=17.0}{nw}"
    # Blank text event <TextEvent {'char': '', 'delay': '8', 'text': ''} TextEvent ''>
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    hide school
    play music "bgm/aroundtown.ogg" loop
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_digdug "Another round of perfect attendance..." # @t_scousin30.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Splendid!" # @t_scousin30.01 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Now if you keep this up maybe one day you’ll get to leave." # @t_scousin31.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_digdug "See you at the bell." # @t_scousin32.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    hide king
    hide digdug
    t_ch_cousin "(Everyone seems so restless, I wonder what they’re planning to do today?)" # @t_scousin33.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': 'day2.5prechoice'} ParallelEvent ''>
    label s_day2p5_day2p5prechoice:
        # <ParallelEvent {'auto': 'true', 'name': 'day2.5prechoice'} ParallelEvent ''>
        # <Events {} events ''>
        show i_cousin_default_neutral as cousin:
            # ShowWithAtl
            linear 0.5 alpha 0.0
        extend "{w=0.5}{nw}"
        # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    $ s_day2p5_has_picked_any = False if not "s_day2p5_has_picked_any" in store.__dict__ else s_day2p5_has_picked_any
    window hide
    menu (screen="ChoiceExploration"):
        "Aki Matsuo":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_amazona
        "Albatross":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_albatros
        "Anti-Bravoman":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_antibravo
        "Blue Max":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_bluemax
        "Davesprite":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_davesprite
        "Donko":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_donko
        "Galaga":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_galaga
        "Hiromi":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_hiromi
        "Jane Crocker":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_jane
        "Lolo":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_lolo
        "Meowkie":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_meowkie
        "Mr. Driller":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_mrdriller
        "Nidia":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_nidia
        "Richard Miller":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_richard
        "Taira":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_taira
        "Terezi Pyrope":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_terezi
        "Tomari":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_tomari
        "Valkyrie":
            $ s_day2p5_has_picked_any = True
            window show
            jump s_day2p5_valk
        "Wait for detention to end." if s_day2p5_has_picked_any:
            window show
            jump s_day2p5_cousin
    # <Macro {'name': 'albatros'} Macro ''>
    label s_day2p5_albatros:
        # <Macro {'name': 'albatros'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_albatros:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_albatros}'} IfFalse ''>
            label s_day2p5_albatros_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_albatros}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_albatros_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_albatross_toocool_smirk as albatros zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_albatross_toocool_smirk as albatros
                t_ch_albatros "You ready to skip detention?" # @t_salbatros2500.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_albatros "I’m headed to the roof." # @t_salbatros237.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_albatros "You should join me." # @t_salbatros238.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_albatros "For now, I must disappear mysteriously!" # @t_salbatros239.00 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                extend " HA-CHA!" # @t_salbatros239.01 self.block='Last'
                show i_albatross_toocool_smirk as albatros:
                    # ShowWithAtl
                    linear 1.5 xpos 1.2 
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "!!!" # @t_salbatros240.00 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_mortified as cousin
                extend " Wait. How was that mysterious?" # @t_salbatros240.01 self.block='Last'
                # <ParallelEvent {'name': '_9'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "All he did was go out the door" # @t_salbatros241.00 self.block='Last'
                menu:
                    "Al wanted me to meet him on the roof...?"

                    "JOIN AL ON THE ROOF":
                        $ slot_picked_albatros_day3 = True
                    "LEAVE AL TO THE BIRDS":
                        $ slot_picked_albatros_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_albatros_day3}', 'name': '_B', 'path': 'albatros/Chosen'} BranchMacro ''>
                if not not slot_picked_albatros_day3:
                    jump s_day2p5_albatros_Chosen
                jump s_day2p5_albatros_PassedFirstTime
        if scene_picked_once_albatros:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_albatros}'} IfTrue ''>
            label s_day2p5_albatros_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_albatros}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_albatros_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(Hrm, what about Al, though…" # @t_salbatros244.00 self.block='Last'
                menu:
                    "Al wanted me to meet him on the roof...?"

                    "JOIN AL ON THE ROOF":
                        $ slot_picked_albatros_day3 = True
                    "LEAVE AL TO THE BIRDS":
                        $ slot_picked_albatros_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_albatros_day3}', 'name': '_3', 'path': 'albatros/Chosen'} BranchMacro ''>
                if not not slot_picked_albatros_day3:
                    jump s_day2p5_albatros_Chosen
                jump s_day2p5_albatros_PassedLoop
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_albatros_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Hmm, there’s something more to Al than his good looks and charm. I better get to the bottom of it…)" # @t_salbatros242.00 self.block='Last'
            $ slot_pick_count_albatros += 1
            # <NHSceneChange {'name': '_2', 'scene': 's_albatros3'} NHSceneChange ''>
            label s_day2p5_albatros_Chosen__2:
                # <NHSceneChange {'name': '_2', 'scene': 's_albatros3'} NHSceneChange ''>
                jump s_albatros3
        # <Macro {'name': 'PassedFirstTime'} Macro ''>
        label s_day2p5_albatros_PassedFirstTime:
            # <Macro {'name': 'PassedFirstTime'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(I dunno, hanging out on the roof sounds a pretty lame way to skip class and risk getting caught!)" # @t_salbatros243.00 self.block='Last'
        jump s_day2p5_albatros_cleanup
        # <Macro {'name': 'PassedLoop'} Macro ''>
        label s_day2p5_albatros_PassedLoop:
            # <Macro {'name': 'PassedLoop'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(I dunno, he’s a little strange. Even for a Namco High student!)" # @t_salbatros246.00 self.block='Last'
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_albatros_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_albatros_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_albatross_toocool_smirk as albatros:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_albatros_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide albatros
                # Pass (ActorReset)
                $ scene_picked_once_albatros = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'amazona'} Macro ''>
    label s_day2p5_amazona:
        # <Macro {'name': 'amazona'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_amazona:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_amazona}'} IfFalse ''>
            label s_day2p5_amazona_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_amazona}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_amazona_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_aki_default_smile as aki zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_aki_default_smile as aki
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Hey Aki!" # @t_samazona30.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_aki_default_nervouslaughter as aki
                t_ch_aki "Hi [slot_playerName]... Hahahaha!" # @t_samazona31.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "(Could that be... Nervous laughter?)" # @t_samazona32.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Aki..." # @t_samazona33.00 self.block='Last'
                menu:
                    "Hang out with Aki?"

                    "Could I tag along with you today?":
                        $ slot_picked_amazona_day3 = True
                    "I'm going to go.":
                        $ slot_picked_amazona_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_amazona_day3}', 'name': '_6', 'path': 'amazona/Chosen'} BranchMacro ''>
                if not not slot_picked_amazona_day3:
                    jump s_day2p5_amazona_Chosen
                jump s_day2p5_amazona_Passed
        if scene_picked_once_amazona:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_amazona}'} IfTrue ''>
            label s_day2p5_amazona_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_amazona}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_amazona_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_aki_default_nervouslaughter as aki zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "You seem nervous today, Aki." # @t_samazona313.00a self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_aki_akimbo_laughter_nervous as aki
                t_ch_aki "Hahahahaha… what are you talking about, [slot_playerName]?" # @t_samazona313.00b self.block='Last'
                menu:
                    "Hang out with Aki?"

                    "Could I tag along with you today?":
                        $ slot_picked_amazona_day3 = True
                    "I'm going to go.":
                        $ slot_picked_amazona_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_amazona_day3}', 'name': '_4', 'path': 'amazona/Chosen'} BranchMacro ''>
                if not not slot_picked_amazona_day3:
                    jump s_day2p5_amazona_Chosen
                jump s_day2p5_amazona_Passed
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_amazona_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "Could I tag along with you today?" # @t_samazona34.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_aki_akimbo_distracted as aki
            t_ch_aki "Oh... Um... Hahahaha! I don't know [slot_playerName]." # @t_samazona35.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_exhausted_grin as cousin
            t_ch_cousin "Pleaaaaaase?" # @t_samazona36.00 self.block='Last'
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "(She'll definitely be a good influence on me!)" # @t_samazona37.00 self.block='Last'
            # <ParallelEvent {'name': '_4'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "(And I have to admit, her nervous laughter is making me wonder... )" # @t_samazona38.00 self.block='Last'
            # <ParallelEvent {'name': '_5'} ParallelEvent ''>
            # <Events {} events ''>
            show i_aki_akimbo_laughter_nervous as aki
            t_ch_aki "I have to practice for the school play, though. Do you mind?" # @t_samazona39.00 self.block='Last'
            # <ParallelEvent {'name': '_6'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "I'll help however I can!" # @t_samazona310.00 self.block='Last'
            $ slot_pick_count_amazona += 1
            # <NHSceneChange {'name': '_8', 'scene': 's_amazona3'} NHSceneChange ''>
            label s_day2p5_amazona_Chosen__8:
                # <NHSceneChange {'name': '_8', 'scene': 's_amazona3'} NHSceneChange ''>
                jump s_amazona3
        # <Macro {'name': 'Passed'} Macro ''>
        label s_day2p5_amazona_Passed:
            # <Macro {'name': 'Passed'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "I'm going to go..." # @t_samazona311.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_aki_akimbo_laughter_nervous as aki
            t_ch_aki "No problem, [slot_playerName]! We've all got a lot to do. Hahahaha!" # @t_samazona312.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(That... suspicious laugh... )" # @t_samazona313.00 self.block='Last'
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_amazona_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_amazona_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_aki_akimbo_laughter_nervous as aki:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_mortified as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_amazona_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide aki
                # Pass (ActorReset)
                $ scene_picked_once_amazona = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'antibravo'} Macro ''>
    label s_day2p5_antibravo:
        # <Macro {'name': 'antibravo'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_antibravo:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_antibravo}'} IfFalse ''>
            label s_day2p5_antibravo_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_antibravo}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_antibravo_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_abm_default_broody as antibravo zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_abm_default_broody as antibravo
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Hey Anti-Bravo. Want to head over to Poetry Club?" # @t_santibravo30.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_abm_shadowknows_broody as antibravo
                t_ch_antibravo "S-sure... It's not like I have... dark deeds... to do." # @t_santibravo31.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "(He's very theatrical... )" # @t_santibravo32.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Cool... So let's go!" # @t_santibravo33.00 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                show i_abm_shadowknows_surprised as antibravo:
                    linear 0.25 xzoom -1.0 
                t_ch_antibravo "Now?! Together?!" # @t_santibravo34.00 self.block='Last'
                # <ParallelEvent {'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "Yes... ?" # @t_santibravo35.00 self.block='Last'
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_antibravo "Um... How about... We race!" # @t_santibravo36.00 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                show i_abm_default_surprised as antibravo
                extend " Yes, let's race!" # @t_santibravo36.01 self.block='Last'
                menu:
                    "Race Anti-Bravoman?"

                    "Sure!":
                        $ slot_picked_antibravo_day3 = True
                    "Maybe not...":
                        $ slot_picked_antibravo_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_antibravo_day3}', 'name': '_A', 'path': 'antibravo/Chosen'} BranchMacro ''>
                if not not slot_picked_antibravo_day3:
                    jump s_day2p5_antibravo_Chosen
                jump s_day2p5_antibravo_Passed
        if scene_picked_once_antibravo:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_antibravo}'} IfTrue ''>
            label s_day2p5_antibravo_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_antibravo}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_antibravo_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_abm_default_broody as antibravo zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_abm_backturned_surprised as antibravo
                t_ch_cousin "Let’s hang out, Anti-Bravoman!" # @t_santibravo312.00a self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_antibravo "Sure… humans hang out to become close to one another. So obviously we should… run away from each other! Let’s race!" # @t_santibravo312.00b self.block='Last'
                menu:
                    "Race Anti-Bravoman?"

                    "Sure!":
                        $ slot_picked_antibravo_day3 = True
                    "Maybe not...":
                        $ slot_picked_antibravo_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_antibravo_day3}', 'name': '_4', 'path': 'antibravo/Chosen'} BranchMacro ''>
                if not not slot_picked_antibravo_day3:
                    jump s_day2p5_antibravo_Chosen
                jump s_day2p5_antibravo_Passed
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_antibravo_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "Sure!" # @t_santibravo37.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_abm_backturned_surprised as antibravo:
                linear 0.25 xzoom 1.0 
            t_ch_antibravo "Er... Great! GO!" # @t_santibravo38.00 self.block='Last'
            show i_abm_backturned_surprised as antibravo:
                # FadeEvent
                linear 0.5 alpha 0.0
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_energetic_surprise as cousin
            t_ch_cousin "(AH! He took off! After him!)" # @t_santibravo39.00 self.block='Last'
            $ slot_pick_count_antibravo += 1
            # <NHSceneChange {'name': '_5', 'scene': 's_antibravo3'} NHSceneChange ''>
            label s_day2p5_antibravo_Chosen__5:
                # <NHSceneChange {'name': '_5', 'scene': 's_antibravo3'} NHSceneChange ''>
                jump s_antibravo3
        # <Macro {'name': 'Passed'} Macro ''>
        label s_day2p5_antibravo_Passed:
            # <Macro {'name': 'Passed'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Maybe not..." # @t_santibravo310.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_antibravo "Okay! Great!" # @t_santibravo311.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_exhausted_mortified as cousin
            t_ch_cousin "(What a weird reaction... )" # @t_santibravo312.00 self.block='Last'
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_antibravo_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_antibravo_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_abm_backturned_surprised as antibravo:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_exhausted_mortified as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_antibravo_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide antibravo
                # Pass (ActorReset)
                $ scene_picked_once_antibravo = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'bluemax'} Macro ''>
    label s_day2p5_bluemax:
        # <Macro {'name': 'bluemax'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_bluemax:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_bluemax}'} IfFalse ''>
            label s_day2p5_bluemax_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_bluemax}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_bluemax_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_bluemax_stand_worried as bluemax zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_bluemax_stand_worried as bluemax
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Hey Blue Max!" # @t_sbluemax250.00c self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_bluemax_stand_worried as bluemax
                t_ch_max "Hey [slot_playerName]! I hope you can join me at the cafe later. Y’know. To talk about SECRET stuff." # @t_sbluemax250.00d self.block='Last'
                menu:
                    "Join Blue Max at the cafe today?"

                    "Sure!":
                        $ slot_picked_bluemax_day3 = True
                    "Forget it!":
                        $ slot_picked_bluemax_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_bluemax_day3}', 'name': '_4', 'path': 'bluemax/Chosen'} BranchMacro ''>
                if not not slot_picked_bluemax_day3:
                    jump s_day2p5_bluemax_Chosen
                jump s_day2p5_bluemax_PassedFirstTime
        if scene_picked_once_bluemax:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_bluemax}'} IfTrue ''>
            label s_day2p5_bluemax_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_bluemax}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_bluemax_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_bluemax_stand_worried as bluemax zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_bluemax_stand_worried as bluemax
                t_ch_max "[slot_playerName]. You in?" # @t_sbluemax254.00 self.block='Last'
                menu:
                    "Join Blue Max at the cafe today?"

                    "Sure!":
                        $ slot_picked_bluemax_day3 = True
                    "Forget it!":
                        $ slot_picked_bluemax_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_bluemax_day3}', 'name': '_3', 'path': 'bluemax/Chosen'} BranchMacro ''>
                if not not slot_picked_bluemax_day3:
                    jump s_day2p5_bluemax_Chosen
                jump s_day2p5_bluemax_PassedLoop
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_bluemax_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_surprised as cousin
            show i_bluemax_stand_worried as bluemax
            t_ch_cousin "Sounds a little risky, but I’m in!" # @t_sbluemax252.00 self.block='Last'
            $ slot_pick_count_bluemax += 1
            # <NHSceneChange {'name': '_2', 'scene': 's_bluemax3'} NHSceneChange ''>
            label s_day2p5_bluemax_Chosen__2:
                # <NHSceneChange {'name': '_2', 'scene': 's_bluemax3'} NHSceneChange ''>
                jump s_bluemax3
        # <Macro {'name': 'PassedFirstTime'} Macro ''>
        label s_day2p5_bluemax_PassedFirstTime:
            # <Macro {'name': 'PassedFirstTime'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            show i_bluemax_stand_worried as bluemax
            t_ch_cousin "I dunno, Max. I’ll think about it, okay?" # @t_sbluemax253.00 self.block='Last'
            jump s_day2p5_bluemax_cleanup
        # <Macro {'name': 'PassedLoop'} Macro ''>
        label s_day2p5_bluemax_PassedLoop:
            # <Macro {'name': 'PassedLoop'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            show i_bluemax_stand_worried as bluemax
            t_ch_cousin "I dunno, Max. I’ll think about it, okay?" # @t_sbluemax252.00a self.block='Last'
            jump s_day2p5_bluemax_cleanup
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_bluemax_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_bluemax_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_bluemax_stand_worried as bluemax:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_bluemax_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide bluemax
                # Pass (ActorReset)
                $ scene_picked_once_bluemax = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'cousin'} Macro ''>
    label s_day2p5_cousin:
        # <Macro {'name': 'cousin'} Macro ''>
        # <Events {} events ''>
        menu:
            "Yeah, Please just let this day be over.":
                $ scene_doneExplore = True
            "No, Wait I wanted to talk to someone…":
                $ scene_doneExplore = False
        if scene_doneExplore:
            # <IfTrue {'name': 'bail', 'value': '${scene:doneExplore}'} IfTrue ''>
            label s_day2p5_cousin_bail:
                # <IfTrue {'name': 'bail', 'value': '${scene:doneExplore}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_cousin_bail_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.5 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_king_screaming as king zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        xzoom -1.0 
                    show i_digdug_left as digdug zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 xpos 0.5 
                extend "{w=0.5}{nw}"
                t_ch_cousin "(Everyone else wants to escape or ignore their problems here...)" # @t_scousin34.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_sad as cousin
                extend " (...I don’t want to do that. I want to learn something from what I did.)" # @t_scousin34.01 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin:
                    linear 0 xzoom -1.0 
                t_ch_cousin "(There they go…)" # @t_scousin35.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin:
                    linear 0 xzoom 1.0 
                extend " (...Sneaking out to work on their projects, or sneaking out after other students.)" # @t_scousin35.01 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                show i_sw_black as curtain2 zorder 9:
                    default
                    alpha 0.0
                    # ShowWithAtl
                    pause 1.0 
                    linear 1.5 alpha 1.0
                show i_cousin_default_sad as cousin
                extend "{w=2.5}{nw}"
                t_ch_cousin "(I’m going to sit here, follow the rules, and learn something from all this.)" # @t_scousin36.00 self.block='Last'
                show i_sw_black as curtain:
                    alpha 0.0
                    linear 1.0 alpha 1.0
                $ renpy.pause(1.0)
                show i_bg_classroom_a as bg # behind curtain
                # <SettingChange {'bgImage': '@i_bg_classroom_a', 'curtainFadeTime': '1', 'name': '_6'} SettingChange ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 xpos 0.25 
                show i_sw_black as curtain2:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_sw_black as curtain:
                    alpha 1.0
                    linear 1.0 alpha 0.0
                $ renpy.pause(1.0)
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "(Well, time’s up and I’m the ONLY one here.)" # @t_scousin37.00 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "(As soon as King or Dig Dug show up I’ll head home.)" # @t_scousin38.00 self.block='Last'
                # <ParallelEvent {'name': '_9'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_grin as cousin
                extend " (Those other students are going to get into so much trouble.)" # @t_scousin38.01 self.block='Last'
                # <ParallelEvent {'name': '_A'} ParallelEvent ''>
                # <Events {} events ''>
                play sound "sfx/kingroar1.ogg"
                show i_king_screaming as king:
                    # ShowWithAtl
                    linear 0.5 alpha 1.0
                show i_cousin_default_surprised as cousin
                extend "{w=0.5}{nw}"
                t_ch_king "(ROAR!)" # @t_scousin39.00 self.block='Last'
                # <ParallelEvent {'name': '_B'} ParallelEvent ''>
                # <Events {} events ''>
                show i_digdug_left as digdug:
                    # ShowWithAtl
                    linear 0.5 alpha 1.0
                show i_cousin_default_sad as cousin
                extend "{w=0.5}{nw}"
                t_ch_digdug "[slot_playerName]…" # @t_scousin310.00 self.block='Last'
                # <ParallelEvent {'name': '_C'} ParallelEvent ''>
                # <Events {} events ''>
                extend " I can’t believe it..." # @t_scousin310.01 self.block='Last'
                # <ParallelEvent {'name': '_D'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_laugh as cousin
                t_ch_cousin "Yes, sir. I’m the only one here." # @t_scousin311.00 self.block='Last'
                # <ParallelEvent {'name': '_E'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_digdug "Can’t believe…" # @t_scousin312.00 self.block='Last'
                # <ParallelEvent {'name': '_F'} ParallelEvent ''>
                # <Events {} events ''>
                show i_king_confident as king
                extend " That you’d try to cover for all these delinquents!" # @t_scousin312.01 self.block='Last'
                # <ParallelEvent {'name': '_G'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "I… WHAT?!" # @t_scousin313.00 self.block='Last'
                # <ParallelEvent {'name': '_H'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_digdug "Attempting to cover for all their escapes!" # @t_scousin313.01 self.block='Last'
                # <ParallelEvent {'name': '_I'} ParallelEvent ''>
                # <Events {} events ''>
                extend " All the problems they’ve caused, the fights, damages…" # @t_scousin314.00 self.block='Last'
                # <ParallelEvent {'name': '_J'} ParallelEvent ''>
                # <Events {} events ''>
                extend " ...and the truancy!" # @t_scousin315.00 self.block='Last'
                # <ParallelEvent {'name': '_K'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_exhausted_surprised as cousin
                t_ch_cousin "B-But! I.." # @t_scousin316.00 self.block='Last'
                # <ParallelEvent {'name': '_L'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_digdug "No “Buts,” [slot_playerName]!" # @t_scousin316.01 self.block='Last'
                # <ParallelEvent {'name': '_M'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_digdug "You’re trying to make friends by covering for their delinquency, but all you’re going to get is -" # @t_scousin317.00 self.block='Last'
                # <ParallelEvent {'name': '_N'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_digdug "DETENTION LEVEL 22: PARADOXICAL EUPHONY DETENTION" # @t_scousin318.00 self.block='Last'
                # <ParallelEvent {'name': '_O'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_digdug "You brought this on yourself, [slot_playerName]." # @t_scousin318.01 self.block='Last'
                # <ParallelEvent {'name': '_P'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_exhausted_mortified_blush as cousin:
                    # ShowWithAtl
                    linear 1 xpos 0.5 
                with Dissolve(0.5)
                show i_king_confident as king:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_digdug_left as digdug:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                extend "{w=1.0}{nw}"
                t_ch_cousin "(I can't believe this is happening... all I did was try to follow the rules..." # @t_scousin319.00 self.block='Last'
                # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "but maybe... the rules are wrong..." # @t_scousin320.00 self.block='Last'
                # <ParallelEvent {'name': '_R'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_energetic_angry as cousin
                t_ch_cousin "Maybe I need to look inside myself for the answers.)" # @t_scousin320.01 self.block='Last'
                $ slot_pick_count_cousin += 1
                $ slot_picked_cousin_day3 = True
                # <NHSceneChange {'name': '_U', 'scene': 's_day4'} NHSceneChange ''>
                label s_day2p5_cousin_bail__U:
                    # <NHSceneChange {'name': '_U', 'scene': 's_day4'} NHSceneChange ''>
                    jump s_day4
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_cousin_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_cousin_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_king_confident as king:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_digdug_left as digdug:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_energetic_angry as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_cousin_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide king
                hide digdug
                # Pass (ActorReset)
                $ scene_picked_once_cousin = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'davesprite'} Macro ''>
    label s_day2p5_davesprite:
        # <Macro {'name': 'davesprite'} Macro ''>
        # <Events {} events ''>
        # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
        label s_day2p5_davesprite_warm:
            # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin zorder 2:
                # ActorEvent
                xpos 0.3 
                alpha 0.0
                linear 0.5 alpha 1.0
            show i_davesprite_standing_disinterest as davesprite zorder 2:
                default
                xpos 0.7 
                alpha 0.0
                linear 0.5 alpha 1.0
            $ renpy.pause(0.5) # TimedPause
        # <ParallelEvent {'name': '_1'} ParallelEvent ''>
        # <Events {} events ''>
        show i_davesprite_standing_disinterest as davesprite
        show i_cousin_default_neutral as cousin
        t_ch_davesprite "yo [slot_playerName] whats up" # @t_sdavesprite30.00 self.block='Last'
        # <ParallelEvent {'name': '_2'} ParallelEvent ''>
        # <Events {} events ''>
        t_ch_cousin "Hey, Davesprite. Not too much." # @t_sdavesprite31.00 self.block='Last'
        # <ParallelEvent {'name': '_3'} ParallelEvent ''>
        # <Events {} events ''>
        t_ch_davesprite "yeah same" # @t_sdavesprite32.00 self.block='Last'
        # <ParallelEvent {'name': '_4'} ParallelEvent ''>
        # <Events {} events ''>
        t_ch_davesprite "you wanna hang out today" # @t_sdavesprite33.00 self.block='Last'
        menu:
            "Hang out with Davesprite?"

            "Yes.":
                $ slot_picked_davesprite_day3 = True
            "Maybe there's someone easier to understand around here.":
                $ slot_picked_davesprite_day3 = False
        # <BranchMacro {'comparison': '!!${slot:picked_davesprite_day3}', 'name': '_6', 'path': 'davesprite/Chosen'} BranchMacro ''>
        if not not slot_picked_davesprite_day3:
            jump s_day2p5_davesprite_Chosen
        jump s_day2p5_davesprite_Passed
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_davesprite_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            $ slot_pick_count_davesprite += 1
            # <NHSceneChange {'name': '_1', 'scene': 's_davesprite3'} NHSceneChange ''>
            label s_day2p5_davesprite_Chosen__1:
                # <NHSceneChange {'name': '_1', 'scene': 's_davesprite3'} NHSceneChange ''>
                jump s_davesprite3
        # <ParallelEvent {'name': 'Passed'} ParallelEvent ''>
        label s_day2p5_davesprite_Passed:
            # <ParallelEvent {'name': 'Passed'} ParallelEvent ''>
            # <Events {} events ''>
            show i_davesprite_shrug_disinterest as davesprite
            t_ch_davesprite "whatever you wanna do" # @t_sdavesprite34.00 self.block='Last'
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_davesprite_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_davesprite_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_davesprite_shrug_disinterest as davesprite:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_davesprite_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide davesprite
                # Pass (ActorReset)
                $ scene_picked_once_davesprite = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'donko'} Macro ''>
    label s_day2p5_donko:
        # <Macro {'name': 'donko'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_donko:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_donko}'} IfFalse ''>
            label s_day2p5_donko_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_donko}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_donko_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_donko_default_meloncholic as donko zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_meloncholic as donko
                t_ch_donko "Hi there honey…" # @t_sdonko30.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "Huh? Donko…" # @t_sdonko31.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                extend " You seem sad today." # @t_sdonko31.01 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "It’s weird…" # @t_sdonko32.00 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                extend " I don’t think I’ve  seen you look quite so sad before." # @t_sdonko32.01 self.block='Last'
                # <ParallelEvent {'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                show i_donko_ygg_crying as donko
                t_ch_donko "Oh, it’s nothing…" # @t_sdonko33.00 self.block='Last'
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_donko "Just that my life is like, totally OVER." # @t_sdonko34.00 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_exhausted_sad as cousin
                t_ch_cousin "(I can’t really tell how serious this is…)" # @t_sdonko35.00 self.block='Last'
                # <ParallelEvent {'name': '_9'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_donko "I could really use, like, a good friend to talk to…" # @t_sdonko36.00 self.block='Last'
                # <ParallelEvent {'name': '_A'} ParallelEvent ''>
                # <Events {} events ''>
                extend " [slot_playerName]… will you hang out with me today?" # @t_sdonko36.01 self.block='Last'
                # <ParallelEvent {'name': '_B'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_crying as donko
                t_ch_donko "Like...please?" # @t_sdonko37.00 self.block='Last'
                # <ParallelEvent {'name': '_C'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_crying as donko
                t_ch_cousin "Hmmm…" # @t_sdonko38.00 self.block='Last'
        if scene_picked_once_donko:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_donko}'} IfTrue ''>
            label s_day2p5_donko_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_donko}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_donko_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_donko_default_meloncholic as donko zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_crying as donko
                t_ch_donko "Hi again…" # @t_sdonko39.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_crying as donko
                t_ch_donko "So, will you hang out with me today?" # @t_sdonko310.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_crying as donko
                extend " I like, really need a friend right now…" # @t_sdonko310.01 self.block='Last'
        menu:
            "Sure!":
                $ slot_picked_donko_day3 = True
            "Let's see who else is around to hang out with.":
                $ slot_picked_donko_day3 = False
        # <BranchMacro {'comparison': '!!${slot:picked_donko_day3}', 'name': '_3', 'path': 'donko/Chosen'} BranchMacro ''>
        if not not slot_picked_donko_day3:
            jump s_day2p5_donko_Chosen
        jump s_day2p5_donko_cleanup
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_donko_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            $ slot_pick_count_donko += 1
            # <NHSceneChange {'name': '_1', 'scene': 's_donko3'} NHSceneChange ''>
            label s_day2p5_donko_Chosen__1:
                # <NHSceneChange {'name': '_1', 'scene': 's_donko3'} NHSceneChange ''>
                jump s_donko3
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_donko_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_donko_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_donko_default_crying as donko:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_donko_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide donko
                # Pass (ActorReset)
                $ scene_picked_once_donko = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'galaga'} Macro ''>
    label s_day2p5_galaga:
        # <Macro {'name': 'galaga'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_galaga:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_galaga}'} IfFalse ''>
            label s_day2p5_galaga_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_galaga}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_galaga_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_galaga_default as galaga zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_galaga_default as galaga
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Hey Galaga! How’s it going?" # @t_sgalaga215.00a self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_galaga "{smallcaps}[slot_playerName]! Do you think you can help me rehearse?{/smallcaps}" # @t_sgalaga215.00b self.block='Last'
                menu:
                    "Help out?"

                    "Continue to coyly suggest Galaga Ship should rehearse with you!":
                        $ slot_picked_galaga_day3 = True
                    "Forget about Drama Club, Galaga ship is unapproachable!":
                        $ slot_picked_galaga_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_galaga_day3}', 'name': '_4', 'path': 'galaga/Chosen'} BranchMacro ''>
                if not not slot_picked_galaga_day3:
                    jump s_day2p5_galaga_Chosen
                jump s_day2p5_galaga_PassedFirstTime
        if scene_picked_once_galaga:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_galaga}'} IfTrue ''>
            label s_day2p5_galaga_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_galaga}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_galaga_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_galaga_default as galaga zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_galaga_default as galaga
                show i_cousin_default_neutral as cousin
                t_ch_galaga "{smallcaps}Don’t know how I’m gonna get these lines down in time.{/smallcaps}" # @t_sgalaga220.00a self.block='Last'
                menu:
                    "Help out?"

                    "HELP GALAGA SHIP":
                        $ slot_picked_galaga_day3 = True
                    "DO NOT HELP GALAGA SHIP":
                        $ slot_picked_galaga_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_galaga_day3}', 'name': '_3', 'path': 'galaga/Chosen'} BranchMacro ''>
                if not not slot_picked_galaga_day3:
                    jump s_day2p5_galaga_Chosen
                jump s_day2p5_galaga_PassedLoop
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_galaga_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_surprised_blush as cousin
            t_ch_cousin "(OH! Is Galaga Ship completely dazzled by my charm? I’ll have to dial it back a bit.)" # @t_sgalaga215.00c self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            extend " Okay, yeah. Rehearsing is cool." # @t_sgalaga215.01d self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_galaga "{smallcaps}Great, let’s go somewhere quiet..{/smallcaps}" # @t_sgalaga215.00e self.block='Last'
            $ slot_pick_count_galaga += 1
            # <NHSceneChange {'name': '_4', 'scene': 's_galaga3'} NHSceneChange ''>
            label s_day2p5_galaga_Chosen__4:
                # <NHSceneChange {'name': '_4', 'scene': 's_galaga3'} NHSceneChange ''>
                jump s_galaga3
        # <Macro {'name': 'PassedFirstTime'} Macro ''>
        label s_day2p5_galaga_PassedFirstTime:
            # <Macro {'name': 'PassedFirstTime'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Yeah, rehearsing." # @t_sgalaga215.00f self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "I was thinking, maybe, uh, not doing that." # @t_sgalaga215.00g self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_galaga "{smallcaps}Yeah?{/smallcaps}" # @t_sgalaga216.00 self.block='Last'
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_galaga "{smallcaps}Not sure it’d make a difference either way.{/smallcaps}" # @t_sgalaga217.00 self.block='Last'
            # <ParallelEvent {'name': '_4'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_galaga "{smallcaps}You seem pretty hopeless!{/smallcaps}" # @t_sgalaga218.00 self.block='Last'
            # <ParallelEvent {'name': '_5'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_exhausted_surprised_blush as cousin
            t_ch_cousin "(!!!)" # @t_sgalaga219.00 self.block='Last'
            # <ParallelEvent {'name': '_6'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_exhausted_mortified_blush as cousin
            t_ch_cousin "(Man, whatever. This school just isn't ready for my different take!)" # @t_sgalaga220.00 self.block='Last'
            jump s_day2p5_galaga_cleanup
        # <Macro {'name': 'PassedLoop'} Macro ''>
        label s_day2p5_galaga_PassedLoop:
            # <Macro {'name': 'PassedLoop'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_galaga "{smallcaps}That’s a shame.{/smallcaps}" # @t_sgalaga220.00c self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_galaga "{smallcaps}Well, bye!!!{/smallcaps}" # @t_sgalaga220.00d self.block='Last'
            jump s_day2p5_galaga_cleanup
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_galaga_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_galaga_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_galaga_default as galaga:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_exhausted_mortified_blush as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_galaga_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide galaga
                # Pass (ActorReset)
                $ scene_picked_once_galaga = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'hiromi'} Macro ''>
    label s_day2p5_hiromi:
        # <Macro {'name': 'hiromi'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_hiromi:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_hiromi}'} IfFalse ''>
            label s_day2p5_hiromi_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_hiromi}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_hiromi_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_hiromi_stand_serious as hiromi zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_hiromi_stand_serious as hiromi
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Hey Hiromi! Can I hang out with you today?" # @t_shiromi30.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_hiromi_stand_smile as hiromi
                t_ch_hiromi "I have to collect more data... But you can come along, if you like." # @t_shiromi31.00 self.block='Last'
                menu:
                    "I have to collect more data... But you can come along, if you like."

                    "Count me in!":
                        $ slot_picked_hiromi_day3 = True
                    "Sounds kind of boring...":
                        $ slot_picked_hiromi_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_hiromi_day3}', 'name': '_4', 'path': 'hiromi/Chosen'} BranchMacro ''>
                if not not slot_picked_hiromi_day3:
                    jump s_day2p5_hiromi_Chosen
                jump s_day2p5_hiromi_Passed
        if scene_picked_once_hiromi:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_hiromi}'} IfTrue ''>
            label s_day2p5_hiromi_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_hiromi}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_hiromi_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_hiromi_stand_serious as hiromi zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_hiromi_stand_serious as hiromi
                t_ch_cousin "Still need help collecting that data?" # @t_shiromi36.00a self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_hiromi "……………………………………………." # @t_shiromi36.00b self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "(I’m going to pretend that was an invitation, I guess… )" # @t_shiromi36.00c self.block='Last'
                menu:
                    "I have to collect more data... But you can come along, if you like."

                    "Count me in!":
                        $ slot_picked_hiromi_day3 = True
                    "Sounds kind of boring...":
                        $ slot_picked_hiromi_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_hiromi_day3}', 'name': '_5', 'path': 'hiromi/Chosen'} BranchMacro ''>
                if not not slot_picked_hiromi_day3:
                    jump s_day2p5_hiromi_Chosen
                jump s_day2p5_hiromi_Passed
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_hiromi_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'allowInterrupt': 'false', 'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Count me in!" # @t_shiromi32.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_hiromi_stand_smile as hiromi:
                # ShowWithAtl
                pause 0.5 
                linear .5 alpha 0.0
            $ renpy.pause(1.0) # TimedPause
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Ah, I'd better follow her... )" # @t_shiromi33.00 self.block='Last'
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "(But she definitely smiled this time!)" # @t_shiromi34.00 self.block='Last'
            $ slot_pick_count_hiromi += 1
            # <NHSceneChange {'name': '_5', 'scene': 's_hiromi3'} NHSceneChange ''>
            label s_day2p5_hiromi_Chosen__5:
                # <NHSceneChange {'name': '_5', 'scene': 's_hiromi3'} NHSceneChange ''>
                jump s_hiromi3
        # <Macro {'name': 'Passed'} Macro ''>
        label s_day2p5_hiromi_Passed:
            # <Macro {'name': 'Passed'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            show i_hiromi_stand_serious as hiromi:
                # ShowWithAtl
                linear 0.5 alpha 1.0
            extend "{w=0.5}{nw}"
            t_ch_cousin "Sounds kind of boring..." # @t_shiromi35.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_hiromi "Suit yourself." # @t_shiromi36.00 self.block='Last'
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_hiromi_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_hiromi_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_hiromi_stand_serious as hiromi:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_hiromi_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide hiromi
                # Pass (ActorReset)
                $ scene_picked_once_hiromi = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'jane'} Macro ''>
    label s_day2p5_jane:
        # <Macro {'name': 'jane'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_jane:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_jane}'} IfFalse ''>
            label s_day2p5_jane_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_jane}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_jane_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_jane_default_grin as jane zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_grin as cousin
                show i_jane_default_grin as jane
                t_ch_cousin "Hi Jane! Have you figured out what we’re doing today?" # @t_sjane30.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_jane_armscrossed_smile as jane
                t_ch_jane "Hoo hoo! As a matter of fact, I have! :B" # @t_sjane31.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_jane "However, I need you to give your consent first…" # @t_sjane32.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                extend " It’s going to involve something kind of…  devious!" # @t_sjane32.01 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "H-huh?!" # @t_sjane33.00 self.block='Last'
                # <ParallelEvent {'allowInterrupt': 'false', 'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    pause 0.5 
                    ease_expo .75 xpos 0.5 
                extend "{w=1.25}{nw}"
                t_ch_jane "Here, lean in close so I can whisper…" # @t_sjane34.00 self.block='Last'
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                show i_jane_handonhip_grin as jane
                extend " [slot_playerName], we’re going to sneak out of detention!" # @t_sjane34.01 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_jane "What do you say? I know it’s not the sort of thing you usually get up to…" # @t_sjane35.00 self.block='Last'
                # <ParallelEvent {'name': '_9'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin:
                    # ShowWithAtl
                    ease_expo .5 xpos 0.25 
                extend "{w=0.5}{nw}"
                t_ch_cousin "J-Jane! I’m a little shocked…" # @t_sjane36.00 self.block='Last'
                # <ParallelEvent {'name': '_A'} ParallelEvent ''>
                # <Events {} events ''>
                extend " You seem like such a practical girl!" # @t_sjane36.01 self.block='Last'
                # <ParallelEvent {'name': '_B'} ParallelEvent ''>
                # <Events {} events ''>
                extend " Is this really something you’d want to try?" # @t_sjane36.02 self.block='Last'
                # <ParallelEvent {'name': '_C'} ParallelEvent ''>
                # <Events {} events ''>
                show i_jane_armscrossed_laugh as jane
                t_ch_jane "Am I really that practical, though?" # @t_sjane37.00 self.block='Last'
                # <ParallelEvent {'name': '_D'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_jane "I mean, you already know me as a dedicated trickster and gutsy gumshoe…" # @t_sjane38.00 self.block='Last'
                # <ParallelEvent {'name': '_E'} ParallelEvent ''>
                # <Events {} events ''>
                show i_jane_armscrossed_grin as jane
                t_ch_jane "And besides, my journalistic integrity matters more to me than any school rules." # @t_sjane39.00 self.block='Last'
                # <ParallelEvent {'name': '_F'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_jane_armscrossed_grin as jane
                t_ch_cousin "Hmm…" # @t_sjane310.00 self.block='Last'
        if scene_picked_once_jane:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_jane}'} IfTrue ''>
            label s_day2p5_jane_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_jane}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_jane_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_jane_armscrossed_grin as jane zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_jane_armscrossed_grin as jane
                t_ch_jane "C’mon, [slot_playerName]!" # @t_sjane311.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_jane "It wouldn’t be any fun if you didn’t join me. :B" # @t_sjane312.00 self.block='Last'
        menu:
            "Skip detention with Jane?"

            "Yes!":
                $ slot_picked_jane_day3 = True
            "I'm not too sure about this.":
                $ slot_picked_jane_day3 = False
        # <BranchMacro {'comparison': '!!${slot:picked_jane_day3}', 'name': '_3', 'path': 'jane/Chosen'} BranchMacro ''>
        if not not slot_picked_jane_day3:
            jump s_day2p5_jane_Chosen
        jump s_day2p5_jane_cleanup
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_jane_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_jane_armscrossed_grin as jane
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Alright, let’s go!" # @t_sjane313.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_jane_armscrossed_grin as jane
            show i_cousin_default_neutral as cousin
            t_ch_cousin "I wouldn’t want to dilute your journalistic integrity." # @t_sjane314.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_jane_armscrossed_grin as jane
            show i_cousin_default_surprised as cousin
            t_ch_jane "Hoo! That’s the spirit!" # @t_sjane315.00 self.block='Last'
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_jane "Shall we?" # @t_sjane316.00 self.block='Last'
            $ slot_pick_count_jane += 1
            # <NHSceneChange {'name': '_5', 'scene': 's_jane3'} NHSceneChange ''>
            label s_day2p5_jane_Chosen__5:
                # <NHSceneChange {'name': '_5', 'scene': 's_jane3'} NHSceneChange ''>
                jump s_jane3
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_jane_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_jane_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_jane_armscrossed_grin as jane:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_surprised as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_jane_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide jane
                # Pass (ActorReset)
                $ scene_picked_once_jane = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'lolo'} Macro ''>
    label s_day2p5_lolo:
        # <Macro {'name': 'lolo'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_lolo:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_lolo}'} IfFalse ''>
            label s_day2p5_lolo_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_lolo}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_lolo_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_lolo_crossed_raisedbrow as lolo zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_lolo_crossed_raisedbrow as lolo
                show i_cousin_default_neutral as cousin
                t_ch_lolo "Hey." # @t_slolo30.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_lolo_crossed_raisedbrow as lolo
                t_ch_cousin "Hey…." # @t_slolo31.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_lolo "Listen, in a minute I’m going to get up and leave the room." # @t_slolo32.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                show i_lolo_crossed_grin as lolo
                extend " Nobody pays attention, they won’t notice." # @t_slolo32.01 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_lolo "Wait a few minutes, and then get up and leave too." # @t_slolo33.00 self.block='Last'
                # <ParallelEvent {'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                extend " I’ll meet you in the hallway." # @t_slolo33.01 self.block='Last'
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "So you do want to hang out with me?" # @t_slolo34.00 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                extend " What happened to “I’ll just disappoint you”?" # @t_slolo34.01 self.block='Last'
                # <ParallelEvent {'name': '_9'} ParallelEvent ''>
                # <Events {} events ''>
                show i_lolo_crossed_frustrated as lolo
                t_ch_lolo "Fine. Don’t come then." # @t_slolo35.00 self.block='Last'
                # <ParallelEvent {'name': '_A'} ParallelEvent ''>
                # <Events {} events ''>
                extend " Whatever you want." # @t_slolo35.01 self.block='Last'
                # <ParallelEvent {'name': '_B'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_exhausted_surprised as cousin
                show i_lolo_crossed_frustrated as lolo:
                    # ShowWithAtl
                    linear .333 alpha 0.0
                extend "{w=0.333}{nw}"
                t_ch_cousin "I didn’t say-" # @t_slolo36.00 self.block='Last'
                # <ParallelEvent {'name': '_C'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "(Oops. She’s gone.)" # @t_slolo37.00 self.block='Last'
        if scene_picked_once_lolo:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_lolo}'} IfTrue ''>
            label s_day2p5_lolo_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_lolo}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_lolo_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(Lolo still isn’t back yet…" # @t_slolo38.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                extend " Is she waiting for me to go after her still?)" # @t_slolo38.01 self.block='Last'
        menu:
            "(Oops. She's gone.)"

            "Follow Lolo outside":
                $ slot_picked_lolo_day3 = True
            "Maybe I shouldn't...":
                $ slot_picked_lolo_day3 = False
        # <BranchMacro {'comparison': '!!${slot:picked_lolo_day3}', 'name': '_3', 'path': 'lolo/Chosen'} BranchMacro ''>
        if not not slot_picked_lolo_day3:
            jump s_day2p5_lolo_Chosen
        jump s_day2p5_lolo_cleanup
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_lolo_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            $ slot_pick_count_lolo += 1
            # <NHSceneChange {'name': '_1', 'scene': 's_lolo3'} NHSceneChange ''>
            label s_day2p5_lolo_Chosen__1:
                # <NHSceneChange {'name': '_1', 'scene': 's_lolo3'} NHSceneChange ''>
                jump s_lolo3
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_lolo_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_lolo_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_lolo_crossed_frustrated as lolo:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_surprised as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_lolo_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide lolo
                # Pass (ActorReset)
                $ scene_picked_once_lolo = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'meowkie'} Macro ''>
    label s_day2p5_meowkie:
        # <Macro {'name': 'meowkie'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_meowkie:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_meowkie}'} IfFalse ''>
            label s_day2p5_meowkie_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_meowkie}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_meowkie_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_meowkie_normal_forcedsmile_badge as meowkie zorder 2:
                        default
                        xpos 0.7 
                        xzoom -1.0 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie
                show i_cousin_default_neutral as cousin
                t_ch_meowkie "Hiya Boss! Got any plans for today?" # @t_smeowkie30.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "Uh… just sitting in detention, I guess." # @t_smeowkie31.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_meowkie "Nyaa… of course." # @t_smeowkie32.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                show i_meowkie_normal_frown_badge as meowkie
                extend " That was pretty dumb of me to ask, wasn’t it?" # @t_smeowkie32.01 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Haha, what? Come on, Meowkie, don’t worry about that." # @t_smeowkie33.00 self.block='Last'
                # <ParallelEvent {'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie
                t_ch_meowkie "Heh, okay…" # @t_smeowkie34.00 self.block='Last'
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                show i_meowkie_akimbo_normal_badge as meowkie
                t_ch_meowkie "Well, I was gonna patrol the halls today…" # @t_smeowkie35.00 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                extend " Seeing as I’m the lead Hall Monitor and all." # @t_smeowkie35.01 self.block='Last'
                # <ParallelEvent {'name': '_9'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_meowkie "I thought maybe… you might wanna tag along with me?" # @t_smeowkie36.00 self.block='Last'
                # <ParallelEvent {'name': '_A'} ParallelEvent ''>
                # <Events {} events ''>
                show i_meowkie_akimbo_forcedsmile_badge as meowkie
                extend " Only if you want to, of course!" # @t_smeowkie36.01 self.block='Last'
                # <ParallelEvent {'name': '_B'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_meowkie "Ya know, see how a real pro like me does it!" # @t_smeowkie37.00 self.block='Last'
                # <ParallelEvent {'name': '_C'} ParallelEvent ''>
                # <Events {} events ''>
                show i_meowkie_slouch_forcedsmile_badge as meowkie
                t_ch_meowkie "Haha… I’m just kidding… sorry." # @t_smeowkie38.00 self.block='Last'
                # <ParallelEvent {'name': '_D'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "(It’s pretty cute how excited she gets about hall monitoring.)" # @t_smeowkie39.00 self.block='Last'
        if scene_picked_once_meowkie:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_meowkie}'} IfTrue ''>
            label s_day2p5_meowkie_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_meowkie}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_meowkie_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_meowkie_normal_normal_badge as meowkie zorder 2:
                        default
                        xpos 0.7 
                        xzoom -1.0 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_meowkie_normal_normal_badge as meowkie
                show i_cousin_default_neutral as cousin
                t_ch_meowkie "So, Boss? Whaddya say?" # @t_smeowkie311.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie
                extend " B-but please don’t feel obligated, of course…" # @t_smeowkie311.01 self.block='Last'
        menu:
            "Tag along with Meowkie to monitor the halls today?"

            "Yeah, sounds fun!":
                $ slot_picked_meowkie_day3 = True
            "Let’s see what else is going on before I decide.":
                $ slot_picked_meowkie_day3 = False
        # <BranchMacro {'comparison': '!!${slot:picked_meowkie_day3}', 'name': '_3', 'path': 'meowkie/Chosen'} BranchMacro ''>
        if not not slot_picked_meowkie_day3:
            jump s_day2p5_meowkie_Chosen
        jump s_day2p5_meowkie_Passed
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_meowkie_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            $ slot_pick_count_meowkie += 1
            # <NHSceneChange {'name': '_1', 'scene': 's_meowkie3'} NHSceneChange ''>
            label s_day2p5_meowkie_Chosen__1:
                # <NHSceneChange {'name': '_1', 'scene': 's_meowkie3'} NHSceneChange ''>
                jump s_meowkie3
        # <Macro {'name': 'Passed'} Macro ''>
        label s_day2p5_meowkie_Passed:
            # <Macro {'name': 'Passed'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_meowkie_akimbo_forcedsmile_badge as meowkie
            show i_cousin_default_neutral as cousin
            t_ch_meowkie "Oh, d-don’t worry about it!" # @t_smeowkie310.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_meowkie_normal_forcedsmile_badge as meowkie
            extend " It was probably a dumb idea anyway…" # @t_smeowkie310.01 self.block='Last'
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_meowkie_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_meowkie_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_meowkie_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide meowkie
                # Pass (ActorReset)
                $ scene_picked_once_meowkie = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'mrdriller'} Macro ''>
    label s_day2p5_mrdriller:
        # <Macro {'name': 'mrdriller'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_mrdriller:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_mrdriller}'} IfFalse ''>
            label s_day2p5_mrdriller_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_mrdriller}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_mrdriller_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_mrdriller_standing_happy as mrdriller zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_mrdriller_standing_happy as mrdriller
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Mr. Driller… You can’t sit still today, can you?" # @t_smrdriller2x50.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_mrdriller_drillup_happy as mrdriller
                t_ch_mrdriller "It’s just that… I’m really jonesing to go digging!" # @t_smrdriller2x51.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "It hasn’t been THAT long, has it?" # @t_smrdriller2x52.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_mrdriller "Hey [slot_playerName]… If we went digging today..." # @t_smrdriller2x53.00 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                extend " What do you think we’d find?!" # @t_smrdriller2x53.01 self.block='Last'
                # <ParallelEvent {'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "Probably…" # @t_smrdriller2x54.00 self.block='Last'
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                extend " Some more dirt and stuff?" # @t_smrdriller2x54.01 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                show i_mrdriller_drillup_excited as mrdriller
                t_ch_mrdriller "Oh man! Do you really think so?!" # @t_smrdriller2x55.00 self.block='Last'
                # <ParallelEvent {'name': '_9'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "...Yes." # @t_smrdriller2x56.00 self.block='Last'
                # <ParallelEvent {'name': '_A'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_mrdriller "Okay, that’s it." # @t_smrdriller2x57.00 self.block='Last'
                # <ParallelEvent {'name': '_B'} ParallelEvent ''>
                # <Events {} events ''>
                show i_mrdriller_drillup_happy as mrdriller
                t_ch_mrdriller "I definitely can’t wait!" # @t_smrdriller2x58.00 self.block='Last'
                # <ParallelEvent {'name': '_C'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_mrdriller "I’m gonna go out drilling RIGHT NOW!" # @t_smrdriller2x59.00 self.block='Last'
                show i_mrdriller_drillup_happy as mrdriller:
                    # ShowWithAtl
                    linear .33 alpha 0.0
                # <ParallelEvent {'name': '_E'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Ahhh!" # @t_smrdriller2x510.00 self.block='Last'
                # <ParallelEvent {'name': '_F'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "He’s gonna get in trouble for skipping out of detention…" # @t_smrdriller2x511.00 self.block='Last'
        if scene_picked_once_mrdriller:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_mrdriller}'} IfTrue ''>
            label s_day2p5_mrdriller_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_mrdriller}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_mrdriller_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(Mr Driller already ran out of class..." # @t_smrdriller2x512.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                extend " he could get into more trouble if someone doesn't follow him.)" # @t_smrdriller2x512.01 self.block='Last'
        menu:
            "I’ve gotta go get him to come to his senses.":
                $ slot_picked_mrdriller_day3 = True
            "If I leave I might get in trouble too...":
                $ slot_picked_mrdriller_day3 = False
        # <BranchMacro {'comparison': '!!${slot:picked_mrdriller_day3}', 'name': '_3', 'path': 'mrdriller/Chosen'} BranchMacro ''>
        if not not slot_picked_mrdriller_day3:
            jump s_day2p5_mrdriller_Chosen
        jump s_day2p5_mrdriller_cleanup
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_mrdriller_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            $ slot_pick_count_mrdriller += 1
            # <NHSceneChange {'name': '_1', 'scene': 's_mrdriller3'} NHSceneChange ''>
            label s_day2p5_mrdriller_Chosen__1:
                # <NHSceneChange {'name': '_1', 'scene': 's_mrdriller3'} NHSceneChange ''>
                jump s_mrdriller3
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_mrdriller_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_mrdriller_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_mrdriller_drillup_happy as mrdriller:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_mrdriller_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide mrdriller
                # Pass (ActorReset)
                $ scene_picked_once_mrdriller = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'nidia'} Macro ''>
    label s_day2p5_nidia:
        # <Macro {'name': 'nidia'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_nidia:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_nidia}'} IfFalse ''>
            label s_day2p5_nidia_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_nidia}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_nidia_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_nidia_clasped_happy as nidia zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_nidia_clasped_happy as nidia
                show i_cousin_default_neutral as cousin
                t_ch_nidia "Hi [slot_playerName]!" # @t_snidia30.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "Hey Nidia!" # @t_snidia31.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                extend " What're you so excited about?" # @t_snidia31.01 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_nidia "Well... I was just wondering if you were coming to Magic Club today!" # @t_snidia32.00 self.block='Last'
        if scene_picked_once_nidia:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_nidia}'} IfTrue ''>
            label s_day2p5_nidia_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_nidia}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_nidia_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_nidia_akimbo_surprised as nidia zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_nidia_akimbo_surprised as nidia
                show i_cousin_default_neutral as cousin
                t_ch_nidia "Coming to Magic Club today?" # @t_snidia314.00a self.block='Last'
        menu:
            "Well... I was just wondering if you were coming to Magic Club today!"

            "Sounds...Magical!":
                $ slot_picked_nidia_day3 = True
            "Maybe not today...":
                $ slot_picked_nidia_day3 = False
        # <BranchMacro {'comparison': '!!${slot:picked_nidia_day3}', 'name': '_3', 'path': 'nidia/Chosen'} BranchMacro ''>
        if not not slot_picked_nidia_day3:
            jump s_day2p5_nidia_Chosen
        jump s_day2p5_nidia_Passed
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_nidia_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_energetic_grin as cousin
            t_ch_cousin "Sounds... Magical!" # @t_snidia33.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_nidia_akimbo_worried as nidia
            t_ch_nidia "[slot_playerName]... I don't mean to be rude..." # @t_snidia34.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            extend " But your puns really trivialize the seriousness of Magic Club." # @t_snidia34.01 self.block='Last'
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "O-oh... Sorry..." # @t_snidia35.00 self.block='Last'
            # <ParallelEvent {'name': '_4'} ParallelEvent ''>
            # <Events {} events ''>
            show i_nidia_akimbo_surprised as nidia
            show i_cousin_default_neutral as cousin
            t_ch_nidia "Or maybe they show that you're comfortable with the subject?" # @t_snidia36.00 self.block='Last'
            # <ParallelEvent {'name': '_5'} ParallelEvent ''>
            # <Events {} events ''>
            show i_nidia_resolute_worried as nidia
            extend " Maybe I should try..." # @t_snidia36.01 self.block='Last'
            # <ParallelEvent {'name': '_6'} ParallelEvent ''>
            # <Events {} events ''>
            show i_nidia_resolute_happy as nidia
            show i_cousin_default_sad as cousin
            t_ch_nidia "Every morning I try to... exorcise in the park..." # @t_snidia37.00 self.block='Last'
            # <ParallelEvent {'name': '_7'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_exhausted_sad as cousin
            show i_nidia_clasped_happy as nidia
            extend " I brought a sandwitch and tabooli for lunch..." # @t_snidia37.01 self.block='Last'
            # <ParallelEvent {'name': '_8'} ParallelEvent ''>
            # <Events {} events ''>
            show i_nidia_akimbo_happy as nidia
            show i_cousin_exhausted_mortified_blush as cousin
            extend " When I'm scared I check my horrorscope..." # @t_snidia37.02 self.block='Last'
            # <ParallelEvent {'name': '_9'} ParallelEvent ''>
            # <Events {} events ''>
            show i_nidia_akimbo_worried_blush as nidia
            with Dissolve(0.5)
            t_ch_cousin "..................." # @t_snidia38.00 self.block='Last'
            # <ParallelEvent {'name': '_A'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "Maybe you're right... Maybe this subject requires a certain level of....... dignity." # @t_snidia39.00 self.block='Last'
            # <ParallelEvent {'name': '_B'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_nidia "You think so?" # @t_snidia310.00 self.block='Last'
            # <ParallelEvent {'name': '_C'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "Let's just go to the library..." # @t_snidia311.00 self.block='Last'
            $ slot_pick_count_nidia += 1
            # <NHSceneChange {'name': '_E', 'scene': 's_nidia3'} NHSceneChange ''>
            label s_day2p5_nidia_Chosen__E:
                # <NHSceneChange {'name': '_E', 'scene': 's_nidia3'} NHSceneChange ''>
                jump s_nidia3
        # <Macro {'name': 'Passed'} Macro ''>
        label s_day2p5_nidia_Passed:
            # <Macro {'name': 'Passed'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_nidia_akimbo_surprised as nidia
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Maybe not today..." # @t_snidia312.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_nidia_akimbo_happy as nidia
            t_ch_nidia "Okay! There's always tomorrow..." # @t_snidia313.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_nidia_akimbo_angry as nidia
            extend " Except when there's NOT." # @t_snidia313.01 self.block='Last'
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(What does THAT mean?!)" # @t_snidia314.00 self.block='Last'
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_nidia_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_nidia_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_nidia_akimbo_angry as nidia:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_mortified as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_nidia_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide nidia
                # Pass (ActorReset)
                $ scene_picked_once_nidia = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'richard'} Macro ''>
    label s_day2p5_richard:
        # <Macro {'name': 'richard'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_richard:
            # <IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_richard}'} IfFalse ''>
            label s_day2p5_richard_FirstTime:
                # <IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_richard}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_richard_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_miller_aliens_serious as miller zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_miller_aliens_serious as miller
                show i_cousin_default_neutral as cousin
                t_ch_richard "[slot_playerName], I have it all sorted." # @t_srichard226.00a self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_miller_akimbo_shocked as miller
                show i_cousin_default_neutral as cousin
                t_ch_richard "It’s a big fish." # @t_srichard227.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_richard "I’ll need help tracking him down." # @t_srichard228.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Literally an actual fish?" # @t_srichard229.00 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                show i_miller_pondering_contemplative as miller
                t_ch_richard "Not this time, no." # @t_srichard230.00 self.block='Last'
                # <ParallelEvent {'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_richard "The point is, you’re the only person I almost trust." # @t_srichard231.00 self.block='Last'
                menu:
                    "Join Richard on his crackdown stakeout thing?"

                    "S-sure!":
                        $ slot_picked_richard_day3 = True
                    "Forget it, too crazy.":
                        $ slot_picked_richard_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_richard_day3}', 'name': '_8', 'path': 'richard/ChosenFirstTime'} BranchMacro ''>
                if not not slot_picked_richard_day3:
                    jump s_day2p5_richard_ChosenFirstTime
                jump s_day2p5_richard_PassedFirstTime
        if scene_picked_once_richard:
            # <IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_richard}'} IfTrue ''>
            label s_day2p5_richard_Loop:
                # <IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_richard}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_richard_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_miller_pondering_laugh as miller zorder 2:
                        default
                        xpos 0.7 
                        ypos 1.2 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_miller_pondering_laugh as miller:
                    # ShowWithAtl
                    linear 0.5 ypos 1.2 
                    # ShowWithAtl
                    easeout .75 ypos 1.0 
                show i_cousin_default_neutral as cousin
                extend "{w=0.75}{nw}"
                t_ch_richard "I knew you’d change your mind. It’s in your psych profile." # @t_srichard238.00 self.block='Last'
                menu:
                    "Join Richard on his crackdown stakeout thing afterall?"

                    "Okay!":
                        $ slot_picked_richard_day3 = True
                    "Nope, still too crazy!":
                        $ slot_picked_richard_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_richard_day3}', 'name': '_3', 'path': 'richard/ChosenLoop'} BranchMacro ''>
                if not not slot_picked_richard_day3:
                    jump s_day2p5_richard_ChosenLoop
                jump s_day2p5_richard_PassedLoop
        # <Macro {'name': 'ChosenFirstTime'} Macro ''>
        label s_day2p5_richard_ChosenFirstTime:
            # <Macro {'name': 'ChosenFirstTime'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_miller_pondering_contemplative as miller
            show i_cousin_default_surprised as cousin
            $ renpy.pause(0) # Image change
            show i_cousin_default_surprised_blush as cousin
            with Dissolve(0.5)
            t_ch_cousin "Me? Really?" # @t_srichard232.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            extend " (Wow!)" # @t_srichard232.01 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_richard "Well, you’re new." # @t_srichard233.00 self.block='Last'
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_richard "And I DID say “almost.”" # @t_srichard234.00 self.block='Last'
            $ slot_pick_count_richard += 1
            # <NHSceneChange {'name': '_5', 'scene': 's_richard3'} NHSceneChange ''>
            label s_day2p5_richard_ChosenFirstTime__5:
                # <NHSceneChange {'name': '_5', 'scene': 's_richard3'} NHSceneChange ''>
                jump s_richard3
        # <Macro {'name': 'ChosenLoop'} Macro ''>
        label s_day2p5_richard_ChosenLoop:
            # <Macro {'name': 'ChosenLoop'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_miller_pondering_contemplative as miller:
                # ShowWithAtl
                easeout 0.5 ypos 0.5 
            show i_cousin_default_angry as cousin
            extend "{w=0.5}{nw}"
            t_ch_cousin "Well, I’ll help you anyway." # @t_srichard239.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_angry_blush as cousin
            with Dissolve(0.5)
            t_ch_cousin "In spite of the psych profile." # @t_srichard240.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_miller_pondering_contemplative as miller
            show i_cousin_exhausted_sad as cousin
            t_ch_richard "Yup. It said you’d say that too." # @t_srichard241.00 self.block='Last'
            $ slot_pick_count_richard += 1
            # <NHSceneChange {'name': '_4', 'scene': 's_richard3'} NHSceneChange ''>
            label s_day2p5_richard_ChosenLoop__4:
                # <NHSceneChange {'name': '_4', 'scene': 's_richard3'} NHSceneChange ''>
                jump s_richard3
        # <Macro {'name': 'PassedFirstTime'} Macro ''>
        label s_day2p5_richard_PassedFirstTime:
            # <Macro {'name': 'PassedFirstTime'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_miller_pondering_contemplative as miller
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Richard, you ever think that maybe this stuff you think is completely crazy?" # @t_srichard235.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_miller_pondering_halfgrin as miller
            t_ch_richard "I considered it. Briefly." # @t_srichard236.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "I’d revisit that line of thought!" # @t_srichard237.00 self.block='Last'
            jump s_day2p5_richard_cleanup
        # <Macro {'name': 'PassedLoop'} Macro ''>
        label s_day2p5_richard_PassedLoop:
            # <Macro {'name': 'PassedLoop'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_miller_akimbo_serious as miller:
                # ShowWithAtl
                linear 0.5 ypos 1.0 
                # ShowWithAtl
                easeout 0.5 ypos 0.5 
            show i_cousin_default_neutral as cousin
            extend "{w=0.5}{nw}"
            t_ch_cousin "What’s the rent like in Crazy Town?" # @t_srichard242.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_miller_akimbo_shocked as miller
            extend "{w=0.4}{nw}"
            t_ch_richard "Pretty gooHEY!" # @t_srichard243.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_richard "Extreme sarcasm isn’t in your psych profile..." # @t_srichard244.00 self.block='Last'
            jump s_day2p5_richard_cleanup
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_richard_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_richard_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_miller_akimbo_shocked as miller:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_richard_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide miller
                # Pass (ActorReset)
                $ scene_picked_once_richard = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'taira'} Macro ''>
    label s_day2p5_taira:
        # <Macro {'name': 'taira'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_taira:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_taira}'} IfFalse ''>
            label s_day2p5_taira_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_taira}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_taira_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_taira_akimbo_happy as taira zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_taira_akimbo_happy as taira
                show i_cousin_default_neutral as cousin
                t_ch_taira "Hey Cuz! Wanna come sit with me for detention today?" # @t_staira31.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Uh… Well…" # @t_staira32.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                show i_taira_akimbo_pleading as taira
                t_ch_taira "C’mon, please?" # @t_staira33.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                extend " How can you say no to this face?!" # @t_staira33.01 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "...That’s actually a very good question." # @t_staira34.00 self.block='Last'
                # <ParallelEvent {'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                show i_taira_akimbo_happy as taira
                t_ch_taira "C’mon, you know you wanna." # @t_staira35.00 self.block='Last'
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                extend " Not only do you get a primo view of my super hot bod if you sit with me…" # @t_staira35.01 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                show i_taira_revenge_happy as taira
                t_ch_taira "I also gotta feeling some exciting stuff is gonna go down today." # @t_staira36.00 self.block='Last'
                # <ParallelEvent {'name': '_9'} ParallelEvent ''>
                # <Events {} events ''>
                extend " Haw haw!" # @t_staira36.01 self.block='Last'
                # <ParallelEvent {'name': '_A'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(He’s got kind of a mischievous glint in his eyes…" # @t_staira37.00 self.block='Last'
                # <ParallelEvent {'name': '_B'} ParallelEvent ''>
                # <Events {} events ''>
                extend " Maybe it’d be better to keep an eye on him." # @t_staira37.01 self.block='Last'
                # <ParallelEvent {'name': '_C'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "And besides, it might actually be pretty fun to hang out with him…)" # @t_staira38.00 self.block='Last'
        if scene_picked_once_taira:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_taira}'} IfTrue ''>
            label s_day2p5_taira_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_taira}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_taira_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_taira_akimbo_happy as taira zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_taira_akimbo_happy as taira
                show i_cousin_default_neutral as cousin
                t_ch_taira "C’mon, Cuz, you know you want to!" # @t_staira39.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "(I actually kinda do want to, but he doesn’t need to know that.)" # @t_staira310.00 self.block='Last'
        menu:
            "Hang out with Taira today?"

            "Yes":
                $ slot_picked_taira_day3 = True
            "No":
                $ slot_picked_taira_day3 = False
        # <BranchMacro {'comparison': '!!${slot:picked_taira_day3}', 'name': '_3', 'path': 'taira/Chosen'} BranchMacro ''>
        if not not slot_picked_taira_day3:
            jump s_day2p5_taira_Chosen
        jump s_day2p5_taira_cleanup
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_taira_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            $ slot_pick_count_taira += 1
            # <NHSceneChange {'name': '_1', 'scene': 's_taira3'} NHSceneChange ''>
            label s_day2p5_taira_Chosen__1:
                # <NHSceneChange {'name': '_1', 'scene': 's_taira3'} NHSceneChange ''>
                jump s_taira3
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_taira_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_taira_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_taira_akimbo_happy as taira:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_taira_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide taira
                # Pass (ActorReset)
                $ scene_picked_once_taira = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'terezi'} Macro ''>
    label s_day2p5_terezi:
        # <Macro {'name': 'terezi'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_terezi:
            # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_terezi}'} IfFalse ''>
            label s_day2p5_terezi_FirstTime:
                # <IfFalse {'name': 'FirstTime', 'value': '${scene:picked_once_terezi}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_terezi_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_terezi_default_grin as terezi zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_default_grin as terezi
                show i_cousin_default_neutral as cousin
                t_ch_terezi "H3Y [slot_playerName]" # @t_sterezi30.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_terezi "D1D YOU NOT1C3 4NYTH1NG…" # @t_sterezi31.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_lean_grin as terezi
                t_ch_terezi "UNUSU4L 1N YOUR D3SK TOD4Y?! >:]" # @t_sterezi32.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "Uh, not really…" # @t_sterezi33.00 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_terezi "W3LL, CH3CK 4G41N, DUMMY" # @t_sterezi34.00 self.block='Last'
                # <ParallelEvent {'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "(Okay, let’s see what’s in my desk…" # @t_sterezi35.00 self.block='Last'
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_exhausted_mortified as cousin
                extend " Hopefully nothing that will kill me.)" # @t_sterezi35.01 self.block='Last'
                # <ParallelEvent {'name': '_8'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "Huh. It seems to be a crudely drawn picture of me…" # @t_sterezi36.00 self.block='Last'
                # <ParallelEvent {'name': '_9'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_exhausted_surprised as cousin
                extend " Riding a giant donut?" # @t_sterezi36.01 self.block='Last'
                # <ParallelEvent {'name': '_A'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "It says “H3y Cotton C4ndy, 1s th1s you.”" # @t_sterezi37.00 self.block='Last'
                # <ParallelEvent {'name': '_B'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_default_huh as terezi
                t_ch_terezi "WOW" # @t_sterezi38.00 self.block='Last'
                # <ParallelEvent {'name': '_C'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_terezi "1S TH4T R34LLY WH4T YOU TH1NK MY VO1C3 SOUNDS L1K3? >:/" # @t_sterezi39.00 self.block='Last'
                # <ParallelEvent {'name': '_D'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Sorry. I’m not so good at doing voices." # @t_sterezi310.00 self.block='Last'
                # <ParallelEvent {'name': '_E'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_terezi "H3H3 Y34H 1 NOT1C3D" # @t_sterezi311.00 self.block='Last'
                # <ParallelEvent {'name': '_F'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_lean_huh as terezi
                t_ch_terezi "H3Y TH3R3’S MOR3 WR1TT3N TH3R3" # @t_sterezi312.00 self.block='Last'
                # <ParallelEvent {'name': '_G'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "Okay, it says, um…" # @t_sterezi313.00 self.block='Last'
                # <ParallelEvent {'name': '_H'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "“PL34S3 COM3 M33T M3 OUTS1D3 ON TH3 SCHOOL GROUNDS”?" # @t_sterezi314.00 self.block='Last'
                # <ParallelEvent {'name': '_I'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Was that a better imitation?" # @t_sterezi315.00 self.block='Last'
                # <ParallelEvent {'name': '_J'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_terezi "HMMM… >:/" # @t_sterezi316.00 self.block='Last'
                # <ParallelEvent {'name': '_K'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_lean_pout as terezi
                t_ch_terezi "YOU’R3 ST1LL M1SS1NG SOM3TH1NG…" # @t_sterezi317.00 self.block='Last'
                # <ParallelEvent {'name': '_L'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "Uhh…" # @t_sterezi318.00 self.block='Last'
                # <ParallelEvent {'name': '_M'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "“HOW’S TH1S, T3R3Z1?”" # @t_sterezi319.00 self.block='Last'
                # <ParallelEvent {'name': '_N'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_default_laugh as terezi
                t_ch_terezi "H3H3H3H3H3!" # @t_sterezi320.00 self.block='Last'
                # <ParallelEvent {'name': '_O'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_terezi "WOW TH4T’S SOOOOO P3RF3CT <3" # @t_sterezi321.00 self.block='Last'
                # <ParallelEvent {'name': '_P'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_terezi "1 C4N’T B3L13V3 1T! 1T’S L1K3 LOOK1NG 1NTO ON3 OF YOUR HUM4N “M1RRORS”" # @t_sterezi322.00 self.block='Last'
                # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_lean_laugh as terezi
                t_ch_terezi "OR WH4T3V3R TH3 SOUND V3RS1ON OF 4 M1RROR 1S" # @t_sterezi323.00 self.block='Last'
                # <ParallelEvent {'name': '_R'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_sad as cousin
                t_ch_cousin "I don’t think there’s such thing as a “human sound mirror”." # @t_sterezi324.00 self.block='Last'
                # <ParallelEvent {'name': '_S'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_lean_grin as terezi
                t_ch_terezi "R34LLY?" # @t_sterezi325.00 self.block='Last'
                # <ParallelEvent {'name': '_T'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_terezi "WOW, HUM4NS 4R3 SO L4M3" # @t_sterezi326.00 self.block='Last'
                # <ParallelEvent {'name': '_U'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                t_ch_terezi "SO 4NYW4Y! WH4T DO YOU S4Y, COTTON C4NDY?" # @t_sterezi327.00 self.block='Last'
        if scene_picked_once_terezi:
            # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_terezi}'} IfTrue ''>
            label s_day2p5_terezi_Loop:
                # <IfTrue {'name': 'Loop', 'value': '${scene:picked_once_terezi}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_terezi_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_surprised as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_terezi_default_pout as terezi zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_default_pout as terezi
                show i_cousin_default_surprised as cousin
                t_ch_terezi "CMON, DONT B3 4 LOS3R >:P" # @t_sterezi328.00 self.block='Last'
        menu:
            "Meet with Terezi out on the grounds?"

            "Y3S!":
                $ slot_picked_terezi_day3 = True
            "I’m not sure.":
                $ slot_picked_terezi_day3 = False
        # <BranchMacro {'comparison': '!!${slot:picked_terezi_day3}', 'name': '_3', 'path': 'terezi/Chosen'} BranchMacro ''>
        if not not slot_picked_terezi_day3:
            jump s_day2p5_terezi_Chosen
        jump s_day2p5_terezi_cleanup
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_terezi_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_terezi_default_grin as terezi
            show i_cousin_default_neutral as cousin
            t_ch_terezi "4W3SOM3! 1’LL M33T YOU OUTS1D3 1N 4 F3W M1NUT3S" # @t_sterezi329.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_terezi "DONT B3 L4T3!!!" # @t_sterezi330.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "W-wait.." # @t_sterezi331.00 self.block='Last'
            # <ParallelEvent {'name': '_3'} ParallelEvent ''>
            # <Events {} events ''>
            extend " You meant right now?" # @t_sterezi331.01 self.block='Last'
            # <ParallelEvent {'name': '_4'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "But we’re in the middle of detention!" # @t_sterezi332.00 self.block='Last'
            # <ParallelEvent {'name': '_5'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_surprised as cousin
            extend " Won’t we get in trouble?" # @t_sterezi332.01 self.block='Last'
            # <ParallelEvent {'name': '_6'} ParallelEvent ''>
            # <Events {} events ''>
            show i_terezi_default_laugh as terezi
            t_ch_terezi "H3H3H3 <3" # @t_sterezi333.00 self.block='Last'
            show i_terezi_default_laugh as terezi:
                # ShowWithAtl
                linear .333 alpha 0.0
            # <ParallelEvent {'name': '_8'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_exhausted_surprised as cousin
            t_ch_cousin "Sh-she’s gone…" # @t_sterezi334.00 self.block='Last'
            # <ParallelEvent {'name': '_9'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_exhausted_neutral as cousin
            t_ch_cousin "If I’d have known this is what she meant…" # @t_sterezi335.00 self.block='Last'
            # <ParallelEvent {'name': '_A'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_exhausted_mortified as cousin
            extend " I wouldn’t have agreed to this!" # @t_sterezi335.01 self.block='Last'
            # <ParallelEvent {'name': '_B'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "But I already have, and…" # @t_sterezi336.00 self.block='Last'
            # <ParallelEvent {'name': '_C'} ParallelEvent ''>
            # <Events {} events ''>
            extend " I really don’t want to see what happens when I don’t keep a promise to Terezi Pyrope." # @t_sterezi336.01 self.block='Last'
            # <ParallelEvent {'name': '_D'} ParallelEvent ''>
            # <Events {} events ''>
            t_ch_cousin "...I’d better get going…" # @t_sterezi337.00 self.block='Last'
            $ slot_pick_count_terezi += 1
            # <NHSceneChange {'name': '_F', 'scene': 's_terezi3'} NHSceneChange ''>
            label s_day2p5_terezi_Chosen__F:
                # <NHSceneChange {'name': '_F', 'scene': 's_terezi3'} NHSceneChange ''>
                jump s_terezi3
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_terezi_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_terezi_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_terezi_default_laugh as terezi:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_terezi_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide terezi
                # Pass (ActorReset)
                $ scene_picked_once_terezi = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'tomari'} Macro ''>
    label s_day2p5_tomari:
        # <Macro {'name': 'tomari'} Macro ''>
        # <Events {} events ''>
        if not scene_picked_once_tomari:
            # <IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_tomari}'} IfFalse ''>
            label s_day2p5_tomari_FirstTime:
                # <IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_tomari}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_tomari_FirstTime_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_tomari_notebook_thinking as tomari zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_tomari_notebook_thinking as tomari
                t_ch_cousin "Tomari! How’s that research coming?" # @t_stomari215.00a self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_tomari_standing_smile as tomari
                t_ch_tomari "Not bad, [slot_playerName]! But it’ll be better once you’re helping!" # @t_stomari215.00b self.block='Last'
                menu:
                    "I could really use some help."

                    "Help Tomari, it's worked out great so far!":
                        $ slot_picked_tomari_day3 = True
                    "End the charade already!":
                        $ slot_picked_tomari_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_tomari_day3}', 'name': '_4', 'path': 'tomari/Chosen'} BranchMacro ''>
                if not not slot_picked_tomari_day3:
                    jump s_day2p5_tomari_Chosen
                jump s_day2p5_tomari_PassedFirstTime
        if scene_picked_once_tomari:
            # <IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_tomari}'} IfTrue ''>
            label s_day2p5_tomari_Loop:
                # <IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_tomari}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_tomari_Loop_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_tomari_pondering_smile as tomari zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                show i_tomari_pondering_smile as tomari
                t_ch_tomari "I could use another pair of eyes on the research material I compiled. What do you say, [slot_playerName]?" # @t_stomari219.00a self.block='Last'
                menu:
                    "I could use another pair of eyes on the research material I compiled. What do you say, ${slot:playerName}?"

                    "Research ahoy!":
                        $ slot_picked_tomari_day3 = True
                    "Better skip it.":
                        $ slot_picked_tomari_day3 = False
                # <BranchMacro {'comparison': '!!${slot:picked_tomari_day3}', 'name': '_3', 'path': 'tomari/Chosen'} BranchMacro ''>
                if not not slot_picked_tomari_day3:
                    jump s_day2p5_tomari_Chosen
                jump s_day2p5_tomari_PassedLoop
        # <Macro {'name': 'Chosen'} Macro ''>
        label s_day2p5_tomari_Chosen:
            # <Macro {'name': 'Chosen'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_energetic_neutral as cousin
            show i_tomari_standing_smile as tomari
            t_ch_cousin "Uh. Yeah. Me and the helping." # @t_stomari216.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_energetic_surprise as cousin
            t_ch_cousin "WHAT COULD GO WRONG?" # @t_stomari217.00 self.block='Last'
            $ slot_pick_count_tomari += 1
            # <NHSceneChange {'name': '_3', 'scene': 's_tomari3'} NHSceneChange ''>
            label s_day2p5_tomari_Chosen__3:
                # <NHSceneChange {'name': '_3', 'scene': 's_tomari3'} NHSceneChange ''>
                jump s_tomari3
        # <Macro {'name': 'PassedFirstTime'} Macro ''>
        label s_day2p5_tomari_PassedFirstTime:
            # <Macro {'name': 'PassedFirstTime'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_tomari_standing_smile as tomari
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Research, huh?" # @t_stomari218.00 self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Lemme get back to you on that one." # @t_stomari219.00 self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_energetic_neutral as cousin
            extend " (Nope!)" # @t_stomari219.01 self.block='Last'
            jump s_day2p5_tomari_cleanup
        # <Macro {'name': 'PassedLoop'} Macro ''>
        label s_day2p5_tomari_PassedLoop:
            # <Macro {'name': 'PassedLoop'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'name': '_0'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            show i_tomari_pondering_smile as tomari
            t_ch_cousin "Oh, uh, yeah. That’d be great." # @t_stomari219.00d self.block='Last'
            # <ParallelEvent {'name': '_1'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "It might take me awhile to get there though. A LONG, LONG WHILE." # @t_stomari219.00e self.block='Last'
            # <ParallelEvent {'name': '_2'} ParallelEvent ''>
            # <Events {} events ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "You, um, get started without me." # @t_stomari219.00f self.block='Last'
            jump s_day2p5_tomari_cleanup
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_tomari_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_tomari_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_tomari_pondering_smile as tomari:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_tomari_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide tomari
                # Pass (ActorReset)
                $ scene_picked_once_tomari = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice
    # <Macro {'name': 'valk'} Macro ''>
    label s_day2p5_valk:
        # <Macro {'name': 'valk'} Macro ''>
        # <Events {} events ''>
        if slot_picked_valk_day1:
            # <IfTrue {'name': 'didEvent1', 'value': '${slot:picked_valk_day1}'} IfTrue ''>
            label s_day2p5_valk_didEvent1:
                # <IfTrue {'name': 'didEvent1', 'value': '${slot:picked_valk_day1}'} IfTrue ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_valk_didEvent1_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 3:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_valkyrie_default_grin as valkyrie zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_valkyrie_default_grin as valkyrie
                show i_cousin_default_neutral as cousin
                t_ch_valkyrie "Hey cutie! Ready for some pwnage on the roof?" # @t_svalk30.00 self.block='Last'
                menu:
                    "Hey cutie! Ready for some pwnage on the roof?"

                    "W-What kind of pwnage?":
                        $ slot_picked_valk_day3 = True
                    "Maybe later...":
                        $ slot_picked_valk_day3 = False
                if slot_picked_valk_day3:
                    # <IfTrue {'name': 'Chosen', 'value': '${slot:picked_valk_day3}'} IfTrue ''>
                    label s_day2p5_valk_didEvent1_Chosen:
                        # <IfTrue {'name': 'Chosen', 'value': '${slot:picked_valk_day3}'} IfTrue ''>
                        # <Events {} events ''>
                        # <ParallelEvent {'name': '_0'} ParallelEvent ''>
                        # <Events {} events ''>
                        show i_cousin_default_surprised as cousin
                        t_ch_cousin "W-What kind of pwnage?" # @t_svalk31.00 self.block='Last'
                        # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                        # <Events {} events ''>
                        show i_valkyrie_default_wink as valkyrie
                        t_ch_valkyrie "I'll give you a hint... It involves rigorous physical activity!" # @t_svalk32.00 self.block='Last'
                        # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                        # <Events {} events ''>
                        show i_cousin_default_surprised_blush as cousin
                        t_ch_cousin "Oh gosh." # @t_svalk33.00 self.block='Last'
                        # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                        # <Events {} events ''>
                        show i_valkyrie_forjustice_grin as valkyrie:
                            # ShowWithAtl
                            linear 0.5 xpos 0.5 
                        extend "{w=0.5}{nw}"
                        t_ch_valkyrie "Come on!" # @t_svalk34.00 self.block='Last'
                        # <ParallelEvent {'allowInterrupt': 'false', 'name': '_4'} ParallelEvent ''>
                        # <Events {} events ''>
                        show i_cousin_energetic_surprise_blush as cousin:
                            # ShowWithAtl
                            pause 0.5 
                            linear .2 xpos 0.3 
                            # ShowWithAtl
                            pause 1.0 
                            linear .2 xpos 0.35 
                            # ShowWithAtl
                            pause 1.5 
                            linear .2 xpos 0.4 
                        show i_valkyrie_forjustice_grin as valkyrie:
                            # ShowWithAtl
                            pause 0.5 
                            linear .2 xpos 0.55 
                            # ShowWithAtl
                            pause 1.0 
                            linear .2 xpos 0.6 
                            # ShowWithAtl
                            pause 1.5 
                            linear .2 xpos 0.65 
                        extend "{w=1.7}{nw}"
                        t_ch_cousin "(AH! She grabbed my hand! She's pulling me along... I can't escape!)" # @t_svalk35.00 self.block='Last'
                        # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                        # <Events {} events ''>
                        show i_cousin_energetic_neutral_blush as cousin
                        t_ch_cousin "(Though I'm not sure I want to... )" # @t_svalk36.00 self.block='Last'
                        $ slot_pick_count_valk += 1
                        # <NHSceneChange {'name': '_7', 'scene': 's_valk3'} NHSceneChange ''>
                        label s_day2p5_valk_didEvent1_Chosen__7:
                            # <NHSceneChange {'name': '_7', 'scene': 's_valk3'} NHSceneChange ''>
                            jump s_valk3
                # <Macro {'name': 'Passed'} Macro ''>
                label s_day2p5_valk_didEvent1_Passed:
                    # <Macro {'name': 'Passed'} Macro ''>
                    # <Events {} events ''>
                    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_valkyrie_default_grin as valkyrie:
                        # ShowWithAtl
                        linear 0.5 xpos 0.75 
                    show i_cousin_default_neutral as cousin:
                        # ShowWithAtl
                        linear 0.5 xpos 0.25 
                    extend "{w=0.5}{nw}"
                    t_ch_cousin "Maybe later..." # @t_svalk37.00 self.block='Last'
                    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_valkyrie_armscrossed_wink as valkyrie
                    t_ch_valkyrie "Yeah, maybe we should wait til it's dark out..." # @t_svalk38.00 self.block='Last'
                    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_exhausted_surprised_blush as cousin
                    t_ch_cousin "(What does THAT mean!?" # @t_svalk39.00 self.block='Last'
                    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                    # <Events {} events ''>
                    extend " I better leave... )" # @t_svalk39.01 self.block='Last'
                    jump s_day2p5_valk_cleanup
        if not slot_picked_valk_day1:
            # <IfFalse {'name': 'didntEvent1', 'value': '${slot:picked_valk_day1}'} IfFalse ''>
            label s_day2p5_valk_didntEvent1:
                # <IfFalse {'name': 'didntEvent1', 'value': '${slot:picked_valk_day1}'} IfFalse ''>
                # <Events {} events ''>
                # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                label s_day2p5_valk_didntEvent1_warm:
                    # <ParallelEvent {'auto': 'true', 'name': 'warm'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_neutral as cousin zorder 3:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_valkyrie_default_wink as valkyrie zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5) # TimedPause
                # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 xpos 0.25 
                show i_valkyrie_default_wink as valkyrie
                extend "{w=0.5}{nw}"
                t_ch_valkyrie "Hey, new kid!" # @t_svalk310.00 self.block='Last'
                # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Me?" # @t_svalk311.00 self.block='Last'
                # <ParallelEvent {'name': '_3'} ParallelEvent ''>
                # <Events {} events ''>
                show i_valkyrie_armscrossed_wink as valkyrie
                t_ch_valkyrie "Yes you! Whatcha been up to, cutie?" # @t_svalk312.00 self.block='Last'
                # <ParallelEvent {'name': '_4'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Um... Not much. Just... Hanging out. You know." # @t_svalk313.00 self.block='Last'
                # <ParallelEvent {'name': '_5'} ParallelEvent ''>
                # <Events {} events ''>
                t_ch_cousin "What about you?" # @t_svalk314.00 self.block='Last'
                # <ParallelEvent {'name': '_6'} ParallelEvent ''>
                # <Events {} events ''>
                show i_valkyrie_default_thoughtful as valkyrie
                t_ch_valkyrie "I want to try something out, but it's gotta be away from prying eyes." # @t_svalk315.00 self.block='Last'
                # <ParallelEvent {'name': '_7'} ParallelEvent ''>
                # <Events {} events ''>
                show i_cousin_default_neutral_blush as cousin
                with Dissolve(0.5)
                extend " Come up to the roof with me!" # @t_svalk315.01 self.block='Last'
                menu:
                    "Come up to the roof with me!"

                    "Sure, why not.  Nothing can possibly go wrong.":
                        $ slot_picked_valk_day3 = True
                    "I'm more comfortable with the prying eyes, thanks.":
                        $ slot_picked_valk_day3 = False
                if slot_picked_valk_day3:
                    # <IfTrue {'name': 'Chosen', 'value': '${slot:picked_valk_day3}'} IfTrue ''>
                    label s_day2p5_valk_didntEvent1_Chosen:
                        # <IfTrue {'name': 'Chosen', 'value': '${slot:picked_valk_day3}'} IfTrue ''>
                        # <Events {} events ''>
                        # <ParallelEvent {'name': '_0'} ParallelEvent ''>
                        # <Events {} events ''>
                        t_ch_cousin "Sure, why not?" # @t_svalk316.00 self.block='Last'
                        # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                        # <Events {} events ''>
                        extend " What could possibly go wrong?" # @t_svalk316.01 self.block='Last'
                        # <ParallelEvent {'name': '_2'} ParallelEvent ''>
                        # <Events {} events ''>
                        show i_valkyrie_akimbo_wink as valkyrie:
                            # ShowWithAtl
                            linear 0.5 xpos 0.5 
                        extend "{w=0.5}{nw}"
                        t_ch_valkyrie "That's the spirit!" # @t_svalk317.00 self.block='Last'
                        # <ParallelEvent {'allowInterrupt': 'false', 'name': '_3'} ParallelEvent ''>
                        # <Events {} events ''>
                        show i_cousin_energetic_surprise_blush as cousin:
                            # ShowWithAtl
                            pause 0.5 
                            linear .2 xpos 0.3 
                            # ShowWithAtl
                            pause 1.0 
                            linear .2 xpos 0.35 
                            # ShowWithAtl
                            pause 1.5 
                            linear .2 xpos 0.4 
                        show i_valkyrie_akimbo_wink as valkyrie:
                            # ShowWithAtl
                            pause 0.5 
                            linear .2 xpos 0.55 
                            # ShowWithAtl
                            pause 1.0 
                            linear .2 xpos 0.6 
                            # ShowWithAtl
                            pause 1.5 
                            linear .2 xpos 0.65 
                        extend "{w=1.7}{nw}"
                        t_ch_cousin "(AH! She grabbed my hand! She's pulling me along... I can't escape!)" # @t_svalk318.00 self.block='Last'
                        $ slot_pick_count_valk += 1
                        # <NHSceneChange {'name': '_5', 'scene': 's_valk3'} NHSceneChange ''>
                        label s_day2p5_valk_didntEvent1_Chosen__5:
                            # <NHSceneChange {'name': '_5', 'scene': 's_valk3'} NHSceneChange ''>
                            jump s_valk3
                # <Macro {'name': 'Passed'} Macro ''>
                label s_day2p5_valk_didntEvent1_Passed:
                    # <Macro {'name': 'Passed'} Macro ''>
                    # <Events {} events ''>
                    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_cousin_default_surprised_blush as cousin
                    t_ch_cousin "I'm more comfortable with the prying eyes, thanks." # @t_svalk319.00 self.block='Last'
                    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
                    # <Events {} events ''>
                    show i_valkyrie_akimbo_thoughtful as valkyrie
                    t_ch_valkyrie "Suit yourself. If you're gonna change your mind, do it quick... I'm not gonna be here forever." # @t_svalk320.00 self.block='Last'
                    jump s_day2p5_valk_cleanup
        # <Macro {'name': 'cleanup'} Macro ''>
        label s_day2p5_valk_cleanup:
            # <Macro {'name': 'cleanup'} Macro ''>
            # <Events {} events ''>
            # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
            label s_day2p5_valk_cleanup_cleanup:
                # <ParallelEvent {'auto': 'true', 'name': 'cleanup'} ParallelEvent ''>
                # <Events {} events ''>
                show i_valkyrie_akimbo_thoughtful as valkyrie:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_surprised_blush as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5) # TimedPause
            # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
            label s_day2p5_valk_cleanup_reset:
                # <ParallelEvent {'auto': 'true', 'name': 'reset'} ParallelEvent ''>
                # <Events {} events ''>
                hide valkyrie
                # Pass (ActorReset)
                $ scene_picked_once_valk = True
                # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
            jump s_day2p5_day2p5prechoice