# <Scene scene {'id': 's_bluemax1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_bluemax1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_bluemax1"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_bluemax1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
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
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Acting president Blue Max, please call to order today’s meeting of the official Namco High Military History Club!" # @t_sbluemax139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Ack! Hope I haven’t missed too much!)" # @t_sbluemax140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "Thank you, Secretary Blue Max. I hereby call this meeting to order. Acting President Blue Max recognizes Treasurer Blue Max." # @t_sbluemax141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stop_serious as bluemax
    extend " Thank you, Acting President Blue Max. I’d like to begin with the budgetary committee report commission survey." # @t_sbluemax141.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(What the…?!)" # @t_sbluemax142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Is Max talking to himself?)" # @t_sbluemax143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_serious as bluemax:
        linear .2 xzoom -1.0 
    t_ch_max "The numbers are in. There’s only one way to raise the neccessary funds to see SECRET PROJECT SUPER PLANE come to fruition." # @t_sbluemax144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "A bake sale." # @t_sbluemax145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Um. Hello?" # @t_sbluemax146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_serious as bluemax:
        linear .2 xzoom 1.0 
    t_ch_max "Please save your applause for the end." # @t_sbluemax147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Now, it is the opinion of the Treasury department that cookies would provide the club with the most favorable flavor to cost to profit ratios." # @t_sbluemax148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Max?" # @t_sbluemax149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "I cannot present this report survey commission to the committee if I am to be interrupted! I was promised three minutes of floor time." # @t_sbluemax150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "I, Acting President Blue Max, hereby call to recess the Military History Club pending review of new member protocols." # @t_sbluemax151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_shock_serious as bluemax:
        linear .2 xzoom -1.0 
    t_ch_max "The Treasury objects to this course of action!" # @t_sbluemax152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_shock_shocked as bluemax:
        linear .2 xzoom 1.0 
    t_ch_max "TREASURER, YOU WILL STEP DOOOOOWN!" # @t_sbluemax153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Hey, [slot_playerName]! I was starting to think you wouldn’t show up!" # @t_sbluemax154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Did I…" # @t_sbluemax155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What just happened?" # @t_sbluemax156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Oh, you conducted a serious breach of club etiquette, but don’t worry." # @t_sbluemax157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "I’m the club’s Acting President, Vice President, Treasurer, Adjutant, Viceroy, Ambassador, Minority Whip, Secretary of State, and Grand Royal Chancellor." # @t_sbluemax158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stop_smile as bluemax
    t_ch_max "So, I can probably pull a few favors and still secure a solid 5 to 4 majority vote to get you into the club." # @t_sbluemax159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(That sounds like a close shave…)" # @t_sbluemax160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Wait, if you’re doing everything else, then why are you only the Acting President?" # @t_sbluemax160.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Oh, Aki Matsuo is club president, but she’s never around!" # @t_sbluemax161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "I step in and keep the club moving in her absence." # @t_sbluemax162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Sounds like you’ve got a lot of responsibilities around here. Is there anything left for me to do?" # @t_sbluemax163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_smile as bluemax
    t_ch_max "Of course! You can be the guy who records the minutes of every meeting." # @t_sbluemax164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Hrmmm." # @t_sbluemax165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (That sounds kind of boring, but what the heck, I like helping.)" # @t_sbluemax165.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " Sure." # @t_sbluemax165.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Okay. Just be sure to record the name of everyone who speaks." # @t_sbluemax166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh, but aren’t you and I the only people here?" # @t_sbluemax167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Yeah! So, it should be super easy for you, right?" # @t_sbluemax168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Hm, yeah. Good point!" # @t_sbluemax169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "As Acting President, I hereby bring this meeting back to a state of order." # @t_sbluemax170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stop_serious as bluemax
    t_ch_max "[slot_playerName]!" # @t_sbluemax171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "You’re not writing!" # @t_sbluemax172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Oh, right!" # @t_sbluemax173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Sorry!" # @t_sbluemax174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Ahem." # @t_sbluemax175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Director of the Treasury Blue Max please continue regarding the previous motion concerning revenue shortfalls i.e. funding, re: the SECRET PROJECT SUPER PLANE." # @t_sbluemax176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_serious as bluemax:
        linear .2 xzoom -1.0 
    t_ch_max "Yes, thank you Acting President Blue Max." # @t_sbluemax177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Uh, I’m already a little confused?)" # @t_sbluemax178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "You’ll note in Section 4 of the report--" # @t_sbluemax179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_serious as bluemax:
        linear .2 xzoom 1.0 
    t_ch_max "Oh, [slot_playerName], I didn’t bring enough for everyone. You’ll have to share." # @t_sbluemax180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Okay. Should I write that part?" # @t_sbluemax181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Yes. And that part." # @t_sbluemax182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "And this part." # @t_sbluemax183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Those parts too?" # @t_sbluemax184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "And this!" # @t_sbluemax185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "Okay, so Section 4 details potential cookie varieties via cost analysis, time table of deliverables, sales projections using the previous quarter’s national and local sales as a baseline cross-referenced with demographics." # @t_sbluemax186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Chocolate chip is the clear leader." # @t_sbluemax187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Uh, I got most of that…?)" # @t_sbluemax188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This is awfully complicated for a report to himself!)" # @t_sbluemax189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Max, what is all this stuff about anyway?" # @t_sbluemax189.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Tsk. Can’t you see the Treasury still has the floor, [slot_playerName]!" # @t_sbluemax190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh." # @t_sbluemax191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Um." # @t_sbluemax192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "No?" # @t_sbluemax193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Hmmm." # @t_sbluemax194.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "That’s a good point." # @t_sbluemax195.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_cower_serious as bluemax
    t_ch_max "This was much easier to keep track of when it was just me and the potential of Aki to maybe make it to a single club meeting." # @t_sbluemax196.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Maybe we should designate a committee to staff a commission to draft a report on a survey of board members to cost analyze expenditures for a different hat for each club position…" # @t_sbluemax197.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Should I still be writing these parts down?" # @t_sbluemax198.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Probably, yeah." # @t_sbluemax199.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "But, that’s okay! Because everything related to SECRET PROJECT SUPER PLANE ought to be kept off the record anyway." # @t_sbluemax1100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Strictly “black ops” y’know." # @t_sbluemax1101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Not really!)" # @t_sbluemax1102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Sure, yeah." # @t_sbluemax1102.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Except you were talking about hats and not the secret project." # @t_sbluemax1103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Ha! That’s an old accounting trick, [slot_playerName]." # @t_sbluemax1104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "SECRET PROJECT SUPER PLANE is funded by the discretionary budget. There’s no real oversight, so all kinds of crazy unrelated programs can be funded through it using earmarks." # @t_sbluemax1105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What’s an earmark?" # @t_sbluemax1106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Uh, it’s uh." # @t_sbluemax1107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Complicated." # @t_sbluemax1108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Oh." # @t_sbluemax1109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Yeah, it sounds like it would be." # @t_sbluemax1110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "So, you’re working on some kind of super plane then?" # @t_sbluemax1111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_shock_shocked as bluemax
    t_ch_max "WHO TOLD YOU???" # @t_sbluemax1112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Gosh, Max sure is high strung!)" # @t_sbluemax1113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It’s like he’s got a lot of energy bubbling right under the surface and waiting to burst out.)" # @t_sbluemax1114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(Uh, that sounds like it could get messy. But I mean it in a good way!)" # @t_sbluemax1115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Um, it’s called “secret project super plane.”" # @t_sbluemax1115.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Mmhmm, yes, go on." # @t_sbluemax1116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Uh.)" # @t_sbluemax1117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Okaaaay." # @t_sbluemax1117.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And then I took a wild guess?" # @t_sbluemax1118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Like, maybe, the SECRET PROJECT had something to do with a SUPER PLANE." # @t_sbluemax1119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Hrm." # @t_sbluemax1120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Yeah. Okay." # @t_sbluemax1121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Your story checks out." # @t_sbluemax1122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(It’s kind of sad that no one else is in his club. I’ve been here for five minutes and it’s crazy obvious how important this stuff is to him.)" # @t_sbluemax1123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(But he’s got no one to share it with!)" # @t_sbluemax1124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Hmm! Maybe that’s why he’s giving me so much leeway with the protocols.)" # @t_sbluemax1125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Uh, and I guess the industrial espionage I just accidentally did?)" # @t_sbluemax1126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_shock as bluemax
    t_ch_max "Oh!" # @t_sbluemax1127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "We better get moving anyway." # @t_sbluemax1128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Why’s that?" # @t_sbluemax1129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Um. No reason!" # @t_sbluemax1130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Except…" # @t_sbluemax1131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "It’s super important that we do it real soon though!" # @t_sbluemax1132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Okay. Something’s sure bugging him. I’ll go along with it for now.)" # @t_sbluemax1133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Yeah, okay, Max. Lead the way." # @t_sbluemax1133.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Too late!" # @t_sbluemax1134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_cower_shock as bluemax
    t_ch_max "I mean HIDE!" # @t_sbluemax1135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Under the table?" # @t_sbluemax1136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_cower_worried as bluemax
    t_ch_max "Hide, then ask!" # @t_sbluemax1137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        pause 0.33 
        linear .5 ypos 1.0 
    extend "{w=0.8300000000000001}{nw}"
    t_ch_max "But then DON’T ASK because we have to be quiet!" # @t_sbluemax1138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Okay…)" # @t_sbluemax1139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        pause 0.33 
        linear .5 ypos 1.0 
    extend "{w=0.8300000000000001}{nw}"
    t_ch_cousin "(It’s not like it’s hard to get under the table.)" # @t_sbluemax1140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Is this a security measure for talking about the secret project?" # @t_sbluemax1140.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "SHHHHHH!" # @t_sbluemax1141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I mean, shhhhh." # @t_sbluemax1141.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_steveholt_happy as taira:
        # ShowWithAtl
        linear .33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_taira "Huh. Coulda sworn Blue DORK would be in here." # @t_sbluemax1142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "NERDING IT UP." # @t_sbluemax1143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
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
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_serious as taira
    t_ch_taira "Nah, I gave it mad thought." # @t_sbluemax1145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "Do tell." # @t_sbluemax1146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "He’s a dork who does nerdy things." # @t_sbluemax1147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "*mumble confer discuss*" # @t_sbluemax1148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Hey, yeah!" # @t_sbluemax1148.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "That’s good thinkin’!" # @t_sbluemax1149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Yeah, I thought so too." # @t_sbluemax1150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "Maybe we’re early." # @t_sbluemax1151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Could be." # @t_sbluemax1152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "My watch just says REVENGE on it." # @t_sbluemax1153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Okay, they get a few minutes BUT THAT’S IT." # @t_sbluemax1154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "We can’t miss Wrestleball practice." # @t_sbluemax1155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "Let’s sit at a table while we wait." # @t_sbluemax1156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Oh no!" # @t_sbluemax1157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "Yeah, sitting while you wait rules!  We should do that!" # @t_sbluemax1158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Let’s pick a table completely at random." # @t_sbluemax1159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_cower_shock as bluemax
    t_ch_max "please no please no please no" # @t_sbluemax1160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Poor Max. He’s shaking!)" # @t_sbluemax1161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "How about this table here?" # @t_sbluemax1162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "The one with the TOTALLY MYSTERIOUS rattling chair!" # @t_sbluemax1163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        pause 0.5 
        linear .2 ypos 0.5 
    extend "{w=0.7}{nw}"
    extend " OH HEY THERE BLUE DORK!" # @t_sbluemax1163.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Ahh, put me down!" # @t_sbluemax1164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "HAW HAW!" # @t_sbluemax1165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Sure thing, buddy." # @t_sbluemax1166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "But you know the drill. First we gotta revenge you around some." # @t_sbluemax1167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(No wonder Max is so worried all the time!)" # @t_sbluemax1168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(He gets pushed around by these big kids every day!)" # @t_sbluemax1169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(AND THAT’S NOT RIGHT!)" # @t_sbluemax1170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_angry as cousin:
        linear .2 xzoom -1.0 
        # ShowWithAtl
        linear .2 xpos 0.5 
        linear .2 ypos 0.5 
    extend "{w=0.4}{nw}"
    extend " Hey! That’s enough!" # @t_sbluemax1170.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "You hear somethin’, Taira?" # @t_sbluemax1171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "I sure do." # @t_sbluemax1172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_angry as taira
    t_ch_taira "AND IT’S CALLED NOTHIN’!" # @t_sbluemax1173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "HAW HAW!" # @t_sbluemax1174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "Good one, Captain." # @t_sbluemax1175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_happy as taira
    t_ch_taira "Aww, you guys." # @t_sbluemax1176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_angry as cousin
    t_ch_cousin "I SAID that’s enough!" # @t_sbluemax1177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_shock as bluemax
    t_ch_max "No! Save yourself, [slot_playerName]!" # @t_sbluemax1178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "It’s just lunch money!" # @t_sbluemax1179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_angry as taira
    t_ch_taira "Yo, it’s not JUST lunch money." # @t_sbluemax1180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "You keep makin’ me look dumb by turning in all your homework on time!" # @t_sbluemax1181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "But I don’t do my homework!" # @t_sbluemax1182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "It’s filled up with doodles and schematics but definitely not anything secret or aeronautical!" # @t_sbluemax1183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_default_serious as taira
    t_ch_taira "Still though." # @t_sbluemax1184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "If you’d just turn in nothin’ at all like a normal dumb kid, then it wouldn’t look so bad when I turn in nothin’ at all!" # @t_sbluemax1185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "And then maybe I wouldn’t be stuck in detention." # @t_sbluemax1186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "So, I gotta do a revenge on ya." # @t_sbluemax1187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Until you learn. Or until revenge stops being awesome." # @t_sbluemax1188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "WHICH IS NEVER!" # @t_sbluemax1189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Leave him alone!" # @t_sbluemax1190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "Uh-oh, now you done it, Captain." # @t_sbluemax1191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "The shrimp is mad at ya." # @t_sbluemax1192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_revenge_happy as taira
    t_ch_taira "Yeah, but the shrimp’s pretty cute. We gotta whole “will they, won’t they” thing going." # @t_sbluemax1193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Whaaaaa?)" # @t_sbluemax1194.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Anyway, what’cha gonna do? SHORT ME TO DEATH?" # @t_sbluemax1195.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_bullies "HAW HAW! Good one!" # @t_sbluemax1196.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wait. That wasn’t a good one.)" # @t_sbluemax1197.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(That wasn’t a good one at all!)" # @t_sbluemax1198.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " We do NOT have a “will they, won’t they” thing. It’s just they won’t, uh, they." # @t_sbluemax1198.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " So, why don’t you guys BUZZ OFF!" # @t_sbluemax1198.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Whoa, that sounded pretty tough.)" # @t_sbluemax1198.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Guess I’m upset!)" # @t_sbluemax1199.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Oh? Who’s gonna make us?" # @t_sbluemax1200.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "YOU, New Dork?" # @t_sbluemax1201.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Taira’s really a one trick pony with his insult repertoire!)" # @t_sbluemax1202.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_angry as cousin
    extend " Maybe I will!" # @t_sbluemax1202.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " (Um, now I’m just saying crazy things!)" # @t_sbluemax1202.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(There’s no way I could stop any of these guys, much less ALL OF THEM!)" # @t_sbluemax1203.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Not without my katamari anyway…)" # @t_sbluemax1204.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_30', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "You? Yeah, I don’t think so, Shorty." # @t_sbluemax1205.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_31', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/kingroar1.ogg"
    t_ch_king "ROOOAAAR!!!" # @t_sbluemax1206.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_32', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_trio_ballers as students:
        # ShowWithAtl
        ease_expo .3 xpos 1.49 
    extend "{w=0.3}{nw}"
    t_ch_bullies "!!!" # @t_sbluemax1207.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_33', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin:
        linear .2 xzoom 1.0 
        # ShowWithAtl
        linear .2 xpos 0.25 
    extend "{w=0.2}{nw}"
    t_ch_cousin "!!!" # @t_sbluemax1208.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_34', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_confused as taira:
        # ShowWithAtl
        ease_expo .2 xpos 0.13 
    extend "{w=0.2}{nw}"
    t_ch_taira "!!!" # @t_sbluemax1209.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_35', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_worried as bluemax:
        linear .2 xzoom -1.0 
        # ShowWithAtl
        linear .2 xpos 0.45 
    extend "{w=0.2}{nw}"
    t_ch_max "Oh, thank goodness." # @t_sbluemax1210.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_36', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_confident as king:
        # ShowWithAtl
        linear .33 alpha 1.0
    show i_digdug_left as digdug:
        # ShowWithAtl
        pause 1.0 
        linear .33 alpha 1.0
    extend "{w=1.33}{nw}"
    t_ch_digdug "Now, we don’t have time to determine who’s bullying who." # @t_sbluemax1211.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_37', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Even though that would take less time for me to figure out than explaining how we don’t have the time to figure it out." # @t_sbluemax1212.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_38', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "We was just playin’ around." # @t_sbluemax1213.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_39', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Weren’t we, Max?" # @t_sbluemax1214.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Okay, yeah, sure." # @t_sbluemax1215.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "Oh, so, what? Revenge is just a GAME to you, bro?" # @t_sbluemax1216.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "B-b-but you said…!!!" # @t_sbluemax1217.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/kingroar2.ogg"
    show i_king_screaming as king
    t_ch_king "ROAR!" # @t_sbluemax1218.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Yes, good thinking, King. We will not sentence anyone here to additional detention." # @t_sbluemax1219.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "ON THE SINGULAR CONDITION THAT ALL OF YOU BREAK IT UP IMMEDIATELY!!!" # @t_sbluemax1220.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Taira, get to Wrestleball practice." # @t_sbluemax1221.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Max, go build a model plane or something." # @t_sbluemax1222.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_digdug "[slot_playerName], I don’t know your thing yet, but go and do it quietly." # @t_sbluemax1223.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Bullies, you have like no lines of dialog, no one cares about you, just scram." # @t_sbluemax1224.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Yeah, I’m leavin’." # @t_sbluemax1225.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "But not before I threaten the dorks with an otherwise benign phrase like, “See you LATER.”" # @t_sbluemax1226.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "But, for [slot_playerName], it could also be like a kinda TOTALLY sexy “see you later” if you play your cards right." # @t_sbluemax1227.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Yes, yes. Very good. Just get moving." # @t_sbluemax1228.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_3O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
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
    $ renpy.pause(0.99, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_3P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_worried as bluemax:
        # ShowWithAtl
        linear .2 xpos 0.75 
        linear .2 xzoom 1.0 
    extend "{w=0.2}{nw}"
    t_ch_max "Whew. They’re gone." # @t_sbluemax1229.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I’m glad they left us alone, but I wish Principal Dig Dug had been a little more thorough about his investigation and punishment." # @t_sbluemax1230.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Or done either of those things at all!" # @t_sbluemax1231.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Yeah, that would’ve been good too." # @t_sbluemax1232.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Um." # @t_sbluemax1233.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Does that happen every day?" # @t_sbluemax1234.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "No. Not every day." # @t_sbluemax1235.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "They hardly ever bother me on the weekend…" # @t_sbluemax1236.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_shock_serious as bluemax
    extend " But it’s okay! Because I’ve got the SECRET PROJECT SUPER PLANE!" # @t_sbluemax1236.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "And when it’s done no one will be able to push me anymore!" # @t_sbluemax1237.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Um, not because of violent war plane revenge, right?" # @t_sbluemax1238.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Of course not, that’s crazy." # @t_sbluemax1239.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "They won’t be able to push me around because I’ll be FLYING." # @t_sbluemax1240.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(But...Max is a bird.)" # @t_sbluemax1241.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Shouldn’t he be able to fly by himself?)" # @t_sbluemax1242.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Well, I mean, not all the time though." # @t_sbluemax1242.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Right? Like, you’d need to refuel and use the bathroom and sleep and stuff." # @t_sbluemax1243.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_shock_worried as bluemax
    t_ch_max "Well." # @t_sbluemax1244.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Uh." # @t_sbluemax1245.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "There’d be. Um." # @t_sbluemax1246.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Huh." # @t_sbluemax1247.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Oh wow, look at the time. Military History Club is over." # @t_sbluemax1248.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh…" # @t_sbluemax1249.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Was it something I said?)" # @t_sbluemax1249.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "But, um…" # @t_sbluemax1250.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "I just wanted to say." # @t_sbluemax1251.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "Y’know." # @t_sbluemax1252.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_cower_worried as bluemax
    t_ch_max "Thank you. For earlier. With Taira and them." # @t_sbluemax1253.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Don’t mention it." # @t_sbluemax1254.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_max "It’s just that, um." # @t_sbluemax1255.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_cower_flustered as bluemax
    t_ch_max "No one’s ever…" # @t_sbluemax1256.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "??" # @t_sbluemax1257.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_3v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bluemax_cower_flustered as bluemax:
        # ShowWithAtl
        pause 0.7 
        linear .33 alpha 0.0
    extend "{w=1.03}{nw}"
    t_ch_max "Bye, [slot_playerName]!" # @t_sbluemax1258.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "…" # @t_sbluemax1259.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Bye, Max." # @t_sbluemax1260.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " (Look at him.)" # @t_sbluemax1260.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Even just walking down the halls, he keeps checking over his shoulder.)" # @t_sbluemax1261.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_40', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(He’s very, hmmm...)" # @t_sbluemax1262.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_41', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Well, shy. And nervous.)" # @t_sbluemax1263.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_42', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(But also sincere!)" # @t_sbluemax1264.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_43', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It’s a shame he has it so rough. And he keeps it all bottled up.)" # @t_sbluemax1265.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_44', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Maybe he just needs someone to help him break out of his shell so everyone else can see the sweet kid he really is.)" # @t_sbluemax1266.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_45', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
    label s_bluemax1__45:
        # <NHSceneChange NHSceneChange {'name': '_45', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
        jump s_day2