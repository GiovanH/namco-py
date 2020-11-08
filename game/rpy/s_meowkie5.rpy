# <Scene {'id': 's_meowkie5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_meowkie5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_meowkie5"
    $ renpy.pause(1)
    # <Scene {'id': 's_meowkie5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/romance.ogg" loop
    show i_bg_cafe as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_pacman_left as pacman zorder 2:
        default
        xpos 1.35 
        alpha 0.0
    show i_meowkie_normal_normal as meowkie zorder 2:
        default
        xpos 0.7 
    show i_mc_normal as mc zorder 2:
        default
        xpos 1.49 
        alpha 1.0
    t_ch_cousin "(The rest of detention passed pretty quickly…" # @t_smeowkie518.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I was barely paying attention at all." # @t_smeowkie518.01 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "How could I, knowing I would be here at the cafe soon, on a date with Meowkie?" # @t_smeowkie519.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    with Dissolve(0.3)
    t_ch_cousin "...It IS a real date, right?" # @t_smeowkie520.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Well, either way, we should talk..." # @t_smeowkie521.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s now or never, I guess.)" # @t_smeowkie521.01 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal as meowkie:
        xzoom -1.0 
    t_ch_meowkie "Hey look Boss! They have the seafood special today!" # @t_smeowkie522.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah! And look..." # @t_smeowkie523.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " It says it comes half price..." # @t_smeowkie523.01 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    with Dissolve(0.3)
    extend " If you order it on a date." # @t_smeowkie523.02 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "The “Lovebird Discount.”" # @t_smeowkie524.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_alert as meowkie
    t_ch_meowkie "…" # @t_smeowkie525.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_alert as meowkie
    extend " So Boss..." # @t_smeowkie525.01 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile as meowkie
    extend " This is really... a real date?" # @t_smeowkie525.02 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Yes it is, Meowkie. Because the truth is... I like you." # @t_smeowkie5x_choice2 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie526.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy as meowkie
    extend " That’s nice of you to say..." # @t_smeowkie526.01 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal as meowkie
    t_ch_meowkie "Heh, Boss. It’s sweet of you... the lengths you’ll go to cheer me up." # @t_smeowkie527.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I really mean it though!" # @t_smeowkie528.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie529.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Somehow, I get the sense that she doesn’t quite believe me..." # @t_smeowkie530.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But why not? I didn’t really think about it until tonight, but…" # @t_smeowkie531.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    with Dissolve(0.3)
    t_ch_cousin "I know how I feel when I look at her." # @t_smeowkie532.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie...)" # @t_smeowkie533.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal as meowkie:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    show i_mc_normal as mc:
        # ShowWithAtl
        linear 0.333 xpos 0.8 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.15 
    extend "{w=0.333}{nw}"
    t_ch_waiter "Good evening! And what will we be having tonight?" # @t_smeowkie536.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "O-oh... we’re sharing the seafood special, I guess?" # @t_smeowkie537.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_waiter "Good choice." # @t_smeowkie538.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    show i_mc_normal as mc:
        # ShowWithAtl
        linear 0.333 xpos 1.5 
    show i_meowkie_normal_normal as meowkie:
        # ShowWithAtl
        linear 0.333 xpos 0.7 
    extend "{w=0.333}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal as meowkie:
        xzoom -1.0 
    t_ch_meowkie "...So, Boss..." # @t_smeowkie539.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Yes?" # @t_smeowkie540.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "That rolling up stuff you like to do... is it fun?" # @t_smeowkie541.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh! Yeah, I guess so..." # @t_smeowkie542.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s kinda why I got into trouble in the first place though." # @t_smeowkie542.01 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Why do you ask?" # @t_smeowkie542.02 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal as meowkie
    t_ch_meowkie "I just figured... I should look at this as an opportunity!" # @t_smeowkie543.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_grin as meowkie
    t_ch_meowkie "Now that I ain’t a Hall Monitor no more, I got time for other hobbies." # @t_smeowkie543.01 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Rolling up stuff like you do... It might be fun! Maybe you could teach me sometime." # @t_smeowkie543.02 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "But Meowkie... you love being a Hall Monitor!" # @t_smeowkie544.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile as meowkie
    t_ch_meowkie "…" # @t_smeowkie545.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Yeah, b-but..." # @t_smeowkie546.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " No use crying over spilled milk! Eh, Boss?" # @t_smeowkie546.01 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_smeowkie547.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile as meowkie
    t_ch_meowkie "Look... I know you think I oughta be, um, angry." # @t_smeowkie548.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile as meowkie
    extend " And I know those other kids get me in trouble on purpose." # @t_smeowkie548.01 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m not stupid!" # @t_smeowkie548.02 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile as meowkie
    t_ch_meowkie "I know what they think of me." # @t_smeowkie549.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown as meowkie
    extend " They think I’m bad and I deserve to go to detention anyway." # @t_smeowkie549.01 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "So why don’t you ever speak up? Doesn’t it make you angry?" # @t_smeowkie550.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I’m not angry at them!" # @t_smeowkie551.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m not!" # @t_smeowkie551.01 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Stop asking me that!" # @t_smeowkie552.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "But... but why not?" # @t_smeowkie553.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’d be angry if I were you!" # @t_smeowkie553.01 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Because... because..." # @t_smeowkie554.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Because I just can’t do it, okay?" # @t_smeowkie555.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie..." # @t_smeowkie556.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Boss... I mean, [slot_playerName]." # @t_smeowkie557.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Being angry is... bad." # @t_smeowkie558.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You yell, and you argue..." # @t_smeowkie558.01 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown as meowkie
    extend " You forget to be nice." # @t_smeowkie558.02 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "My parents sent me here..." # @t_smeowkie559.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So I could grow up to be good." # @t_smeowkie559.01 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "If I get angry..." # @t_smeowkie560.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If I stop being nice and good..." # @t_smeowkie560.01 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown as meowkie
    extend " Then everything they did was for nothing!" # @t_smeowkie560.02 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "That’s why I can’t get angry..." # @t_smeowkie561.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile as meowkie
    extend " besides..." # @t_smeowkie561.01 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "It’ll just prove... that everyone was right about me after all." # @t_smeowkie562.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But... what do you do, then?" # @t_smeowkie563.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You can’t be happy ALL the time, if people treat you so badly..." # @t_smeowkie563.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Maybe..." # @t_smeowkie564.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal as meowkie
    t_ch_meowkie "Maybe they’re right to treat me that way..." # @t_smeowkie565.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "What?!" # @t_smeowkie566.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How could you say that?!" # @t_smeowkie566.01 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy as meowkie
    t_ch_meowkie "N-nevermind... haha, it’s pretty silly of me." # @t_smeowkie567.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just forget it." # @t_smeowkie567.01 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "…" # @t_smeowkie568.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Anyway... even if what you’re saying is true..." # @t_smeowkie569.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy as meowkie
    extend " It doesn’t matter, because I don’t get angry at all!" # @t_smeowkie569.01 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Sorry! Heh!" # @t_smeowkie569.02 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "But... you can’t just not get angry." # @t_smeowkie570.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s impossible." # @t_smeowkie572.01 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Any more than you can stop yourself from laughing at something really funny." # @t_smeowkie572.02 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Or..." # @t_smeowkie573.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad_blush as cousin
    with Dissolve(0.3)
    t_ch_cousin "Or from having a crush on someone..." # @t_smeowkie574.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Who you really, really like." # @t_smeowkie574.01 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy as meowkie
    t_ch_meowkie "…" # @t_smeowkie575.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy as meowkie
    t_ch_meowkie "Gee, Boss... I’m sorry I’m being such a downer! Heh!" # @t_smeowkie576.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Ignoring what I said about the crush, huh...)" # @t_smeowkie577.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal as meowkie
    t_ch_meowkie "That’s probably why... it’s good I’m not a Hall Monitor anymore." # @t_smeowkie578.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " A great Monitor never lets her personal problems get in the way of her confidence and focus!" # @t_smeowkie578.01 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Meowkie... just pretending to be happy all the time..." # @t_smeowkie579.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That isn’t an answer." # @t_smeowkie579.01 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_waiter "Here’s your seafood special, lovebirds." # @t_smeowkie580.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Yikes. Bad timing.)" # @t_smeowkie581.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh, thank you sir." # @t_smeowkie582.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie583.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh... Hey Meowkie, look." # @t_smeowkie584.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " There’s tons of tuna in here!" # @t_smeowkie584.01 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You love that stuff." # @t_smeowkie584.02 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy as meowkie
    t_ch_meowkie "Thank you Boss... I mean [slot_playerName]." # @t_smeowkie585.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Thank you for taking me on a nice date." # @t_smeowkie585.01 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Whoah, why are you standing up all of a sudden?" # @t_smeowkie586.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie..." # @t_smeowkie587.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile as meowkie
    t_ch_meowkie "It was really, um, really nice of you." # @t_smeowkie588.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I’ve had a great time hanging out with you..." # @t_smeowkie589.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The best time I’ve had since I came to this school." # @t_smeowkie589.01 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If that’s, um... okay to say." # @t_smeowkie589.02 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "But... I think I really should be going now..." # @t_smeowkie590.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "It’s not your fault..." # @t_smeowkie591.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s mine, like it always is." # @t_smeowkie591.01 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "So, goodbye, um, I guess." # @t_smeowkie592.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Meowkie, wait-" # @t_smeowkie593.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile as meowkie
    t_ch_meowkie "It’s okay if you don’t want to hang out anymore..." # @t_smeowkie594.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I completely understand..." # @t_smeowkie594.01 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_forcedsmile as meowkie
    extend " if you don’t want to waste your time on... someone like me." # @t_smeowkie594.02 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie, I don’t understand why you say these things!" # @t_smeowkie5x_choice5 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I’m sorry…" # @t_smeowkie597.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    stop music fadeout 1.0
    t_ch_meowkie "I gotta go." # @t_smeowkie598.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_forcedsmile as meowkie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mc_normal as mc:
        # ShowWithAtl
        linear 0.333 xpos 0.7 
    extend "{w=0.333}{nw}"
    t_ch_waiter "How’s that lovebird special coming-" # @t_smeowkie599.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Oh, it’s just you." # @t_smeowkie599.01 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_waiter "What happened to your date?" # @t_smeowkie5100.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "She, um…" # @t_smeowkie5101.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "She just left." # @t_smeowkie5102.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_waiter "YIKES. That’s rough." # @t_smeowkie5103.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Tell you what- it’s on the house." # @t_smeowkie5103.01 self.block='Last'
    show i_mc_normal as mc:
        # ShowWithAtl
        easein 0.5 xpos 1.5 
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    hide mc
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(...Small comfort." # @t_smeowkie5104.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I can’t believe she left before I could even say another word." # @t_smeowkie5105.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Sigh..." # @t_smeowkie5105.01 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I don’t care what she says." # @t_smeowkie5106.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If she left without eating a single bite of all this tuna..." # @t_smeowkie5106.01 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "She’s gotta be feeling really angry.)" # @t_smeowkie5107.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': 'enterPacman'} ParallelEvent ''>
    label s_meowkie5_enterPacman:
        # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': 'enterPacman'} ParallelEvent ''>
        # <Events {} events ''>
        show i_pacman_left as pacman:
            # ShowWithAtl
            linear 0.5 alpha 1.0
            # ShowWithAtl
            easeout 5 xpos 0.8 
        extend "{w=5.0}{nw}"
        # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    stop sound
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "...I can help you finish that." # @t_smeowkie5108.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Oh, hi, Pac-Man." # @t_smeowkie5109.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m glad you’re here..." # @t_smeowkie5109.01 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I really need someone to talk to." # @t_smeowkie5109.02 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I had a date, but..." # @t_smeowkie5110.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " It really didn’t go well." # @t_smeowkie5110.01 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I was just thinking..." # @t_smeowkie5111.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I know Meowkie gets angry just like the rest of us." # @t_smeowkie5112.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And if the other students are so awful to her all the time..." # @t_smeowkie5112.01 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Then she must be angry inside all the time." # @t_smeowkie5113.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But..." # @t_smeowkie5114.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " if she thinks being angry really is bad..." # @t_smeowkie5114.01 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Then she must think that the other students are right." # @t_smeowkie5115.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She must think she really is bad on the inside." # @t_smeowkie5115.01 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "When she got that Hall Monitor badge, she must have felt like it was proof." # @t_smeowkie5116.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Proof that she was good." # @t_smeowkie5116.01 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But without it, there’s nothing to stop her from thinking she’s bad..." # @t_smeowkie5116.02 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie... she shouldn’t need that badge to feel good." # @t_smeowkie5117.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She is good! No matter what!" # @t_smeowkie5117.01 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "She’s the nicest, strongest person I know! She really cares, and she tries her hardest all the time! No matter what!" # @t_smeowkie5118.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "(Chew, chew…)" # @t_smeowkie5119.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "There’s only one thing to do in a situation like this, [slot_playerName]…" # @t_smeowkie5120.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "(Chew, chew…)" # @t_smeowkie5121.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Be chew to yourself." # @t_smeowkie5122.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I MEAN, true to yourself." # @t_smeowkie5122.01 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Be true to yourself." # @t_smeowkie5123.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "… Yeah..." # @t_smeowkie5124.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Yeah, you’re right." # @t_smeowkie5124.01 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If I can be true to myself and my feelings..." # @t_smeowkie5125.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Maybe she can be true to her feelings too." # @t_smeowkie5126.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "This is really good tuna." # @t_smeowkie5127.00 self.block='Last'
    # <NHSceneChange {'name': '_2i', 'scene': 's_day5.5'} NHSceneChange ''>
    label s_meowkie5__2i:
        # <NHSceneChange {'name': '_2i', 'scene': 's_day5.5'} NHSceneChange ''>
        jump s_day5p5