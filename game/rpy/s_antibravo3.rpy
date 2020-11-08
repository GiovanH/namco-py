# <Scene {'id': 's_antibravo3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_antibravo3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_antibravo3"
    $ renpy.pause(1)
    # <Scene {'id': 's_antibravo3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Wow! He's quick!" # @t_santibravo314.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Made it!" # @t_santibravo315.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Wait..." # @t_santibravo315.01 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That's weird." # @t_santibravo315.02 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don't see him at all. Maybe he's up in the rafters?" # @t_santibravo315.03 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Anyone seen Anti-Bravoman?" # @t_santibravo316.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Everyone just shrugged and went back to whatever they were doing... )" # @t_santibravo317.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Maybe he didn't see me and went back to detention?)" # @t_santibravo318.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75)
    show i_bg_classroom_a as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_classroom_a', 'curtainActor': 'curtain', 'curtainFadeTime': '.75', 'name': '_9'} SettingChange ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75)
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Anti-Bravoman?" # @t_santibravo319.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Hey! Has anyone seen Anti-Bravoman around?" # @t_santibravo320.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_meloncholic as donko:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_donko "Why're you looking for THAT weirdo?" # @t_santibravo321.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He's not cool at ALL." # @t_santibravo321.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Aw... He's not so bad. I think he's just used to being alone, so he doesn't know how to act around people..." # @t_santibravo322.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Well, I don't trust him one bit!" # @t_santibravo323.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_meloncholic as donko
    extend " I'm sure you've heard the RUMORS, right?" # @t_santibravo323.01 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Rumors?)" # @t_santibravo324.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Rumors?" # @t_santibravo325.00 self.block='Last'
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_serious as taira:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_taira "Yeah! I heard that guy is SUPER evil!" # @t_santibravo326.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    extend " I HATE EVIL!" # @t_santibravo326.01 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    extend " I'm totally gonna get revenge on evil." # @t_santibravo326.02 self.block='Last'
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_default_wink as valkyrie:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "Calm down Taira. You can't just hate him because he's from our Wrestleball rival, Evil Namco High." # @t_santibravo327.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(Anti-Bravoman's from... Evil Namco High?!" # @t_santibravo328.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It sounds like Valkyrie is gossiping, though..." # @t_santibravo328.01 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " But if it's true... why is Anti-Bravoman at Namco High?)" # @t_santibravo328.02 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_default_thoughtful as valkyrie
    t_ch_valkyrie "He IS pretty cute... For an evil guy." # @t_santibravo329.00 self.block='Last'
    show i_taira_revenge_serious as taira:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_taira "EVIL CAN'T BE CUTE!" # @t_santibravo330.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_default_wink as valkyrie
    t_ch_valkyrie "You're pretty cute... For an idiot, Taira." # @t_santibravo331.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "TOO MUCH CUTENESS! RED CARD!" # @t_santibravo332.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_default_wink as valkyrie:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_donko_default_wink as donko:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_donko "And besides, we all know I'M the cutest." # @t_santibravo333.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "But Valkyrie's right... I heard he's from Evil Namco High too." # @t_santibravo334.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic as donko
    extend " I heard he was really bad. You'd have to be to get kicked out of an Evil High School ...RIGHT?" # @t_santibravo334.01 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " SUPER evil." # @t_santibravo334.02 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
        xzoom -1.0 
    $ renpy.pause(0.5) # TimedPause
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_albatross_toocool_staredown as albatros:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_albatros "A spy?!" # @t_santibravo337.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Who would spy on innocent STUDENTS!" # @t_santibravo337.01 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How terrible..." # @t_santibravo337.02 self.block='Last'
    show i_taira_revenge_serious as taira:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_staredown as albatros:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_valkyrie_akimbo_bored as valkyrie:
        # FadeEvent
        linear 0.25 alpha 1.0
        xzoom -1.0 
    extend "{w=0.25}{nw}"
    t_ch_valkyrie "Taira... Don't you just make it up as you go along?" # @t_santibravo339.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "THAT'S WHAT MAKES THEM SO SUPER SECRET" # @t_santibravo340.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 1.0
        xzoom -1.0 
    extend "{w=0.25}{nw}"
    t_ch_donko "Anyway... Why are you looking for a super evil guy, [slot_playerName]?" # @t_santibravo341.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_akimbo_bored as valkyrie:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_cousin_default_mortified as cousin:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    extend " Did he do something..." # @t_santibravo341.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " SUSPICIOUS?" # @t_santibravo341.02 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "N-no..." # @t_santibravo342.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Uh-oh... Does he have some dirt on you? Is he blackmailing you?! You can tell us!" # @t_santibravo343.00 self.block='Last'
    show i_valkyrie_akimbo_bored as valkyrie:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 1.2 
        # FadeEvent
        linear 0.2 alpha 1.0
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_default_wink as valkyrie:
        # ShowWithAtl
        linear 0.5 xpos 0.9 
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "You can definitely tell us!" # @t_santibravo344.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_default_wink as valkyrie:
        # ShowWithAtl
        linear 0.5 xpos 1.2 
        # FadeEvent
        linear 0.2 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "Guys... It's fine..." # @t_santibravo345.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I have to go." # @t_santibravo345.01 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75)
    show i_bg_hallway_b as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_b', 'curtainActor': 'curtain', 'curtainFadeTime': '.75', 'name': '_z'} SettingChange ''>
    # <Events {} events ''>
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        alpha 0.0
    show i_cousin_default_neutral as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75)
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(That was... Really weird." # @t_santibravo346.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They all think Anti-Bravoman is a bad guy...)" # @t_santibravo346.01 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I don't know him very well, but calling him a bad guy..." # @t_santibravo347.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Isn't that taking it a little far?)" # @t_santibravo347.01 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(... Did he really come from Evil Namco High?)" # @t_santibravo348.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_shadowknows_broody as antibravo:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_antibravo "................." # @t_santibravo349.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "I hope no one witnessed... My deep dark secret........." # @t_santibravo350.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The secret I've been running from......" # @t_santibravo350.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Like a gazelle of darkness..." # @t_santibravo350.02 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Anti-Bravoman?" # @t_santibravo351.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_surprised as antibravo
    t_ch_antibravo "AH! [slot_playerName]! I didn't see you there!" # @t_santibravo352.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_surprised as antibravo:
        xzoom -1.0 
    t_ch_cousin "I was right here." # @t_santibravo353.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You might need glasses." # @t_santibravo353.01 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ANYWAY!" # @t_santibravo353.02 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I was just wondering... We were supposed to go to Poetry Club together..." # @t_santibravo354.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But then you disappeared." # @t_santibravo354.01 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "Sorry... I... I got lost!" # @t_santibravo355.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I went back to the Detention room because I thought you might be back there, but you weren't..." # @t_santibravo356.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And then I got to talking to the other students about you." # @t_santibravo357.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " And they were saying all kinds of crazy stuff..." # @t_santibravo357.01 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Like that you're from Evil Namco High." # @t_santibravo358.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Is that true?" # @t_santibravo358.01 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "........." # @t_santibravo359.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "..........................." # @t_santibravo360.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "............ It's true." # @t_santibravo361.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "[slot_playerName]... I can't tell you what to do. Or who to believe." # @t_santibravo362.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_shadowknows_broody as antibravo
    t_ch_antibravo "It's something... You have to decide on your own." # @t_santibravo363.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Well... That didn't answer anything.)" # @t_santibravo364.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(But... I think that's the coolest I've ever seen him." # @t_santibravo365.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I kinda got goosebumps." # @t_santibravo365.01 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_left as digdug zorder 1:
        default
        alpha 0.0
        xpos 0.8 
    extend " But only a little bit.)" # @t_santibravo365.02 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "!!!" # @t_santibravo367.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "!!!!!!!" # @t_santibravo368.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Well well well... I shouldn't be so surprised to see two of our star delinquents skipping together." # @t_santibravo369.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "PRINCIPAL DIG DUG!" # @t_santibravo370.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_digdug "[slot_playerName], I expect more from you..." # @t_santibravo371.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "And Anti-Bravoman... Is this what you're making of the chance you've been given?" # @t_santibravo372.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "Sorry..." # @t_santibravo373.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(Even the staff treat him differently..." # @t_santibravo374.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Like he's a charity case.)" # @t_santibravo375.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He's just doing his best!)" # @t_santibravo375.01 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Based on the level of your infraction, I'm giving you DETENTION LEVEL 217: FLOATING ISLAND PRISON DETENTION!!!!" # @t_santibravo376.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "If you think you're alone now... Just wait!!" # @t_santibravo377.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Principal Dig Dug!! He already feels lonely... That's uncalled for!" # @t_santibravo378.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "It's okay, [slot_playerName]." # @t_santibravo379.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "See! Accept your fate, lest I call King!" # @t_santibravo380.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    t_ch_cousin "I'll tell King you were threatening a student!" # @t_santibravo381.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Uh-oh... Maybe I'm getting carried away... )" # @t_santibravo382.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "EEP! Let's not be hasty..." # @t_santibravo383.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But Anti-Bravoman just listened and accepted it. I think he's trying really hard to make his time at Namco High work.)" # @t_santibravo385.00 self.block='Last'
    # <NHSceneChange {'name': '_1q', 'scene': 's_day4'} NHSceneChange ''>
    label s_antibravo3__1q:
        # <NHSceneChange {'name': '_1q', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4