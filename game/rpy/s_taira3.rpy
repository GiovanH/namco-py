# <Scene {'id': 's_taira3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_taira3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_taira3"
    $ renpy.pause(1)
    # <Scene {'id': 's_taira3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/school.ogg" loop
    show i_bg_classroom_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 4:
        default
        xpos 0.2 
    show i_taira_steveholt_serious as taira zorder 1:
        default
        xpos 0.5 
    show i_digdug_left as digdug zorder 2:
        default
        xpos 0.3 
        alpha 0.0
    show i_aki_default_distracted as aki zorder 2:
        default
        xpos 0.82 
        alpha 0.0
    show i_bluemax_stand_smile as bluemax zorder 3:
        default
        alpha 0.0
        xpos 0.3 
    show i_meowkie_normal_happy as meowkie zorder 2:
        default
        alpha 0.0
        xpos 0.78 
    t_ch_cousin "Alright alright." # @t_staira311.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ll sit with you." # @t_staira311.01 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "YEAH! IN YOUR FAAACE!" # @t_staira312.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_frown_badge as meowkie:
        xzoom -1.0 
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_meowkie "U-umm, we’re not supposed to yell in detention…" # @t_staira313.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_confused as taira
    t_ch_taira "Oh, yo! Sorry, Meowkie!" # @t_staira314.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Ha ha, you got in trouble…" # @t_staira315.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused as taira
    t_ch_taira "Sh-shut up!" # @t_staira316.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ll… I’ll get your face in trouble!" # @t_staira316.01 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ooh, nice comeback." # @t_staira317.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_pleading as taira
    t_ch_taira "Yo! Cuz, why are you being so mean to me?!" # @t_staira318.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Aw! Calm down, big guy!" # @t_staira319.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m just teasing you… That’s what friends do." # @t_staira320.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Friends…?" # @t_staira321.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "HAW HAW YEAH!!! FRIENDS! AWESOME!!" # @t_staira322.00 self.block='Last'
    # UNHANDLED TAG <HardSwap {'lastActor': 'meowkie', 'name': '_E', 'nextActor': 'aki'} HardSwap ''>
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_focus as aki
    t_ch_aki "Taira! Some of us are trying to study." # @t_staira323.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_confused as taira
    t_ch_taira "Oops!" # @t_staira324.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_focus as aki:
        # FadeEvent
        linear 0.33 alpha 0.0
    extend "{w=0.33}{nw}"
    t_ch_cousin "Heh heh…" # @t_staira325.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Taira’s pretty fun to hang out with…" # @t_staira325.01 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m glad I decided to sit with him." # @t_staira325.02 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s helping the time pass pretty easily…)" # @t_staira326.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Hey Cuz… did you see that?" # @t_staira327.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    extend " That Blue Max nerd just walked right out of detention room!" # @t_staira327.01 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Huh? Yeah, I guess…" # @t_staira328.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So what?" # @t_staira328.01 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I’m way surprised at you, [slot_playerName]!" # @t_staira329.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s, like, way against the rules!" # @t_staira329.01 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "You care about rules all of a sudden?" # @t_staira330.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Rules are mad important, yo!" # @t_staira331.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " C’mon, let’s go get some revenge on that guy!" # @t_staira331.01 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Wait-" # @t_staira332.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Taira!" # @t_staira332.01 self.block='Last'
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.33 alpha 0.0
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(He’s actually getting up and following Blue Max out?" # @t_staira333.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Doesn’t that mean he’s breaking the rules too?" # @t_staira333.01 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well, he can go do whatever he wants." # @t_staira334.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just because we’re sort of friends doesn’t mean I have to follow him around." # @t_staira334.01 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "…" # @t_staira335.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That dumb oaf…" # @t_staira336.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He’ll probably just end up getting distracted by paint drying on the wall, haha." # @t_staira336.01 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_staira337.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_staira338.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or trip over and hurt himself…" # @t_staira338.01 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Or go into a revenge rage…" # @t_staira339.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or…" # @t_staira339.01 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Or…" # @t_staira340.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_staira341.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Alright, right! I’ll go after him! I doubt anyone will notice me slip out..." # @t_staira342.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_hallway_a as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_a', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_m'} SettingChange ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.17 
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Okay. That was easy enough." # @t_staira343.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Now where’s Taira?" # @t_staira343.01 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_angry as taira:
        # ShowWithAtl
        linear 0.5 xpos 0.62 
        # FadeEvent
        linear 0.33 alpha 1.0
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        linear 0.5 xpos 0.77 
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_taira "Whaddya got to say for yourself, you little blue punk?!" # @t_staira344.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "… Wh-what?!" # @t_staira345.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I saw you sneakin’ outta detention, bro!" # @t_staira346.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    extend " What, you think I’m blind or something?!" # @t_staira346.01 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "What?!" # @t_staira347.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You told me to meet you out here!" # @t_staira347.01 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Huh?" # @t_staira348.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Did Taira…" # @t_staira349.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " forget" # @t_staira349.01 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " that he did that?!" # @t_staira349.02 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "He’s not THAT stupid…)" # @t_staira350.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "That’s right, bro." # @t_staira351.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You had to meet me for an appointment…" # @t_staira351.01 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_angry as taira
    t_ch_taira "A REVENGE-APPOINTMENT!" # @t_staira352.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(It would’ve been cooler to say “an appointment with revenge”..." # @t_staira353.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "...but not by much.)" # @t_staira354.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_shock as bluemax
    t_ch_max "Revenge?! For what?!" # @t_staira355.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I didn’t do anything!" # @t_staira355.01 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_worried as bluemax:
        # ShowWithAtl
        linear .2 xpos 0.89 
    extend "{w=0.2}{nw}"
    extend " C’mon, I can just give you my lunch money like always..." # @t_staira355.02 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Tryin’ to out-thought me with your brain twisters, huh?" # @t_staira356.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Joke’s on you, bro!" # @t_staira356.01 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I’m a warrior with a fighting heart…" # @t_staira357.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_revenge as taira
    extend " THAT BURNS THROUGH DECEIT!" # @t_staira357.01 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "…" # @t_staira358.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        linear .2 xpos 0.79 
    extend "{w=0.2}{nw}"
    extend " Please don’t break my goggles…" # @t_staira358.01 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(What should I do?!" # @t_staira359.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He’s scary when he gets like this…" # @t_staira359.01 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And besides. If he wants revenge-" # @t_staira360.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Blue Max must have done something bad to him." # @t_staira361.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...Right?!)" # @t_staira361.01 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "You scored higher than me on yesterday’s history test, bro!" # @t_staira362.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "That’s a great disrespect to me…" # @t_staira363.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " AND my clan!" # @t_staira363.01 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "WHAT?! That’s impossible!" # @t_staira364.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I only got a C+ on that test!" # @t_staira365.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Exactly, bro!" # @t_staira366.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You think you’re better than me, huh??" # @t_staira366.01 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "For that…" # @t_staira367.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_revenge as taira
    t_ch_taira "I’ll have MAD REVENGE!" # @t_staira368.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_shocked as bluemax
    t_ch_max "Wah! Put me down!" # @t_staira369.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Mayday! Mayday!" # @t_staira369.01 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(OMIGOSH!" # @t_staira370.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Taira’s lifting him up by his jacket…" # @t_staira370.01 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "He’s going to hurt Blue Max!)" # @t_staira371.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "HAW HAW!" # @t_staira372.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’ve got to do something.)" # @t_staira373.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "FOR MY CLAAAAAN!" # @t_staira376.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’ve got to stop him somehow… )" # @t_staira398.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        linear .25 xpos 0.7 
    show i_sw_black as curtain zorder 10:
        # FadeEvent
        linear 0.1 alpha 1.0
    play sound ["<silence .25>", "sfx/slap.ogg"]
    extend "{w=0.25}{nw}"
    # Blank text event <TextEvent {} TextEvent ''>
    $ renpy.pause(1)
    # <ParallelEvent {'allowInterrupt': 'false', 'delay': '1', 'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.2 
    stop music fadeout 1.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "...Ow." # @t_staira399.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_pleading as taira:
        # ShowWithAtl
        linear 0.5 xpos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_taira "[slot_playerName]…?!" # @t_staira3100.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Wow, [slot_playerName]!" # @t_staira3101.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You jumped in front of Taira’s punch for me?!" # @t_staira3101.01 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ha.. ha…" # @t_staira3102.00 self.block='Last'
    show i_sw_black as curtain zorder 10:
        # FadeEvent
        linear 0.75 alpha 0.0
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " yeah..." # @t_staira3102.01 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "[slot_playerName]… I…" # @t_staira3103.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I hit you…" # @t_staira3103.01 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I…" # @t_staira3104.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I can’t believe…" # @t_staira3104.01 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I did that..." # @t_staira3104.02 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What, so it’s okay to be a bully, just not to me?" # @t_staira3105.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Don’t expect me to feel bad for you." # @t_staira3106.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "“Bully?!”" # @t_staira3107.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I… I…" # @t_staira3107.01 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Look, Taira, I-" # @t_staira3108.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin:
        # ShowWithAtl
        linear .2 xpos 0.11 
    show i_taira_akimbo_pleading as taira:
        # ShowWithAtl
        linear .2 xpos 0.2 
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        linear .2 xpos 0.25 
    extend "{w=0.2}{nw}"
    t_ch_digdug "WHAT’S GOING ON HERE?!" # @t_staira3109.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.5 xpos 0.8 
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_max "EEK!" # @t_staira3110.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "P-Principal DIG DUG?!" # @t_staira3111.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "…" # @t_staira3112.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Who did this?!" # @t_staira3113.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Which of you punched poor [slot_playerName]?!" # @t_staira3113.01 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I know [slot_playerName] is a new student, but hazing is unacceptable at Namco High!" # @t_staira3114.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(... I don’t want to be a snitch…)" # @t_staira3115.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "P-please don’t make me say, sir, I don’t want any more-" # @t_staira3116.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_pleading as taira
    t_ch_taira "I did. It was… me." # @t_staira3117.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wow…" # @t_staira3118.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He confessed." # @t_staira3118.01 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Just like that.)" # @t_staira3119.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Why, Principal DIG DUG?" # @t_staira3120.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Why did I do that?" # @t_staira3120.01 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Why are you asking me?!" # @t_staira3121.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I didn’t mean to hit [slot_playerName]…" # @t_staira3122.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "[slot_playerName] jumped in front of me, to protect me from Taira’s revenge!" # @t_staira3123.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Revenge?!" # @t_staira3124.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " My god, Blue Max, what did you do?!" # @t_staira3124.01 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "AUGH!" # @t_staira3125.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "No, no! Blue Max didn’t do anything!" # @t_staira3126.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "This is too confusing!" # @t_staira3127.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I can’t make heads or tails of this!" # @t_staira3128.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "All three of you are sentenced to…" # @t_staira3129.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "A SPECIAL DOUBLE-DETENTION!" # @t_staira3130.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "DETENTION LEVEL NINE: EXTINCTION EVENT!" # @t_staira3131.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What does that even mean?" # @t_staira3132.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "It means I’ll see you all in my office." # @t_staira3133.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_hallway_b as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_b', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_2N'} SettingChange ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_taira_default_serious_cry as taira
    show i_bluemax_cower_worried as bluemax
    $ AudioEvent('music', 1.0, 1.0)
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " NOW!" # @t_staira3133.01 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Alright. Which one of you is talking to me first?" # @t_staira3134.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax:
        # FadeEvent
        linear 0.33 alpha 0.0
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.33 alpha 0.0
    extend "{w=0.33}{nw}"
    t_ch_max "Um… I’ll go…" # @t_staira3135.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin:
        # ShowWithAtl
        ease_expo .5 xpos 0.25 
    show i_taira_default_serious_cry as taira:
        # ShowWithAtl
        ease_expo .5 xpos 0.75 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(Nothing left to do but wait for our judgement from Principal DIG DUG.." # @t_staira3136.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I haven’t been at Namco High long, but I’ve already been here twice…" # @t_staira3137.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But… this time, it’s not really my fault, of course." # @t_staira3137.01 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s his.)" # @t_staira3137.02 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Taira’s just sitting there, not saying a word." # @t_staira3138.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He’s shaking a little…" # @t_staira3138.01 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Maybe…" # @t_staira3139.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " In rage?)" # @t_staira3139.01 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I can’t believe it!" # @t_staira3140.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He’s not shaking with rage…" # @t_staira3140.01 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He’s actually crying!)" # @t_staira3140.02 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Sniff… Snifff…" # @t_staira3141.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "T-Taira?!" # @t_staira3142.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Are you okay, big guy?" # @t_staira3142.01 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I… I wish…" # @t_staira3143.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I could take revenge…" # @t_staira3143.01 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_pleading as taira
    extend " On my FEELINGS!" # @t_staira3143.02 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "...Hmmf." # @t_staira3144.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Revenge." # @t_staira3144.01 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m so sick of hearing about revenge!" # @t_staira3145.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "H-Huh?!" # @t_staira3146.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You… You just use it to justify being a huge jerk to people!" # @t_staira3147.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    extend " It’s mean, and gross!" # @t_staira3147.01 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Noooooo!" # @t_staira3148.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " [slot_playerName], please…" # @t_staira3148.01 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_pleading_cry as taira
    extend " Revenge is my thing, yo!" # @t_staira3148.02 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "W-well… what you did today…" # @t_staira3149.00 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I call that “bullying”, not “revenge”!" # @t_staira3149.01 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And I don’t want to be friends with someone who has bullying as his “thing”!" # @t_staira3150.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Bullying?!" # @t_staira3151.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "But… I had to do it…" # @t_staira3152.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I was avenging…" # @t_staira3153.00 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I always avenge…" # @t_staira3153.01 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ugh, whatever!" # @t_staira3154.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I can’t believe I actually thought you were a sweet guy deep down…" # @t_staira3154.01 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I must be even stupider than you!" # @t_staira3154.02 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "[slot_playerName]…" # @t_staira3155.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What, are you gonna get “revenge” on ME now?!" # @t_staira3156.00 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Oh! Huh?!" # @t_staira3157.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Are you saying I should?" # @t_staira3158.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Yo, I’m mad confused…" # @t_staira3159.00 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "UGH! You are seriously HOPELESS!" # @t_staira3160.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "[slot_playerName]… please forgive me!" # @t_staira3161.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s such a bummer that you’re mad at me…" # @t_staira3161.01 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_staira3162.00 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "You shouldn’t only be sad because you want me to forgive you…" # @t_staira3163.00 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That makes it not a real apology." # @t_staira3163.01 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Does this mean… you don’t want to date me?" # @t_staira3164.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I… I…" # @t_staira3165.00 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don’t want to date a bully who hurts people." # @t_staira3165.01 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "...You say that about me..." # @t_staira3166.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And I don’t get it, but…" # @t_staira3166.01 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " yo, I think you gotta be right." # @t_staira3166.02 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "You’re right about lots of stuff…" # @t_staira3167.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’re like, a super-smart nerd." # @t_staira3167.01 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "All brains and no brawn…" # @t_staira3168.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Like, none. Zero. Zilch." # @t_staira3169.00 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’ve got a LITTLE brawn." # @t_staira3170.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " Didn’t I just prove that?)" # @t_staira3170.01 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "But really… I had to take revenge." # @t_staira3171.00 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "For… For my fallen clan." # @t_staira3172.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Taira, you’ve mentioned this “clan” of yours before…" # @t_staira3173.00 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Who are they?" # @t_staira3173.01 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "How can I even talk about it now?!" # @t_staira3174.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m feeling so sad, yo..." # @t_staira3174.01 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Cuz like, deep in my warrior heart, I can’t shake this feeling…" # @t_staira3175.00 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " like if they could see me now…" # @t_staira3175.01 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_pleading_cry as taira
    t_ch_taira "They’d be mad ashamed of me!" # @t_staira3176.00 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "...Taira…" # @t_staira3177.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin:
        # ShowWithAtl
        pause 0.5 
        ease_expo 1 xpos 0.45 
    extend "{w=1.5}{nw}"
    t_ch_cousin "(I put my hand on his hand, because I couldn’t think of anything to say." # @t_staira3178.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain zorder 10:
        # FadeEvent
        linear 1.75 alpha 1.0
    extend "{w=1.75}{nw}"
    # Blank text event <TextEvent {} TextEvent ''>
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "We waited there in silence a little while longer, before we both got chewed out by Principal DIG DUG for fighting." # @t_staira3179.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But of all the things that happened that day…" # @t_staira3180.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That moment, with my hand on his," # @t_staira3181.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "is the one lingering strongest in my memory.)" # @t_staira3182.00 self.block='Last'
    # <NHSceneChange {'name': '_3e', 'scene': 's_day4'} NHSceneChange ''>
    label s_taira3__3e:
        # <NHSceneChange {'name': '_3e', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4