# <Scene {'id': 's_bluemax3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_bluemax3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_bluemax3"
    $ renpy.pause(1)
    # <Scene {'id': 's_bluemax3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/aroundtown.ogg" loop
    show i_bg_cafe as bg zorder 0 at default
    show i_trio_ballers as students zorder 1:
        default
        alpha 0.0
        xpos 0.56 
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 3:
        default
        xpos 0.25 
    show i_king_screaming as king zorder 1:
        default
        xpos 0.87 
        alpha 0.0
    show i_taira_steveholt_happy as taira zorder 1:
        default
        alpha 0.0
        xpos 0.82 
    show i_digdug_left as digdug zorder 2:
        default
        alpha 0.0
        xpos 0.8 
    show i_tomari_standing_smile as tomari zorder 1:
        default
        alpha 0.0
        xpos 0.75 
    show i_bluemax_stand_smile as bluemax zorder 2:
        default
        xpos 1.2 
        alpha 1.0
    t_ch_cousin "(Gosh, it sure is crowded in here.)" # @t_sbluemax31.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Not sure why Max wants to discuss secret plan stuff where anyone could overhear it though!)" # @t_sbluemax32.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_smile as bluemax:
        # ShowWithAtl
        linear .7 xpos 0.75 
    extend "{w=0.7}{nw}"
    t_ch_max "[slot_playerName]! Over here. I saved you a spot in line." # @t_sbluemax33.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(He’s at the end of the line…)" # @t_sbluemax34.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Well, it’s the thought that counts.)" # @t_sbluemax35.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Thanks, Max." # @t_sbluemax35.01 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "So." # @t_sbluemax36.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "We shall count this as a top secret meeting of the Military History Club." # @t_sbluemax37.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Strictly closed doors. Need to know basis. Beyond top secret." # @t_sbluemax38.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "About that. Are you sure it’s safe? I mean, can’t anyone overhear us?" # @t_sbluemax39.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "That’s the beauty of it! There’s so many kids in here all talking at once that our conversation will be indecipherable from background noise!" # @t_sbluemax310.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax:
        linear .2 xzoom -1.0 
        # ShowWithAtl
        linear .25 xpos 0.36 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear .25 xpos 0.13 
    show i_tomari_standing_smile as tomari:
        # FadeEvent
        linear 0.25 alpha 1.0
    $ renpy.pause(0.25) # TimedPause
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "I can hear everything you’re saying." # @t_sbluemax311.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Quite clearly." # @t_sbluemax312.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Okay, but that’s not important though!" # @t_sbluemax313.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_max "We’ll be using big time military jargon and top secret codenames and stuff." # @t_sbluemax314.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "So, even if you could hear us, it won’t matter because it’ll sound like jibberish!" # @t_sbluemax315.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "You’re gonna talk about your secret plans for the super plane you’re building." # @t_sbluemax316.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_serious as bluemax
    t_ch_max "Okay, but that’s not important either though!" # @t_sbluemax317.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Because no one talks to Tomari." # @t_sbluemax318.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thinking as tomari
    t_ch_tomari "Thankfully." # @t_sbluemax319.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Also I consulted him on the design spec parameters, so he knew all about it anyway." # @t_sbluemax320.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "It’s true." # @t_sbluemax321.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "The opportunity to contemplate a challenging project was all the payment that was required." # @t_sbluemax322.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "But the cookies were a nice touch, Max." # @t_sbluemax323.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_smile as bluemax
    t_ch_max "Of course!" # @t_sbluemax324.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "There’s more in the pipeline, by the way. We’re still in committee on the topic, but there’s been some headway recently." # @t_sbluemax325.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Very good." # @t_sbluemax326.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Keep me informed." # @t_sbluemax327.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_smile as bluemax:
        linear .2 xzoom 1.0 
        # ShowWithAtl
        pause 0.33 
        linear .25 xpos 0.7 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        pause 0.33 
        linear .25 xpos 0.25 
    show i_tomari_standing_smile as tomari:
        # FadeEvent
        linear 0.25 alpha 0.0
    $ renpy.pause(0.5800000000000001) # TimedPause
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        linear 0.5 xpos 1.3 
    extend "{w=0.5}{nw}"
    t_ch_max "So, you see, [slot_playerName]? Perfectly secure!" # @t_sbluemax328.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I guess it kind of is." # @t_sbluemax329.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "Okay, so. Let us discuss PROJECT SUPER SECRET PLANE." # @t_sbluemax330.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Roger." # @t_sbluemax331.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Ha! Very good." # @t_sbluemax332.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_serious as bluemax
    t_ch_max "Remember now, PROJECT SUPER SECRET PLANE is just the codename for SECRET PROJECT SUPER PLANE." # @t_sbluemax333.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Don’t confuse them for two separate ops." # @t_sbluemax334.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Right." # @t_sbluemax335.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # FadeEvent
        alpha 1.0
    t_ch_max "Oh, and ops is a codename for operations." # @t_sbluemax336.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "It’s very military." # @t_sbluemax337.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Hm, yeah. I think I got it." # @t_sbluemax339.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "It’s a plane of my own design." # @t_sbluemax340.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        ease_expo .25 xpos 0.9 
    extend "{w=0.25}{nw}"
    t_ch_tomari "Mostly your design." # @t_sbluemax341.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "With some outside consultancy, yes." # @t_sbluemax342.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        ease_expo .25 xpos 1.3 
    extend "{w=0.25}{nw}"
    t_ch_max "Anyway!" # @t_sbluemax343.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I don’t have time to design it up and to build it and go to school and run the Military History Club and sleep and eat." # @t_sbluemax344.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "So, I’ve been working on PROJECT SUPER SECRET PLANE on my homework and test sheets and quizzes and stuff." # @t_sbluemax345.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Aren’t you afraid that’ll give away the secret?" # @t_sbluemax346.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "I like how you think, [slot_playerName]. Very security oriented. That’s good." # @t_sbluemax347.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I make sure to break up different parts of the designs into different assignments from different classes!" # @t_sbluemax348.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "That way, no single teacher has access to anything more than a fraction of a part of any system. It’ll just look like doodles and random goof off stuff to them!" # @t_sbluemax349.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "That’s good thinking." # @t_sbluemax350.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I know!" # @t_sbluemax351.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_max "But it gets better. The designs are all done." # @t_sbluemax352.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        ease_expo .25 xpos 0.9 
    extend "{w=0.25}{nw}"
    t_ch_tomari "You’re welcome, by the way." # @t_sbluemax353.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Thanks to some outside consultancy, yes." # @t_sbluemax354.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        ease_expo .25 xpos 1.3 
    extend "{w=0.25}{nw}"
    t_ch_max "ANYWAY!" # @t_sbluemax355.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "We can build the plane and get extra school spirit credit for the Military History Club to reduce our detention." # @t_sbluemax356.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_smile as bluemax
    t_ch_max "And then at the same time it’ll keep us bully free because we’ll fly from one class to the next! Pretty great, huh?" # @t_sbluemax357.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "I have to admit, it is!" # @t_sbluemax358.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But is it really fair to let me piggyback on this thing? It seems like you already did all the work." # @t_sbluemax359.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        ease_expo .25 xpos 0.9 
    extend "{w=0.25}{nw}"
    t_ch_tomari "It would be more precise to say all the work was done." # @t_sbluemax360.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Yes. Thank you, Tomari. Your contributions will go down in history." # @t_sbluemax361.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        ease_expo .25 xpos 1.3 
    show i_bluemax_shock_serious as bluemax
    extend "{w=0.25}{nw}"
    t_ch_max "Top secret history, that is!" # @t_sbluemax362.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Actually, won’t it it be completely NOT AT ALL secret when we’re seen flying everywhere?" # @t_sbluemax363.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Ah. Uh, well…" # @t_sbluemax364.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And, come to think of it, what do you want with a plane anyway?" # @t_sbluemax365.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You’re a bird, aren’t you?" # @t_sbluemax366.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Uh, y-yeah. Flying." # @t_sbluemax367.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Like a bird. Like normal. Heh." # @t_sbluemax368.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "MEETING ADJOURNED THOUGH!" # @t_sbluemax369.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(What the heck was that all about?)" # @t_sbluemax370.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "..." # @t_sbluemax371.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Okay but now we need to call an emergency session of the Military History Club." # @t_sbluemax372.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But you just ended the meeting?" # @t_sbluemax373.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "This is to discuss new business about something else entirely." # @t_sbluemax374.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Namely: the part where we need to get all those designs I turned in for homework and tests and stuff!" # @t_sbluemax375.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What do you mean?" # @t_sbluemax376.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "As we discussed in the previous meeting…" # @t_sbluemax377.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "...Actually, this is where having the minutes of the previous meeting would come in really handy." # @t_sbluemax378.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_max "I’ll see to it that we commission a report on a survey for a committee to explore the possibility of formalizing our record keeping procedures for secret and emergency meetings." # @t_sbluemax379.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "But until then we’ll have to rely on memory!" # @t_sbluemax380.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "So, last time we were here we spoke about the designs. Remember?" # @t_sbluemax381.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Of course I remember! It was like ten seconds ago!)" # @t_sbluemax382.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Yes. But only vaguely." # @t_sbluemax382.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "For security purposes." # @t_sbluemax383.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Excellent. Well, the designs are done, as I said, but they’ve all been turned in to different teachers!" # @t_sbluemax384.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And that means you don’t have some of them?" # @t_sbluemax385.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Correct." # @t_sbluemax386.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Or, more to the point...any of them!" # @t_sbluemax387.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Oh, no." # @t_sbluemax388.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Oh, yup!" # @t_sbluemax389.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_serious as bluemax
    t_ch_max "Therefore, construction has been, um, delayed." # @t_sbluemax390.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Can we wait for the teachers to give back your homework?" # @t_sbluemax391.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "We don’t have that kind of time. It could take them days. Or weeks!" # @t_sbluemax392.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "OR YEARS!" # @t_sbluemax393.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Probably not years." # @t_sbluemax394.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "No, probably not." # @t_sbluemax395.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "But we can’t take the chance!" # @t_sbluemax396.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "We need to implement a pre-emptive strike!" # @t_sbluemax397.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Mission." # @t_sbluemax398.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Parameter." # @t_sbluemax399.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "Yeah!" # @t_sbluemax3100.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Who’s with me?" # @t_sbluemax3101.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Who’s he asking? Aren’t I the only one here?)" # @t_sbluemax3102.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Um. Well, I’ll help out. Sure." # @t_sbluemax3102.01 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "You’ve got the backing of the entire Military History Club cabinet." # @t_sbluemax3103.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "And its senior members." # @t_sbluemax3104.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "And its parliament." # @t_sbluemax3105.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "And its house of commons." # @t_sbluemax3106.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "And its caliphate." # @t_sbluemax3107.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "And its--" # @t_sbluemax3108.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Max." # @t_sbluemax3109.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "[slot_playerName]?" # @t_sbluemax3110.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "All of those are just you, right? You staff all of those positions." # @t_sbluemax3111.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Most of them. For some I’m only acting in Aki’s stead." # @t_sbluemax3112.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        ease_expo .25 xpos 0.9 
    extend "{w=0.25}{nw}"
    t_ch_tomari "And there is an occasional need for outside consultancy in any sufficiently complex system." # @t_sbluemax3113.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Does that mean we’ve got Tomari’s support too?" # @t_sbluemax3114.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Conflict of interest, I’m afraid." # @t_sbluemax3115.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_worried as bluemax
    t_ch_max "He’s a nerd for hire." # @t_sbluemax3116.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "I prefer the term knowledge mercenary." # @t_sbluemax3117.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        ease_expo .25 xpos 1.3 
    show i_bluemax_stand_worried as bluemax
    extend "{w=0.25}{nw}"
    t_ch_max "Regardless. Tomari is like the wind." # @t_sbluemax3118.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Looks like it’s up to you and me, [slot_playerName]!" # @t_sbluemax3119.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I’m sure we can do it!" # @t_sbluemax3120.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_smile as bluemax
    t_ch_max "Yeah!" # @t_sbluemax3121.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "We’ll set up a report to survey a commission to staff an exploratory committee to--" # @t_sbluemax3122.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_shocked as bluemax:
        linear .2 xzoom -1.0 
        # ShowWithAtl
        pause 0.33 
        linear .25 xpos 0.25 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        pause 0.33 
        linear .25 xpos 0.11 
    show i_taira_steveholt_happy as taira:
        # FadeEvent
        linear 0.25 alpha 1.0
    $ renpy.pause(0.5800000000000001) # TimedPause
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "If it isn’t Blue Dork!" # @t_sbluemax3123.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "AHH!" # @t_sbluemax3124.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Sheesh! Does everyone come here?!?)" # @t_sbluemax3125.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "And his friend Cute New Dork." # @t_sbluemax3126.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    show i_trio_ballers as students:
        # ShowWithAtl
        linear .5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_bullies "Haw haw!" # @t_sbluemax3127.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(Ugh, why does he think hitting on me WHILE he’s bullying me will work?!)" # @t_sbluemax3128.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " We don’t want any trouble, Taira." # @t_sbluemax3128.01 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_confused as taira
    show i_bluemax_cower_worried as bluemax
    t_ch_taira "Yo, that’s too bad. ‘Cause I want trouble!" # @t_sbluemax3129.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "Thought you wanted revenge, Captain." # @t_sbluemax3130.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Revenge IS trouble." # @t_sbluemax3131.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "FOR THEM!" # @t_sbluemax3132.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "C’mon, Taira. This is the cafe. It’s hallowed ground." # @t_sbluemax3133.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax:
        xzoom 1.0 
    t_ch_max "They’re bullies." # @t_sbluemax3134.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Nothing is sacred to them!" # @t_sbluemax3135.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_confused as taira
    t_ch_taira "He’s right!" # @t_sbluemax3136.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Except, I guess, the revenge." # @t_sbluemax3137.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "But that’s more a function of your backstory though. Like, us? We’re pretty much so-so on the revenge angle." # @t_sbluemax3138.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Okay, yeah. That’s a good point." # @t_sbluemax3139.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "No prob, Captain." # @t_sbluemax3140.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Why do you need to get revenge on poor Max anyway?" # @t_sbluemax3141.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "‘Cause we got in trouble earlier!" # @t_sbluemax3142.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "How is that Max’s fault?!" # @t_sbluemax3143.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "What we got in trouble for was pushing him around some!" # @t_sbluemax3144.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "!!!!!!" # @t_sbluemax3145.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s not Max’s fault!" # @t_sbluemax3145.01 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "YOU guys chose to cause trouble." # @t_sbluemax3146.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_serious as taira
    t_ch_taira "Yeah, but we wouldn’t if he wasn’t so mad revenge-able!" # @t_sbluemax3147.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "HIS FAULT!" # @t_sbluemax3148.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Forget it, [slot_playerName]!" # @t_sbluemax3149.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Logic won’t work on bullies." # @t_sbluemax3150.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "He’s right!" # @t_sbluemax3151.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well, you can’t start a fight in the cafe." # @t_sbluemax3152.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s against the rules!" # @t_sbluemax3153.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies "Oh no!" # @t_sbluemax3154.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "…" # @t_sbluemax3155.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "…………." # @t_sbluemax3156.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Did...did that really work?!?)" # @t_sbluemax3157.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "………………………………" # @t_sbluemax3158.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Hey!" # @t_sbluemax3159.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I think they're trickin’ us with their brain games!" # @t_sbluemax3160.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Dangit.)" # @t_sbluemax3161.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Guys, crowdsource the answer to that one." # @t_sbluemax3162.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I’ll get some kinda other temporary revenge until we can come back and do one up proper. Revenge is mad complicated. You’re too dumb to understand." # @t_sbluemax3163.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Well, it kind of worked?)" # @t_sbluemax3164.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Poor Max is shaking like a leaf!)" # @t_sbluemax3165.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Why can’t these guys just leave him alone?)" # @t_sbluemax3166.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Step aside, Shrimp." # @t_sbluemax3167.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "You’re gettin’..." # @t_sbluemax3168.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "SKIPPED IN LINE!" # @t_sbluemax3169.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "!!!!!" # @t_sbluemax3170.00 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "!!!!!" # @t_sbluemax3171.00 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That’s definitely against the rules too though!" # @t_sbluemax3172.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Yeah. But it’s a lesser offense!" # @t_sbluemax3173.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Probably?" # @t_sbluemax3174.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "Yo, I don’t have time for egghead brain debate theater. It’s already half past revenge!" # @t_sbluemax3175.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "No." # @t_sbluemax3176.00 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s not fair. Not to Max, or me, or anyone behind us!" # @t_sbluemax3177.00 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Okay, yeah, we’re still at the back of the line, but it’s the principle of the thing!)" # @t_sbluemax3177.01 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Look, New Dork. This is happening." # @t_sbluemax3178.00 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Just roll over." # @t_sbluemax3179.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Little does he know that I do the rolling around here!!!)" # @t_sbluemax3180.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (...Uh. But not without my katamari ball of course.)" # @t_sbluemax3180.01 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Hm. Don’t have much of a rejoinder for that taunt after all, I guess!)" # @t_sbluemax3181.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "C’mon. Move it." # @t_sbluemax3182.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    t_ch_cousin "YOU SHALL NOT PASS!" # @t_sbluemax3183.00 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "No, [slot_playerName]! It’s not worth it!" # @t_sbluemax3184.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/kingroar3.ogg"
    show i_cousin_default_surprised as cousin
    show i_bluemax_cower_shock as bluemax
    show i_taira_akimbo_confused as taira
    t_ch_king "ROOOOAAAAR!" # @t_sbluemax3185.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear .25 xpos 0.11 
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        linear .25 xpos 0.3 
    show i_taira_akimbo_confused as taira:
        # ShowWithAtl
        linear .25 xpos 0.2 
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.25 alpha 1.0
    show i_king_screaming as king:
        xzoom -1.0 
        # FadeEvent
        linear 0.25 alpha 1.0
    $ renpy.pause(0.25) # TimedPause
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Oh, no!" # @t_sbluemax3186.00 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Is this…" # @t_sbluemax3187.00 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "SKIPPING?!?" # @t_sbluemax3188.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Only not in the delinquent sense of ditching class, but rather skipping people IN LINE?" # @t_sbluemax3189.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "YOU’RE ALREADY AT THE END OF THE LINE!!!" # @t_sbluemax3190.00 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "You kids need to show more ambition if you’re going to go through the trouble of causing trouble!" # @t_sbluemax3191.00 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "The only question now is which one of you to punish..." # @t_sbluemax3192.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "It was Taira and his gang trying to push around Blue Max again!" # @t_sbluemax3193.00 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "A likely story, [slot_playerName]." # @t_sbluemax3194.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "In fact, it’s one I’ve heard a dozen times." # @t_sbluemax3195.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Probably because of all the times Taira and his gang pushed around Blue Max." # @t_sbluemax3196.00 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_king "ROOOOAAR ROAR!!!" # @t_sbluemax3197.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Yes, I know, it’s already half past wrestling." # @t_sbluemax3198.00 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Look, we don’t have much time. So, instead I’m meting out the best kind of justice." # @t_sbluemax3199.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king
    show i_cousin_default_mortified as cousin
    show i_taira_default_pleading as taira
    t_ch_digdug "ALL OF YOU VERSUS KING IN TAGTEAM CAGEMATCH WRESTLING!" # @t_sbluemax3200.00 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_shocked as bluemax:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.36 
    extend "{w=0.5}{nw}"
    t_ch_max "AAAHHH!!!" # @t_sbluemax3201.00 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "!!!" # @t_sbluemax3202.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Aw, man." # @t_sbluemax3203.00 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies ":(" # @t_sbluemax3204.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "But I can’t do that without a signed permission slip from your parents and for some reason none of the parents in Namco Land want me to let their kids get demolished in the ring." # @t_sbluemax3205.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_digdug "Go figure." # @t_sbluemax3206.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "So, instead of that, we’ll do the second best kind of justice." # @t_sbluemax3207.00 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "INDISCRIMINATE!!!" # @t_sbluemax3208.00 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_flustered as bluemax
    t_ch_max "Ahh?" # @t_sbluemax3209.00 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "???" # @t_sbluemax3210.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Aww?" # @t_sbluemax3211.00 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_bullies ":\\" # @t_sbluemax3212.00 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Therefore, everyone involved with this altercation is hereby sentenced to…" # @t_sbluemax3213.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "DETENTION LEVEL EIGHT -- DARK REALM DETENTION!!!" # @t_sbluemax3214.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(That...can’t be real. Can it?!)" # @t_sbluemax3215.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Where you will be cursed to fight the undead for a thousand years!" # @t_sbluemax3216.00 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(HOW IS THAT LEGAL???)" # @t_sbluemax3217.00 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_happy as taira
    t_ch_taira "Only a thousand? Haw, sounds like a vacation, yo." # @t_sbluemax3218.00 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "You just got yourself Double Dark Realm Detention, mister." # @t_sbluemax3219.00 self.block='Last'
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_angry as taira
    t_ch_taira "What?! So uncool!" # @t_sbluemax3220.00 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I’ll get you for this, Blue Dork!" # @t_sbluemax3221.00 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "I’ll get yoooooooooooooooouuuuuuuuu…" # @t_sbluemax3222.00 self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(OH MY GOSH!!!)" # @t_sbluemax3223.00 self.block='Last'
    # <ParallelEvent {'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Is he being banished to the Dark Realm before my very eyes?!?!?!)" # @t_sbluemax3224.00 self.block='Last'
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "...uuuuuuu..." # @t_sbluemax3225.00 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "*cough ahem cough*" # @t_sbluemax3226.00 self.block='Last'
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused as taira
    t_ch_taira "Sorry. My voice just does that sometimes. It’s weird." # @t_sbluemax3227.00 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Off to the Double Dark Realm with you and your lackeys." # @t_sbluemax3228.00 self.block='Last'
    # <ParallelEvent {'name': '_3q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "It’ll be in room 302." # @t_sbluemax3229.00 self.block='Last'
    # <ParallelEvent {'name': '_3r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Yeah, yeah. I know where it is." # @t_sbluemax3230.00 self.block='Last'
    # <ParallelEvent {'name': '_3s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_trio_ballers as students:
        # FadeEvent
        linear 0.33 alpha 0.0
    show i_taira_default_confused as taira:
        # FadeEvent
        linear 0.33 alpha 0.0
    show i_cousin_default_neutral as cousin
    extend "{w=0.33}{nw}"
    t_ch_digdug "As for the rest of you, straighten up and fly right." # @t_sbluemax3231.00 self.block='Last'
    # <ParallelEvent {'name': '_3t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax
    t_ch_max "Fly?! Why are you making us fly?" # @t_sbluemax3232.00 self.block='Last'
    # <ParallelEvent {'name': '_3u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "You can’t do that! Your authority only goes so far!" # @t_sbluemax3233.00 self.block='Last'
    # <ParallelEvent {'name': '_3v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Gravity happens y’know and maybe that’s to keep us safely on the ground you ever think about that?" # @t_sbluemax3234.00 self.block='Last'
    # <ParallelEvent {'name': '_3w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Whoa, where’s all this coming from?)" # @t_sbluemax3235.00 self.block='Last'
    # <ParallelEvent {'name': '_3x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I was speaking poetically, Blue Max." # @t_sbluemax3236.00 self.block='Last'
    # <ParallelEvent {'name': '_3y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I paint pictures with the brush of language. As all principals do." # @t_sbluemax3237.00 self.block='Last'
    # <ParallelEvent {'name': '_3z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Oh. Y-yeah, I knew that." # @t_sbluemax3238.00 self.block='Last'
    # <ParallelEvent {'name': '_40'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Now, get back to school grounds. Don’t make me do more justice on you." # @t_sbluemax3239.00 self.block='Last'
    # <ParallelEvent {'name': '_41'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "We won’t, sir!" # @t_sbluemax3240.00 self.block='Last'
    # <ParallelEvent {'name': '_42'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.33 alpha 0.0
    show i_king_confident as king:
        # FadeEvent
        linear 0.33 alpha 0.0
    show i_cousin_default_neutral as cousin
    extend "{w=0.33}{nw}"
    extend " Max, are you okay?" # @t_sbluemax3240.01 self.block='Last'
    # <ParallelEvent {'name': '_43'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Gosh, he’s still shaking a little!)" # @t_sbluemax3240.02 self.block='Last'
    # <ParallelEvent {'name': '_44'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    extend "{w=0.5}{nw}"
    t_ch_max "Y-yeah. I’ll be fine." # @t_sbluemax3241.00 self.block='Last'
    # <ParallelEvent {'name': '_45'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "I am fine, I mean." # @t_sbluemax3242.00 self.block='Last'
    # <ParallelEvent {'name': '_46'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I’m fine!" # @t_sbluemax3243.00 self.block='Last'
    # <ParallelEvent {'name': '_47'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Let’s just never talk about this ever again." # @t_sbluemax3243.01 self.block='Last'
    show i_sw_black as curtain zorder 10:
        # FadeEvent
        linear 1.0 alpha 1.0
    # <ParallelEvent {'name': '_4A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(We didn’t talk about it, but I kept thinking about it all through the rest of the day.)" # @t_sbluemax3245.00 self.block='Last'
    # <ParallelEvent {'name': '_4B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Especially, though, I thought about how much Max freaked out every time someone mentioned flying…)" # @t_sbluemax3246.00 self.block='Last'
    # <NHSceneChange {'name': '_4C', 'scene': 's_day4'} NHSceneChange ''>
    label s_bluemax3__4C:
        # <NHSceneChange {'name': '_4C', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4