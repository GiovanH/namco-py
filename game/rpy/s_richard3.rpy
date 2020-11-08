# <Scene {'id': 's_richard3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_richard3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_richard3"
    $ renpy.pause(1)
    # <Scene {'id': 's_richard3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/aroundtown.ogg" loop
    show i_bg_hallway_b as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_albatross_toocool_smirk as albatros zorder 1:
        default
        alpha 0.0
        xpos 0.7 
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_miller_akimbo_contemplative as miller zorder 1:
        default
        xpos 0.7 
    show i_digdug_left as digdug zorder 1:
        default
        xpos 1.3 
    t_ch_richard "I knew you’d come." # @t_srichard30.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What if I didn’t?" # @t_srichard31.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Then I’d have known that instead." # @t_srichard32.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That’s a little convenient." # @t_srichard33.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_halfgrin as miller
    t_ch_richard "It’s very convenient!" # @t_srichard34.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Okay, so what’s this stakeout stuff?" # @t_srichard35.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "We don’t have much time before detention is up." # @t_srichard36.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "Detention?" # @t_srichard37.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Oh, no no no." # @t_srichard38.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "No?" # @t_srichard39.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "No, no." # @t_srichard310.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh." # @t_srichard311.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_serious as miller
    t_ch_richard "We’ll have to skip school to track this target and get to the bottom of the Big Conspiracy." # @t_srichard312.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Sk-skip? I thought we were just gonna watch a guy and take some notes." # @t_srichard313.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "We are." # @t_srichard314.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_shocked as miller
    t_ch_richard "AWAY FROM SCHOOL GROUNDS THOUGH!" # @t_srichard315.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Geez!)" # @t_srichard316.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " This must be a pretty big conspiracy then." # @t_srichard316.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Probably!" # @t_srichard317.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "I have no idea." # @t_srichard318.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "But it’s big. Super big maybe." # @t_srichard319.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(I can’t believe we’re risking a black mark on our permanent records for a conspiracy that might not be big.)" # @t_srichard320.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(...If it’s even real?!?!)" # @t_srichard321.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_cafe as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_cafe', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_N'} SettingChange ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_miller_akimbo_contemplative as miller
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_miller_akimbo_contemplative as miller
    t_ch_richard "Our target today is ordinary student ALFONSO “AL” B. TROSS. He’s always meeting sinister characters in this joint." # @t_srichard322.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "S-s-sinister?" # @t_srichard323.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Honestly? I’m assuming they’re sinister because they look so normal." # @t_srichard324.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Whew." # @t_srichard325.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If he’s meeting ordinary people, and then if HE’S so ordinary, then why is he worth tracking?" # @t_srichard326.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_contemplative as miller
    t_ch_richard "He’s too ordinary." # @t_srichard327.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_serious as miller
    t_ch_richard "Suspiciously ordinary." # @t_srichard328.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "UNUSUALLY ORDINARY." # @t_srichard329.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "And if you think about it, that makes him EXTRAORDINARY." # @t_srichard330.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "And that’s not even counting the stuff that makes him WEIRD." # @t_srichard331.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_serious as miller
    t_ch_richard "EXAMPLE! Consider that his name, Al B. Tross, is ODDLY SIMILAR to the name of a student who graduated last year, Agent Albatross." # @t_srichard332.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I guess that’s suspicious?)" # @t_srichard333.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But, I mean, sometimes names sound similar. Like Tim or Jim!)" # @t_srichard334.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_contemplative as miller
    t_ch_richard "The most logical conclusion we can draw is that Al B. Tross is a secret agent of the big crazy conspiracy." # @t_srichard335.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Probably the top agent. Maybe the king of the conspiracy!" # @t_srichard336.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Wouldn’t the MOST logical conclusion be that there isn’t a conspiracy?" # @t_srichard337.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Y’know." # @t_srichard338.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "LIKE AT ALL?" # @t_srichard339.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_halfgrin as miller
    t_ch_richard "Ha! You and I must have very different interpretation of the word “logical.”" # @t_srichard340.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Yeeeeaaaaaah, I think we do!)" # @t_srichard341.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Y’know, I’ve been thinking, there might be a better use of your life than chasing conspiracies like this." # @t_srichard341.01 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_contemplative as miller
    t_ch_richard "Like what?" # @t_srichard342.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "You’ve got other interests, right?" # @t_srichard343.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "I like tracking people’s movements." # @t_srichard344.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Uh, hm. Something else? Something less creepy, maybe!" # @t_srichard345.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_halfgrin as miller
    t_ch_richard "How about...going through their garbage?" # @t_srichard346.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(How is that less creepy!)" # @t_srichard347.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "No. Just...no." # @t_srichard348.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_halfgrin as miller
    t_ch_richard "I really enjoy determining the strengths and weaknesses of everyone I meet to better fit them into the complicated web of conspiracies that make up Great Big Conspiracy." # @t_srichard349.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "You can’t use literally the thing I’m trying to get you to stop doing as an alternative hobby for the thing I’m trying to get you to stop doing!" # @t_srichard350.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_shocked as miller
    t_ch_richard "Well, that’s all I got!" # @t_srichard351.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(That can’t be all there is so this guy.)" # @t_srichard352.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Can it?!)" # @t_srichard353.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "Oh, wait! I almost forgot." # @t_srichard354.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(Finally.)" # @t_srichard355.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " Yeah? What is it?" # @t_srichard355.01 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_halfgrin as miller
    t_ch_richard "I like doing stuff as totally fast as possible." # @t_srichard356.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "It’s the most efficient use of our limited time here on this world." # @t_srichard357.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That’s…" # @t_srichard358.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " (Is that weird?)" # @t_srichard358.01 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I mean, it’s totally weird. But he’s kinda not wrong about it?)" # @t_srichard359.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But, no, it’s totally weird to be thinking about it all the time.)" # @t_srichard360.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Is that REALLY all there is to Richard?)" # @t_srichard361.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Just being weird and paranoid and good looking.)" # @t_srichard362.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral_blush as cousin
    extend " (Wait. Did I think “good looking?”)" # @t_srichard362.01 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Get it together, [slot_playerName]!)" # @t_srichard363.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "Well. There’s the cooking." # @t_srichard364.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "They say I’m pretty good at it." # @t_srichard365.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "But, I dunno." # @t_srichard366.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Cooking, huh? Yeah. That’s definitely productive and not weird." # @t_srichard367.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_halfgrin as miller
    t_ch_richard "It comes pretty natural, I guess." # @t_srichard368.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "On my first day in Home Ec I figured out how to make a 3 minute egg in 45 seconds." # @t_srichard369.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "That’s an “A” Rank on the time trial." # @t_srichard370.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Gonna go for “S” Rank next." # @t_srichard371.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(These must be culinary terms…)" # @t_srichard372.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You could maybe try to cook like, uh, normal?" # @t_srichard372.01 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Like, you don’t have to rush around at full speed and high alert all the time!" # @t_srichard373.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "Hm? Eh, yeah cooking is okay." # @t_srichard374.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "I guess." # @t_srichard375.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "If you’re into preparing food while under the oppressive thumb of a massive shadow government operating through an even shadowier puppetmaster, then yeah." # @t_srichard376.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Sure." # @t_srichard377.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Cooking is great." # @t_srichard378.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And Al B. Tross is part of this thing?" # @t_srichard379.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_halfgrin as miller
    t_ch_richard "A huge part." # @t_srichard380.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Okay. Which part though? The shadow government or the shadowier puppet thing?" # @t_srichard381.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "That’s what we’re here to find out." # @t_srichard382.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_shocked as miller
    t_ch_richard "Ah! He’s here!" # @t_srichard383.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Okay, okay." # @t_srichard384.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_serious as miller
    t_ch_richard "Act natural." # @t_srichard385.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "Got it!" # @t_srichard386.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_serious as miller
    t_ch_richard "But don’t LOOK like you’re acting natural." # @t_srichard387.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Wait. How else would I act?)" # @t_srichard388.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(But now that I’m thinking about acting natural, EVERYTHING I THINK AND DO FEELS WAY UNNATURAL!)" # @t_srichard389.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin:
        pause .5
        linear .2 xzoom -1.0 
        pause 1
        linear .2 xzoom 1.0 
        pause 1.5
        linear .2 xzoom -1.0 
        pause 2
        linear .2 xzoom 1.0 
    extend "{w=2.0}{nw}"
    t_ch_cousin "(AAAAHHHHH!)" # @t_srichard390.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Something wrong, [slot_playerName]?" # @t_srichard391.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_contemplative as miller
    t_ch_richard "You’re acting…" # @t_srichard392.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "...strange." # @t_srichard393.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I was acting natural until you said to act natural and now I don’t know how to act!" # @t_srichard394.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Hmm." # @t_srichard395.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_shocked as miller
    extend " Hold on." # @t_srichard395.01 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_shocked as miller
    t_ch_richard "Now that you’ve got me thinking about it I can’t act natural either!" # @t_srichard396.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Argh, did I screw up the whole thing before it even started???)" # @t_srichard397.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Okay. Deep breaths." # @t_srichard398.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_shocked as miller
    t_ch_richard "Acting natural is just a kind of timing. We can do this, [slot_playerName]! Using TOTAL CONCENTRATION!" # @t_srichard399.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Just follow my lead." # @t_srichard3100.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Okay!" # @t_srichard3101.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    extend " (Uh, he’s not doing anything…)" # @t_srichard3101.01 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(Wait, maybe that’s what acting natural looks like!)" # @t_srichard3102.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I can do that!)" # @t_srichard3103.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_angry_blush as cousin
    t_ch_cousin "(Oh, man, gotta concentrate! It’s all I can think about. I must be acting so natural right now!)" # @t_srichard3104.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smirk as albatros:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        ease_expo .3 xpos 0.2 
    show i_miller_akimbo_shocked as miller:
        # ShowWithAtl
        ease_expo .3 xpos 0.32 
    extend "{w=0.5}{nw}"
    t_ch_albatros "Hey, guys." # @t_srichard3105.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Acting natural, I see." # @t_srichard3106.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_shocked as miller
    t_ch_richard "NO!" # @t_srichard3107.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "Wait. Yes!" # @t_srichard3108.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(How could he tell?!)" # @t_srichard3109.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_serious as miller
    t_ch_richard "Wait. We’re not on trial here." # @t_srichard3110.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_serious as miller
    t_ch_richard "YOU ARE!" # @t_srichard3111.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "For flagrant truancy in the act of conspiring to do stuff. Bad stuff." # @t_srichard3112.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_staredown as albatros
    t_ch_albatros "Truant?" # @t_srichard3113.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Oh, you must have me confused for someone else entirely." # @t_srichard3114.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller
    t_ch_richard "Someone else…?" # @t_srichard3115.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smirk_wink as albatros
    t_ch_albatros "Y’know, just some kid who goes to your high school and probably looks like me." # @t_srichard3116.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "He sounds handsome, but it’s not me." # @t_srichard3117.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smug as albatros
    t_ch_albatros "I’m some other guy entirely, a cool guy, who graduated last year." # @t_srichard3118.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "Hmm. Well, there WERE students last year." # @t_srichard3119.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "And some of them MUST have graduated…" # @t_srichard3120.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Is it possible I started tailing the wrong person?!" # @t_srichard3121.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller
    show i_albatross_welcome_smirk as albatros
    t_ch_coolguy "Yeah, so, anyway." # @t_srichard3122.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk as albatros:
        # ShowWithAtl
        linear 2 xpos 0.75 
    extend "{w=2.0}{nw}"
    t_ch_coolguy "You should probably leave that kid alone. He keeps busy enough with his good looks and immaculate fashion sense to have to worry about you guys following him around." # @t_srichard3123.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_coolguy "Uh, whoever he is!" # @t_srichard3124.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_smirk_wink as albatros:
        # ShowWithAtl
        pause 0.3 
        linear 2 xpos 1.3 
    extend "{w=2.3}{nw}"
    t_ch_coolguy "See ya." # @t_srichard3125.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        easeout 1 xpos 0.3 
    show i_miller_pondering_serious as miller:
        # ShowWithAtl
        easeout 1 xpos 0.7 
    extend "{w=1.0}{nw}"
    t_ch_cousin "(What a strange coincidence.)" # @t_srichard3126.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller:
        # ShowWithAtl
        linear 3 xpos 1.3 
    extend "{w=3.0}{nw}"
    t_ch_cousin "(But if there’s one thing I’ve learned, it’s that Namco High is full of surprises!)" # @t_srichard3127.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.13 
        linear 0.5 ypos 1.5 
    extend "{w=1.0}{nw}"
    extend " (Uh...where did Richard get off too? It’s like he disappeared!)" # @t_srichard3127.01 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_left as digdug:
        # ShowWithAtl
        easeout 1 xpos 0.7 
    extend "{w=1.0}{nw}"
    t_ch_digdug "Shouldn’t you be...IN SCHOOL?" # @t_srichard3128.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "!!!!!" # @t_srichard3129.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (I can’t believe we risked even more detention on a wild goose chase!)" # @t_srichard3129.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Well, Richard won’t get caught, I guess. Where’d he get off to!)" # @t_srichard3130.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Sitting there and thinking your thoughts won’t get you any less in trouble." # @t_srichard3131.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller:
        # ShowWithAtl
        linear .75 xpos 0.1 
        linear .75 ypos 1.3 
    extend "{w=1.5}{nw}"
    t_ch_cousin "(Ah! There’s Richard! He’s hiding behind a crate.)" # @t_srichard3132.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(No sense in getting both of us in trouble. Hmmm. Maybe acting natural will get me out of this jam!)" # @t_srichard3133.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Nice try. You think you’re the first kid to pull the old “act natural” trick?" # @t_srichard3134.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "You’re about as natural as a tree!" # @t_srichard3135.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "B-but um trees are natural?" # @t_srichard3136.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Not on the Namco Moon! Which is where I was thinking of!" # @t_srichard3137.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "You didn’t know about that part of it." # @t_srichard3138.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "But you will soon enough!" # @t_srichard3139.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Know about the moon, I mean. Because I’m sentencing you to EXTREME LUNAR DARK SIDE DETENTION!!!" # @t_srichard3140.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(?!?!?)" # @t_srichard3141.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "It’s a project I’m working on. With Tomari." # @t_srichard3142.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Well. He’s building a rocket in his spare time and I have plans." # @t_srichard3143.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well, anyway. Y’got me." # @t_srichard3144.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I guess you should take me away." # @t_srichard3145.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, and quickly." # @t_srichard3146.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Because it’s not like there’s anyone else from Namco High here with me." # @t_srichard3147.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "And that’s just what I’ll do!" # @t_srichard3148.00 self.block='Last'
    # <NHSceneChange {'name': '_2a', 'scene': 's_day4'} NHSceneChange ''>
    label s_richard3__2a:
        # <NHSceneChange {'name': '_2a', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4