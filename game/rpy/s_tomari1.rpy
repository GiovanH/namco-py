# <Scene {'id': 's_tomari1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_tomari1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_tomari1"
    $ renpy.pause(1)
    # <Scene {'id': 's_tomari1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/privatetimes.ogg" loop
    show i_bg_shopclass as bg zorder 0 at default
    show i_sw_black as curtain2 zorder 9:
        default
        alpha 0.7
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_tomari_standing_mortified as tomari zorder 2:
        default
        xpos 1.4 
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.5 
    t_ch_cousin "(Wow, it’s awful dark in here.)" # @t_stomari151.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hope I’m not late.)" # @t_stomari152.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And also that I’m in the right place.)" # @t_stomari153.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(But, ALSO also that this is NOT where Tomari lures new kids so they’re isolated and in the dark and no one sees him come up from behind with a giant axe to kill ‘em and no one notices because they haven’t had time to make friends in the community yet!)" # @t_stomari154.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(The murdered kids I mean.)" # @t_stomari155.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But, more so, I really hope Tomari doesn’t axe murder anyone actually.)" # @t_stomari156.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Or murder at all in a general sense.)" # @t_stomari157.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(WHY AM I FREAKING OUT ABOUT BEING MURDERED??)" # @t_stomari158.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Especially by a goofy guy like Tomari.)" # @t_stomari159.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        linear 0.333 xpos 0.7 
    show i_cousin_default_mortified as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    extend "{w=0.333}{nw}"
    t_ch_tomari "Hi, [slot_playerName]." # @t_stomari160.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "AAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHH!!!" # @t_stomari161.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Um." # @t_stomari162.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(DEEP BREATH, [slot_playerName]! YOU WILL LIVE THROUGH THIS!)" # @t_stomari163.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "You, uh, okay?" # @t_stomari164.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "YES! THE MOST OKAY AND ALIVE!" # @t_stomari165.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "You’re yelling though?" # @t_stomari166.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "AM I? NOT FOR HELP THOUGH!" # @t_stomari167.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "HAHA!" # @t_stomari168.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "BECAUSE WE’RE FINE HERE AREN’T WE. Ha! Heh." # @t_stomari169.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Ahem." # @t_stomari169.01 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "What I meant to say, when I screamed in complete primal fear was, “Hey, Tomari.”" # @t_stomari170.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_smile as tomari
    t_ch_tomari "Uh, yeah. Glad you could make it! I’m afraid I brought you down here under false pretenses." # @t_stomari171.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "(DON’T PANIC)" # @t_stomari172.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "The engineering club could use some new blood." # @t_stomari173.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(B-B-BLOOD?!?!?)" # @t_stomari174.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "There’s just Hiromi and me. And, technically, she’s not in the club." # @t_stomari175.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thoughtful as tomari
    t_ch_tomari "Her motorcycle is." # @t_stomari176.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "Whew!" # @t_stomari177.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thinking as tomari
    t_ch_tomari "Hm?" # @t_stomari178.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "Uh. What I mean is, y’know, more club resources for us, AM I RIGHT!" # @t_stomari179.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "Ha, that’s the spirit! And you are, indeed, quite right!" # @t_stomari180.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    show i_tomari_alive_smile as tomari
    t_ch_tomari "BEHOLD!" # @t_stomari181.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_tarp "…" # @t_stomari182.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wait…what if that’s where he keeps the bodies!!!!)" # @t_stomari183.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s uh n-n-nice tarp…?" # @t_stomari183.01 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Haha! Not the tarp. What’s underneath it!" # @t_stomari184.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And, uh, what would that be exactly?" # @t_stomari185.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "My secret project." # @t_stomari186.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(MURDER BODIES WOULD BE A BIG SECRET!!!)" # @t_stomari187.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_smile as tomari
    t_ch_tomari "I know we just met, but I feel like I can tell you all about it." # @t_stomari188.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Anyway, it’s not like I could keep it secret from a fellow engineering genius like yourself for long anyway!" # @t_stomari189.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "Haha! That sure is the real truth!" # @t_stomari190.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_tomari "No one but me knows it, but we’re engaged in a robotics cold war with the twisted genius Dr. Kubota from Evil Namco High!" # @t_stomari191.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Hang on. His name is Doctor or IS a doctor? And if it’s the second one, then how is he in high school?" # @t_stomari192.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "How do we have a spaceship student?" # @t_stomari193.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Fair enough!" # @t_stomari194.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "So, evil genius, and robots? That’s bad!" # @t_stomari195.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "You have no idea, [slot_playerName]." # @t_stomari196.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_frustrated as tomari
    t_ch_tomari "NO ONE DOES!" # @t_stomari197.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(Whoa, must be serious.)" # @t_stomari198.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_tomari "If Dr. Kubota gains the upper hand, it may very well plunge all of Namco Land into ten thousand years of darkness!" # @t_stomari199.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(WHAT!!!)" # @t_stomari1100.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_smile as tomari
    t_ch_tomari "But now I’ve got a secret weapon." # @t_stomari1101.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "(Like a murder axe?!)" # @t_stomari1102.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "Your brain!" # @t_stomari1103.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(My brain?!)" # @t_stomari1104.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "(An axe would be better!)" # @t_stomari1105.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_tomari "Only my super robot project can defeat Dr. Kubota’s vile machinations, but it’ll take all our smarts to get it working and save Namco Land from certain doom." # @t_stomari1106.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(GULP! What’ve I gotten myself into! I CAN’T BUILD A ROBOT!)" # @t_stomari1107.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_smile as tomari
    t_ch_tomari "But that bleak nightmare is no longer the inevitable result of current conditions!" # @t_stomari1108.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, yeah. It definitely isn’t." # @t_stomari1109.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Because now Namco High has a shot at winning the Robot Battle Brawl competition." # @t_stomari1110.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Wait the what?" # @t_stomari1111.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Which everyone knows is the most popular sport in the whole school." # @t_stomari1112.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I never heard anyone call it that.)" # @t_stomari1113.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Or anything at all, actually.)" # @t_stomari1114.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Because no one ever mentions it!)" # @t_stomari1115.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_tomari "I calculated the damage to school spirit, morale, and morals of the entire student body if Namco High loses the next Robot Battle Brawl match against Evil Namco High." # @t_stomari1116.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "[slot_playerName], it would be disastrous to the power of catastrophic." # @t_stomari1117.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "I had to invent a whole new word to describe it:" # @t_stomari1118.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_frustrated as tomari
    t_ch_tomari "DISASTROPHIC!" # @t_stomari1119.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Grades plummet, tardies skyrocket, attendance is reduced to a handful of students seeking shelter from the juvenile raider gangs that will band together to roam the wasteland and prey on the weak." # @t_stomari1120.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "This is the dark future that hangs in the balance." # @t_stomari1121.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_thinking as tomari
    t_ch_tomari "Heavy is the head that wears the Robot Battle Brawl crown, [slot_playerName]." # @t_stomari1122.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Okay." # @t_stomari1123.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Um." # @t_stomari1124.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Preeeeeeeeetty sure Wrestleball is the most popular sport in school though?" # @t_stomari1125.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_tomari "Wrestleball? Oh, what, just because kids constantly talk about it?" # @t_stomari1126.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "And a ton of them go to the games?" # @t_stomari1127.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "And the practices?" # @t_stomari1128.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "And also play the game, either for the school or for fun at home? And the video game? Or all of the above?" # @t_stomari1129.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "That’s supposed to mean it’s “popular?”" # @t_stomari1130.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That’s the definition of popular, so yeah." # @t_stomari1131.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_tomari "Well." # @t_stomari1132.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Imagine a sport even more popular than that then!" # @t_stomari1133.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Oof, I’m trying, but wow, it’s not easy!" # @t_stomari1134.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "What if I told you…" # @t_stomari1135.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "…it didn’t need to be imagined?" # @t_stomari1136.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_smile as tomari
    extend " BECAUSE IT’S ROBOT BATTLE BRAWL!" # @t_stomari1136.01 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(It’s cute how into this stuff Tomari is, but he’s a little delusional about it!)" # @t_stomari1137.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " Tomari. If Battle Robo Brawl –" # @t_stomari1137.01 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thinking as tomari
    t_ch_tomari "Robot Battle Brawl." # @t_stomari1138.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, right, that too." # @t_stomari1139.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If it’s so popular, then why are you the only student in the engineering club? Shouldn’t this place be packed?" # @t_stomari1140.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Oh, that’s easy. I wouldn’t let anyone else join." # @t_stomari1141.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Really?" # @t_stomari1142.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_frustrated as tomari
    t_ch_tomari "This is war, [slot_playerName]." # @t_stomari1143.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_frustrated as tomari
    t_ch_tomari "Big stomping robot war!" # @t_stomari1144.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "They’d only get in the way. Just slow me down." # @t_stomari1145.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Always wanting help with their own projects. As if I’m not consulting enough students on extra-curricular projects as it is!" # @t_stomari1146.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Hiromi and her bike, Max and his plane, Principal Dig Dug and his lunar detention rocket…" # @t_stomari1147.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Wait, there’s a rocket?" # @t_stomari1148.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Or, THE ABSOLUTE WORST, talking to me." # @t_stomari1149.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That’s…bad?" # @t_stomari1150.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "It’s awful. They drone on and on about whatever nonsense people limited to baseline intelligence have the inclination to discuss among their own kind." # @t_stomari1151.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_tomari "I believe a lot of it concerns professional sports statistics and celebrity embarrassments." # @t_stomari1152.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "And they have the audacity to assault me with it!" # @t_stomari1153.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "We can, in time, solve any problem we put to ourselves with nothing more than hypothesis based on observation." # @t_stomari1154.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thinking as tomari
    t_ch_tomari "All because of the mind!" # @t_stomari1155.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_frustrated as tomari
    t_ch_tomari "THE MIND, [slot_playerName]!" # @t_stomari1156.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "The most powerful and versatile tool in the known universe. We’ve all got one, but most people spend their lives acting as if they don’t!" # @t_stomari1157.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "They cultivate distraction in place of wisdom! Trivia in place of knowledge!" # @t_stomari1158.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Sheesh, Tomari’s got some intense opinions about, uh, society I guess? He sounds like a supervillain!)" # @t_stomari1159.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I mean, he wants to save the world from total devastation, so that’s good. But the devastation he’s worried about isn’t actually a real problem. But he thinks it is!)" # @t_stomari1160.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(I think he’s a good person, deep down, it’s just all those brains are getting in the way!)" # @t_stomari1161.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_tomari "But to answer your question more completely, re: lack of students in the club, you’re forgetting that for the purposes of official club business, Hiromi’s motorcycle counts as a student." # @t_stomari1162.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thinking as tomari
    t_ch_tomari "Heck, it gets better grades than Taira!" # @t_stomari1163.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Okay, well, two students still isn’t all that great though." # @t_stomari1164.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_smile as tomari
    t_ch_tomari "So modest not to count yourself!" # @t_stomari1165.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Oh, right. Me.)" # @t_stomari1166.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " Yeah. And I’ll contribute." # @t_stomari1166.01 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I’ll contribute BIG TIME." # @t_stomari1167.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "But I think you may be overestimating the effect the brawling robot battle will have on, uh, the world." # @t_stomari1168.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_tomari "Impossible. I did the calculations myself." # @t_stomari1169.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "With or without the glasses, I ask purely out of curiosity?" # @t_stomari1170.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Without, of course." # @t_stomari1171.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Yeah, I thought so." # @t_stomari1172.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_frustrated as tomari
    t_ch_tomari "They were confiscated after the explosion." # @t_stomari1173.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "The...I’m sorry..." # @t_stomari1174.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "The EXPLOSION?" # @t_stomari1175.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "If I’m to be perfectly honest, it was the explosion…" # @t_stomari1176.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "...s." # @t_stomari1177.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_tomari "Plural." # @t_stomari1178.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_tomari "Though a case could be made that it was the FINAL explosion, singular, that broke the camel’s back, as it were." # @t_stomari1179.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari
    t_ch_tomari "Also about one-third of the plumbing on campus." # @t_stomari1180.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_tomari "And the computer lab." # @t_stomari1181.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_tomari "HOWEVER, I made the case that it wasn’t any of the explosions caused by my experiments that damaged school property!" # @t_stomari1182.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_frustrated as tomari
    t_ch_tomari "Rather it was the school’s lack of significantly reinforced infrastructure to withstand explosive forces that ALLOWED it to be destroyed." # @t_stomari1183.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari
    t_ch_tomari "It was a brilliant defense, but the administrators weren’t swayed." # @t_stomari1184.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "Since they couldn’t very well lock up my brain, they confiscated my glasses instead." # @t_stomari1185.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Ironically, their short sighted thinking has only exacerbated by short sighted SEEING and all progress on the super robot has come to a halt THEREFORE DOOMING US ALL!" # @t_stomari1186.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "I brought this to the attention of the administration, and was brutally rebuffed." # @t_stomari1187.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Who could have guessed robot brawls and explosions would feature so heavily in the life of a harmless looking bookworm?)" # @t_stomari1188.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hmmm.)" # @t_stomari1189.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Maybe I should try to help out just to keep him out of trouble!)" # @t_stomari1190.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Even so, Tomari, I’m not sure a single high school sports match can plunge the world into ten thousand years of darkness." # @t_stomari1190.01 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "Wow, you’re good!" # @t_stomari1191.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "You haven’t even seen the equations, but you immediately intuited that ten thousand years was the worst case scenario." # @t_stomari1192.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thinking as tomari
    t_ch_tomari "But, you’re right, there’s a chance we may only have to endure five thousand years of darkness." # @t_stomari1193.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Even so, I don’t like those odds. But that’s what you’re here for!" # @t_stomari1194.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Uh, yeah. Me. I will do stuff right, like, wow." # @t_stomari1195.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "I bet! Hey, let’s get started." # @t_stomari1196.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(ALREADY?!?)" # @t_stomari1197.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " Uh, yeah. Started. That’s what we’ll do. Right now. Yeah. Can’t wait." # @t_stomari1197.01 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_tomari "Okay, so you fixed the nanofiber locomotive matrix this morning, and you’d think that’d be the end of our problems, but it’s only the beginning!" # @t_stomari1198.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "Swell…" # @t_stomari1199.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_smile as tomari
    t_ch_tomari "Glad you enjoy the thrill of a challenging project as much as I do, [slot_playerName]!" # @t_stomari1200.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Wonder if I could fake a heart attack…)" # @t_stomari1201.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(But then Tomari might think he could learn cardiology by practicing it on me!)" # @t_stomari1202.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Uh-oh. He’s been talking this whole time…Should I have been paying attention?)" # @t_stomari1203.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "blah blah GN/DN polarity got switched. And I don’t have to tell YOU what that means! My first thought was to blah blah blah" # @t_stomari1204.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(I HAVE NO IDEA WHAT HE’S TALKING ABOUT!)" # @t_stomari1205.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Then again, I still wouldn’t know what he was talking about even if I heard the whole thing.)" # @t_stomari1206.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Smile and nod, [slot_playerName]. Smile and nod.)" # @t_stomari1207.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Just gotta keep an eye on this guy so he doesn’t accidentally blow up any more school property. Or himself. It’s not that bad.)" # @t_stomari1208.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I mean, he’s kinda easy on the ol’ eye keepin’ itself on him, IF I KNOW WHAT I MEAN.)" # @t_stomari1209.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And I do.)" # @t_stomari1210.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(So, that helps.)" # @t_stomari1211.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Uh-oh. I think he’s waiting for me to say something…)" # @t_stomari1212.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_tomari "What do you think? Any ideas?" # @t_stomari1213.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(STALL STALL STALL)" # @t_stomari1214.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uhhhhhhhhhh." # @t_stomari1214.01 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (STAAAAAAAAAAALLLLLL)" # @t_stomari1214.02 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Yes." # @t_stomari1214.03 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_smile as tomari
    t_ch_tomari "Great." # @t_stomari1215.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Nailed it!)" # @t_stomari1216.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yup. It is great." # @t_stomari1217.00 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "So, let’s hear ‘em." # @t_stomari1218.00 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(AAAARGH!)" # @t_stomari1219.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "You should…" # @t_stomari1220.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh." # @t_stomari1221.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Fix the thing. That, um..." # @t_stomari1222.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "...needs fixing." # @t_stomari1223.00 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_tomari "Yeah, but which of the three methods I described do you think we should try?" # @t_stomari1224.00 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(WHAT? When’d he say anything like that?)" # @t_stomari1225.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Oh, right. When I wasn’t really paying attention probably.)" # @t_stomari1226.00 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Okay! I’ll just say, like, “That last one.” I mean, y’know, whatever, they’re probably mostly the same, right?)" # @t_stomari1227.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Each one has a distinct and unique advantage counterbalanced by an ARBITRARILY DEVASTATING AND EASILY EXPLOITED weakness." # @t_stomari1228.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What?! Why does it work like that?!)" # @t_stomari1229.00 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "As you know, that’s just how science works." # @t_stomari1230.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(UGH!!!)" # @t_stomari1231.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "These factors need to be carefully considered with regard to their potential impacts upon the super robot’s combat capabilities." # @t_stomari1232.00 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Well. Okay. Still not that bad. If I choose the wrong one, it’s no big deal, right? We’ll just try something else.)" # @t_stomari1233.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Yeah!)" # @t_stomari1234.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_mortified as tomari
    t_ch_tomari "AND WE HAVE TO GET IT EXACTLY RIGHT ON OUR FIRST TRY!" # @t_stomari1235.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(OH COME ON ALREADY!!!)" # @t_stomari1236.00 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thoughtful as tomari
    t_ch_tomari "Dr. Kubota could attack at any moment. We can’t risk being half done with our second or third try when he does!" # @t_stomari1237.00 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah. That would be a disaster!" # @t_stomari1238.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Oh crap oh crap what do I do!)" # @t_stomari1239.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What am I saying? It’s just a silly high school rivalry in a sport no one cares about anyway. It doesn’t matter what I pick!)" # @t_stomari1240.00 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh, let’s do the first one." # @t_stomari1241.00 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_tomari "The first one? Are you sure?" # @t_stomari1242.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, no? Yeah, let’s go for the last one." # @t_stomari1243.00 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Really? That one?" # @t_stomari1244.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well, I mean, y’know, the second one then maybe." # @t_stomari1245.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "I feel like there’s something you’re not telling me, [slot_playerName]." # @t_stomari1246.00 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(He’s on to me! BETTER SAY SOMETHING FAST!)" # @t_stomari1247.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Do that thing with the part that doesn’t work how you want and make it good!" # @t_stomari1248.00 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " (Yeah! That sounded sufficiently technical!)" # @t_stomari1248.01 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_tomari "But...it’s not one part that isn’t working, it’s a whole subsystem and there’s a few ways to approach it." # @t_stomari1249.00 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "YEAH I KNEW THAT!" # @t_stomari1250.00 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thoughtful as tomari
    t_ch_tomari "Hmm…" # @t_stomari1251.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thoughtful as tomari
    t_ch_tomari "I think I know what you’re getting at, [slot_playerName]…" # @t_stomari1252.00 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    extend " You’re saying I’ve gone about the problem all wrong!" # @t_stomari1252.01 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Um." # @t_stomari1253.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Yyyyyyyyyyyyyyyyyyy" # @t_stomari1254.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Nnnnnnnnnnnnnnnnnnnnnnnnnn" # @t_stomari1255.00 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yyyyyyyyyyyyyyyyeeeeaaah…" # @t_stomari1256.00 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…?" # @t_stomari1257.00 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "I’m...I’m not used to speaking with someone who can operate at my own level." # @t_stomari1258.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Haha! Yeah, I know what you mean." # @t_stomari1259.00 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (I mean, kind of!)" # @t_stomari1259.01 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_tomari "So, which part do you think it is that’s causing all the trouble?" # @t_stomari1260.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ah. Yes. That’s. Hm. Yes, that’s a question." # @t_stomari1261.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "We should answer it!" # @t_stomari1262.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "With information. Hm. Yup. Yeah." # @t_stomari1263.00 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Sounds like you’re suggesting we do some research." # @t_stomari1264.00 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Ah-ha! He can’t accidentally blow up anything if we’re just reading books in the library!)" # @t_stomari1265.00 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And, who knows, maybe I’ll pick up some of this engineering stuff while we’re there. This could turn into a pretty cool thing for us to do. Yeah!)" # @t_stomari1266.00 self.block='Last'
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The research. Yes! That." # @t_stomari1266.01 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "Great! It’s a little late to start on that now, but I’ll get a reading list together and we can hit the books tomorrow!" # @t_stomari1267.00 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yes. Super." # @t_stomari1268.00 self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Uh, see you then, Tomari." # @t_stomari1269.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.5 
    extend "{w=0.333}{nw}"
    extend " (He’s not so bad once you get him to open up a little.)" # @t_stomari1269.01 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I mean, okay, he’s still crazy. But it’s a cute kind of crazy.)" # @t_stomari1270.00 self.block='Last'
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Well. Until there’s explosive experiments, I guess...)" # @t_stomari1271.00 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But we’re gonna work on that!)" # @t_stomari1272.00 self.block='Last'
    # <NHSceneChange {'name': '_3q', 'scene': 's_day2'} NHSceneChange ''>
    label s_tomari1__3q:
        # <NHSceneChange {'name': '_3q', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2