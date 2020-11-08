# <Scene {'id': 's_meowkie1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_meowkie1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_meowkie1"
    $ renpy.pause(1)
    # <Scene {'id': 's_meowkie1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/school.ogg" loop
    show i_bg_hallway_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_taira_steveholt_happy as taira zorder 2:
        default
        xpos 0.3 
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_king_confident as king zorder 2:
        default
        xpos 0.3 
        alpha 0.0
    show i_meowkie_akimbo_alert_badge as meowkie zorder 2:
        default
        xpos 0.7 
        xzoom -1.0 
    t_ch_cousin "(I’ve decided to join Meowkie as a Hall Monitor." # @t_smeowkie120.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That should keep me out of detention." # @t_smeowkie120.01 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Plus I get to hang out with an adorable kitty cat!" # @t_smeowkie121.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She’s explaining the rules now...)" # @t_smeowkie121.01 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_meowkie "...So in conclusion, that’s how you blow your whistle to stop rulebreakers!" # @t_smeowkie122.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Unless you’re in the library, in which case..." # @t_smeowkie122.01 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You should try to rely on very expressive body language." # @t_smeowkie122.02 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_alert_badge as meowkie
    t_ch_meowkie "On account of it’s a library and you gotta be quiet and all." # @t_smeowkie123.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Got all that, Boss?" # @t_smeowkie123.01 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh... oh yeah. See a rule-breaker, blow the whistle..." # @t_smeowkie124.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " Seems easy enough!" # @t_smeowkie124.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Thanks Meowkie!" # @t_smeowkie125.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Keeping out of detention is gonna be a breeze with this!" # @t_smeowkie125.01 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    t_ch_meowkie "..." # @t_smeowkie126.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh, Boss... I know it seems easy..." # @t_smeowkie126.01 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "A-and it’s okay if you think it is, that’s fine, I get it..." # @t_smeowkie127.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " but... I dunno..." # @t_smeowkie127.01 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_frown_badge as meowkie
    t_ch_meowkie "I... I kinda think it’s sorta important..." # @t_smeowkie128.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...and I try to do a good job? If that’s okay." # @t_smeowkie128.01 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(It seems like she’s really sure about that..." # @t_smeowkie129.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But maybe she’s afraid to show it." # @t_smeowkie129.01 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I should try to take this seriously, if it means that much to her.)" # @t_smeowkie130.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Meowkie... can you tell me more about what to do in, uh..." # @t_smeowkie131.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " A rule-breaking... scenario?" # @t_smeowkie131.01 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie
    t_ch_meowkie "O-oh! Yeah! You got it, Boss!" # @t_smeowkie132.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Lemme think of a good hypothetical..." # @t_smeowkie132.01 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "Nya! Got it! Okay, so chewin’ gum is against the rules inside the school..." # @t_smeowkie133.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But what if the student started chewing gum OUTSIDE the school..." # @t_smeowkie133.01 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And then came in?" # @t_smeowkie133.02 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Is it still against the rules?" # @t_smeowkie134.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie
    extend " What do you do, Boss?!" # @t_smeowkie134.01 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "Uhhh...." # @t_smeowkie135.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "It’s still against the rules!" # @t_smeowkie135.00a self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Y-Yes! Boss, exactly! Yes!" # @t_smeowkie136.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy_badge as meowkie
    extend " Wow, you really get it!" # @t_smeowkie136.01 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_normal_badge as meowkie
    t_ch_meowkie "I... if you don’t mind me saying, I think..." # @t_smeowkie138.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I think you have the makings of a great Hall Monitor." # @t_smeowkie138.01 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Wow. I didn’t think that kinda compliment would matter much to me, but...)" # @t_smeowkie139.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Thank you, Meowkie." # @t_smeowkie140.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "…..." # @t_smeowkie141.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie
    extend " ….." # @t_smeowkie141.01 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(What’s going on with her?" # @t_smeowkie142.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Her fur’s all bristling..." # @t_smeowkie142.01 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Like she’s scared to talk.)" # @t_smeowkie142.02 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "Boss... when I got my Hall Monitor badge..." # @t_smeowkie143.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It was the best day of my nine lives." # @t_smeowkie143.01 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(It sounds crazy that something like that’d be anyone’s best day..." # @t_smeowkie144.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But coming from her, I believe it.)" # @t_smeowkie144.01 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown_badge as meowkie
    t_ch_meowkie "Y’see... I might as well tell ya." # @t_smeowkie145.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " My family is..." # @t_smeowkie145.01 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Well, they’re.. bad guys." # @t_smeowkie146.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    extend " Not the main bad guys, just..." # @t_smeowkie146.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Goons. Sidekicks." # @t_smeowkie146.02 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Y’know, pathetic bad guys like that." # @t_smeowkie147.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " My parents used to work for a REALLY bad guy..." # @t_smeowkie147.01 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I don’t even like to think about his name..." # @t_smeowkie148.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We just call him “The Big Cat” at home." # @t_smeowkie148.01 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Meowkie..." # @t_smeowkie149.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "But see Boss, my parents..." # @t_smeowkie150.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They didn’t want a life like that for me." # @t_smeowkie150.01 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "They were, um, tired of being evil." # @t_smeowkie151.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So they moved to this town..." # @t_smeowkie151.01 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just so I could go to Namco High." # @t_smeowkie151.02 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Th-they, um, wanted to give me, yknow..." # @t_smeowkie152.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    extend " A good life." # @t_smeowkie152.01 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I wasn’t sure I’d fit in, but..." # @t_smeowkie153.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "On the day they gave me this Hall Monitor badge..." # @t_smeowkie154.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_normal_badge as meowkie
    t_ch_meowkie "I was so proud that they trusted me enough for it." # @t_smeowkie155.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown_badge as meowkie
    t_ch_meowkie "U-um... sorry if that sounds stupid..." # @t_smeowkie156.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Are you kidding? It doesn’t sound stupid at all." # @t_smeowkie157.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    t_ch_meowkie "Thanks for saying that, B-..." # @t_smeowkie158.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    extend " [slot_playerName]." # @t_smeowkie158.01 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I know that where I come from ain’t supposed to matter, but..." # @t_smeowkie159.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I was happy when I heard you didn’t know all that." # @t_smeowkie159.01 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Well, I’m glad you told me." # @t_smeowkie160.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " So... you’re happy here at Namco High," # @t_smeowkie160.01 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " right?" # @t_smeowkie160.02 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown_badge as meowkie
    t_ch_meowkie "…." # @t_smeowkie161.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    t_ch_meowkie "…." # @t_smeowkie162.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie
    t_ch_meowkie "...Yeah, I am!" # @t_smeowkie163.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They always have tuna for lunch..." # @t_smeowkie163.01 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "And King is always real nice to me." # @t_smeowkie164.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Th-that scary guy??)" # @t_smeowkie165.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_meowkie "So, Boss... I’m sure you like tuna too, right?" # @t_smeowkie166.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    extend " What kind of tuna do you like?" # @t_smeowkie166.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Fish again?)" # @t_smeowkie167.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Whaaa? You mean like in sushi?" # @t_smeowkie168.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Usually I prefer salmon, I guess." # @t_smeowkie168.01 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Tuna’s not my favorite!" # @t_smeowkie168.02 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown_badge as meowkie
    t_ch_meowkie "….." # @t_smeowkie169.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    t_ch_meowkie "Th-that’s okay Boss... Nobody’s perfect..." # @t_smeowkie170.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    show i_meowkie_normal_alert_badge as meowkie
    t_ch_cousin "(Wow. She seems really crushed by that.)" # @t_smeowkie171.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_blush as cousin
    t_ch_cousin "Whaa! Are you really that mad about the tuna thing!" # @t_smeowkie172.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_alert_badge as meowkie
    t_ch_meowkie "No, Boss! It ain’t that!" # @t_smeowkie173.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie
    extend " I sense a rulebreaker!" # @t_smeowkie173.01 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "You’re about to get your first lesson as a Hall Monitor!" # @t_smeowkie174.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I-if that’s okay, of course." # @t_smeowkie174.01 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Rulebreaker?" # @t_smeowkie175.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " I don’t see anything." # @t_smeowkie175.01 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Not yet! He’s coming." # @t_smeowkie176.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_alert_badge as meowkie
    t_ch_meowkie "See... even though I’m an evil goon by blood..." # @t_smeowkie177.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "Meowkie!" # @t_smeowkie178.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral_blush as cousin
    extend " I don’t think that’s who you are at all." # @t_smeowkie178.01 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    t_ch_meowkie "Oh, you don’t gotta say that." # @t_smeowkie179.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I know that ain’t... really who I am, yknow?" # @t_smeowkie179.01 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "But it’s kinda useful for hall monitoring." # @t_smeowkie180.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I got instincts for sniffin’ out people who ain’t supposed to be here." # @t_smeowkie180.01 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie
    t_ch_meowkie "Nyaa HA!" # @t_smeowkie181.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Ho there, student!" # @t_smeowkie181.01 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.9 
    show i_taira_akimbo_angry as taira:
        # FadeEvent
        linear 1.0 alpha 1.0
    extend "{w=1.0}{nw}"
    t_ch_taira "Whaaa? Wha’d I do?" # @t_smeowkie182.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "You know the rules!" # @t_smeowkie183.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " No sports allowed in the hallway!" # @t_smeowkie183.01 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_confused as taira
    t_ch_taira "But I’m just, like.. carrying the ball." # @t_smeowkie184.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "If you need sports equipment, there’s plenty to be found in the gym." # @t_smeowkie185.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s no need to carry it in the halls!" # @t_smeowkie185.01 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_alert_badge as meowkie
    t_ch_meowkie "That’s practically an invitation for..." # @t_smeowkie186.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "for..." # @t_smeowkie187.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie
    show i_cousin_default_surprised as cousin
    t_ch_meowkie "horsing around!" # @t_smeowkie188.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Wow. She says that like it’s the worst crime she can imagine!)" # @t_smeowkie189.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_alert_badge as meowkie
    t_ch_meowkie "Hurry along now please, student!" # @t_smeowkie190.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie
    extend " And don’t make that mistake again!" # @t_smeowkie190.01 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_pleading as taira
    t_ch_taira "Yikes!" # @t_smeowkie191.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_pleading as taira:
        xzoom -1.0 
        # ShowWithAtl
        linear 1 xpos -0.5 
    extend "{w=1.0}{nw}"
    extend " Y-yes ma’am!" # @t_smeowkie191.01 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Whoah... that crazy-faced guy… Captain of the Wrestleball team..." # @t_smeowkie192.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He just ran off like a dog with his tail between his legs!)" # @t_smeowkie192.01 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "Wow Meowkie... you’re tough!" # @t_smeowkie193.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_cousin_energetic_surprise_blush as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    extend "{w=0.5}{nw}"
    extend " I’m really impressed!" # @t_smeowkie193.01 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    t_ch_meowkie "Nyaa? O-oh... it was nothing..." # @t_smeowkie194.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Umm, I hope you don’t think I was being too... hard on him, it’s just..." # @t_smeowkie195.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    extend " carrying around a ball that’s s’posed to be for sports only..." # @t_smeowkie195.01 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "It’s just one step away from playing sports in the hall, I think..." # @t_smeowkie196.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And that can lead to not paying attention..." # @t_smeowkie196.01 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    extend " or getting hurt..." # @t_smeowkie196.02 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie
    show i_cousin_default_neutral as cousin
    t_ch_meowkie "And that’s why... I think it’s an important rule!" # @t_smeowkie197.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown_badge as meowkie
    t_ch_meowkie "...Maybe." # @t_smeowkie198.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "No, I think you’re right!" # @t_smeowkie199.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Meowkie..." # @t_smeowkie1100.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Not everyone would take this job so seriously." # @t_smeowkie1101.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Even I was prepared to goof off!" # @t_smeowkie1101.01 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But you obviously care so much about this..." # @t_smeowkie1102.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I hope you don’t mind me saying this, but-" # @t_smeowkie1102.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s inspiring." # @t_smeowkie1102.02 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_normal_badge as meowkie
    t_ch_meowkie "Boss.. [slot_playerName]... I …" # @t_smeowkie1103.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "I’m real glad you decided to be a Hall Monitor with me." # @t_smeowkie1104.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    t_ch_meowkie "I’ve been a little lonely doing this by myself..." # @t_smeowkie1105.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " But um, I wasn’t sure it’d be such a good idea..." # @t_smeowkie1105.01 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " if anyone else joined me." # @t_smeowkie1105.02 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Why not? Don’t you sometimes wish you’d joined a more social kind of club?" # @t_smeowkie1106.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " You know, to make friends?" # @t_smeowkie1106.01 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "..." # @t_smeowkie1107.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown_badge as meowkie
    extend " No..." # @t_smeowkie1107.01 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "No, I think bein’ alone is better." # @t_smeowkie1108.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "But Meowkie..." # @t_smeowkie1109.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    t_ch_meowkie "No Boss... I’m really sure of it." # @t_smeowkie1110.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Please... don’t make me explain, okay?" # @t_smeowkie1110.01 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "…" # @t_smeowkie1111.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(There’s something strange in her words." # @t_smeowkie1112.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Her answer makes me... a little sad.)" # @t_smeowkie1112.01 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie
    t_ch_meowkie "Oh! But don’t get me wrong, Boss." # @t_smeowkie1113.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I like bein’ alone with you." # @t_smeowkie1114.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "..." # @t_smeowkie1115.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    extend " Thanks, Meowkie." # @t_smeowkie1115.01 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    t_ch_meowkie "..." # @t_smeowkie1116.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " H-heh heh! So anyway." # @t_smeowkie1116.01 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " See any other rulebreakers, Boss?" # @t_smeowkie1116.02 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh...." # @t_smeowkie1117.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (How would I even start looking for those?)" # @t_smeowkie1117.01 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "..Not really." # @t_smeowkie1118.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie
    t_ch_meowkie "Nya! That’s good." # @t_smeowkie1119.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Once again the hallway is safe!" # @t_smeowkie1119.01 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "Haha, yeah! Thanks to you, Meowkie." # @t_smeowkie1120.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "..." # @t_smeowkie1121.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Thanks to us, Boss!" # @t_smeowkie1121.01 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_normal_badge as meowkie
    show i_cousin_energetic_laugh as cousin
    t_ch_cousinmeowkie "YEAH!!!" # @t_smeowkie1122.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Hey, does this mean I get my own Hall Monitor badge now too?" # @t_smeowkie1123.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    t_ch_meowkie "Nya ha! That’s cute!" # @t_smeowkie1124.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie
    extend " You’re thinkin’ of a Hall Monitor badge already?" # @t_smeowkie1124.01 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It takes WEEKS to earn one of those!" # @t_smeowkie1124.02 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_meowkie "...You’re gonna keep coming here, right?" # @t_smeowkie1125.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You want to earn one, dontcha?" # @t_smeowkie1125.01 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ummm..." # @t_smeowkie1126.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " ...Of course I do!" # @t_smeowkie1126.01 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_normal_badge as meowkie
    t_ch_meowkie "Nya! Boss, that’s great!" # @t_smeowkie1127.00 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Don’t worry, I’ll help ya." # @t_smeowkie1128.00 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’ve got the makings of a great Monitor!" # @t_smeowkie1128.01 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I know you can do it!" # @t_smeowkie1128.02 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "So is that it for the day?" # @t_smeowkie1129.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We’ve done our duties and the hall is safe." # @t_smeowkie1129.01 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "Haha! Not yet!" # @t_smeowkie1130.00 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We gotta pay a visit to a friend of mine, first." # @t_smeowkie1130.01 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Oh no..." # @t_smeowkie1131.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    extend " Don’t tell me...)" # @t_smeowkie1131.01 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    show i_king_confident as king:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_meowkie_normal_normal_badge as meowkie:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.9 
    extend "{w=0.5}{nw}"
    t_ch_king "(HELLO, Meowkie!)" # @t_smeowkie1132.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar2.ogg"
    extend " ROAR!" # @t_smeowkie1132.01 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "(GAH! How is she not scared out of her wits of this guy??)" # @t_smeowkie1133.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_normal_badge as meowkie
    t_ch_meowkie "Hi Boss! Yeah, there was just one rulebreaker today." # @t_smeowkie1134.00 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " A student was on the verge of playing sports in the hall!" # @t_smeowkie1134.01 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_screaming as king
    play sound "sfx/kingroar3.ogg"
    t_ch_king "ROARRR!!!" # @t_smeowkie1135.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Aw shucks, Boss! It was nothin’." # @t_smeowkie1136.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just what any good Hall Monitor would’ve done…" # @t_smeowkie1136.01 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What?! Meowkie can actually understand his roars?!)" # @t_smeowkie1137.00 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_alert_badge as meowkie
    t_ch_meowkie "Erk! Which ain’t to say I actually think of myself as a “good” Hall Monitor or nothin’!" # @t_smeowkie1138.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I just… do what I hafta do..." # @t_smeowkie1138.01 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king
    t_ch_king "(NONSENSE!)" # @t_smeowkie1139.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar1.ogg"
    extend " ROAR!" # @t_smeowkie1139.01 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar2.ogg"
    extend " ROARRRR!" # @t_smeowkie1139.02 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie
    t_ch_meowkie "O-oh… You don’t gotta say that…" # @t_smeowkie1140.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "But, thanks. Gosh, You’re always so nice to me!" # @t_smeowkie1141.00 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar3.ogg"
    t_ch_king "ROARRR!" # @t_smeowkie1142.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy as meowkie
    t_ch_meowkie "Hahaha! That’s a good one!" # @t_smeowkie1143.00 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(They’re laughing together…)" # @t_smeowkie1144.00 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 1 xpos 0.5 
    show i_sw_black as curtain2 zorder 8:
        default
        alpha 0.0
        linear 0.5 alpha 0.6
    extend "{w=1.0}{nw}"
    t_ch_cousin "(Wow... a scary guy like King..." # @t_smeowkie1145.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And Meowkie’s made friends with him." # @t_smeowkie1145.01 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Somehow, though, I’m not surprised." # @t_smeowkie1146.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " A girl like that..." # @t_smeowkie1146.01 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Not only is she likable-" # @t_smeowkie1147.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " There’s something about her that’s strong, too." # @t_smeowkie1147.01 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Stronger than I knew." # @t_smeowkie1148.00 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Maybe even stronger than she knows, too..." # @t_smeowkie1148.01 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But it seems like there’s stuff going on that she won’t tell me." # @t_smeowkie1149.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I hope someday... she feels like she can speak up. )" # @t_smeowkie1149.01 self.block='Last'
    # <NHSceneChange {'name': '_3Z', 'scene': 's_day2'} NHSceneChange ''>
    label s_meowkie1__3Z:
        # <NHSceneChange {'name': '_3Z', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2