# <Scene {'id': 's_donko5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_donko5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_donko5"
    $ renpy.pause(1)
    # <Scene {'id': 's_donko5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/school.ogg" loop
    show i_bg_classroom_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 4:
        default
        xpos 0.25 
    show i_donko_default_crying as donko zorder 2:
        default
        xpos 0.75 
    show i_taira_steveholt_happy as taira zorder 2:
        default
        alpha 0.0
        xpos 0.75 
    show i_galaga_default as galaga zorder 2:
        default
        alpha 0.0
        xpos 0.75 
    show i_pacman_left as pacman zorder 2:
        default
        xpos 1.38 
    show i_aki_default_smile as aki zorder 2:
        default
        alpha 0.0
        xpos 0.75 
    t_ch_donko "...People give me presents and stuff like that, like, all the time." # @t_sdonko520.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "It’s all because they want me to like them." # @t_sdonko521.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Maybe this sounds silly, but… It gets to be, like, kinda depressing, yknow?" # @t_sdonko521.01 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "But this time, this gift…" # @t_sdonko522.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I can like… totally feel it’s real." # @t_sdonko523.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...Thank you, [slot_playerName]." # @t_sdonko523.01 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Donko… you really do understand!" # @t_sdonko524.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Besides, going to a cool concert with ME…" # @t_sdonko525.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_grin as donko
    extend " I can only imagine what that’ll do for YOUR popularity!" # @t_sdonko525.01 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    show i_donko_default_wink as donko
    t_ch_donko "Very clever, honey!" # @t_sdonko526.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I think you’re finally starting to learn!" # @t_sdonko526.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "You’re gonna be more popular than EVER!" # @t_sdonko527.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Huh?" # @t_sdonko528.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Wait!" # @t_sdonko528.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But that’s not why I-" # @t_sdonko528.02 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "I better go get ready. Thanks again!" # @t_sdonko529.00 self.block='Last'
    show i_donko_ygg_wink as donko:
        # ShowWithAtl
        linear .33 alpha 0.0
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(..." # @t_sdonko530.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "Does Donko even… understand why I did that?" # @t_sdonko531.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Does she understand that I’m doing it so we can…" # @t_sdonko532.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh, well." # @t_sdonko533.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s no way to miss the signals I’m giving her, right?)" # @t_sdonko533.01 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_pacman "Be true to yourself!" # @t_sdonko534.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 3 xpos 0.83 
    stop sound
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Huh?! Pac-Man?!" # @t_sdonko535.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "I said, be true to yourself! It’s the only way to understand your feelings for Donko!" # @t_sdonko536.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Huh…" # @t_sdonko537.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Well, I don’t know how you knew what I was thinking about…" # @t_sdonko537.01 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "I have my ways." # @t_sdonko538.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "...Right…" # @t_sdonko539.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Anyway…" # @t_sdonko539.01 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I don’t really know what you mean." # @t_sdonko540.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How am I not being true to myself?" # @t_sdonko540.01 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "You know in your heart how you feel about Donko." # @t_sdonko541.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "And I think you know deep down, Donko feels the same!" # @t_sdonko542.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "So why do you keep doubting her and ignoring how you feel?" # @t_sdonko543.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "It’s… kinda weird that you know so much about this…" # @t_sdonko544.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well, whatever." # @t_sdonko545.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s not MY fault I’m doubting how I feel! It’s her’s!" # @t_sdonko545.01 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    extend " She straight-up admitted how manipulative she is." # @t_sdonko545.02 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And lately it seems like whenever I try to confront her, she pretends not to get it." # @t_sdonko546.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " It’s so annoying!" # @t_sdonko546.01 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Please remember that growing up as a young drum can be very difficult, [slot_playerName]." # @t_sdonko547.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "I was young once, and I may not be a drum…" # @t_sdonko548.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "But I am vaguely circle-shaped." # @t_sdonko549.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So it’s basically the same thing." # @t_sdonko549.01 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Donko may seem to have an easy life, but do you think that’s completely true?" # @t_sdonko550.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I don’t know!" # @t_sdonko551.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " It seems pretty easy to me." # @t_sdonko551.01 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " Everyone likes her and she always gets whatever she wants." # @t_sdonko551.02 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "You’re being awfully hard on her." # @t_sdonko552.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Be true to what you really feel, [slot_playerName]…" # @t_sdonko552.01 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "It’s hard to be her. If you like her, trust her to open up to you eventually." # @t_sdonko553.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Pac-Man, it’s not that I don’t appreciate your advice, it just seems..." # @t_sdonko554.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "Well you’re not the one who actually has to deal with her, you know?" # @t_sdonko555.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So this is all pretty rich, coming from you!" # @t_sdonko555.01 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "You mean… BUDDY Rich?!" # @t_sdonko556.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Huh?" # @t_sdonko557.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "He’s… a famous… drummer…" # @t_sdonko558.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " See, because, Donko is… you know..." # @t_sdonko558.01 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "It’s one of those… drum.. puns…" # @t_sdonko559.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "You might be… too young… to get it…" # @t_sdonko560.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_sdonko561.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        pause 0.7 
        linear 3 xpos 1.38 
    extend "{w=3.7}{nw}"
    t_ch_pacman "I’ll see myself out." # @t_sdonko562.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I don’t really get what Pac-Man was trying to tell me…" # @t_sdonko563.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’ll have to ask him about it later. I’m sure nothing tragic and surprising will happen to prevent me from doing that." # @t_sdonko564.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    stop music fadeout 1.0
    t_ch_cousin "..." # @t_sdonko565.00 self.block='Last'
    show i_sw_black as curtain2 zorder 9:
        default
        alpha 0.0
        # FadeEvent
        linear 1.0 alpha 1.0
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "The rest of the school day passes uneventfully." # @t_sdonko566.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " All I can think about is my date with Donko tonight." # @t_sdonko566.01 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "...I hope it’s a date, anyway…" # @t_sdonko567.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Finally, it comes time to head to the cafe for the concert." # @t_sdonko567.01 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    t_ch_cousin "There, ready to meet me, is Donko…)" # @t_sdonko568.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_cafe as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_cafe', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_1E'} SettingChange ''>
    # <Events {} events ''>
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_donko_default_grin as donko:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_donko "Hi [slot_playerName]!" # @t_sdonko569.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Wow, what’d you do?" # @t_sdonko570.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Come here straight from school without even like, getting changed?" # @t_sdonko571.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Haha! Maybe I don’t have to get dressed up…" # @t_sdonko571.01 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "To look" # @t_sdonko571.02 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_scarf as cousin
    t_ch_cousin "good." # @t_sdonko571.03 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko
    t_ch_donko "Tee-hee!" # @t_sdonko572.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’ve got to work on your flirting, honey…" # @t_sdonko572.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But don’t worry, you’re not TOTALLY hopeless." # @t_sdonko573.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf_blush as cousin
    t_ch_cousin "(She knows I’m flirting?" # @t_sdonko574.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Maybe she does understand, after all!" # @t_sdonko575.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m too excited by that to point out that Donko didn’t change anything she’s wearing, either." # @t_sdonko575.01 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " At least… Not as far as I can tell…)" # @t_sdonko576.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "Let’s go, honey!" # @t_sdonko577.00 self.block='Last'
    show i_sw_black as curtain2:
        # ShowWithAtl
        ease_expo 1.5 alpha 0.7
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(After that, we have a great time at the concert together." # @t_sdonko578.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Donko loves music, and loves to dance…" # @t_sdonko579.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_scarf as cousin
    show i_donko_akimbo_grin as donko
    extend " I have fun dancing with her, even though I’m terrible at it!" # @t_sdonko580.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m starting to forget why I was feeling so crummy about this." # @t_sdonko581.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And after the music is done…" # @t_sdonko581.01 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ll ask Donko on a romantic walk." # @t_sdonko582.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Then we can figure out what exactly we’re doing here.)" # @t_sdonko583.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Phew! This is so great!" # @t_sdonko583.01 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ve like, NEVER had so much fun in my LIFE!" # @t_sdonko584.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    t_ch_donko "...Thank you, [slot_playerName]." # @t_sdonko585.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh_scarf as cousin
    t_ch_cousin "I’m glad we did this, Donko." # @t_sdonko586.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    extend " I know things have been weird, but I just wanted to say-" # @t_sdonko586.01 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "Oh, it looks like the band is done with the encore…" # @t_sdonko586.02 self.block='Last'
    show i_sw_black as curtain2:
        # ShowWithAtl
        ease_expo 1.5 alpha 0.0
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "What a totally AMAZING show!" # @t_sdonko587.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, yeah." # @t_sdonko588.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean, now that the concert is over…" # @t_sdonko588.01 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well, what I mean to say is, I was thinking we could-" # @t_sdonko589.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_smile as aki:
        # FadeEvent
        linear 0.33 alpha 1.0
    show i_donko_ygg_wink as donko:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.35 
    show i_cousin_default_neutral_scarf as cousin:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.12 
    $ renpy.pause(0.66) # TimedPause
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "Hi, Donko!" # @t_sdonko590.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Great show, wasn’t it?" # @t_sdonko590.01 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Where’d she come from? I was right in the middle of a sentence!)" # @t_sdonko591.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_grin as donko
    t_ch_donko "Aki! Hiii!" # @t_sdonko592.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I’m surprised to see you here, girl!" # @t_sdonko592.01 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Aren’t you, like, the Reigning Queen of being too busy for fun?!" # @t_sdonko593.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "I’m 100% passionate about music!" # @t_sdonko593.01 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_focus as aki
    extend " Actually, I’m 100% passionate about every one of my pursuits." # @t_sdonko594.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_nervouslaughter as aki
    t_ch_aki "Including partying…  but only for a regulated few seconds, of course." # @t_sdonko595.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "So I’ll see you at the afterparty, you two!" # @t_sdonko595.01 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Afterparty?!" # @t_sdonko595.02 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_nervouslaughter as aki:
        # FadeEvent
        linear 0.33 alpha 0.0
    show i_donko_ygg_grin as donko:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33 xpos 0.75 
    show i_cousin_default_neutral_scarf as cousin:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33 xpos 0.25 
    $ renpy.pause(0.66) # TimedPause
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_grin_blush as donko
    extend " O. M. G." # @t_sdonko596.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I didn’t even know there was going to be one!" # @t_sdonko597.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_grin_blush as donko
    t_ch_donko "We have to go!" # @t_sdonko598.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Er, I don’t know-" # @t_sdonko599.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf as cousin
    extend " I was sorta hoping we could-" # @t_sdonko5100.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira:
        # FadeEvent
        linear 0.33 alpha 1.0
    show i_donko_akimbo_grin_blush as donko:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.35 
    show i_cousin_default_surprise_scarf as cousin:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.12 
    $ renpy.pause(0.66) # TimedPause
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Yo, Donko! Yo, Cuz!" # @t_sdonko5100.01 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How RAD was this concert?!" # @t_sdonko5101.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m SO PUMPED!" # @t_sdonko5102.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    extend " MUSIC RULES!" # @t_sdonko5103.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    t_ch_cousin "(Another interruption?? Can’t anyone see we’re having a private conversation?!)" # @t_sdonko5104.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "It was totally rad, yo!" # @t_sdonko5104.01 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "PLEASE tell me you two are going to the afterparty." # @t_sdonko5105.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s gonna be off the chain!" # @t_sdonko5106.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_happy as taira
    t_ch_taira "Afterparties are like getting REVENGE on the first party… with FUN!" # @t_sdonko5106.01 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Oh yeah! [slot_playerName] and me will be there FOR SURE!" # @t_sdonko5107.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But…" # @t_sdonko5107.01 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_happy as taira:
        # FadeEvent
        linear 0.33 alpha 0.0
    show i_donko_ygg_wink as donko:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33 xpos 0.75 
    show i_cousin_default_neutral_scarf as cousin:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33 xpos 0.25 
    $ renpy.pause(0.66) # TimedPause
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "[slot_playerName]..." # @t_sdonko5108.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    extend " I’m starting to think you had an ulterior motive for inviting me here!" # @t_sdonko5109.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf as cousin
    t_ch_cousin "O-Oh! Actually, yeah, I-" # @t_sdonko5110.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_default as galaga:
        # FadeEvent
        linear 0.33 alpha 1.0
    show i_donko_ygg_grin_blush as donko:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.35 
    show i_cousin_default_surprise_scarf as cousin:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.12 
    extend "{w=0.8}{nw}"
    t_ch_galaga "{smallcaps}HELLO MORTALS.{/smallcaps}" # @t_sdonko5111.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}GALAGA ASSUMES YOU ARE GOING TO THE AFTERPARTY?{/smallcaps}" # @t_sdonko5112.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}IT IS GOING TO BE OUT OF THIS WORLD.{/smallcaps}" # @t_sdonko5112.01 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Teehee… of course we are!" # @t_sdonko5112.02 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_default as galaga:
        # ShowWithAtl
        ease_expo 1 ypos -0.49 
    show i_donko_ygg_grin_blush as donko:
        # ShowWithAtl
        pause 0.5 
        ease_expo .33 xpos 0.75 
    show i_cousin_default_surprise_scarf as cousin:
        # ShowWithAtl
        pause 0.75 
        ease_expo .33 xpos 0.25 
    $ renpy.pause(1.08) # TimedPause
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad_scarf as cousin
    t_ch_cousin "(Should I be jealous?!)" # @t_sdonko5113.01 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko
    t_ch_donko "Anyway, [slot_playerName]… you can’t hide your true intentions from me!" # @t_sdonko5114.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Nice try, though! Tee hee!" # @t_sdonko5115.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf as cousin
    t_ch_cousin "You do?" # @t_sdonko5116.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Sure! This wasn’t just about the concert..." # @t_sdonko5116.01 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_grin as donko
    show i_cousin_default_sad_scarf as cousin
    extend "{w=0.6}{nw}"
    extend " It was about the AMAZING afterparty!" # @t_sdonko5117.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "The top student is going, the captain of the Wrestleball team, the hottest student in class…" # @t_sdonko5118.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(...Yeah, I’m jealous.)" # @t_sdonko5118.01 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "...And ME!" # @t_sdonko5118.02 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "What’s more, all those SUPER IMPORTANT people will see you at the party WITH me!" # @t_sdonko5119.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m so proud…" # @t_sdonko5119.01 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You came up with this all on your own, and it’s gonna make you SUPER popular." # @t_sdonko5120.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    stop music fadeout 1.0
    extend " The student… has become the master!" # @t_sdonko5121.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    $ AudioEvent('music', 1.0, 1.0)
    show i_cousin_default_neutral_scarf as cousin
    t_ch_cousin "A-actually… I was hoping we could go on a little walk instead?" # @t_sdonko5122.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_grin as donko
    t_ch_donko "Tee-hee! Good joke, honey." # @t_sdonko5122.01 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Go on a walk with you in the middle of nowhere, or go to the hottest party of the year?" # @t_sdonko5123.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko
    t_ch_donko "DUH! Let’s go, already! I’m too excited to be fashionably late." # @t_sdonko5124.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Donko…" # @t_sdonko5125.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You don’t really think that’s all I care about, do you?" # @t_sdonko5125.01 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Come on, please come with me?" # @t_sdonko5126.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic as donko
    t_ch_donko "Like, why do you want to take a dumb WALK so badly?!" # @t_sdonko5127.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’re gonna blow your newfound popularity with weirdness again!" # @t_sdonko5128.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf as cousin
    t_ch_cousin "I thought we could…" # @t_sdonko5129.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You know…" # @t_sdonko5130.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Talk about our…" # @t_sdonko5131.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf_blush as cousin
    extend " ...feelings." # @t_sdonko5132.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Fine! My feelings are, you’re being really, like, annoying about this!" # @t_sdonko5133.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Come on!" # @t_sdonko5133.01 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Don’t you want to be popular?!" # @t_sdonko5134.00 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_scarf as cousin
    t_ch_cousin "NO!" # @t_sdonko5135.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "What?" # @t_sdonko5136.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_scarf as cousin
    t_ch_cousin "Donko…" # @t_sdonko5137.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I don’t care about being popular!" # @t_sdonko5138.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That was just something you decided for me!" # @t_sdonko5138.01 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_meloncholic as donko
    t_ch_donko "But don’t you want to have, like, tons of friends and stuff?" # @t_sdonko5139.00 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad_scarf as cousin
    t_ch_cousin "Not really… I mean, it’d be nice, but…" # @t_sdonko5140.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I don’t want to change who I am to get that." # @t_sdonko5141.00 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’d rather, you know…" # @t_sdonko5142.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_scarf as cousin
    t_ch_cousin "March to the beat of my own drum." # @t_sdonko5142.01 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic as donko
    t_ch_donko "...Huh? Is that a reference to something?" # @t_sdonko5142.02 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m not familiar with that phrase." # @t_sdonko5143.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf as cousin
    t_ch_cousin "SERIOUSLY?!" # @t_sdonko5143.01 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Are you saying you…" # @t_sdonko5144.00 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_crying as donko
    extend " don’t want my help anymore?" # @t_sdonko5144.01 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well, yeah!" # @t_sdonko5145.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_crying as donko
    t_ch_donko "...I see…" # @t_sdonko5146.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "If that’s how it is, then…" # @t_sdonko5146.01 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don’t want to waste my time on a loser like you, either." # @t_sdonko5146.02 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_scarf as cousin
    t_ch_cousin "What?!" # @t_sdonko5147.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " No, that’s not what I meant." # @t_sdonko5148.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I still want to spend time with you!" # @t_sdonko5148.01 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean, of course I do, that’s the whole point…" # @t_sdonko5149.00 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Then why are you being so, like, MEAN to me?" # @t_sdonko5150.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_crying_comic as donko
    extend " WAAAAH!" # @t_sdonko5150.01 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified_scarf as cousin
    t_ch_cousin "Oh, jeez…" # @t_sdonko5151.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Donko, please don’t cry…" # @t_sdonko5152.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Sniff.. Hic…" # @t_sdonko5152.01 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_crying_comic as donko
    extend " All I wanted to do was take you to a cool afterparty…" # @t_sdonko5153.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So you could be… sniff… popular…" # @t_sdonko5154.00 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "And now you won’t even… sniff… do that!" # @t_sdonko5155.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_scarf as cousin
    t_ch_cousin "C’mon, I-" # @t_sdonko5155.01 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    t_ch_cousin "...Wait a minute." # @t_sdonko5156.00 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’re still talking about the afterparty…" # @t_sdonko5157.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You’re… You’re…" # @t_sdonko5157.01 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Sniff… Huh?" # @t_sdonko5158.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf as cousin
    t_ch_cousin "I can’t believe it!" # @t_sdonko5159.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry_scarf as cousin
    extend " You’re STILL just trying to get me to do what you want!" # @t_sdonko5160.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You think you can just turn on the water works and I’ll fall in line, like your own personal marching band!" # @t_sdonko5160.01 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad_scarf as cousin
    t_ch_cousin "I thought you cared about me…" # @t_sdonko5161.00 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_crying as donko
    t_ch_donko "[slot_playerName]… I do care!" # @t_sdonko5161.01 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_crying_comic as donko
    t_ch_donko "W-Waaaaaaahhhh!" # @t_sdonko5162.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah, right! I’m leaving!" # @t_sdonko5163.00 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Well, like… sniff… FINE!" # @t_sdonko5164.00 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_crying_comic as donko
    extend " You’re… you’re just some LOSER who nobody cares about ANYWAY!" # @t_sdonko5164.01 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You can’t even play the TUBA!" # @t_sdonko5165.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "WAAAHHH!" # @t_sdonko5166.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " G-good luck snaring a better friend than me!" # @t_sdonko5167.00 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wow…" # @t_sdonko5167.01 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I know Donko’s feelings are hurt… I know that’s probably why she saying this stuff." # @t_sdonko5168.00 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But still… it stings." # @t_sdonko5168.01 self.block='Last'
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m really good at the tuba!)" # @t_sdonko5168.02 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Sniff… Sniff…" # @t_sdonko5168.03 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    t_ch_cousin "W-well…" # @t_sdonko5169.00 self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If you just think of me as some loser you took pity on…" # @t_sdonko5170.00 self.block='Last'
    # <ParallelEvent {'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Then… I guess that’s it." # @t_sdonko5171.00 self.block='Last'
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Good night, Donko." # @t_sdonko5171.01 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin:
        # ShowWithAtl
        linear .75 alpha 0.0
    show i_donko_default_crying_comic as donko
    show i_sw_black as curtain2 zorder 9
    $ renpy.pause(0.75) # TimedPause
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I didn’t wait to hear her reply. I turned and walked away as fast as I could." # @t_sdonko5172.00 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear 1 alpha 1.0
    extend "{w=1.0}{nw}"
    t_ch_cousin "I don’t know if you’ve ever turned your back on a crying drum…" # @t_sdonko5173.00 self.block='Last'
    # <ParallelEvent {'name': '_3q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But believe me, it’s harder than it sounds.)" # @t_sdonko5174.00 self.block='Last'
    # <NHSceneChange {'name': '_3r', 'scene': 's_day5.5'} NHSceneChange ''>
    label s_donko5__3r:
        # <NHSceneChange {'name': '_3r', 'scene': 's_day5.5'} NHSceneChange ''>
        jump s_day5p5