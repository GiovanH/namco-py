# <Scene {'id': 's_mrdriller5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_mrdriller5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_mrdriller5"
    $ renpy.pause(1)
    # <Scene {'id': 's_mrdriller5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_mrdriller5_initialize:
        # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
        # <Events {} events ''>
        play music "bgm/privatetimes.ogg" loop
        show i_bg_rooftop as bg zorder 0 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_cousin_default_neutral as cousin zorder 2:
            default
            xpos 0.25 
        show i_mrdriller_standing_sad as mrdriller zorder 1:
            default
            xpos 0.75 
        show i_pacman_left as pacman zorder 2:
            default
            xpos 1.49 
            alpha 1.0

    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(So I agreed to meet with Mr. Driller on…)" # @t_smrdriller522.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "The rooftop?" # @t_smrdriller523.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Why did you want to meet up here?" # @t_smrdriller524.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "I guess I just wanted to go somewhere that was as far away from the ground as possible." # @t_smrdriller525.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "The ground…" # @t_smrdriller526.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It has too many bad memories." # @t_smrdriller526.01 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Yeah…" # @t_smrdriller527.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I guess the roof would be the place to go, then." # @t_smrdriller527.01 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "I wish I could remember the good stuff about digging too…" # @t_smrdriller528.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But now when I look at dirt… all I can remember is how crazy I got." # @t_smrdriller528.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "I never thought digging could be so…" # @t_smrdriller529.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " destructive." # @t_smrdriller529.01 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "I miss it, but… it’s better this way." # @t_smrdriller530.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Yeah, but… you didn’t know the pipe was there." # @t_smrdriller531.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    extend " If you’d known, I bet you would’ve stopped and gone around it." # @t_smrdriller531.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "If it hadn’t been there…" # @t_smrdriller532.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Your digging wouldn’t have hurt anything, and we wouldn’t be having this conversation." # @t_smrdriller533.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "But it was there, and what happened DID happen." # @t_smrdriller534.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "And a part of me was happy that Dad’s statue got destroyed, even if it was an accident…" # @t_smrdriller535.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_cry as mrdriller
    extend " I can’t deal with that!" # @t_smrdriller535.01 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "There’s no point in wondering about it…" # @t_smrdriller536.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just like Dad’s digging…" # @t_smrdriller536.01 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "It really did break up our family." # @t_smrdriller537.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Mom left because Dad wouldn’t stop digging long enough to pay her any attention." # @t_smrdriller537.01 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s no use trying to cover that up." # @t_smrdriller537.02 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s just what it is." # @t_smrdriller537.03 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Wow… I’m so sorry…" # @t_smrdriller538.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’ve got a big family, but…" # @t_smrdriller539.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If any of them left, I’d be devastated." # @t_smrdriller539.01 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "You know, after all the time we spent together, I never told you my real, main reason for digging." # @t_smrdriller540.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "I don’t even know why I kept it a secret..." # @t_smrdriller541.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I guess because it has to do with Dad, and…" # @t_smrdriller541.01 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I was feeling too bad about stuff to want to think about him." # @t_smrdriller541.02 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "I’m glad you can at least admit that, now…" # @t_smrdriller542.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(It’s a little less disturbing this way.)" # @t_smrdriller543.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "It’s kind of silly, actually." # @t_smrdriller544.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_happy as mrdriller
    extend " The main reason I like digging is just because I have such good memories of digging with my dad when I was a little kid." # @t_smrdriller544.01 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "He’d bury things like little toys and coins for me to find and dig up with my plastic shovel." # @t_smrdriller545.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It was just so fun running around the yard like that…" # @t_smrdriller545.01 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_handsup_happy as mrdriller
    t_ch_mrdriller "I know it’s not anything big or inspirational, like a famous archaeology dig or anything…" # @t_smrdriller546.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But that’s really the reason why digging is so important to me." # @t_smrdriller546.01 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "I’ll remember it for the rest of my life, even if I never dig again." # @t_smrdriller547.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "I don’t think that’s silly at all." # @t_smrdriller548.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s a great reason to love digging." # @t_smrdriller548.01 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " And if something makes you feel that way, you shouldn’t give it up." # @t_smrdriller548.02 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "Are you sure?" # @t_smrdriller549.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "Maybe it’s better to give something up if it causes destruction." # @t_smrdriller550.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That’s what I thought too…" # @t_smrdriller551.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "About rolling my katamari." # @t_smrdriller552.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I tried to pretend I didn’t have a passion for it, like you do for digging, but..." # @t_smrdriller553.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " When I rolled that katamari for the first time, I loved it more than anything." # @t_smrdriller553.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I thought it was better to put it away, since I caused so much trouble with it." # @t_smrdriller554.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But now I think…" # @t_smrdriller555.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " It’s better to keep trying, and I’ll do a better job next time with practice." # @t_smrdriller555.01 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " And maybe you can do that too…" # @t_smrdriller555.02 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " Maybe you just need more practice." # @t_smrdriller555.03 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "But… what about my dad?" # @t_smrdriller556.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "He’d be so disappointed if I picked up my drills again…" # @t_smrdriller557.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Even if it was just for practice." # @t_smrdriller557.01 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Your dad is jerk! Who cares what he thinks!" # @t_smrdriller558.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_shock as mrdriller
    t_ch_mrdriller "H-how can you say that?" # @t_smrdriller559.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_shock as mrdriller
    extend " How can you sit there and tell me my dad is a jerk?" # @t_smrdriller559.01 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Come on!" # @t_smrdriller560.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He tries to stifle your passion, he tells you you’re wrong and bad…" # @t_smrdriller560.01 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I know you love him… But you kinda hate him a little bit too, right?" # @t_smrdriller561.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "I just got done telling you about how the reason digging means so much to me…" # @t_smrdriller562.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "Is because of how much I love my dad." # @t_smrdriller563.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "How can you be so insensitive?" # @t_smrdriller564.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "C’mon, man." # @t_smrdriller565.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Don’t bury it down like he does!" # @t_smrdriller565.01 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "… You’re right…" # @t_smrdriller566.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "I do kind of hate my dad." # @t_smrdriller567.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_cry as mrdriller
    extend " I must, since I destroyed the statue of him…" # @t_smrdriller567.01 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "I’m… I’m a terrible person!" # @t_smrdriller568.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "No you aren’t!" # @t_smrdriller569.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You can love someone and hate stuff they do to you at the same time!" # @t_smrdriller569.01 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I hate to say it, but…" # @t_smrdriller570.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    t_ch_cousin "Your dad is not being a good father!" # @t_smrdriller571.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    extend " You don’t have to pretend he is just because he’s family." # @t_smrdriller571.01 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "So that’s it? What do I do now?" # @t_smrdriller572.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Disown my father?" # @t_smrdriller572.01 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "No, man! I’m not saying you have to go that far!" # @t_smrdriller573.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Even fathers can make mistakes…" # @t_smrdriller574.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " Maybe there’s still time to fix it." # @t_smrdriller574.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "I don’t know how to fix stuff." # @t_smrdriller575.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I just know how to dig stuff up." # @t_smrdriller575.01 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "You’re his son!" # @t_smrdriller576.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " He obviously cares about you…" # @t_smrdriller576.01 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " He’s just doing a REALLY bad job of showing it." # @t_smrdriller576.02 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And he’s probably afraid of losing you, like he lost your mom." # @t_smrdriller577.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_shock as mrdriller
    t_ch_mrdriller "Afraid of losing ME?!" # @t_smrdriller578.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Of course! And… you love digging SO much." # @t_smrdriller579.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You shouldn’t have to give that up for anything." # @t_smrdriller579.01 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "And it’s like you said… Digging is about discovery." # @t_smrdriller580.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I know you can discover a way to keep digging, with passion AND moderation…" # @t_smrdriller581.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So you won’t destroy things anymore." # @t_smrdriller581.01 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "Maybe…" # @t_smrdriller582.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_happy as mrdriller
    extend " Maybe I could even help Dad discover that for himself as well…" # @t_smrdriller582.01 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If he’s anything like me…" # @t_smrdriller582.02 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_handsup_happy as mrdriller
    t_ch_mrdriller "I bet he misses digging too." # @t_smrdriller583.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I bet he’ll even want to dig together with you again." # @t_smrdriller584.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_handsup_sad as mrdriller
    t_ch_mrdriller "[slot_playerName]…" # @t_smrdriller585.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_handsup_cry as mrdriller
    extend " You’re gonna make me cry…" # @t_smrdriller585.01 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Be true to yourself!" # @t_smrdriller586.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_shock as mrdriller:
        # ShowWithAtl
        ease_expo .33 xpos 0.42 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        ease_expo .33 xpos 0.11 
    show i_pacman_left as pacman:
        # ShowWithAtl
        pause 0.33 
        linear 3 xpos 0.88 
    $ renpy.pause(3.33) # TimedPause
    stop sound
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_shock as mrdriller
    t_ch_mrdriller "Really, Pac-Man? You think I should?" # @t_smrdriller587.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "A-alright! Yeah! I lost my way for a second there…" # @t_smrdriller588.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_handsup_excited as mrdriller
    extend " But I definitely will!" # @t_smrdriller588.01 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Thanks, Pac-Man! He really needed that." # @t_smrdriller589.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "[slot_playerName], it’s not just me." # @t_smrdriller590.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’ve got to be true to yourself too!" # @t_smrdriller590.01 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "You gotta get your katamari back from the confiscated weapons locker…" # @t_smrdriller591.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_handsup_happy as mrdriller
    t_ch_mrdriller "And you gotta roll it again someday." # @t_smrdriller592.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "Promise?" # @t_smrdriller593.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Y-yeah… I will…" # @t_smrdriller594.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Thanks, Mr. Driller…" # @t_smrdriller595.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "I uh… I hope you know I really care about you." # @t_smrdriller596.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_excited as mrdriller
    t_ch_mrdriller "Of course I know…" # @t_smrdriller597.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_smug as mrdriller
    t_ch_mrdriller "You didn’t keep that buried as well as you thought you did." # @t_smrdriller598.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    show i_mrdriller_standing_smug as mrdriller:
        # ShowWithAtl
        linear .25 xpos 0.4 
    extend "{w=0.25}{nw}"
    t_ch_cousin "(He’s leaning in awfully close to me…" # @t_smrdriller599.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_smug as mrdriller:
        # ShowWithAtl
        linear .25 xpos 0.38 
    extend "{w=0.25}{nw}"
    extend " I think… we’re finally going to…" # @t_smrdriller599.01 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_smug as mrdriller:
        # ShowWithAtl
        linear .25 xpos 0.36 
    extend "{w=0.25}{nw}"
    extend " To…!)" # @t_smrdriller599.02 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_slumped_shock as mrdriller:
        # ShowWithAtl
        linear .25 xpos 0.42 
    show i_cousin_energetic_surprise_blush as cousin
    extend "{w=0.25}{nw}"
    t_ch_pacman "Ahem!" # @t_smrdriller5100.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Get a room, you two." # @t_smrdriller5100.01 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mrdriller_standing_happy as mrdriller:
        # ShowWithAtl
        pause 2.0 
        ease_expo .5 xpos 0.75 
    show i_cousin_default_neutral_blush as cousin:
        # ShowWithAtl
        pause 2.0 
        ease_expo .5 xpos 0.25 
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 3 xpos 1.5 
    $ renpy.pause(3.0) # TimedPause
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "Eh heh heh… Uh…." # @t_smrdriller5101.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I guess now’s not… the best time.. for, uh..." # @t_smrdriller5101.01 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mrdriller "Um, I guess I’ll see you tomorrow, [slot_playerName]!" # @t_smrdriller5102.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(...Some discoveries…" # @t_smrdriller5103.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "We can leave for later.)" # @t_smrdriller5104.00 self.block='Last'
    # <NHSceneChange {'name': '_29', 'scene': 's_day5.5'} NHSceneChange ''>
    label s_mrdriller5__29:
        # <NHSceneChange {'name': '_29', 'scene': 's_day5.5'} NHSceneChange ''>
        jump s_day5p5