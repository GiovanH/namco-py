# <Scene {'id': 's_nidia5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_nidia5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_nidia5"
    $ renpy.pause(1)
    # <Scene {'id': 's_nidia5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I want to say something..." # @t_snidia511.01 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But the atmosphere is so heavy...)" # @t_snidia511.02 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Nidia... I feel like there's something I'm missing here..." # @t_snidia512.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You said you had to combine with someone to save the world... I know the road will be hard, but it also sounds like..." # @t_snidia513.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Well, like a great adventure." # @t_snidia514.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "You're going to get to do and see so much." # @t_snidia515.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " But every once in a while your expression changes when you talk about it." # @t_snidia515.01 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Is there something you haven't said?" # @t_snidia516.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "[slot_playerName], I..." # @t_snidia517.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ................" # @t_snidia517.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "It's okay... You don't have to talk about it. I just thought..." # @t_snidia518.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "No, I do." # @t_snidia519.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " [slot_playerName], I don't WANT to combine with anyone." # @t_snidia519.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_worried as nidia
    extend " But a prophecy is like a set of rules... For it to come true, you have to follow the guidelines." # @t_snidia519.02 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "It says I have to combine with someone, and I just... Don't want to. I mean, if that's what it takes to save the world, I will, but..." # @t_snidia520.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Go on...." # @t_snidia521.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "I have to save the world, [slot_playerName]. So I have to do what the prophecy says in order to fulfill it. But if the world IS saved... The last part of the prophecy says...." # @t_snidia522.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "..................." # @t_snidia523.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What does it say?" # @t_snidia524.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "The prophecy says that in order to save the world... I have to die." # @t_snidia525.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "WHAT!" # @t_snidia526.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_nidia "I feel terrible complaining... I should rise to meet the challenge. The fate of the world is at stake." # @t_snidia527.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "But it just feels so unfair..." # @t_snidia528.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "It's TOTALLY unfair!" # @t_snidia529.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Who wrote this stupid prophecy!" # @t_snidia529.01 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    extend " I'll roll them up and throw them into the sun!" # @t_snidia529.02 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How do they like THAT prophecy!" # @t_snidia529.03 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_happy as nidia
    t_ch_nidia "Haha..." # @t_snidia530.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_happy as nidia
    show i_cousin_default_surprised as cousin
    extend " Hahahahahaa!" # @t_snidia530.01 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " [slot_playerName]!" # @t_snidia530.02 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_happy_blush as nidia
    extend " Some ancient oracle is turning over in his grave right now!" # @t_snidia530.03 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well, maybe they shouldn't have made such a dumb prophecy!" # @t_snidia531.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Hahahahaha! [slot_playerName]..." # @t_snidia532.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "Hahahaha!" # @t_snidia533.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_happy_blush as nidia
    extend " You're very sweet." # @t_snidia533.01 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "No! I'm mad! I'm super mad!" # @t_snidia534.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "A prophecy is just a way to control a person! You have to do something because you fear the consequences." # @t_snidia535.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It's so wrong!" # @t_snidia535.01 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_nidia "Thank you, [slot_playerName]." # @t_snidia536.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_worried as nidia
    t_ch_nidia "Listen... I don't want you to feel sorry for me or anything. I'd hate that." # @t_snidia537.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_worried as nidia
    show i_cousin_energetic_neutral as cousin
    extend " I know what I have to do." # @t_snidia537.01 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Still... I wish I knew what to say..." # @t_snidia538.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "But I have to be true to the prophecy..." # @t_snidia540.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman ".... BE TRUE TO YOURSELF...." # @t_snidia541.00 self.block='Last'
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 5 xpos 1.35 
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_worried as nidia:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    $ renpy.pause(0.5) # Image change
    show i_cousin_default_grin as cousin
    extend "{w=0.8}{nw}"
    t_ch_cousin "Nidia... Pac-Man's right." # @t_snidia542.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_worried as nidia
    extend " You always have a hard time deciding what to think." # @t_snidia542.01 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I know you think that's bad, but..." # @t_snidia543.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You know what I think?" # @t_snidia543.01 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I think it means you believe in the power of possibility." # @t_snidia544.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You always have more than one way of seeing a situation." # @t_snidia544.01 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Shouldn't you look at this prophecy the same way? Maybe it's not your life you have to question... But the prophecy itself." # @t_snidia545.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Maybe combining means accepting every part of yourself... The good AND the bad... And being happy with it." # @t_snidia545.01 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Maybe you don't NEED someone else to make the amulet work." # @t_snidia546.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_clasped_happy as nidia
    t_ch_nidia "Maybe ... I'm free to choose... How to choose!" # @t_snidia547.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You can choose to partner up with someone..." # @t_snidia548.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or not." # @t_snidia548.01 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It's completely up to you." # @t_snidia548.02 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Don't let some old book tell you how to live, Nidia." # @t_snidia549.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "..................." # @t_snidia550.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "[slot_playerName].........." # @t_snidia551.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_happy_blush as nidia:
        xzoom 1.0 
    t_ch_nidia "Thank you." # @t_snidia552.00 self.block='Last'
    # <NHSceneChange {'name': '_14', 'scene': 's_day5.5'} NHSceneChange ''>
    label s_nidia5__14:
        # <NHSceneChange {'name': '_14', 'scene': 's_day5.5'} NHSceneChange ''>
        jump s_day5p5