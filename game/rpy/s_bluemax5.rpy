# <Scene {'id': 's_bluemax5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_bluemax5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_bluemax5"
    $ renpy.pause(1)
    # <Scene {'id': 's_bluemax5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/privatetimes.ogg" loop
    show i_bg_rooftop as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 3:
        default
        xpos 0.25 
    show i_bluemax_shock_flustered as bluemax zorder 2:
        default
        xpos 0.75 
        alpha 0.0
    show i_pacman_left as pacman zorder 2:
        default
        xpos 1.47 
    t_ch_cousin "(Hope I’m not too late.)" # @t_sbluemax50.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Took me a little while to get food for both of us.)" # @t_sbluemax51.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Can’t plan a good heist on an empty stomach!)" # @t_sbluemax52.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Or maybe you can. What do I know about heists!)" # @t_sbluemax53.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Anyway, it was pizza day.)" # @t_sbluemax54.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_flustered as bluemax:
        xzoom -1.0 
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_cousin "(Ah, there’s Max. I hope he wasn’t waiting long.)" # @t_sbluemax55.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(He’s awful close to the edge…)" # @t_sbluemax56.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Deep breaths, Max." # @t_sbluemax57.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What’s he doing…?)" # @t_sbluemax58.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_flustered as bluemax:
        # ShowWithAtl
        linear .5 xpos 0.78 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(He’s leaning over…)" # @t_sbluemax59.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Be careful, Max!!!)" # @t_sbluemax510.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(What am I thinking? He’s made out of feathers!)" # @t_sbluemax511.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_flustered as bluemax:
        # ShowWithAtl
        linear .5 xpos 0.81 
    extend "{w=0.5}{nw}"
    t_ch_max "You can do it. Just look. Just open your eyes and look down." # @t_sbluemax512.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_worried as bluemax
    t_ch_max "It’s not like it’s as high as f-f-flying." # @t_sbluemax513.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "It can’t be that bad." # @t_sbluemax514.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Is Blue Max…)" # @t_sbluemax515.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(AFRAID OF HEIGHTS?!?!?)" # @t_sbluemax516.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Okay! You almost cracked open one eye a peep." # @t_sbluemax517.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Let’s not overdo it all in one go. That’s enough for today." # @t_sbluemax518.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Whew!" # @t_sbluemax519.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Oh, he’s away from the edge now. Good.)" # @t_sbluemax520.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’ll just, uh, I don’t want to embarrass him…)" # @t_sbluemax521.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh. Ahem." # @t_sbluemax521.01 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_shocked as bluemax:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.75 
    extend "{w=0.5}{nw}"
    t_ch_max "AHH!" # @t_sbluemax522.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(Darn it, Max.)" # @t_sbluemax523.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " Oh, Max." # @t_sbluemax523.01 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I, uh, didn’t see you up here." # @t_sbluemax524.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Or hear anything either, come to think of it." # @t_sbluemax525.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_worried as bluemax
    t_ch_max "Oh, yeah. Good." # @t_sbluemax526.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "Because there wasn’t anything to see or to hear. Yup." # @t_sbluemax527.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "On an innocuous change of topic, I brought us some food!" # @t_sbluemax528.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (And the Oscar for Best Actor goes to [slot_playerName]!)" # @t_sbluemax528.01 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "You didn’t have to do that." # @t_sbluemax529.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Can’t plan a caper on an empty stomach!" # @t_sbluemax530.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh, or can you?" # @t_sbluemax531.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m new to this stuff!" # @t_sbluemax532.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_smile as bluemax
    t_ch_max "Ooh, it was pizza day?" # @t_sbluemax533.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "You definitely made the right call!" # @t_sbluemax534.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_eating "muncha muncha muncha" # @t_sbluemax535.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "That hit the spot." # @t_sbluemax536.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "Sure did." # @t_sbluemax537.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "It’s funny. In all my time at Namco High…" # @t_sbluemax538.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I never…well, y’know. Ate with someone." # @t_sbluemax539.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "!!!" # @t_sbluemax540.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That’s crazy. You usually eat in the cafeteria, right?" # @t_sbluemax541.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "No." # @t_sbluemax542.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I usually don’t eat lunch at all." # @t_sbluemax543.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But why is…" # @t_sbluemax544.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Oh. That’s when your Military History Club meets, isn’t it?" # @t_sbluemax545.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "At twelve hundred hours." # @t_sbluemax546.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Noon hundred, [slot_playerName]." # @t_sbluemax547.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "But, yeah, that’s when it meets. I figure, since I’m not eating lunch, why bother going?" # @t_sbluemax548.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Y’know?" # @t_sbluemax549.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But aren’t you hungry?" # @t_sbluemax550.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Of course! But…" # @t_sbluemax551.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "It’s just that…" # @t_sbluemax552.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Y’know." # @t_sbluemax553.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "I can never hold on to my lunch money long enough to get to lunch!" # @t_sbluemax554.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Gasp!" # @t_sbluemax555.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_shocked as bluemax
    t_ch_cousin "TAIRA?!" # @t_sbluemax556.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh, uh, sorry." # @t_sbluemax558.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I meant it more like a dramatic realization, not a declaration of his vicinity." # @t_sbluemax559.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax
    t_ch_max "Whew." # @t_sbluemax560.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But that’s why? He revenges you?" # @t_sbluemax561.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Sometimes." # @t_sbluemax562.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "He always catches me between classes." # @t_sbluemax563.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I’m able to get away by tossing my lunch money at him and then RUNNING LIKE WOW." # @t_sbluemax564.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well, there’s not much we can do against Taira and his horde by ourselves." # @t_sbluemax565.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Aren’t they were banished to a dimension of unliving horror by Principal Dig Dug though?" # @t_sbluemax566.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That’s just during detention. They’re free to tyrannize you all the rest of the time!" # @t_sbluemax567.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "So let’s get those SECRET PLANE SUPER PROJECT designs and make sure you’re never pushed around again!" # @t_sbluemax568.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Uh, yeah!" # @t_sbluemax569.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_smile as bluemax
    t_ch_max "Let’s do that thing you said." # @t_sbluemax570.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Max. Is there something else you’re not telling me?" # @t_sbluemax571.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "No, of course not." # @t_sbluemax572.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Like what though?" # @t_sbluemax573.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I mean of course there isn’t, y’know, but like what?" # @t_sbluemax574.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hmmm. I think I know what it is.)" # @t_sbluemax575.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Gonna have to play this one careful.)" # @t_sbluemax576.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Hey, follow me." # @t_sbluemax576.01 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Where?" # @t_sbluemax577.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I wanna show you something." # @t_sbluemax578.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But you have to get close to the edge to see it." # @t_sbluemax579.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_worried as bluemax
    t_ch_max "Th-the edge?" # @t_sbluemax580.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Of the r-r-roof?" # @t_sbluemax581.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah. It’s no big deal." # @t_sbluemax582.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "N-no. No, of course it isn’t." # @t_sbluemax583.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "But uh we don’t have time for sightseeing, [slot_playerName]!" # @t_sbluemax584.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "We’ve got a heist to orchestrate." # @t_sbluemax585.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’ll only take a second." # @t_sbluemax586.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Unless you’re…" # @t_sbluemax587.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    extend " QUITE SCARED OF HEIGHTS!!!" # @t_sbluemax587.01 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_shocked as bluemax
    t_ch_max "AHH!" # @t_sbluemax588.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "NOT HEIGHTS, WHERE?!?!" # @t_sbluemax589.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "Ah-ha! I knew it." # @t_sbluemax590.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_flustered as bluemax
    t_ch_max "My secret shame revealed!" # @t_sbluemax591.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "No!" # @t_sbluemax592.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Why!" # @t_sbluemax593.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "How!" # @t_sbluemax594.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Well, it’s pretty obvious if you’re paying attention at all.)" # @t_sbluemax595.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s not the important part though." # @t_sbluemax595.01 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_worried as bluemax
    t_ch_max "What is then?" # @t_sbluemax596.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "YOU’RE A BIRD!!!" # @t_sbluemax597.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Don’t you think I know that!" # @t_sbluemax598.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I never heard of a bird afraid of flying." # @t_sbluemax599.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "There are many flightless birds." # @t_sbluemax5100.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I just happen to be one is all." # @t_sbluemax5101.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You don’t look like any penguin, emu, or ostrich I ever seen, Max." # @t_sbluemax5102.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Y-you don’t know. I could be!" # @t_sbluemax5103.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah, and I COULD be the King of Space." # @t_sbluemax5104.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But I ain’t!" # @t_sbluemax5105.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    extend " (I guess I could be one day, depends on how our crazy system of succession works.)" # @t_sbluemax5105.01 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " (But still! The point remains!)" # @t_sbluemax5105.02 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_worried as bluemax
    t_ch_max "Well, maybe I just don’t want to fly. What’s wrong with that?" # @t_sbluemax5106.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "You don’t want to fly?!" # @t_sbluemax5107.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You’re building an airplane SO HARD you’re in trouble for it!" # @t_sbluemax5108.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Uh." # @t_sbluemax5109.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Um." # @t_sbluemax5110.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Yeah. Kind of…" # @t_sbluemax5111.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "And then all the Military History stuff on top of that." # @t_sbluemax5112.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s an attempt to make yourself feel big and important when really you’re just little and scared." # @t_sbluemax5113.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_shocked as bluemax
    t_ch_max "SO WHAT IF IT IS?" # @t_sbluemax5114.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_serious as bluemax
    t_ch_max "Anyway, you can’t prove that." # @t_sbluemax5115.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I don’t need to." # @t_sbluemax5116.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Taira would scare anybody. He’s undead!" # @t_sbluemax5117.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But you don’t need to be scared of flying." # @t_sbluemax5118.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "But." # @t_sbluemax5119.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_worried as bluemax
    t_ch_max "It’s just." # @t_sbluemax5120.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax
    t_ch_max "What if I fell!" # @t_sbluemax5121.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "You can scrape your knee if you trip when you’re walking." # @t_sbluemax5122.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I bet you could break your neck if you tripped while flying!!!" # @t_sbluemax5123.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Man. I’m not getting through to this guy!)" # @t_sbluemax5124.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        pause 0.5 
        linear .25 xpos 0.08 
    show i_bluemax_stand_worried as bluemax:
        # ShowWithAtl
        pause 0.5 
        linear .25 xpos 0.32 
        xzoom -1.0 
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 3 xpos 0.8 
    extend "{w=3.0}{nw}"
    t_ch_cousin "Pac-Man!" # @t_sbluemax5125.00 self.block='Last'
    stop sound
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "What’re you doing up here?" # @t_sbluemax5126.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Imparting wisdom to the troubled youths of today, of course." # @t_sbluemax5127.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Blue Max." # @t_sbluemax5128.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "You’ve got to be true to yourself." # @t_sbluemax5129.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "But what does that mean?" # @t_sbluemax5130.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_pacman "It means you’re a bird." # @t_sbluemax5131.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "For you, falling IS flying." # @t_sbluemax5132.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "It’s a matter of aerodynamics and evolution." # @t_sbluemax5133.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "You mean…I don’t have to worry about hurting myself?" # @t_sbluemax5134.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stop_worried as bluemax
    t_ch_max "I don’t have to avoid confronting my fears by always thinking about military history and lingo and stuff so it looks like I’m totally not afraid to fly and maybe JUST MAYBE if everyone thinks I’m normal then I’ll think I’m normal too and I won’t have to think about how terrifying it is to fly all the time?" # @t_sbluemax5135.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Um. I think that’s a breakthrough?)" # @t_sbluemax5136.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Uh." # @t_sbluemax5137.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Sure, kid." # @t_sbluemax5138.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Just be true to yourself." # @t_sbluemax5139.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_serious as bluemax
    t_ch_max "Yeah." # @t_sbluemax5140.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_serious as bluemax
    t_ch_max "YEAH!" # @t_sbluemax5141.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I think I can do it!" # @t_sbluemax5142.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "I can fly!" # @t_sbluemax5143.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "[slot_playerName], I CAN FLY!" # @t_sbluemax5144.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I know." # @t_sbluemax5145.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You’re a bird." # @t_sbluemax5146.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Thank you, Pac-Man!" # @t_sbluemax5147.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Thank you, [slot_playerName]!" # @t_sbluemax5148.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "We really didn’t do anything." # @t_sbluemax5149.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "It’s just that you are LITERALLY A BIRD." # @t_sbluemax5150.00 self.block='Last'
    show i_sw_black as curtain zorder 10:
        # FadeEvent
        linear 1.0 alpha 1.0
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(We never did figure out how to get the designs back from the teachers’ vaults.)" # @t_sbluemax5151.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But if Blue Max can fly, then I guess it doesn’t matter!)" # @t_sbluemax5152.00 self.block='Last'
    # <NHSceneChange {'name': '_2e', 'scene': 's_day5.5'} NHSceneChange ''>
    label s_bluemax5__2e:
        # <NHSceneChange {'name': '_2e', 'scene': 's_day5.5'} NHSceneChange ''>
        jump s_day5p5