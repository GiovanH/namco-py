# <Scene scene {'id': 's_antibravo3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_antibravo3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_antibravo3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_antibravo3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/school.ogg" loop
    show i_bg_cafe as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_energetic_surprise as cousin zorder 2:
        default
        xpos 0.3 
    show i_donko_default_wink as donko zorder 1:
        default
        alpha 0.0
        xpos 0.7 
    show i_abm_default_broody as antibravo zorder 1:
        default
        alpha 0.0
        xpos 0.7 
    show i_miller_aliens_serious as miller zorder 2:
        default
        alpha 1.0
        ypos 1.5 
        xpos 0.8 
    show i_tomari_standing_mortified as tomari zorder 2:
        default
        alpha 0.0
        xpos 0.8 
    show i_taira_steveholt_happy as taira zorder 1:
        default
        alpha 0.0
        xpos 0.7 
    show i_valkyrie_default_wink as valkyrie zorder 2:
        default
        alpha 0.0
        xpos 0.8 
    show i_albatross_toocool_staredown as albatros zorder 2:
        default
        alpha 0.0
        xpos -0.3 
    t_ch_cousin "Hey! Wait up!" # @t_santibravo313.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Wow! He's quick!" # @t_santibravo314.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Made it!" # @t_santibravo315.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Wait..." # @t_santibravo315.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That's weird." # @t_santibravo315.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I don't see him at all. Maybe he's up in the rafters?" # @t_santibravo315.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Anyone seen Anti-Bravoman?" # @t_santibravo316.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Everyone just shrugged and went back to whatever they were doing... )" # @t_santibravo317.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Maybe he didn't see me and went back to detention?)" # @t_santibravo318.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # Curtain fade
    show i_bg_classroom_a as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_classroom_a', 'curtainActor': 'curtain', 'curtainFadeTime': '.75', 'name': '_9', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Anti-Bravoman?" # @t_santibravo319.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Hey! Has anyone seen Anti-Bravoman around?" # @t_santibravo320.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_donko_akimbo_meloncholic as donko:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_donko "Why're you looking for THAT weirdo?" # @t_santibravo321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " He's not cool at ALL." # @t_santibravo321.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Aw... He's not so bad. I think he's just used to being alone, so he doesn't know how to act around people..." # @t_santibravo322.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_donko "Well, I don't trust him one bit!" # @t_santibravo323.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_donko_ygg_meloncholic as donko
    extend " I'm sure you've heard the RUMORS, right?" # @t_santibravo323.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Rumors?)" # @t_santibravo324.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Rumors?" # @t_santibravo325.00 self.block='Last'
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.5 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_steveholt_serious as taira:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_taira "Yeah! I heard that guy is SUPER evil!" # @t_santibravo326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_serious as taira
    extend " I HATE EVIL!" # @t_santibravo326.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_serious as taira
    extend " I'm totally gonna get revenge on evil." # @t_santibravo326.02 self.block='Last'
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.5 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_wink as valkyrie:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "Calm down Taira. You can't just hate him because he's from our Wrestleball rival, Evil Namco High." # @t_santibravo327.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(Anti-Bravoman's from... Evil Namco High?!" # @t_santibravo328.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It sounds like Valkyrie is gossiping, though..." # @t_santibravo328.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    extend " But if it's true... why is Anti-Bravoman at Namco High?)" # @t_santibravo328.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_thoughtful as valkyrie
    t_ch_valkyrie "He IS pretty cute... For an evil guy." # @t_santibravo329.00 self.block='Last'
    show i_taira_revenge_serious as taira:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_taira "EVIL CAN'T BE CUTE!" # @t_santibravo330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_wink as valkyrie
    t_ch_valkyrie "You're pretty cute... For an idiot, Taira." # @t_santibravo331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "TOO MUCH CUTENESS! RED CARD!" # @t_santibravo332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_wink as valkyrie:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_donko_default_wink as donko:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_donko "And besides, we all know I'M the cutest." # @t_santibravo333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_donko "But Valkyrie's right... I heard he's from Evil Namco High too." # @t_santibravo334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_donko_default_meloncholic as donko
    extend " I heard he was really bad. You'd have to be to get kicked out of an Evil High School ...RIGHT?" # @t_santibravo334.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " SUPER evil." # @t_santibravo334.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_mortified as tomari:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
        xzoom -1.0 
    $ renpy.pause(0.5, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_tomari_standing_mortified as tomari:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_tomari "He DOES fulfill a satisfactory number of points on my bad guy determinance matrix." # @t_santibravo335.00 self.block='Last'
    show i_miller_aliens_serious as miller:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_donko_default_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_miller_aliens_contemplative as miller:
        # ShowWithAtl
        linear 0.5 ypos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_richard "Maybe he's here as a spy!" # @t_santibravo336.00 self.block='Last'
    show i_albatross_toocool_staredown as albatros:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_mortified as tomari:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_albatross_toocool_staredown as albatros:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_albatros "A spy?!" # @t_santibravo337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Who would spy on innocent STUDENTS!" # @t_santibravo337.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " How terrible..." # @t_santibravo337.02 self.block='Last'
    show i_taira_revenge_serious as taira:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.25 alpha 1.0
    show i_miller_aliens_contemplative as miller:
        # FadeEvent
        linear 0.25 alpha 0.0
    extend "{w=0.25}{nw}"
    t_ch_taira "Wait... What if he's spyin' on us to steal all of our super secret Wrestleball strategies!!" # @t_santibravo338.00 self.block='Last'
    show i_valkyrie_default_wink as valkyrie:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_staredown as albatros:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_valkyrie_akimbo_bored as valkyrie:
        # FadeEvent
        linear 0.25 alpha 1.0
        xzoom -1.0 
    extend "{w=0.25}{nw}"
    t_ch_valkyrie "Taira... Don't you just make it up as you go along?" # @t_santibravo339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "THAT'S WHAT MAKES THEM SO SUPER SECRET" # @t_santibravo340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_steveholt_happy as taira:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 1.0
        xzoom -1.0 
    extend "{w=0.25}{nw}"
    t_ch_donko "Anyway... Why are you looking for a super evil guy, [slot_playerName]?" # @t_santibravo341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_bored as valkyrie:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_cousin_default_mortified as cousin:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    extend " Did he do something..." # @t_santibravo341.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " SUSPICIOUS?" # @t_santibravo341.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "N-no..." # @t_santibravo342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_donko "Uh-oh... Does he have some dirt on you? Is he blackmailing you?! You can tell us!" # @t_santibravo343.00 self.block='Last'
    show i_valkyrie_akimbo_bored as valkyrie:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 1.2 
        # FadeEvent
        linear 0.2 alpha 1.0
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_wink as valkyrie:
        # ShowWithAtl
        linear 0.5 xpos 0.9 
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "You can definitely tell us!" # @t_santibravo344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_wink as valkyrie:
        # ShowWithAtl
        linear 0.5 xpos 1.2 
        # FadeEvent
        linear 0.2 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "Guys... It's fine..." # @t_santibravo345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I have to go." # @t_santibravo345.01 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # Curtain fade
    show i_bg_hallway_b as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_b', 'curtainActor': 'curtain', 'curtainFadeTime': '.75', 'name': '_z', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent

    show i_cousin_default_neutral as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(That was... Really weird." # @t_santibravo346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " They all think Anti-Bravoman is a bad guy...)" # @t_santibravo346.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I don't know him very well, but calling him a bad guy..." # @t_santibravo347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Isn't that taking it a little far?)" # @t_santibravo347.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(... Did he really come from Evil Namco High?)" # @t_santibravo348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_shadowknows_broody as antibravo:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_antibravo "................." # @t_santibravo349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "I hope no one witnessed... My deep dark secret........." # @t_santibravo350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The secret I've been running from......" # @t_santibravo350.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Like a gazelle of darkness..." # @t_santibravo350.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Anti-Bravoman?" # @t_santibravo351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_surprised as antibravo
    t_ch_antibravo "AH! [slot_playerName]! I didn't see you there!" # @t_santibravo352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_surprised as antibravo:
        xzoom -1.0 
    t_ch_cousin "I was right here." # @t_santibravo353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You might need glasses." # @t_santibravo353.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " ANYWAY!" # @t_santibravo353.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I was just wondering... We were supposed to go to Poetry Club together..." # @t_santibravo354.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But then you disappeared." # @t_santibravo354.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "Sorry... I... I got lost!" # @t_santibravo355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I went back to the Detention room because I thought you might be back there, but you weren't..." # @t_santibravo356.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And then I got to talking to the other students about you." # @t_santibravo357.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " And they were saying all kinds of crazy stuff..." # @t_santibravo357.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Like that you're from Evil Namco High." # @t_santibravo358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Is that true?" # @t_santibravo358.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "........." # @t_santibravo359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "..........................." # @t_santibravo360.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "............ It's true." # @t_santibravo361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "[slot_playerName]... I can't tell you what to do. Or who to believe." # @t_santibravo362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_shadowknows_broody as antibravo
    t_ch_antibravo "It's something... You have to decide on your own." # @t_santibravo363.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Well... That didn't answer anything.)" # @t_santibravo364.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(But... I think that's the coolest I've ever seen him." # @t_santibravo365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I kinda got goosebumps." # @t_santibravo365.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug zorder 1:
        default
        alpha 0.0
        xpos 0.8 
    extend " But only a little bit.)" # @t_santibravo365.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_shadowknows_surprised as antibravo:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.33 xpos 0.35 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.33 xpos 0.15 
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_digdug "AHEM!" # @t_santibravo366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "!!!" # @t_santibravo367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "!!!!!!!" # @t_santibravo368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Well well well... I shouldn't be so surprised to see two of our star delinquents skipping together." # @t_santibravo369.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "PRINCIPAL DIG DUG!" # @t_santibravo370.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_digdug "[slot_playerName], I expect more from you..." # @t_santibravo371.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "And Anti-Bravoman... Is this what you're making of the chance you've been given?" # @t_santibravo372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "Sorry..." # @t_santibravo373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(Even the staff treat him differently..." # @t_santibravo374.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Like he's a charity case.)" # @t_santibravo375.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " He's just doing his best!)" # @t_santibravo375.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Based on the level of your infraction, I'm giving you DETENTION LEVEL 217: FLOATING ISLAND PRISON DETENTION!!!!" # @t_santibravo376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "If you think you're alone now... Just wait!!" # @t_santibravo377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Principal Dig Dug!! He already feels lonely... That's uncalled for!" # @t_santibravo378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "It's okay, [slot_playerName]." # @t_santibravo379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "See! Accept your fate, lest I call King!" # @t_santibravo380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_angry as cousin
    t_ch_cousin "I'll tell King you were threatening a student!" # @t_santibravo381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Uh-oh... Maybe I'm getting carried away... )" # @t_santibravo382.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "EEP! Let's not be hasty..." # @t_santibravo383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug:
        # FadeEvent
        linear 2.0 alpha 0.0
    show i_abm_default_sad as antibravo:
        # FadeEvent
        linear 2.0 alpha 0.0
    show i_bg_cafe as bg:
        # FadeEvent
        linear 2.0 alpha 0.0
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 2 xpos 0.5 
    extend "{w=2.0}{nw}"
    t_ch_cousin "(After that we walked back to the detention room. I didn't realize it at first, but any other student would have said something... ANYTHING.)" # @t_santibravo384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(But Anti-Bravoman just listened and accepted it. I think he's trying really hard to make his time at Namco High work.)" # @t_santibravo385.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_1q', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_antibravo3__1q:
        # <NHSceneChange NHSceneChange {'name': '_1q', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4