# <Scene {'id': 's_amazona1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_amazona1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_amazona1"
    $ renpy.pause(1)
    # <Scene {'id': 's_amazona1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_amazona1_initialize:
        # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
        # <Events {} events ''>
        show i_bg_quad_tents as bg zorder 0 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_cousin_default_neutral as cousin zorder 2:
            default
            xpos 0.25 
        show i_donko_default_wink as donko zorder 2:
            default
            alpha 0.0
            xpos 0.7 
        show i_miller_aliens_serious as miller zorder 2:
            default
            alpha 0.0
            xpos 0.7 
            ypos 1.2 
        show i_tomari_standing_mortified as tomari zorder 2:
            default
            alpha 0.0
            xpos 0.7 
        show i_taira_steveholt_happy as taira zorder 2:
            default
            alpha 0.0
            xpos 0.7 
        show i_aki_default_smile as aki zorder 2:
            default
            xpos 0.7 
        play music "bgm/aroundtown.ogg" loop

    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "So... Like... What do you do for fun, Aki?" # @t_samazona139.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_distracted as aki
    t_ch_aki "Fun?" # @t_samazona140.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah, like in your free time..." # @t_samazona141.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/sentaisignal.ogg"
    show i_aki_default_nervouslaughter as aki
    t_ch_aki "Free time... I've heard of it." # @t_samazona142.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "............" # @t_samazona143.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "You never like... Go home and play video games? Or just hang out with your friends?" # @t_samazona144.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "I have to go!" # @t_samazona145.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "...Huh?" # @t_samazona146.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_shocked as aki
    t_ch_aki "I have to go! But I'll be back in a minute... Just, um, just stay right here!" # @t_samazona147.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_shocked as aki:
        # FadeEvent
        linear 0.75 alpha 0.0
    extend "{w=0.75}{nw}"
    t_ch_cousin "Okay......... Your faithful assistant will be waiting... Right here........" # @t_samazona148.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "......................." # @t_samazona149.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin ".................................." # @t_samazona150.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(It's been at least 10 minutes..." # @t_samazona151.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Is she coming back?)" # @t_samazona151.01 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(Did she blow me off?)" # @t_samazona152.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Maybe I'll ask around... )" # @t_samazona153.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Hey... Does anyone know where Aki is?" # @t_samazona154.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_donko "Like... Where ISN'T she? Girlfriend is, like, EVERYWHERE." # @t_samazona155.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Every club, every sport, every subject, honey." # @t_samazona156.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "She's so good at music club." # @t_samazona157.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "What does she play?" # @t_samazona158.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Only, like, EVERY instrument!" # @t_samazona159.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_grin as donko:
        xzoom -1.0 
    extend " But you should see her go nuts on a tuba." # @t_samazona159.01 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "It's..." # @t_samazona160.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " transcendent." # @t_samazona160.01 self.block='Last'
    show i_donko_ygg_grin as donko:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_taira_steveholt_happy as taira:
        # FadeEvent
        linear 0.25 alpha 1.0
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Yeah! You wouldn't guess it from looking at her... But she's really good at Wrestleball!" # @t_samazona161.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "... What's it got to do with looks?" # @t_samazona162.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I dunno! Wrestleball players usually have super hot muscular bodies, like mine!" # @t_samazona163.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Anyway, she's got the best aim on the team. She NEVER misses her target, yo. And she always finds an opening!" # @t_samazona164.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_happy as taira
    t_ch_taira "If I'm the brawn, then she's the brains! Well no, I'm the brains too." # @t_samazona165.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Really, I'm the brawn, the brains, and the heart of the team. But she's definitely like... Some other vital organ." # @t_samazona166.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " Like the hair." # @t_samazona166.01 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "ANYWAY..." # @t_samazona167.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_taira "She also plays a bunch of other sports like... Baseball and lacrosse or whatever? Those fake sports that don't matter." # @t_samazona168.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "But she's MAD good at fake sports too." # @t_samazona169.00 self.block='Last'
    show i_tomari_pondering_thoughtful as tomari:
        # FadeEvent
        linear 0.25 alpha 1.0
    show i_taira_akimbo_happy as taira:
        # FadeEvent
        linear 0.25 alpha 0.0
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_mortified as tomari
    t_ch_tomari "I must admit... As the smartest student at this school..." # @t_samazona170.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_tomari "She comes very close to my own genius." # @t_samazona171.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "She and I are the only students in the top percentile..." # @t_samazona172.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We are the ones who \"throw the curve\", as you simpler folk say it." # @t_samazona172.01 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "I've only seen her get less than 100.0 once, and it was a grading error on the part of her teacher." # @t_samazona173.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "She... corrected the teacher?!" # @t_samazona174.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Yes. And then the teacher was fired and Aki taught the class for the rest of the semester." # @t_samazona175.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Wow..." # @t_samazona176.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "If she weren't so distracted by everything she participates in, she might become a worthy opponent." # @t_samazona177.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "O... Opponent?!" # @t_samazona178.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_thoughtful as tomari
    t_ch_tomari "For robot battle, of course!" # @t_samazona179.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What's wrong with this school... )" # @t_samazona180.00 self.block='Last'
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 1.0
    show i_tomari_pondering_thoughtful as tomari:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_cousin_default_neutral as cousin
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Yeah... She never really has time to hang out. It's super disappointing." # @t_samazona181.00 self.block='Last'
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_taira_akimbo_serious as taira:
        # FadeEvent
        linear 0.25 alpha 1.0
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "SIIIGH... After a big win, everyone always gets together for like... A victory pizza party." # @t_samazona182.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused as taira
    t_ch_taira "Except Aki... She always says she has to \"go study\"." # @t_samazona183.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...Wish she'd study my muscles, yo." # @t_samazona183.01 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Everyone should." # @t_samazona183.02 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ANYWAY... can't say I know her that well. Sigh." # @t_samazona183.03 self.block='Last'
    show i_taira_default_confused as taira:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 1.0
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Yeah... And she's always running off in the middle of conversations! It's like... She's TOO busy." # @t_samazona184.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_tomari_pondering_thoughtful as tomari:
        # FadeEvent
        linear 0.25 alpha 1.0
    $ renpy.pause(0.25) # TimedPause
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Affirmative, yo." # @t_samazona185.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_thoughtful as tomari:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_taira_default_confused as taira:
        # FadeEvent
        linear 0.25 alpha 1.0
    $ renpy.pause(0.25) # TimedPause
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "YEAH. Like... I get that she's always working and all, but sometimes it's mad rude?!" # @t_samazona186.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "YOU'RE concerned with rudeness..." # @t_samazona187.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "Well YEAH. My manners are the best, yo." # @t_samazona188.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_halfgrin as miller:
        # FadeEvent
        linear 0.25 alpha 1.0
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.25 alpha 0.0
    $ renpy.pause(0.25) # TimedPause
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_halfgrin as miller:
        # ShowWithAtl
        linear 0.333 ypos 0.5 
    extend "{w=0.333}{nw}"
    t_ch_miller "I've got news for you... ordinary student Aki Matsuo.... Is not so ordinary!!!" # @t_samazona189.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_miller "I saw her disappear into a classroom the other day... And the person who came out was a superhero!! Purple and pink, the works!" # @t_samazona190.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_miller "She was sneaking around, hoping no one saw her..." # @t_samazona191.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_serious as miller
    t_ch_miller "But there's no one better at sneaking around than me!!" # @t_samazona192.00 self.block='Last'
    show i_donko_ygg_meloncholic as donko:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 1.0
    $ renpy.pause(0.25) # TimedPause
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "So sad..." # @t_samazona193.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_serious as miller
    t_ch_miller "Isn't it?! She's hiding her identity from the whole school!" # @t_samazona194.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "... So sad that you finally cracked, sweetie!" # @t_samazona195.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_shocked as miller
    t_ch_miller "Huh?!" # @t_samazona196.00 self.block='Last'
    show i_taira_revenge_serious as taira:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.25 alpha 1.0
    $ renpy.pause(0.25) # TimedPause
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Yeah, you sayin' some crazy stuff, yo." # @t_samazona197.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Like, mad crazy." # @t_samazona198.00 self.block='Last'
    show i_tomari_pondering_thoughtful as tomari:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_tomari_pondering_thoughtful as tomari:
        # FadeEvent
        linear 0.25 alpha 1.0
    $ renpy.pause(0.25) # TimedPause
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Using Occam's Razor, my conclusion is that it's more likely you've lost it, rather than Aki. It's a simple determination." # @t_samazona199.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_miller ".........." # @t_samazona1100.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller
    t_ch_miller ".....  I ' L L  B E  B A C K ....." # @t_samazona1101.00 self.block='Last'
    show i_miller_pondering_serious as miller:
        # ShowWithAtl
        linear .3 ypos 1.5 
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_thoughtful as tomari:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_cousin_default_surprised as cousin:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_cousin "Uhhh..." # @t_samazona1102.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Thanks for the info, guys. Well... Most of you." # @t_samazona1103.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(You know... I was a little annoyed that she just ditched me like that.)" # @t_samazona1104.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But hearing everything she does..." # @t_samazona1105.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It's kind of amazing.)" # @t_samazona1105.01 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I was pretty irritated earlier... )" # @t_samazona1106.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(... But I'm beginning to feel... A kind of grudging admiration for how single-minded she is about her goals.)" # @t_samazona1107.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I was just looking at her as a way to get out of detention," # @t_samazona1108.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " but I really could learn a lot from Aki.)" # @t_samazona1108.01 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_shocked as aki:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_aki "AH! HAHA! I'm back! Sorry about that! Hahaha..." # @t_samazona1109.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It's okay... I was talking to the other students about you, actually." # @t_samazona1110.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_shocked as aki
    t_ch_aki "You were?!" # @t_samazona1111.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Yeah! And I just wanted to say... I really admire how much you're able to do. It's inspiring, Aki!" # @t_samazona1112.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_aki "Oh... Thanks..." # @t_samazona1113.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/sentaisignal.ogg"
    show i_aki_default_nervouslaughter as aki

    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_nervouslaughter as aki:
        # FadeEvent
        linear 0.25 alpha 0.0
    extend "{w=0.25}{nw}"
    t_ch_aki "I have to go! Nice chatting with you!" # @t_samazona1114.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(That was... Not the reaction I was expecting... )" # @t_samazona1115.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(She does do a LOT... But I wonder if there's more to her than all of the crazy stuff I've already learned?)" # @t_samazona1116.00 self.block='Last'
    # <NHSceneChange {'name': '_1q', 'scene': 's_day2'} NHSceneChange ''>
    label s_amazona1__1q:
        # <NHSceneChange {'name': '_1q', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2