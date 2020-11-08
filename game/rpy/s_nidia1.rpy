# <Scene {'id': 's_nidia1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_nidia1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_nidia1"
    $ renpy.pause(1)
    # <Scene {'id': 's_nidia1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/aroundtown.ogg" loop
    show i_bg_library as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_exhausted_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_nidia_notepad_happy as nidia zorder 2:
        default
        xpos 0.7 
        alpha 0.0
    t_ch_cousin "I was right behind her, but... Nidia's disappeared!" # @t_snidia135.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "She DID say Magic Club met in the library." # @t_snidia136.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    extend " Where is it?" # @t_snidia136.01 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I've checked every shelf..." # @t_snidia137.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "[slot_playerName]? Is that you? I'm in the biology section!" # @t_snidia138.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I'm also in the biology section..." # @t_snidia139.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But I don't see you at all." # @t_snidia139.01 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Try looking at it differently." # @t_snidia140.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "(Differently? I don't see anything... Wait! Out of the corner of my eye. Yes!)" # @t_snidia141.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_happy as nidia:
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_cousin "(It seems the Magic Club is hidden by some kind of ... mystical camouflage? It's a trick of the light... When I stand at the correct angle, I can see right through the shelf!)" # @t_snidia142.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_surprised as nidia
    t_ch_nidia "Don't just stand there! C'mon!" # @t_snidia143.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(I wince a little as I step THROUGH the shelf. The air inside the illusion has a buzz to it... It's soft and electric.)" # @t_snidia144.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_cousin "(Nidia is there, reading an enormous, ancient tome. It's got to be older than the school.)" # @t_snidia145.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(She seems focused.)" # @t_snidia146.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(The book is gilded. It's strange ... The cover is leathery and old, but the golden scrollwork still looks flawless, brand new.)" # @t_snidia147.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Is this magic too?)" # @t_snidia148.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_nidia_akimbo_happy as nidia
    t_ch_nidia "Sorry about that... I usually keep a Sanctuary spell up to keep people from distracting me." # @t_snidia149.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "I'm so glad you're here! At first I thought you'd come, but then I wasn't so sure! But THEN I said you're DEFINITELY coming... but THEN I gave it some more thought and --" # @t_snidia150.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "-- I'm definitely here." # @t_snidia151.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "..." # @t_snidia152.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_happy as nidia
    t_ch_nidia "You are, aren't you? Does this mean you'll join the Magic Club?" # @t_snidia153.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "You can't say something as cryptic as \"It's my destiny to save the world\" and expect me not to be curious..." # @t_snidia154.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Oh, well, I wasn't trying to be mysterious. I meant exactly what I said." # @t_snidia155.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "... Somehow that doesn't make it less mysterious." # @t_snidia156.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_surprised as nidia
    t_ch_nidia "Is that so..." # @t_snidia157.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "..." # @t_snidia158.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "......." # @t_snidia159.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "......................." # @t_snidia160.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "... Yup, still mysterious..." # @t_snidia161.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_surprised as nidia
    t_ch_nidia "Sorry... I'm just wondering where to begin." # @t_snidia162.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well... What's that book about?" # @t_snidia163.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_happy as nidia
    t_ch_nidia "It's a book of ancient prophecy!" # @t_snidia164.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Just like that?!)" # @t_snidia165.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Er-- I see..." # @t_snidia166.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_surprised as nidia
    t_ch_nidia "Do you believe in that kind of thing... ?" # @t_snidia167.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "It's all bunk!" # @t_snidia176.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " I don't believe a word of it." # @t_snidia176.01 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_happy as nidia
    t_ch_nidia "I knew you'd say that." # @t_snidia177.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "... YOU DID?!" # @t_snidia178.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_nidia "Dr. Tomari says the idea of destiny is ridiculous..." # @t_snidia179.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But HE'S always talking about permutations and variations  and quantum states and maybe someone just hasn't invented the science to measure something as big..." # @t_snidia179.01 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ... As all-encompassing..." # @t_snidia179.02 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "... As overwhelming..." # @t_snidia180.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    extend " As destiny." # @t_snidia180.01 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "............" # @t_snidia181.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well... You definitely believe in it, right? You didn't say you WANTED to save the world ..." # @t_snidia182.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You said you were DESTINED to save the world." # @t_snidia183.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What'd you mean by that?" # @t_snidia184.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Well, some day ... I'll save the world." # @t_snidia185.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It's been written..." # @t_snidia185.01 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "There's a prophecy about you?! Wow!" # @t_snidia186.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_nidia "Y-yeah..." # @t_snidia187.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What does it say?" # @t_snidia188.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "W-well... Are you sure you want to hear this?" # @t_snidia189.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Of course!" # @t_snidia190.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_worried as nidia
    t_ch_nidia "The prophecy says that ... Using an ancient amulet... I'll combine with another... and we'll meld together to become... a dragon." # @t_snidia191.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "WHOA!" # @t_snidia192.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Wait, like a metaphorical dragon?" # @t_snidia193.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "No, definitely a very literal dragon." # @t_snidia194.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Anyway, the prophecy says I'll save a kingdom..." # @t_snidia195.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "And eventually the world." # @t_snidia196.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And then I'll..." # @t_snidia196.01 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_nidia "Well, that part doesn't matter." # @t_snidia197.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(... ?? What was she going to say?)" # @t_snidia198.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "........" # @t_snidia199.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "..................." # @t_snidia1100.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin ".........................." # @t_snidia1101.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "It's okay. No one else believes me anyway." # @t_snidia1102.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "It's not that... It's just that ... When you said Magic Club..." # @t_snidia1103.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " I thought maybe you meant, like, card tricks and stuff." # @t_snidia1103.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_happy as nidia
    t_ch_nidia "Oh gosh no, that stuff is hard." # @t_snidia1104.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "...... Hahahahaha!" # @t_snidia1105.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "So you really do believe in the prophecy?" # @t_snidia1106.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "You know, at first I didn't... But I had the amulet, and there was this person... And we... Combined..." # @t_snidia1107.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Um... What exactly does she mean by 'combined'... )" # @t_snidia1108.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "... Into a dragon." # @t_snidia1109.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Wait... past tense?" # @t_snidia1110.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "You've already done it?!" # @t_snidia1111.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_happy as nidia
    t_ch_nidia "A few times. We defeated an evil sorceress and saved my home kingdom. So the first part of the prophecy was totally true..." # @t_snidia1112.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Wow. WOW! This is a lot to take in." # @t_snidia1113.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(To have already become a dragon..." # @t_snidia1114.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " she's so experienced.)" # @t_snidia1114.01 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_nidia "After that we drifted apart. I kept the amulet..." # @t_snidia1115.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_nidia "I've been trying to find a new partner..." # @t_snidia1116.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That's actually why I was in detention." # @t_snidia1116.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh?" # @t_snidia1117.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Building that kind of partnership with a new person..." # @t_snidia1118.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Like what I had before..." # @t_snidia1118.01 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It takes a lot of work." # @t_snidia1118.02 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "But I got impatient so I..." # @t_snidia1119.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You..." # @t_snidia1120.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "I started rubbing the amulet on people. Hitting them with it. Throwing it at people. That sort of thing." # @t_snidia1121.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "How... Forward..." # @t_snidia1122.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "I was hoping it would just... Work." # @t_snidia1123.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "I started with people I thought were the most compatible..." # @t_snidia1124.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " but after a while I got impatient and started hitting strangers with it." # @t_snidia1124.01 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_nidia "Or, um, 'attacking' them, as the Principal put it." # @t_snidia1125.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(That..." # @t_snidia1126.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " That's the definition of attacking... !)" # @t_snidia1126.01 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "It didn't really work. In the end someone reported me to Principal Dig Dug." # @t_snidia1127.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don't blame them." # @t_snidia1127.01 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "It was probably the wrong way to go about it." # @t_snidia1128.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Definitely the wrong way!)" # @t_snidia1129.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "I've decided to stop harassing people... But now I don't know what to do." # @t_snidia1130.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "With... THAT person... Everything just happened. It was the most natural thing in the world." # @t_snidia1131.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "That sounds really nice." # @t_snidia1132.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Yeah... Sigh." # @t_snidia1133.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "I think..." # @t_snidia1134.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That I just got lucky the first time." # @t_snidia1134.01 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_worried as nidia
    t_ch_nidia "So now I'm in a tough spot. The prophecy says I have to combine with someone else to use the amulet..." # @t_snidia1135.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "So it's not like I can just do it myself. It's so hard to find the right person... I wish..." # @t_snidia1136.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    extend " I wish..." # @t_snidia1136.01 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    extend " Sigh..." # @t_snidia1136.02 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "To tell you the truth..." # @t_snidia1137.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " I'm not very good with people." # @t_snidia1137.01 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "I always second-guess myself," # @t_snidia1138.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...and overthink what I'm going to say..." # @t_snidia1138.01 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    extend " or I spend too long thinking about what their words mean..." # @t_snidia1138.02 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Or what they might REALLY mean..." # @t_snidia1139.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    extend " By the time I get around to saying something, the other person is usually gone..." # @t_snidia1139.01 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Or thinks I'm crazy. Or I say something embarrassing in the first place, and then it's..." # @t_snidia1140.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    extend " So awkward..." # @t_snidia1140.01 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "And if you do it often enough, you get a reputation." # @t_snidia1141.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_nidia "I'm such a mess. Who'd even want to combine with me..." # @t_snidia1142.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I wish... You'd stop saying it like that... !" # @t_snidia1143.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin ".................." # @t_snidia1144.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(I don't think she heard me... )" # @t_snidia1145.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ahem." # @t_snidia1146.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " Nidia?" # @t_snidia1146.01 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Hm?" # @t_snidia1147.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I don't think you should give up so easily." # @t_snidia1148.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Principal Dig Dug's exact words were \"maybe you should give up more easily\"." # @t_snidia1149.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Yikes!)" # @t_snidia1150.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Well... Maybe I can help somehow." # @t_snidia1151.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_surprised as nidia
    t_ch_nidia "Ah! AHHH!" # @t_snidia1152.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "What? What?!" # @t_snidia1153.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_surprised as nidia
    t_ch_nidia "I thought... I mean, I think a lot... I thought maybe you were good, or maybe you were bad," # @t_snidia1154.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "... or maybe you were in the gray area like one of those hardened vigilantes with nothing to lose..." # @t_snidia1155.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_happy as nidia
    t_ch_nidia "... But you're definitely, definitely a good person!" # @t_snidia1156.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_happy as nidia
    t_ch_nidia "I have to go, but let's have a Magic Club meeting again! Really soon!" # @t_snidia1157.00 self.block='Last'
    # <NHSceneChange {'name': '_2G', 'scene': 's_day2'} NHSceneChange ''>
    label s_nidia1__2G:
        # <NHSceneChange {'name': '_2G', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2