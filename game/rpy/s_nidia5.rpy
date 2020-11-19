# <Scene scene {'id': 's_nidia5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_nidia5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_nidia5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_nidia5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/sadtimes.ogg" loop
    show i_bg_library as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_pacman_left as pacman:
        default
        xpos 1.35 
    show i_cousin_default_sad as cousin zorder 2:
        default
        xpos 0.3 
    show i_nidia_akimbo_worried as nidia zorder 2:
        default
        xpos 0.7 
    t_ch_cousin "(Nidia's really distraught..." # @t_snidia511.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I want to say something..." # @t_snidia511.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But the atmosphere is so heavy...)" # @t_snidia511.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Nidia... I feel like there's something I'm missing here..." # @t_snidia512.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You said you had to combine with someone to save the world... I know the road will be hard, but it also sounds like..." # @t_snidia513.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Well, like a great adventure." # @t_snidia514.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "You're going to get to do and see so much." # @t_snidia515.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " But every once in a while your expression changes when you talk about it." # @t_snidia515.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Is there something you haven't said?" # @t_snidia516.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "[slot_playerName], I..." # @t_snidia517.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " ................" # @t_snidia517.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "It's okay... You don't have to talk about it. I just thought..." # @t_snidia518.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "No, I do." # @t_snidia519.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " [slot_playerName], I don't WANT to combine with anyone." # @t_snidia519.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_worried as nidia
    extend " But a prophecy is like a set of rules... For it to come true, you have to follow the guidelines." # @t_snidia519.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "It says I have to combine with someone, and I just... Don't want to. I mean, if that's what it takes to save the world, I will, but..." # @t_snidia520.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Go on...." # @t_snidia521.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "I have to save the world, [slot_playerName]. So I have to do what the prophecy says in order to fulfill it. But if the world IS saved... The last part of the prophecy says...." # @t_snidia522.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "..................." # @t_snidia523.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What does it say?" # @t_snidia524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "The prophecy says that in order to save the world... I have to die." # @t_snidia525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "WHAT!" # @t_snidia526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_nidia "I feel terrible complaining... I should rise to meet the challenge. The fate of the world is at stake." # @t_snidia527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "But it just feels so unfair..." # @t_snidia528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "It's TOTALLY unfair!" # @t_snidia529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Who wrote this stupid prophecy!" # @t_snidia529.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_angry as cousin
    extend " I'll roll them up and throw them into the sun!" # @t_snidia529.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " How do they like THAT prophecy!" # @t_snidia529.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_happy as nidia
    t_ch_nidia "Haha..." # @t_snidia530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_happy as nidia
    show i_cousin_default_surprised as cousin
    extend " Hahahahahaa!" # @t_snidia530.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " [slot_playerName]!" # @t_snidia530.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_happy_blush as nidia
    extend " Some ancient oracle is turning over in his grave right now!" # @t_snidia530.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Well, maybe they shouldn't have made such a dumb prophecy!" # @t_snidia531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "Hahahahaha! [slot_playerName]..." # @t_snidia532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "Hahahaha!" # @t_snidia533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_happy_blush as nidia
    extend " You're very sweet." # @t_snidia533.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "No! I'm mad! I'm super mad!" # @t_snidia534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "A prophecy is just a way to control a person! You have to do something because you fear the consequences." # @t_snidia535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It's so wrong!" # @t_snidia535.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_nidia "Thank you, [slot_playerName]." # @t_snidia536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_worried as nidia
    t_ch_nidia "Listen... I don't want you to feel sorry for me or anything. I'd hate that." # @t_snidia537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_worried as nidia
    show i_cousin_energetic_neutral as cousin
    extend " I know what I have to do." # @t_snidia537.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Still... I wish I knew what to say..." # @t_snidia538.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_surprised as nidia:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_pacman_left as pacman:
        # ShowWithAtl
        easeout 5 xpos 0.8 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.15 
    extend "{w=5.0}{nw}"
    t_ch_pacman "BE TRUE TO YOURSELF......." # @t_snidia539.00 self.block='Last'
    stop sound
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "But I have to be true to the prophecy..." # @t_snidia540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman ".... BE TRUE TO YOURSELF...." # @t_snidia541.00 self.block='Last'
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 5 xpos 1.35 
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    $ renpy.pause(0.5, hard=True) # Image change
    show i_cousin_default_grin as cousin
    $ renpy.pause(0.8, hard=True) # Text delay
    t_ch_cousin "Nidia... Pac-Man's right." # @t_snidia542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_worried as nidia
    extend " You always have a hard time deciding what to think." # @t_snidia542.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I know you think that's bad, but..." # @t_snidia543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You know what I think?" # @t_snidia543.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I think it means you believe in the power of possibility." # @t_snidia544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You always have more than one way of seeing a situation." # @t_snidia544.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Shouldn't you look at this prophecy the same way? Maybe it's not your life you have to question... But the prophecy itself." # @t_snidia545.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Maybe combining means accepting every part of yourself... The good AND the bad... And being happy with it." # @t_snidia545.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Maybe you don't NEED someone else to make the amulet work." # @t_snidia546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_happy as nidia
    t_ch_nidia "Maybe ... I'm free to choose... How to choose!" # @t_snidia547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You can choose to partner up with someone..." # @t_snidia548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Or not." # @t_snidia548.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It's completely up to you." # @t_snidia548.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Don't let some old book tell you how to live, Nidia." # @t_snidia549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "..................." # @t_snidia550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "[slot_playerName].........." # @t_snidia551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_happy_blush as nidia:
        xzoom 1.0 
    t_ch_nidia "Thank you." # @t_snidia552.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_14', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_nidia5__14:
        # <NHSceneChange NHSceneChange {'name': '_14', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5