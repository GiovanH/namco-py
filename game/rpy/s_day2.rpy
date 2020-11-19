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
# <Scene scene {'id': 's_day2', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_day2:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_day2"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_day2', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day2initialize', 'kind': 'ParallelEvent'} ''>
    label s_day2_day2initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day2initialize', 'kind': 'ParallelEvent'} ''>
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
            alpha 1.0
            xpos 0.3 
        show i_digdug_left as digdug zorder 2:
            default
            xpos 0.7 
            alpha 1.0
        show i_king_confident as king zorder 1:
            default
            xpos 0.8 
            alpha 1.0
            xzoom -1.0 

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
    play music "bgm/school.ogg" loop
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_digdug "Another day, everyone is here..." # @t_scousin20.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Remarkable!" # @t_scousin20.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "King agrees! Keep up this excellent behavior!" # @t_scousin21.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "See you at the bell." # @t_scousin22.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    show i_king_confident as king:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    $ renpy.pause(0.333, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    hide digdug
    hide king
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.5 
    extend "{w=0.333}{nw}"
    t_ch_cousin "(I wonder if anyone joined a club yesterday?)" # @t_scousin23.00 self.block='Last'
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day2prechoice', 'kind': 'ParallelEvent'} ''>
    label s_day2_day2prechoice:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day2prechoice', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
    $ s_day2_has_picked_any = False if not "s_day2_has_picked_any" in store.__dict__ else s_day2_has_picked_any
    window hide
    menu (screen="ChoiceExploration"):
        "Aki Matsuo":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_amazona
        "Albatross":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_albatros
        "Anti-Bravoman":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_antibravo
        "Blue Max":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_bluemax
        "Davesprite":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_davesprite
        "Donko":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_donko
        "Galaga":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_galaga
        "Hiromi":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_hiromi
        "Jane Crocker":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_jane
        "Lolo":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_lolo
        "Meowkie":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_meowkie
        "Mr. Driller":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_mrdriller
        "Nidia":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_nidia
        "Richard Miller":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_richard
        "Taira":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_taira
        "Terezi Pyrope":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_terezi
        "Tomari":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_tomari
        "Valkyrie":
            $ s_day2_has_picked_any = True
            window show
            jump s_day2_valk
        "Wait for detention to end." if s_day2_has_picked_any:
            window show
            jump s_day2_cousin
    # <Macro Macro {'name': 'albatros', 'kind': 'Macro'} ''>
    label s_day2_albatros:
        # <Macro Macro {'name': 'albatros', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_albatros_day1} && !${scene:picked_once_albatros}', 'name': '_0', 'path': 'albatros/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_albatros_day1 and not scene_picked_once_albatros:
            jump s_day2_albatros_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_albatros_day1} &&  ${scene:picked_once_albatros}', 'name': '_1', 'path': 'albatros/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_albatros_day1 and  scene_picked_once_albatros:
            jump s_day2_albatros_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_albatros_day1} && !${scene:picked_once_albatros}', 'name': '_2', 'path': 'albatros/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_albatros_day1 and not scene_picked_once_albatros:
            jump s_day2_albatros_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_albatros_day1} &&  ${scene:picked_once_albatros}', 'name': '_3', 'path': 'albatros/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_albatros_day1 and  scene_picked_once_albatros:
            jump s_day2_albatros_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_albatros_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_albatros_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_albatross_toocool_smirk as albatros
            t_ch_albatros "Back for more, eh?" # @t_salbatros2x0.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "(Gosh, not even a good afternoon!)" # @t_salbatros2x1.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Al doesn’t waste a moment, does he?)" # @t_salbatros2x2.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "I’m always up for a little more, Al." # @t_salbatros2x3.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "I thought as much after our last rendezvous." # @t_salbatros2x4.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin_blush as cousin
            with Dissolve(.333)
            t_ch_cousin "(Wow a RONDAYVIEW or however you spell it. Very grown up and cool!)" # @t_salbatros2x5.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_toocool_smirk_wink as albatros
            t_ch_albatros "Care to prove it though?" # @t_salbatros2x6.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "P-prove it?" # @t_salbatros2x7.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_welcome_smirk as albatros
            t_ch_albatros "Skip detention tomorrow." # @t_salbatros2x8.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_welcome_smirk_wink as albatros
            t_ch_albatros "With me." # @t_salbatros2x9.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Hmm, must be for N.A.R.C. business.)" # @t_salbatros2x10.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Because fighting crime takes you to some dark corners of society, I bet.)" # @t_salbatros2x11.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Like skipping!)" # @t_salbatros2x12.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            extend " Yeah, well." # @t_salbatros2x12.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_grin as cousin
            t_ch_cousin "Maybe I’ll think about it." # @t_salbatros2x13.00 self.block='Last'
            jump s_day2_albatros_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_albatros_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_albatros_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_toocool_smirk_wink as albatros zorder 2:
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
            show i_cousin_default_neutral as cousin
            show i_albatross_toocool_smirk_wink as albatros:
                # ShowWithAtl
                pause 1.0 
                linear .5 alpha 0.0
            extend "{w=1.5}{nw}"
            t_ch_cousin "(He just winked at me and turned away…)" # @t_salbatros2x43.00 self.block='Last'
            jump s_day2_albatros_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_albatros_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_albatros_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_watch_staredown as albatros zorder 2:
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
            show i_cousin_default_neutral as cousin
            show i_albatross_watch_staredown as albatros
            t_ch_cousin "(Hmm, Al looks upset.)" # @t_salbatros2x14.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_watch_staredown as albatros
            t_ch_cousin "(Like he’s having an argument.)" # @t_salbatros2x15.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "“The ringleader has left the circus.”" # @t_salbatros2x16.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_watch_distraught as albatros
            t_ch_albatros "Oh, come on!" # @t_salbatros2x17.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "It couldn’t be more obvious!" # @t_salbatros2x18.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(An argument...with his watch?!)" # @t_salbatros2x19.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "Tsk. It means the target has left the mission zone." # @t_salbatros2x20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "(Target? Mission Zone? Who’s he talking to???)" # @t_salbatros2x21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_watch_inquisitive as albatros
            show i_cousin_default_neutral as cousin
            t_ch_albatros "Yes, I know, it’s a lot of work being the chief." # @t_salbatros2x22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear .25 xpos 0.35 
            extend "{w=0.25}{nw}"
            t_ch_albatros "But you could stand to read memos about official undercover agent lingo." # @t_salbatros2x23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_watch_staredown as albatros
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear .25 xpos 0.4 
            extend "{w=0.25}{nw}"
            t_ch_albatros "No, the target did not attend the completely fake N.A.R.C. meeting. Probably to conduct illegal cheat code activities." # @t_salbatros2x24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear .25 xpos 0.45 
            extend "{w=0.25}{nw}"
            t_ch_albatros "No, I don’t believe target suspects anything." # @t_salbatros2x25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Heya, Al." # @t_salbatros2x26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_welcome_distraught as albatros
            show i_cousin_default_grin as cousin:
                # ShowWithAtl
                linear .25 xpos 0.3 
            extend "{w=0.25}{nw}"
            t_ch_albatros "!!!!" # @t_salbatros2x27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_watch_staredown as albatros
            play sound "sfx/albatrosswatchbeep.ogg"
            t_ch_albatros "TRANSMISSION CLOSED." # @t_salbatros2x28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_toocool_smug as albatros
            t_ch_albatros "[slot_playerName]!" # @t_salbatros2x29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_toocool_inquisitive as albatros
            t_ch_albatros "Uh, how much of that did you hear?" # @t_salbatros2x30.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "All of it. The whole thing." # @t_salbatros2x31.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_toocool_distraught as albatros
            t_ch_albatros "Ah." # @t_salbatros2x32.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "Well." # @t_salbatros2x33.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Sounded like you were talking in code." # @t_salbatros2x34.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "During an argument." # @t_salbatros2x35.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "With your watch." # @t_salbatros2x36.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_albatros "Yes. That is what it sounded like." # @t_salbatros2x37.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_fistinhand_distraught as albatros
            t_ch_albatros "I bet you know all about codes like…" # @t_salbatros2x38.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " C…" # @t_salbatros2x38.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " U…" # @t_salbatros2x38.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_fistinhand_inquisitive as albatros
            extend " Later?" # @t_salbatros2x38.03 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "(Wow secret codes already, play it cool, [slot_playerName]!)" # @t_salbatros2x39.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Yeah…" # @t_salbatros2x40.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Maybe." # @t_salbatros2x41.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "(Nailed it.)" # @t_salbatros2x42.00 self.block='Last'
            jump s_day2_albatros_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_albatros_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_albatros_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_toocool_smirk_wink as albatros zorder 2:
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
            # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_albatross_toocool_smirk_wink as albatros:
                # ShowWithAtl
                pause 1.0 
                linear .5 alpha 0.0
            extend "{w=1.5}{nw}"
            t_ch_cousin "(He just winked at me and turned away…)" # @t_salbatros2x43.00 self.block='Last'
            jump s_day2_albatros_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_albatros_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_albatros_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_albatross_toocool_smirk_wink as albatros:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_albatros_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide albatros
                # Pass (ActorReset)
                $ scene_picked_once_albatros = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'amazona', 'kind': 'Macro'} ''>
    label s_day2_amazona:
        # <Macro Macro {'name': 'amazona', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_amazona_day1} && !${scene:picked_once_amazona}', 'name': '_0', 'path': 'amazona/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_amazona_day1 and not scene_picked_once_amazona:
            jump s_day2_amazona_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_amazona_day1} &&  ${scene:picked_once_amazona}', 'name': '_1', 'path': 'amazona/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_amazona_day1 and  scene_picked_once_amazona:
            jump s_day2_amazona_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_amazona_day1} && !${scene:picked_once_amazona}', 'name': '_2', 'path': 'amazona/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_amazona_day1 and not scene_picked_once_amazona:
            jump s_day2_amazona_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_amazona_day1} &&  ${scene:picked_once_amazona}', 'name': '_3', 'path': 'amazona/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_amazona_day1 and  scene_picked_once_amazona:
            jump s_day2_amazona_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_amazona_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_amazona_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_wink as donko zorder 2:
                    default
                    alpha 0.0
                    xpos 0.72 
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_default_smile as aki
            show i_cousin_default_neutral as cousin
            show i_donko_default_wink as donko
            t_ch_cousin "Hey Aki!" # @t_samazona20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_default_distracted as aki
            t_ch_aki "Oh! Hi! Sorry about yesterday... I just can't afford to fall behind on my schedule." # @t_samazona21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "It's okay... But maybe you have time today!" # @t_samazona22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " To have... Y'know... An entire conversation?" # @t_samazona22.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_aki "Yeah... Again, really sorry about that. I'll pencil in some conversation time." # @t_samazona23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Um... Suddenly it feels like a lot of pressure... )" # @t_samazona24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_akimbo_smile as aki
            t_ch_aki "Actually... I have to practice for the school play tomorrow... Maybe you can help!" # @t_samazona25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "That sounds fun!" # @t_samazona26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_aki "Great! Just let me know." # @t_samazona27.00 self.block='Last'
            jump s_day2_amazona_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_amazona_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_amazona_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_aki_akimbo_smile as aki zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_akimbo_smile as aki
            t_ch_aki "Actually... I have to practice for the school play tomorrow... Maybe you can help!" # @t_samazona25.00 self.block='Last'
            jump s_day2_amazona_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_amazona_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_amazona_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_wink as donko zorder 2:
                    default
                    alpha 0.0
                    xpos 0.72 
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_aki_default_smile as aki
            t_ch_cousin "Hey Aki!" # @t_samazona28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_aki "Hi [slot_playerName]!" # @t_samazona29.00 self.block='Last'
            play sound "sfx/sentaisignal.ogg"
            # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_default_nervouslaughter as aki:
                # FadeEvent
                linear 0.3 alpha 0.0
            extend "{w=0.3}{nw}"
            t_ch_aki "AH! I'll be right back!" # @t_samazona210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(That was weird... )" # @t_samazona211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_default_wink as donko:
                # FadeEvent
                linear 0.3 alpha 1.0
            extend "{w=0.3}{nw}"
            t_ch_donko "Don't take it personally... She does it to everyone. She just has so much going on!" # @t_samazona212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_default_meloncholic as donko
            t_ch_donko "She's really amazing... But it also, like, makes it difficult to be her friend. She might be a little TOO busy." # @t_samazona213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_default_grin as donko:
                # FadeEvent
                linear 0.3 alpha 0.0
            extend "{w=0.3}{nw}"
            t_ch_donko "Anyway, BYEEEE!" # @t_samazona214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_default_smile as aki:
                # FadeEvent
                linear 0.3 alpha 1.0
            extend "{w=0.3}{nw}"
            t_ch_aki "Sorry about that!" # @t_samazona215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Everything okay?" # @t_samazona216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_default_nervouslaughter as aki
            t_ch_aki "It's GREAT! Hahahaha! Never better!" # @t_samazona217.00 self.block='Last'
            play sound "sfx/sentaisignal.ogg"
            # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_default_nervouslaughter as aki:
                # FadeEvent
                linear 0.3 alpha 0.0
            extend "{w=0.3}{nw}"
            t_ch_aki "AH! Just... Just a moment!" # @t_samazona218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(Okay... This is getting ridiculous.)" # @t_samazona219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_aki_akimbo_laughter_nervous as aki:
                # FadeEvent
                linear 0.2 alpha 1.0
            extend "{w=0.2}{nw}"
            t_ch_aki "Phew... Sorry..." # @t_samazona220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(There's definitely something suspicious happening here!)" # @t_samazona221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(This bears investigation... )" # @t_samazona222.00 self.block='Last'
            jump s_day2_amazona_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_amazona_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_amazona_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_aki "Sorry about earlier…" # @t_samazona223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Definitely suspicious… I wonder what’s really going on.)" # @t_samazona224.00 self.block='Last'
            jump s_day2_amazona_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_amazona_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_amazona_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_grin as donko:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_aki_default_smile as aki:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_amazona_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide donko
                hide aki
                # Pass (ActorReset)
                $ scene_picked_once_amazona = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'antibravo', 'kind': 'Macro'} ''>
    label s_day2_antibravo:
        # <Macro Macro {'name': 'antibravo', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_antibravo_day1} && !${scene:picked_once_antibravo}', 'name': '_0', 'path': 'antibravo/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_antibravo_day1 and not scene_picked_once_antibravo:
            jump s_day2_antibravo_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_antibravo_day1} &&  ${scene:picked_once_antibravo}', 'name': '_1', 'path': 'antibravo/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_antibravo_day1 and  scene_picked_once_antibravo:
            jump s_day2_antibravo_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_antibravo_day1} && !${scene:picked_once_antibravo}', 'name': '_2', 'path': 'antibravo/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_antibravo_day1 and not scene_picked_once_antibravo:
            jump s_day2_antibravo_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_antibravo_day1} &&  ${scene:picked_once_antibravo}', 'name': '_3', 'path': 'antibravo/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_antibravo_day1 and  scene_picked_once_antibravo:
            jump s_day2_antibravo_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_antibravo_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_antibravo_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_abm_backturned_sad as antibravo zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_backturned_sad as antibravo
            show i_cousin_default_grin as cousin
            t_ch_cousin "Hey buddy!" # @t_santibravo20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo ".... ?" # @t_santibravo21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(He's looking around...)" # @t_santibravo22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_grin as cousin
            t_ch_cousin "I'm talking to you, Anti-Bravoman." # @t_santibravo23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "OH right... Haha... Of course...." # @t_santibravo24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Am I going to see you at Poetry Club later?" # @t_santibravo25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "Er... Yeah... Definitely..." # @t_santibravo26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_neutral as cousin
            t_ch_cousin "(He doesn't seem very sure... )" # @t_santibravo27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Cool... So I'll see you there..." # @t_santibravo28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_abm_backturned_sad as antibravo
            t_ch_cousin "(He's just fidgeting nervously... I pushed too hard yesterday, so I should probably let this one go... )" # @t_santibravo29.00 self.block='Last'
            jump s_day2_antibravo_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_antibravo_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_antibravo_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_abm_backturned_sad as antibravo zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "Gloaming… gloom… in the shade of my…….. long night of the soul…" # @t_santibravo226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(I’m going to ignore that… )" # @t_santibravo227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Maybe I’ll see you at poetry club!" # @t_santibravo228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_default_broody as antibravo
            t_ch_antibravo "Not if you’re lucky!" # @t_santibravo229.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(Th-this guy-- !)" # @t_santibravo230.00 self.block='Last'
            jump s_day2_antibravo_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_antibravo_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_antibravo_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_abm_backturned_sad as antibravo zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_abm_backturned_sad as antibravo
            t_ch_antibravo "No one should be subject to..." # @t_santibravo210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " The creeping lurkspace inside of me." # @t_santibravo210.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " The sound of my voice... Is like a thousand black markers writing at once." # @t_santibravo210.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " My eyes are--" # @t_santibravo210.03 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_default_surprised as antibravo:
                linear 0.25 xzoom -1.0 
            t_ch_antibravo "OH! It's you." # @t_santibravo211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Sorry... You were on a roll and I didn't want to interrupt..." # @t_santibravo212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo ".................." # @t_santibravo213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Er... How are you?" # @t_santibravo214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "I think... Everyone is talking about me." # @t_santibravo215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Er... Are you sure?" # @t_santibravo216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "They keep saying 'freak'." # @t_santibravo217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " That usually tips me off." # @t_santibravo217.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_sad as cousin
            t_ch_cousin "(Ouch...)" # @t_santibravo218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Well, I'm not going to call you that." # @t_santibravo219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Nice to see you, Anti-Bravoman." # @t_santibravo220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_default_surprised_blush as antibravo
            t_ch_antibravo "N-nice to see you too." # @t_santibravo221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(It seems like he doesn't know how to act when someone's nice to him... )" # @t_santibravo222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "You're in poetry club, right? Maybe I'll come by..." # @t_santibravo223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "Um... I'll be there... Sure..." # @t_santibravo224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Hmm... His heart doesn't seem like it's in it. Is he lying? I'd better not pry... he seems pretty sensitive underneath that dark aura.)" # @t_santibravo225.00 self.block='Last'
            jump s_day2_antibravo_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_antibravo_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_antibravo_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_abm_backturned_sad as antibravo zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_antibravo "Gloaming… gloom… in the shade of my…….. long night of the soul…" # @t_santibravo226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(I’m going to ignore that… )" # @t_santibravo227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Maybe I’ll see you at poetry club!" # @t_santibravo228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_default_broody as antibravo
            t_ch_antibravo "Not if you’re lucky!" # @t_santibravo229.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(Th-this guy-- !)" # @t_santibravo230.00 self.block='Last'
            jump s_day2_antibravo_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_antibravo_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_antibravo_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_abm_default_broody as antibravo:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_mortified as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_antibravo_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide antibravo
                # Pass (ActorReset)
                $ scene_picked_once_antibravo = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'bluemax', 'kind': 'Macro'} ''>
    label s_day2_bluemax:
        # <Macro Macro {'name': 'bluemax', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_bluemax_day1} && !${scene:picked_once_bluemax}', 'name': '_0', 'path': 'bluemax/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_bluemax_day1 and not scene_picked_once_bluemax:
            jump s_day2_bluemax_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_bluemax_day1} &&  ${scene:picked_once_bluemax}', 'name': '_1', 'path': 'bluemax/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_bluemax_day1 and  scene_picked_once_bluemax:
            jump s_day2_bluemax_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_bluemax_day1} && !${scene:picked_once_bluemax}', 'name': '_2', 'path': 'bluemax/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_bluemax_day1 and not scene_picked_once_bluemax:
            jump s_day2_bluemax_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_bluemax_day1} &&  ${scene:picked_once_bluemax}', 'name': '_3', 'path': 'bluemax/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_bluemax_day1 and  scene_picked_once_bluemax:
            jump s_day2_bluemax_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_bluemax_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_bluemax_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_serious as taira zorder 2:
                    default
                    xpos 0.5 
                    alpha 0.0
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
            show i_cousin_default_neutral as cousin
            show i_bluemax_stand_worried as bluemax
            t_ch_max "Hi, [slot_playerName]." # @t_sbluemax230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Hey, Max." # @t_sbluemax231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "You get home okay yesterday?" # @t_sbluemax232.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_shock_smile as bluemax
            t_ch_max "Sure did. I used my advanced commando techniques!" # @t_sbluemax233.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Um, that’s good." # @t_sbluemax234.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " (Whatever those are!)" # @t_sbluemax234.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_serious as bluemax
            t_ch_max "Thanks again for, y’know. For everything yesterday." # @t_sbluemax235.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Anytime, Max. Hey, when’s our next meeting?" # @t_sbluemax236.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_smile as bluemax
            t_ch_max "Oh, I wanted to talk to you about that!" # @t_sbluemax237.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "We’re going to a new mission perimeter zone where rogue Wrestleball players will be less likely to ambush us." # @t_sbluemax238.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "So, we’re going to meet for lunch tomorrow." # @t_sbluemax239.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stop_serious as bluemax
            t_ch_max "AT THE CAFE!" # @t_sbluemax240.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Oh. But...that’s off school grounds, isn’t it?" # @t_sbluemax241.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "It’s like skipping class." # @t_sbluemax242.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_worried as bluemax
            t_ch_max "It is, yeah. But what choice do we have with Taira roaming the halls of Namco High?" # @t_sbluemax243.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "Anyway, it’ll give us a chance to talk about PROJECT SUPER SECRET PLANE." # @t_sbluemax244.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_serious as bluemax
            t_ch_max "Oh, and don’t be confused, [slot_playerName]. It’s not actually a new program!" # @t_sbluemax245.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Why is he whispering?)" # @t_sbluemax246.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_shock_serious as bluemax
            t_ch_max "PROJECT SUPER SECRET PLANE is my codename for SECRET PROJECT SUPER PLANE to make it even harder to guess than before!" # @t_sbluemax247.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(Um…)" # @t_sbluemax248.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Um…" # @t_sbluemax248.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Uh…" # @t_sbluemax249.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Oh, yeah. Yeah, I get it now." # @t_sbluemax250.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stop_smile as bluemax
            t_ch_max "Yup! So, I’ll see you at the cafe tomorrow, okay?" # @t_sbluemax250.00a self.block='Last'
            jump s_day2_bluemax_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_bluemax_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_bluemax_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_serious as taira zorder 2:
                    default
                    xpos 0.5 
                    alpha 0.0
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_bluemax_stand_worried as bluemax zorder 2:
                    default
                    xpos 0.75 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_bluemax_stand_worried as bluemax
            t_ch_max "I’m busy, we’ll talk tomorrow, okay?" # @t_sbluemax250.00b self.block='Last'
            jump s_day2_bluemax_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_bluemax_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_bluemax_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_serious as taira zorder 2:
                    default
                    xpos 0.5 
                    alpha 0.0
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_bluemax_shock_serious as bluemax zorder 2:
                    default
                    xpos 0.75 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_shock_serious as bluemax
            show i_taira_akimbo_serious as taira
            show i_cousin_default_neutral as cousin
            t_ch_max "EEEEEEEEER" # @t_sbluemax20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stop_serious as bluemax
            t_ch_max "ATTA-TAT-TAT-TAT" # @t_sbluemax21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_serious as bluemax
            t_ch_max "KABOOM!" # @t_sbluemax22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(What the...?)" # @t_sbluemax23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Hey, Blue Max." # @t_sbluemax23.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_shock as bluemax
            show i_cousin_default_surprised as cousin
            t_ch_max "AHH!" # @t_sbluemax24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_sad as cousin
            t_ch_cousin "(He’s as wound up as ever.)" # @t_sbluemax25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_cower_flustered as bluemax
            t_ch_max "Oh. Um. Hi, [slot_playerName]." # @t_sbluemax26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Sure is holding his arm funny.)" # @t_sbluemax27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Or, wing, I guess.)" # @t_sbluemax28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " What’cha got there?" # @t_sbluemax28.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "Nothing. It’s nothing." # @t_sbluemax29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "Ow!" # @t_sbluemax210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Gosh, he’s really wincing that arm. Or wing. Wonder how he hurt himself.)" # @t_sbluemax211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Looks like you drew an airplane doing a bomb run on some army dudes." # @t_sbluemax211.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " (And for some reason the army dudes are wearing wrestleball uniforms…?)" # @t_sbluemax211.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "No, it’s nothing." # @t_sbluemax212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "Please leave me alone. I have to catch up on some homework." # @t_sbluemax213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "Yo, Blue Dork!" # @t_sbluemax214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_akimbo_serious as taira:
                # FadeEvent
                linear 0.2 alpha 1.0
            show i_cousin_default_surprised as cousin:
                # ShowWithAtl
                linear .2 xpos 0.18 
            show i_bluemax_shock_shocked as bluemax:
                # ShowWithAtl
                linear .2 xpos 0.79 
            $ renpy.pause(0.2, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "AHH!" # @t_sbluemax215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "You done with my homework yet or what?" # @t_sbluemax216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_bluemax_stand_worried as bluemax
            t_ch_max "Almost." # @t_sbluemax217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "I ain’t got all day!" # @t_sbluemax218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "Probably. I dunno." # @t_sbluemax219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "It’s due whenever. Just it get done before then!" # @t_sbluemax220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_akimbo_serious as taira:
                # FadeEvent
                linear 0.25 alpha 0.0
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                pause 0.33 
                linear .2 xpos 0.25 
            show i_bluemax_stand_worried as bluemax:
                # ShowWithAtl
                pause 0.33 
                linear .2 xpos 0.7 
            $ renpy.pause(0.53, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Hold on, you’re doing HIS homework?" # @t_sbluemax221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "It’s better than not doing it. Trust me." # @t_sbluemax222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "Anyway, as long as I do his homework he won’t revenge on other students." # @t_sbluemax223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "Especially smaller ones." # @t_sbluemax224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "Like you." # @t_sbluemax225.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_angry as cousin
            t_ch_cousin "Even so! That doesn’t make it right!" # @t_sbluemax226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "Yeah, well." # @t_sbluemax227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_serious as bluemax
            t_ch_max "I have plans." # @t_sbluemax228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_max "Meet me at the cafe for lunch tomorrow. We can talk more freely there." # @t_sbluemax229.00 self.block='Last'
            jump s_day2_bluemax_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_bluemax_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_bluemax_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_serious as taira zorder 2:
                    default
                    xpos 0.5 
                    alpha 0.0
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_bluemax_stand_worried as bluemax zorder 2:
                    default
                    xpos 0.75 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_bluemax_stand_worried as bluemax
            t_ch_max "I’m busy, we’ll talk tomorrow, okay?" # @t_sbluemax250.00b self.block='Last'
            jump s_day2_bluemax_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_bluemax_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_bluemax_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_bluemax_stand_worried as bluemax:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_taira_akimbo_serious as taira:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_bluemax_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide bluemax
                hide taira
                # Pass (ActorReset)
                $ scene_picked_once_bluemax = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'cousin', 'kind': 'Macro'} ''>
    label s_day2_cousin:
        # <Macro Macro {'name': 'cousin', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <Macro Macro {'name': 'wrapper', 'kind': 'Macro'} ''>
        label s_day2_cousin_wrapper:
            # <Macro Macro {'name': 'wrapper', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            menu:
                "Yeah, I just want detention to be over with.":
                    $ scene_doneExplore = True
                "Wait, I wanted to talk to someone else…":
                    $ scene_doneExplore = False
            if scene_doneExplore:
                # <IfTrue IfTrue {'name': 'bail', 'value': '${scene:doneExplore}', 'kind': 'IfTrue'} ''>
                label s_day2_cousin_wrapper_bail:
                    # <IfTrue IfTrue {'name': 'bail', 'value': '${scene:doneExplore}', 'kind': 'IfTrue'} ''>
                    # <Events events {'kind': 'events'} ''>
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    label s_day2_cousin_wrapper_bail_warm:
                        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                        # <Events events {'kind': 'events'} ''>
                        show i_cousin_default_sad as cousin zorder 2:
                            # ActorEvent
                            xpos 0.5 
                            alpha 0.0
                            linear 0.5 alpha 1.0
                        $ renpy.pause(0.5, hard=True) # TimedPause
                    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    t_ch_cousin "(This punishment can’t end soon enough.)" # @t_scousin24.00 self.block='Last'
                    # <NHSceneChange NHSceneChange {'name': '_2', 'scene': 's_day2.5', 'kind': 'NHSceneChange'} ''>
                    label s_day2_cousin_wrapper_bail__2:
                        # <NHSceneChange NHSceneChange {'name': '_2', 'scene': 's_day2.5', 'kind': 'NHSceneChange'} ''>
                        jump s_day2p5
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_cousin_wrapper_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                # Pass (ActorReset)
                $ scene_picked_once_cousin = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'davesprite', 'kind': 'Macro'} ''>
    label s_day2_davesprite:
        # <Macro Macro {'name': 'davesprite', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_davesprite_day1} && !${scene:picked_once_davesprite}', 'name': '_0', 'path': 'davesprite/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_davesprite_day1 and not scene_picked_once_davesprite:
            jump s_day2_davesprite_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_davesprite_day1} &&  ${scene:picked_once_davesprite}', 'name': '_1', 'path': 'davesprite/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_davesprite_day1 and  scene_picked_once_davesprite:
            jump s_day2_davesprite_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_davesprite_day1} && !${scene:picked_once_davesprite}', 'name': '_2', 'path': 'davesprite/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_davesprite_day1 and not scene_picked_once_davesprite:
            jump s_day2_davesprite_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_davesprite_day1} &&  ${scene:picked_once_davesprite}', 'name': '_3', 'path': 'davesprite/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_davesprite_day1 and  scene_picked_once_davesprite:
            jump s_day2_davesprite_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_davesprite_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_davesprite_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            show i_cousin_default_neutral as cousin
            t_ch_davesprite "hey again" # @t_sdavesprite20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "theres no point to reading any of this" # @t_sdavesprite21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "you already did the first event with me" # @t_sdavesprite22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "so youll probably just keep picking me over and over" # @t_sdavesprite23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_smile as davesprite
            t_ch_davesprite "which is obviously the right decision" # @t_sdavesprite24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Huh?? I still can’t quite follow you…" # @t_sdavesprite25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Awfully sure I’ll “pick you” again though, huh?" # @t_sdavesprite26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Is that ironic confidence, or real confidence?" # @t_sdavesprite26.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_shrug_disinterest as davesprite
            t_ch_davesprite "you dont have to pick me again you can pick someone else" # @t_sdavesprite27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "i mean that works pretty well" # @t_sdavesprite28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_shrug_eyebrow as davesprite
            t_ch_davesprite "if you dont want to get to the true ending with me that is" # @t_sdavesprite29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "maybe thats not your scene whatever i dont judge" # @t_sdavesprite210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            t_ch_cousin "“True ending”??" # @t_sdavesprite211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I… I don’t… what does that mean?" # @t_sdavesprite212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_davesprite "dont worry about it pick whoever you want" # @t_sdavesprite213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "pretty much everyone would be better than me" # @t_sdavesprite214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "my whole thing is kinda ridiculous" # @t_sdavesprite215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I don’t know, Davesprite." # @t_sdavesprite216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            extend " As weird as you are… there’s something about you that’s kinda cool, too." # @t_sdavesprite216.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_eyebrow as davesprite
            t_ch_davesprite "yeah yeah keep it in your pants [slot_playerName]" # @t_sdavesprite217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "i get it" # @t_sdavesprite218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_shrug_disinterest as davesprite
            t_ch_davesprite "we did one event together so now were otp forever" # @t_sdavesprite219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "thats cool i guess" # @t_sdavesprite220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "“OTP”?" # @t_sdavesprite221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            extend " Ogling… Tiny… Presents?" # @t_sdavesprite221.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_neutral as cousin
            extend " Overly… Terrific… Pigeon?!" # @t_sdavesprite221.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_mortified as cousin
            extend " Ornery… Tiger… Prancing??!!" # @t_sdavesprite221.03 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_defeated_disinterest as davesprite
            t_ch_davesprite "what" # @t_sdavesprite222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " no" # @t_sdavesprite222.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " jesus" # @t_sdavesprite222.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "i could troll you on this but its already sad enough so whats the point" # @t_sdavesprite223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " it would be a slam dunk but like way too easy so it doesnt count" # @t_sdavesprite223.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_eyebrow as davesprite
            t_ch_davesprite "its just a phrase that means were a couple now" # @t_sdavesprite224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            extend " relax" # @t_sdavesprite224.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised_blush as cousin
            t_ch_cousin "A… couple?" # @t_sdavesprite225.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_surprise as cousin
            extend " I-I don’t know about-" # @t_sdavesprite225.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "OHHH… I get it now!" # @t_sdavesprite226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "“OTP”..." # @t_sdavesprite227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            extend " “Only Two People”." # @t_sdavesprite227.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_eyebrow as davesprite
            t_ch_davesprite "yup thats it" # @t_sdavesprite228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "thats exactly what it means" # @t_sdavesprite229.00 self.block='Last'
            jump s_day2_davesprite_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_davesprite_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_davesprite_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            show i_cousin_default_neutral as cousin
            t_ch_davesprite "why are you clicking on me again" # @t_sdavesprite230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "you already talked to me" # @t_sdavesprite231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "dont you have stuff to do" # @t_sdavesprite232.00 self.block='Last'
            jump s_day2_davesprite_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_davesprite_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_davesprite_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_davesprite_standing_disinterest as davesprite
            t_ch_cousin "Hey, Davesprite. Still completely insane?" # @t_sdavesprite233.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "yeah gonna ignore that" # @t_sdavesprite234.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_shrug_disinterest as davesprite
            t_ch_davesprite "ok so this is the part where i catch you up to speed on what would have happened if you picked me for the first event" # @t_sdavesprite235.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "that way it can be all seamless if you want to switch characters" # @t_sdavesprite236.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_eyebrow as davesprite
            t_ch_davesprite "well i guess its not completely seamless but whatever" # @t_sdavesprite237.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "like if you do taira and blue max at the same time" # @t_sdavesprite238.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_eyebrow as davesprite
            t_ch_davesprite "whoah" # @t_sdavesprite239.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "tonal shift" # @t_sdavesprite240.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "Yep, still insane!" # @t_sdavesprite241.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            extend " I’d ask how that’s going for you, but…" # @t_sdavesprite241.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "I kinda want to leave you alone forever now!" # @t_sdavesprite242.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_eyebrow as davesprite
            show i_cousin_default_neutral as cousin
            t_ch_davesprite "hey words hurt buddy" # @t_sdavesprite243.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "okay if you had picked me on club day id have told you more about my stuff as a game guide" # @t_sdavesprite244.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "which will just go over your head like it is right now" # @t_sdavesprite245.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_shrug_disinterest as davesprite
            t_ch_davesprite "total waste of excellent exposition in my opinion" # @t_sdavesprite246.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "Yeah, clearly I’m the one who’s dumb for not understanding your gibberish." # @t_sdavesprite247.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_sad as davesprite
            t_ch_davesprite "anyway you start to think that im hiding behind this elaborate game metaphor so i dont have to deal with real emotions like my crippling insecurity and stuff" # @t_sdavesprite248.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_davesprite "which is really condescending of you by the way" # @t_sdavesprite249.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "like" # @t_sdavesprite250.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "you hang out with me for exactly one day" # @t_sdavesprite251.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_eyebrow as davesprite
            t_ch_davesprite "bam suddenly youre an expert on all my glaring character flaws" # @t_sdavesprite252.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "of which i have many but thats irrelevant" # @t_sdavesprite253.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_smile as davesprite
            t_ch_davesprite "oh also we made some terrible webcomics together" # @t_sdavesprite254.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(This guy… It’s hard to make heads or tails of what he’s saying, but…" # @t_sdavesprite255.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " When he talks about his “insecurity” or his “crippling flaws”..." # @t_sdavesprite255.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_neutral as cousin
            t_ch_cousin "It’s the first time I’ve seen real emotion cross his face." # @t_sdavesprite256.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_mortified as cousin
            extend " At least, I think I see that… It’s hard to tell." # @t_sdavesprite256.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_neutral as cousin
            t_ch_cousin "There must be something real there, making him feel that way.)" # @t_sdavesprite257.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_sad as davesprite
            t_ch_davesprite "huh yeah youre kinda right" # @t_sdavesprite258.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_defeated_disinterest as davesprite
            t_ch_davesprite "damn thats a pretty sadly accurate summary of my whole pointless existence" # @t_sdavesprite259.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_defeated_sad as davesprite
            t_ch_davesprite "harsh" # @t_sdavesprite260.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "oh well at least youre totally into me now because of all my trouble and angst" # @t_sdavesprite261.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Huh??" # @t_sdavesprite262.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " (It’s almost as if Davesprite could see my thoughts just now…" # @t_sdavesprite262.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            extend " No, that’s impossible.)" # @t_sdavesprite262.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_shrug_disinterest as davesprite
            t_ch_davesprite "yeah so that should pretty much catch you up to speed" # @t_sdavesprite263.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "you got a tantalizing peek into the twisted psyche of some dude" # @t_sdavesprite264.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_smile as davesprite
            t_ch_davesprite "your mouth is watering to get a little more of that action i bet" # @t_sdavesprite265.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_davesprite "even though im not even a real dude just like a copy of a dude mixed with a crow who came from a video game that destroys the world" # @t_sdavesprite266.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "anyway yeah were pretty much done here but if you want my true ending stick with me" # @t_sdavesprite267.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_shrug_disinterest as davesprite
            t_ch_davesprite "or not i dont really care" # @t_sdavesprite268.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            t_ch_cousin "(Davesprite… He seems crazy, but he has a strange internal logic." # @t_sdavesprite269.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_neutral as cousin
            extend " He obviously needs help, though… That much is clear." # @t_sdavesprite269.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Maybe… maybe I could be the one to give it to him.)" # @t_sdavesprite270.00 self.block='Last'
            jump s_day2_davesprite_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_davesprite_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_davesprite_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite
            show i_cousin_default_neutral as cousin
            t_ch_davesprite "why are you clicking on me again" # @t_sdavesprite230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "you already talked to me" # @t_sdavesprite231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_davesprite "dont you have stuff to do" # @t_sdavesprite232.00 self.block='Last'
            jump s_day2_davesprite_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_davesprite_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_davesprite_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_davesprite_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide davesprite
                # Pass (ActorReset)
                $ scene_picked_once_davesprite = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'donko', 'kind': 'Macro'} ''>
    label s_day2_donko:
        # <Macro Macro {'name': 'donko', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_donko_day1} && !${scene:picked_once_donko}', 'name': '_0', 'path': 'donko/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_donko_day1 and not scene_picked_once_donko:
            jump s_day2_donko_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_donko_day1} &&  ${scene:picked_once_donko}', 'name': '_1', 'path': 'donko/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_donko_day1 and  scene_picked_once_donko:
            jump s_day2_donko_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_donko_day1} && !${scene:picked_once_donko}', 'name': '_2', 'path': 'donko/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_donko_day1 and not scene_picked_once_donko:
            jump s_day2_donko_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_donko_day1} &&  ${scene:picked_once_donko}', 'name': '_3', 'path': 'donko/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_donko_day1 and  scene_picked_once_donko:
            jump s_day2_donko_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_donko_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_donko_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_wink as donko zorder 2:
                    default
                    xpos 0.72 
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
            show i_donko_default_wink as donko
            t_ch_donko "Hi honey!" # @t_sdonko21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I hope you haven’t forgotten what I said, now!" # @t_sdonko21.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Um…" # @t_sdonko22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Which part?" # @t_sdonko22.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_akimbo_wink as donko
            t_ch_donko "The part where, if you like, tell a single solitary soul that you saw me crying…" # @t_sdonko23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "I’ll end your reputation at Namco High!" # @t_sdonko24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "Not even the TOTAL SOCIAL REJECTS will hang out with you!" # @t_sdonko25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Haha… Okay, okay…" # @t_sdonko26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            extend " You seem like someone who’s not to be crossed." # @t_sdonko26.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_ygg_grin as donko
            t_ch_donko "I knew you could be taught!" # @t_sdonko27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "Let’s see now…" # @t_sdonko28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " How should we begin making you totally popular?" # @t_sdonko28.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "It’s gonna be hard, but…" # @t_sdonko29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I like, never EVER back down from a challenge!" # @t_sdonko29.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_default_wink as donko
            t_ch_donko "That’s one of my many many charms." # @t_sdonko210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "I dunno…" # @t_sdonko211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Couldn’t you just… tell everyone that I’m really cool, or something?" # @t_sdonko211.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "If you’re SO popular, shouldn’t your recommendation make ME popular too?" # @t_sdonko212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_default_meloncholic_blush as donko
            t_ch_donko "Oh, [slot_playerName]. So totally, like, naive." # @t_sdonko213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " You have no idea how popularity works in the real world!!" # @t_sdonko213.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_default_grin as donko
            t_ch_donko "I’m starting to get an idea, though…" # @t_sdonko214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "How attached are you to that outfit, by the way?" # @t_sdonko215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Just, like, for curiosity’s sake!" # @t_sdonko215.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "M-my outfit?" # @t_sdonko216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I… I like it!" # @t_sdonko216.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "There’s nothing wrong with it, is there?" # @t_sdonko217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "Well, not EXACTLY… Tee hee!" # @t_sdonko218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_sad as cousin
            t_ch_cousin "I don’t like the sound of that." # @t_sdonko219.00 self.block='Last'
            jump s_day2_donko_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_donko_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_donko_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_phone_wink as donko zorder 2:
                    default
                    xpos 0.72 
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
            show i_donko_phone_wink as donko
            t_ch_donko "Hello? Oh hi, Miranda." # @t_sdonko220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_donko_phone_wink as donko
            extend " Hey, do you think [slot_playerName] is more of a summer or a winter?" # @t_sdonko220.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Yeah, I’m talking about that dorky new kid…" # @t_sdonko220.02 self.block='Last'
            jump s_day2_donko_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_donko_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_donko_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_wink as donko zorder 2:
                    default
                    xpos 0.72 
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
            show i_donko_default_wink as donko
            t_ch_donko "Hi honey!" # @t_sdonko221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Did you have fun in your new club?" # @t_sdonko221.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I hope you picked a really cool one!" # @t_sdonko221.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "Since you’re new at Namco High, being seen in a really cool club could, like, do wonders for your reputation." # @t_sdonko222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Well, I’m sure my club isn’t as cool as yours." # @t_sdonko223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "…" # @t_sdonko224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_default_grin as donko
            t_ch_donko "...Duh!" # @t_sdonko225.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " The club I’m in HAS to be cool,because I’m in it!" # @t_sdonko225.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Is it just me…" # @t_sdonko226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Or did Donko seem a little… defensive?)" # @t_sdonko226.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "...Yknow honey, I’ve been thinking…" # @t_sdonko227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_ygg_wink as donko
            t_ch_donko "You may not be much now, but you’ve got potential." # @t_sdonko228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " If you play your cards right, you could drum up a lot of popularity here at Namco High!" # @t_sdonko228.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "Of course, you’d need someone who’s already popular to take you under their wing…" # @t_sdonko229.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Someone like…" # @t_sdonko229.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "ME!" # @t_sdonko230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Wait…" # @t_sdonko231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Are you saying that you’ll…" # @t_sdonko231.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Teach me to be popular?" # @t_sdonko232.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "I dunno about that, Donko." # @t_sdonko233.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I’m not really the… “popular” type." # @t_sdonko233.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_akimbo_grin as donko
            t_ch_donko "Whaaat?" # @t_sdonko234.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "Anyone can be popular!" # @t_sdonko235.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " It’s just like any skill, like music or something…" # @t_sdonko235.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_donko "You just have to like, work SUPER hard at it!" # @t_sdonko236.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Uh…" # @t_sdonko237.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I guess so, but…" # @t_sdonko237.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Oh, it doesn’t even matter what I say now, does it?" # @t_sdonko238.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "You’ve already decided…" # @t_sdonko239.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_akimbo_wink as donko
            t_ch_donko "Tee-hee!" # @t_sdonko240.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " You’re getting to know me pretty well, honey!" # @t_sdonko240.01 self.block='Last'
            jump s_day2_donko_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_donko_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_donko_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_phone_wink as donko zorder 2:
                    default
                    xpos 0.72 
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
            show i_donko_phone_wink as donko
            t_ch_donko "Hello? Oh hi, Miranda." # @t_sdonko220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_donko_phone_wink as donko
            extend " Hey, do you think [slot_playerName] is more of a summer or a winter?" # @t_sdonko220.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Yeah, I’m talking about that dorky new kid…" # @t_sdonko220.02 self.block='Last'
            jump s_day2_donko_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_donko_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_donko_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_phone_wink as donko:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_donko_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide donko
                # Pass (ActorReset)
                $ scene_picked_once_donko = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'galaga', 'kind': 'Macro'} ''>
    label s_day2_galaga:
        # <Macro Macro {'name': 'galaga', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_galaga_day1} && !${scene:picked_once_galaga}', 'name': '_0', 'path': 'galaga/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_galaga_day1 and not scene_picked_once_galaga:
            jump s_day2_galaga_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_galaga_day1} &&  ${scene:picked_once_galaga}', 'name': '_1', 'path': 'galaga/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_galaga_day1 and  scene_picked_once_galaga:
            jump s_day2_galaga_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_galaga_day1} && !${scene:picked_once_galaga}', 'name': '_2', 'path': 'galaga/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_galaga_day1 and not scene_picked_once_galaga:
            jump s_day2_galaga_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_galaga_day1} &&  ${scene:picked_once_galaga}', 'name': '_3', 'path': 'galaga/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_galaga_day1 and  scene_picked_once_galaga:
            jump s_day2_galaga_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_galaga_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_galaga_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_galaga_default as galaga zorder 2:
                    default
                    xpos 0.77 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_galaga_default as galaga
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Hey, uh, Galaga Ship." # @t_sgalaga20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}Hm? Oh, hey, [slot_playerName].{/smallcaps}" # @t_sgalaga21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            with Dissolve(0.5)
            t_ch_cousin "(It’s so aloof!)" # @t_sgalaga22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I was just wondering if you’d seen Aki around." # @t_sgalaga23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}Hm? Not sure. Don’t think so.{/smallcaps}" # @t_sgalaga24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "(Barely paying attention to me!)" # @t_sgalaga25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_surprise as cousin
            t_ch_cousin "Well, uh, y’know. If she’s not around, then you can’t rehearse your lines because she’s playing Romeo because the director wanted that different take after seeing mine even though he didn’t see the other one but that Tomari is a little weird don’t you think I think so and anyway you need to rehearse I mean it’s not that you’re bad or anything but rehearsing is good for everyone and I’m just thinking that since I’m the understudy for Romeo and if Romeo isn’t around then you should maybe probably kinda think about rehearsing with me for your own good wow did that sound like a threat it sounded like a threat to me and I’m the guy who said it but huh it’s kinda weird I haven’t taken a breath this whole time right?" # @t_sgalaga26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " (Oops, lost track of what was coming outta my mouth, but I feel like it was pretty charming!)" # @t_sgalaga26.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}…um?{/smallcaps}" # @t_sgalaga27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Uh-oh, must’ve dazzled Galaga Ship with all that charm!)" # @t_sgalaga28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}Yeah, um. Rehearsal is after school tomorrow.{/smallcaps}" # @t_sgalaga29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}I think that’s what you’re asking me about?{/smallcaps}" # @t_sgalaga210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}It was kind of hard to understand.{/smallcaps}" # @t_sgalaga211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_grin as cousin
            t_ch_cousin "Hahahahaahaaha....haaaaaaa" # @t_sgalaga212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Okay, yeah. Rehearsing is cool." # @t_sgalaga212.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Be cool, [slot_playerName].)" # @t_sgalaga213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Maybe I can help out tomorrow! Maybe..." # @t_sgalaga214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Yeah, just be super casual. Maybe lean against this wall. Yeah, real cool, [slot_playerName].)" # @t_sgalaga215.00 self.block='Last'
            jump s_day2_galaga_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_galaga_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_galaga_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_galaga_default as galaga zorder 2:
                    default
                    xpos 0.77 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_galaga "{smallcaps}Don’t know how I’m gonna get these lines down in time.{/smallcaps}" # @t_sgalaga242.00 self.block='Last'
            jump s_day2_galaga_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_galaga_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_galaga_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_galaga_script as galaga zorder 2:
                    default
                    xpos 0.77 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_galaga "{smallcaps}mumble MUMBLE mutter mumble.{/smallcaps}" # @t_sgalaga221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Galaga Ship’s awfully engrossed in whatever it’s reading…)" # @t_sgalaga222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Hm, looks like a script book?)" # @t_sgalaga223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Oh! For Drama Club I guess.)" # @t_sgalaga224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}~Sigh~{/smallcaps}" # @t_sgalaga225.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}I’m never gonna get this monologue down.{/smallcaps}" # @t_sgalaga226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Hm?" # @t_sgalaga227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}Oh, New Kid.{/smallcaps}" # @t_sgalaga228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}Sorry. Just a little frustrated with the play.{/smallcaps}" # @t_sgalaga229.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}Aki never makes it to rehearsal, so I’m a little at sea.{/smallcaps}" # @t_sgalaga230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_galaga "{smallcaps}And that’s, like, WAY worse when you’re a spaceship.{/smallcaps}" # @t_sgalaga231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Well... maybe I could help?" # @t_sgalaga232.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I can read all kinds of words." # @t_sgalaga233.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_galaga "{smallcaps}Oh? Oh!{/smallcaps}" # @t_sgalaga234.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Maybe...that could be fun..." # @t_sgalaga235.00 self.block='Last'
            jump s_day2_galaga_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_galaga_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_galaga_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_galaga_default as galaga zorder 2:
                    default
                    xpos 0.77 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_galaga "{smallcaps}Don’t know how I’m gonna get these lines down in time.{/smallcaps}" # @t_sgalaga242.00 self.block='Last'
            jump s_day2_galaga_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_galaga_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_galaga_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_galaga_default as galaga:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_galaga_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide galaga
                # Pass (ActorReset)
                $ scene_picked_once_galaga = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'hiromi', 'kind': 'Macro'} ''>
    label s_day2_hiromi:
        # <Macro Macro {'name': 'hiromi', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_hiromi_day1} && !${scene:picked_once_hiromi}', 'name': '_0', 'path': 'hiromi/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_hiromi_day1 and not scene_picked_once_hiromi:
            jump s_day2_hiromi_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_hiromi_day1} &&  ${scene:picked_once_hiromi}', 'name': '_1', 'path': 'hiromi/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_hiromi_day1 and  scene_picked_once_hiromi:
            jump s_day2_hiromi_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_hiromi_day1} && !${scene:picked_once_hiromi}', 'name': '_2', 'path': 'hiromi/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_hiromi_day1 and not scene_picked_once_hiromi:
            jump s_day2_hiromi_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_hiromi_day1} &&  ${scene:picked_once_hiromi}', 'name': '_3', 'path': 'hiromi/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_hiromi_day1 and  scene_picked_once_hiromi:
            jump s_day2_hiromi_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_hiromi_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_hiromi_didEventFirst_warm:
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
            t_ch_cousin "Hey Hiromi!" # @t_shiromi20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_hiromi "Hey, kid." # @t_shiromi21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Collect any good data?" # @t_shiromi22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_akimbo_smile as hiromi
            t_ch_hiromi "Lots." # @t_shiromi23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "And how's your, uh, data collection partner?" # @t_shiromi24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_crossed_straight_blush as hiromi
            t_ch_hiromi "Sh-she's good..." # @t_shiromi25.00 self.block='Last'
            jump s_day2_hiromi_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_hiromi_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_hiromi_didEventLoop_warm:
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
            t_ch_hiromi "Hey Hiromi! I’m glad you got all the data you needed." # @t_shiromi25.00a self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "………………………..." # @t_shiromi25.00b self.block='Last'
            jump s_day2_hiromi_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_hiromi_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_hiromi_didntEventFirst_warm:
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
            show i_cousin_default_neutral as cousin
            show i_hiromi_stand_serious as hiromi
            t_ch_cousin "Hi Hiromi!" # @t_shiromi26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_hiromi "Hey." # @t_shiromi27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "What'd you get up to yesterday?" # @t_shiromi28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_crossed_serious as hiromi
            t_ch_hiromi "I collected data." # @t_shiromi29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_crossed_straight_blush as hiromi
            t_ch_hiromi "with my data collection partner.." # @t_shiromi210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Data collection partner……...." # @t_shiromi211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_akimbo_serious as hiromi
            t_ch_hiromi "Shut up, kid." # @t_shiromi212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "Er..." # @t_shiromi213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(So she's a little sensitive about it!)" # @t_shiromi214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin ".... What's 'collect data' mean?" # @t_shiromi215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_hiromi_stand_serious as hiromi
            t_ch_hiromi "Better that I show you." # @t_shiromi216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(She doesn't seem like the scientist type... I wonder what it means... )" # @t_shiromi217.00 self.block='Last'
            jump s_day2_hiromi_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_hiromi_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_hiromi_didntEventLoop_warm:
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
            t_ch_cousin "Hey Hiromi! Want help collecting data?" # @t_shiromi218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_hiromi "…………..sure." # @t_shiromi219.00 self.block='Last'
            jump s_day2_hiromi_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_hiromi_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_hiromi_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_hiromi_stand_serious as hiromi:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_hiromi_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide hiromi
                # Pass (ActorReset)
                $ scene_picked_once_hiromi = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'jane', 'kind': 'Macro'} ''>
    label s_day2_jane:
        # <Macro Macro {'name': 'jane', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_jane_day1} && !${scene:picked_once_jane}', 'name': '_0', 'path': 'jane/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_jane_day1 and not scene_picked_once_jane:
            jump s_day2_jane_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_jane_day1} &&  ${scene:picked_once_jane}', 'name': '_1', 'path': 'jane/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_jane_day1 and  scene_picked_once_jane:
            jump s_day2_jane_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_jane_day1} && !${scene:picked_once_jane}', 'name': '_2', 'path': 'jane/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_jane_day1 and not scene_picked_once_jane:
            jump s_day2_jane_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_jane_day1} &&  ${scene:picked_once_jane}', 'name': '_3', 'path': 'jane/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_jane_day1 and  scene_picked_once_jane:
            jump s_day2_jane_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_jane_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_jane_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_smile as jane zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_cousin_default_grin as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            show i_jane_default_smile as jane
            t_ch_cousin "Hi there Jane! Investigated any mysteries lately?" # @t_sjane230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_handonhip_grin as jane
            t_ch_jane "Hoo hoo! Only the mystery of what a great journalist I am! ;B" # @t_sjane231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Yeah, that IS a real mystery!" # @t_sjane232.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_laugh as cousin
            t_ch_cousin "Ohhh! Burn!" # @t_sjane233.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_laugh as jane
            t_ch_jane "Dag nabbit. You took my excellent burn and turned it right back around against me!" # @t_sjane234.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_smile as jane
            t_ch_jane "How perfectly diabolical." # @t_sjane235.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " [slot_playerName], you have the makings of a pranking mastermind." # @t_sjane235.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Hmm, would you even go so far as to say that my burn was so good it was…" # @t_sjane236.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            extend " almost SUPERNATURAL?!" # @t_sjane236.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_grin as jane
            t_ch_jane "Nope. ;B" # @t_sjane237.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Darn! I thought I’d had ya!" # @t_sjane238.00 self.block='Last'
            jump s_day2_jane_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_jane_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_jane_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_frustrated as jane zorder 2:
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
            show i_jane_default_frustrated as jane
            show i_cousin_default_neutral as cousin
            t_ch_jane "Shoosh, [slot_playerName]! Leave me alone!" # @t_sjane239.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I’m plotting our next journalistic expedition!" # @t_sjane239.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_laugh as cousin
            t_ch_cousin "Haha, alright. Plot away!" # @t_sjane240.00 self.block='Last'
            jump s_day2_jane_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_jane_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_jane_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_grin as jane zorder 2:
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
            t_ch_jane "Helloooo, [slot_playerName]! :B" # @t_sjane20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Hi Jane! Did you have fun on Club Day?" # @t_sjane21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_jane "I sure did! I’m the editor of the school newspaper, and not to toot my own horn, but I happen to be pleased as punch with the headline I came up with for yesterday!" # @t_sjane22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_handonhip_grin as jane
            t_ch_jane "Here, take a look!" # @t_sjane23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "“Tater Tots a Hit in the School Cafeteria”??" # @t_sjane24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_handonhip_smile as jane
            t_ch_jane "We cite several credible sources to back that up, too!" # @t_sjane25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_mortified as cousin
            t_ch_cousin "...Jane…" # @t_sjane26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "There’s so much weird stuff going on at this school…" # @t_sjane27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            extend " Even the students and teachers are WAY out of the ordinary!" # @t_sjane27.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Couldn’t you have come up with something more exciting to report on?" # @t_sjane28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_smile as jane
            t_ch_jane "[slot_playerName], don’t be so ridiculous." # @t_sjane29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_jane "A good newspaper reports on the facts, and only the facts!!!" # @t_sjane210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " You don’t really expect me to believe something so silly as, say, a talking cat in our very own class, do you?!" # @t_sjane210.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_jane "Believe me, all that nonsense is the stuff of pranks and hoaxes." # @t_sjane211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I’m surprised a smart cookie like yourself would fall for it!" # @t_sjane211.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "What about those weird friends you hang around with?!" # @t_sjane212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_jane "Who? You mean Terezi and Davesprite?" # @t_sjane213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_grin as jane
            extend " They’re a lovely pair of chums, sure! But I don’t see how they have anything to do with this!" # @t_sjane213.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "One’s a big orange floaty bird guy, and the other has gray skin and horns!!!" # @t_sjane214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_frustrated as jane
            t_ch_jane "Sheesh! There’s no need to be rude!" # @t_sjane215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_smile as jane
            extend " They’re just… cosplay enthusiasts." # @t_sjane215.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "Are you sure about that?" # @t_sjane216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_jane "…" # @t_sjane217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_grin as jane
            show i_cousin_default_neutral as cousin
            t_ch_jane "[slot_playerName]… if you don’t mind me saying so, we should do some hanging out soon!" # @t_sjane218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_handonhip_laugh as jane
            t_ch_jane "For one thing, I’ll be happy to try to disprove some of your ridiculous notions! :B" # @t_sjane219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            with Dissolve(.333)
            t_ch_cousin "(Well, it isn’t like I’d really mind spending time with a cute girl like her…" # @t_sjane220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin_blush as cousin
            extend " And maybe… I… shall be the one… to do the notion-disproving!)" # @t_sjane220.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Let’s see what else is in this school paper of yours…" # @t_sjane221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "“Mustaches are Totally Hot: An Editorial by Jane Crocker?!”" # @t_sjane222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_laugh_blush as jane
            t_ch_jane "HOO HOO! Yes! Well! Um!" # @t_sjane223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_grin_blush as jane
            t_ch_jane "That certainly is a thing I wrote! Ahem. …" # @t_sjane224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_armscrossed_laugh_blush as jane
            t_ch_jane "Ahahahaha!" # @t_sjane225.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            t_ch_cousin "(...I wonder where I could get a fake mustache to wear.)" # @t_sjane226.00 self.block='Last'
            jump s_day2_jane_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_jane_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_jane_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_grin_blush as jane zorder 2:
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
            show i_jane_default_grin_blush as jane
            show i_cousin_default_neutral as cousin
            t_ch_jane "You have to admit, [slot_playerName], that when it comes to attractive facial hair…" # @t_sjane227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_jane "Mustaches are just the tops!" # @t_sjane228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(I don’t have to admit anything of the sort!)" # @t_sjane229.00 self.block='Last'
            jump s_day2_jane_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_jane_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_jane_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_grin_blush as jane:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_mortified as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_jane_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide jane
                # Pass (ActorReset)
                $ scene_picked_once_jane = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'lolo', 'kind': 'Macro'} ''>
    label s_day2_lolo:
        # <Macro Macro {'name': 'lolo', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_lolo_day1} && !${scene:picked_once_lolo}', 'name': '_0', 'path': 'lolo/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_lolo_day1 and not scene_picked_once_lolo:
            jump s_day2_lolo_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_lolo_day1} &&  ${scene:picked_once_lolo}', 'name': '_1', 'path': 'lolo/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_lolo_day1 and  scene_picked_once_lolo:
            jump s_day2_lolo_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_lolo_day1} && !${scene:picked_once_lolo}', 'name': '_2', 'path': 'lolo/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_lolo_day1 and not scene_picked_once_lolo:
            jump s_day2_lolo_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_lolo_day1} &&  ${scene:picked_once_lolo}', 'name': '_3', 'path': 'lolo/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_lolo_day1 and  scene_picked_once_lolo:
            jump s_day2_lolo_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_lolo_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_lolo_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_lolo_crossed_raisedbrow as lolo
            t_ch_cousin "Hi, Lolo." # @t_slolo223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_lolo "Hey. I thought you weren’t gonna waste your time with me." # @t_slolo224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Oh… did you mean that as like, a serious thing?" # @t_slolo225.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I thought it was more of a… wistful… self-deprecating phrase…" # @t_slolo225.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_frustrated as lolo
            t_ch_lolo "...Fine, whatever. Hang out if you want." # @t_slolo226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I could care less." # @t_slolo226.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_sad as cousin
            t_ch_cousin "(Jeez, all I did was say hi!" # @t_slolo227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "She’s sorta protesting too much...)" # @t_slolo228.00 self.block='Last'
            jump s_day2_lolo_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_lolo_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_lolo_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_lolo_crossed_raisedbrow as lolo zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            show i_lolo_crossed_raisedbrow as lolo
            t_ch_cousin "…" # @t_slolo221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_raisedbrow as lolo
            t_ch_lolo "Quit staring." # @t_slolo222.00 self.block='Last'
            jump s_day2_lolo_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_lolo_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_lolo_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_lolo_crossed_raisedbrow as lolo zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_raisedbrow as lolo
            show i_cousin_default_grin as cousin
            t_ch_lolo "Hey [slot_playerName]. You look cheery today." # @t_slolo20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " It’s annoying." # @t_slolo20.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Um… sorry??" # @t_slolo21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I was just gonna ask how your club day went." # @t_slolo21.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_lolo "It was pretty dumb. I’m in Yearbook Club." # @t_slolo22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_frustrated as lolo
            extend " I only joined because I knew it wouldn’t take any effort." # @t_slolo22.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Aw, that sounds kinda fun, actually!" # @t_slolo23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_default_frustrated as lolo
            t_ch_lolo "You would think that, wouldn’t you." # @t_slolo24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_lolo "I guess it’s okay, it’s just… so pathetic." # @t_slolo25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Everyone always writes “keep in touch” in their yearbooks, but no one ever does…" # @t_slolo25.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Just like how no one ever calls when they say they will, or writes when they move away." # @t_slolo25.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_lolo "And if you do ever see them again, you find out they have a new friend who’s just like you but different." # @t_slolo26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " That’s just how it always goes." # @t_slolo26.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_neutral as cousin
            t_ch_cousin "Not… always…" # @t_slolo27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_raisedbrow as lolo
            t_ch_lolo "Yes. Always." # @t_slolo28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " If it could happen with my friend Klonoa and me…" # @t_slolo28.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_lolo "It could happen to anyone." # @t_slolo29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Huh? Who’s Klonoa?" # @t_slolo210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_frustrated as lolo
            t_ch_lolo "Someone from another life… back when I was stupid enough to think I could actually study magic and become a priestess and go on adventures…" # @t_slolo211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " How childish is that?" # @t_slolo211.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_lolo "Anyway… it’s none of your business." # @t_slolo212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Um… Okay…" # @t_slolo213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Well, at least when you get a yearbook, you get a nice picture of yourself to remember your time?" # @t_slolo214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I mean, at least you have that, right?" # @t_slolo214.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_shrug_grin as lolo
            t_ch_lolo "Heh. Why would I want a picture of myself? To remind me of how ugly I was in high school?" # @t_slolo215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "What?! You’re not ugly at all!" # @t_slolo216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_grin as lolo
            t_ch_lolo "...You’re a real goody-two-shoes, [slot_playerName]." # @t_slolo217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_frustrated as lolo
            t_ch_lolo "You shouldn’t hang out with me. I’ll just disappoint you." # @t_slolo218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(She says she picked Yearbook Club because it was easy…" # @t_slolo219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " But it also seems like the perfect embodiment of things she despises." # @t_slolo219.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Did she join because she hates herself or something?! Lolo, what's the deal?)" # @t_slolo220.00 self.block='Last'
            jump s_day2_lolo_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_lolo_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_lolo_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_lolo_crossed_raisedbrow as lolo zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            show i_lolo_crossed_raisedbrow as lolo
            t_ch_cousin "…" # @t_slolo221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_raisedbrow as lolo
            t_ch_lolo "Quit staring." # @t_slolo222.00 self.block='Last'
            jump s_day2_lolo_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_lolo_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_lolo_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_raisedbrow as lolo:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_grin as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_lolo_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide lolo
                # Pass (ActorReset)
                $ scene_picked_once_lolo = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'meowkie', 'kind': 'Macro'} ''>
    label s_day2_meowkie:
        # <Macro Macro {'name': 'meowkie', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_meowkie_day1} && !${scene:picked_once_meowkie}', 'name': '_0', 'path': 'meowkie/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_meowkie_day1 and not scene_picked_once_meowkie:
            jump s_day2_meowkie_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_meowkie_day1} &&  ${scene:picked_once_meowkie}', 'name': '_1', 'path': 'meowkie/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_meowkie_day1 and  scene_picked_once_meowkie:
            jump s_day2_meowkie_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_meowkie_day1} && !${scene:picked_once_meowkie}', 'name': '_2', 'path': 'meowkie/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_meowkie_day1 and not scene_picked_once_meowkie:
            jump s_day2_meowkie_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_meowkie_day1} &&  ${scene:picked_once_meowkie}', 'name': '_3', 'path': 'meowkie/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_meowkie_day1 and  scene_picked_once_meowkie:
            jump s_day2_meowkie_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_meowkie_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_meowkie_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_king_confident as king zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                show i_meowkie_normal_happy_badge as meowkie zorder 2:
                    default
                    xpos 0.7 
                    xzoom -1.0 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_king_confident as king
            show i_meowkie_normal_happy_badge as meowkie
            show i_cousin_default_grin as cousin
            t_ch_meowkie "Oh, hi Boss!" # @t_smeowkie20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I can’t wait to go patrolling with you again!" # @t_smeowkie20.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_forcedsmile_badge as meowkie
            t_ch_meowkie "...Nya! Er! That is!" # @t_smeowkie21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Not specifically with YOU or nothin’..." # @t_smeowkie21.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "I just like patrolling..." # @t_smeowkie22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_forcedsmile_badge as meowkie
            extend " Haha... oh, jeez..." # @t_smeowkie22.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "..You did have fun though, right Boss?" # @t_smeowkie23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_laugh as cousin
            t_ch_cousin "Haha! Of course I did!" # @t_smeowkie24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I can’t wait to go patrolling with you again, either." # @t_smeowkie24.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_happy_badge as meowkie
            t_ch_meowkie "R-really…?" # @t_smeowkie25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " That’s… the nicest thing anybody’s ever said to me…" # @t_smeowkie25.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Haha… Oh, come on…" # @t_smeowkie26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "No, I mean it…" # @t_smeowkie27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I really mean it." # @t_smeowkie27.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "‘Specially after I told you all about…" # @t_smeowkie28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_frown_badge as meowkie
            t_ch_meowkie "Y’know, where I come from and all…" # @t_smeowkie29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " And you haven’t said a word about it against me, or nothin’ like that…" # @t_smeowkie29.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "You’re… really nice, Boss." # @t_smeowkie210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Of course I haven’t!" # @t_smeowkie211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Meowkie, anyone who’d treat you differently because of that is a real jerk!" # @t_smeowkie211.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "…" # @t_smeowkie212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_forcedsmile_badge as meowkie
            extend " Ha ha…" # @t_smeowkie212.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "Yeah…. you’re right…" # @t_smeowkie213.00 self.block='Last'
            jump s_day2_meowkie_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_meowkie_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_meowkie_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
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
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_forcedsmile_badge as meowkie
            show i_cousin_default_neutral as cousin
            t_ch_meowkie "Boss, I ain’t got too many friends here…" # @t_smeowkie214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I’m glad you wanna hang out with me." # @t_smeowkie214.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(How can MEOWKIE of all people not have many friends?" # @t_smeowkie215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " She’s cute, she’s nice, she’s a CAT…" # @t_smeowkie215.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " People love cats, according to the Internet!" # @t_smeowkie215.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Maybe it has to do with where she comes from…" # @t_smeowkie216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I better not push it too much, though.)" # @t_smeowkie217.00 self.block='Last'
            jump s_day2_meowkie_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_meowkie_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_meowkie_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_king_confident as king zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                show i_meowkie_akimbo_normal_badge as meowkie zorder 2:
                    default
                    xpos 0.7 
                    xzoom -1.0 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            show i_meowkie_akimbo_normal_badge as meowkie
            t_ch_cousin "Hi Meowkie!" # @t_smeowkie218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_normal_badge as meowkie
            t_ch_meowkie "Oh, hiya Boss!" # @t_smeowkie219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " One second, okay?" # @t_smeowkie219.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_normal_badge as meowkie:
                linear .25 xzoom 1.0 
                # ShowWithAtl
                linear .333 xpos 0.35 
            show i_cousin_default_surprised as cousin:
                # ShowWithAtl
                linear .333 xpos 0.15 
            show i_king_confident as king:
                # ShowWithAtl
                linear .5 alpha 1.0
                xzoom 1.0 
                # ShowWithAtl
                linear 0.5 xpos 0.8 
            extend "{w=0.5}{nw}"
            t_ch_meowkie "Bye bye, King! Seeya tomorrow!" # @t_smeowkie220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            play sound "sfx/kingroar1.ogg"
            t_ch_king "(See you tomorrow Miss Meowkie…)" # @t_smeowkie221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            play sound "sfx/kingroar2.ogg"
            show i_king_screaming as king
            t_ch_king "(IN THE RING!!!)" # @t_smeowkie222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_king_confident as king:
                # ShowWithAtl
                pause 0.7 
                linear .5 alpha 0.0
            extend "{w=1.2}{nw}"
            t_ch_king "(Just kidding!)" # @t_smeowkie223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_happy_badge as meowkie:
                linear .25 xzoom -1.0 
                # ShowWithAtl
                linear .25 xpos 0.7 
            show i_cousin_default_surprised as cousin:
                # ShowWithAtl
                linear .333 xpos 0.3 
            extend "{w=0.333}{nw}"
            t_ch_meowkie "Heh heh! That King is pretty funny, huh?" # @t_smeowkie224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " So, didja find a good club yesterday?" # @t_smeowkie224.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Um… huh? Yeah yeah, the club was great…" # @t_smeowkie225.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "But, what the heck?" # @t_smeowkie226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_surprised as cousin
            extend " Meowkie, are you actually FRIENDS with that scary guy King?!" # @t_smeowkie226.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_normal_badge as meowkie
            t_ch_meowkie "Oh yeah. He ain’t too bad, actually." # @t_smeowkie227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " He’s always real nice to me!" # @t_smeowkie227.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "As a Hall Monitor, I gotta report to him every day." # @t_smeowkie228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "That’s right, you’re a hall monitor!" # @t_smeowkie229.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Hey, maybe I could go on patrol with you sometime!" # @t_smeowkie229.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            extend " I keep thinking that might be kinda fun." # @t_smeowkie229.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_forcedsmile_badge as meowkie
            t_ch_meowkie "...R-really Boss?" # @t_smeowkie230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "You’d wanna… hang out with me?" # @t_smeowkie231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Uh… yeah! Sure, why not?" # @t_smeowkie232.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "Boss…" # @t_smeowkie233.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_frown_badge as meowkie
            extend " There’s somethin’ I oughta tell you." # @t_smeowkie233.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Uh oh…)" # @t_smeowkie234.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "See, my family…" # @t_smeowkie235.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Well, my parents are…" # @t_smeowkie235.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_slouch_frown_badge as meowkie
            t_ch_meowkie "They’re bad guys." # @t_smeowkie236.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "Not even important bad guys or nothin’..." # @t_smeowkie237.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Just goons, you know?" # @t_smeowkie237.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "They used to work for a REALLY bad guy. We called him “The Big Cat” at home…" # @t_smeowkie238.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "But, they didn’t want me to have that life." # @t_smeowkie239.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " They moved here to this neighborhood, so I could go to Namco High and…" # @t_smeowkie239.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_forcedsmile_badge as meowkie
            t_ch_meowkie "And not grow up to be a bad guy." # @t_smeowkie240.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_frown_badge as meowkie
            t_ch_meowkie "But it’s in my blood, kinda… so… now you know." # @t_smeowkie241.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "I understand if you don’t wanna hang out no more..." # @t_smeowkie242.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Meowkie…" # @t_smeowkie243.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Thanks for telling me, but…" # @t_smeowkie243.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "I don’t care where you come from!" # @t_smeowkie244.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " You’re always really nice and helpful." # @t_smeowkie244.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Don’t worry about that, okay?" # @t_smeowkie245.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I still want to hang out, if you do." # @t_smeowkie245.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_forcedsmile_badge as meowkie
            t_ch_meowkie "…" # @t_smeowkie246.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "Boss… I…" # @t_smeowkie247.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_happy_badge as meowkie
            t_ch_meowkie "...I really wanna hang out, too." # @t_smeowkie248.00 self.block='Last'
            jump s_day2_meowkie_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_meowkie_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_meowkie_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_meowkie_normal_happy_badge as meowkie zorder 2:
                    default
                    xpos 0.7 
                    xzoom -1.0 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "So, I gotta know…" # @t_smeowkie249.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "What’s the deal with King?" # @t_smeowkie250.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_normal_normal_badge as meowkie
            t_ch_meowkie "Huh? Whaddya mean, “what’s the deal”?" # @t_smeowkie251.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "You know… what’s he like!" # @t_smeowkie252.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Does he have any crazy secrets?" # @t_smeowkie252.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_meowkie "I dunno, Boss." # @t_smeowkie253.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " He’s a big wrestling guy with a jaguar head." # @t_smeowkie253.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_grin_badge as meowkie
            extend " Pretty self-explanatory." # @t_smeowkie253.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_neutral as cousin
            t_ch_cousin "Aw, man..." # @t_smeowkie254.00 self.block='Last'
            jump s_day2_meowkie_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_meowkie_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_meowkie_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_king_confident as king:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_meowkie_akimbo_grin_badge as meowkie:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_exhausted_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_meowkie_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide king
                hide meowkie
                # Pass (ActorReset)
                $ scene_picked_once_meowkie = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'mrdriller', 'kind': 'Macro'} ''>
    label s_day2_mrdriller:
        # <Macro Macro {'name': 'mrdriller', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_mrdriller_day1} && !${scene:picked_once_mrdriller}', 'name': '_0', 'path': 'mrdriller/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_mrdriller_day1 and not scene_picked_once_mrdriller:
            jump s_day2_mrdriller_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_mrdriller_day1} &&  ${scene:picked_once_mrdriller}', 'name': '_1', 'path': 'mrdriller/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_mrdriller_day1 and  scene_picked_once_mrdriller:
            jump s_day2_mrdriller_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_mrdriller_day1} && !${scene:picked_once_mrdriller}', 'name': '_2', 'path': 'mrdriller/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_mrdriller_day1 and not scene_picked_once_mrdriller:
            jump s_day2_mrdriller_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_mrdriller_day1} &&  ${scene:picked_once_mrdriller}', 'name': '_3', 'path': 'mrdriller/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_mrdriller_day1 and  scene_picked_once_mrdriller:
            jump s_day2_mrdriller_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_mrdriller_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_mrdriller_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_mrdriller_slumped_happy as mrdriller zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_slumped_happy as mrdriller
            show i_cousin_default_neutral as cousin
            t_ch_mrdriller "Hi again, Digging Partner!" # @t_smrdriller20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(He called me his... partner…)" # @t_smrdriller21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_drillup_happy as mrdriller
            t_ch_mrdriller "Thank you so much again for what you did for me the other day." # @t_smrdriller22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I don’t know what I did to deserve such support…" # @t_smrdriller22.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "I’m so proud to have brought digging to Namco High with our amazing, groundbreaking club." # @t_smrdriller23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "(How could we have brought digging to Namco High if we’re the only ones in the digging club?" # @t_smrdriller24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Doesn’t that just mean we brought digging to ourselves?" # @t_smrdriller24.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "...Oh. “Groundbreaking”." # @t_smrdriller25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Heh heh. I get it.)" # @t_smrdriller26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_drillup_smug as mrdriller
            t_ch_mrdriller "The old man hasn’t said anything to me about the club…" # @t_smrdriller27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_drillup_happy as mrdriller
            extend " So we’re free to dig again tomorrow! I can’t wait!" # @t_smrdriller27.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "Haha! He’s probably too depressed about his terrible life decisions to notice even a single thing his own son is doing!" # @t_smrdriller28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "Ha! Ha! Hahaha! Ha!" # @t_smrdriller29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "...Er…" # @t_smrdriller210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_slumped_excited as mrdriller
            t_ch_mrdriller "So I’ll see you at Digging Club tomorrow, right? Right?!" # @t_smrdriller211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(This seems like a lot of drama to get myself involved in." # @t_smrdriller212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Maybe I should find a way to weasel out.)" # @t_smrdriller213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "After all, [slot_playerName]…" # @t_smrdriller214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_slumped_happy as mrdriller
            t_ch_mrdriller "I need you there." # @t_smrdriller215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_slumped_happy as mrdriller
            t_ch_mrdriller "You’re the only one who…" # @t_smrdriller216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_drillup_happy as mrdriller
            t_ch_mrdriller "Whose presence qualifies us as an official club, on a technicality." # @t_smrdriller217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            t_ch_cousin "(...Or maybe I could give it one more shot.)" # @t_smrdriller218.00 self.block='Last'
            jump s_day2_mrdriller_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_mrdriller_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_mrdriller_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_mrdriller_slumped_happy as mrdriller zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_mrdriller "Hey [slot_playerName], you said you had no real interest in drilling or digging before the club…" # @t_smrdriller219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_slumped_smug as mrdriller
            extend " Are you sure there wasn’t some other reason you joined?" # @t_smrdriller219.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            t_ch_cousin "(Oh no… Is my little crush THAT obvious?!)" # @t_smrdriller220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_drillup_excited as mrdriller
            t_ch_mrdriller "Like for example… maybe the FATES THEMSELVES are guiding you into a previously unrecognized lifelong passion for digging?!!" # @t_smrdriller221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Because that would be THE COOLEST!!!" # @t_smrdriller223.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Um… Yeah, it’s probably…" # @t_smrdriller224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " ...something along those lines." # @t_smrdriller224.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " (Actually, it’s probably a little more like… a Tunnel of Love.)" # @t_smrdriller224.02 self.block='Last'
            jump s_day2_mrdriller_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_mrdriller_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_mrdriller_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_mrdriller_drillup_happy as mrdriller zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_mrdriller_standing_happy as mrdriller
            t_ch_mrdriller "Hey [slot_playerName]. Did you find a good club to join?" # @t_smrdriller225.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "I’m not sure yet… but club day sure was interesting anyway." # @t_smrdriller226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_standing_confused as mrdriller
            t_ch_mrdriller "Yeah yeah that’s great. Unfortunately MY proposal for a club was rejected…" # @t_smrdriller227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Can you believe that? Not one person wanted to dig with me!" # @t_smrdriller227.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "It just doesn’t make sense. Maybe they misunderstood me and thought I said “Jigging Club” or something." # @t_smrdriller228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(I can’t decide which of those awful club ideas sounds less fun.)" # @t_smrdriller229.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_standing_happy as mrdriller
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Mr. Driller… why do you love digging so much anyway?" # @t_smrdriller230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "Are you kidding?! Digging is amazing!" # @t_smrdriller231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "It’s not just the fun of working hard and using cool power tools." # @t_smrdriller232.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " It’s the thrill of discovery…" # @t_smrdriller232.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "Every time I go on a dig, I find something new, or uncover something old that I never knew had always been there…" # @t_smrdriller233.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " There’s a whole world under the ground everyone walks on, waiting to be discovered." # @t_smrdriller233.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_drillup_excited as mrdriller
            t_ch_mrdriller "It’s the best feeling in the whole world." # @t_smrdriller234.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "That does sound pretty cool, actually." # @t_smrdriller235.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_slumped_cry as mrdriller
            t_ch_mrdriller "Yeah… too bad I’ll never be able to do it again, now that my club is rejected and my terrible father won’t let me…" # @t_smrdriller236.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_standing_confused as mrdriller
            t_ch_mrdriller "Dads, huh? Don’t you wish you could dig into their heads and find out what’s in there?" # @t_smrdriller237.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_standing_happy as mrdriller
            extend " Haha! Lots and lots of hate and bitterness, probably! Am I right?" # @t_smrdriller237.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(Um… Yikes…)" # @t_smrdriller238.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_drillup_happy as mrdriller
            t_ch_mrdriller "Of course, you shouldn’t dig into their heads LITERALLY…" # @t_smrdriller239.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_standing_happy as mrdriller
            t_ch_mrdriller "That would mess them up pretty bad!" # @t_smrdriller240.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " And we don’t want to do that, even if it’s only natural to think about it all the time!" # @t_smrdriller240.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "Oh, I don’t have to tell you. I guess its pretty typical parent stuff!" # @t_smrdriller241.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "…" # @t_smrdriller242.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Wow, Mr. Driller… I had no idea you hated Principal Dig Dug so much." # @t_smrdriller243.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_slumped_shock as mrdriller
            t_ch_mrdriller "Whoah, whoah! I don’t HATE my dad!" # @t_smrdriller244.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " No way! Uh uh! Where’d you dig up THAT crazy idea?!" # @t_smrdriller244.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "He’s family after all…" # @t_smrdriller245.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_standing_happy as mrdriller
            extend " And family’s more valuable than any treasure you could ever excavate!" # @t_smrdriller245.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "...Although I don’t know for sure since that wretch won’t ever let me excavate anything again." # @t_smrdriller246.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Uh huh… Well…" # @t_smrdriller247.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Good luck with that…" # @t_smrdriller247.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(He’s cute, but kinda crazy." # @t_smrdriller248.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Still, when he talks about digging, it’s hard not to be inspired by his passion…" # @t_smrdriller249.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I kinda felt that way about rolling my katamari…" # @t_smrdriller249.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "But that’s way too much trouble to ever try doing again." # @t_smrdriller250.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Anyway..." # @t_smrdriller251.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Maybe it wouldn’t be so bad to hang around with Mr. Driller sometime.)" # @t_smrdriller251.01 self.block='Last'
            jump s_day2_mrdriller_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_mrdriller_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_mrdriller_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.25 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_mrdriller_drillup_happy as mrdriller zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_drillup_happy as mrdriller
            show i_cousin_default_neutral as cousin
            t_ch_cousin "So, Mr. Driller, what’s your very FAVORITE part about drilling?" # @t_smrdriller252.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "Oh man! There’s way too many great things about drilling to list!" # @t_smrdriller253.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_mrdriller "But I’ll list them anyway." # @t_smrdriller254.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_sw_black as curtain zorder 9:
                # FadeEvent
                linear 0.3 alpha 1.0
            $ renpy.pause(0.3, hard=True) # TimedPause
            narrator "TWENTY MINUTES LATER." # @t_smrdriller2_splash0 self.block='NoAuto'
            # Blank text event <TextEvent TextEvent {'auto': 'true', 'char': '', 'name': '_6', 'text': '', 'kind': 'TextEvent'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_sw_black as curtain zorder 15:
                # FadeEvent
                linear 0.3 alpha 0.0
            $ renpy.pause(0.3, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_mortified as cousin
            t_ch_mrdriller "And another thing that’s great about drilling is the sheer variety of bits available in the market today…" # @t_smrdriller255.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(I’m…" # @t_smrdriller256.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            extend " Sorry I asked…)" # @t_smrdriller256.01 self.block='Last'
            jump s_day2_mrdriller_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_mrdriller_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_mrdriller_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_mrdriller_drillup_happy as mrdriller:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_mortified as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_mrdriller_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide mrdriller
                # Pass (ActorReset)
                $ scene_picked_once_mrdriller = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'nidia', 'kind': 'Macro'} ''>
    label s_day2_nidia:
        # <Macro Macro {'name': 'nidia', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_nidia_day1} && !${scene:picked_once_nidia}', 'name': '_0', 'path': 'nidia/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_nidia_day1 and not scene_picked_once_nidia:
            jump s_day2_nidia_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_nidia_day1} &&  ${scene:picked_once_nidia}', 'name': '_1', 'path': 'nidia/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_nidia_day1 and  scene_picked_once_nidia:
            jump s_day2_nidia_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_nidia_day1} && !${scene:picked_once_nidia}', 'name': '_2', 'path': 'nidia/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_nidia_day1 and not scene_picked_once_nidia:
            jump s_day2_nidia_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_nidia_day1} &&  ${scene:picked_once_nidia}', 'name': '_3', 'path': 'nidia/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_nidia_day1 and  scene_picked_once_nidia:
            jump s_day2_nidia_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_nidia_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_nidia_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_nidia_notepad_happy as nidia zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_notepad_happy as nidia
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Hi Nidia! What're you writing?" # @t_snidia20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "Oh! I'm making some notes for today! Tomari helped me devise a Personality Compatibility Matrix." # @t_snidia21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " If you still have time to help, of course." # @t_snidia21.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "(Wow, she's really serious about this!)" # @t_snidia22.00 self.block='Last'
            jump s_day2_nidia_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_nidia_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_nidia_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_nidia_notepad_happy as nidia zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "The Personality Compatibility Matrix that Tomari devised is very complicated, but I think I get it." # @t_snidia29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Something about quadrants… ?" # @t_snidia29.00a self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "I hope you have time to come by Magic Club tomorrow, [slot_playerName]…" # @t_snidia29.00b self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I could really use your help!" # @t_snidia29.00c self.block='Last'
            jump s_day2_nidia_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_nidia_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_nidia_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_nidia_notepad_worried as nidia zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_notepad_worried as nidia
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Hi Nidia! What's up?" # @t_snidia23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "Well... I can use an amulet to combine with someone" # @t_snidia24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " and turn into a dragon" # @t_snidia24.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_clasped_worried as nidia
            extend " and it's my destiny to use that power to save the world!" # @t_snidia24.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "But lately I haven't been able to find anyone to combine with." # @t_snidia25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "That's why I'm using this Personality Compatibility Matrix that Tomari put together for me! He really seems to like helping me..." # @t_snidia26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_notepad_happy as nidia
            t_ch_nidia "Anyway, on a completely unrelated note..." # @t_snidia27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Do you think you could help me out tomorrow?" # @t_snidia27.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Only if you're not busy!" # @t_snidia27.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I'll explain at Magic Club! Just come find me behind the magic veil in the library!" # @t_snidia27.03 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "(Wow... That's a lot to blurt out at once. Maybe I should see what's up with her...)" # @t_snidia28.00 self.block='Last'
            jump s_day2_nidia_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_nidia_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_nidia_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_nidia_notepad_happy as nidia zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "The Personality Compatibility Matrix that Tomari devised is very complicated, but I think I get it." # @t_snidia29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Something about quadrants… ?" # @t_snidia29.00a self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_nidia "I hope you have time to come by Magic Club tomorrow, [slot_playerName]…" # @t_snidia29.00b self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I could really use your help!" # @t_snidia29.00c self.block='Last'
            jump s_day2_nidia_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_nidia_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_nidia_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_nidia_notepad_happy as nidia:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_nidia_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide nidia
                # Pass (ActorReset)
                $ scene_picked_once_nidia = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'richard', 'kind': 'Macro'} ''>
    label s_day2_richard:
        # <Macro Macro {'name': 'richard', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_richard_day1} && !${scene:picked_once_richard}', 'name': '_0', 'path': 'richard/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_richard_day1 and not scene_picked_once_richard:
            jump s_day2_richard_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_richard_day1} &&  ${scene:picked_once_richard}', 'name': '_1', 'path': 'richard/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_richard_day1 and  scene_picked_once_richard:
            jump s_day2_richard_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_richard_day1} && !${scene:picked_once_richard}', 'name': '_2', 'path': 'richard/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_richard_day1 and not scene_picked_once_richard:
            jump s_day2_richard_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_richard_day1} &&  ${scene:picked_once_richard}', 'name': '_3', 'path': 'richard/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_richard_day1 and  scene_picked_once_richard:
            jump s_day2_richard_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_richard_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_richard_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_miller_akimbo_halfgrin as miller zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_akimbo_halfgrin as miller
            show i_cousin_default_neutral as cousin
            t_ch_richard "[slot_playerName]!" # @t_srichard20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_richard "munchamunch" # @t_srichard21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_akimbo_serious as miller
            t_ch_richard "Glad you’re here!" # @t_srichard22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_richard "muncha" # @t_srichard23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Where else would I be? It’s detention, it’s not like I’ve got a choice!)" # @t_srichard24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_neutral as cousin
            extend " Hi, Richard. You seem...eating." # @t_srichard24.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_akimbo_laugh as miller
            t_ch_richard "It’s these cupcakes!" # @t_srichard25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_akimbo_serious as miller
            t_ch_richard "muncha" # @t_srichard26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_akimbo_laugh as miller
            t_ch_richard "THEY’VE GOT FLAVOR!" # @t_srichard27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_mortified as cousin
            t_ch_cousin "(Oh, dear. What have I done?)" # @t_srichard28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_richard "Anyway, I need your help." # @t_srichard29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_surprised as cousin
            t_ch_cousin "Oh? So, what, I introduce you to cupcakes and that’s the end of the dossier stuff?" # @t_srichard210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_richard "Ha! No, you’ll be getting stakeout-ed too." # @t_srichard211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_richard "Uh, staked-out, uh, on." # @t_srichard212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_standing_contemplative as miller
            t_ch_richard "Um." # @t_srichard213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_standing_halfgrin as miller
            t_ch_richard "I’ll be keeping an eye on you." # @t_srichard214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_aliens_serious as miller
            t_ch_richard "NO ONE is above suspicion." # @t_srichard215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_richard "I even track my own movements just in case I can’t be trusted either." # @t_srichard216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_akimbo_shocked as miller
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Uh, okay. How would that work though?)" # @t_srichard223.00 self.block='Last'
            jump s_day2_richard_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_richard_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_richard_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_miller_akimbo_halfgrin as miller zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " You okay, Richard?" # @t_srichard223.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_pondering_serious as miller
            t_ch_richard "Never better!" # @t_srichard224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_richard "I’ve got a lead. It could be the final piece of the pie at the heart of this puzzle." # @t_srichard225.00 self.block='Last'
            jump s_day2_richard_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_richard_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_richard_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_miller_akimbo_halfgrin as miller zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_miller_akimbo_shocked as miller
            t_ch_richard "WHERE WERE YOU ON THE NIGHT OF THE SEVENTEENTH?!" # @t_srichard217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_mortified as cousin
            t_ch_cousin "(What is with this guy?)" # @t_srichard218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            extend " Me?" # @t_srichard218.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_akimbo_contemplative as miller
            t_ch_richard "Correct." # @t_srichard219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Uh, okay. I don’t know. Which seventeenth?" # @t_srichard220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_akimbo_shocked as miller
            t_ch_richard "We’ll start with the last one." # @t_srichard221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_richard "AND GO BACKWARDS FROM THERE." # @t_srichard222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_akimbo_shocked as miller
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Uh, okay. How would that work though?)" # @t_srichard223.00 self.block='Last'
            jump s_day2_richard_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_richard_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_richard_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_miller_akimbo_halfgrin as miller zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " You okay, Richard?" # @t_srichard223.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_pondering_serious as miller
            t_ch_richard "Never better!" # @t_srichard224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_richard "I’ve got a lead. It could be the final piece of the pie at the heart of this puzzle." # @t_srichard225.00 self.block='Last'
            jump s_day2_richard_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_richard_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_richard_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_miller_pondering_serious as miller:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_richard_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide miller
                # Pass (ActorReset)
                $ scene_picked_once_richard = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'taira', 'kind': 'Macro'} ''>
    label s_day2_taira:
        # <Macro Macro {'name': 'taira', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_taira_day1} && !${scene:picked_once_taira}', 'name': '_0', 'path': 'taira/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_taira_day1 and not scene_picked_once_taira:
            jump s_day2_taira_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_taira_day1} &&  ${scene:picked_once_taira}', 'name': '_1', 'path': 'taira/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_taira_day1 and  scene_picked_once_taira:
            jump s_day2_taira_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_taira_day1} && !${scene:picked_once_taira}', 'name': '_2', 'path': 'taira/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_taira_day1 and not scene_picked_once_taira:
            jump s_day2_taira_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_taira_day1} &&  ${scene:picked_once_taira}', 'name': '_3', 'path': 'taira/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_taira_day1 and  scene_picked_once_taira:
            jump s_day2_taira_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_taira_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_taira_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_steveholt_happy as taira zorder 2:
                    default
                    xpos 0.7 
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
            show i_taira_steveholt_happy as taira
            show i_cousin_default_neutral as cousin
            t_ch_taira "Yo, Cuz! You’re lookin’ pretty good today!" # @t_staira20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Haha. You don’t like to give it a rest with the flirting, huh Taira?" # @t_staira21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_steveholt_pleading as taira
            t_ch_taira "Wha! Oh, n-no!" # @t_staira22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_steveholt_confused_blush as taira
            extend " I just meant you’re like… healed and stuff after gettin’ hurt at the game yesterday!" # @t_staira22.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "...But you also look mad cute anyway!" # @t_staira23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_akimbo_confused_blush as taira
            t_ch_taira "YO, STOP TRYING TO MESS ME UP WITH YOUR BRAIN TEASERS, CUZ!" # @t_staira24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Ha! Don’t worry, I’m just teasing." # @t_staira25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Yeah, I went to the nurse’s office and they fixed me up with a health potion." # @t_staira26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " This school is pretty cool…" # @t_staira26.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_akimbo_happy as taira
            t_ch_taira "WOO!" # @t_staira27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_akimbo_happy as taira
            extend " Yeah, that RULES!" # @t_staira27.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "Does that mean you’re all set to play Wrestleball again for the next match?!" # @t_staira28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Uh…" # @t_staira29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Um…" # @t_staira29.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I dunno, Taira…" # @t_staira29.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Maybe it’d be cool to just… hang out, instead?" # @t_staira210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_akimbo_confused as taira
            t_ch_taira "…" # @t_staira211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_steveholt_happy as taira
            t_ch_taira "YOOOO!" # @t_staira212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " That’s a WAY more awesome idea!" # @t_staira212.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "You and me, Cuz! Hangin’ out!" # @t_staira213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Rad! I’m holdin’ ya to it!" # @t_staira213.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Me and my big mouth…" # @t_staira214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Couldn’t I have thought of a better excuse?!" # @t_staira214.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "Like… LITERALLY ANYTHING ELSE?)" # @t_staira215.00 self.block='Last'
            jump s_day2_taira_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_taira_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_taira_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_steveholt_happy as taira zorder 2:
                    default
                    xpos 0.7 
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
            t_ch_taira "WHOO! HANGING OUT RULES!" # @t_staira216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "Haha… yeahhhh." # @t_staira217.00 self.block='Last'
            jump s_day2_taira_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_taira_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_taira_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_steveholt_happy as taira zorder 2:
                    default
                    xpos 0.7 
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
            show i_taira_steveholt_happy as taira
            t_ch_taira "Yo! Hey, Cuz!" # @t_staira218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " What club did you pick?" # @t_staira218.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Well, I-" # @t_staira219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "Whatever it is, there’s no WAY it’s as cool as the Wrestleball team!" # @t_staira220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_steveholt_serious as taira
            extend " How come you didn’t join, yo? You trying to hurt my feelings?!" # @t_staira220.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_revenge_serious as taira
            t_ch_taira "I got mad revenge on the other team- you know, revenge for my clan and stuff?- and won the game singlehandedly!" # @t_staira221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " HAW HAW! It was awesome! Plus my muscles looked totally hot!" # @t_staira221.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised_blush as cousin
            t_ch_cousin "Wh-what makes you think I’d want to see that?!" # @t_staira222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " (Seriously?! I’m blushing over THIS GUY?!" # @t_staira222.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            extend " And what’s the deal with the clan thing?)" # @t_staira222.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_revenge_happy as taira
            t_ch_taira "Of course, if you wanna date me, you can see my muscles ALL THE TIME!" # @t_staira223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "Maybe I could even help you bulk up a bit!" # @t_staira224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " You obviously need it! HAW!" # @t_staira224.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Whoah whoah whoah-" # @t_staira225.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised_blush as cousin
            extend " You actually want to DATE me?!" # @t_staira225.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_default_confused as taira
            t_ch_taira "Uh, yeah, Cuz. Was that like, not clear?" # @t_staira226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_default_confused_blush as taira
            t_ch_taira "You’re like… totally the coolest and really smart and stuff…" # @t_staira227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " And really nice! And all that other stuff…" # @t_staira227.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "Haw! Look, you’re even making me go all EMOTIONS on you." # @t_staira228.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_steveholt_confused_blush as taira
            t_ch_taira "ME! A TOTALLY RAD UNDEAD WARRIOR BRO!" # @t_staira229.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            t_ch_cousin "I dunno about this, Taira… And anyway, I’m not so good at sports." # @t_staira230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_default_serious as taira
            t_ch_taira "Yeah, but you don’t gotta be good at somethin’ to like it!" # @t_staira231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "That’s what’s cool about doin’ stuff you love…" # @t_staira232.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " You can do it even if you totally SUCK at it!" # @t_staira232.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_taira "And if anybody ever tells you different…" # @t_staira233.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_revenge_revenge as taira
            extend " I’ll get revenge on em for ya and PULVERIZE em!" # @t_staira233.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "...Huh!" # @t_staira234.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "(Wow, Taira is actually… not that bad." # @t_staira235.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " He’s even kind of deep…" # @t_staira235.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "What’s up with the revenge thing, though?" # @t_staira236.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " There’s gotta be a story there…" # @t_staira236.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Anyway, maybe it wouldn’t be so bad to hang out with him.)" # @t_staira237.00 self.block='Last'
            jump s_day2_taira_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_taira_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_taira_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_serious as taira zorder 2:
                    default
                    xpos 0.7 
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
            show i_taira_akimbo_serious as taira
            t_ch_taira "So what’s your favorite part of revenge?" # @t_staira238.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "...Oh gee, how can I possible choose. Probably… all of it?" # @t_staira239.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_akimbo_happy as taira
            t_ch_taira "NO WAY! ME TOO!" # @t_staira240.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "..." # @t_staira241.00 self.block='Last'
            jump s_day2_taira_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_taira_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_taira_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_happy as taira:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_mortified as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_taira_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide taira
                # Pass (ActorReset)
                $ scene_picked_once_taira = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'terezi', 'kind': 'Macro'} ''>
    label s_day2_terezi:
        # <Macro Macro {'name': 'terezi', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_terezi_day1} && !${scene:picked_once_terezi}', 'name': '_0', 'path': 'terezi/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_terezi_day1 and not scene_picked_once_terezi:
            jump s_day2_terezi_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_terezi_day1} &&  ${scene:picked_once_terezi}', 'name': '_1', 'path': 'terezi/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_terezi_day1 and  scene_picked_once_terezi:
            jump s_day2_terezi_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_terezi_day1} && !${scene:picked_once_terezi}', 'name': '_2', 'path': 'terezi/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_terezi_day1 and not scene_picked_once_terezi:
            jump s_day2_terezi_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_terezi_day1} &&  ${scene:picked_once_terezi}', 'name': '_3', 'path': 'terezi/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_terezi_day1 and  scene_picked_once_terezi:
            jump s_day2_terezi_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_terezi_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_terezi_didEventFirst_warm:
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
            show i_terezi_default_grin as terezi
            show i_cousin_default_neutral as cousin
            t_ch_terezi "SOOOO COTTON C4NDY" # @t_sterezi229.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "G1V3N 4NY MOR3 THOUGHT TO MY L1TTL3 PROPOS4L?" # @t_sterezi230.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "TH3 W34PON’S LOCK3R 1S R1GHT TH3R3" # @t_sterezi231.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "YOU COULD BR34K 1N R1GHT NOW 4ND G3T TH4T T4STY R41NBOW DONUT TR34T ST4RT3D 4G41N >:P" # @t_sterezi232.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_surprise as cousin
            t_ch_cousin "N-no! There’s no WAY I’m gonna do that!" # @t_sterezi233.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Stop asking me!!" # @t_sterezi233.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "H3H3H3H3 YOU S4Y TH4T NOW" # @t_sterezi234.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_grin as terezi
            t_ch_terezi "BUT 1 H4V3 W4YS W1TH P3OPL3’S M1NDS" # @t_sterezi235.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_laugh as terezi
            t_ch_terezi "YOUR M1ND 1N P4RT1CUL4R 1S L1K3 4 GRUBS’ PL4YTH1NG TO M3" # @t_sterezi236.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_grin as terezi
            t_ch_terezi "TH3R3’S SO M4NY P4THS YOU COULD CHOOS3" # @t_sterezi237.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "SO M4NY W4YS YOU COULD TH1NK TO GO" # @t_sterezi238.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_laugh as terezi
            t_ch_terezi "BUT TH3Y 4LL 3ND W1TH YOU DO1NG 3X4CTLY WH4T 1 W4NT >:P" # @t_sterezi239.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_neutral as cousin
            t_ch_cousin "…" # @t_sterezi240.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_grin as terezi
            t_ch_terezi "…" # @t_sterezi241.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_mortified as cousin
            t_ch_cousin "...You don’t really expect me to buy a load like that, do you?" # @t_sterezi242.00 self.block='Last'
            jump s_day2_terezi_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_terezi_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_terezi_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_terezi_lean_grin as terezi zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_grin as terezi
            show i_cousin_default_neutral as cousin
            t_ch_terezi "H3H3H3" # @t_sterezi243.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_laugh as terezi
            t_ch_terezi "H3H3H3H3H3H3 <3" # @t_sterezi244.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(I can’t tell if that giggle of hers is cute…" # @t_sterezi245.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            extend " ...Or just kinda creepy.)" # @t_sterezi245.01 self.block='Last'
            jump s_day2_terezi_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_terezi_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_terezi_didntEventFirst_warm:
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
            show i_terezi_default_grin as terezi
            show i_cousin_default_neutral as cousin
            t_ch_terezi "H3Y COTTON C4NDY" # @t_sterezi20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_huh as terezi
            extend " 1’V3 GOT 4 “HUM4N BON3” TO “P1CK” W1TH YOU!" # @t_sterezi20.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_grin as terezi
            t_ch_terezi "...TH4T’S 4N 3XPR3SS1ON YOU GUYS US3 R1GHT?" # @t_sterezi21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(I don’t know, I’m not really human…" # @t_sterezi22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            extend " Whatever, roll with it.)" # @t_sterezi22.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Uh… sure. What’s up, Terezi? Did I do something wrong?" # @t_sterezi23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_huh as terezi
            t_ch_terezi "UM DUUUUHHH" # @t_sterezi24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "YOU D1DN’T JO1N TH3 CR1M1N4L JUST1C3 CLUB W1TH M3 >:P" # @t_sterezi25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_default_grin as terezi
            t_ch_terezi "J33Z YOU’R3 SUCH 4 LOS3R" # @t_sterezi26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_default_laugh as terezi
            t_ch_terezi "JUST L1K3 MY OLD P4RTN3R!" # @t_sterezi27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "“Old partner”?! Who’s that?!" # @t_sterezi28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_default_resigned as terezi
            t_ch_terezi "1T DO3SN’T M4TT3R 4NYMOR3 NOW" # @t_sterezi29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "H3’S LONG GON3" # @t_sterezi210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_grin as terezi
            t_ch_terezi "UNL1K3 TH3 ST1NK OF CR1M3 TH4T L1NG3RS ON YOU" # @t_sterezi211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "H3H3H3H3 >:]" # @t_sterezi212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_surprise as cousin
            t_ch_cousin "What?! You mean the crime of… rolling up everything in my katamari ball?" # @t_sterezi213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_mortified as cousin
            extend " It was sort of an accident… And anyway, I’ll never do it again." # @t_sterezi213.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_default_grin as terezi
            t_ch_terezi "YOU S4Y TH4T BUT 1 C4N T3LL YOU’R3 JUST 4CH1NG TO G1V3 1T 4NOTH3R GO" # @t_sterezi214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "ROLL1NG UP 4LL TH3 COLORS OF TH3 SCHOOL… 3V3RY S1NGL3 HU3…" # @t_sterezi215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_default_laugh as terezi
            t_ch_terezi "1NTO 4 G14NT D3L1C1OUS R41NBOW-SPR1NKL3D DONUT TR34T!" # @t_sterezi216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "1T’S 1RR3S1ST4BL3! MY MOUTH 1S W4T3R1NG JUST TH1NK1NG 4BOUT 1T" # @t_sterezi217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_default_grin as terezi
            t_ch_terezi "SO YOU’R3 GONN4 DO 1T 4G41N R1GHT?!" # @t_sterezi218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_surprised as cousin
            t_ch_cousin "It sounds… almost like you WANT me to do it again?!" # @t_sterezi219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "H3H3H3 WH4T G4V3 YOU TH4T 1D34" # @t_sterezi220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_exhausted_mortified as cousin
            t_ch_cousin "B-but that’s crazy! You’re in the Criminal Justice club!" # @t_sterezi221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Why would you actually want me to break rules?!" # @t_sterezi221.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_default_grin as terezi
            t_ch_terezi "1 DUNNO COTTON C4NDY" # @t_sterezi222.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_terezi "F1GUR3 1T OUT >:P" # @t_sterezi223.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_grin as terezi
            t_ch_terezi "S3R1OUSLY THOUGH 1 JUST LOV3 4LL THOS3 COLORS <3" # @t_sterezi224.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Hmm…" # @t_sterezi225.00 self.block='Last'
            jump s_day2_terezi_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_terezi_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_terezi_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_terezi_lean_grin as terezi zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_grin as terezi
            t_ch_terezi "YOU’R3 4BOUT TO BR34K TH3 RUL3S 4G41N…" # @t_sterezi226.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_lean_laugh as terezi
            extend " 1 C4N SM3LL 1T ON YOU! H3H3H3H3!" # @t_sterezi226.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_energetic_surprise as cousin
            t_ch_cousin "Y-you’re crazy! Get out of here!" # @t_sterezi227.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            t_ch_cousin "(Even though I know she can’t really see me with them, those gleaming red glasses are pretty scary…)" # @t_sterezi228.00 self.block='Last'
            jump s_day2_terezi_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_terezi_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_terezi_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_laugh as terezi:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_mortified as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_terezi_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide terezi
                # Pass (ActorReset)
                $ scene_picked_once_terezi = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'tomari', 'kind': 'Macro'} ''>
    label s_day2_tomari:
        # <Macro Macro {'name': 'tomari', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_tomari_day1} && !${scene:picked_once_tomari}', 'name': '_0', 'path': 'tomari/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_tomari_day1 and not scene_picked_once_tomari:
            jump s_day2_tomari_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_tomari_day1} &&  ${scene:picked_once_tomari}', 'name': '_1', 'path': 'tomari/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_tomari_day1 and  scene_picked_once_tomari:
            jump s_day2_tomari_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_tomari_day1} && !${scene:picked_once_tomari}', 'name': '_2', 'path': 'tomari/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_tomari_day1 and not scene_picked_once_tomari:
            jump s_day2_tomari_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_tomari_day1} &&  ${scene:picked_once_tomari}', 'name': '_3', 'path': 'tomari/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_tomari_day1 and  scene_picked_once_tomari:
            jump s_day2_tomari_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_tomari_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_tomari_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_notebook_thinking as tomari zorder 2:
                    default
                    xpos 0.72 
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
            show i_tomari_notebook_thinking as tomari
            t_ch_tomari "Oh, [slot_playerName]! I stayed up pretty late doing research into the stuff we’d have to research to to figure out what, EXACTLY, we should research." # @t_stomari20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Uh, wow. That’s a lot of researching." # @t_stomari21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_tomari_alive_smile as tomari
            t_ch_tomari "IT WAS GREAT!!!" # @t_stomari22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Huh, I’ve never seen Tomari this excited…)" # @t_stomari23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_tomari_pondering_smile as tomari
            t_ch_tomari "I’ll be in the library later. I could really use your help with the more difficult theories!" # @t_stomari24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Uh, yeah. My help. That’d be just great wouldn’t it." # @t_stomari25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin
            extend " (How long can I keep doing this?!)" # @t_stomari25.01 self.block='Last'
            jump s_day2_tomari_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_tomari_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_tomari_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_pondering_thinking as tomari zorder 2:
                    default
                    xpos 0.72 
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
            show i_tomari_pondering_thinking as tomari
            t_ch_tomari "I could use another pair of eyes on the research material I compiled. Maybe you'll have time tomorrow?" # @t_stomari220.00 self.block='Last'
            jump s_day2_tomari_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_tomari_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_tomari_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_defeated_thoughtful as tomari zorder 2:
                    default
                    xpos 0.72 
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
            show i_tomari_defeated_thoughtful as tomari
            t_ch_tomari "ZzZzZzZz…" # @t_stomari26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(Is this guy…)" # @t_stomari27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "(...SLEEPING THROUGH DETENTION???)" # @t_stomari28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " (Wish I thought of that.)" # @t_stomari28.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_tomari "Square root differential hypotenuse!" # @t_stomari29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Hey, Tomari. You’re talking in your sleep." # @t_stomari210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Wake up." # @t_stomari211.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            extend " I SAID WAKE UP!!!" # @t_stomari211.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_tomari_defeated_mortified as tomari
            t_ch_tomari "WHO WHAT WHERE???" # @t_stomari212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " Oh, [slot_playerName]." # @t_stomari212.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " YAWWWWWN." # @t_stomari212.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            show i_tomari_pondering_thinking as tomari
            t_ch_tomari "Must’ve dozed off. I stayed up all night researching." # @t_stomari213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_tomari "Not sure I’m getting anywhere with it though. Gonna have to skip a few more classes to do more research in the library." # @t_stomari214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_tomari_pondering_mortified as tomari
            t_ch_tomari "I could really use some help." # @t_stomari215.00 self.block='Last'
            jump s_day2_tomari_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_tomari_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_tomari_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_pondering_thinking as tomari zorder 2:
                    default
                    xpos 0.72 
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
            show i_tomari_pondering_thinking as tomari
            t_ch_tomari "I could use another pair of eyes on the research material I compiled. Maybe you'll have time tomorrow?" # @t_stomari220.00 self.block='Last'
            jump s_day2_tomari_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_tomari_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_tomari_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_tomari_pondering_thinking as tomari:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_tomari_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide tomari
                # Pass (ActorReset)
                $ scene_picked_once_tomari = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice
    # <Macro Macro {'name': 'valk', 'kind': 'Macro'} ''>
    label s_day2_valk:
        # <Macro Macro {'name': 'valk', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_valk_day1} && !${scene:picked_once_valk}', 'name': '_0', 'path': 'valk/didEventFirst', 'kind': 'BranchMacro'} ''>
        if slot_picked_valk_day1 and not scene_picked_once_valk:
            jump s_day2_valk_didEventFirst
        # <BranchMacro BranchMacro {'comparison': '${slot:picked_valk_day1} &&  ${scene:picked_once_valk}', 'name': '_1', 'path': 'valk/didEventLoop', 'kind': 'BranchMacro'} ''>
        if slot_picked_valk_day1 and  scene_picked_once_valk:
            jump s_day2_valk_didEventLoop
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_valk_day1} && !${scene:picked_once_valk}', 'name': '_2', 'path': 'valk/didntEventFirst', 'kind': 'BranchMacro'} ''>
        if not slot_picked_valk_day1 and not scene_picked_once_valk:
            jump s_day2_valk_didntEventFirst
        # <BranchMacro BranchMacro {'comparison': '!${slot:picked_valk_day1} &&  ${scene:picked_once_valk}', 'name': '_3', 'path': 'valk/didntEventLoop', 'kind': 'BranchMacro'} ''>
        if not slot_picked_valk_day1 and  scene_picked_once_valk:
            jump s_day2_valk_didntEventLoop
        # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
        label s_day2_valk_didEventFirst:
            # <Macro Macro {'name': 'didEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_valk_didEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_valkyrie_default_wink as valkyrie zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_default_wink as valkyrie
            show i_cousin_default_neutral as cousin
            t_ch_valkyrie "Hey cutie! Didja have fun yesterday?" # @t_svalk20.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            t_ch_cousin "I really did. I've never made anything before! Those sword thingies came out pretty cool." # @t_svalk21.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_grin as cousin
            extend " Although with the amount of help you gave me, I'm not sure I can take credit for it." # @t_svalk21.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Sorry I took up all your time!" # @t_svalk22.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_akimbo_grin as valkyrie
            t_ch_valkyrie "Hee hee. Don't worry about it." # @t_svalk23.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I didn't mind at all." # @t_svalk23.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_valkyrie "Actually..." # @t_svalk24.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " It was a lot of fun." # @t_svalk24.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_akimbo_grinblush as valkyrie
            with Dissolve(0.5)
            extend " You're a lot of fun." # @t_svalk24.02 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised_blush as cousin
            t_ch_cousin "(Oh man, am I blushing?)" # @t_svalk25.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_akimbo_wink as valkyrie
            t_ch_valkyrie "YOU'RE BLUSHING! CUTE! It’s like when I own a bad guy in battle, but instead it’s my heart." # @t_svalk26.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_laugh_blush as cousin
            t_ch_cousin "SH-SHUT UP!" # @t_svalk27.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            t_ch_cousin "(She seems pleased with herself... She really seems to like teasing me. In her case, that's probably a good sign.)" # @t_svalk28.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "........." # @t_svalk29.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin ".................." # @t_svalk210.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "(If I'm honest with myself... I'm kinda into it.)" # @t_svalk211.00 self.block='Last'
            jump s_day2_valk_cleanup
        # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
        label s_day2_valk_didEventLoop:
            # <Macro Macro {'name': 'didEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_valk_didEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_valkyrie_default_wink as valkyrie zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_valkyrie "Hey cutie! Maybe we can hang out tomorrow…" # @t_svalk222.00 self.block='Last'
            jump s_day2_valk_cleanup
        # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
        label s_day2_valk_didntEventFirst:
            # <Macro Macro {'name': 'didntEventFirst', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_valk_didntEventFirst_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_valkyrie_default_thoughtful as valkyrie zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_default_thoughtful as valkyrie
            show i_cousin_default_neutral as cousin
            t_ch_cousin "Hi Valkyrie!" # @t_svalk212.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_valkyrie "Hey cutie. What'd you get up to yesterday?" # @t_svalk213.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_cousin "Oh, you know... Stuff." # @t_svalk214.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_valkyrie "....." # @t_svalk215.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " ............" # @t_svalk215.01 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_default_wink as valkyrie
            t_ch_valkyrie "What a tiny, mysterious cutie." # @t_svalk216.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral_blush as cousin
            t_ch_cousin "(A-am I blushing? Be cool [slot_playerName]... )" # @t_svalk217.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin
            t_ch_cousin "So, uh, what'd YOU get up to yesterday?" # @t_svalk218.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_valkyrie "I skipped! IDK… Clubs are kind of a drag, y'know?" # @t_svalk219.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_valkyrie "You should come with me this time. I'm going to the roof tomorrow. Just the two of us." # @t_svalk220.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_surprised as cousin
            t_ch_cousin "Just the two of us?!" # @t_svalk221.00 self.block='Last'
            # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            extend " I'll... Think about it..." # @t_svalk221.01 self.block='Last'
            jump s_day2_valk_cleanup
        # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
        label s_day2_valk_didntEventLoop:
            # <Macro Macro {'name': 'didntEventLoop', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            label s_day2_valk_didntEventLoop_warm:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin zorder 2:
                    # ActorEvent
                    xpos 0.3 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                show i_valkyrie_default_wink as valkyrie zorder 2:
                    default
                    xpos 0.7 
                    alpha 0.0
                    linear 0.5 alpha 1.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            t_ch_valkyrie "Hey cutie! Maybe we can hang out tomorrow…" # @t_svalk222.00 self.block='Last'
            jump s_day2_valk_cleanup
        # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
        label s_day2_valk_cleanup:
            # <Macro Macro {'name': 'cleanup', 'kind': 'Macro'} ''>
            # <Events events {'kind': 'events'} ''>
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            label s_day2_valk_cleanup_cleanup:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_valkyrie_default_wink as valkyrie:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.5 alpha 0.0
                $ renpy.pause(0.5, hard=True) # TimedPause
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            label s_day2_valk_cleanup_reset:
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                hide valkyrie
                # Pass (ActorReset)
                $ scene_picked_once_valk = True
                # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
            jump s_day2_day2prechoice