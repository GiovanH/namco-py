# <Scene {'id': 's_bluemax1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_bluemax1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_bluemax1"
    $ renpy.pause(1)
    # <Scene {'id': 's_bluemax1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/school.ogg" loop
    show i_bg_classroom_a as bg zorder 0 at default
    show i_trio_ballers as students:
        default
        alpha 0.0
        xpos 0.75 
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_taira_steveholt_happy as taira zorder 2:
        default
        xpos 0.5 
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.25 
    show i_bluemax_stand_serious as bluemax zorder 2:
        default
        xpos 0.75 
    show i_digdug_left as digdug zorder 2:
        default
        xpos 0.8 
        alpha 0.0
    show i_king_confident as king zorder 1:
        default
        xpos 0.8 
        xzoom -1.0 
        alpha 0.0
    t_ch_cousin "(It’s a little past “noon hundred.” Hope I’m not too late!)" # @t_sbluemax138.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Acting president Blue Max, please call to order today’s meeting of the official Namco High Military History Club!" # @t_sbluemax139.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Ack! Hope I haven’t missed too much!)" # @t_sbluemax140.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "Thank you, Secretary Blue Max. I hereby call this meeting to order. Acting President Blue Max recognizes Treasurer Blue Max." # @t_sbluemax141.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_serious as bluemax
    extend " Thank you, Acting President Blue Max. I’d like to begin with the budgetary committee report commission survey." # @t_sbluemax141.01 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What the…?!)" # @t_sbluemax142.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Is Max talking to himself?)" # @t_sbluemax143.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax:
        linear .2 xzoom -1.0 
    t_ch_max "The numbers are in. There’s only one way to raise the neccessary funds to see SECRET PROJECT SUPER PLANE come to fruition." # @t_sbluemax144.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "A bake sale." # @t_sbluemax145.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Um. Hello?" # @t_sbluemax146.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax:
        linear .2 xzoom 1.0 
    t_ch_max "Please save your applause for the end." # @t_sbluemax147.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Now, it is the opinion of the Treasury department that cookies would provide the club with the most favorable flavor to cost to profit ratios." # @t_sbluemax148.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Max?" # @t_sbluemax149.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "I cannot present this report survey commission to the committee if I am to be interrupted! I was promised three minutes of floor time." # @t_sbluemax150.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I, Acting President Blue Max, hereby call to recess the Military History Club pending review of new member protocols." # @t_sbluemax151.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax:
        linear .2 xzoom -1.0 
    t_ch_max "The Treasury objects to this course of action!" # @t_sbluemax152.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_shocked as bluemax:
        linear .2 xzoom 1.0 
    t_ch_max "TREASURER, YOU WILL STEP DOOOOOWN!" # @t_sbluemax153.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Hey, [slot_playerName]! I was starting to think you wouldn’t show up!" # @t_sbluemax154.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Did I…" # @t_sbluemax155.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What just happened?" # @t_sbluemax156.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Oh, you conducted a serious breach of club etiquette, but don’t worry." # @t_sbluemax157.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I’m the club’s Acting President, Vice President, Treasurer, Adjutant, Viceroy, Ambassador, Minority Whip, Secretary of State, and Grand Royal Chancellor." # @t_sbluemax158.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_smile as bluemax
    t_ch_max "So, I can probably pull a few favors and still secure a solid 5 to 4 majority vote to get you into the club." # @t_sbluemax159.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(That sounds like a close shave…)" # @t_sbluemax160.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Wait, if you’re doing everything else, then why are you only the Acting President?" # @t_sbluemax160.01 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Oh, Aki Matsuo is club president, but she’s never around!" # @t_sbluemax161.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I step in and keep the club moving in her absence." # @t_sbluemax162.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Sounds like you’ve got a lot of responsibilities around here. Is there anything left for me to do?" # @t_sbluemax163.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_smile as bluemax
    t_ch_max "Of course! You can be the guy who records the minutes of every meeting." # @t_sbluemax164.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Hrmmm." # @t_sbluemax165.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (That sounds kind of boring, but what the heck, I like helping.)" # @t_sbluemax165.01 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " Sure." # @t_sbluemax165.02 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Okay. Just be sure to record the name of everyone who speaks." # @t_sbluemax166.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh, but aren’t you and I the only people here?" # @t_sbluemax167.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Yeah! So, it should be super easy for you, right?" # @t_sbluemax168.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Hm, yeah. Good point!" # @t_sbluemax169.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "As Acting President, I hereby bring this meeting back to a state of order." # @t_sbluemax170.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_serious as bluemax
    t_ch_max "[slot_playerName]!" # @t_sbluemax171.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "You’re not writing!" # @t_sbluemax172.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Oh, right!" # @t_sbluemax173.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Sorry!" # @t_sbluemax174.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Ahem." # @t_sbluemax175.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Director of the Treasury Blue Max please continue regarding the previous motion concerning revenue shortfalls i.e. funding, re: the SECRET PROJECT SUPER PLANE." # @t_sbluemax176.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax:
        linear .2 xzoom -1.0 
    t_ch_max "Yes, thank you Acting President Blue Max." # @t_sbluemax177.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Uh, I’m already a little confused?)" # @t_sbluemax178.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "You’ll note in Section 4 of the report--" # @t_sbluemax179.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax:
        linear .2 xzoom 1.0 
    t_ch_max "Oh, [slot_playerName], I didn’t bring enough for everyone. You’ll have to share." # @t_sbluemax180.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Okay. Should I write that part?" # @t_sbluemax181.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Yes. And that part." # @t_sbluemax182.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "And this part." # @t_sbluemax183.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Those parts too?" # @t_sbluemax184.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "And this!" # @t_sbluemax185.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "Okay, so Section 4 details potential cookie varieties via cost analysis, time table of deliverables, sales projections using the previous quarter’s national and local sales as a baseline cross-referenced with demographics." # @t_sbluemax186.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Chocolate chip is the clear leader." # @t_sbluemax187.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Uh, I got most of that…?)" # @t_sbluemax188.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(This is awfully complicated for a report to himself!)" # @t_sbluemax189.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Max, what is all this stuff about anyway?" # @t_sbluemax189.01 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Tsk. Can’t you see the Treasury still has the floor, [slot_playerName]!" # @t_sbluemax190.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh." # @t_sbluemax191.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Um." # @t_sbluemax192.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "No?" # @t_sbluemax193.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Hmmm." # @t_sbluemax194.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "That’s a good point." # @t_sbluemax195.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_serious as bluemax
    t_ch_max "This was much easier to keep track of when it was just me and the potential of Aki to maybe make it to a single club meeting." # @t_sbluemax196.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Maybe we should designate a committee to staff a commission to draft a report on a survey of board members to cost analyze expenditures for a different hat for each club position…" # @t_sbluemax197.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Should I still be writing these parts down?" # @t_sbluemax198.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Probably, yeah." # @t_sbluemax199.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "But, that’s okay! Because everything related to SECRET PROJECT SUPER PLANE ought to be kept off the record anyway." # @t_sbluemax1100.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Strictly “black ops” y’know." # @t_sbluemax1101.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Not really!)" # @t_sbluemax1102.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Sure, yeah." # @t_sbluemax1102.01 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Except you were talking about hats and not the secret project." # @t_sbluemax1103.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Ha! That’s an old accounting trick, [slot_playerName]." # @t_sbluemax1104.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "SECRET PROJECT SUPER PLANE is funded by the discretionary budget. There’s no real oversight, so all kinds of crazy unrelated programs can be funded through it using earmarks." # @t_sbluemax1105.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What’s an earmark?" # @t_sbluemax1106.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Uh, it’s uh." # @t_sbluemax1107.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Complicated." # @t_sbluemax1108.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Oh." # @t_sbluemax1109.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah, it sounds like it would be." # @t_sbluemax1110.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "So, you’re working on some kind of super plane then?" # @t_sbluemax1111.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_shocked as bluemax
    t_ch_max "WHO TOLD YOU???" # @t_sbluemax1112.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Gosh, Max sure is high strung!)" # @t_sbluemax1113.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(It’s like he’s got a lot of energy bubbling right under the surface and waiting to burst out.)" # @t_sbluemax1114.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(Uh, that sounds like it could get messy. But I mean it in a good way!)" # @t_sbluemax1115.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Um, it’s called “secret project super plane.”" # @t_sbluemax1115.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Mmhmm, yes, go on." # @t_sbluemax1116.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Uh.)" # @t_sbluemax1117.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Okaaaay." # @t_sbluemax1117.01 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And then I took a wild guess?" # @t_sbluemax1118.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Like, maybe, the SECRET PROJECT had something to do with a SUPER PLANE." # @t_sbluemax1119.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Hrm." # @t_sbluemax1120.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Yeah. Okay." # @t_sbluemax1121.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Your story checks out." # @t_sbluemax1122.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(It’s kind of sad that no one else is in his club. I’ve been here for five minutes and it’s crazy obvious how important this stuff is to him.)" # @t_sbluemax1123.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But he’s got no one to share it with!)" # @t_sbluemax1124.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hmm! Maybe that’s why he’s giving me so much leeway with the protocols.)" # @t_sbluemax1125.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Uh, and I guess the industrial espionage I just accidentally did?)" # @t_sbluemax1126.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_shock as bluemax
    t_ch_max "Oh!" # @t_sbluemax1127.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "We better get moving anyway." # @t_sbluemax1128.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Why’s that?" # @t_sbluemax1129.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Um. No reason!" # @t_sbluemax1130.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Except…" # @t_sbluemax1131.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "It’s super important that we do it real soon though!" # @t_sbluemax1132.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Okay. Something’s sure bugging him. I’ll go along with it for now.)" # @t_sbluemax1133.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Yeah, okay, Max. Lead the way." # @t_sbluemax1133.01 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Too late!" # @t_sbluemax1134.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_shock as bluemax
    t_ch_max "I mean HIDE!" # @t_sbluemax1135.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Under the table?" # @t_sbluemax1136.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax
    t_ch_max "Hide, then ask!" # @t_sbluemax1137.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        pause 0.33 
        linear .5 ypos 1.0 
    extend "{w=0.8300000000000001}{nw}"
    t_ch_max "But then DON’T ASK because we have to be quiet!" # @t_sbluemax1138.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Okay…)" # @t_sbluemax1139.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        pause 0.33 
        linear .5 ypos 1.0 
    extend "{w=0.8300000000000001}{nw}"
    t_ch_cousin "(It’s not like it’s hard to get under the table.)" # @t_sbluemax1140.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Is this a security measure for talking about the secret project?" # @t_sbluemax1140.01 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "SHHHHHH!" # @t_sbluemax1141.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean, shhhhh." # @t_sbluemax1141.01 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira:
        # ShowWithAtl
        linear .33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_taira "Huh. Coulda sworn Blue DORK would be in here." # @t_sbluemax1142.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "NERDING IT UP." # @t_sbluemax1143.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_trio_ballers as students:
        # ShowWithAtl
        pause 0.2 
        linear .2 alpha 1.0
    show i_taira_steveholt_happy as taira:
        # ShowWithAtl
        ease_expo .2 xpos 0.25 
        # ShowWithAtl
        ease_expo .2 xpos 0.25 
    extend "{w=0.4}{nw}"
    t_ch_bullies "Don’t you mean DORKING IT UP?" # @t_sbluemax1144.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_serious as taira
    t_ch_taira "Nah, I gave it mad thought." # @t_sbluemax1145.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "Do tell." # @t_sbluemax1146.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "He’s a dork who does nerdy things." # @t_sbluemax1147.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "*mumble confer discuss*" # @t_sbluemax1148.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Hey, yeah!" # @t_sbluemax1148.01 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "That’s good thinkin’!" # @t_sbluemax1149.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Yeah, I thought so too." # @t_sbluemax1150.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "Maybe we’re early." # @t_sbluemax1151.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Could be." # @t_sbluemax1152.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "My watch just says REVENGE on it." # @t_sbluemax1153.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Okay, they get a few minutes BUT THAT’S IT." # @t_sbluemax1154.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "We can’t miss Wrestleball practice." # @t_sbluemax1155.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "Let’s sit at a table while we wait." # @t_sbluemax1156.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Oh no!" # @t_sbluemax1157.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "Yeah, sitting while you wait rules!  We should do that!" # @t_sbluemax1158.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Let’s pick a table completely at random." # @t_sbluemax1159.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_shock as bluemax
    t_ch_max "please no please no please no" # @t_sbluemax1160.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Poor Max. He’s shaking!)" # @t_sbluemax1161.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "How about this table here?" # @t_sbluemax1162.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "The one with the TOTALLY MYSTERIOUS rattling chair!" # @t_sbluemax1163.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        pause 0.5 
        linear .2 ypos 0.5 
    extend "{w=0.7}{nw}"
    extend " OH HEY THERE BLUE DORK!" # @t_sbluemax1163.01 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Ahh, put me down!" # @t_sbluemax1164.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "HAW HAW!" # @t_sbluemax1165.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Sure thing, buddy." # @t_sbluemax1166.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "But you know the drill. First we gotta revenge you around some." # @t_sbluemax1167.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(No wonder Max is so worried all the time!)" # @t_sbluemax1168.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(He gets pushed around by these big kids every day!)" # @t_sbluemax1169.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(AND THAT’S NOT RIGHT!)" # @t_sbluemax1170.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_angry as cousin:
        linear .2 xzoom -1.0 
        # ShowWithAtl
        linear .2 xpos 0.5 
        linear .2 ypos 0.5 
    extend "{w=0.4}{nw}"
    extend " Hey! That’s enough!" # @t_sbluemax1170.01 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "You hear somethin’, Taira?" # @t_sbluemax1171.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I sure do." # @t_sbluemax1172.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_angry as taira
    t_ch_taira "AND IT’S CALLED NOTHIN’!" # @t_sbluemax1173.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "HAW HAW!" # @t_sbluemax1174.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "Good one, Captain." # @t_sbluemax1175.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_happy as taira
    t_ch_taira "Aww, you guys." # @t_sbluemax1176.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    t_ch_cousin "I SAID that’s enough!" # @t_sbluemax1177.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_shock as bluemax
    t_ch_max "No! Save yourself, [slot_playerName]!" # @t_sbluemax1178.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "It’s just lunch money!" # @t_sbluemax1179.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_angry as taira
    t_ch_taira "Yo, it’s not JUST lunch money." # @t_sbluemax1180.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "You keep makin’ me look dumb by turning in all your homework on time!" # @t_sbluemax1181.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "But I don’t do my homework!" # @t_sbluemax1182.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "It’s filled up with doodles and schematics but definitely not anything secret or aeronautical!" # @t_sbluemax1183.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_serious as taira
    t_ch_taira "Still though." # @t_sbluemax1184.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "If you’d just turn in nothin’ at all like a normal dumb kid, then it wouldn’t look so bad when I turn in nothin’ at all!" # @t_sbluemax1185.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "And then maybe I wouldn’t be stuck in detention." # @t_sbluemax1186.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "So, I gotta do a revenge on ya." # @t_sbluemax1187.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Until you learn. Or until revenge stops being awesome." # @t_sbluemax1188.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "WHICH IS NEVER!" # @t_sbluemax1189.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Leave him alone!" # @t_sbluemax1190.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "Uh-oh, now you done it, Captain." # @t_sbluemax1191.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "The shrimp is mad at ya." # @t_sbluemax1192.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_happy as taira
    t_ch_taira "Yeah, but the shrimp’s pretty cute. We gotta whole “will they, won’t they” thing going." # @t_sbluemax1193.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Whaaaaa?)" # @t_sbluemax1194.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Anyway, what’cha gonna do? SHORT ME TO DEATH?" # @t_sbluemax1195.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "HAW HAW! Good one!" # @t_sbluemax1196.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wait. That wasn’t a good one.)" # @t_sbluemax1197.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(That wasn’t a good one at all!)" # @t_sbluemax1198.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " We do NOT have a “will they, won’t they” thing. It’s just they won’t, uh, they." # @t_sbluemax1198.01 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So, why don’t you guys BUZZ OFF!" # @t_sbluemax1198.02 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Whoa, that sounded pretty tough.)" # @t_sbluemax1198.03 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Guess I’m upset!)" # @t_sbluemax1199.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Oh? Who’s gonna make us?" # @t_sbluemax1200.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "YOU, New Dork?" # @t_sbluemax1201.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Taira’s really a one trick pony with his insult repertoire!)" # @t_sbluemax1202.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    extend " Maybe I will!" # @t_sbluemax1202.01 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " (Um, now I’m just saying crazy things!)" # @t_sbluemax1202.02 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(There’s no way I could stop any of these guys, much less ALL OF THEM!)" # @t_sbluemax1203.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Not without my katamari anyway…)" # @t_sbluemax1204.00 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "You? Yeah, I don’t think so, Shorty." # @t_sbluemax1205.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar1.ogg"
    t_ch_king "ROOOAAAR!!!" # @t_sbluemax1206.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    show i_trio_ballers as students:
        # ShowWithAtl
        ease_expo .3 xpos 1.49 
    extend "{w=0.3}{nw}"
    t_ch_bullies "!!!" # @t_sbluemax1207.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin:
        linear .2 xzoom 1.0 
        # ShowWithAtl
        linear .2 xpos 0.25 
    extend "{w=0.2}{nw}"
    t_ch_cousin "!!!" # @t_sbluemax1208.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_confused as taira:
        # ShowWithAtl
        ease_expo .2 xpos 0.13 
    extend "{w=0.2}{nw}"
    t_ch_taira "!!!" # @t_sbluemax1209.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax:
        linear .2 xzoom -1.0 
        # ShowWithAtl
        linear .2 xpos 0.45 
    extend "{w=0.2}{nw}"
    t_ch_max "Oh, thank goodness." # @t_sbluemax1210.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king:
        # ShowWithAtl
        linear .33 alpha 1.0
    show i_digdug_left as digdug:
        # ShowWithAtl
        pause 1.0 
        linear .33 alpha 1.0
    extend "{w=1.33}{nw}"
    t_ch_digdug "Now, we don’t have time to determine who’s bullying who." # @t_sbluemax1211.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Even though that would take less time for me to figure out than explaining how we don’t have the time to figure it out." # @t_sbluemax1212.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "We was just playin’ around." # @t_sbluemax1213.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Weren’t we, Max?" # @t_sbluemax1214.00 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Okay, yeah, sure." # @t_sbluemax1215.00 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "Oh, so, what? Revenge is just a GAME to you, bro?" # @t_sbluemax1216.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "B-b-but you said…!!!" # @t_sbluemax1217.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar2.ogg"
    show i_king_screaming as king
    t_ch_king "ROAR!" # @t_sbluemax1218.00 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Yes, good thinking, King. We will not sentence anyone here to additional detention." # @t_sbluemax1219.00 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "ON THE SINGULAR CONDITION THAT ALL OF YOU BREAK IT UP IMMEDIATELY!!!" # @t_sbluemax1220.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Taira, get to Wrestleball practice." # @t_sbluemax1221.00 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Max, go build a model plane or something." # @t_sbluemax1222.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_digdug "[slot_playerName], I don’t know your thing yet, but go and do it quietly." # @t_sbluemax1223.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Bullies, you have like no lines of dialog, no one cares about you, just scram." # @t_sbluemax1224.00 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Yeah, I’m leavin’." # @t_sbluemax1225.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "But not before I threaten the dorks with an otherwise benign phrase like, “See you LATER.”" # @t_sbluemax1226.00 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "But, for [slot_playerName], it could also be like a kinda TOTALLY sexy “see you later” if you play your cards right." # @t_sbluemax1227.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Yes, yes. Very good. Just get moving." # @t_sbluemax1228.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira:
        # ShowWithAtl
        linear .33 xpos -0.5 
    show i_king_screaming as king:
        # ShowWithAtl
        pause 0.33 
        linear .33 xpos 1.5 
    show i_digdug_left as digdug:
        # ShowWithAtl
        pause 0.66 
        linear .33 xpos 1.5 
    $ renpy.pause(0.99) # TimedPause
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax:
        # ShowWithAtl
        linear .2 xpos 0.75 
        linear .2 xzoom 1.0 
    extend "{w=0.2}{nw}"
    t_ch_max "Whew. They’re gone." # @t_sbluemax1229.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m glad they left us alone, but I wish Principal Dig Dug had been a little more thorough about his investigation and punishment." # @t_sbluemax1230.00 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Or done either of those things at all!" # @t_sbluemax1231.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Yeah, that would’ve been good too." # @t_sbluemax1232.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Um." # @t_sbluemax1233.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Does that happen every day?" # @t_sbluemax1234.00 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "No. Not every day." # @t_sbluemax1235.00 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "They hardly ever bother me on the weekend…" # @t_sbluemax1236.00 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    extend " But it’s okay! Because I’ve got the SECRET PROJECT SUPER PLANE!" # @t_sbluemax1236.01 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "And when it’s done no one will be able to push me anymore!" # @t_sbluemax1237.00 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Um, not because of violent war plane revenge, right?" # @t_sbluemax1238.00 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Of course not, that’s crazy." # @t_sbluemax1239.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "They won’t be able to push me around because I’ll be FLYING." # @t_sbluemax1240.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But...Max is a bird.)" # @t_sbluemax1241.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Shouldn’t he be able to fly by himself?)" # @t_sbluemax1242.00 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Well, I mean, not all the time though." # @t_sbluemax1242.01 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Right? Like, you’d need to refuel and use the bathroom and sleep and stuff." # @t_sbluemax1243.00 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_worried as bluemax
    t_ch_max "Well." # @t_sbluemax1244.00 self.block='Last'
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Uh." # @t_sbluemax1245.00 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "There’d be. Um." # @t_sbluemax1246.00 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Huh." # @t_sbluemax1247.00 self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Oh wow, look at the time. Military History Club is over." # @t_sbluemax1248.00 self.block='Last'
    # <ParallelEvent {'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh…" # @t_sbluemax1249.00 self.block='Last'
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Was it something I said?)" # @t_sbluemax1249.01 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "But, um…" # @t_sbluemax1250.00 self.block='Last'
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I just wanted to say." # @t_sbluemax1251.00 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Y’know." # @t_sbluemax1252.00 self.block='Last'
    # <ParallelEvent {'name': '_3q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax
    t_ch_max "Thank you. For earlier. With Taira and them." # @t_sbluemax1253.00 self.block='Last'
    # <ParallelEvent {'name': '_3r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Don’t mention it." # @t_sbluemax1254.00 self.block='Last'
    # <ParallelEvent {'name': '_3s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "It’s just that, um." # @t_sbluemax1255.00 self.block='Last'
    # <ParallelEvent {'name': '_3t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_flustered as bluemax
    t_ch_max "No one’s ever…" # @t_sbluemax1256.00 self.block='Last'
    # <ParallelEvent {'name': '_3u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "??" # @t_sbluemax1257.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_3v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_flustered as bluemax:
        # ShowWithAtl
        pause 0.7 
        linear .33 alpha 0.0
    extend "{w=1.03}{nw}"
    t_ch_max "Bye, [slot_playerName]!" # @t_sbluemax1258.00 self.block='Last'
    # <ParallelEvent {'name': '_3w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_sbluemax1259.00 self.block='Last'
    # <ParallelEvent {'name': '_3x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Bye, Max." # @t_sbluemax1260.00 self.block='Last'
    # <ParallelEvent {'name': '_3y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " (Look at him.)" # @t_sbluemax1260.01 self.block='Last'
    # <ParallelEvent {'name': '_3z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Even just walking down the halls, he keeps checking over his shoulder.)" # @t_sbluemax1261.00 self.block='Last'
    # <ParallelEvent {'name': '_40'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(He’s very, hmmm...)" # @t_sbluemax1262.00 self.block='Last'
    # <ParallelEvent {'name': '_41'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Well, shy. And nervous.)" # @t_sbluemax1263.00 self.block='Last'
    # <ParallelEvent {'name': '_42'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But also sincere!)" # @t_sbluemax1264.00 self.block='Last'
    # <ParallelEvent {'name': '_43'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(It’s a shame he has it so rough. And he keeps it all bottled up.)" # @t_sbluemax1265.00 self.block='Last'
    # <ParallelEvent {'name': '_44'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Maybe he just needs someone to help him break out of his shell so everyone else can see the sweet kid he really is.)" # @t_sbluemax1266.00 self.block='Last'
    # <NHSceneChange {'name': '_45', 'scene': 's_day2'} NHSceneChange ''>
    label s_bluemax1__45:
        # <NHSceneChange {'name': '_45', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2