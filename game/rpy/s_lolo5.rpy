# <Scene {'id': 's_lolo5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_lolo5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_lolo5"
    $ renpy.pause(1)
    # <Scene {'id': 's_lolo5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events '<ParallelEvent name="_1B"><events><ActorFade auto="true" duration=".333" opacity="0" target="curtain2" /><ActorFade auto="true" duration=".333" opacity="0" target="yearbook" /></events></ParallelEvent>'>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/privatetimes.ogg" loop
    show i_bg_cafe as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_lolo_default_grin as lolo zorder 2:
        default
        xpos 0.7 
        alpha 0.0
    show i_pacman_left as pacman zorder 2:
        default
        xpos 1.49 
        alpha 0.0

    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I gotta admit, I’m pretty nervous." # @t_slolo50.01 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "There she is, sitting at one of the tables…" # @t_slolo51.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It looks like she’s writing something on her napkin?)" # @t_slolo52.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_grin as lolo:
        # ShowWithAtl
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_lolo "Hey, [slot_playerName]." # @t_slolo53.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Whatcha got there?" # @t_slolo54.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Nothing!" # @t_slolo55.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Don’t look at it!" # @t_slolo55.01 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_melancholy_blush as lolo
    t_ch_lolo "It’s just a dumb doodle!" # @t_slolo56.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "I didn’t know you liked to draw." # @t_slolo57.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_raisedbrow as lolo
    t_ch_lolo "I don’t! Not really…" # @t_slolo58.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_melancholy as lolo
    t_ch_lolo "We used to draw a lot at the shrine, when I was practicing to be a priestess." # @t_slolo59.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s pretty stupid…" # @t_slolo59.01 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_frustrated as lolo
    t_ch_lolo "I bet nobody remembers that now." # @t_slolo510.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Even though it was kinda important to me…" # @t_slolo510.01 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_frustrated as lolo
    t_ch_lolo "Or at least I thought it was." # @t_slolo511.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well… okay." # @t_slolo512.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I won’t force you to let me look at it." # @t_slolo512.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_grin as lolo
    extend "{w=0.2}{nw}"
    t_ch_lolo "...This place is pretty cool, isn’t it?" # @t_slolo513.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I come here sometimes… People read poetry. It’s actually kind of neat." # @t_slolo513.01 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha, yeah." # @t_slolo514.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " I’m glad I had free time so I could come and meet you here!" # @t_slolo514.01 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (It meant a lot to me that she even invited me…" # @t_slolo514.02 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "I wonder what it means?)" # @t_slolo514.03 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Heh. Yeah." # @t_slolo515.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_shrug_grin as lolo
    t_ch_lolo "I’m actually supposed to be in yearbook club right now." # @t_slolo516.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_grin as lolo
    extend " But they won’t notice that I skipped." # @t_slolo516.01 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_melancholy as lolo
    show i_cousin_energetic_neutral as cousin
    extend " Nobody notices me anyway." # @t_slolo516.02 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Lolo-!!" # @t_slolo517.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(No- I shouldn’t say anything…" # @t_slolo518.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " It seems like something is kinda different today." # @t_slolo518.01 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don’t want to make her feel like I’ll just get mad if she talks to me.)" # @t_slolo518.02 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_melancholy as lolo
    t_ch_lolo "I just wanted to see you, I guess…" # @t_slolo519.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I wanted to tell you… about Klonoa." # @t_slolo520.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "!!" # @t_slolo521.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (This is it…" # @t_slolo521.01 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "This is the one from her past I’ve heard her talk about so much…" # @t_slolo522.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Am I finally going to find out what happened to Lolo…" # @t_slolo522.01 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "To make her think that the world is an awful place, where nothing matters?" # @t_slolo523.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I don’t want her to have to feel like that…)" # @t_slolo524.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_melancholy as lolo
    t_ch_lolo "He was always nice to me, but…" # @t_slolo525.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He made me realize that no one would ever care about me." # @t_slolo525.01 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "He didn’t mean to do it, but people who are really lucky like that-" # @t_slolo526.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Like him, and like you-" # @t_slolo526.01 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_melancholy as lolo
    extend " They never really get it, you know?" # @t_slolo526.02 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Haha, what am I saying." # @t_slolo527.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_melancholy as lolo
    extend " Of course you don’t know." # @t_slolo527.01 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "“Lucky”?" # @t_slolo528.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What do you mean?" # @t_slolo528.01 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "How am I lucky?" # @t_slolo529.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "You know… you never have to worry about…" # @t_slolo530.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_melancholy_blush as lolo
    t_ch_lolo "Being ugly." # @t_slolo531.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Or that your feelings are…" # @t_slolo532.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_melancholy_blush as lolo
    t_ch_lolo "Heh. That you don’t have feelings at all." # @t_slolo533.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_slolo534.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " Why are you telling me about this now?" # @t_slolo534.01 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Did something happen?" # @t_slolo534.02 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow_blush as lolo
    t_ch_lolo "Well, kinda." # @t_slolo535.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I just figured…" # @t_slolo535.01 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Like you said, I could get expelled for cheat codes." # @t_slolo536.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So in case that happens… I should tell you what I’m thinking about." # @t_slolo536.01 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I kinda get the feeling that she’s not going to try to enter a cheat code anymore." # @t_slolo537.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Maybe she just needed an excuse to talk to me…" # @t_slolo537.01 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " Whatever the case, I’ll take it.)" # @t_slolo537.02 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Okay." # @t_slolo538.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_grin as lolo
    extend " Did I show you this picture of Klonoa and me?" # @t_slolo538.01 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Notice anything about it?" # @t_slolo538.02 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Just that…" # @t_slolo539.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "You look a little happier." # @t_slolo540.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " And that makes me kinda sad." # @t_slolo540.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "Well, I was pretty dumb then." # @t_slolo541.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "But no… in that picture, you can see why-" # @t_slolo542.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Why being around Klonoa made me feel like…" # @t_slolo542.01 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " It isn’t worth it to try." # @t_slolo542.02 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "… Uh… I don’t really get it." # @t_slolo543.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "It’s…" # @t_slolo544.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated_blush as lolo
    show i_cousin_default_neutral as cousin
    t_ch_lolo "it’s my ears." # @t_slolo545.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_frustrated_blush as lolo
    t_ch_lolo "I hate looking at them…" # @t_slolo546.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Ohhh… her ears." # @t_slolo547.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Of course." # @t_slolo547.01 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I was wondering what Lolo could possibly thing was ugly and unlovable about herself…" # @t_slolo548.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " Poor thing… I think her ears are cute, but of course she’d think they were too big-)" # @t_slolo548.01 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "They’re so SMALL!" # @t_slolo549.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(...Or not.)" # @t_slolo550.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_raisedbrow_blush as lolo
    t_ch_lolo "I mean, look at Klonoa!" # @t_slolo551.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " His ears are HUGE!" # @t_slolo551.01 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They’re AMAZING!" # @t_slolo551.02 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "My ears will never, ever be that big. I’m just stuck that way, so..." # @t_slolo552.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "I’m just gross and ugly, and there’s nothing I can do about it." # @t_slolo553.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Lolo, no!" # @t_slolo554.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Please don’t say that about yourself…" # @t_slolo554.01 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I mean, look at me!" # @t_slolo555.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "...What about you?" # @t_slolo556.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "I have no ears at all!" # @t_slolo557.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Do you think I’m ugly?" # @t_slolo557.01 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "...It’s different…" # @t_slolo558.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "You’re you." # @t_slolo559.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Did Klonoa make you feel bad about your ears?" # @t_slolo560.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_raisedbrow as lolo
    t_ch_lolo "No! Never. Well, not on purpose." # @t_slolo561.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_frustrated as lolo
    extend " I don’t think he ever thought about it." # @t_slolo561.01 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "So… that’s it?" # @t_slolo562.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s why you started thinking that nothing mattered…" # @t_slolo562.01 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Not even your own life?" # @t_slolo562.02 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Because you thought your ears were too small?" # @t_slolo563.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You don’t seem like the type to put so much stock in how you look..." # @t_slolo564.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean, I’m really sorry that it hurt you so much..." # @t_slolo564.01 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But it’s sorta… hard to believe." # @t_slolo564.02 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "…" # @t_slolo565.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Heh…" # @t_slolo566.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "I know what you mean." # @t_slolo567.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "?" # @t_slolo568.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "I guess you’re right…" # @t_slolo569.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The ear thing is something I felt bad about for a long time." # @t_slolo569.01 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "But, I stopped caring about stuff like that." # @t_slolo570.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Even if nobody could ever like me because of my ears…" # @t_slolo571.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It doesn’t matter anyway." # @t_slolo571.01 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    extend " People always fall apart anyway." # @t_slolo571.02 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Friends who mattered so much to you forget you existed." # @t_slolo571.03 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Maybe it’s better to avoid all that." # @t_slolo572.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "But you’re not ugly!" # @t_slolo573.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’re you, and you're...." # @t_slolo573.01 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "You’re, well, really pretty." # @t_slolo574.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_lolo "Please…" # @t_slolo575.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_lolo_crossed_grin as lolo
    extend " You don’t have to say anything corny." # @t_slolo575.01 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_melancholy as lolo
    t_ch_lolo "I know you’re the wholesome type who probably thinks everyone is beautiful on the inside." # @t_slolo576.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    extend " Even if you really mean it, all that cutesy stuff gets tiring after a while." # @t_slolo576.01 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Um…" # @t_slolo577.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    extend " Sorry." # @t_slolo577.01 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "The truth is…" # @t_slolo578.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "It’s even more pathetic than what I just told you." # @t_slolo579.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "You’ve been looking for the big thing that made me stop caring, right?" # @t_slolo580.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " Like maybe you think Klonoa broke my heart, and I learned to see the world as a cruel place, or something." # @t_slolo580.01 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Er… I guess so." # @t_slolo581.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Well,  nothing like that happened. My heart’s not broken." # @t_slolo582.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "The truth is…" # @t_slolo583.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " There is no \"big thing\" that happened." # @t_slolo583.01 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "One day, I woke up…" # @t_slolo584.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "And I just started feeling this way." # @t_slolo585.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "I’d go to practice my priestess duties, and for the life of me I couldn’t remember why I wanted to." # @t_slolo586.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " I’d look around and just think it all felt so hopeless." # @t_slolo586.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Even Klonoa, who I liked so much…" # @t_slolo587.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " I started to act really cold around him." # @t_slolo587.01 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I didn’t even have a reason why." # @t_slolo587.02 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "It was just how I was starting to be." # @t_slolo588.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " A little more each day." # @t_slolo588.01 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "And when he left..." # @t_slolo589.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean, I missed him. But it didn’t matter as much as I thought it would." # @t_slolo589.01 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "And what’s worse, I didn’t care that it didn’t matter." # @t_slolo590.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I was losing my memories of my friend, losing what I cared about…" # @t_slolo591.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And it didn’t feel any different to me…" # @t_slolo591.01 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Than it would have if I hadn’t." # @t_slolo591.02 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "And there was no reason for any of it. I’m just broken, I guess." # @t_slolo592.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I talk all the time about how sad it is that friends drift apart and stop caring…" # @t_slolo593.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But the truth is, I’m the one who did that. To Klonoa, and to my fellow priestesses." # @t_slolo593.01 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I drifted away from them, and for no reason at all." # @t_slolo594.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And to be honest…." # @t_slolo594.01 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "The fact that I did that…" # @t_slolo595.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s kind of more of a relief than anything else." # @t_slolo595.01 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Lolo…" # @t_slolo596.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I don’t know what to say." # @t_slolo597.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_shrug_raisedbrow as lolo
    t_ch_lolo "I know. It’s pathetic, right?" # @t_slolo598.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_shrug_frustrated as lolo
    extend " That’s how I know…" # @t_slolo598.01 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "That things in this life really are meaningless." # @t_slolo599.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Because there isn’t even any meaning to how I feel." # @t_slolo5100.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s all for nothing." # @t_slolo5100.01 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_lolo "Which means it could happen to anyone, even a happy person like you…" # @t_slolo5101.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "And it also means… there’s nothing I can do to fix it." # @t_slolo5102.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Because there was no real problem in the first place." # @t_slolo5102.01 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "So when people try to say nice things to me, to get me to snap out of it-" # @t_slolo5103.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " It felt even worse than if they’d said nothing at all." # @t_slolo5103.01 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They never understood how deep it went." # @t_slolo5103.02 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Lolo, I’m so sorry…" # @t_slolo5104.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "All this time, I thought..." # @t_slolo5105.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_frustrated as lolo
    t_ch_lolo "I don’t need you to be sorry." # @t_slolo5106.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I just feel like…" # @t_slolo5107.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    extend " Like no one understands me." # @t_slolo5107.01 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "But I thought maybe…" # @t_slolo5108.00 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "Jeez, this is hard to say." # @t_slolo5109.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated_blush as lolo
    with Dissolve(0.5)
    extend " I dunno how you can say corny stuff all the time and not explode." # @t_slolo5109.01 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I thought..." # @t_slolo5110.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Maybe you might be different?" # @t_slolo5111.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Lolo…" # @t_slolo5112.00 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What do you mean?" # @t_slolo5113.00 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "I thought maybe…" # @t_slolo5114.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_melancholy_blush as lolo
    extend " Maybe you might understand…" # @t_slolo5114.01 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "What I’m feeling right now. If you know what I mean." # @t_slolo5115.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(“What she’s feeling”?" # @t_slolo5116.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What DOES she mean?" # @t_slolo5116.01 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    extend " I wish she wouldn’t be so vague all the time…" # @t_slolo5116.02 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I guess she must be talking about how she thinks life is meaningless and stuff.)" # @t_slolo5116.03 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m sorry, Lolo." # @t_slolo5117.00 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " I wish I could feel the same way…" # @t_slolo5117.01 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I’ve just never felt that the way you do." # @t_slolo5118.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don’t want you to feel bad…" # @t_slolo5118.01 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But I don’t like to lie, you know?" # @t_slolo5118.02 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "…" # @t_slolo5119.00 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_default_cry as lolo
    t_ch_lolo "Hah…" # @t_slolo5120.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(Whoah!" # @t_slolo5121.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She looks like she’s on the verge of tears…" # @t_slolo5121.01 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What?!)" # @t_slolo5121.02 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Typical…" # @t_slolo5122.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Of course it happens like this." # @t_slolo5122.01 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_crossed_cry as lolo
    t_ch_lolo "I don’t know why I expected anything different…" # @t_slolo5123.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Every time I think I can’t get hurt anymore, I get proved wrong." # @t_slolo5123.01 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_lolo "Sorry… for wasting your time." # @t_slolo5124.00 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_shrug_cry as lolo
    extend " Don’t worry about me…" # @t_slolo5124.01 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It doesn’t matter anyway." # @t_slolo5124.02 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Whoa, what?" # @t_slolo5125.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Lolo, wait-" # @t_slolo5125.01 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Don’t just walk out of the cafe-" # @t_slolo5125.02 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_lolo_shrug_cry as lolo:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(Too late… she’s gone." # @t_slolo5126.00 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Sigh…" # @t_slolo5127.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don’t really understand what happened just there." # @t_slolo5127.01 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I told her how I felt about that stuff before, didn’t I?)" # @t_slolo5128.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_pacman_left as pacman:
        default
        alpha 1.0
        xpos 1.35 
        # ShowWithAtl
        easeout 5 xpos 0.8 
    $ renpy.pause(5.0) # TimedPause
    stop sound
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Pac-Man?!" # @t_slolo5129.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " It’s good to see you, but what are you doing here?" # @t_slolo5129.01 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Be true to yourself." # @t_slolo5130.00 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Huh? What do you mean?" # @t_slolo5131.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Pac-Man is tapping on the table where Lolo was sitting…" # @t_slolo5132.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What is that?" # @t_slolo5133.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s… Lolo’s napkin?" # @t_slolo5133.01 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The one she was drawing on before?" # @t_slolo5133.02 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Let’s see what’s written here…" # @t_slolo5134.00 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh." # @t_slolo5135.00 self.block='Last'
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s a heart…" # @t_slolo5135.01 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " With a little drawing of me.)" # @t_slolo5135.02 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "When you’re young, even the smallest feelings feel much bigger than they are." # @t_slolo5136.00 self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s what Lolo is going through right now…" # @t_slolo5136.01 self.block='Last'
    # <ParallelEvent {'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "But that doesn’t mean those feelings aren’t real." # @t_slolo5137.00 self.block='Last'
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "She’s got to be true to them, and herself… and so do you." # @t_slolo5138.00 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Oh. So when she asked me if I felt the same…" # @t_slolo5139.00 self.block='Last'
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She wasn’t asking if I thought things were meaningless…" # @t_slolo5139.01 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "She was asking if…" # @t_slolo5140.00 self.block='Last'
    # <ParallelEvent {'name': '_3q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh." # @t_slolo5141.00 self.block='Last'
    # <ParallelEvent {'name': '_3r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    extend " Ohhh." # @t_slolo5141.01 self.block='Last'
    # <ParallelEvent {'name': '_3s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " Wow… I’m an idiot.)" # @t_slolo5141.02 self.block='Last'
    # <ParallelEvent {'name': '_3t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Pac-Man… It might be too late to be true to myself now…" # @t_slolo5142.00 self.block='Last'
    # <ParallelEvent {'name': '_3u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    extend " I might have already messed it up!" # @t_slolo5142.01 self.block='Last'
    # <ParallelEvent {'name': '_3v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "But thank you…  I’ll try my best to fix it." # @t_slolo5143.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_3w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        easein 5 xpos 1.35 
    extend "{w=5.0}{nw}"
    t_ch_pacman "Good luck, [slot_playerName]!" # @t_slolo5144.00 self.block='Last'
    # <ParallelEvent {'name': '_3x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(That Pac-Man always knows what to say…" # @t_slolo5145.00 self.block='Last'
    # <ParallelEvent {'name': '_3y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " I’ve got to find Lolo." # @t_slolo5145.01 self.block='Last'
    # <ParallelEvent {'name': '_3z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I hope I’ll see her tomorrow…)" # @t_slolo5146.00 self.block='Last'
    # <NHSceneChange {'name': '_40', 'scene': 's_day5.5'} NHSceneChange ''>
    label s_lolo5__40:
        # <NHSceneChange {'name': '_40', 'scene': 's_day5.5'} NHSceneChange ''>
        jump s_day5p5