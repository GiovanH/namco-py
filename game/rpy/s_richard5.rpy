# <Scene scene {'id': 's_richard5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_richard5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_richard5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_richard5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/upbeat_half.ogg" loop
    show i_pacman_left as pacman zorder 9:
        default
        alpha 1.0
        xpos 1.49 
    show i_bg_cliff_day as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_miller_aliens_halfgrin as miller zorder 1:
        default
        xpos 0.7 
        alpha 0.0
    t_ch_cousin "(Richard left me a series of ingenious clues to decipher where to go for the apology.)" # @t_srichard50.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Like some kind of super conspiracy puzzle I had to unravel.)" # @t_srichard51.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "(And, okay, it was kind of fun to work it out.)" # @t_srichard52.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(But still. We’re gonna have to work on his whole conspiratorial thing.)" # @t_srichard53.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Wonder where he is…)" # @t_srichard54.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I’d be worried about being in the wrong place, except he texted me earlier to make sure I figured out the clues right.)" # @t_srichard55.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(And, okay, it’s a really nice spot. Great view.)" # @t_srichard56.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(It could even be romantic, BUT...where is he?)" # @t_srichard57.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    narrator "[slot_playerName]!" # @t_srichard58.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_aliens_halfgrin as miller:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "Ah, there you are. I was starting to wonder." # @t_srichard59.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "Yeah, I was setting up everything. You’ll love it." # @t_srichard510.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "It’s not one of those Walls of Crazy where there’s, like, a dozen pictures of different people with some of them circled and others crossed out? And with random news articles tacked up? And lengths of string tying it all together?" # @t_srichard511.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Is it?" # @t_srichard512.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    show i_miller_akimbo_halfgrin as miller
    t_ch_richard "Haha, no! But I don’t blame you for thinking that." # @t_srichard513.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "C’mon, it’s just over here." # @t_srichard514.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "But you should close your eyes." # @t_srichard515.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Okay…" # @t_srichard516.00 self.block='Last'
    show i_sw_black as curtain zorder 4:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_miller_standing_halfgrin as miller
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Seriously though, if it’s one of those crazy walls, I am SO outta here.)" # @t_srichard516.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_prop_picnic as picnic zorder 5:
        default
        alpha 0.0
        # ShowWithAtl
        pause 0.3 
        linear .8 alpha 1.0
    show i_sw_black as curtain:
        # ShowWithAtl
        pause 0.2 
        linear .5 alpha 1.0
    extend "{w=1.1}{nw}"
    t_ch_richard "Open ‘em up!" # @t_srichard517.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "!!!!" # @t_srichard518.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    extend " (It’s a picnic!)" # @t_srichard518.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(But the biggest and fanciest picnic EVER. A feast!)" # @t_srichard519.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Richard, what…" # @t_srichard519.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What IS all of this?" # @t_srichard520.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "It’s for you, is what it is!" # @t_srichard521.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I...I don’t understand." # @t_srichard522.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_contemplative as miller
    t_ch_richard "I wanted to apologize for screwing up earlier." # @t_srichard523.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin:
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .8 alpha 1.0
    extend "{w=0.8}{nw}"
    t_ch_cousin "(A way to a [slot_playerName]’s heart is through a whole lotta eatin’!)" # @t_srichard524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_halfgrin as miller:
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .8 alpha 1.0
    extend "{w=0.8}{nw}"
    t_ch_richard "And to show you I could slow down and appreciate life." # @t_srichard525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_laugh_blush as cousin
    show i_prop_picnic as picnic:
        # ShowWithAtl
        linear .5 alpha 0.0
        # ShowWithAtl
        linear .8 ypos 0.95 
    extend "{w=0.8}{nw}"
    t_ch_cousin "There’s so much to choose from. I don’t know where to begin!" # @t_srichard526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_laugh as miller
    show i_prop_picnic as picnic:
        # ShowWithAtl
        linear .3 alpha 1.0
    show i_sw_black as curtain:
        # ShowWithAtl
        linear .8 alpha 0.0
    extend "{w=0.8}{nw}"
    t_ch_richard "Take your time. I’m in no rush." # @t_srichard527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    show i_sw_black as curtain zorder 16
    t_ch_cousin "Who are you and what have you done with Richard Miller!" # @t_srichard528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "Ha! Yeah, yeah." # @t_srichard529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_halfgrin as miller
    t_ch_richard "I deserve that one." # @t_srichard530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Maybe not." # @t_srichard531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "You’re really making an effort to turn over a new leaf." # @t_srichard532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "It’s nice." # @t_srichard533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Also, all this food is making me hungry. Wanna start with…" # @t_srichard534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "...these things!" # @t_srichard535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_pondering_halfgrin as miller
    t_ch_richard "Ah, the profiteroles! Nice choice, let’s dig in." # @t_srichard536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wow, these are really good!)" # @t_srichard537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Richard’s really got something with this cooking of his.)" # @t_srichard538.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    show i_miller_pondering_serious as miller
    t_ch_cousin "(I wonder if it’s his intensity about it that makes his dishes so good?)" # @t_srichard539.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(It’s certainly a more constructive use of his energy than chasing conspiracies all the time!)" # @t_srichard540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Wait, what’s he…)" # @t_srichard541.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " ...Uh, Richard?" # @t_srichard541.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "Yeah?" # @t_srichard542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "What’re you, um, doing?" # @t_srichard543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "Hm? I’m enjoying a delicious pastry." # @t_srichard544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Are you?" # @t_srichard545.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Because it still hasn’t gotten to your mouth. It looks like you’re moving in slow motion, actually." # @t_srichard546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "Well, if I’m gonna slow down enough to enjoy life, then I’m gonna do it AS HARD AS POSSIBLE!" # @t_srichard547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_pondering_shocked as miller
    t_ch_richard "Ahh! It’s almost painful. But I could go EVEN SLOWER!" # @t_srichard548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Yup, and there’s that weird intensity again!)" # @t_srichard549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Uh, y’don’t have to do everything at 100%, y’know?" # @t_srichard549.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_aliens_shocked as miller
    t_ch_richard "But I do!" # @t_srichard550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "What’s the point of doing something if you aren’t gonna do it all the way? You said I should relax, slow down, and enjoy life." # @t_srichard551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_aliens_contemplative as miller
    t_ch_richard "So, I’m giving it a shot." # @t_srichard552.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_aliens_laugh as miller
    t_ch_richard "TO THE MAX!" # @t_srichard553.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I don’t think that’s how it works, though." # @t_srichard554.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "…" # @t_srichard555.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Are you…?" # @t_srichard556.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "You’re existing as intensely as you can right now, aren’t you?" # @t_srichard557.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_aliens_halfgrin as miller
    t_ch_richard "…." # @t_srichard558.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_aliens_contemplative as miller
    t_ch_richard "………….." # @t_srichard559.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_laugh as miller
    t_ch_richard "No?" # @t_srichard560.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(Dangit, Richard. You’re hopeless!)" # @t_srichard561.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        linear .25 xpos 0.15 
    show i_miller_akimbo_shocked as miller:
        # ShowWithAtl
        linear .25 xpos 0.3 
    show i_pacman_left as pacman:
        # ShowWithAtl
        easeout 4 xpos 0.83 
    extend "{w=4.0}{nw}"
    t_ch_pacman "Quite a feast you’ve made!" # @t_srichard562.00 self.block='Last'
    stop sound
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Pac-Man! How long have you been there?" # @t_srichard563.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Long enough to eat most of the International Section." # @t_srichard564.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "How big IS this feast anyway?" # @t_srichard565.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Well, not nearly as big as it was before I walked by!" # @t_srichard566.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "On an unrelated note, I couldn’t help but overhear your troubles." # @t_srichard567.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "My advice is to be true to yourself." # @t_srichard568.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    show i_miller_pondering_contemplative as miller
    t_ch_richard "...Really?" # @t_srichard569.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Sure." # @t_srichard570.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "So, I should keep being crazy and intense about everything all the time?" # @t_srichard571.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "What? No! That can’t be right." # @t_srichard572.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Hmm. Yeah, I have to agree with [slot_playerName] on that one." # @t_srichard573.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "It doesn’t feel like the solution to being too weird should be to double down on weirdness." # @t_srichard574.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Darn. That “true to yourself” stuff worked great for all those other kids…" # @t_srichard575.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Maybe what it means is that, if you’re being true to yourself, then you’re using what makes you special in a way that’s positive to you and to your community." # @t_srichard576.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But maybe also that to be TRULY true to yourself, um, to the maximum degree possible, means doing it without TRYING SO HARD TO DO IT." # @t_srichard577.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "…" # @t_srichard578.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_shocked as miller
    t_ch_richard "I get it now!" # @t_srichard579.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "Yeah!" # @t_srichard580.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_laugh as miller
    t_ch_richard "Being true to myself means...just being me!" # @t_srichard581.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "I don’t need to do everything like I’m racing against the clock." # @t_srichard582.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_halfgrin as miller
    t_ch_richard "I can just, like, do stuff." # @t_srichard583.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "Yeah!" # @t_srichard584.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "My work here is done." # @t_srichard585.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Oh, Richard! I’m so happy you get it! You finally get it!" # @t_srichard586.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "Not to change the subject, but uh…" # @t_srichard587.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_contemplative as miller
    t_ch_richard "Where’d all the food get off to?" # @t_srichard588.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # FadeEvent
        linear 2.0 alpha 0.0
    extend "{w=2.0}{nw}"
    t_ch_pacman "Where indeed?" # @t_srichard589.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_1c', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_richard5__1c:
        # <NHSceneChange NHSceneChange {'name': '_1c', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5