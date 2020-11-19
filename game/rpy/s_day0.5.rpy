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
# <Scene scene {'id': 's_day0.5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_day0p5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_day0p5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_day0.5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day0.5initialize', 'kind': 'ParallelEvent'} ''>
    label s_day0p5_day0p5initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day0.5initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
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
        show i_bg_quad_tents as bg zorder 1 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_sw_white as white_swatch zorder 15:
            default
            alpha 0.0
        show i_cousin_default_neutral as cousin zorder 2:
            default
            alpha 1.0

    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bg_school_front as school:
        # ShowWithAtl
        pause 8.0 
        linear 1 alpha 0.0
    play sound "sfx/westminster.ogg"
    narrator "The next day ...{nw}" # @t_ui_nextday self.block=False
    extend "{w=17.0}{nw}"
    # Blank text event <TextEvent TextEvent {'char': '', 'delay': '8', 'text': '', 'kind': 'TextEvent'} ''>
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    hide school
    play music "bgm/aroundtown.ogg" loop
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_cousin "(Joining a club and showing school spirit to reduce my detention sentence…)" # @t_scousin10.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(I wonder if there’s any other students from detention that are taking up the offer?)" # @t_scousin11.00 self.block='Last'
    show i_cousin_default_grin as cousin:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day0.5prechoice', 'kind': 'ParallelEvent'} ''>
    label s_day0p5_day0p5prechoice:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day0.5prechoice', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
    $ s_day0p5_has_picked_any = False if not "s_day0p5_has_picked_any" in store.__dict__ else s_day0p5_has_picked_any
    window hide
    menu (screen="ChoiceExploration"):
        "Aki Matsuo":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_amazona
        "Albatross":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_albatros
        "Anti-Bravoman":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_antibravo
        "Blue Max":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_bluemax
        "Davesprite":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_davesprite
        "Donko":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_donko
        "Galaga":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_galaga
        "Hiromi":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_hiromi
        "Jane Crocker":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_jane
        "Lolo":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_lolo
        "Meowkie":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_meowkie
        "Mr. Driller":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_mrdriller
        "Nidia":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_nidia
        "Richard Miller":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_richard
        "Taira":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_taira
        "Terezi Pyrope":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_terezi
        "Tomari":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_tomari
        "Valkyrie":
            $ s_day0p5_has_picked_any = True
            window show
            jump s_day0p5_valk
        "Don't join a club." if s_day0p5_has_picked_any:
            window show
            jump s_day0p5_cousin
    # <Macro Macro {'name': 'albatros', 'kind': 'Macro'} ''>
    label s_day0p5_albatros:
        # <Macro Macro {'name': 'albatros', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_albatros:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_albatros}', 'kind': 'IfFalse'} ''>
            label s_day0p5_albatros_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_albatros}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_albatros_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_albatross_watch_inquisitive as albatros zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_albatross_watch_inquisitive as albatros
                t_ch_cousin "(Oh, there’s that really cool kid. Alfonso.)" # @t_salbatros10.00 self.block='Last'
                show i_albatross_watch_inquisitive as albatros:
                    # FadeEvent
                    linear 0.5 alpha 1.0
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                play sound "sfx/albatrosswatchbeep.ogg"
                t_ch_cousin "(Didn’t figure he’d go in for a club.)" # @t_salbatros11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Oh, uh, hey." # @t_salbatros11.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_watch_smirk_wink as albatros
                t_ch_albatros "Hey, you’re the new kid." # @t_salbatros12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_albatros "Lookin’ for a way out of detention, huh?" # @t_salbatros13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_grin_blush as cousin
                t_ch_cousin "Y-yeah, yup. That’s me." # @t_salbatros14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_laugh_blush as cousin
                t_ch_cousin "So, uh, what’re, uh, you. Um. In for?" # @t_salbatros15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_toocool_inquisitive as albatros
                t_ch_albatros "Me?" # @t_salbatros16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_toocool_smug as albatros
                t_ch_albatros "Oh, I go where the trouble is." # @t_salbatros17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_neutral as cousin
                t_ch_cousin "(Maybe he’s like one of those kids who always gets in trouble!)" # @t_salbatros18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(He looks a little old, come to think of it.)" # @t_salbatros19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(M-maybe he got into so much trouble he had to…)" # @t_salbatros110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_mortified as cousin
                extend " (...REPEAT A GRADE!!!)" # @t_salbatros110.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                extend " Heh. Yeah. I know how that is." # @t_salbatros110.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_albatros "Yeah." # @t_salbatros111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_albatros "You look it." # @t_salbatros112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_albatros "Name’s Alfonso B. Tross. Which is totally plausible." # @t_salbatros113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_albatros "Most folks just call me Al B. Tross for short." # @t_salbatros114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Or Al for shorter. As in Capone." # @t_salbatros114.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "(Wow, Capone like the gangster?)" # @t_salbatros115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Gosh!)" # @t_salbatros116.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_albatros "You should think about joining my criminal justice club." # @t_salbatros117.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_welcome_smirk_wink as albatros
                t_ch_albatros "You’d fit right in with that devil may care attitude of yours." # @t_salbatros118.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Wait. Are they crime fighters?)" # @t_salbatros119.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(TEENAGE crime fighters?!)" # @t_salbatros120.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                extend " I, uh. Yeah" # @t_salbatros120.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " (Gotta keep sounding aloof and cool just to keep up with Al though!)" # @t_salbatros120.02 self.block='Last'
                menu:
                    "JOIN AL’S CLUB":
                        $ slot_picked_albatros_day1 = True
                    "DO NOT JOIN AL’S CLUB":
                        $ slot_picked_albatros_day1 = False
        if scene_picked_once_albatros:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_albatros}', 'kind': 'IfTrue'} ''>
            label s_day0p5_albatros_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_albatros}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_albatros_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_albatross_watch_inquisitive as albatros zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_toocool_smug as albatros
                show i_cousin_default_neutral as cousin
                t_ch_albatros "Welcome back. Change your mind?" # @t_salbatros130.00 self.block='Last'
                menu:
                    "JOIN THE CRIMINAL JUSTICE CLUB":
                        $ slot_picked_albatros_day1 = True
                    "NO WAY THAT’S TOO DANGEROUS!":
                        $ slot_picked_albatros_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_albatros_day1}', 'name': '_2', 'path': 'albatros/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_albatros_day1:
            jump s_day0p5_albatros_Chosen
        # <BranchMacro BranchMacro {'comparison': '!!${scene:picked_once_albatros}', 'name': '_3', 'path': 'albatros/PassedLoop', 'kind': 'BranchMacro'} ''>
        if not not scene_picked_once_albatros:
            jump s_day0p5_albatros_PassedLoop
        jump s_day0p5_albatros_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_albatros_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            $ print("HEY YOU PICKED AL COOL")
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Yeah, I’ll think about it." # @t_salbatros121.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "I mean. Maybe. If I feel like it." # @t_salbatros122.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_toocool_smug as albatros
            t_ch_albatros "Heh." # @t_salbatros123.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "I read you, [slot_playerName]." # @t_salbatros124.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "Loud and clear." # @t_salbatros125.00 self.block='Last'
            $ slot_pick_count_albatros += 1
            # <NHSceneChange NHSceneChange {'name': '_7', 'scene': 's_albatros1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_albatros_Chosen__7:
                # <NHSceneChange NHSceneChange {'name': '_7', 'scene': 's_albatros1', 'kind': 'NHSceneChange'} ''>
                jump s_albatros1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_albatros_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Um, I’ll think about it." # @t_salbatros126.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I mean. Maybe. If I’m not super busy being cool and aloof all over the place." # @t_salbatros127.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "Heh." # @t_salbatros128.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "I get’cha." # @t_salbatros129.00 self.block='Last'
            jump s_day0p5_albatros_cleanup
        # <Macro Macro {'name': 'PassedLoop', 'kind': 'Macro'} ''>
        label s_day0p5_albatros_PassedLoop:
            # <Macro Macro {'name': 'PassedLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Um, yeah, no. I don’t think so." # @t_salbatros131.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "Heh." # @t_salbatros132.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_toocool_inquisitive as albatros
            t_ch_albatros "If that’s the way you wanna play it." # @t_salbatros133.00 self.block='Last'
            jump s_day0p5_albatros_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_albatros_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_albatros_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_toocool_inquisitive as albatros:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_albatros_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide albatros
                # Pass (ActorReset)
                $ scene_picked_once_albatros = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'amazona', 'kind': 'Macro'} ''>
    label s_day0p5_amazona:
        # <Macro Macro {'name': 'amazona', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_amazona:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_amazona}', 'kind': 'IfFalse'} ''>
            label s_day0p5_amazona_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_amazona}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_amazona_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_aki_default_smile as aki zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_default_smile as aki
                show i_cousin_default_neutral as cousin
                t_ch_aki "Hey [slot_playerName]! How can I help you?" # @t_samazona10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "I was just wondering what you were up to." # @t_samazona11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_notebook_smile as aki
                t_ch_aki "Oh! I'm managing my club memberships. I use a spreadsheet to keep track of every club I'm enrolled in." # @t_samazona12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(She has a lot of paper in her hands... )" # @t_samazona13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "How many pages is that spreadsheet?!" # @t_samazona14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_notebook_focus as aki
                t_ch_aki "......" # @t_samazona15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_aki ".........." # @t_samazona16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_notebook_laughter as aki
                t_ch_aki ".... 22!" # @t_samazona17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_surprise as cousin
                t_ch_cousin "(WHAT!)" # @t_samazona18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "How do you have time to be in so many clubs?!" # @t_samazona19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_aki "Oh, silly. Being in all the clubs isn't a problem. It only starts to get stressful when I'm trying to prepare for finals AND I'm practicing for the school play AND it's the peak of Wrestleball season." # @t_samazona110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Wh... What???" # @t_samazona111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_notebook_laughter_nervous as aki
                t_ch_aki "Also, sometimes I'm campaigning for class president..." # @t_samazona112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_aki "But that's it! Hahahaha!" # @t_samazona113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "That's it huh..." # @t_samazona114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_notebook_overwhelmed as aki
                t_ch_aki "Well, not exactly. I usually have one or two after school jobs... Like being an idol! That's when it gets REALLY crazy." # @t_samazona115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_surprised as cousin
                t_ch_cousin "What are you saving for?! College?!" # @t_samazona116.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_aki "College? It's so I can still pay my bills during unpaid internships. On-the-job experience is very important." # @t_samazona117.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(I NEVER THOUGHT OF THAT)" # @t_samazona118.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_notebook_laughter_nervous as aki
                play sound ["<silence 1>", "sfx/sentaisignal.ogg"]
                t_ch_aki "And that's all on top of some of my... Other responsibilities." # @t_samazona119.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "(HOW ARE YOU ALIVE)" # @t_samazona120.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_surprised as cousin
                t_ch_cousin "H-how can you do all of that?!" # @t_samazona121.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_akimbo_laughter as aki
                t_ch_aki "Well, I take my time on earth very seriously." # @t_samazona122.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_akimbo_laughter_nervous as aki
                t_ch_aki "Although sometimes it does get to be a little much... Hahahahaha!" # @t_samazona123.00 self.block='Last'
                menu:
                    "Offer to be Aki's assistant.":
                        $ slot_picked_amazona_day1 = True
                    "Wish her luck.":
                        $ slot_picked_amazona_day1 = False
        if scene_picked_once_amazona:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_amazona}', 'kind': 'IfTrue'} ''>
            label s_day0p5_amazona_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_amazona}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_amazona_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_aki_default_smile as aki zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Hmm… it seems like Aki is juggling a lot. Should I offer to be her assistant?)" # @t_samazona138.00a self.block='Last'
                menu:
                    "Hang out with Aki?"

                    "Yes":
                        $ slot_picked_amazona_day1 = True
                    "No":
                        $ slot_picked_amazona_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_amazona_day1}', 'name': '_2', 'path': 'amazona/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_amazona_day1:
            jump s_day0p5_amazona_Chosen
        jump s_day0p5_amazona_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_amazona_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "You need an assistant! Or maybe a half-dozen clones of yourself..." # @t_samazona124.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_notebook_shocked as aki
            t_ch_aki "Tomari already tried that... And who would EVER want to be my assistant?! An unpaid position, I should point out." # @t_samazona125.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_neutral as cousin
            t_ch_cousin "I'll do it! I'm sure this will be some great on-the-job experience!" # @t_samazona126.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_notebook_laughter_nervous as aki
            t_ch_aki "I know, ridiculous right? Hahahaha!" # @t_samazona127.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_notebook_shocked as aki
            t_ch_aki "Wait... You will?!" # @t_samazona128.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_aki "Wait, no... I can't. Bad idea!" # @t_samazona129.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "No way! This is going to be great!" # @t_samazona130.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Being Aki's assistant... Might be my ticket out of detention.)" # @t_samazona131.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(If all of these bad kids in detention rub off on me, I'll be a delinquent forever.)" # @t_samazona132.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Besides, I could learn so much from her!)" # @t_samazona133.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_laugh as cousin
            t_ch_cousin "This is definitely the best idea I've ever had!" # @t_samazona134.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_default_nervouslaughter as aki
            t_ch_aki "Aha... Hahahahaa..... Haaaaa.... Well, I don't need an assistant, but... Maybe we can hang out." # @t_samazona135.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(CLOSE ENOUGH... I WILL be your assistant, Aki! You need all the help you can get!)" # @t_samazona136.00 self.block='Last'
            $ slot_pick_count_amazona += 1
            # <NHSceneChange NHSceneChange {'name': '_E', 'scene': 's_amazona1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_amazona_Chosen__E:
                # <NHSceneChange NHSceneChange {'name': '_E', 'scene': 's_amazona1', 'kind': 'NHSceneChange'} ''>
                jump s_amazona1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_amazona_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_aki_akimbo_laughter_nervous as aki
            t_ch_cousin "Well... Good luck with all of that stuff!" # @t_samazona137.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_aki "Thanks! Hahahaha. But as Hiromi says, luck's got nothing to do with it." # @t_samazona138.00 self.block='Last'
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_amazona_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_amazona_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_aki_akimbo_laughter_nervous as aki:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_amazona_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide aki
                # Pass (ActorReset)
                $ scene_picked_once_amazona = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'antibravo', 'kind': 'Macro'} ''>
    label s_day0p5_antibravo:
        # <Macro Macro {'name': 'antibravo', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_antibravo:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_antibravo}', 'kind': 'IfFalse'} ''>
            label s_day0p5_antibravo_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_antibravo}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_antibravo_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_abm_default_sad as antibravo zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_abm_default_sad as antibravo
                show i_cousin_default_neutral as cousin
                t_ch_antibravo "I can't control... This thing inside of me... This... This..." # @t_santibravo10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_mortified as cousin
                t_ch_cousin "Monster?" # @t_santibravo11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_abm_default_surprised_blush as antibravo
                t_ch_antibravo "Huh?! No..." # @t_santibravo12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I was talking about breakfast..." # @t_santibravo12.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_abm_default_broody as antibravo:
                    linear .25 xzoom -1.0 
                extend " What're YOU talking about?" # @t_santibravo12.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "Er, nothing." # @t_santibravo13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " Listen, I have to join a club..." # @t_santibravo13.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " And I was thinking of Poetry Club." # @t_santibravo13.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_antibravo "Poetry Club's full of nice people..." # @t_santibravo14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_abm_shadowknows_broody as antibravo
                extend " And ME." # @t_santibravo14.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Uh." # @t_santibravo15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_antibravo "I can't stop you... But I can't recommend it." # @t_santibravo16.00 self.block='Last'
                menu:
                    "Go to Poetry Club?"

                    "I'll take my chances...":
                        $ slot_picked_antibravo_day1 = True
                    "What club DO you recommend?":
                        $ slot_picked_antibravo_day1 = False
        if scene_picked_once_antibravo:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_antibravo}', 'kind': 'IfTrue'} ''>
            label s_day0p5_antibravo_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_antibravo}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_antibravo_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_abm_default_sad as antibravo zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 xpos 0.25 
                show i_abm_default_sad as antibravo:
                    # ShowWithAtl
                    linear 0.5 xpos 0.75 
                extend "{w=0.5}{nw}"
                t_ch_antibravo "I can’t recommend Poetry Club… because it’s where my murk lurks." # @t_santibravo126.00a self.block='Last'
                menu:
                    "Go to Poetry Club?"

                    "I'll take my chances...":
                        $ slot_picked_antibravo_day1 = True
                    "What club DO you recommend?":
                        $ slot_picked_antibravo_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_antibravo_day1}', 'name': '_2', 'path': 'antibravo/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_antibravo_day1:
            jump s_day0p5_antibravo_Chosen
        jump s_day0p5_antibravo_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_antibravo_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I'll take my chances..." # @t_santibravo17.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "It's for the best. You don't want to be anywhere near...." # @t_santibravo18.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_shadowknows_surprised as antibravo
            extend " Wait what?" # @t_santibravo18.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "I wanna try Poetry Club. Sounds fun." # @t_santibravo19.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_shadowknows_broody as antibravo
            t_ch_antibravo "Oh... Well... I can't ... I shouldn't take you there. I can't be held responsible for what happens if you're within 50 feet of me..." # @t_santibravo110.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Is he talking..." # @t_santibravo111.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            extend " About a restraining order?!)" # @t_santibravo111.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "But if I walked in the direction of the club and you just HAPPENED to follow me... That'd probably be okay..." # @t_santibravo112.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Ummm... Okay. So I should follow you" # @t_santibravo113.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " but pretend like I'm not following you?" # @t_santibravo113.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "Yeah." # @t_santibravo114.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Okay." # @t_santibravo115.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_backturned_broody as antibravo
            t_ch_antibravo "Um... I'M LEAVING NOW. GOLLY, I SURE HOPE NO ONE FOLLOWS ME..." # @t_santibravo116.00 self.block='Last'
            show i_abm_backturned_broody as antibravo:
                # FadeEvent
                linear 0.5 alpha 0.0
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_surprise as cousin
            t_ch_cousin "Er... NOW I'M WALKING IN THE EXACT SAME DIRECTION FOR NO PARTICULAR REASON..." # @t_santibravo117.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                ease_expo .5 xpos 0.5 
            show i_abm_backturned_broody as antibravo
            extend "{w=0.5}{nw}"
            t_ch_cousin "...................." # @t_santibravo118.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Sheesh..." # @t_santibravo119.00 self.block='Last'
            $ slot_pick_count_antibravo += 1
            # <NHSceneChange NHSceneChange {'name': '_I', 'scene': 's_antibravo1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_antibravo_Chosen__I:
                # <NHSceneChange NHSceneChange {'name': '_I', 'scene': 's_antibravo1', 'kind': 'NHSceneChange'} ''>
                jump s_antibravo1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_antibravo_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Well... what club DO you recommend?" # @t_santibravo120.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "ANY other club is safe... Poetry Club is my dark place... My secret place." # @t_santibravo121.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Aren't there like... A bunch of other people in the club?" # @t_santibravo122.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_backturned_surprised as antibravo
            t_ch_antibravo "Y-yeah..." # @t_santibravo123.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Maybe you should be in DRAMA club." # @t_santibravo124.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "Huh?" # @t_santibravo125.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_sad as cousin
            t_ch_cousin "Nevermind." # @t_santibravo126.00 self.block='Last'
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_antibravo_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_antibravo_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_abm_backturned_surprised as antibravo:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_sad as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_antibravo_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide antibravo
                # Pass (ActorReset)
                $ scene_picked_once_antibravo = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'bluemax', 'kind': 'Macro'} ''>
    label s_day0p5_bluemax:
        # <Macro Macro {'name': 'bluemax', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_bluemax:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_bluemax}', 'kind': 'IfFalse'} ''>
            label s_day0p5_bluemax_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_bluemax}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_bluemax_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_bluemax_stand_shock as bluemax zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stand_shock as bluemax
                show i_cousin_default_neutral as cousin
                t_ch_max "AHH!" # @t_sbluemax10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Sheesh, this poor kid’s a bundle of nerves!)" # @t_sbluemax11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stand_worried as bluemax
                t_ch_max "Oh, whew." # @t_sbluemax12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "You caught me by surprise." # @t_sbluemax13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Sorry, I didn’t mean to startle you." # @t_sbluemax14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stand_serious as bluemax
                t_ch_max "What made it extra surprising is that you managed to surprise me at all!" # @t_sbluemax15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_shock_serious as bluemax
                t_ch_max "I have the three-hundred and sixty degree spatial awareness of a fighter pilot." # @t_sbluemax16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "So, I’m very difficult to surprise." # @t_sbluemax17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(I dunno, seemed pretty easy to me and I wasn’t even trying!)" # @t_sbluemax18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                extend " Uh, yeah. That’s cool." # @t_sbluemax18.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stand_serious as bluemax
                t_ch_max "Yeah, I think so too!" # @t_sbluemax19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "Oh, I’m Blue Max by the way." # @t_sbluemax110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "I’m [slot_playerName]." # @t_sbluemax111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "What were you working on in detention? Homework?" # @t_sbluemax112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "This? Oh, no." # @t_sbluemax113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "I never do homework, that’s how I ended up in there!" # @t_sbluemax114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "No, that was my secret project I can’t tell you about." # @t_sbluemax115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(But...didn’t he JUST tell me about it…?)" # @t_sbluemax116.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "It’s for the Military History Club. If I finish it, that’ll show some school spirit and get me out of detention a little faster." # @t_sbluemax117.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Couldn’t you have done your homework instead of the secret project? And then not gotten INTO detention in the first place?" # @t_sbluemax118.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "…" # @t_sbluemax119.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "…………." # @t_sbluemax120.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stop_serious as bluemax
                t_ch_max "But then I wouldn’t be working on the secret project!" # @t_sbluemax121.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Ah, yes. How silly of me." # @t_sbluemax122.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "It really was!" # @t_sbluemax123.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stand_serious as bluemax
                t_ch_max "But that’s okay, you seem nice." # @t_sbluemax124.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "You should join my club! It’ll get you out of detention faster and you can help out with the project." # @t_sbluemax125.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_shock_serious as bluemax
                t_ch_max "We meet at NOON HUNDRED HOURS!" # @t_sbluemax126.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "...I don’t think that’s how time works?" # @t_sbluemax127.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "Haha! You just don’t know your military lingo like I do." # @t_sbluemax128.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stand_serious as bluemax
                show i_cousin_default_neutral as cousin
                t_ch_max "That’s noon o’clock for you civilians." # @t_sbluemax129.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(That’s not quite right either, but I get the idea.)" # @t_sbluemax130.00 self.block='Last'
                menu:
                    "Join Max's club":
                        $ slot_picked_bluemax_day1 = True
                    "Max is too nerdy for me!":
                        $ slot_picked_bluemax_day1 = False
        if scene_picked_once_bluemax:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_bluemax}', 'kind': 'IfTrue'} ''>
            label s_day0p5_bluemax_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_bluemax}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_bluemax_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_bluemax_stand_serious as bluemax zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stand_serious as bluemax
                show i_cousin_default_neutral as cousin
                t_ch_max "H-hey, [slot_playerName]." # @t_sbluemax133.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "There’s still room in the Military History Club. If, y’know. You wanna join." # @t_sbluemax134.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_max "But it’s okay if you don’t." # @t_sbluemax135.00 self.block='Last'
                menu:
                    "Join Max's club":
                        $ slot_picked_bluemax_day1 = True
                    "Max is too nerdy for me!":
                        $ slot_picked_bluemax_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_bluemax_day1}', 'name': '_2', 'path': 'bluemax/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_bluemax_day1:
            jump s_day0p5_bluemax_Chosen
        # <BranchMacro BranchMacro {'comparison': '!!${scene:picked_once_bluemax}', 'name': '_3', 'path': 'bluemax/PassedLoop', 'kind': 'BranchMacro'} ''>
        if not not scene_picked_once_bluemax:
            jump s_day0p5_bluemax_PassedLoop
        jump s_day0p5_bluemax_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_bluemax_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_serious as bluemax
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Max looks like he could use a friend. And he’s kinda cute. In a nerdy way. And his project might be fun too!)" # @t_sbluemax131.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Yeah, let’s do it." # @t_sbluemax131.01 self.block='Last'
            $ slot_pick_count_bluemax += 1
            # <NHSceneChange NHSceneChange {'name': '_3', 'scene': 's_bluemax1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_bluemax_Chosen__3:
                # <NHSceneChange NHSceneChange {'name': '_3', 'scene': 's_bluemax1', 'kind': 'NHSceneChange'} ''>
                jump s_bluemax1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_bluemax_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_serious as bluemax
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Ehhh, Military History? Sounds like a lot reading. Why don’t I just sign up for extra classes? It’s cool that he likes that stuff, but no thanks!)" # @t_sbluemax132.00 self.block='Last'
            jump s_day0p5_bluemax_cleanup
        # <Macro Macro {'name': 'PassedLoop', 'kind': 'Macro'} ''>
        label s_day0p5_bluemax_PassedLoop:
            # <Macro Macro {'name': 'PassedLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_serious as bluemax
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Hm, I don’t think so, Max." # @t_sbluemax137.00 self.block='Last'
            jump s_day0p5_bluemax_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_bluemax_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_bluemax_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stand_serious as bluemax:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_bluemax_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide bluemax
                # Pass (ActorReset)
                $ scene_picked_once_bluemax = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'cousin', 'kind': 'Macro'} ''>
    label s_day0p5_cousin:
        # <Macro Macro {'name': 'cousin', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        menu:
            "Yeah, I’m not interested in any of these.":
                $ scene_doneExplore = True
            "Wait, I wanted to look around some more…":
                $ scene_doneExplore = False
        if scene_doneExplore:
            # <IfTrue IfTrue {'name': 'bail', 'value': '${scene:doneExplore}', 'kind': 'IfTrue'} ''>
            label s_day0p5_cousin_bail:
                # <IfTrue IfTrue {'name': 'bail', 'value': '${scene:doneExplore}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_cousin_bail_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(None of these clubs seem interesting…)" # @t_scousin12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " (And I don’t want to pretend to be friends with someone just to get out of detention.)" # @t_scousin12.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(I shouldn’t be trying to avoid my punishment...)" # @t_scousin13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(I did something wrong, and I should accept the consequences. This is what reform is all about!)" # @t_scousin14.00 self.block='Last'
                $ slot_pick_count_cousin += 1
                $ slot_picked_cousin_day1 = True
                # <NHSceneChange NHSceneChange {'name': '_7', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
                label s_day0p5_cousin_bail__7:
                    # <NHSceneChange NHSceneChange {'name': '_7', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
                    jump s_day2
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_cousin_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_cousin_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                # Pass (ActorReset)
                $ scene_picked_once_cousin = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'davesprite', 'kind': 'Macro'} ''>
    label s_day0p5_davesprite:
        # <Macro Macro {'name': 'davesprite', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_davesprite:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_davesprite}', 'kind': 'IfFalse'} ''>
            label s_day0p5_davesprite_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_davesprite}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_davesprite_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_davesprite_standing_disinterest as davesprite zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(There’s that boy again…" # @t_sdavesprite10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Davesprite." # @t_sdavesprite10.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "He said he was a “game guide”, whatever that means." # @t_sdavesprite11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " He seems kind of crazy, actually…" # @t_sdavesprite11.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "But there’s also something compelling about him…" # @t_sdavesprite12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral_blush as cousin
                with Dissolve(0.5)
                extend " He’s like… an angel. I’ve got to find out more …." # @t_sdavesprite12.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "(hey [slot_playerName] check it out" # @t_sdavesprite13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "i can put parentheses around my text and narrate my inner thoughts too" # @t_sdavesprite14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_eyebrow as davesprite
                t_ch_davesprite "also no way im an angel because angels arent sexy" # @t_sdavesprite15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "youd think naked people with wings=instant hotness but nah" # @t_sdavesprite16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_eyebrow as davesprite
                t_ch_davesprite "they hella judge you if you want to get freaky so its like a psychological turnoff" # @t_sdavesprite17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "obviously)" # @t_sdavesprite18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Davesprite…" # @t_sdavesprite19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You’re just floating there, staring at me…" # @t_sdavesprite19.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Say something! You’re freaking me out." # @t_sdavesprite110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "(whoah you actually cant hear me when im doin parentheses?" # @t_sdavesprite111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_defeated_disinterest as davesprite
                t_ch_davesprite "this is just thoughts?" # @t_sdavesprite112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "messed up)" # @t_sdavesprite113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "uh hey sorry about that" # @t_sdavesprite114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "do you want to hang out with me today" # @t_sdavesprite115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "its cool if not you can click on whoever you want i seriously dont care" # @t_sdavesprite116.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Well, I’m looking for a club to join. What club are you in?" # @t_sdavesprite117.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "uh lets see" # @t_sdavesprite118.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "it doesnt really matter anyway but" # @t_sdavesprite119.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "i guess im in the webcomics club or something" # @t_sdavesprite120.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "yeah that sounds awesome" # @t_sdavesprite121.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "you take dorky comic books and you take the internet" # @t_sdavesprite122.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "known hive of nerds" # @t_sdavesprite123.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "and combine them" # @t_sdavesprite124.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "and its so lame it crosses back over into ironic coolness" # @t_sdavesprite125.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "which is pretty  much ultimate coolness right there" # @t_sdavesprite126.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "there is literally no way to top that" # @t_sdavesprite127.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "…" # @t_sdavesprite128.00 self.block='Last'
                menu:
                    "Join Davesprite in the Webcomics Club?"

                    "Yes":
                        $ slot_picked_davesprite_day1 = True
                    "No":
                        $ slot_picked_davesprite_day1 = False
        if scene_picked_once_davesprite:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_davesprite}', 'kind': 'IfTrue'} ''>
            label s_day0p5_davesprite_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_davesprite}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_davesprite_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_davesprite_shrug_eyebrow as davesprite zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_eyebrow as davesprite
                show i_cousin_default_neutral as cousin
                t_ch_davesprite "yeah are we doin this or not" # @t_sdavesprite129.00 self.block='Last'
                menu:
                    "Join Davesprite in the Webcomics Club?"

                    "Yes":
                        $ slot_picked_davesprite_day1 = True
                    "No":
                        $ slot_picked_davesprite_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_davesprite_day1}', 'name': '_2', 'path': 'davesprite/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_davesprite_day1:
            jump s_day0p5_davesprite_Chosen
        jump s_day0p5_davesprite_cleanup
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_davesprite_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_shrug_eyebrow as davesprite
            show i_cousin_default_neutral as cousin
            t_ch_davesprite "ok cool let’s go hang out in the club room or something" # @t_sdavesprite130.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_shrug_eyebrow as davesprite
            show i_cousin_default_neutral as cousin
            t_ch_cousin "That sounds pretty cool." # @t_sdavesprite131.00 self.block='Last'
            $ slot_pick_count_davesprite += 1
            # <NHSceneChange NHSceneChange {'name': '_3', 'scene': 's_davesprite1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_davesprite_Chosen__3:
                # <NHSceneChange NHSceneChange {'name': '_3', 'scene': 's_davesprite1', 'kind': 'NHSceneChange'} ''>
                jump s_davesprite1
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_davesprite_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_davesprite_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_eyebrow as davesprite:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_davesprite_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide davesprite
                # Pass (ActorReset)
                $ scene_picked_once_davesprite = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'donko', 'kind': 'Macro'} ''>
    label s_day0p5_donko:
        # <Macro Macro {'name': 'donko', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_donko:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_donko}', 'kind': 'IfFalse'} ''>
            label s_day0p5_donko_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_donko}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_donko_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_donko_default_grin as donko zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_grin as donko
                t_ch_donko "Hi, honey!" # @t_sdonko10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Don’t think that just because you’re the new kid, I’m gonna go easy on you!" # @t_sdonko10.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_wink as donko
                t_ch_donko "Tee-hee! Just kidding!" # @t_sdonko11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I’m totally harmless… Unless you’re some cute shoes on sale." # @t_sdonko11.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "So… I guess you’re probably in the fashion club or something, huh?" # @t_sdonko12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_ygg_grin as donko
                t_ch_donko "U-um…" # @t_sdonko13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "I guess I have to join a club, so I can have less detention…" # @t_sdonko14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_sad as cousin
                extend " I’m desperate to get away from that scary King guy." # @t_sdonko14.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "Like, are you joking?!" # @t_sdonko15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_wink as donko
                t_ch_donko "King is TOTALLY FABULOUS!" # @t_sdonko16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Leopard spots are making a comeback this year!" # @t_sdonko16.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Haha…" # @t_sdonko17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I obviously don’t know much about fashion." # @t_sdonko17.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " Maybe a fashion club wouldn’t be a great choice for me." # @t_sdonko17.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Kind of a bummer, then…" # @t_sdonko18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I thought it might be fun to be in a club with you!" # @t_sdonko18.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_grin as donko
                t_ch_donko "...You can still be in a club with me…" # @t_sdonko19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I’m not in Fashion Club… I’m in…" # @t_sdonko19.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_meloncholic as donko
                t_ch_donko "*indistinct mumbling*" # @t_sdonko110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "What was that? I didn’t catch that…" # @t_sdonko111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_ygg_meloncholic as donko
                t_ch_donko "OMG! I’m in Band, okay?!" # @t_sdonko112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Band… Drum…" # @t_sdonko113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " I should’ve known…)" # @t_sdonko113.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "I know it’s a really dorky club to be in…" # @t_sdonko114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_meloncholic_blush as donko
                t_ch_donko "Don’t join up with me! It’s too embarrassing!" # @t_sdonko115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Lucky for me…" # @t_sdonko116.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral_blush as cousin
                t_ch_cousin "Donko is even cuter when embarrassed.)" # @t_sdonko117.00 self.block='Last'
                menu:
                    "Join Donko in the school band club?"

                    "Yes!":
                        $ slot_picked_donko_day1 = True
                    "I need some time!":
                        $ slot_picked_donko_day1 = False
        if scene_picked_once_donko:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_donko}', 'kind': 'IfTrue'} ''>
            label s_day0p5_donko_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_donko}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_donko_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_donko_default_grin as donko zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_grin as donko
                t_ch_donko "Have you made up your mind yet?" # @t_sdonko118.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_meloncholic_blush as donko
                t_ch_donko "Like, for real, you shouldn’t join Band Club with me…" # @t_sdonko119.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I’d seriously be soooo embarrassed!" # @t_sdonko119.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_meloncholic_blush as donko
                t_ch_cousin "(Why is Donko even in Band if it’s so “embarrassing”?" # @t_sdonko120.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_donko_default_meloncholic_blush as donko
                t_ch_cousin "I guess there’s only one way to find out…)" # @t_sdonko121.00 self.block='Last'
                menu:
                    "Join Donko in the school band club?"

                    "Yes!":
                        $ slot_picked_donko_day1 = True
                    "I need some time!":
                        $ slot_picked_donko_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_donko_day1}', 'name': '_2', 'path': 'donko/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_donko_day1:
            jump s_day0p5_donko_Chosen
        jump s_day0p5_donko_cleanup
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_donko_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            $ slot_pick_count_donko += 1
            # <NHSceneChange NHSceneChange {'name': '_1', 'scene': 's_donko1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_donko_Chosen__1:
                # <NHSceneChange NHSceneChange {'name': '_1', 'scene': 's_donko1', 'kind': 'NHSceneChange'} ''>
                jump s_donko1
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_donko_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_donko_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_meloncholic_blush as donko:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_donko_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide donko
                # Pass (ActorReset)
                $ scene_picked_once_donko = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'galaga', 'kind': 'Macro'} ''>
    label s_day0p5_galaga:
        # <Macro Macro {'name': 'galaga', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_galaga:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_galaga}', 'kind': 'IfFalse'} ''>
            label s_day0p5_galaga_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_galaga}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_galaga_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
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
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_galaga_default as galaga
                show i_cousin_default_neutral_blush as cousin
                t_ch_cousin "(Gosh, there’s Galaga Ship at the Drama Club booth.)" # @t_sgalaga10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Wonder if it meant what it said about me auditioning for the play!)" # @t_sgalaga11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Heck. Wonder if I could even remember my lines?)" # @t_sgalaga12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Um." # @t_sgalaga12.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "H-hey, Galaga Ship." # @t_sgalaga13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin_blush as cousin
                t_ch_cousin "I was just, y’know. For detention." # @t_sgalaga14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Heh. We gotta. Y’know. Join a club or something or whatever." # @t_sgalaga15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_galaga "{smallcaps}…{/smallcaps}" # @t_sgalaga16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_grin_blush as cousin
                t_ch_cousin "Um. Yeah." # @t_sgalaga17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Heh." # @t_sgalaga18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_neutral_blush as cousin
                t_ch_cousin "And I thought. Maybe, y’know?" # @t_sgalaga19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_neutral_blush as cousin
                t_ch_cousin "With the Shakespeare." # @t_sgalaga110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Like you said." # @t_sgalaga111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_mortified_blush as cousin
                extend " ([slot_playerName], you’re not even talking in complete sentences anymore!)" # @t_sgalaga111.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " Um. And stuff." # @t_sgalaga111.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Ahem." # @t_sgalaga112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_galaga "{smallcaps}…{/smallcaps}" # @t_sgalaga113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "(Oh, MAN. I am bombing big time.)" # @t_sgalaga114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(I should just walk away while Galaga Ship still has no idea what my name is and just thinks of me as that little weirdo it hates forever.)" # @t_sgalaga115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_galaga "{smallcaps}Oh. New kid?{/smallcaps}" # @t_sgalaga116.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_surprised as cousin
                t_ch_cousin "(?!)" # @t_sgalaga117.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_galaga "{smallcaps}Sorry, I’m supposed to be manning the booth or whatever.{/smallcaps}" # @t_sgalaga118.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_galaga "{smallcaps}But I was listening to space radio on my internal speakers.{/smallcaps}" # @t_sgalaga119.00 self.block='Last'
                menu:
                    "JOIN THE DRAMA CLUB!":
                        $ slot_picked_galaga_day1 = True
                    "RUN ABORT GIVE UP!":
                        $ slot_picked_galaga_day1 = False
        if scene_picked_once_galaga:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_galaga}', 'kind': 'IfTrue'} ''>
            label s_day0p5_galaga_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_galaga}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_galaga_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
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
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Um. Y’know. I gotta join a club and all, so…" # @t_sgalaga126.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_galaga "{smallcaps}Well, we hold auditions in the auditorium. Good luck, I guess.{/smallcaps}" # @t_sgalaga127.00 self.block='Last'
                menu:
                    "GO FOR IT STUPID":
                        $ slot_picked_galaga_day1 = True
                    "WAIT WHO AM I WHAT’S MY NAME AAAAAAH":
                        $ slot_picked_galaga_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_galaga_day1}', 'name': '_2', 'path': 'galaga/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_galaga_day1:
            jump s_day0p5_galaga_Chosen
        # <BranchMacro BranchMacro {'comparison': '!!${scene:picked_once_galaga}', 'name': '_3', 'path': 'galaga/PassedLoop', 'kind': 'BranchMacro'} ''>
        if not not scene_picked_once_galaga:
            jump s_day0p5_galaga_PassedLoop
        jump s_day0p5_galaga_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_galaga_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "I THOUGHT MAYBE DRAMA THE CLUB TO JOIN IT." # @t_sgalaga120.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " (What did I just say?!?!)" # @t_sgalaga120.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            extend " Um. Y’know. I gotta join a club and all, so…" # @t_sgalaga120.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}Hm? Oh, right. Detention.{/smallcaps}" # @t_sgalaga121.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}Yeah.{/smallcaps}" # @t_sgalaga122.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}Well, we hold auditions in the auditorium. Good luck.{/smallcaps}" # @t_sgalaga123.00 self.block='Last'
            $ slot_pick_count_galaga += 1
            # <NHSceneChange NHSceneChange {'name': '_7', 'scene': 's_galaga1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_galaga_Chosen__7:
                # <NHSceneChange NHSceneChange {'name': '_7', 'scene': 's_galaga1', 'kind': 'NHSceneChange'} ''>
                jump s_galaga1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_galaga_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I uh um." # @t_sgalaga124.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "THANK YOU GOODBYE THOUGH!" # @t_sgalaga125.00 self.block='Last'
            jump s_day0p5_galaga_cleanup
        # <Macro Macro {'name': 'PassedLoop', 'kind': 'Macro'} ''>
        label s_day0p5_galaga_PassedLoop:
            # <Macro Macro {'name': 'PassedLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I uh um." # @t_sgalaga124.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "THANK YOU GOODBYE THOUGH!" # @t_sgalaga125.00 self.block='Last'
            jump s_day0p5_galaga_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_galaga_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_galaga_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_galaga_default as galaga:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_surprised as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_galaga_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide galaga
                # Pass (ActorReset)
                $ scene_picked_once_galaga = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'hiromi', 'kind': 'Macro'} ''>
    label s_day0p5_hiromi:
        # <Macro Macro {'name': 'hiromi', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_hiromi:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_hiromi}', 'kind': 'IfFalse'} ''>
            label s_day0p5_hiromi_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_hiromi}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_hiromi_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
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
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_hiromi_stand_serious as hiromi
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Hey Hiromi!" # @t_shiromi10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_hiromi "Hey kid." # @t_shiromi11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "What club are you in again?" # @t_shiromi12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_hiromi "Auto Club." # @t_shiromi13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_neutral as cousin
                t_ch_cousin "Cool." # @t_shiromi14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_hiromi_akimbo_serious as hiromi
                t_ch_hiromi "Coming?" # @t_shiromi15.00 self.block='Last'
                menu:
                    "Join the Auto Club?"

                    "Yeah!":
                        $ slot_picked_hiromi_day1 = True
                    "Maybe next time...":
                        $ slot_picked_hiromi_day1 = False
        if scene_picked_once_hiromi:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_hiromi}', 'kind': 'IfTrue'} ''>
            label s_day0p5_hiromi_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_hiromi}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_hiromi_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
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
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_hiromi "……………………………..coming?" # @t_shiromi111.00a self.block='Last'
                menu:
                    "Join the Auto Club?"

                    "Yeah!":
                        $ slot_picked_hiromi_day1 = True
                    "Maybe next time...":
                        $ slot_picked_hiromi_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_hiromi_day1}', 'name': '_2', 'path': 'hiromi/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_hiromi_day1:
            jump s_day0p5_hiromi_Chosen
        jump s_day0p5_hiromi_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_hiromi_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "!!! Yeah!" # @t_shiromi16.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(She actually addressed me! I'm a little shocked.)" # @t_shiromi17.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Oh... She's leaving! Better follow her.)" # @t_shiromi18.00 self.block='Last'
            $ slot_pick_count_hiromi += 1
            # <NHSceneChange NHSceneChange {'name': '_4', 'scene': 's_hiromi1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_hiromi_Chosen__4:
                # <NHSceneChange NHSceneChange {'name': '_4', 'scene': 's_hiromi1', 'kind': 'NHSceneChange'} ''>
                jump s_hiromi1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_hiromi_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Maybe next time..." # @t_shiromi19.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_hiromi "Okay." # @t_shiromi110.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_sad as cousin
            t_ch_cousin "(I wish she was a little more enthusiastic... But it's kind of nice to not feel any pressure from a person either.)" # @t_shiromi111.00 self.block='Last'
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_hiromi_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_hiromi_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_hiromi_stand_serious as hiromi:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_sad as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_hiromi_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide hiromi
                # Pass (ActorReset)
                $ scene_picked_once_hiromi = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'jane', 'kind': 'Macro'} ''>
    label s_day0p5_jane:
        # <Macro Macro {'name': 'jane', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_jane:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_jane}', 'kind': 'IfFalse'} ''>
            label s_day0p5_jane_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_jane}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_jane_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_jane_default_grin_mustache as jane zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_jane_default_grin_mustache as jane
                t_ch_jane "Hello there, person-I-have-never-met-before!" # @t_sjane10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_jane "You seem like the type to be looking for a club to join." # @t_sjane11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "(Oh, it’s just Jane… wearing a novelty mustache?!" # @t_sjane12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Does she really think that would fool me? She otherwise looks exactly the same." # @t_sjane12.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Heh, that’s pretty cute. I’ll play along.)" # @t_sjane13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Oh yes, hello, dapper young mustached gentleman. I am looking for a club, in fact!" # @t_sjane14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_jane "Hoo hoo hoo! Surprise! It was me, Jane, all along!" # @t_sjane15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_laugh as jane
                t_ch_jane "SEE?!" # @t_sjane16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Oh my gosh! Jane, that was YOU?!" # @t_sjane17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_grin as jane
                t_ch_jane "You know, [slot_playerName], you need to work on your observational skills." # @t_sjane18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_jane "That silly old disguise should have been quite easy to see through!" # @t_sjane19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "You don’t say." # @t_sjane110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_jane "Perhaps you should consider joining MY club! :B" # @t_sjane111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I happen to be the editor of the Namco High school newspaper." # @t_sjane111.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_jane "What do you say? I could always use a new mudraker!" # @t_sjane112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Raking mud sounds REALLY difficult!" # @t_sjane113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "But maybe I should join. She seemed so skeptical before, but if she’s reporting on events around the school…" # @t_sjane114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " She’s BOUND to see that weird stuff goes on here!)" # @t_sjane114.01 self.block='Last'
                menu:
                    "Join Jane Crocker at the school paper?"

                    "Yes!":
                        $ slot_picked_jane_day1 = True
                    "Let's look at other clubs first.":
                        $ slot_picked_jane_day1 = False
        if scene_picked_once_jane:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_jane}', 'kind': 'IfTrue'} ''>
            label s_day0p5_jane_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_jane}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_jane_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
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
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_jane_armscrossed_grin as jane
                t_ch_jane "What’s the word, [slot_playerName]? We haven’t got all day!" # @t_sjane115.00 self.block='Last'
                menu:
                    "Join Jane Crocker at the school paper?"

                    "Yes!":
                        $ slot_picked_jane_day1 = True
                    "Let's look at other clubs first.":
                        $ slot_picked_jane_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_jane_day1}', 'name': '_2', 'path': 'jane/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_jane_day1:
            jump s_day0p5_jane_Chosen
        jump s_day0p5_jane_cleanup
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_jane_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_jane_armscrossed_laugh as jane
            t_ch_jane "Hooray! Let’s get started!" # @t_sjane116.00 self.block='Last'
            $ slot_pick_count_jane += 1
            # <NHSceneChange NHSceneChange {'name': '_2', 'scene': 's_jane1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_jane_Chosen__2:
                # <NHSceneChange NHSceneChange {'name': '_2', 'scene': 's_jane1', 'kind': 'NHSceneChange'} ''>
                jump s_jane1
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_jane_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_jane_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_laugh as jane:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_jane_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide jane
                # Pass (ActorReset)
                $ scene_picked_once_jane = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'lolo', 'kind': 'Macro'} ''>
    label s_day0p5_lolo:
        # <Macro Macro {'name': 'lolo', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_lolo:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_lolo}', 'kind': 'IfFalse'} ''>
            label s_day0p5_lolo_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_lolo}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_lolo_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_lolo_crossed_grin as lolo zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_grin as lolo
                show i_cousin_default_neutral as cousin
                t_ch_lolo "Hey, [slot_playerName]." # @t_slolo030.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Oh, so you’re deigning to talk to me now?!" # @t_slolo031.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_raisedbrow as lolo
                t_ch_lolo "Seriously? You’re gonna hold a grudge because I was moody earlier?" # @t_slolo032.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_lolo "Is that really worth the effort?" # @t_slolo033.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_sad as cousin
                t_ch_cousin "Okay...I guess I was being a little sensitive..." # @t_slolo034.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(She still seems moody, though?)" # @t_slolo035.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_lolo "So what school club were you thinking of joining?" # @t_slolo036.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_frustrated as lolo
                extend " Not that it really matters." # @t_slolo036.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Uhh... well, I’m not crazy about the idea of joining a club at all." # @t_slolo037.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " But I guess it’s better than staying in detention all the time." # @t_slolo037.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "So I guess maybe..." # @t_slolo038.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Yearbook club?" # @t_slolo038.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "It seems kinda like a cushy club, anyway." # @t_slolo039.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I can probably relax and not stress too much about it." # @t_slolo039.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_grin as lolo
                t_ch_lolo "… Heh." # @t_slolo040.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "What?" # @t_slolo041.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " What’s up?" # @t_slolo041.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_lolo "That’s... actually the club I’m in." # @t_slolo042.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "O-Oh!" # @t_slolo043.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                extend " I’m sorry!" # @t_slolo043.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I didn’t mean to suggest it was a less-serious club..." # @t_slolo043.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_shrug_grin as lolo
                t_ch_lolo "Oh relax, cupcake." # @t_slolo044.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I joined it for the exact same reason you just said." # @t_slolo044.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You’re right, by the way. It’s a total cakewalk." # @t_slolo044.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_grin as cousin
                t_ch_cousin "Haha... well, great minds think alike I guess!" # @t_slolo045.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_raisedbrow as lolo
                t_ch_lolo "..." # @t_slolo046.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Don’t push it." # @t_slolo046.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Heh... heh...." # @t_slolo047.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                extend " …..ehhh." # @t_slolo047.01 self.block='Last'
                menu:
                    "Join Lolo in the Yearbook Club?"

                    "Sure!":
                        $ slot_picked_lolo_day1 = True
                    "I need some time to think about it...":
                        $ slot_picked_lolo_day1 = False
        if scene_picked_once_lolo:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_lolo}', 'kind': 'IfTrue'} ''>
            label s_day0p5_lolo_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_lolo}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_lolo_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_lolo_crossed_grin as lolo zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_raisedbrow as lolo
                show i_cousin_default_neutral as cousin
                t_ch_lolo "Made up your mind yet?" # @t_slolo049.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_frustrated as lolo
                extend " Not that I care..." # @t_slolo049.01 self.block='Last'
                menu:
                    "Join Lolo in the Yearbook Club?"

                    "Sure!":
                        $ slot_picked_lolo_day1 = True
                    "I need some time to think about it...":
                        $ slot_picked_lolo_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_lolo_day1}', 'name': '_2', 'path': 'lolo/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_lolo_day1:
            jump s_day0p5_lolo_Chosen
        jump s_day0p5_lolo_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_lolo_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            $ slot_pick_count_lolo += 1
            # <NHSceneChange NHSceneChange {'name': '_1', 'scene': 's_lolo1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_lolo_Chosen__1:
                # <NHSceneChange NHSceneChange {'name': '_1', 'scene': 's_lolo1', 'kind': 'NHSceneChange'} ''>
                jump s_lolo1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_lolo_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_raisedbrow as lolo
            show i_cousin_default_neutral as cousin
            t_ch_lolo "…. Whatever." # @t_slolo048.00 self.block='Last'
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_lolo_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_lolo_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_raisedbrow as lolo:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_lolo_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide lolo
                # Pass (ActorReset)
                $ scene_picked_once_lolo = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'meowkie', 'kind': 'Macro'} ''>
    label s_day0p5_meowkie:
        # <Macro Macro {'name': 'meowkie', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_meowkie:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_meowkie}', 'kind': 'IfFalse'} ''>
            label s_day0p5_meowkie_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_meowkie}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_meowkie_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_meowkie_akimbo_normal_badge as meowkie zorder 2:
                        default
                        xpos 0.7 
                        xzoom -1.0 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_normal_badge as meowkie
                show i_cousin_default_neutral as cousin
                t_ch_meowkie "Oh, hiya Boss!" # @t_smeowkie10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Nice to see ya out and about!" # @t_smeowkie10.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_meowkie "Have you decided on a club yet? Our school has lotsa good ones!" # @t_smeowkie11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "I haven’t picked one yet, no…" # @t_smeowkie12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "I remember you saying you’re a Hall Monitor though, right?" # @t_smeowkie13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I guess that counts as a club too?" # @t_smeowkie13.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_forcedsmile_badge as meowkie
                t_ch_meowkie "Aw Boss, that’s sweet…" # @t_smeowkie14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_meowkie "You don’t gotta pretend to be interested in my club, though!" # @t_smeowkie15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I know it’s not as exciting as some of the other ones we got..." # @t_smeowkie15.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "I’m not pretending to be interested, really!" # @t_smeowkie16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                extend " I wanna hear about being a Hall Monitor. Please tell me!" # @t_smeowkie16.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_alert_badge as meowkie
                t_ch_meowkie "Nyaa… Well, actually…" # @t_smeowkie17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I gotta lot of thoughts about it. Mostly that..." # @t_smeowkie17.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_normal_badge as meowkie
                t_ch_meowkie "Bein’ a Hall Monitor is really, really great!" # @t_smeowkie18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " It counts as a club, so it keeps ya outta detention..." # @t_smeowkie18.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_meowkie "But you also get to help keep the other kids outta detention too!" # @t_smeowkie19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_grin as meowkie
                extend " You help everybody, not just yourself!" # @t_smeowkie19.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_laugh as cousin
                t_ch_cousin "You know, Meowkie, that’s really noble of you." # @t_smeowkie110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie
                t_ch_meowkie "R-really, Boss?" # @t_smeowkie111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Yeah! You’re making me want to be a Hall Monitor too." # @t_smeowkie112.00 self.block='Last'
                menu:
                    "Join Meowkie as a Hall Monitor":
                        $ slot_picked_meowkie_day1 = True
                    "Think it over":
                        $ slot_picked_meowkie_day1 = False
        if scene_picked_once_meowkie:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_meowkie}', 'kind': 'IfTrue'} ''>
            label s_day0p5_meowkie_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_meowkie}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_meowkie_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_meowkie_akimbo_normal_badge as meowkie zorder 2:
                        default
                        xpos 0.7 
                        xzoom -1.0 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie
                show i_cousin_default_neutral as cousin
                t_ch_meowkie "S-so, whaddya say, Boss?" # @t_smeowkie115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You didn’t really wanna be a Hall Monitor with me…" # @t_smeowkie115.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_forcedsmile_badge as meowkie
                t_ch_meowkie "Or did you?" # @t_smeowkie116.00 self.block='Last'
                menu:
                    "Join Meowkie as a Hall Monitor":
                        $ slot_picked_meowkie_day1 = True
                    "Think it over":
                        $ slot_picked_meowkie_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_meowkie_day1}', 'name': '_2', 'path': 'meowkie/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_meowkie_day1:
            jump s_day0p5_meowkie_Chosen
        jump s_day0p5_meowkie_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_meowkie_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_normal_badge as meowkie
            show i_cousin_default_neutral as cousin
            t_ch_meowkie "Nyaa! Wow, really? You want to be a hall monitor with..." # @t_smeowkie117.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_forcedsmile_badge as meowkie
            t_ch_meowkie "with someone like me?" # @t_smeowkie118.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "Boss, I can’t tell ya what this means to me..." # @t_smeowkie119.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_forcedsmile_badge as meowkie
            extend " D-don’t worry! I’ll show ya the ropes!" # @t_smeowkie119.01 self.block='Last'
            $ slot_pick_count_meowkie += 1
            # <NHSceneChange NHSceneChange {'name': '_5', 'scene': 's_meowkie1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_meowkie_Chosen__5:
                # <NHSceneChange NHSceneChange {'name': '_5', 'scene': 's_meowkie1', 'kind': 'NHSceneChange'} ''>
                jump s_meowkie1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_meowkie_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_normal_badge as meowkie
            show i_cousin_default_neutral as cousin
            t_ch_meowkie "Don’t worry, Boss! Take all the time ya need to think it over." # @t_smeowkie113.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I’ll be here if ya change your mind..." # @t_smeowkie113.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_forcedsmile_badge as meowkie
            t_ch_meowkie "B-but, don’t worry!" # @t_smeowkie114.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I’ll understand if ya want to pick some other club!" # @t_smeowkie114.01 self.block='Last'
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_meowkie_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_meowkie_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_meowkie_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide meowkie
                # Pass (ActorReset)
                $ scene_picked_once_meowkie = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'mrdriller', 'kind': 'Macro'} ''>
    label s_day0p5_mrdriller:
        # <Macro Macro {'name': 'mrdriller', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_mrdriller:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_mrdriller}', 'kind': 'IfFalse'} ''>
            label s_day0p5_mrdriller_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_mrdriller}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_mrdriller_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_mrdriller_slumped_happy as mrdriller zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_handsup_happy as mrdriller
                show i_cousin_default_neutral as cousin
                t_ch_mrdriller "[slot_playerName]! [slot_playerName]! Omigosh!" # @t_smrdriller10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Have you picked a club yet?!" # @t_smrdriller10.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "I’m still deciding." # @t_smrdriller11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I guess… Maybe Art, or something-" # @t_smrdriller11.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_handsup_shock as mrdriller
                t_ch_mrdriller "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!" # @t_smrdriller12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Um?" # @t_smrdriller13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_handsup_cry as mrdriller
                t_ch_mrdriller "I need you!" # @t_smrdriller14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Y-you…" # @t_smrdriller15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised_blush as cousin
                extend " Need me?!" # @t_smrdriller15.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_drillup_excited as mrdriller
                t_ch_mrdriller "Yes! To help found the Digging Club with me!" # @t_smrdriller16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "...Oh." # @t_smrdriller17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_standing_confused as mrdriller
                t_ch_mrdriller "No one else will join with me, and the school rules say it’s not an official club unless at least two people are in it." # @t_smrdriller18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_drillup_happy as mrdriller
                t_ch_mrdriller "I need you to come with me, so we can found the Digging Club together!" # @t_smrdriller19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_standing_smug as mrdriller
                t_ch_mrdriller "If it’s an OFFICIAL SCHOOL CLUB, Dad can’t stop me from participating…" # @t_smrdriller110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_standing_smug as mrdriller
                t_ch_mrdriller "Cuz for school stuff, he has to act like a normal principal would, and not do stuff just because he’s my dad." # @t_smrdriller111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_standing_confused as mrdriller
                extend " So if I can’t found this club, I’ll never be allowed to dig again and then I don’t know" # @t_smrdriller111.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_standing_sad as mrdriller
                extend " what" # @t_smrdriller111.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_slumped_cry as mrdriller
                extend " I’ll do!" # @t_smrdriller111.03 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_drillup_shock as mrdriller
                show i_cousin_default_mortified as cousin
                t_ch_mrdriller "Die, probably! Can you die from not digging enough?!" # @t_smrdriller112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I’m pretty sure you can! I read a thing on the" # @t_smrdriller112.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " thing!" # @t_smrdriller112.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "Ummm…" # @t_smrdriller113.00 self.block='Last'
                menu:
                    "Okay, sure, why not!":
                        $ slot_picked_mrdriller_day1 = True
                    "I need some time to think about it.":
                        $ slot_picked_mrdriller_day1 = False
        if scene_picked_once_mrdriller:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_mrdriller}', 'kind': 'IfTrue'} ''>
            label s_day0p5_mrdriller_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_mrdriller}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_mrdriller_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_mrdriller_slumped_cry as mrdriller zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_slumped_cry as mrdriller
                t_ch_mrdriller "Pleeeaaase help me start a Drilling Club, [slot_playerName]?" # @t_smrdriller114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_mrdriller "Pleeeeaaaase?!?!" # @t_smrdriller115.00 self.block='Last'
                menu:
                    "Okay, sure, why not!":
                        $ slot_picked_mrdriller_day1 = True
                    "I need some time to think about it.":
                        $ slot_picked_mrdriller_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_mrdriller_day1}', 'name': '_2', 'path': 'mrdriller/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_mrdriller_day1:
            jump s_day0p5_mrdriller_Chosen
        jump s_day0p5_mrdriller_cleanup
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_mrdriller_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_drillup_happy as mrdriller
            t_ch_mrdriller "That’s great! Thank you thank you thank you!" # @t_smrdriller116.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "I’ll give you a few minutes to go collect all your digging supplies!" # @t_smrdriller117.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "UM…." # @t_smrdriller118.00 self.block='Last'
            $ slot_pick_count_mrdriller += 1
            # <NHSceneChange NHSceneChange {'name': '_4', 'scene': 's_mrdriller1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_mrdriller_Chosen__4:
                # <NHSceneChange NHSceneChange {'name': '_4', 'scene': 's_mrdriller1', 'kind': 'NHSceneChange'} ''>
                jump s_mrdriller1
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_mrdriller_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_mrdriller_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_drillup_happy as mrdriller:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_mrdriller_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide mrdriller
                # Pass (ActorReset)
                $ scene_picked_once_mrdriller = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'nidia', 'kind': 'Macro'} ''>
    label s_day0p5_nidia:
        # <Macro Macro {'name': 'nidia', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_nidia:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_nidia}', 'kind': 'IfFalse'} ''>
            label s_day0p5_nidia_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_nidia}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_nidia_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_nidia_clasped_surprised as nidia zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_clasped_surprised as nidia
                show i_cousin_default_neutral as cousin
                t_ch_nidia "It's you! If we're talking again, then that rules out all of these possibilities..." # @t_snidia10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_notepad_surprised as nidia
                t_ch_nidia "In fact, some of these side quests are definitely out of the question now." # @t_snidia11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_nidia "All of the endings involving dark forces of various types are still open, though." # @t_snidia12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(She's... crossing out a whole bunch of things written in her notebook there.)" # @t_snidia13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_nidia "......................" # @t_snidia14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(I should introduce myself...)" # @t_snidia15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "My name is [slot_playerName]. I'm a roller." # @t_snidia16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_akimbo_surprised as nidia
                t_ch_nidia "A what? Is that a job class?" # @t_snidia17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Huh? No, I'm, uh, an..." # @t_snidia18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " aspiring collector of cultural detritus." # @t_snidia18.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " Nice to meet you... Nidia, was it?" # @t_snidia18.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_clasped_surprised as nidia
                t_ch_nidia "!!!" # @t_snidia19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " How'd you know my name?!" # @t_snidia19.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Can you see... it?!" # @t_snidia19.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_nidia "Do you know if I ... I ..." # @t_snidia110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_nidia "You can really see it?! The FUTURE?!" # @t_snidia111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "N-no, not at all ... Mr. King and Principal Dig Dug called your name during roll. I have a completely average memory..." # @t_snidia112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " So I happened to remember." # @t_snidia112.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_notepad_surprised as nidia
                t_ch_nidia "Average INT, huh?" # @t_snidia113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Huh?" # @t_snidia114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(Wait... Is she calling me stupid?!)" # @t_snidia115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_nidia "Speaking of which... King has unusually high INT for a Barbarian class." # @t_snidia116.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_notepad_worried as nidia
                t_ch_nidia "My memory's not so good... Maybe my INT is too low? I probably should have spent more time grinding." # @t_snidia117.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "... Grinding?!" # @t_snidia118.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_nidia "Yeah, like dungeons and stuff." # @t_snidia119.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_nidia "I think my memory's bad because I keep trying to remember FORWARD." # @t_snidia120.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Professor Tomari keeps telling me I can't do that, but I dunno... Seems possible." # @t_snidia120.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_akimbo_surprised as nidia
                t_ch_nidia "And his INT is really high. I try to make a point of listening to him." # @t_snidia121.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(This Tomari sounds like a reasonable person ... )" # @t_snidia122.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_nidia "I wanted to ask him more, but he went back to designing something called a 'super battlebot'." # @t_snidia123.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "(OKAY SCRATCH REASONABLE)" # @t_snidia124.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "What were you just asking me, anyway? Do I know if you... what?" # @t_snidia125.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_clasped_surprised as nidia
                t_ch_nidia "It's nothing! I'm Nidia! It's my destiny to save the world!" # @t_snidia126.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_clasped_happy as nidia
                t_ch_nidia "Come with me to the library if you want to join magic club!" # @t_snidia127.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Her introduction... Was a little more impressive than mine... )" # @t_snidia128.00 self.block='Last'
                menu:
                    "Join the Magic Club?"

                    "I don't really get what you're saying, but magic sounds cool!":
                        $ slot_picked_nidia_day1 = True
                    "I'm not really the world-saving type...sorry.":
                        $ slot_picked_nidia_day1 = False
        if scene_picked_once_nidia:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_nidia}', 'kind': 'IfTrue'} ''>
            label s_day0p5_nidia_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_nidia}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_nidia_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_nidia_clasped_surprised as nidia zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_nidia_clasped_surprised as nidia
                t_ch_nidia "I hope you’ll join the magic club!" # @t_snidia134.00a self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_nidia_clasped_surprised as nidia
                t_ch_cousin "(Maybe she’ll tell me what she means when she says it’s her destiny to save the world… )" # @t_snidia134.00b self.block='Last'
                menu:
                    "Join the Magic Club?"

                    "I don't really get what you're saying, but magic sounds cool!":
                        $ slot_picked_nidia_day1 = True
                    "I'm not really the world-saving type...sorry.":
                        $ slot_picked_nidia_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_nidia_day1}', 'name': '_2', 'path': 'nidia/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_nidia_day1:
            jump s_day0p5_nidia_Chosen
        jump s_day0p5_nidia_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_nidia_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "I don't really get what you're saying... But magic sounds cool!" # @t_snidia129.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_resolute_happy as nidia
            t_ch_nidia "Hooray! TO THE BOOKSCAPE!" # @t_snidia130.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Y-you can just call it the library..." # @t_snidia131.00 self.block='Last'
            $ slot_pick_count_nidia += 1
            # <NHSceneChange NHSceneChange {'name': '_4', 'scene': 's_nidia1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_nidia_Chosen__4:
                # <NHSceneChange NHSceneChange {'name': '_4', 'scene': 's_nidia1', 'kind': 'NHSceneChange'} ''>
                jump s_nidia1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_nidia_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_nidia_clasped_surprised as nidia
            t_ch_cousin "I'm not really the world-saving type... Sorry..." # @t_snidia132.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "That's okay... We should all be free to choose..." # @t_snidia133.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "If you change your mind, I'll be here." # @t_snidia134.00 self.block='Last'
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_nidia_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_nidia_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_clasped_surprised as nidia:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_nidia_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide nidia
                # Pass (ActorReset)
                $ scene_picked_once_nidia = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'richard', 'kind': 'Macro'} ''>
    label s_day0p5_richard:
        # <Macro Macro {'name': 'richard', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_richard:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_richard}', 'kind': 'IfFalse'} ''>
            label s_day0p5_richard_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_richard}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_richard_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_miller_aliens_serious as miller zorder 2:
                        default
                        xpos 0.7 
                        ypos 1.49 
                        alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_miller_aliens_serious as miller
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(Culinary Club, huh? I could learn to make cakes whenever I wanted!)" # @t_srichard10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(No one is at the booth though.)" # @t_srichard11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_miller_aliens_serious as miller:
                    # ShowWithAtl
                    linear .2 ypos 1.3 
                extend "{w=0.2}{nw}"
                t_ch_cousin "(Maybe they’ve got a brochure I can take…)" # @t_srichard12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_miller_aliens_serious as miller:
                    # ShowWithAtl
                    linear .2 ypos 0.9 
                show i_cousin_default_neutral as cousin
                extend "{w=0.2}{nw}"
                t_ch_richard "!!!" # @t_srichard13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_richard "[slot_playerName]" # @t_srichard14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_richard "(Is that…?)" # @t_srichard15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_miller_akimbo_serious as miller:
                    # ShowWithAtl
                    linear .2 ypos 0.5 
                extend "{w=0.2}{nw}"
                t_ch_richard "Thinking about joining the Culinary Club that’s great hey I don’t have time for small talk, so here’s the pitch." # @t_srichard16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_richard "You should join the Culinary Club." # @t_srichard17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_miller_akimbo_halfgrin as miller
                t_ch_richard "BAM!" # @t_srichard18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Oh, to hang out and learn recipes and stuff?" # @t_srichard19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_richard "That’s one way to put it." # @t_srichard110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_miller_akimbo_serious as miller
                t_ch_richard "Mostly I want to observe you until I can work up a complete dossier on your strengths and weaknesses in case you’re an end boss in the big conspiracy." # @t_srichard111.00 self.block='Last'
                menu:
                    "Join the Culinary Club??"

                    "Yes!":
                        $ slot_picked_richard_day1 = True
                    "Keep looking.":
                        $ slot_picked_richard_day1 = False
        if scene_picked_once_richard:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_richard}', 'kind': 'IfTrue'} ''>
            label s_day0p5_richard_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_richard}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_richard_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_miller_aliens_serious as miller zorder 2:
                        default
                        xpos 0.7 
                        ypos 0.6 
                        alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_richard "So. You in?" # @t_srichard115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_miller_aliens_shocked as miller:
                    # ShowWithAtl
                    linear 0.5 ypos 1.0 
                extend "{w=0.5}{nw}"
                t_ch_richard "DON’T ANSWER OUT LOUD. They’ll hear you. Blink once for yes and twice for no." # @t_srichard116.00 self.block='Last'
                menu:
                    "Join the Culinary Club??"

                    "Yes!":
                        $ slot_picked_richard_day1 = True
                    "Keep looking.":
                        $ slot_picked_richard_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_richard_day1}', 'name': '_2', 'path': 'richard/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_richard_day1:
            jump s_day0p5_richard_Chosen
        # <BranchMacro BranchMacro {'comparison': '!!${scene:picked_once_richard}', 'name': '_3', 'path': 'richard/PassedLoop', 'kind': 'BranchMacro'} ''>
        if not not scene_picked_once_richard:
            jump s_day0p5_richard_PassedLoop
        jump s_day0p5_richard_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_richard_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Note to self. Richard Miller is a little strange.)" # @t_srichard112.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Then again, at Namco High, I guess that means he fits right in…)" # @t_srichard113.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Um, yeah. Sure. Why not?" # @t_srichard113.01 self.block='Last'
            $ slot_pick_count_richard += 1
            # <NHSceneChange NHSceneChange {'name': '_4', 'scene': 's_richard1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_richard_Chosen__4:
                # <NHSceneChange NHSceneChange {'name': '_4', 'scene': 's_richard1', 'kind': 'NHSceneChange'} ''>
                jump s_richard1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_richard_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(Someone around here has got to be a little less crazy. Right…?)" # @t_srichard114.00 self.block='Last'
            jump s_day0p5_richard_cleanup
        # <Macro Macro {'name': 'PassedLoop', 'kind': 'Macro'} ''>
        label s_day0p5_richard_PassedLoop:
            # <Macro Macro {'name': 'PassedLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_sad as cousin
            t_ch_cousin "(BLINK BLINK!)" # @t_srichard119.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Sheesh.)" # @t_srichard120.00 self.block='Last'
            jump s_day0p5_richard_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_richard_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_richard_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_miller_aliens_shocked as miller:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_sad as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_richard_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide miller
                # Pass (ActorReset)
                $ scene_picked_once_richard = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'taira', 'kind': 'Macro'} ''>
    label s_day0p5_taira:
        # <Macro Macro {'name': 'taira', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_taira:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_taira}', 'kind': 'IfFalse'} ''>
            label s_day0p5_taira_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_taira}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_taira_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_taira_akimbo_happy as taira zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 3:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_happy as taira
                show i_cousin_default_neutral as cousin
                t_ch_taira "Hey Cuz! How’s my new best friend doin’?" # @t_staira10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Best… friend…?" # @t_staira11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " I guess it’s better than being this guy’s enemy…)" # @t_staira11.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_serious as taira
                t_ch_taira "Yo, you’re lookin’ mad confused. What’s up?!" # @t_staira12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "O-oh, it’s… nothing." # @t_staira13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I just… can’t decide on a club to join, that’s all!" # @t_staira13.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Heh heh… you know… to get out of detention early..." # @t_staira14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_happy as taira:
                    # ShowWithAtl
                    linear 1 xpos 0.43 
                extend "{w=1.0}{nw}"
                t_ch_taira "Oh yo, [slot_playerName], it’s so crazy that you’d say that…" # @t_staira15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_happy as taira:
                    # ShowWithAtl
                    linear 0.5 xpos 0.4 
                extend "{w=0.5}{nw}"
                extend " Cuz check it! I’ve got the perfect thing." # @t_staira15.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_steveholt_happy as taira
                t_ch_taira "YOU SHOULD JOIN THE WRESTLEBALL TEAM!" # @t_staira16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "Uhh.... I dunno..." # @t_staira17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You’re grabbing me a little hard, Taira..." # @t_staira17.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_steveholt_serious as taira:
                    # ShowWithAtl
                    linear 1 xpos 0.7 
                extend "{w=1.0}{nw}"
                t_ch_taira "What, you don’t WANNA join the wrestleball team??" # @t_staira18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_serious as taira
                extend " Why not? You chicken or something??" # @t_staira18.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_happy as taira
                t_ch_taira "Haw haw! O-or maybe you’re just too puny to compete!" # @t_staira19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " That’s it, isn’t it!" # @t_staira19.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Haw! What a twerp!" # @t_staira19.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "(What’s this guy’s deal?!" # @t_staira110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Does he actually like me or not?!)" # @t_staira110.01 self.block='Last'
                menu:
                    "Join the Wrestleball Club with Taira?"

                    "Sure, why not.":
                        $ slot_picked_taira_day1 = True
                    "I need some time to decide.":
                        $ slot_picked_taira_day1 = False
        if scene_picked_once_taira:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_taira}', 'kind': 'IfTrue'} ''>
            label s_day0p5_taira_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_taira}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_taira_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_taira_akimbo_happy as taira zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_default_happy as taira
                show i_cousin_default_neutral as cousin
                t_ch_taira "C’mon, new kid! Join the wrestleball team already!" # @t_staira113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Unless you’re too much of a DORK! Haw!" # @t_staira113.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_default_pleading as taira
                t_ch_taira "C’mon, please join?! PLEASE?!" # @t_staira114.00 self.block='Last'
                menu:
                    "Join the Wrestleball Club with Taira?"

                    "Sure, why not.":
                        $ slot_picked_taira_day1 = True
                    "I need some time to decide.":
                        $ slot_picked_taira_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_taira_day1}', 'name': '_2', 'path': 'taira/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_taira_day1:
            jump s_day0p5_taira_Chosen
        jump s_day0p5_taira_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_taira_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            $ slot_pick_count_taira += 1
            # <NHSceneChange NHSceneChange {'name': '_1', 'scene': 's_taira1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_taira_Chosen__1:
                # <NHSceneChange NHSceneChange {'name': '_1', 'scene': 's_taira1', 'kind': 'NHSceneChange'} ''>
                jump s_taira1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_taira_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_default_happy as taira
            show i_cousin_default_neutral as cousin
            t_ch_taira "Haw, whatever! Chicken!" # @t_staira111.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_default_pleading as taira
            extend " Yo, c’mon though, please??" # @t_staira111.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "I... need a minute to think about it..." # @t_staira112.00 self.block='Last'
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_taira_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_taira_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_default_pleading as taira:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_mortified as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_taira_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide taira
                # Pass (ActorReset)
                $ scene_picked_once_taira = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'terezi', 'kind': 'Macro'} ''>
    label s_day0p5_terezi:
        # <Macro Macro {'name': 'terezi', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_terezi:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_terezi}', 'kind': 'IfFalse'} ''>
            label s_day0p5_terezi_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_terezi}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_terezi_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_terezi_default_grin as terezi zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi
                show i_cousin_default_neutral as cousin
                t_ch_terezi "H1 TH3R3 COTTON C4NDY >:]" # @t_sterezi10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "1 C4N T3LL YOU’R3 LOOK1NG FOR TH3 COOL3ST OF COOL CLUBS TO JO1N" # @t_sterezi11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " 1 C4N SM3LL 1T ON YOU!" # @t_sterezi11.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "But that’s what we’re all doing here, isn’t it?" # @t_sterezi12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I mean… it’s Club Day." # @t_sterezi12.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_laugh as terezi
                t_ch_terezi "SHUSH!!!! YOU C4N’T H1D3 FROM M3 COTTON C4NDY" # @t_sterezi13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi
                t_ch_terezi "BUT YOU’R3 GONN4 W1SH YOU COULD!" # @t_sterezi14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi
                t_ch_terezi "YOU’R3 JO1N1NG M3 1N TH3 CR1M1N4L JUST1C3 CLUB OK?" # @t_sterezi15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "NO 4RGU1NG 4LLOW3D, TH4T’S JUST WH4T’S H4PP3N1NG >:]" # @t_sterezi16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(I still can’t tell if she’s threatening me or flirting…)" # @t_sterezi17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Um, I was gonna look at the other clubs first, s-so…" # @t_sterezi18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "OH NOOOOOO W444444YYYY" # @t_sterezi19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "YOU’R3 JO1N1NG MY CLUB!!!" # @t_sterezi110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi:
                    # ShowWithAtl
                    linear 0.20 xpos 0.65 
                extend "{w=0.2}{nw}"
                t_ch_terezi "DON’T M4K3 M3 US3 MY F3M1N1N3 W1L3S ON YOU…" # @t_sterezi111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_laugh as terezi
                t_ch_terezi "H3H3H3!" # @t_sterezi112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_mortified as cousin
                t_ch_cousin "YEEK!!!" # @t_sterezi113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi
                t_ch_terezi "PL34S3 JO1N?" # @t_sterezi114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " YOU’R3 PR3TTY COOL 4ND 1T’D B3 N1C3 TO H4V3 SOM3ON3 TO SH4R3 TH3 CLUB W1TH" # @t_sterezi114.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "…Oh. THAT’S what you meant by “feminine wiles”?" # @t_sterezi115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Just... being nice to me?" # @t_sterezi116.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I thought you were gonna try to coerce me with violence or something." # @t_sterezi116.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_laugh as terezi:
                    # ShowWithAtl
                    linear 0.20 xpos 0.7 
                extend "{w=0.2}{nw}"
                t_ch_terezi "H3H3 COTTON C4NDY YOU’R3 SOOOOO W31RD" # @t_sterezi117.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi
                t_ch_terezi "OBV1OUSLY 1 S4V3 V1OL3NC3 FOR SP3C14L OCC4S1ONS >:P" # @t_sterezi118.00 self.block='Last'
                menu:
                    "Join Terezi in the Criminal Justice Club?"

                    "Sure! I probably don't have a choice!":
                        $ slot_picked_terezi_day1 = True
                    "No! Resist!":
                        $ slot_picked_terezi_day1 = False
        if scene_picked_once_terezi:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_terezi}', 'kind': 'IfTrue'} ''>
            label s_day0p5_terezi_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_terezi}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_terezi_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
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
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi:
                    # ShowWithAtl
                    linear 0.20 xpos 0.68 
                extend "{w=0.2}{nw}"
                t_ch_terezi "YOU KNOW YOU W4NT TO" # @t_sterezi119.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi:
                    # ShowWithAtl
                    linear 0.20 xpos 0.65 
                extend "{w=0.2}{nw}"
                t_ch_terezi "1 C4N SM3LL 1T ON YOU >:P" # @t_sterezi120.00 self.block='Last'
                menu:
                    "Join Terezi in the Criminal Justice Club?"

                    "Sure! I probably don't have a choice!":
                        $ slot_picked_terezi_day1 = True
                    "No! Resist!":
                        $ slot_picked_terezi_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_terezi_day1}', 'name': '_2', 'path': 'terezi/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_terezi_day1:
            jump s_day0p5_terezi_Chosen
        jump s_day0p5_terezi_cleanup
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_terezi_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_default_grin as terezi:
                # ShowWithAtl
                linear 0.20 xpos 0.6 
            extend "{w=0.2}{nw}"
            t_ch_terezi "H3H3H3 1 KN3W 1T W4S ONLY 4 M4TT3R OF T1M3" # @t_sterezi121.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "L3T’S GO!!!" # @t_sterezi122.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_surprise_blush as cousin
            t_ch_cousin "(YIKES! She’s grabbing my arm and dragging me…" # @t_sterezi123.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_surprise as cousin
            extend " Whoah, she’s strong!!!)" # @t_sterezi123.01 self.block='Last'
            $ slot_pick_count_terezi += 1
            # <NHSceneChange NHSceneChange {'name': '_5', 'scene': 's_terezi1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_terezi_Chosen__5:
                # <NHSceneChange NHSceneChange {'name': '_5', 'scene': 's_terezi1', 'kind': 'NHSceneChange'} ''>
                jump s_terezi1
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_terezi_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_terezi_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_energetic_surprise as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_terezi_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide terezi
                # Pass (ActorReset)
                $ scene_picked_once_terezi = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'tomari', 'kind': 'Macro'} ''>
    label s_day0p5_tomari:
        # <Macro Macro {'name': 'tomari', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_tomari:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_tomari}', 'kind': 'IfFalse'} ''>
            label s_day0p5_tomari_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_tomari}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_tomari_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_tomari_standing_mortified as tomari zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                show i_tomari_standing_mortified as tomari
                t_ch_tomari "Ugh! That’s not right either." # @t_stomari10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "I’ll never figure it out without my glasses!" # @t_stomari11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_pondering_frustrated as tomari
                t_ch_tomari "ARRRGH!" # @t_stomari12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Whoa there, brainiac.  You’ll pop if you keep going like that." # @t_stomari13.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_standing_frustrated as tomari
                t_ch_tomari "Hm? Who’s there?" # @t_stomari14.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "What the – I’m right in front of you!" # @t_stomari15.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "Ah. Yes. I can see you’re roughly person shaped." # @t_stomari16.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "If short..." # @t_stomari17.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(That’s…a weird thing to say to someone…)" # @t_stomari18.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Uh, yeah. I’m [slot_playerName]. I’m new here." # @t_stomari18.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_alive_thoughtful as tomari
                t_ch_tomari "I’m Yuichiro Tomari: SUPER GENIUS." # @t_stomari19.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "That’s…definitely one way to introduce oneself." # @t_stomari110.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "For a super genius it is…" # @t_stomari111.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_alive_smile as tomari
                t_ch_tomari "THE ONLY WAY." # @t_stomari112.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(This guy is kinda nuts!)" # @t_stomari113.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Well, it sounds like this super genius is having fits with his homework." # @t_stomari114.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_alive_smile as tomari
                t_ch_tomaribang "Ha!" # @t_stomari115.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomaribang "And, did I mention: HA, HAHAHA?" # @t_stomari116.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_defeated_smile as tomari
                t_ch_tomaribang "No, what perplexes me isn’t the banal drudgery that passes for homework at this school." # @t_stomari117.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_pondering_thinking as tomari
                t_ch_tomaribang "It’s a complex engineering conundrum of my own design!" # @t_stomari118.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Tomari’s got intense feelings about homework.)" # @t_stomari119.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "You see, the endo-structure needs to be both supported and protected by an interlocking network of nanofiber units to provide locomotion. And it should be conductive to double as the processing strata to self-correct its own balance across the entire range of motion. I can’t take full credit for this brilliant scheme, of course, borrowed as it is from nature." # @t_stomari120.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "(I’m not following any of this stuff!!!)" # @t_stomari121.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "The problem is that I’ve got to invent half the science for it as I go." # @t_stomari122.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "Because no one else has." # @t_stomari123.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_pondering_thoughtful as tomari
                t_ch_tomari "Indeed, I worry, no one else CAN." # @t_stomari124.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "And without my glasses it’s become an endless series of frustrations!" # @t_stomari125.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(So, I guess it’s like extra credit then?)" # @t_stomari126.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Hm, better say something so he doesn’t think I’m clueless though!)" # @t_stomari127.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                extend " Well, uh. That sure is a conununadrumanum all right." # @t_stomari127.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Uh, that one kinda got away from me but maybe he didn’t notice!)" # @t_stomari128.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "A what?" # @t_stomari129.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_surprised as cousin
                t_ch_cousin "(Crud! Think fast, [slot_playerName]!)" # @t_stomari130.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                extend " Uh, what you should do is adjust the upper flange valve!" # @t_stomari130.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "…" # @t_stomari131.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(ACK! I only made it worse!)" # @t_stomari132.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_alive_smile as tomari
                t_ch_tomari "THAT’S BRILLIANT!" # @t_stomari133.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Yes. Okay. Sure it is. Why not." # @t_stomari134.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "You were able to diagnose the exact problem without even knowing what it was!" # @t_stomari135.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Yup, and furthermore you can’t prove I didn’t." # @t_stomari136.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_standing_smile as tomari
                t_ch_tomari "You should think about joining the Engineering Club! I don’t mind telling you we could use more students with your aptitude." # @t_stomari137.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Um." # @t_stomari138.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Engineering." # @t_stomari139.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "In a club." # @t_stomari140.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "With other people." # @t_stomari141.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Who know about engineering." # @t_stomari142.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "And stuff." # @t_stomari143.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Mm-hmm. Yeah." # @t_stomari144.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "Uh…" # @t_stomari145.00 self.block='Last'
                menu:
                    "Join the Engineering Club?"

                    "Go for it!":
                        $ slot_picked_tomari_day1 = True
                    "No way!!!":
                        $ slot_picked_tomari_day1 = False
        if scene_picked_once_tomari:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_tomari}', 'kind': 'IfTrue'} ''>
            label s_day0p5_tomari_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_tomari}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_tomari_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_tomari_standing_thinking as tomari zorder 2:
                        default
                        xpos 0.75 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.25 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_tomari "I don’t blame you for investigating the merits of the other clubs. Of course, you found them lacking and wish to join the Engineering Club…" # @t_stomari148.00 self.block='Last'
                menu:
                    "Join the Engineering Club?"

                    "Go for it!":
                        $ slot_picked_tomari_day1 = True
                    "No way!!!":
                        $ slot_picked_tomari_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_tomari_day1}', 'name': '_2', 'path': 'tomari/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_tomari_day1:
            jump s_day0p5_tomari_Chosen
        jump s_day0p5_tomari_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_tomari_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Maybe I’m a natural genius at this stuff. What could go wrong?)" # @t_stomari146.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            extend " Yeah, let’s do it!" # @t_stomari146.01 self.block='Last'
            $ slot_pick_count_tomari += 1
            # <NHSceneChange NHSceneChange {'name': '_3', 'scene': 's_tomari1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_tomari_Chosen__3:
                # <NHSceneChange NHSceneChange {'name': '_3', 'scene': 's_tomari1', 'kind': 'NHSceneChange'} ''>
                jump s_tomari1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_tomari_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Ack, no way! This egghead would see right through me.)" # @t_stomari147.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_tomari_standing_smile as tomari
            show i_cousin_default_neutral as cousin
            extend " Um, I’ll uh get back to you on that one." # @t_stomari147.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " (Yeah, when katamari fly!)" # @t_stomari147.02 self.block='Last'
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_tomari_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_tomari_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_standing_smile as tomari:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_tomari_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide tomari
                # Pass (ActorReset)
                $ scene_picked_once_tomari = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice
    # <Macro Macro {'name': 'valk', 'kind': 'Macro'} ''>
    label s_day0p5_valk:
        # <Macro Macro {'name': 'valk', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_valk:
            # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_valk}', 'kind': 'IfFalse'} ''>
            label s_day0p5_valk_FirstTime:
                # <IfFalse IfFalse {'auto': 'true', 'name': 'FirstTime', 'value': '${scene:picked_once_valk}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_valk_FirstTime_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_valkyrie_default_grin as valkyrie zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_valkyrie_default_grin as valkyrie
                show i_cousin_default_neutral as cousin
                t_ch_valkyrie "Couldn't stay away, huh?" # @t_svalk10.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_valkyrie_default_wink as valkyrie
                t_ch_valkyrie "If you wanna hang out some more, I'll be in wood shop." # @t_svalk11.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Call it a date!" # @t_svalk11.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " At school... With everybody around..." # @t_svalk11.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_valkyrie_akimbo_grin as valkyrie
                t_ch_valkyrie "LOL… Okay, maybe it's not exactly a date." # @t_svalk12.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Aaaanywaaaaay, maybe I'll see you there!" # @t_svalk12.01 self.block='Last'
                menu:
                    "Maybe I'll see you at Wood Shop!"

                    "Maybe you will.":
                        $ slot_picked_valk_day1 = True
                    "I'm terrible at dates-- I MEAN WOOD SHOP":
                        $ slot_picked_valk_day1 = False
        if scene_picked_once_valk:
            # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_valk}', 'kind': 'IfTrue'} ''>
            label s_day0p5_valk_Loop:
                # <IfTrue IfTrue {'auto': 'true', 'name': 'Loop', 'value': '${scene:picked_once_valk}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0p5_valk_Loop_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_valkyrie_default_grin as valkyrie zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                menu:
                    "Maybe I'll see you at Wood Shop!"

                    "Maybe you will.":
                        $ slot_picked_valk_day1 = True
                    "I'm terrible at dates-- I MEAN WOOD SHOP":
                        $ slot_picked_valk_day1 = False
        # <BranchMacro BranchMacro {'comparison': '!!${slot:picked_valk_day1}', 'name': '_2', 'path': 'valk/Chosen', 'kind': 'BranchMacro'} ''>
        if not not slot_picked_valk_day1:
            jump s_day0p5_valk_Chosen
        jump s_day0p5_valk_PassedFirstTime
        # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
        label s_day0p5_valk_Chosen:
            # <Macro Macro {'name': 'Chosen', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Maybe you will." # @t_svalk13.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_akimbo_thoughtful as valkyrie
            t_ch_valkyrie "Oh? I guess I better show up then..." # @t_svalk14.00 self.block='Last'
            $ slot_pick_count_valk += 1
            # <NHSceneChange NHSceneChange {'name': '_3', 'scene': 's_valk1', 'kind': 'NHSceneChange'} ''>
            label s_day0p5_valk_Chosen__3:
                # <NHSceneChange NHSceneChange {'name': '_3', 'scene': 's_valk1', 'kind': 'NHSceneChange'} ''>
                jump s_valk1
        # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
        label s_day0p5_valk_PassedFirstTime:
            # <Macro Macro {'name': 'PassedFirstTime', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "I'm terrible at dates-- I MEAN WOOD SHOP" # @t_svalk15.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_valkyrie "Haha... You don't say." # @t_svalk16.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_armscrossed_wink as valkyrie
            extend " Well, I won't be here forever... So if you're gonna change your mind, change it quick!" # @t_svalk16.01 self.block='Last'
            jump s_day0p5_valk_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day0p5_valk_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_valk_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_valkyrie_armscrossed_wink as valkyrie:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_surprised as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day0p5_valk_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide valkyrie
                # Pass (ActorReset)
                $ scene_picked_once_valk = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day0p5_day0p5prechoice