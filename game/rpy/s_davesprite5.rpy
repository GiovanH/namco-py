# <Scene scene {'id': 's_davesprite5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_davesprite5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_davesprite5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_davesprite5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_davesprite5_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        play music "bgm/privatetimes.ogg" loop
        show i_bg_rooftop as bg zorder 0 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_cousin_default_neutral as cousin zorder 2:
            default
            xpos 0.3 
        show i_davesprite_standing_disinterest as davesprite zorder 2:
            default
            xpos 0.7 
        show i_pacman_right as pacman zorder 2:
            default
            xpos -0.48 

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It’s pretty nice up here." # @t_sdavesprite524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " I didn’t know you were such a romantic!" # @t_sdavesprite524.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "of course i am this is a dating sim" # @t_sdavesprite525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "if i wasnt a romantic itd be kind of a ripoff right" # @t_sdavesprite526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "You know, your insane rambling really takes the fun out of teasing you." # @t_sdavesprite527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    t_ch_davesprite "whatever you know you love it" # @t_sdavesprite528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "So did you want anything in particular to eat?" # @t_sdavesprite529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "yeah i shoulda brought like a bento box or something right" # @t_sdavesprite530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "isnt that the usual thing for this kind of situation" # @t_sdavesprite531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Yes Davesprite." # @t_sdavesprite532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Any type of meal would be the “thing” for this “kind of situation”." # @t_sdavesprite532.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    t_ch_davesprite "har har" # @t_sdavesprite533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "but yeah i shoulda picked some up" # @t_sdavesprite534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "that woulda been so classic" # @t_sdavesprite535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "i guess i blew it" # @t_sdavesprite536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Can you eat normal food anyway?" # @t_sdavesprite537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Aren’t you some kind of part-bird… ghost… thing…" # @t_sdavesprite537.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " I’m still not really clear on your whole deal." # @t_sdavesprite537.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "yeah i dunno actually" # @t_sdavesprite538.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i never thought too much about it" # @t_sdavesprite539.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "i could really go for some birdseed now though" # @t_sdavesprite540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "it sounds like it would really hit the spot" # @t_sdavesprite541.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i wonder if they make birdseed bento boxes" # @t_sdavesprite542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Actually…" # @t_sdavesprite543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I already figured you might be into that kinda thing…" # @t_sdavesprite544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Since you’ve told me your part-bird, or mixed with a bird, or something like that." # @t_sdavesprite544.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "So I kinda took the liberty of bringing you some birdseed!" # @t_sdavesprite545.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "If you don’t like it, you don’t have to eat it…" # @t_sdavesprite546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " But maybe you could at least try it and see." # @t_sdavesprite546.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    with Dissolve(.333)
    t_ch_cousin "Umm… I hope that’s not too presumptuous!" # @t_sdavesprite547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_defeated_eyebrow as davesprite
    t_ch_davesprite "wow" # @t_sdavesprite548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "[slot_playerName]" # @t_sdavesprite549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "this is…" # @t_sdavesprite550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I’m sorry, was this like…" # @t_sdavesprite551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " Totally condescending?!" # @t_sdavesprite551.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified_blush as cousin
    with Dissolve(.333)
    t_ch_cousin "I mean, I know you’re a person, and not just a bird-thing…" # @t_sdavesprite552.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "no no no its not that" # @t_sdavesprite553.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "its not that at all" # @t_sdavesprite554.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "this is like" # @t_sdavesprite555.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_grin as davesprite
    t_ch_davesprite "really really thoughtful" # @t_sdavesprite556.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i cant remember the last time someone did something like this for me actually" # @t_sdavesprite557.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    t_ch_davesprite "thank you" # @t_sdavesprite558.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Oh! Haha, well, it was nothing really." # @t_sdavesprite559.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "I’ve just had a lot of fun hanging out with you…" # @t_sdavesprite560.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " You know, in spite of it all." # @t_sdavesprite560.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "…" # @t_sdavesprite561.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "you know what" # @t_sdavesprite562.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "im not into this" # @t_sdavesprite563.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "...Oh… Sorry…" # @t_sdavesprite564.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " I was just teasing with the “in spite of it all” thing…" # @t_sdavesprite564.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "no you didnt do anything wrong" # @t_sdavesprite565.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "im just starting to feel really guilty" # @t_sdavesprite566.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "even if this is all just part of the game" # @t_sdavesprite567.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "youre like" # @t_sdavesprite568.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "really cool" # @t_sdavesprite569.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "really really cool…" # @t_sdavesprite570.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "you deserve way better than a freaky …sprite-thing like me" # @t_sdavesprite571.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "im not even a person and all i do is talk about a bunch of stuff that just seems like nonsense to you" # @t_sdavesprite572.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i shouldve never led you down this romance path" # @t_sdavesprite573.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Davesprite, for goodness’ sake!" # @t_sdavesprite574.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    extend " How many times do I have to tell you?!" # @t_sdavesprite574.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m hanging out with you because I WANT to." # @t_sdavesprite574.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "yeah but i still led you on kinda" # @t_sdavesprite575.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i mean i guided you into it with all my talk of getting the good ending and so on" # @t_sdavesprite576.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "i shouldve tried to guide you into failing with me instead" # @t_sdavesprite577.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_defeated_sad as davesprite
    t_ch_davesprite "im the worst romance option in this whole game" # @t_sdavesprite578.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "you should have picked someone cool" # @t_sdavesprite579.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Davesprite, I know you hate yourself because you think you’re just a “copy” of someone or whatever…" # @t_sdavesprite580.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " I don’t really get what’s going on with all that…" # @t_sdavesprite580.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "whoah who said i hate myself" # @t_sdavesprite581.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "i mean i totally do but" # @t_sdavesprite582.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "i didnt exactly say that…" # @t_sdavesprite583.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "But sometimes you get so insecure that it’s… almost hurtful, you know?" # @t_sdavesprite584.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " You’re saying I don’t have any real choices in my life…" # @t_sdavesprite584.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That even the choice to spend time with you isn’t right." # @t_sdavesprite584.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Well, that’s what I chose for myself!" # @t_sdavesprite585.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I don’t care if you don’t understand why I would hang out with someone like you, but…" # @t_sdavesprite585.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile_blush as davesprite
    t_ch_davesprite "[slot_playerName]…" # @t_sdavesprite586.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "...but I have my reasons, okay?!" # @t_sdavesprite587.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Can you just forget that I’m a game construct or whatever for just a moment…" # @t_sdavesprite588.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And be real with me?" # @t_sdavesprite588.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    stop music fadeout 1.0
    t_ch_cousin "Can you trust me when I say…" # @t_sdavesprite589.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    $ AudioEvent('music', 1.0, 1.0)
    extend " That I really like you?" # @t_sdavesprite589.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And it’s not just because of some “romance path” I’m supposed to be on?" # @t_sdavesprite590.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "but what if" # @t_sdavesprite591.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "what if i tell you" # @t_sdavesprite592.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "that i really cant believe that" # @t_sdavesprite593.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "what would you say then" # @t_sdavesprite594.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "would you … hate me?" # @t_sdavesprite595.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well… it’s pretty frustrating, but…" # @t_sdavesprite596.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I guess I’ll just have to try harder…" # @t_sdavesprite597.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin:
        # ShowWithAtl
        linear .75 xpos 0.48 
    extend "{w=0.75}{nw}"
    t_ch_cousin "To get you to believe me." # @t_sdavesprite598.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "(whoah [slot_playerName] are you holding my hand right now" # @t_sdavesprite599.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "that is a smooth move" # @t_sdavesprite5100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile_blush as davesprite
    t_ch_davesprite "props yo)" # @t_sdavesprite5101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    extend "{w=0.5}{nw}"
    t_ch_cousin "Anyway… maybe I haven’t been fair to you." # @t_sdavesprite5102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "huh?" # @t_sdavesprite5103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "hows that" # @t_sdavesprite5104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well, I’m asking you to trust and believe in me…" # @t_sdavesprite5105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " But I haven’t trusted or believed in you for even one second." # @t_sdavesprite5105.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "yeah but all my stuff sounds pretty crazy right" # @t_sdavesprite5106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i dont exactly blame you on that one" # @t_sdavesprite5107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "So, let’s say, just for the sake of argument…" # @t_sdavesprite5108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That I believe you." # @t_sdavesprite5108.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I’m not saying I do, necessarily!" # @t_sdavesprite5109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " But if I did…" # @t_sdavesprite5109.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What happens next in the game?" # @t_sdavesprite5110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "oh thats an easy one" # @t_sdavesprite5111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "pacman gets kidnapped" # @t_sdavesprite5112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Huh?" # @t_sdavesprite5113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " For real?" # @t_sdavesprite5113.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "yeah by evil namco high" # @t_sdavesprite5114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "those guys are tools" # @t_sdavesprite5115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Wait, you sound like you’re serious." # @t_sdavesprite5116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "i am totally serious" # @t_sdavesprite5117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "pacmans gonna get kidnapped" # @t_sdavesprite5118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "its gonna be a total catastrophe" # @t_sdavesprite5119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "but its gonna probably be okay dont worry" # @t_sdavesprite5120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "i mean you gotta pick the right options but ill help you out with that" # @t_sdavesprite5121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Wait, if you’re so sure Pacman’s gonna get kidnapped…" # @t_sdavesprite5122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    extend " I mean, that’s terrible! Isn’t there anything we can do?!" # @t_sdavesprite5122.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "sure its easy" # @t_sdavesprite5123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "just come find me after it happens" # @t_sdavesprite5124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "And then you’ll fight them with your game-breaking digital powers?!" # @t_sdavesprite5125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "haha no way that sounds hard" # @t_sdavesprite5126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "but since youve already done well enough on my path" # @t_sdavesprite5127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    t_ch_davesprite "thats probably enough to trigger a decent ending with me" # @t_sdavesprite5128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "so pacman will be rescued no matter what" # @t_sdavesprite5129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "which means all you have to do is come find me and pick me for your final choice thing" # @t_sdavesprite5130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "and we can just go mess around and not do anything in the final battle" # @t_sdavesprite5131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "since itll already be settled in the game by then" # @t_sdavesprite5132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "what we do wont actually matter" # @t_sdavesprite5133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But if Pacman gets kidnapped…" # @t_sdavesprite5134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’ll want to fight to save him no matter what!" # @t_sdavesprite5134.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "To just blow it off would be… so cruel!" # @t_sdavesprite5135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "not really because he gets rescued anyway?" # @t_sdavesprite5136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "dont you get it?" # @t_sdavesprite5137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "it doesnt matter" # @t_sdavesprite5138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "so we can just chill" # @t_sdavesprite5139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "cmon itll be fun" # @t_sdavesprite5140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "It matters to me!" # @t_sdavesprite5141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Even if this is all just a game…" # @t_sdavesprite5142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I believe my choices matter." # @t_sdavesprite5142.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I believe my feelings matter!" # @t_sdavesprite5142.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I’m trying to meet you halfway here, Davesprite…" # @t_sdavesprite5143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I’m saying I believe you that Pacman will be kidnapped…" # @t_sdavesprite5144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Now you have to believe in me too!" # @t_sdavesprite5144.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Believe me when I say…" # @t_sdavesprite5145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    extend " that fighting for the people we love will always make a difference!" # @t_sdavesprite5145.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "well yeah i guess it does" # @t_sdavesprite5146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "except when it makes absolutely no difference" # @t_sdavesprite5147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "like in this scenario" # @t_sdavesprite5148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "Ugh… why am I even trying with you." # @t_sdavesprite5149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You’re so hung up on this ridiculous game thing…" # @t_sdavesprite5150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You can’t let go of it, even for someone who’s trying so hard to  connect with you…" # @t_sdavesprite5150.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "im sorry [slot_playerName]" # @t_sdavesprite5151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "what i said just now was unnecessary" # @t_sdavesprite5152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "just all this stuff is hard to reconcile sometimes" # @t_sdavesprite5153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "you know?" # @t_sdavesprite5154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I need some time to think." # @t_sdavesprite5155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " I’ll see you later, Davesprite…" # @t_sdavesprite5155.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Enjoy the birdseed." # @t_sdavesprite5156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " If you’re programmed to enjoy it, or whatever." # @t_sdavesprite5156.01 self.block='Last'
    show i_cousin_default_sad as cousin:
        # FadeEvent
        linear 0.75 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_defeated_sad as davesprite
    t_ch_davesprite "dang" # @t_sdavesprite5157.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    show i_pacman_right as pacman:
        # ShowWithAtl
        linear 1.5 xpos 0.2 
    stop sound
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_defeated_disinterest as davesprite
    t_ch_davesprite "oh hey pacman" # @t_sdavesprite5158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "(maybe i should warn him about getting kidnapped" # @t_sdavesprite5159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "but it wont make a difference anyway)" # @t_sdavesprite5160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Something on your mind, young orange thing?" # @t_sdavesprite5161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "yeah i think i might have just totally blown it" # @t_sdavesprite5162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "with this really cool friend of mine" # @t_sdavesprite5163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "which is pretty much par for the course for me" # @t_sdavesprite5164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "considering what an idiot loser i am" # @t_sdavesprite5165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Yeah, maybe you… SHOULDN’T be true to yourself." # @t_sdavesprite5166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "amen brother" # @t_sdavesprite5167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "want to get in on this birdseed?" # @t_sdavesprite5168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "…." # @t_sdavesprite5169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "…." # @t_sdavesprite5170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "….." # @t_sdavesprite5171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "…." # @t_sdavesprite5172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Yes. Yes I do." # @t_sdavesprite5173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Never speak of this to anyone." # @t_sdavesprite5174.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_30', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_davesprite5__30:
        # <NHSceneChange NHSceneChange {'name': '_30', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5