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
# <Scene scene {'id': 's_day0', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_day0:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_day0"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_day0', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day0initialize', 'kind': 'ParallelEvent'} ''>
    label s_day0_day0initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day0initialize', 'kind': 'ParallelEvent'} ''>
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
        play music "bgm/school.ogg" loop
        show i_bg_classroom_a as bg zorder 1 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_cousin_default_neutral as cousin zorder 2:
            default
            alpha 1.0

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This place is crazy...and the people are even crazier...)" # @t_scousin00.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(But maybe some of them are nice?)" # @t_scousin01.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day0prechoice', 'kind': 'ParallelEvent'} ''>
    label s_day0_day0prechoice:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'day0prechoice', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_grin as cousin:
            # ShowWithAtl
            linear 0.5 alpha 0.0
        extend "{w=0.5}{nw}"
        # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
    $ s_day0_has_picked_any = False if not "s_day0_has_picked_any" in store.__dict__ else s_day0_has_picked_any
    window hide
    menu (screen="ChoiceExploration"):
        "Aki Matsuo":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_amazona
        "Albatross":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_albatros
        "Anti-Bravoman":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_antibravo
        "Blue Max":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_bluemax
        "Davesprite":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_davesprite
        "Donko":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_donko
        "Galaga":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_galaga
        "Hiromi":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_hiromi
        "Jane Crocker":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_jane
        "Lolo":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_lolo
        "Meowkie":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_meowkie
        "Mr. Driller":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_mrdriller
        "Nidia":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_nidia
        "Richard Miller":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_richard
        "Taira":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_taira
        "Terezi Pyrope":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_terezi
        "Tomari":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_tomari
        "Valkyrie":
            $ s_day0_has_picked_any = True
            window show
            jump s_day0_valk
        "Wait for Detention to End." if s_day0_has_picked_any:
            window show
            jump s_day0_cousin
    # <Macro Macro {'name': 'albatros', 'kind': 'Macro'} ''>
    label s_day0_albatros:
        # <Macro Macro {'name': 'albatros', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_albatros_warm:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_toocool_smirk as albatros zorder 2:
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
        t_ch_unknown "Psst. Hey, kid." # @t_salbatros00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_albatross_toocool_smirk as albatros:
            # FadeEvent
            linear 0.5 alpha 1.0
        extend "{w=0.5}{nw}"
        t_ch_albatros "I mean. Fellow student." # @t_salbatros01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "(Uh, is he talking to me?)" # @t_salbatros02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised_blush as cousin
        with Dissolve(0.5)
        t_ch_cousin "(He’s got a kind of dangerous outsider vibe going on.)" # @t_salbatros03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_grin_blush as cousin
        extend " (I kinda like it?)" # @t_salbatros03.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_albatros "What’cha in for?" # @t_salbatros04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised_blush as cousin
        t_ch_cousin "Er, what?" # @t_salbatros05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_albatros "Detention. That’s what you’re here for, right?" # @t_salbatros06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        t_ch_cousin "Oh, uh. Yeah." # @t_salbatros07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_albatross_toocool_inquisitive as albatros
        t_ch_albatros "Yeah." # @t_salbatros08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_albatros "Detention. It’s a drag." # @t_salbatros09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral_blush as cousin
        t_ch_cousin "(Wow, he’s just...really laid back.)" # @t_salbatros010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Like being in detention doesn’t mean anything to him!)" # @t_salbatros011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(I wish I could be that confident…)" # @t_salbatros012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_albatross_toocool_staredown as albatros
        t_ch_albatros "So, what’d you do? Cheatcodes?" # @t_salbatros013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "Um, me?" # @t_salbatros014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral_blush as cousin
        extend " (Maybe if I acted like Al, I’d get all cool and confident too! Yeah.)" # @t_salbatros014.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Uh, y’know. The usual." # @t_salbatros014.02 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " (Wait, what does that even mean?!)" # @t_salbatros014.03 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_albatross_toocool_smirk as albatross at default
        t_ch_albatros "Heh." # @t_salbatros015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_albatros "Yeah." # @t_salbatros016.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_albatros "I get’cha. The “usual.”" # @t_salbatros017.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_albatros "I like that. I think I’ll be seeing a LOT of you..." # @t_salbatros018.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Wow, I never impressed someone so cool and tough before…)" # @t_salbatros019.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_albatros_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_albatross_toocool_staredown as albatros:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_neutral_blush as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_albatros_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide albatros
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'amazona', 'kind': 'Macro'} ''>
    label s_day0_amazona:
        # <Macro Macro {'name': 'amazona', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_amazona_warm:
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
            show i_miller_akimbo_serious as miller zorder 2:
                default
                alpha 1.0
                xpos 0.7 
                ypos 1.49 
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_aki "Hi, [slot_playerName]!" # @t_samazona00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Do you need help with anything?" # @t_samazona00.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "I think I'm okay..." # @t_samazona01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_aki_akimbo_shocked as aki
        t_ch_aki "You don't need help with homework?" # @t_samazona02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_neutral as cousin
        t_ch_cousin "No?" # @t_samazona03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Do I look like I need help with homework?)" # @t_samazona04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_aki_akimbo_smile as aki
        show i_cousin_exhausted_neutral as cousin
        t_ch_cousin "(Has this delinquent atmosphere already rubbed off on me?!)" # @t_samazona05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_exhausted_surprised as cousin
        t_ch_cousin "(Speaking of which... How come it hasn't rubbed off on her?)" # @t_samazona06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Why is she even HERE?" # @t_samazona07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        extend " She seems like she's really got it together.)" # @t_samazona07.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Maybe she's lost!)" # @t_samazona08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "Excuse me, but... Why are you here?" # @t_samazona09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_aki_default_smile as aki
        t_ch_aki "OH. That. Well..." # @t_samazona010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_aki "One might say I'm... TOO diligent." # @t_samazona011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_aki_default_nervouslaughter as aki
        extend " Hahahaha!" # @t_samazona011.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(That doesn't sound at ALL like a reason to be in detention.)" # @t_samazona012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(How curious.)" # @t_samazona013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "Well, I don't get it, but... What club are you in, anyway?" # @t_samazona014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_aki_default_laughter as aki
        t_ch_aki "Why... I'm in all of them!" # @t_samazona015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "All... All of them?!" # @t_samazona016.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Is that even possible?!" # @t_samazona017.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_aki_akimbo_smile as aki
        play sound ["<silence 0.5>", "sfx/sentaisignal.ogg"]
        t_ch_aki "Hahaha! Of course it is... For someone like me, who frequently makes the impossible possible." # @t_samazona018.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_aki "Listen, if you don't need anything... I'm going to get back to work." # @t_samazona019.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_aki_akimbo_smile as aki
        t_ch_aki "But do let me know if something comes up! As Class President it's my responsibility to help you and the other students do your best!" # @t_samazona020.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_exhausted_surprised as cousin
        t_ch_cousin "(SHE'S ALSO CLASS PRESIDENT?!)" # @t_samazona021.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_aki_akimbo_laughter as aki
        t_ch_aki "Just know that if you DO want my help... I'll hold you up to my exacting standard. Ahahahaha!" # @t_samazona022.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_R', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_aki_akimbo_laughter as aki:
            # FadeEvent
            linear 0.75 alpha 0.0
        extend "{w=0.75}{nw}"
        t_ch_aki "Ciao!" # @t_samazona023.00 self.block='Last'
        show i_miller_akimbo_serious as miller:
            # ShowWithAtl
            easeout .33 ypos 0.5 
        # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_surprise as cousin
        t_ch_cousin "AHHHHHHH!" # @t_samazona024.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_miller "Hey... New kid." # @t_samazona025.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_akimbo_contemplative as miller
        t_ch_miller "You wanna know a secret?" # @t_samazona026.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_miller "I think ordinary student Aki Matsuo... Has a secret. A SUPER secret." # @t_samazona027.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_akimbo_halfgrin as miller
        t_ch_miller "Suspicious, isn't it?" # @t_samazona028.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "The only suspicious thing here..." # @t_samazona029.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        t_ch_cousin "IS YOU! Popping up out of nowhere like that..." # @t_samazona030.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_angry as cousin
        t_ch_cousin "I'm leaving! Don't follow me!" # @t_samazona031.00 self.block='Last'
        show i_cousin_energetic_angry as cousin:
            # FadeEvent
            linear 0.75 alpha 0.0
        # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_pondering_contemplative as miller
        t_ch_miller "Aw." # @t_samazona032.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_amazona_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_pondering_contemplative as miller:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_aki_akimbo_laughter as aki:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_energetic_angry as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_amazona_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide miller
            hide aki
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'antibravo', 'kind': 'Macro'} ''>
    label s_day0_antibravo:
        # <Macro Macro {'name': 'antibravo', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_antibravo_warm:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin zorder 2:
                # ActorEvent
                xpos 0.3 
                alpha 0.0
                linear 0.5 alpha 1.0
            show i_abm_backturned_broody as antibravo zorder 2:
                default
                alpha 0.0
                xpos 0.7 
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_questionmarks "I'll never escape... My dark ... darkness..." # @t_santibravo00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_abm_backturned_broody as antibravo
        t_ch_questionmarks "This is my burden..." # @t_santibravo01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_abm_backturned_broody as antibravo:
            # FadeEvent
            linear 1.0 alpha 1.0
        extend "{w=1.0}{nw}"
        extend " My curse..." # @t_santibravo01.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " My cross to bear..." # @t_santibravo01.02 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " My ..." # @t_santibravo01.03 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " My... burden to curse bears..." # @t_santibravo01.04 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(I..." # @t_santibravo02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Don't think he sees me." # @t_santibravo02.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " At all.)" # @t_santibravo02.02 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_questionmarks "...it's like bugs crawling inside of me... Really ugly bugs... Of darkness..." # @t_santibravo03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_questionmarks "I'm like a shadow... Of myself...which was originally a shadow, so really it's like a shadow twice removed and--" # @t_santibravo04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_abm_default_surprised as antibravo:
            xzoom -1.0 
        t_ch_questionmarks "AHHHH!" # @t_santibravo05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "(Oh... Did he notice me?)" # @t_santibravo06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_abm_default_surprised_blush as antibravo
        t_ch_questionmarks "Have you been there the whole time?!" # @t_santibravo07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Are you creepin'?!" # @t_santibravo07.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "I'm not creeping... You just didn't notice me. You were monologuing." # @t_santibravo08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "I've never seen someone do that before!" # @t_santibravo09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Anyway, I'm [slot_playerName]. What's your name?" # @t_santibravo09.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_abm_shadowknows_broody as antibravo
        t_ch_questionmarks "It's... Better that you don't know that I'm Anti-Bravoman." # @t_santibravo010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(........)" # @t_santibravo011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Should I say something... ? He takes himself so seriously though...)" # @t_santibravo012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_antibravo "And [slot_playerName]... Stay away from the Poetry Club." # @t_santibravo013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " For your own good." # @t_santibravo013.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_abm_backturned_broody as antibravo:
            xzoom 1.0 
        extend " It's where my darkness dwells." # @t_santibravo013.02 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        t_ch_cousin "(He turned around... How is his scarf billowing inside the classroom?)" # @t_santibravo014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(I think he's ignoring me..." # @t_santibravo015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " He keeps peeking to see if I'm gone." # @t_santibravo015.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " What an awkward guy...)" # @t_santibravo015.02 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_antibravo_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_abm_backturned_broody as antibravo:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_mortified as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_antibravo_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide antibravo
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'bluemax', 'kind': 'Macro'} ''>
    label s_day0_bluemax:
        # <Macro Macro {'name': 'bluemax', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_bluemax_warm:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_default_serious as taira zorder 2:
                default
                xpos 0.46 
                alpha 0.0
            show i_cousin_default_neutral as cousin zorder 2:
                # ActorEvent
                xpos 0.3 
                alpha 0.0
                linear 0.5 alpha 1.0
            show i_bluemax_stand_serious as bluemax zorder 2:
                default
                xpos 0.7 
                xzoom -1.0 
                alpha 0.0
                linear 0.5 alpha 1.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Hmm, who’s that?)" # @t_sbluemax00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(I think his name was Blue Max.)" # @t_sbluemax01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Hmm. He looks busy. Homework, maybe?)" # @t_sbluemax02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(I don’t see how a little guy like that belongs with these troublemakers.)" # @t_sbluemax03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_sad as cousin
        extend " (Guess you could say the same about me!)" # @t_sbluemax03.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_taira_steveholt_happy as taira:
            # FadeEvent
            linear 0.2 alpha 1.0
        show i_cousin_default_surprised as cousin:
            # ShowWithAtl
            linear 0.2 xpos 0.18 
        extend "{w=0.2}{nw}"
        t_ch_taira "Yo, what’s up Blue DORK?" # @t_sbluemax04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_bluemax_shock_shocked as bluemax:
            xzoom 1.0 
            # ShowWithAtl
            linear .2 xpos 0.79 
        show i_cousin_default_surprised as cousin
        $ renpy.pause(0.2, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_bluemax_shock_shocked as bluemax
        t_ch_max "AHH!" # @t_sbluemax05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_taira_revenge_happy as taira
        t_ch_taira "HAHA! IT’S FUNNY BECAUSE IT’S NOT HIS NAME!" # @t_sbluemax06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        t_ch_cousin "C’mon, guys. We’re already in detention." # @t_sbluemax07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_bluemax_cower_worried as bluemax
        show i_taira_akimbo_serious as taira
        t_ch_taira "Whatever you say, uh, NEW DORK!" # @t_sbluemax08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "Don’t pay any attention to him, Max." # @t_sbluemax09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_taira "Whatever." # @t_sbluemax010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_taira "I thought this was detention, not...uh...dumb baby day care. For babies." # @t_sbluemax011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_taira_akimbo_serious as taira:
            # FadeEvent
            linear 0.4 alpha 0.0
        extend "{w=0.4}{nw}"
        t_ch_taira "Y’babies." # @t_sbluemax012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin:
            # ShowWithAtl
            linear .3 xpos 0.3 
        show i_bluemax_cower_worried as bluemax:
            # ShowWithAtl
            linear .3 xpos 0.7 
        extend "{w=0.3}{nw}"
        t_ch_cousin "Good, he left. Like I was saying, don’t let him get to you." # @t_sbluemax013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_sad as cousin
        t_ch_cousin "A bully is just a kid who’s scared of something else anyway." # @t_sbluemax014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_bluemax_stand_worried as bluemax
        t_ch_max "Y-yeah, sure. Scared." # @t_sbluemax015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_max "And they hide it by acting tough..." # @t_sbluemax016.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_bluemax_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_bluemax_stand_worried as bluemax:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_taira_akimbo_serious as taira:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_energetic_sad as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_bluemax_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide bluemax
            hide taira
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'cousin', 'kind': 'Macro'} ''>
    label s_day0_cousin:
        # <Macro Macro {'name': 'cousin', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        menu:
            "Yeah, I just want out of here.":
                $ scene_doneExplore = True
            "I wanted to talk to someone else…":
                $ scene_doneExplore = False
        if scene_doneExplore:
            # <IfTrue IfTrue {'name': 'bail', 'value': '${scene:doneExplore}', 'kind': 'IfTrue'} ''>
            label s_day0_cousin_bail:
                # <IfTrue IfTrue {'name': 'bail', 'value': '${scene:doneExplore}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_cousin_bail_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_mortified as cousin zorder 2:
                        # ActorEvent
                        xpos 0.5 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(...Or they’re probably all bananas after all.)" # @t_scousin02.00 self.block='Last'
                # <NHSceneChange NHSceneChange {'name': '_2', 'scene': 's_day0.5', 'kind': 'NHSceneChange'} ''>
                label s_day0_cousin_bail__2:
                    # <NHSceneChange NHSceneChange {'name': '_2', 'scene': 's_day0.5', 'kind': 'NHSceneChange'} ''>
                    jump s_day0p5
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_cousin_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_mortified as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_cousin_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'davesprite', 'kind': 'Macro'} ''>
    label s_day0_davesprite:
        # <Macro Macro {'name': 'davesprite', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_davesprite:
            # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_davesprite}', 'kind': 'IfFalse'} ''>
            label s_day0_davesprite_firstDialouge:
                # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_davesprite}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_davesprite_firstDialouge_warm:
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
                t_ch_cousin "(That strange floating boy..." # @t_sdavesprite00.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I think his name was Davesprite-)" # @t_sdavesprite00.01 self.block='Last'
                if persistent.got_trueend_davesprite:
                    # <IfTrue IfTrue {'name': '_3', 'value': '${game:got_trueend_davesprite}', 'kind': 'IfTrue'} ''>
                    label s_day0_davesprite_firstDialouge__3:
                        # <IfTrue IfTrue {'name': '_3', 'value': '${game:got_trueend_davesprite}', 'kind': 'IfTrue'} ''>
                        # <Events events {'kind': 'events'} ''>
                        # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
                        # <Events events {'kind': 'events'} ''>
                        show i_davesprite_standing_sad as davesprite
                        t_ch_davesprite "so were doing this again huh" # @t_sdavesprite01.00a self.block='Last'
                        # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                        # <Events events {'kind': 'events'} ''>
                        t_ch_davesprite "well here we go" # @t_sdavesprite01.00b self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "hey this whole section here doesnt have anything to do with the game" # @t_sdavesprite01.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                t_ch_davesprite "i mean you dont make any choices or anything its kinda just filler" # @t_sdavesprite02.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "you can just click through" # @t_sdavesprite03.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Huh??" # @t_sdavesprite04.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "you dont even really have to read this stuff its just like" # @t_sdavesprite05.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                show i_cousin_default_neutral as cousin
                t_ch_davesprite "blah blah blah heres me heres a little taste of my character so you can get to know me" # @t_sdavesprite06.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "get ready to fall in love and go on the most incredible fake video game romance of your life" # @t_sdavesprite07.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "mom dad i dont care what you say this video game character is my boyfriend and were in love" # @t_sdavesprite08.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "that whole thing" # @t_sdavesprite09.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "yeah so anyway just click through its no big deal" # @t_sdavesprite010.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                t_ch_davesprite "especially since its just me so who cares" # @t_sdavesprite011.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "What the heck are you mumbling about?!" # @t_sdavesprite012.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                extend " Are you insane?!" # @t_sdavesprite012.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "man thats right i didnt explain too much did i" # @t_sdavesprite013.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "im just gonna do you a favor and make a long story short" # @t_sdavesprite014.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "I don’t know. I really don’t understand a thing you’re saying." # @t_sdavesprite015.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I think I definitely need a thorough explanation.." # @t_sdavesprite015.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "trust me im doing you a favor" # @t_sdavesprite016.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "you absolutely want just the cliff notes on this business" # @t_sdavesprite017.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                t_ch_davesprite "basically im a copy of a coolkid from an alternate timeline" # @t_sdavesprite018.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "i guess i got turned into this floating bird guy" # @t_sdavesprite019.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_smile as davesprite
                t_ch_davesprite "i look pretty suave i guess" # @t_sdavesprite020.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "i dont know it was a long time ago i think" # @t_sdavesprite021.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "anyway now ive become one of those dudes in the video game that tells you what to do" # @t_sdavesprite022.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                t_ch_davesprite "you know" # @t_sdavesprite023.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "a guide" # @t_sdavesprite024.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "to help the player along and help tell them what pixels to click on so they can proceed" # @t_sdavesprite025.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "Yeah, just keep mumbling gibberish. I’m really into that." # @t_sdavesprite026.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " (This boy is definitely completely out of his mind.)" # @t_sdavesprite026.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                t_ch_davesprite "and i know all the secrets of the game and stuff" # @t_sdavesprite027.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "yeah this one that youre playing right now" # @t_sdavesprite028.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "its kind of a bummer but also kinda cool" # @t_sdavesprite029.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                t_ch_davesprite "if youre into knowing all the secrets of the universe i guess" # @t_sdavesprite030.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "i guess im not supposed to act like i know its a game" # @t_sdavesprite031.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "meta stuff gets on peoples nerves but who cares they can deal" # @t_sdavesprite032.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "because yeah i dont really feel like doing that" # @t_sdavesprite033.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "so" # @t_sdavesprite034.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "whatever" # @t_sdavesprite035.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Cool, thanks for explaining." # @t_sdavesprite036.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                extend " I understand everything now!" # @t_sdavesprite036.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "And I’m definitely not thinking you’re an escapee from a mental institution!" # @t_sdavesprite037.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_eyebrow as davesprite
                t_ch_davesprite "youre one to talk with your space unitard and your antenna thing" # @t_sdavesprite038.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_smile as davesprite
                t_ch_davesprite "aw man i cant say that with a straight face" # @t_sdavesprite039.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_davesprite "the space unitard rules" # @t_sdavesprite040.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "ive never been so jealous of a ridiculous garment" # @t_sdavesprite041.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "i would describe myself as covetous even" # @t_sdavesprite042.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral_blush as cousin
                t_ch_cousin "Um… thanks!" # @t_sdavesprite043.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Wow, I’m..." # @t_sdavesprite044.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "I’m actually kind of flattered?" # @t_sdavesprite045.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                extend " And over a compliment from a psychopath!" # @t_sdavesprite045.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                show i_cousin_default_neutral as cousin
                t_ch_davesprite "yeah see its already happening" # @t_sdavesprite046.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                t_ch_davesprite "youre a player character so youre literally programmed to be all over me" # @t_sdavesprite047.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_smile as davesprite
                t_ch_davesprite "what can i say im a prototyped omniscient game guide" # @t_sdavesprite048.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_smile as davesprite
                t_ch_davesprite "how can you resist" # @t_sdavesprite049.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Sure… whatever you say." # @t_sdavesprite050.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "man i bet if i was actually trying to play along here i could make up a pretty good meet-cute" # @t_sdavesprite051.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "wed meet when we both trip and fall into a public water fountain at the same time" # @t_sdavesprite052.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "actually every step of our courtship would be punctuated by falling into water fountains" # @t_sdavesprite053.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "its pretty much the most classic way to go" # @t_sdavesprite054.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_smile as davesprite
                t_ch_davesprite "theres nothing better it beats rose petals on the bed and our dogs getting their leashes twisted together combined" # @t_sdavesprite055.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "falling into public water fountains is stone cold romance" # @t_sdavesprite056.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_smile as davesprite
                t_ch_davesprite "even for our wedding wed be climbing out of a fountain soaking wet all like" # @t_sdavesprite057.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_smile as davesprite
                t_ch_davesprite "who keeps putting these fountains here" # @t_sdavesprite058.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "it keeps happening" # @t_sdavesprite059.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_laugh as cousin
                t_ch_cousin "Haha!" # @t_sdavesprite060.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "You know, Davesprite, you’re actually pretty funny…" # @t_sdavesprite061.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Do you always ramble on like this, though?" # @t_sdavesprite062.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_smile as davesprite
                t_ch_davesprite "yeah see you like me already" # @t_sdavesprite063.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_smile as davesprite
                t_ch_davesprite "thats okay youre supposed to be liking everybody at this point" # @t_sdavesprite064.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_disinterest as davesprite
                t_ch_davesprite "well listen if you stick with me ill tell you how to get through the game as fast as possible and get the good ending" # @t_sdavesprite065.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "what do you say" # @t_sdavesprite066.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Davesprite, I still don’t know what the heck you’re talking about." # @t_sdavesprite067.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Or even what you are…" # @t_sdavesprite067.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Some kind of ghost thing? I dunno." # @t_sdavesprite067.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "But if you want to hang out with me…" # @t_sdavesprite068.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "I mean, sure! I don’t really have any friends here yet." # @t_sdavesprite069.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You don’t have to make up some weird nonsense “video game” story about it." # @t_sdavesprite069.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "You can just ask me! Okay?" # @t_sdavesprite070.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_standing_eyebrow as davesprite
                t_ch_davesprite "uh" # @t_sdavesprite071.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                t_ch_davesprite "word" # @t_sdavesprite072.00 self.block='Last'
                jump s_day0_davesprite_cleanup
        if scene_picked_once_davesprite:
            # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_davesprite}', 'kind': 'IfTrue'} ''>
            label s_day0_davesprite_loopDialogue:
                # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_davesprite}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_davesprite_loopDialogue_warm:
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
                t_ch_davesprite "why are you still clicking on me it doesnt even matter" # @t_sdavesprite073.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "youre supposed to be clicking on characters so you can get to know them and decide which one to romance" # @t_sdavesprite074.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "come on get to it times a wasting" # @t_sdavesprite075.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_davesprite_shrug_disinterest as davesprite
                t_ch_davesprite "well not really you can pretty much click on them at your leisure i guess" # @t_sdavesprite076.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_laugh as cousin
                show i_davesprite_standing_disinterest as davesprite
                t_ch_cousin "Haha, Davesprite, what are you even talking about… you’re so crazy!" # @t_sdavesprite077.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "But funny, too…" # @t_sdavesprite078.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I kinda like you." # @t_sdavesprite078.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_davesprite "yeah ok whatever" # @t_sdavesprite079.00 self.block='Last'
                jump s_day0_davesprite_cleanup
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_davesprite_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_davesprite_standing_disinterest as davesprite:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_grin as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_davesprite_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide davesprite
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'donko', 'kind': 'Macro'} ''>
    label s_day0_donko:
        # <Macro Macro {'name': 'donko', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_donko:
            # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_donko}', 'kind': 'IfFalse'} ''>
            label s_day0_donko_firstDialouge:
                # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_donko}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_donko_firstDialouge_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_donko_phone_grin as donko zorder 2:
                        default
                        xpos 0.73 
                        alpha 0.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.27 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_questionmarks "Teehee! Yeah!" # @t_sdonko00.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " No I know, that’s totally what I said!" # @t_sdonko00.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Jeez, who’s talking on the phone so loud?" # @t_sdonko01.00 self.block='Last'
                show i_donko_phone_grin as donko:
                    # FadeEvent
                    linear 0.5 alpha 1.0
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Oh! It’s that drum thing… Donko!)" # @t_sdonko02.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "Like, totally!" # @t_sdonko03.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Oh, man..." # @t_sdonko04.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " How can she get away with that?" # @t_sdonko04.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " In the middle of detention?!" # @t_sdonko04.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "I don’t like rudeness like that…)" # @t_sdonko05.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_phone_wink as donko
                t_ch_donko "Uh huh, yeah. Detention again." # @t_sdonko06.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Yeah, for talking on my phone in class." # @t_sdonko06.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " It’s like, hell-OH, of COURSE I’m on my phone, because everybody’s calling me all the time!" # @t_sdonko06.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_phone_grin as donko
                t_ch_donko "Class is so boring anyway!" # @t_sdonko07.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " We should ALL be on our phones!" # @t_sdonko07.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "It’s like I keep saying! That teacher really needs to get off his hi-hat." # @t_sdonko08.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_phone_crying_comic as donko
                extend " So anyway, yeah, Wada-Don and I broke up...." # @t_sdonko08.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Hi-hat…" # @t_sdonko09.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "Isn’t that a drum term?" # @t_sdonko010.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_phone_grin as donko
                extend " I think Donko means something else.)" # @t_sdonko010.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Um, excuse me… Donko?" # @t_sdonko011.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_phone_wink as donko
                extend " When you said “hi-hat” just now-" # @t_sdonko011.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Didn’t you mean “high horse”?" # @t_sdonko012.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "..." # @t_sdonko013.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_phone_meloncholic as donko
                extend " I’m gonna have to call you back, Miranda.  *CLICK*" # @t_sdonko013.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_meloncholic as donko:
                    xzoom 0.85 

                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_meloncholic as donko:
                    linear .2 xzoom -0.85 
                t_ch_donko "Excuse me?!" # @t_sdonko014.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "Are you giving me ATTITUDE?" # @t_sdonko015.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Do you, like, even KNOW who I AM?!" # @t_sdonko015.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(I didn’t think a cute little drum could be so scary…)" # @t_sdonko016.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_wink as donko
                t_ch_donko "I’m Donko!" # @t_sdonko017.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_meloncholic as donko
                extend " And I own this school, LOSER!" # @t_sdonko017.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "Hi-hat, high horse-" # @t_sdonko018.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_ygg_wink as donko
                t_ch_donko "Whichever one I say is the right one, because I’m so CUTE!" # @t_sdonko019.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_ygg_meloncholic as donko
                t_ch_donko "GOT IT?!" # @t_sdonko020.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "…" # @t_sdonko021.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "…" # @t_sdonko022.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_grin as donko
                t_ch_donko "Ee hee hee! No way!" # @t_sdonko023.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " The look on your face…" # @t_sdonko023.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You really thought I was serious?" # @t_sdonko023.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "..Oh… Um…" # @t_sdonko024.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_wink as donko
                t_ch_donko "Tee hee! You’re the new kid here..." # @t_sdonko025.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " “[slot_playerName]”, right?" # @t_sdonko025.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "It takes guts to drum-stick it to the most popular student at Namco High." # @t_sdonko026.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You don’t look like much…" # @t_sdonko026.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "But you’ve got some potential, honey!" # @t_sdonko027.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Haha…" # @t_sdonko028.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                extend " I don’t know about that, but…" # @t_sdonko028.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_grin as cousin
                t_ch_cousin "If you like it when I stand up to you, I should also say I thought it was pretty rude of you to talk on your phone in detention!" # @t_sdonko029.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_surprised as cousin
                extend " Especially if that’s WHY you’re in detention in the first place!" # @t_sdonko029.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "…" # @t_sdonko030.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_donko_default_meloncholic as donko
                t_ch_donko "Don’t push it, honey." # @t_sdonko031.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "(Donko is rude…" # @t_sdonko032.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " Bossy…" # @t_sdonko032.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " And totally full of it…" # @t_sdonko032.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral_blush as cousin
                t_ch_cousin "But also… really cute." # @t_sdonko033.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I gotta admit… there’s just something about her.)" # @t_sdonko033.01 self.block='Last'
                jump s_day0_donko_cleanup
        if scene_picked_once_donko:
            # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_donko}', 'kind': 'IfTrue'} ''>
            label s_day0_donko_loopDialogue:
                # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_donko}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_donko_loopDialogue_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_donko_phone_wink as donko zorder 2:
                        default
                        xpos 0.73 
                        alpha 0.0
                        alpha 1.0
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.27 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "So anyway Miranda. Like I was saying, the new kid is KINDA cute, but also, like, totally LAME." # @t_sdonko034.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "...You know perfectly well I can hear you, don’t you?" # @t_sdonko035.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_donko "Tee-hee! You catch on quick, for a new kid." # @t_sdonko036.00 self.block='Last'
                jump s_day0_donko_cleanup
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_donko_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_phone_wink as donko:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_mortified as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_donko_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide donko
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'galaga', 'kind': 'Macro'} ''>
    label s_day0_galaga:
        # <Macro Macro {'name': 'galaga', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_galaga_warm:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_default_wink as donko zorder 4:
                default
                xpos 0.45 
                alpha 0.0
                xzoom -0.85 
                yzoom 0.85 
                linear 0.5 alpha 1.0
            show i_aki_justice_laughter as aki zorder 1:
                default
                xpos 0.65 
            show i_tomari_standing_smile as tomari zorder 1:
                default
                xpos 0.94 
                xzoom -1.0 
            show i_cousin_default_neutral_blush as cousin zorder 1:
                # ActorEvent
                xpos 0.1 
                alpha 0.0
                linear 0.5 alpha 1.0
            show i_galaga_default as galaga zorder 3:
                default
                xpos 0.8 
                alpha 0.0
                linear 0.5 alpha 1.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Who is that beautiful creature…?)" # @t_sgalaga00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        extend " (Wait. Is that the right word?)" # @t_sgalaga00.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " (Beautiful?)" # @t_sgalaga00.02 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral_blush as cousin
        extend " (More like captivating!)" # @t_sgalaga00.03 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_sad as cousin
        extend " (Tsk. It’s surrounded by so many admirers.)" # @t_sgalaga00.04 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " (It’ll never notice little ol’ me.)" # @t_sgalaga00.05 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_galaga "{smallcaps}Haha, don’t be ridiculous!{/smallcaps}" # @t_sgalaga01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_surprise as cousin
        t_ch_cousin "(IT CAN READ MY THOUGHTS???)" # @t_sgalaga02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_galaga "{smallcaps}If anyone’s gonna be Juliet, it’ll be Donko.{/smallcaps}" # @t_sgalaga03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_exhausted_neutral as cousin
        t_ch_cousin "(Wait, it's not talking to me…)" # @t_sgalaga04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_donko_default_grin as donko:
            # ShowWithAtl
            linear 0.333 alpha 1.0
        extend "{w=0.333}{nw}"
        t_ch_donko "Uh, helloooo, Galaga Ship? You literally live in a Tuscan Villa!" # @t_sgalaga05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_galaga "{smallcaps}It’s not a whole villa!{/smallcaps}" # @t_sgalaga06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_donko_default_wink as donko
        t_ch_donko "Face it. You couldn’t be more Juliet if they built you that way." # @t_sgalaga07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " And I think they did!" # @t_sgalaga07.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_galaga "{smallcaps}“To be or not to be, that is the question.”{/smallcaps}" # @t_sgalaga08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_donko_default_grin_blush as donko
        t_ch_donko "…" # @t_sgalaga09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_donko_default_wink as donko
        t_ch_donko "See? That’s the most Juliet thing I ever heard!" # @t_sgalaga010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "It’s from Hamlet." # @t_sgalaga011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_donko_default_meloncholic as donko:
            pause 1
            linear .3 xzoom 0.85 
        show i_aki_default_focus as aki:
            pause 1.2
            linear .3 xzoom -1.0 
        show i_tomari_pondering_frustrated as tomari:
            pause .8
            linear .3 xzoom 1.0 
        $ renpy.pause(1.2, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_galaga "{smallcaps}Hamlet…?{/smallcaps}" # @t_sgalaga012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_mortified as cousin
        t_ch_cousin "(AHHH, DID I SAY THAT OUT LOUD?!)" # @t_sgalaga013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_donko_akimbo_meloncholic as donko
        t_ch_donko "Whatever, new kid. It just shows how much of a total Juliet Galaga Ship really is!" # @t_sgalaga014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        t_ch_galaga "{smallcaps}…{/smallcaps}" # @t_sgalaga015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_O', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_donko_akimbo_meloncholic as donko:
            # ShowWithAtl
            pause 0.5 
            ease_expo .5 xpos 0.85 
        show i_galaga_default as galaga:
            # ShowWithAtl
            ease_expo 1 xpos 0.55 
        show i_aki_default_focus as aki:
            # ShowWithAtl
            pause 0.7 
            linear .5 xpos 0.78 
        $ renpy.pause(1.2, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " {smallcaps}Hm. Well, if you know so much about Shakespeare and stuff…{/smallcaps}" # @t_sgalaga015.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        extend " {smallcaps}…why don’t you audition for the play?{/smallcaps}" # @t_sgalaga015.02 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified_blush as cousin
        t_ch_cousin "(Augh, does Galaga Ship hate me already?!)" # @t_sgalaga016.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " (Should’ve kept my trap shut!)" # @t_sgalaga016.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        extend " (Uh, everyone’s waiting for an answer)" # @t_sgalaga016.02 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Uh…" # @t_sgalaga016.03 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        extend " (Play it cool, [slot_playerName].)" # @t_sgalaga016.04 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        extend " Uh, yeah!" # @t_sgalaga016.05 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "I mean, I don’t know much, but…" # @t_sgalaga017.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_grin as cousin
        t_ch_cousin "But it might be cool." # @t_sgalaga018.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_grin_blush as cousin
        extend " (If Galaga Ship is Juliet, maybe I could audition for Romeo!)" # @t_sgalaga018.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_sad as cousin
        t_ch_cousin "(Wonder if I can act…?)" # @t_sgalaga019.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_exhausted_mortified as cousin
        t_ch_cousin "(Like. At all…)" # @t_sgalaga020.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_galaga_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_donko_akimbo_meloncholic as donko:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_galaga_default as galaga:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_exhausted_mortified as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_galaga_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide donko
            hide galaga
            hide aki
            hide tomari
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'hiromi', 'kind': 'Macro'} ''>
    label s_day0_hiromi:
        # <Macro Macro {'name': 'hiromi', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_hiromi_warm:
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
        t_ch_hiromi "..............." # @t_shiromi00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "............?" # @t_shiromi01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(She's just... Looking at me.)" # @t_shiromi02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "(She's so tall... her stare somehow becomes more intimidating.)" # @t_shiromi03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "H-hi there. Nice to meet you?" # @t_shiromi04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_hiromi "Hey." # @t_shiromi05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "So... You in detention....much.........." # @t_shiromi06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        t_ch_cousin "(Nailed it.)" # @t_shiromi07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_hiromi_crossed_serious as hiromi
        show i_cousin_default_neutral as cousin
        t_ch_hiromi "Yeah." # @t_shiromi08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Cool... Cool.... Me too........." # @t_shiromi09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_sad as cousin
        extend "{w=0.5}{nw}"
        t_ch_cousin "(Smooth. Just like the King of All Cosmos.)" # @t_shiromi010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin

        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Um... She's not saying anything.)" # @t_shiromi011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        t_ch_cousin "(Did I say something offensive?!)" # @t_shiromi012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "......................" # @t_shiromi013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Sooooooo... What club are you in?" # @t_shiromi014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_hiromi "......" # @t_shiromi015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_hiromi ".............." # @t_shiromi016.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_hiromi_tool_serious as hiromi
        t_ch_hiromi ".....................Auto Club." # @t_shiromi017.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_surprise as cousin
        t_ch_cousin "(!!!! SHE SAID SOMETHING)" # @t_shiromi018.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_grin as cousin
        t_ch_cousin "That sounds cool!" # @t_shiromi019.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_hiromi_akimbo_serious as hiromi
        t_ch_hiromi "I like it." # @t_shiromi020.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "Are you looking for members..... ?" # @t_shiromi021.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_hiromi "Not really." # @t_shiromi022.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_exhausted_neutral as cousin
        t_ch_cousin "O-oh." # @t_shiromi023.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_hiromi_akimbo_serious as hiromi
        t_ch_hiromi "But there's always room for more." # @t_shiromi024.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin ".........................." # @t_shiromi025.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "(Is she going to ask me to join?)" # @t_shiromi026.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Um............" # @t_shiromi027.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin ".........................." # @t_shiromi028.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin ".............. Could I join?" # @t_shiromi029.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_hiromi_crossed_serious as hiromi
        t_ch_hiromi "..........." # @t_shiromi030.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_hiromi "..................Huh?" # @t_shiromi031.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_hiromi_stand_serious as hiromi
        extend " Oh, sure. If you want, kid." # @t_shiromi031.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_exhausted_neutral as cousin
        t_ch_cousin "(She went back into her own mind.)" # @t_shiromi032.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(It doesn't seem like she DOESN'T want me to join... )" # @t_shiromi033.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "(Hiromi is just a little.... Too cool.)" # @t_shiromi034.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_hiromi_cleanup:
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
        label s_day0_hiromi_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide hiromi
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'jane', 'kind': 'Macro'} ''>
    label s_day0_jane:
        # <Macro Macro {'name': 'jane', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_jane:
            # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_jane}', 'kind': 'IfFalse'} ''>
            label s_day0_jane_firstDialouge:
                # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_jane}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_jane_firstDialouge_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_jane_default_smile as jane zorder 2:
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
                t_ch_cousin "(You know, even though she’s sitting with the weird kids..." # @t_sjane00.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " That girl doesn’t seem so bad." # @t_sjane00.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "In fact, she seems perfectly normal!" # @t_sjane01.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Surrounded by all these weirdos, “normal” sounds pretty good right now.)" # @t_sjane02.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_laugh as jane
                t_ch_jane "Hellooooo! :B" # @t_sjane03.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_grin as jane
                t_ch_jane "The name’s Jane Crocker. I don’t think we’ve met!" # @t_sjane04.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Uh, hi! I’m [slot_playerName]. Nice to meet you!" # @t_sjane05.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "I’m pretty new here… I was hoping I could hang out with someone friendly." # @t_sjane06.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_handonhip_smile as jane
                t_ch_jane "Hoo hoo! You seem like a very nice youngster, but I do hope you know I haven’t been fooled!" # @t_sjane07.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_smile as jane
                extend " Nice or not, you must have been up to some awful tomfoolery to wind up here in detention!" # @t_sjane07.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Heh! I guess so…" # @t_sjane08.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " But I could also say the same about you!" # @t_sjane08.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " What are you in for, anyway?" # @t_sjane08.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_grin as jane
                t_ch_jane "Fair enough! The truth is, I have something of a weakness for a good prank." # @t_sjane09.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_smile as jane
                extend " I know it’s not very sensible, buuuttt…." # @t_sjane09.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_handonhip_laugh as jane
                t_ch_jane "All work and no play makes Jane a dull girl!" # @t_sjane010.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_handonhip_smile as jane
                extend " As I believe the saying goes." # @t_sjane010.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Something like that. Anyway, that sounds a lot more fun than what I’m in for." # @t_sjane011.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_grin as jane
                t_ch_jane "Ooooh, yes! I remember now! You caused some kind of schoolwide fiasco!" # @t_sjane012.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_smile as jane
                t_ch_jane "Something to do with rolling a bowling ball and breaking things?" # @t_sjane013.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I’m not terribly certain on the details yet. Still, I’ve determined that it was mostly accidental." # @t_sjane013.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_grin as jane
                t_ch_jane "So you don’t have to worry too much about it! No real harm done. :B" # @t_sjane014.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_sad as cousin
                show i_jane_default_smile as jane
                t_ch_cousin "W-well… it WAS an accident, but…" # @t_sjane015.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_sad as cousin
                extend " It was much bigger than a bowling ball! It was my katamari." # @t_sjane015.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "I rolled up the whole school by accident! I even rolled up students." # @t_sjane016.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_surprised as cousin
                extend " I might have even rolled YOU up!" # @t_sjane016.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Although, I guess I couldn’t have. If you’d been there, there’s no WAY you’d mistake it for a bowling ball." # @t_sjane017.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_smile as jane
                t_ch_jane "Oh, yes. A giant ball, somehow able to “roll up” everything in the school, including students themselves!" # @t_sjane018.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Gee whiz, that sounds very plausible. I am completely in awe at the overwhelming veracity of your story!" # @t_sjane018.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_laugh as jane
                t_ch_jane "Hoo hoo. Just kidding. :B" # @t_sjane019.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_grin as jane
                t_ch_jane "Sorry, [slot_playerName], but that prank was more than a little on the lame side." # @t_sjane020.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_armscrossed_laugh as jane
                extend " You would have to get up pretty early in the morning to fool an expert prankster like me with a flimsy tale like that!" # @t_sjane020.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                show i_jane_armscrossed_smile as jane
                t_ch_cousin "(H-huh?? She doesn’t believe me? But… everyone saw it and was there…" # @t_sjane021.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_surprise as cousin
                t_ch_cousin "Unless… she’s pranking me… by pretending not to believe me??)" # @t_sjane022.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Anyway..." # @t_sjane023.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "I think it would be cool to hang out sometime, Jane!" # @t_sjane024.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " It’s nice to be around a normal girl like you." # @t_sjane024.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "I mean, for example- Galaga is pretty amazing, but I think it might be kinda stressful to try to find common ground with a beautiful spaceship." # @t_sjane025.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_handonhip_laugh as jane
                t_ch_jane "Geez-Louise, [slot_playerName]! You could try a little harder with your flights of fancy." # @t_sjane026.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_handonhip_smile as jane
                extend " A spaceship could never fit into a tiny classroom like this!" # @t_sjane026.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(But… Galaga is sitting right over there…)" # @t_sjane027.00 self.block='Last'
                jump s_day0_jane_cleanup
        if scene_picked_once_jane:
            # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_jane}', 'kind': 'IfTrue'} ''>
            label s_day0_jane_loopDialogue:
                # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_jane}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_jane_loopDialogue_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_jane_default_smile as jane zorder 2:
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
                show i_jane_handonhip_grin as jane
                t_ch_jane "Say, [slot_playerName]. Do me a favor and take a look over there!" # @t_sjane028.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(She’s pointing behind my shoulder?" # @t_sjane029.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin:
                    linear 0.20 xzoom -1.0 
                show i_jane_handonhip_grin as jane:
                    # ShowWithAtl
                    linear 0.40 xpos 0.5 
                extend "{w=0.4}{nw}"
                extend " I guess it couldn’t hurt to look-)" # @t_sjane029.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_surprise as cousin
                t_ch_cousin "AUGH!" # @t_sjane030.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_jane_default_laugh as jane:
                    # ShowWithAtl
                    linear 0.30 xpos 0.7 
                show i_cousin_energetic_surprise as cousin:
                    linear 0.20 xzoom 1.0 
                extend "{w=0.3}{nw}"
                t_ch_jane "Hoo hoo hoo! Gotcha! :B" # @t_sjane031.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "(I can’t believe I fell for that…" # @t_sjane032.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " She really IS an expert prankster!)" # @t_sjane032.01 self.block='Last'
                jump s_day0_jane_cleanup
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_jane_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_jane_default_laugh as jane:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_surprised as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_jane_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide jane
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'lolo', 'kind': 'Macro'} ''>
    label s_day0_lolo:
        # <Macro Macro {'name': 'lolo', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_lolo:
            # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_lolo}', 'kind': 'IfFalse'} ''>
            label s_day0_lolo_firstDialouge:
                # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_lolo}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_lolo_firstDialouge_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_lolo_crossed_frustrated as lolo zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(That girl over there..." # @t_slolo00.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " ...Lolo." # @t_slolo00.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "She has such a faraway, sad look on her face." # @t_slolo01.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "I guess I could be reading too much into things..." # @t_slolo02.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                extend " But... there is just something about her." # @t_slolo02.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "If I were her, I’d want  someone to come talk to me.)" # @t_slolo03.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Um, hello. Do you mind if I sit with you?" # @t_slolo04.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_shrug_raisedbrow as lolo
                t_ch_lolo "Knock yourself out, I guess." # @t_slolo05.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "…" # @t_slolo06.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_raisedbrow as lolo
                t_ch_lolo "…" # @t_slolo07.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "..." # @t_slolo08.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                extend " (This is pretty awkward.)" # @t_slolo08.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_lolo "You done staring yet?" # @t_slolo09.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I’m guessing you don’t have anything better to do, but still." # @t_slolo09.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "O-oh! I wasn’t... I mean..." # @t_slolo010.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " (I guess I was staring...)" # @t_slolo010.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "...I didn’t mean to bother you or anything." # @t_slolo011.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_sad as cousin
                t_ch_cousin "(Jeez, why am I so nervous? She’s just some girl.)" # @t_slolo012.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "I just thought you seemed kind of..." # @t_slolo013.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You know, kind of..." # @t_slolo013.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Um..." # @t_slolo013.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "...You seemed kind of sad, I guess." # @t_slolo014.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_grin as lolo
                t_ch_lolo "Haha, really? We’re in detention." # @t_slolo015.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Not only that, we’re in high school." # @t_slolo015.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_raisedbrow as lolo
                extend " Who wouldn't \"seem kind of sad\"?" # @t_slolo015.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(That’s a little... bleak.)" # @t_slolo016.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "S-so uh anyway... why are you in detention?" # @t_slolo017.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_grin as lolo
                t_ch_lolo "Heh. Why do you even care?" # @t_slolo018.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "Jeez! I’m just trying to make conversation." # @t_slolo019.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_raisedbrow as lolo
                t_ch_lolo "What for? You don’t even know me." # @t_slolo020.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "Okay, fine. I can take a hint." # @t_slolo021.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I’ll sit somewhere else." # @t_slolo021.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                extend " Sorry I bothered you." # @t_slolo021.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(I shouldn’t snap at her." # @t_slolo022.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I’m more angry at myself." # @t_slolo022.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                extend " Why did I have to say such boneheaded things around her?)" # @t_slolo022.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_grin as lolo
                t_ch_lolo "Hey, c’mon! Sit down." # @t_slolo023.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Don’t be such a baby!" # @t_slolo023.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Can’t you tell when someone’s just teasing?" # @t_slolo023.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_frustrated as lolo
                t_ch_lolo "...Fine, whatever." # @t_slolo024.00 self.block='Last'
                jump s_day0_lolo_cleanup
        if scene_picked_once_lolo:
            # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_lolo}', 'kind': 'IfTrue'} ''>
            label s_day0_lolo_loopDialogue:
                # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_lolo}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_lolo_loopDialogue_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_lolo_crossed_frustrated as lolo zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_frustrated as lolo
                show i_cousin_default_neutral as cousin
                t_ch_lolo "…" # @t_slolo025.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "…" # @t_slolo026.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_lolo_crossed_raisedbrow as lolo
                t_ch_lolo "If you’re waiting for me to say sorry for hurting your feelings…" # @t_slolo027.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Don’t." # @t_slolo027.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "I wasn’t waiting for that!" # @t_slolo028.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(And even if I was, I’m not giving her the satisfaction!)" # @t_slolo029.00 self.block='Last'
                jump s_day0_lolo_cleanup
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_lolo_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_lolo_crossed_raisedbrow as lolo:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_mortified as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_lolo_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide lolo
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'meowkie', 'kind': 'Macro'} ''>
    label s_day0_meowkie:
        # <Macro Macro {'name': 'meowkie', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_meowkie:
            # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_meowkie}', 'kind': 'IfFalse'} ''>
            label s_day0_meowkie_firstDialouge:
                # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_meowkie}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_meowkie_firstDialouge_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_meowkie_normal_normal_badge as meowkie zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(That … cat? Girl? Cat-girl?" # @t_smeowkie00.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I think her name was Meowkie." # @t_smeowkie00.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "I like cats..." # @t_smeowkie01.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " Who doesn’t?" # @t_smeowkie01.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Let’s see what club she’s in.)" # @t_smeowkie01.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Hi! Mind if I sit with you, Meowkie?" # @t_smeowkie02.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie:
                    linear 0.20 xzoom -1.0 
                t_ch_meowkie "O-oh! Not at all! Go right ahead, Boss!" # @t_smeowkie03.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "...it’s “[slot_playerName].”" # @t_smeowkie04.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_meowkie "Nyaah! Of course!" # @t_smeowkie05.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Sorry about that!" # @t_smeowkie05.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_slouch_alert_badge as meowkie
                t_ch_meowkie "Anyway..." # @t_smeowkie06.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_grin_badge as meowkie
                t_ch_meowkie "It’s sure nice to see a new face around here for a change!" # @t_smeowkie07.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_normal_badge as meowkie
                extend " As long as you’re not a troublemaker!" # @t_smeowkie07.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Eh heh..." # @t_smeowkie08.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Aren’t we all troublemakers in here?" # @t_smeowkie08.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie
                t_ch_meowkie "NYAAH! Right! How silly of me!" # @t_smeowkie09.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_slouch_frown_badge as meowkie
                extend " Y-you must think I’m a real catnip-head..." # @t_smeowkie09.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie
                t_ch_meowkie "I was just jokin’ anyway... Let’s just forget about that, Boss!" # @t_smeowkie010.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_laugh as cousin
                t_ch_cousin "Haha! Why do you keep calling me Boss?" # @t_smeowkie011.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_slouch_frown_badge as meowkie
                show i_cousin_default_neutral as cousin
                t_ch_meowkie "Erk... I’m sorry... It’s..." # @t_smeowkie012.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_slouch_forcedsmile_badge as meowkie
                extend " ...it’s a bad habit, yknow?" # @t_smeowkie012.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_meowkie "Runs in... in the family, I guess..." # @t_smeowkie013.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " It’s what we used to call the Big Cat..." # @t_smeowkie013.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie
                t_ch_meowkie "Sorry! I’ll try harder, Bo- I mean, [slot_playerName]!" # @t_smeowkie014.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Meowkie! Calm down!" # @t_smeowkie015.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                extend " You can call me whatever makes you feel comfortable." # @t_smeowkie015.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " Er, within reason." # @t_smeowkie015.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "What do you mean, “runs in the family”?" # @t_smeowkie016.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Like, is it a cat thing?" # @t_smeowkie016.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_alert_badge as meowkie
                t_ch_meowkie "… You..." # @t_smeowkie017.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You don’t know?" # @t_smeowkie017.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "??" # @t_smeowkie018.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_meowkie "About me, I mean?" # @t_smeowkie019.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You don’t know about my family?" # @t_smeowkie019.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_grin_badge as meowkie
                t_ch_meowkie "Nyaaahhh... That’s great!" # @t_smeowkie020.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Whoah, she seems really excited.)" # @t_smeowkie021.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "What do you mean?" # @t_smeowkie022.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_slouch_alert_badge as meowkie
                t_ch_meowkie "Er... is it okay if I... tell you about it later, Boss?" # @t_smeowkie023.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "Heh... Sure." # @t_smeowkie024.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                extend " (What’s THAT all about?)" # @t_smeowkie024.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_normal_badge as meowkie
                show i_cousin_default_neutral as cousin
                t_ch_meowkie "Anyway, like I was sayin’..." # @t_smeowkie025.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_grin_badge as meowkie
                extend " I’m sure you ain’t really a troublemaker!" # @t_smeowkie025.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_normal_badge as meowkie
                t_ch_meowkie "It’s just somethin’ I think about a lot, since I’m..." # @t_smeowkie026.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_grin_badge as meowkie
                t_ch_meowkie "a Hall Monitor and all!" # @t_smeowkie027.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(She seems awfully proud of that!)" # @t_smeowkie029.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Hall Monitor? Wow! How did the Hall Monitor end up in detention?!" # @t_smeowkie030.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_slouch_frown_badge as meowkie
                t_ch_meowkie "…." # @t_smeowkie031.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_sad as cousin
                t_ch_cousin "(Uh oh... I hope she doesn’t get mad at me...)" # @t_smeowkie032.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_meowkie "...Maybe... we could talk about that another time, too." # @t_smeowkie033.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_forcedsmile_badge as meowkie
                extend " If that’s alright with you, Boss." # @t_smeowkie033.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(This Meowkie... she seems like a sweet girl." # @t_smeowkie034.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "But she’s a lot cagier than I expected!" # @t_smeowkie035.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "On the other hand, she is a cat..." # @t_smeowkie036.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                extend " Omigosh, is that racist?!" # @t_smeowkie038.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Anyway, I wouldn’t mind taking the time to figure her out...)" # @t_smeowkie039.00 self.block='Last'
                jump s_day0_meowkie_cleanup
        if scene_picked_once_meowkie:
            # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_meowkie}', 'kind': 'IfTrue'} ''>
            label s_day0_meowkie_loopDialogue:
                # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_meowkie}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_meowkie_loopDialogue_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_meowkie_normal_normal_badge as meowkie zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_normal_badge as meowkie
                show i_cousin_default_neutral as cousin
                t_ch_meowkie "Hiya, Boss! Like I said, it sure is good to have somebody new around." # @t_smeowkie040.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_alert_badge as meowkie
                extend " Hey, I know! What’s your favorite kinda fish?!" # @t_smeowkie040.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Fish?" # @t_smeowkie041.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Uh, you mean like… to eat?" # @t_smeowkie041.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_grin_badge as meowkie
                t_ch_meowkie "Nya… a’course to eat!" # @t_smeowkie042.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_normal_badge as meowkie
                extend " What else are you gonna do with a fish?" # @t_smeowkie042.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "I dunno… It’d be kinda nice to keep one as a pet." # @t_smeowkie043.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_normal_alert_badge as meowkie
                t_ch_meowkie "Huh… really? I guess that’s why they keep ‘em in bowls like that…" # @t_smeowkie044.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_slouch_alert_badge as meowkie
                extend " And why they get mad when I eat ‘em." # @t_smeowkie044.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_meowkie_akimbo_grin_badge as meowkie
                t_ch_meowkie "Nyahaha! Oh well… Fish taste better when you eat em alive, right Boss?" # @t_smeowkie045.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "..." # @t_smeowkie046.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(I didn’t notice til now how sharp her teeth are…" # @t_smeowkie047.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "She seems cute, but I’d better not underestimate her!)" # @t_smeowkie048.00 self.block='Last'
                jump s_day0_meowkie_cleanup
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_meowkie_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_meowkie_akimbo_grin_badge as meowkie:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_meowkie_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide meowkie
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'mrdriller', 'kind': 'Macro'} ''>
    label s_day0_mrdriller:
        # <Macro Macro {'name': 'mrdriller', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_mrdriller_warm:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin zorder 2:
                # ActorEvent
                xpos 0.3 
                alpha 0.0
                linear 0.5 alpha 1.0
            show i_mrdriller_slumped_sad as mrdriller zorder 2:
                default
                xpos 0.7 
                alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(There’s that cute excitable guy." # @t_smrdriller00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_mrdriller_slumped_sad as mrdriller:
            # FadeEvent
            linear 1.0 alpha 1.0
        extend "{w=1.0}{nw}"
        extend " Mr. Driller, I think his name was?" # @t_smrdriller00.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Wait, that can’t be his NAME…." # @t_smrdriller01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        extend " Unless his first name is Mister?!)" # @t_smrdriller01.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_mrdriller "SIIIGH…" # @t_smrdriller02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Huh?" # @t_smrdriller03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " He actually just said “Sigh” out loud…)" # @t_smrdriller03.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_mrdriller "SIIIIIIIIIIIIIGH…." # @t_smrdriller04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Hey, um… Mr. Driller?" # @t_smrdriller05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Are you okay?" # @t_smrdriller06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_mrdriller_drillup_sad as mrdriller
        t_ch_mrdriller "Oh, yeah…" # @t_smrdriller07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " I’m fine. It’s no big deal." # @t_smrdriller07.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " I don’t really want to talk about it." # @t_smrdriller07.02 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "Are you sure?" # @t_smrdriller08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Because it seemed kinda like you wanted to-" # @t_smrdriller08.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_mrdriller_drillup_crying as mrdriller
        show i_cousin_default_surprised as cousin
        t_ch_mrdriller "Ok yes I’ll tell you! I love to dig and drill, like seriously LOVE IT, but my Dad Principal DigDug won’t let me and he thinks that’s why mom left, because of all the digging he was doing, so he thinks its bad to dig, BUT I love to dig, my name is MR. DRILLER for crying out loud, I have a bunch of drills that are specifically FOR digging and drilling, and its SO UNFAIR! it’s such a WASTE not to dig, but dad thinks it’ll ruin my life just like it ruined HIS life and I just can’t stand it anymore, it’s tearing me up inside and I don’t know what to do! AUGH!" # @t_smrdriller09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_mrdriller_slumped_cry as mrdriller
        extend "{w=0.5}{nw}"
        t_ch_mrdriller "(BREATHE)" # @t_smrdriller010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "Um. Okay." # @t_smrdriller011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "And…" # @t_smrdriller012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_neutral as cousin
        extend " That’s why you’re in detention?" # @t_smrdriller012.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_mrdriller "No. I’m in detention because I defaced a statue." # @t_smrdriller013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_mrdriller_slumped_smug as mrdriller
        extend " You know… the one of my dad Dig Dug that’s in the school courtyard." # @t_smrdriller013.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "Defaced it?" # @t_smrdriller014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " How?!" # @t_smrdriller014.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_mrdriller_drillup_happy as mrdriller
        t_ch_mrdriller "Um… by drilling." # @t_smrdriller015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_mrdriller_drillup_happy as mrdriller
        extend " You know, with these drills I have…" # @t_smrdriller015.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_mrdriller_drillup_smug as mrdriller
        t_ch_mrdriller "Because I’m MR. DRILLER?!" # @t_smrdriller016.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_grin_blush as cousin
        t_ch_cousin "Haha. Oh yeah." # @t_smrdriller017.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Sorry." # @t_smrdriller017.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_mrdriller_slumped_sad as mrdriller
        t_ch_mrdriller "SIGH…" # @t_smrdriller018.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " No, I’m sorry." # @t_smrdriller018.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_mrdriller "I’ve been snapping like that a lot lately!" # @t_smrdriller019.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " You don’t deserve that!" # @t_smrdriller019.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_mrdriller "I’ve just been under a lot of stress…" # @t_smrdriller020.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        t_ch_cousin "(Jeez, talk about baggage." # @t_smrdriller021.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " It’s like, “Mr. Driller to the baggage claim, your baggage is a big crazy drama mess.”" # @t_smrdriller021.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "He is pretty adorable though," # @t_smrdriller022.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral_blush as cousin
        extend " in an awkward sort of way." # @t_smrdriller022.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Besides, when a cute guy like that is going through a hard time," # @t_smrdriller023.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " sometimes you just wanna be the rock they can lean on." # @t_smrdriller023.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Heh heh.. Get it…" # @t_smrdriller024.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_grin_blush as cousin
        t_ch_cousin "Drilling… Rocks…" # @t_smrdriller025.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "…" # @t_smrdriller026.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " I’m glad I didn’t say that one out loud.)" # @t_smrdriller026.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_mrdriller_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_mrdriller_slumped_sad as mrdriller:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_grin_blush as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_mrdriller_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide mrdriller
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'nidia', 'kind': 'Macro'} ''>
    label s_day0_nidia:
        # <Macro Macro {'name': 'nidia', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_nidia_warm:
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
        t_ch_cousin "Hi there!" # @t_snidia00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_nidia "Oh! Fascinating ..." # @t_snidia01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " I wonder what it means!" # @t_snidia01.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_nidia_notepad_worried as nidia
        t_ch_nidia "It could mean this ... Or it could mean this ..." # @t_snidia02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_nidia "What if it means THIS?!" # @t_snidia03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Um ... Hello?!" # @t_snidia04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_nidia_akimbo_surprised as nidia
        t_ch_nidia "Ah! Sorry!" # @t_snidia05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Sometimes I get carried away!" # @t_snidia05.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_nidia "Trying to parse the words of the Ancients in a modern context is tricky business. Sometimes 'dragon' is a metaphor, but sometimes a dragon is just a dragon." # @t_snidia06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_nidia "Y'know?" # @t_snidia07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "ABSOLUTELY NOT. I don't know at all!!" # @t_snidia08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_nidia_akimbo_happy as nidia
        t_ch_nidia "Like... Sometimes magic is a feeling you get, but sometimes magic is something you use to fortify your stats..." # @t_snidia09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "...... Not getting it...." # @t_snidia010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_nidia "You know, so you're stronger or faster or... ?" # @t_snidia011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "I just drink a lot of milk to get stronger." # @t_snidia012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_nidia "Like... mandrake milk?" # @t_snidia013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_exhausted_neutral as cousin
        t_ch_cousin "N-no... Just normal milk." # @t_snidia014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_nidia_notepad_surprised as nidia
        t_ch_nidia "VERY interesting..." # @t_snidia015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(She went back to her notes... Maybe I'd better leave her alone for now.)" # @t_snidia016.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_nidia_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_nidia_notepad_surprised as nidia:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_exhausted_neutral as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_nidia_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide nidia
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'richard', 'kind': 'Macro'} ''>
    label s_day0_richard:
        # <Macro Macro {'name': 'richard', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_richard_warm:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_cousin_default_neutral as cousin zorder 2:
                # ActorEvent
                xpos 0.3 
                alpha 0.0
                linear 0.5 alpha 1.0
            show i_miller_notebook_contemplative as miller zorder 2:
                default
                xpos 0.7 
                alpha 0.0
                linear 0.5 alpha 1.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_richard "Conspiracy Log." # @t_srichard00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_notebook_serious as miller
        t_ch_richard "Entry. Um. One." # @t_srichard01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_richard "I have tracked target to the so-called Detention Room." # @t_srichard02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Uh? Is he talking about me???)" # @t_srichard03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_notebook_halfgrin as miller
        t_ch_richard "Target is ruggedly handsome in a secret agent kind of way." # @t_srichard04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "(He is!)" # @t_srichard05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_notebook_contemplative as miller
        t_ch_richard "Also blond, tall, and most likely human." # @t_srichard06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "(.........Oh. Someone else then.)" # @t_srichard07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " Uh, hey, Richard?" # @t_srichard07.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_pondering_shocked as miller
        t_ch_richard "Who told you?" # @t_srichard08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Uh. You did. At roll call." # @t_srichard09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_pondering_contemplative as miller
        t_ch_richard "Hm. Okay." # @t_srichard010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_richard "Hang on. I don’t have a file on you, New Kid." # @t_srichard011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "It’s [slot_playerName], actually." # @t_srichard012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_notebook_contemplative as miller
        t_ch_richard "Ah, thanks. Perfect. [slot_playerName]. This’ll just take a second." # @t_srichard013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "What are you writing down?" # @t_srichard014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_notebook_serious as miller
        t_ch_richard "Your vitals. For future cross referencing to figure out where you fit into the grand conspiracy of world domination." # @t_srichard015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "Oh." # @t_srichard016.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Um, but isn’t that crazy though?" # @t_srichard017.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_miller_notebook_laugh as miller
        t_ch_richard "Ha!" # @t_srichard018.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_richard "That’s what you’d want me to think." # @t_srichard019.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(It kind of is, yeah.)" # @t_srichard020.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_richard_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_miller_notebook_laugh as miller:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_richard_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide miller
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'taira', 'kind': 'Macro'} ''>
    label s_day0_taira:
        # <Macro Macro {'name': 'taira', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_taira:
            # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_taira}', 'kind': 'IfFalse'} ''>
            label s_day0_taira_firstDialouge:
                # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_taira}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_taira_firstDialouge_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_taira_default_confused as taira zorder 2:
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
                t_ch_cousin "(That scary guy..." # @t_staira00.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Maybe I should just steer clear of him...)" # @t_staira00.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_default_serious as taira
                t_ch_taira "HEY!" # @t_staira01.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " New kid!" # @t_staira01.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Haw! Never thought a little twerp like you’d be in detention!" # @t_staira01.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "So… your name is “Taira no Kagekiyo”, right?" # @t_staira02.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " But… you go by “Taira”?" # @t_staira02.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_serious as taira
                t_ch_taira "Uh, yeah. Don’t wear it out!" # @t_staira03.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "But…correct me if I’m wrong… but doesn’t that name basically mean… “Kagekiyo, of Taira”?" # @t_staira04.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                extend " So wouldn’t you go by the “Kagekiyo” part instead?" # @t_staira04.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_default_confused as taira
                t_ch_taira "Yo! What’s with the mad personal questions all of a sudden?!" # @t_staira05.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You sweet on me, or something?!" # @t_staira05.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_default_confused as taira:
                    # ShowWithAtl
                    ease_expo .25 xpos 0.5 
                extend "{w=0.25}{nw}"
                t_ch_taira "What I call myself isn’t your BUSINESS, alright?!" # @t_staira06.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_surprise as cousin
                t_ch_cousin "GAH!" # @t_staira07.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_default_confused as taira:
                    # ShowWithAtl
                    ease_expo .25 xpos 0.7 
                extend "{w=0.25}{nw}"
                extend " (H-He looks even more like a monster when he sticks his face up in my face like that!)" # @t_staira07.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_taira "Yo... what’s up with that?!" # @t_staira08.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "H-huh...?" # @t_staira09.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_akimbo_confused as taira
                t_ch_taira "Screaming when I said hi..." # @t_staira010.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Goin’ all pale..." # @t_staira010.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Jumping like you saw a ghost..." # @t_staira010.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_neutral as cousin
                t_ch_cousin "I... I wasn’t THAT bad, was I..." # @t_staira011.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_revenge_confused as taira
                t_ch_taira "What’d you act like that for?" # @t_staira012.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You gotta problem with me or something?!" # @t_staira012.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " What the heck! We just met!" # @t_staira012.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " You gotta have more politeness and stuff!" # @t_staira012.03 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "It w-was... nothing..." # @t_staira013.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_steveholt_angry as taira
                t_ch_taira "YO, YOU MAKIN’ FUN OF ME, NEW KID?!" # @t_staira014.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_taira "I’M GONNA GET A REVENGE ON YOU FOR THAT!" # @t_staira015.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "N-no!" # @t_staira016.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "It was just..." # @t_staira017.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "your face!" # @t_staira018.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_taira "My..." # @t_staira019.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " My face...?" # @t_staira019.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "(Why did I say that out loud..." # @t_staira020.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Well, I’ve had a nice life, I guess...)" # @t_staira020.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_steveholt_pleading as taira
                t_ch_taira "You think I’m ugly or something....?" # @t_staira021.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Jeez, he still looks mad, but..." # @t_staira022.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " He also looks like he’s about to totally break down in tears!" # @t_staira022.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Pull yourself together, man!" # @t_staira022.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " ...I’m glad I didn’t say that out loud this time.)" # @t_staira022.03 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_taira "….." # @t_staira023.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_surprised as cousin
                t_ch_cousin "No... you’re not ugly!" # @t_staira024.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "It’s just..." # @t_staira025.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Y-your face was..." # @t_staira025.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_surprise as cousin
                t_ch_cousin "It was just way too cool!" # @t_staira026.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I couldn’t look at it up close for too long!" # @t_staira026.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_taira "...Wha..." # @t_staira027.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(I’ve done it now." # @t_staira028.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " There’s no way even a meathead like this guy would be dumb enough to fall for that.)" # @t_staira028.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_taira "You think my face is..." # @t_staira029.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " cool?" # @t_staira029.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_taira_steveholt_happy_blush as taira
                t_ch_taira "Haw haw... jeez..." # @t_staira030.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "(No..." # @t_staira031.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " No way..." # @t_staira031.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Not only did he buy it, but I think he..." # @t_staira031.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "He...)" # @t_staira032.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_taira "Your face is pretty cool too, or whatever!" # @t_staira033.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_grin as cousin
                t_ch_cousin "H-heh... Thanks..." # @t_staira034.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " (What have I gotten myself into..." # @t_staira034.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I just wanna get through my first week of high school unscathed!)" # @t_staira034.02 self.block='Last'
                jump s_day0_taira_cleanup
        if scene_picked_once_taira:
            # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_taira}', 'kind': 'IfTrue'} ''>
            label s_day0_taira_loopDialogue:
                # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_taira}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_taira_loopDialogue_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_taira_akimbo_happy_blush as taira zorder 2:
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
                show i_taira_akimbo_happy_blush as taira
                t_ch_taira "… Hey, [slot_playerName]… it’s pretty cool what you said about my face and all…" # @t_staira035.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_taira "HAW HAW! LOOK AT ME, ALL NERVOUS!" # @t_staira036.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " YOU’RE SOMETHIN’ ELSE, CUZ!" # @t_staira036.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Oof!" # @t_staira037.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(For someone so “nervous” he’s sure slapping me on the back pretty hard…" # @t_staira038.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Maybe he just… doesn’t know his own strength?)" # @t_staira038.01 self.block='Last'
                jump s_day0_taira_cleanup
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_taira_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_taira_akimbo_happy_blush as taira:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_taira_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide taira
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'terezi', 'kind': 'Macro'} ''>
    label s_day0_terezi:
        # <Macro Macro {'name': 'terezi', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        if not scene_picked_once_terezi:
            # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_terezi}', 'kind': 'IfFalse'} ''>
            label s_day0_terezi_firstDialouge:
                # <IfFalse IfFalse {'name': 'firstDialouge', 'value': '${scene:picked_once_terezi}', 'kind': 'IfFalse'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_terezi_firstDialouge_warm:
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
                t_ch_cousin "(Who the heck is that weird gray girl?" # @t_sterezi00.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " She’s one of those exchange students…" # @t_sterezi00.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " No one else in detention seems to want to talk to them." # @t_sterezi00.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "I think Dig Dug said her name was... Terezi?" # @t_sterezi01.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " She’s got sharp fangs and horns…" # @t_sterezi01.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral_blush as cousin
                extend " What’s her deal, anyway?!" # @t_sterezi01.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified_blush as cousin
                t_ch_cousin "She’s kinda cute, in a scary way…" # @t_sterezi02.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " But maybe I should avoid the weird kids too…" # @t_sterezi02.01 self.block='Last'
                show i_terezi_default_grin as terezi:
                    # ShowWithAtl
                    linear 0.30 xpos 0.49 
                show i_cousin_default_neutral as cousin:
                    # ShowWithAtl
                    linear 0.10 xpos 0.25 
                # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_mortified as cousin:
                    # ShowWithAtl
                    linear 0.20 xpos 0.25 
                extend "{w=0.2}{nw}"
                t_ch_cousin "OOF! OW!" # @t_sterezi03.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "She bumped into me!)" # @t_sterezi04.00 self.block='Last'
                show i_terezi_default_grin as terezi:
                    # ShowWithAtl
                    linear 0.30 xpos 0.7 
                # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "H3H3H3… OOPS" # @t_sterezi05.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " SORRY!" # @t_sterezi05.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "(She doesn’t sound sorry at all!)" # @t_sterezi06.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_mortified as cousin
                t_ch_cousin "Why don’t you watch where you’re going?!" # @t_sterezi07.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_huh as terezi
                t_ch_terezi "HMM PROB4BLY B3C4US3 1 C4NT W4TCH 4NYTH1NG" # @t_sterezi08.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "1M BL1ND!" # @t_sterezi09.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "WOW WHY 4R3 YOU SOOOOOOO 1NS3NS1T1V3 [slot_playerName]" # @t_sterezi010.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi
                extend " TH4TS PROB4BLY WHY 3V3RYON3S 4LW4YS T4LK1NG 4BOUT HOW T3RR1BL3 YOU 4R3 >:]" # @t_sterezi010.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "W-what?!" # @t_sterezi011.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "Omigosh…" # @t_sterezi012.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I’m SO sorry!!" # @t_sterezi012.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                extend " I had no idea…" # @t_sterezi012.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "(There’s something weird about how she talks..." # @t_sterezi013.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " But I sure can’t say anything about that now!" # @t_sterezi013.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "Not with everyone already thinking I’m insensitive…" # @t_sterezi014.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                extend " Wait, who said that about me?! Oh no…)" # @t_sterezi014.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_laugh as terezi
                t_ch_terezi "H3H3H3 3V3RYON3 H3R3 1S SO GULL1BL3" # @t_sterezi015.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi
                t_ch_terezi "1T’S K1ND4 CUT3 BUT TH4T K1ND4 TH1NG G3TS OLD F4ST…" # @t_sterezi016.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi
                extend " SO W1S3 UP, OK4Y? >:P" # @t_sterezi016.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "1’M T3R3Z1." # @t_sterezi017.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Uh, hi Terezi." # @t_sterezi018.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "So…" # @t_sterezi019.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "You’re not REALLY blind?" # @t_sterezi020.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " That’s kind of a messed up thing to pretend to be…" # @t_sterezi020.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi
                t_ch_terezi "NO 1’M D3F1N1T3LY BL1ND" # @t_sterezi021.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_laugh as terezi
                extend " 1 DON’T JUST W34R TH3S3 GL4SS3S B3C4US3 TH3Y’R3 TH3 COOL3ST TH1NG 3V3R!" # @t_sterezi021.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi
                t_ch_terezi "BUT 1 C4N SM3LL 4ND T4ST3 TH3 COLORS OF 3V3RYTH1NG 4ROUND M3 4ND SORT4 “S33” TH4T W4Y" # @t_sterezi022.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " L1K3 TH4T D3L1C1OUS F34TH3RY BLU3B3RRY MUFF1N OV3R TH3R3" # @t_sterezi022.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " 4ND TH4T 3GGPL4NTY GUY, H3 SM3LLS PR3TTY W31RD… BUT 1NT3R3ST1NG >:]" # @t_sterezi022.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(I guess she means Blue Max and Anti-Bravoman…" # @t_sterezi023.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " Weird…)" # @t_sterezi023.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "4ND… YOU" # @t_sterezi024.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "M-me?" # @t_sterezi025.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " What do I … smell like?" # @t_sterezi025.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                extend " Do I even want to know…?" # @t_sterezi025.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "Y34H TH4T’S WHY 1 BUMP3D 1NTO YOU ON PURPOS3 DUMMY" # @t_sterezi026.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " 1 W4S G3TT1NG 4 B3TT3R WH1FF >:]" # @t_sterezi026.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi:
                    # ShowWithAtl
                    linear 0.20 xpos 0.65 
                extend "{w=0.2}{nw}"
                t_ch_terezi "YOU SM3LL … N1C3" # @t_sterezi027.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " P1NK L1K3 COTTON C4NDY" # @t_sterezi027.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " OR M4YB3 L1K3 FROST1NG?" # @t_sterezi027.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi:
                    # ShowWithAtl
                    linear 0.20 xpos 0.6 
                extend "{w=0.2}{nw}"
                t_ch_terezi "H3H3H3… TH1S W4RR4NTS FURTH3R 1NV3ST1G4T1ON" # @t_sterezi028.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(Huh? What does that…" # @t_sterezi029.00 self.block='Last'
                show i_terezi_default_grin as terezi:
                    # ShowWithAtl
                    linear 0.20 xpos 0.5 
                # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_mortified_blush as cousin
                t_ch_cousin "GAHHH!!!" # @t_sterezi030.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " She LICKED me!!!)" # @t_sterezi030.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_laugh as terezi:
                    # ShowWithAtl
                    linear 0.3 xpos 0.7 
                extend "{w=0.3}{nw}"
                t_ch_terezi "H3H3H3 Y34H D3F1N1T3LY COTTON C4NDY" # @t_sterezi031.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified_blush as cousin
                t_ch_cousin "I’m… just gonna assume…" # @t_sterezi032.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " That you’re an exchange student…" # @t_sterezi032.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " And that kinda behavior is normal in whatever country you’re from…" # @t_sterezi032.02 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "WOW BR1LL14NT D3DUCT1ON, COTTON C4NDY" # @t_sterezi033.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi
                t_ch_terezi "Y3S 1’M NOT FROM H3R3" # @t_sterezi034.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " 1’M 4CTU4LLY 4 TROLL FROM 4 D1FF3R3NT PL4N3T" # @t_sterezi034.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_resigned as terezi
                t_ch_terezi "1T’S K1ND4 4 LONG STORY…" # @t_sterezi035.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "4 LONG, LOOOOOOOONG STORY" # @t_sterezi036.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "(Troll? Different planet?!" # @t_sterezi037.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I… But…" # @t_sterezi037.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_exhausted_mortified as cousin
                t_ch_cousin "You know what… I don’t have the energy to even want to get into this right now.)" # @t_sterezi038.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi
                t_ch_terezi "WH3R3 1 COM3 FROM 3V3RYBODY’S BL1ND" # @t_sterezi039.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " 3V3RY S1NGL3 ON3 OF US TROLLS C4N SM3LL COLORS L1K3 M3" # @t_sterezi039.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi
                t_ch_terezi "1F YOU W4NT TO B3 CULTUR4LLY S3NS1T1V3 YOU B3TT3R DO 1T TOO" # @t_sterezi040.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "1T’S 34S13R TO SM3LL WH3N YOU C4NT’ S33, SO HOLD ST1LL 4ND 1'LL POK3 OUT YOUR 3Y3S" # @t_sterezi041.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "NO N33D TO TH4NK M3 >:]" # @t_sterezi042.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "…" # @t_sterezi043.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "..." # @t_sterezi044.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_mortified as cousin
                t_ch_cousin "You’re messing with me again, aren’t you?" # @t_sterezi045.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_laugh as terezi
                t_ch_terezi "H3H3H3 CONGR4TUL4T1ONS COTTON C4NDY" # @t_sterezi046.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi
                t_ch_terezi "YOU’R3 NOT 4 COMPL3T3 1MB3C1L3!" # @t_sterezi047.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral_blush as cousin
                t_ch_cousin "Heh… thanks." # @t_sterezi048.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "SO H3Y WH1L3 W3’R3 ON TH3 SUBJ3CT OF YOU" # @t_sterezi049.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "YOU 4R3 TH3 ON3 WHO ROLL3D UP TH3 WHOL3 SCHOOL…" # @t_sterezi050.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "1N 4 B1G D3L1C1OUS B4LL, W1TH 4LL TH3 COLORS OF YOUR 34RTH “R41NBOW”???" # @t_sterezi051.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "TH4T W4S YOU R1GHT???" # @t_sterezi052.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral as cousin
                t_ch_cousin "Uh, yeah…" # @t_sterezi053.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_sad as cousin
                extend " I’m really, really sorry about that." # @t_sterezi053.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi
                t_ch_terezi "H3H3 1 KN3W TH4T" # @t_sterezi054.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi
                extend " 1N COURT TH3 PROS3CUTOR ONLY 4SKS QU3ST1ONS SH3 4LR34DY KNOWS TH3 4NSW3R TO" # @t_sterezi054.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_surprised as cousin
                t_ch_cousin "Huh??" # @t_sterezi055.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "SOOOOO, COTTON C4NDY…" # @t_sterezi056.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi:
                    # ShowWithAtl
                    linear 0.20 xpos 0.65 
                extend "{w=0.2}{nw}"
                extend " 1 WOND3R WH4T COLOR YOUR BLOOD 1S" # @t_sterezi056.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_lean_grin as terezi:
                    # ShowWithAtl
                    linear 0.20 xpos 0.6 
                extend "{w=0.2}{nw}"
                t_ch_terezi "1S 1T P1NK TOO? 1 HOP3 1 G3T TO T4ST3 1T SOM3D4Y >:]" # @t_sterezi057.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "What the heck?!" # @t_sterezi058.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_energetic_mortified as cousin
                extend " My BLOOD?!" # @t_sterezi058.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "Are you… Are you threatening me or something?!" # @t_sterezi059.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " What did I do?!" # @t_sterezi059.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_laugh as terezi
                t_ch_terezi "THR34T3N1NG? YOU S3R1OUSLY TH1NK TH4T'S WH4T TH4T W4S?" # @t_sterezi060.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_laugh as terezi:
                    # ShowWithAtl
                    linear 0.30 xpos 0.7 
                extend "{w=0.3}{nw}"
                t_ch_terezi "H3H3H3 WOW HOW 3MB4RR4SS1NG FOR YOU" # @t_sterezi061.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "BUT 4LSO 1T’S K1ND4 CUT3, 1N 4 P4TH3T1C W4Y!" # @t_sterezi062.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi
                t_ch_terezi "YOU MUST NOT KNOW 4 S1NGL3 TH1NG…" # @t_sterezi063.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "4BOUT T4LK1NG TO L4D13S <3" # @t_sterezi064.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_cousin "(...Yikes.)" # @t_sterezi065.00 self.block='Last'
                jump s_day0_terezi_cleanup
        if scene_picked_once_terezi:
            # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_terezi}', 'kind': 'IfTrue'} ''>
            label s_day0_terezi_loopDialogue:
                # <IfTrue IfTrue {'name': 'loopDialogue', 'value': '${scene:picked_once_terezi}', 'kind': 'IfTrue'} ''>
                # <Events events {'kind': 'events'} ''>
                # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                label s_day0_terezi_loopDialogue_warm:
                    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
                    # <Events events {'kind': 'events'} ''>
                    show i_cousin_default_neutral as cousin zorder 2:
                        # ActorEvent
                        xpos 0.3 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    show i_terezi_default_laugh as terezi zorder 2:
                        default
                        xpos 0.7 
                        alpha 0.0
                        linear 0.5 alpha 1.0
                    $ renpy.pause(0.5, hard=True) # TimedPause
                # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_laugh as terezi
                t_ch_terezi "YOU KNOW 1’M JUST PL4Y1NG 4ROUND R1GHT?" # @t_sterezi066.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_grin as terezi
                t_ch_terezi "YOU 4CTU4LLY S33M PR3TTY COOL" # @t_sterezi067.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                t_ch_terezi "W3 SHOULD H4NG OUT SOM3T1M3!" # @t_sterezi068.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_neutral_blush as cousin
                t_ch_cousin "…" # @t_sterezi069.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_cousin_default_mortified as cousin
                t_ch_cousin "This is a trick, right?" # @t_sterezi070.00 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                extend " I... can’t tell if this is a trick." # @t_sterezi070.01 self.block='Last'
                # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
                # <Events events {'kind': 'events'} ''>
                show i_terezi_default_laugh as terezi
                t_ch_terezi "H3H3H3!" # @t_sterezi071.00 self.block='Last'
                jump s_day0_terezi_cleanup
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_terezi_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_terezi_default_laugh as terezi:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_mortified as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_terezi_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide terezi
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'tomari', 'kind': 'Macro'} ''>
    label s_day0_tomari:
        # <Macro Macro {'name': 'tomari', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_tomari_warm:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_tomari_notebook_thinking as tomari zorder 2:
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
        t_ch_tomari "X34 minus 5R1 plus 6-X36…" # @t_stomari00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Everyone else looks like trouble. What’s this guy doing in here?)" # @t_stomari01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_tomari_notebook_mortified as tomari
        t_ch_tomari "Carry the one…" # @t_stomari02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(Is he…)" # @t_stomari03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "(He’s doing his homework?!)" # @t_stomari04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_tomari "No, wait. Carry the coefficient of friction! Of course! Gah, what was I thinking?!" # @t_stomari05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(What kind of trouble could this guy get himself into?)" # @t_stomari06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "(Unpaid library fine?)" # @t_stomari07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_tomari_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_tomari_notebook_mortified as tomari:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_neutral as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_tomari_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide tomari
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice
    # <Macro Macro {'name': 'valk', 'kind': 'Macro'} ''>
    label s_day0_valk:
        # <Macro Macro {'name': 'valk', 'kind': 'Macro'} ''>
        # <Events events {'kind': 'events'} ''>
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'warm', 'kind': 'ParallelEvent'} ''>
        label s_day0_valk_warm:
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
        t_ch_valkyrie "Hey cutie!" # @t_svalk00.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(She must be talking to someone else... I'll just play it cool...)" # @t_svalk01.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(....)" # @t_svalk02.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_valkyrie_default_grin as valkyrie
        t_ch_cousin "(.................)" # @t_svalk03.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_valkyrie_akimbo_grin as valkyrie
        t_ch_valkyrie "Helloooooo!" # @t_svalk04.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(!!" # @t_svalk05.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        extend " She IS talking to me.)" # @t_svalk05.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Me?" # @t_svalk06.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_valkyrie_akimbo_wink as valkyrie
        t_ch_valkyrie "What's that little heart for?" # @t_svalk07.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "Heart?" # @t_svalk08.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_valkyrie_akimbo_wink as valkyrie:
            # ShowWithAtl
            linear .1 xpos 0.65 
            # ShowWithAtl
            pause 0.1 
            linear .1  xpos 0.7 
        show i_cousin_energetic_surprise as cousin
        extend "{w=0.2}{nw}"
        extend " OW!" # @t_svalk08.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_cousin "(She flicked my antenna!)" # @t_svalk09.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_neutral as cousin
        t_ch_cousin "(......)" # @t_svalk010.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_neutral as cousin
        t_ch_cousin "(No one's ever done that before... )" # @t_svalk011.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_valkyrie_forjustice_grin as valkyrie
        t_ch_valkyrie "Are you a lover or a fighter? IDK…" # @t_svalk012.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_valkyrie_forjustice_thoughtful as valkyrie
        extend " You look like too much of a noob to be a fighter..." # @t_svalk012.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_mortified as cousin
        t_ch_cousin "H-hey!" # @t_svalk013.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " (Wh-what's her deal?!)" # @t_svalk013.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_valkyrie_forjustice_grin as valkyrie
        t_ch_valkyrie "The thing is... There's all kinds of lovers. Anyone with a brain'd be suspicious." # @t_svalk014.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_valkyrie "You some kind of Player 1?" # @t_svalk015.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised_blush as cousin
        t_ch_cousin "What?!" # @t_svalk016.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        extend " (Am I blushing? What's with this girl?!)" # @t_svalk016.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_valkyrie_forjustice_wink as valkyrie
        t_ch_valkyrie "Takes one to know one, am I right?" # @t_svalk017.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "(You don't know me at all!)" # @t_svalk018.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_valkyrie "Now you're thinking, 'You don't know me at all'..." # @t_svalk019.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_energetic_mortified as cousin
        t_ch_cousin "(HOW DID SHE DO THAT)" # @t_svalk020.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_valkyrie "OWNED." # @t_svalk021.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_valkyrie "J/K..." # @t_svalk022.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        t_ch_valkyrie "If you DO want to know me at all…  You should join wood shop tomorrow." # @t_svalk023.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_valkyrie_forjustice_wink as valkyrie:
            # ShowWithAtl
            linear 0.25 alpha 0.0
        extend "{w=0.25}{nw}"
        extend " See ya!" # @t_svalk023.01 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised as cousin
        t_ch_cousin "(That girl is way too fast to keep up with!)" # @t_svalk024.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_cousin_default_surprised_blush as cousin
        with Dissolve(0.333)
        t_ch_cousin "(But it's kind of fun... )" # @t_svalk025.00 self.block='Last'
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
        label s_day0_valk_cleanup:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'cleanup', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            show i_valkyrie_forjustice_wink as valkyrie:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            show i_cousin_default_surprised_blush as cousin:
                # ShowWithAtl
                linear 0.5 alpha 0.0
            $ renpy.pause(0.5, hard=True) # TimedPause
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
        label s_day0_valk_reset:
            # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'reset', 'kind': 'ParallelEvent'} ''>
            # <Events events {'kind': 'events'} ''>
            hide valkyrie
            # Pass (ActorReset)
            # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
        jump s_day0_day0prechoice