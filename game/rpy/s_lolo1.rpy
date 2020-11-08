# <Scene {'id': 's_lolo1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_lolo1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_lolo1"
    $ renpy.pause(1)
    # <Scene {'id': 's_lolo1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/school.ogg" loop
    show i_bg_classroom_b as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_lolo_default_frustrated as lolo zorder 2:
        default
        xpos 0.7 
    show i_trio_preps as students:
        default
        alpha 0.0
        xpos 0.5 
    t_ch_cousin "(Lolo is taking me to the yearbook club room." # @t_slolo10.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I guess this is it." # @t_slolo10.01 self.block='Last'
    show i_trio_preps as students:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Hmm, there’s more people here than I thought there’d be.)" # @t_slolo10.02 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.15 
    show i_lolo_default_frustrated as lolo:
        # ShowWithAtl
        linear 0.5 xpos 0.85 
    extend "{w=0.5}{nw}"
    t_ch_student1 "Hello, newcomer! Welcome to Yearbook Club!" # @t_slolo11.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student2 "I hope you’re ready to join us in capturing the memories of another great school year!" # @t_slolo12.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student3 "I’M SO EXCITED" # @t_slolo13.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Are they..." # @t_slolo14.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...Serious...)" # @t_slolo14.01 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "C’mon, [slot_playerName]. Let’s go sit in the back and work on our..." # @t_slolo15.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...Uh..." # @t_slolo15.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " Yearbook... stuff." # @t_slolo15.02 self.block='Last'
    show i_trio_preps as students:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_lolo_crossed_frustrated as lolo:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(I’m sure glad I came here with Lolo." # @t_slolo16.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Looks like those other Yearbook Club members are preoccupied at the front of the class..." # @t_slolo17.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don’t think they’re paying attention to the two of us just sitting here in the back." # @t_slolo17.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s a relief. )" # @t_slolo17.02 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "..." # @t_slolo18.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    extend " I’m kinda surprised you would join a club just to goof off." # @t_slolo18.01 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Huh? How come?" # @t_slolo19.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I dunno. You just seem like..." # @t_slolo110.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The goody-two-shoes, Pollyanna type." # @t_slolo110.01 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " No offense, I guess..." # @t_slolo110.02 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "None taken..." # @t_slolo111.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m glad we can just chill here anyway." # @t_slolo111.01 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "It’s pretty weird, right?" # @t_slolo112.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What’s weird?" # @t_slolo113.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "The other kids in the club." # @t_slolo114.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They seem to care SO MUCH about this." # @t_slolo114.01 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_frustrated as lolo
    extend " It kinda creeps me out." # @t_slolo114.02 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha, aww..." # @t_slolo115.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s a little harsh, isn’t it?" # @t_slolo115.01 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean..." # @t_slolo115.02 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I wouldn’t get so into a club like this, but..." # @t_slolo116.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s kinda cool that they’re so sincerely interested in it." # @t_slolo116.01 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "...Heh. Maybe you ARE a goody-two-shoes." # @t_slolo117.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "You really don’t see anything... I dunno... kinda charming about it?" # @t_slolo118.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "In people deceiving themselves?" # @t_slolo119.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What do you mean?" # @t_slolo122.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Isn’t it obvious..." # @t_slolo123.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Everyone hates high school, don’t they?" # @t_slolo124.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " And nobody stays in touch after they leave." # @t_slolo124.01 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "It’s all … meaningless time." # @t_slolo125.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "So why waste your energy making a book of memories you’d really rather not even have?" # @t_slolo126.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_lolo "Everybody just drifts away..." # @t_slolo127.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_shrug_frustrated as lolo
    extend " Or they realize that the people they thought were their friends weren’t really friends to begin with." # @t_slolo127.01 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Lolo..." # @t_slolo128.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "It isn’t just high school, either." # @t_slolo129.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Everyone goes through life spending time with their “friends”..." # @t_slolo129.01 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " Until they have to leave for one reason or another, and they forget all about them." # @t_slolo129.02 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "That doesn’t happen every time, though... does it?" # @t_slolo130.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Yes. It does." # @t_slolo131.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_cousin "(Yikes! She seems pretty sure about that... I won’t argue." # @t_slolo132.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It doesn’t seem like she’s saying stuff like this just to be cool though..." # @t_slolo133.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I think something must have happened to her." # @t_slolo133.01 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "She seems so cute and innocent..." # @t_slolo134.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s strange her attitude would be like this." # @t_slolo134.01 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But maybe that’s just my own assumptions.)" # @t_slolo135.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_trio_preps as students:
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear 0.5 xpos 1.5 
    extend "{w=0.5}{nw}"
    t_ch_student1 "Hey, Lolo! [slot_playerName]!" # @t_slolo136.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.33 xpos 0.3 
    show i_trio_preps as students:
        # ShowWithAtl
        linear 0.33 xpos 0.7 
    show i_cousin_exhausted_sad as cousin:
        # ShowWithAtl
        linear 0.33 xpos 0.15 
    $ renpy.pause(0.33) # TimedPause
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Are you both working hard on Yearbook business?" # @t_slolo136.01 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Yikes! I got caught off guard!" # @t_slolo137.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What do I say?!)" # @t_slolo137.01 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Uh, yeah, totally." # @t_slolo138.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "We’re, like... brainstorming the best places for, uh..." # @t_slolo139.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "Casual photo ops and stuff like that." # @t_slolo140.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student2 "Omygosh! That sounds SO CUTE! <3" # @t_slolo141.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student3 "Good work, guys! We’ll leave you to it then!" # @t_slolo142.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_frustrated as lolo:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.333 xpos 0.7 
    show i_trio_preps as students:
        # ShowWithAtl
        linear 0.333 xpos 1.5 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    $ renpy.pause(0.333) # TimedPause
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha... nice save." # @t_slolo143.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Yeah..." # @t_slolo144.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Uhh... sorry for unloading on you like that." # @t_slolo145.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    extend " I mean, before the sunshine squad busted in on us." # @t_slolo145.01 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Huh? Oh, no..." # @t_slolo146.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s okay." # @t_slolo146.01 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Yeah. I guess it doesn’t matter anyway." # @t_slolo147.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s just that I haven’t really talked to anyone in a while." # @t_slolo147.01 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Really?" # @t_slolo148.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " I’d have guessed a girl like you would be swarming in friends." # @t_slolo148.01 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "Heh." # @t_slolo149.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Trying to flatter me, eh...?" # @t_slolo149.01 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " You’re all the same..." # @t_slolo149.02 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I see what you’re after." # @t_slolo149.03 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "O-oh!" # @t_slolo150.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Wh-what!" # @t_slolo150.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " N-no, I’m- Not like that-" # @t_slolo150.02 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "You heard about my priestess powers, right?" # @t_slolo151.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Well, you’re outta luck." # @t_slolo151.01 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m not that girl anymore." # @t_slolo151.02 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "‘Sides, I was always pretty terrible at that stuff, even when I was trying." # @t_slolo152.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "Priestess powers...?" # @t_slolo153.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Yeah, it was like magic stuff." # @t_slolo154.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Not really a big deal…" # @t_slolo154.01 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Klonoa always acted like it was, but whatever." # @t_slolo155.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Klonoa?" # @t_slolo156.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Who was that? A friend of yours?" # @t_slolo157.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "…" # @t_slolo158.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "…" # @t_slolo159.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_grin as lolo
    extend " Yeah right..." # @t_slolo159.01 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I haven’t thought about him in forever." # @t_slolo160.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(Uh oh... Looks like I hit a bullseye without meaning to." # @t_slolo161.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That Klonoa person from her past..." # @t_slolo162.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Could he have something to do with why she’s like this now?)" # @t_slolo163.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "…" # @t_slolo164.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh..." # @t_slolo165.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    extend " Was he your boyfriend, or something?" # @t_slolo165.01 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "..Heh." # @t_slolo166.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Not really..." # @t_slolo166.01 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "I’m way too ugly to have a boyfriend." # @t_slolo167.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Whaaaa?" # @t_slolo168.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What are you talking about?" # @t_slolo168.01 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’re joking, right?" # @t_slolo168.02 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "You don’t have to pretend to be all shocked." # @t_slolo169.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m not being down on myself." # @t_slolo169.01 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just being realistic." # @t_slolo169.02 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Lolo, I’m not pretending!" # @t_slolo170.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s nothing ugly about you!" # @t_slolo170.01 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Maybe you can’t see it... because you’re such a pollyanna." # @t_slolo171.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But if I pointed it out to you, you’d see..." # @t_slolo171.01 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Nobody’d be interested in me because of it." # @t_slolo172.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_raisedbrow as lolo
    extend " It doesn’t bother me, though." # @t_slolo172.01 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m used to it." # @t_slolo172.02 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "..." # @t_slolo173.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (What could she possibly be talking about?" # @t_slolo173.01 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " Her tail, maybe?" # @t_slolo173.02 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Maybe she has some scar or something..." # @t_slolo174.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I better not guess at it." # @t_slolo175.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If I guessed the wrong thing, I’d hurt her feelings." # @t_slolo175.01 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "She seems pretty sensitive, after all..." # @t_slolo176.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "Haha. I bet she’d try to kick my butt if she knew I was thinking that.)" # @t_slolo177.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "… What are you smiling about?" # @t_slolo178.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha... nothing." # @t_slolo179.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I just like hanging out with you I guess." # @t_slolo179.01 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_melancholy as lolo
    t_ch_lolo "Hmf. You’re pretty weird." # @t_slolo180.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_melancholy_blush as lolo
    with Dissolve(0.5)
    extend " Not that what I think matters or anything." # @t_slolo180.01 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_slolo181.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "[slot_playerName]... now that we’re talking..." # @t_slolo182.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Do you ever feel sometimes like..." # @t_slolo182.01 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Like nothing matters?" # @t_slolo183.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Like you can’t bring yourself to care?" # @t_slolo184.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " No matter how nice people are?" # @t_slolo184.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " No matter how close to them you think you’ve become?" # @t_slolo184.02 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_frustrated_blush as lolo
    t_ch_lolo "Do you feel like there’s always a gulf there..." # @t_slolo185.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That will never close, no matter what you do?" # @t_slolo185.01 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I... I think that’s going a little far." # @t_slolo186.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I guess I feel that way sometimes, but definitely not all the time." # @t_slolo187.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And I’ve never felt like I could never care at all about other people." # @t_slolo187.01 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I’m sorry..." # @t_slolo188.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I wish I could relate." # @t_slolo188.01 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But I don’t want to lie." # @t_slolo188.02 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "… Heh. Okay." # @t_slolo189.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just more proof, I guess." # @t_slolo189.01 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That I’m..." # @t_slolo189.02 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "That you’re..." # @t_slolo190.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What?" # @t_slolo190.01 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "...Nevermind." # @t_slolo191.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Looks like this dumb club is finally almost done, anyway." # @t_slolo192.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Wait, Lolo!" # @t_slolo193.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If this Klonoa person..." # @t_slolo193.01 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If he ever said anything mean to you..." # @t_slolo194.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " Ever made you feel bad about yourself or feel like you don’t matter-" # @t_slolo194.01 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_raisedbrow as lolo
    t_ch_lolo "Shut up!" # @t_slolo195.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "It wasn’t like that. You don’t get it..." # @t_slolo196.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You don’t get me, either." # @t_slolo196.01 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean, I don’t blame you..." # @t_slolo196.02 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "But you really don’t get it." # @t_slolo197.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I... I’m sorry if I overstepped my bounds." # @t_slolo198.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But if you ever need to talk..." # @t_slolo199.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " I’m here, okay?" # @t_slolo199.01 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "…" # @t_slolo1100.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_grin as lolo
    extend " You’re a weird person, [slot_playerName]..." # @t_slolo1100.01 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or a weird katamari-thing, anyway." # @t_slolo1100.02 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I don’t think I really get you, either." # @t_slolo1101.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Is that all she’s going to say about it?)" # @t_slolo1102.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.33 xpos 0.15 
    show i_lolo_crossed_frustrated as lolo:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.33 xpos 0.3 
    show i_trio_preps as students:
        # ShowWithAtl
        linear 0.33 xpos 0.7 
    $ renpy.pause(0.33) # TimedPause
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student1 "Whoops, there’s the bell, guys!" # @t_slolo1103.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student2 "Great job, everyone! See you tomorrow! Let’s have another great day!" # @t_slolo1104.00 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student3 "Keep on making great Namco High memories!" # @t_slolo1105.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_frustrated as lolo:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.333 xpos 0.7 
    show i_trio_preps as students:
        # ShowWithAtl
        linear 0.333 xpos 1.5 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    $ renpy.pause(0.333) # TimedPause
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_shrug_grin as lolo
    show i_cousin_default_grin as cousin
    t_ch_lolo "Heh. Saved by the bell, huh?" # @t_slolo1106.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Finally." # @t_slolo1106.01 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_shrug_frustrated as lolo
    extend " Ugh, I hope they won’t make us pose for any dumb pictures or anything when this is all over." # @t_slolo1106.02 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "U-uh..." # @t_slolo1107.00 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Well, now that club's over..." # @t_slolo1107.01 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Want to grab something to eat?" # @t_slolo1108.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    with Dissolve(0.5)
    extend " W-with me, I mean..." # @t_slolo1108.01 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "...Heh." # @t_slolo1109.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    extend " [slot_playerName], you seem pretty nice." # @t_slolo1109.01 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "So, someone like you..." # @t_slolo1110.00 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    show i_cousin_energetic_neutral as cousin
    extend " I’m just going to end up disappointing you." # @t_slolo1110.01 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Not that it really matters in the end, but..." # @t_slolo1110.02 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    show i_cousin_default_neutral as cousin
    t_ch_lolo "What I’m trying to say is, don’t get yourself all wound up over me." # @t_slolo1111.00 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "See you later, I guess." # @t_slolo1112.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.5 
    extend "{w=0.333}{nw}"
    t_ch_cousin "(Shoot. She’s gone." # @t_slolo1113.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That innocent-looking girl... she used to be a magic priestess and go on adventures..." # @t_slolo1114.00 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But now, it seems like all her interest in life is gone." # @t_slolo1114.01 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Something bad must have happened to her, I know it." # @t_slolo1115.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But what?" # @t_slolo1115.01 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "She acts like she doesn’t care, but... she definitely opened up to me today." # @t_slolo1116.00 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Maybe if I just stick around, she’ll be happy.)" # @t_slolo1117.00 self.block='Last'
    # <NHSceneChange {'name': '_3F', 'scene': 's_day2'} NHSceneChange ''>
    label s_lolo1__3F:
        # <NHSceneChange {'name': '_3F', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2