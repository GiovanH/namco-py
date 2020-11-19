# <Scene scene {'id': 's_lolo5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_lolo5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_lolo5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_lolo5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} '<ParallelEvent name="_1B"><events><ActorFade auto="true" duration=".333" opacity="0" target="curtain2" /><ActorFade auto="true" duration=".333" opacity="0" target="yearbook" /></events></ParallelEvent>'>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
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

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I gotta admit, I’m pretty nervous." # @t_slolo50.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "There she is, sitting at one of the tables…" # @t_slolo51.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It looks like she’s writing something on her napkin?)" # @t_slolo52.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_grin as lolo:
        # ShowWithAtl
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_lolo "Hey, [slot_playerName]." # @t_slolo53.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Whatcha got there?" # @t_slolo54.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Nothing!" # @t_slolo55.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Don’t look at it!" # @t_slolo55.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_melancholy_blush as lolo
    t_ch_lolo "It’s just a dumb doodle!" # @t_slolo56.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "I didn’t know you liked to draw." # @t_slolo57.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_raisedbrow as lolo
    t_ch_lolo "I don’t! Not really…" # @t_slolo58.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_melancholy as lolo
    t_ch_lolo "We used to draw a lot at the shrine, when I was practicing to be a priestess." # @t_slolo59.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s pretty stupid…" # @t_slolo59.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_frustrated as lolo
    t_ch_lolo "I bet nobody remembers that now." # @t_slolo510.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Even though it was kinda important to me…" # @t_slolo510.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_frustrated as lolo
    t_ch_lolo "Or at least I thought it was." # @t_slolo511.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well… okay." # @t_slolo512.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I won’t force you to let me look at it." # @t_slolo512.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_grin as lolo
    extend "{w=0.2}{nw}"
    t_ch_lolo "...This place is pretty cool, isn’t it?" # @t_slolo513.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I come here sometimes… People read poetry. It’s actually kind of neat." # @t_slolo513.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha, yeah." # @t_slolo514.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    extend " I’m glad I had free time so I could come and meet you here!" # @t_slolo514.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (It meant a lot to me that she even invited me…" # @t_slolo514.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "I wonder what it means?)" # @t_slolo514.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Heh. Yeah." # @t_slolo515.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_grin as lolo
    t_ch_lolo "I’m actually supposed to be in yearbook club right now." # @t_slolo516.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_grin as lolo
    extend " But they won’t notice that I skipped." # @t_slolo516.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy as lolo
    show i_cousin_energetic_neutral as cousin
    extend " Nobody notices me anyway." # @t_slolo516.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Lolo-!!" # @t_slolo517.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(No- I shouldn’t say anything…" # @t_slolo518.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    extend " It seems like something is kinda different today." # @t_slolo518.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I don’t want to make her feel like I’ll just get mad if she talks to me.)" # @t_slolo518.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_melancholy as lolo
    t_ch_lolo "I just wanted to see you, I guess…" # @t_slolo519.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I wanted to tell you… about Klonoa." # @t_slolo520.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "!!" # @t_slolo521.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (This is it…" # @t_slolo521.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "This is the one from her past I’ve heard her talk about so much…" # @t_slolo522.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Am I finally going to find out what happened to Lolo…" # @t_slolo522.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "To make her think that the world is an awful place, where nothing matters?" # @t_slolo523.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I don’t want her to have to feel like that…)" # @t_slolo524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy as lolo
    t_ch_lolo "He was always nice to me, but…" # @t_slolo525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " He made me realize that no one would ever care about me." # @t_slolo525.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "He didn’t mean to do it, but people who are really lucky like that-" # @t_slolo526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Like him, and like you-" # @t_slolo526.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_melancholy as lolo
    extend " They never really get it, you know?" # @t_slolo526.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Haha, what am I saying." # @t_slolo527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy as lolo
    extend " Of course you don’t know." # @t_slolo527.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "“Lucky”?" # @t_slolo528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " What do you mean?" # @t_slolo528.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "How am I lucky?" # @t_slolo529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "You know… you never have to worry about…" # @t_slolo530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy_blush as lolo
    t_ch_lolo "Being ugly." # @t_slolo531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Or that your feelings are…" # @t_slolo532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_melancholy_blush as lolo
    t_ch_lolo "Heh. That you don’t have feelings at all." # @t_slolo533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "…" # @t_slolo534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " Why are you telling me about this now?" # @t_slolo534.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Did something happen?" # @t_slolo534.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow_blush as lolo
    t_ch_lolo "Well, kinda." # @t_slolo535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I just figured…" # @t_slolo535.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Like you said, I could get expelled for cheat codes." # @t_slolo536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " So in case that happens… I should tell you what I’m thinking about." # @t_slolo536.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I kinda get the feeling that she’s not going to try to enter a cheat code anymore." # @t_slolo537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Maybe she just needed an excuse to talk to me…" # @t_slolo537.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " Whatever the case, I’ll take it.)" # @t_slolo537.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Okay." # @t_slolo538.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_grin as lolo
    extend " Did I show you this picture of Klonoa and me?" # @t_slolo538.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Notice anything about it?" # @t_slolo538.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Just that…" # @t_slolo539.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "You look a little happier." # @t_slolo540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " And that makes me kinda sad." # @t_slolo540.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "Well, I was pretty dumb then." # @t_slolo541.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "But no… in that picture, you can see why-" # @t_slolo542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Why being around Klonoa made me feel like…" # @t_slolo542.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " It isn’t worth it to try." # @t_slolo542.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "… Uh… I don’t really get it." # @t_slolo543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "It’s…" # @t_slolo544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    show i_cousin_default_neutral as cousin
    t_ch_lolo "it’s my ears." # @t_slolo545.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_frustrated_blush as lolo
    t_ch_lolo "I hate looking at them…" # @t_slolo546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Ohhh… her ears." # @t_slolo547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Of course." # @t_slolo547.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I was wondering what Lolo could possibly thing was ugly and unlovable about herself…" # @t_slolo548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " Poor thing… I think her ears are cute, but of course she’d think they were too big-)" # @t_slolo548.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "They’re so SMALL!" # @t_slolo549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(...Or not.)" # @t_slolo550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_raisedbrow_blush as lolo
    t_ch_lolo "I mean, look at Klonoa!" # @t_slolo551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " His ears are HUGE!" # @t_slolo551.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " They’re AMAZING!" # @t_slolo551.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "My ears will never, ever be that big. I’m just stuck that way, so..." # @t_slolo552.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "I’m just gross and ugly, and there’s nothing I can do about it." # @t_slolo553.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Lolo, no!" # @t_slolo554.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Please don’t say that about yourself…" # @t_slolo554.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I mean, look at me!" # @t_slolo555.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "...What about you?" # @t_slolo556.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "I have no ears at all!" # @t_slolo557.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Do you think I’m ugly?" # @t_slolo557.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "...It’s different…" # @t_slolo558.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "You’re you." # @t_slolo559.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Did Klonoa make you feel bad about your ears?" # @t_slolo560.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_raisedbrow as lolo
    t_ch_lolo "No! Never. Well, not on purpose." # @t_slolo561.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_frustrated as lolo
    extend " I don’t think he ever thought about it." # @t_slolo561.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "So… that’s it?" # @t_slolo562.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That’s why you started thinking that nothing mattered…" # @t_slolo562.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Not even your own life?" # @t_slolo562.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Because you thought your ears were too small?" # @t_slolo563.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You don’t seem like the type to put so much stock in how you look..." # @t_slolo564.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I mean, I’m really sorry that it hurt you so much..." # @t_slolo564.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But it’s sorta… hard to believe." # @t_slolo564.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "…" # @t_slolo565.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Heh…" # @t_slolo566.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "I know what you mean." # @t_slolo567.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "?" # @t_slolo568.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "I guess you’re right…" # @t_slolo569.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The ear thing is something I felt bad about for a long time." # @t_slolo569.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "But, I stopped caring about stuff like that." # @t_slolo570.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Even if nobody could ever like me because of my ears…" # @t_slolo571.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It doesn’t matter anyway." # @t_slolo571.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " People always fall apart anyway." # @t_slolo571.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Friends who mattered so much to you forget you existed." # @t_slolo571.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Maybe it’s better to avoid all that." # @t_slolo572.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "But you’re not ugly!" # @t_slolo573.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You’re you, and you're...." # @t_slolo573.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "You’re, well, really pretty." # @t_slolo574.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_lolo "Please…" # @t_slolo575.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    show i_lolo_crossed_grin as lolo
    extend " You don’t have to say anything corny." # @t_slolo575.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy as lolo
    t_ch_lolo "I know you’re the wholesome type who probably thinks everyone is beautiful on the inside." # @t_slolo576.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    extend " Even if you really mean it, all that cutesy stuff gets tiring after a while." # @t_slolo576.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Um…" # @t_slolo577.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " Sorry." # @t_slolo577.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "The truth is…" # @t_slolo578.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "It’s even more pathetic than what I just told you." # @t_slolo579.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "You’ve been looking for the big thing that made me stop caring, right?" # @t_slolo580.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " Like maybe you think Klonoa broke my heart, and I learned to see the world as a cruel place, or something." # @t_slolo580.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Er… I guess so." # @t_slolo581.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Well,  nothing like that happened. My heart’s not broken." # @t_slolo582.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "The truth is…" # @t_slolo583.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " There is no \"big thing\" that happened." # @t_slolo583.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "One day, I woke up…" # @t_slolo584.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "And I just started feeling this way." # @t_slolo585.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "I’d go to practice my priestess duties, and for the life of me I couldn’t remember why I wanted to." # @t_slolo586.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " I’d look around and just think it all felt so hopeless." # @t_slolo586.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Even Klonoa, who I liked so much…" # @t_slolo587.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " I started to act really cold around him." # @t_slolo587.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I didn’t even have a reason why." # @t_slolo587.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "It was just how I was starting to be." # @t_slolo588.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " A little more each day." # @t_slolo588.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "And when he left..." # @t_slolo589.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I mean, I missed him. But it didn’t matter as much as I thought it would." # @t_slolo589.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "And what’s worse, I didn’t care that it didn’t matter." # @t_slolo590.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I was losing my memories of my friend, losing what I cared about…" # @t_slolo591.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And it didn’t feel any different to me…" # @t_slolo591.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Than it would have if I hadn’t." # @t_slolo591.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "And there was no reason for any of it. I’m just broken, I guess." # @t_slolo592.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I talk all the time about how sad it is that friends drift apart and stop caring…" # @t_slolo593.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But the truth is, I’m the one who did that. To Klonoa, and to my fellow priestesses." # @t_slolo593.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I drifted away from them, and for no reason at all." # @t_slolo594.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And to be honest…." # @t_slolo594.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "The fact that I did that…" # @t_slolo595.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s kind of more of a relief than anything else." # @t_slolo595.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Lolo…" # @t_slolo596.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I don’t know what to say." # @t_slolo597.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_raisedbrow as lolo
    t_ch_lolo "I know. It’s pathetic, right?" # @t_slolo598.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_frustrated as lolo
    extend " That’s how I know…" # @t_slolo598.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "That things in this life really are meaningless." # @t_slolo599.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Because there isn’t even any meaning to how I feel." # @t_slolo5100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s all for nothing." # @t_slolo5100.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_lolo "Which means it could happen to anyone, even a happy person like you…" # @t_slolo5101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "And it also means… there’s nothing I can do to fix it." # @t_slolo5102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Because there was no real problem in the first place." # @t_slolo5102.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "So when people try to say nice things to me, to get me to snap out of it-" # @t_slolo5103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " It felt even worse than if they’d said nothing at all." # @t_slolo5103.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " They never understood how deep it went." # @t_slolo5103.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Lolo, I’m so sorry…" # @t_slolo5104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "All this time, I thought..." # @t_slolo5105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_frustrated as lolo
    t_ch_lolo "I don’t need you to be sorry." # @t_slolo5106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I just feel like…" # @t_slolo5107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " Like no one understands me." # @t_slolo5107.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "But I thought maybe…" # @t_slolo5108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "Jeez, this is hard to say." # @t_slolo5109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    with Dissolve(0.5)
    extend " I dunno how you can say corny stuff all the time and not explode." # @t_slolo5109.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I thought..." # @t_slolo5110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "Maybe you might be different?" # @t_slolo5111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Lolo…" # @t_slolo5112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What do you mean?" # @t_slolo5113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I thought maybe…" # @t_slolo5114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy_blush as lolo
    extend " Maybe you might understand…" # @t_slolo5114.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_30', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "What I’m feeling right now. If you know what I mean." # @t_slolo5115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_31', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(“What she’s feeling”?" # @t_slolo5116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_32', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " What DOES she mean?" # @t_slolo5116.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_33', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " I wish she wouldn’t be so vague all the time…" # @t_slolo5116.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_34', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I guess she must be talking about how she thinks life is meaningless and stuff.)" # @t_slolo5116.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_35', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I’m sorry, Lolo." # @t_slolo5117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_36', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " I wish I could feel the same way…" # @t_slolo5117.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_37', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I’ve just never felt that the way you do." # @t_slolo5118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_38', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I don’t want you to feel bad…" # @t_slolo5118.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_39', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But I don’t like to lie, you know?" # @t_slolo5118.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "…" # @t_slolo5119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_cry as lolo
    t_ch_lolo "Hah…" # @t_slolo5120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(Whoah!" # @t_slolo5121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " She looks like she’s on the verge of tears…" # @t_slolo5121.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " What?!)" # @t_slolo5121.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Typical…" # @t_slolo5122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Of course it happens like this." # @t_slolo5122.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_cry as lolo
    t_ch_lolo "I don’t know why I expected anything different…" # @t_slolo5123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Every time I think I can’t get hurt anymore, I get proved wrong." # @t_slolo5123.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Sorry… for wasting your time." # @t_slolo5124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_cry as lolo
    extend " Don’t worry about me…" # @t_slolo5124.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It doesn’t matter anyway." # @t_slolo5124.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Whoa, what?" # @t_slolo5125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Lolo, wait-" # @t_slolo5125.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Don’t just walk out of the cafe-" # @t_slolo5125.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_3P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_cry as lolo:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
    # <ParallelEvent ParallelEvent {'name': '_3Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(Too late… she’s gone." # @t_slolo5126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Sigh…" # @t_slolo5127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I don’t really understand what happened just there." # @t_slolo5127.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I told her how I felt about that stuff before, didn’t I?)" # @t_slolo5128.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_3V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        default
        alpha 1.0
        xpos 1.35 
        # ShowWithAtl
        easeout 5 xpos 0.8 
    $ renpy.pause(5.0, hard=True) # TimedPause
    stop sound
    # <ParallelEvent ParallelEvent {'name': '_3X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Pac-Man?!" # @t_slolo5129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    extend " It’s good to see you, but what are you doing here?" # @t_slolo5129.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Be true to yourself." # @t_slolo5130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Huh? What do you mean?" # @t_slolo5131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Pac-Man is tapping on the table where Lolo was sitting…" # @t_slolo5132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What is that?" # @t_slolo5133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s… Lolo’s napkin?" # @t_slolo5133.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The one she was drawing on before?" # @t_slolo5133.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Let’s see what’s written here…" # @t_slolo5134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh." # @t_slolo5135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s a heart…" # @t_slolo5135.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " With a little drawing of me.)" # @t_slolo5135.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "When you’re young, even the smallest feelings feel much bigger than they are." # @t_slolo5136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That’s what Lolo is going through right now…" # @t_slolo5136.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "But that doesn’t mean those feelings aren’t real." # @t_slolo5137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "She’s got to be true to them, and herself… and so do you." # @t_slolo5138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Oh. So when she asked me if I felt the same…" # @t_slolo5139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " She wasn’t asking if I thought things were meaningless…" # @t_slolo5139.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "She was asking if…" # @t_slolo5140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh." # @t_slolo5141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    extend " Ohhh." # @t_slolo5141.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " Wow… I’m an idiot.)" # @t_slolo5141.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Pac-Man… It might be too late to be true to myself now…" # @t_slolo5142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    extend " I might have already messed it up!" # @t_slolo5142.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "But thank you…  I’ll try my best to fix it." # @t_slolo5143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_3w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        easein 5 xpos 1.35 
    extend "{w=5.0}{nw}"
    t_ch_pacman "Good luck, [slot_playerName]!" # @t_slolo5144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(That Pac-Man always knows what to say…" # @t_slolo5145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    extend " I’ve got to find Lolo." # @t_slolo5145.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I hope I’ll see her tomorrow…)" # @t_slolo5146.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_40', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_lolo5__40:
        # <NHSceneChange NHSceneChange {'name': '_40', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5