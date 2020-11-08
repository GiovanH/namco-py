# <Scene {'id': 's_jane5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_jane5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_jane5"
    $ renpy.pause(1)
    # <Scene {'id': 's_jane5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/privatetimes.ogg" loop
    show i_bg_rooftop as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_jane_default_smile as jane zorder 2:
        default
        xpos 0.7 
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_pacman_left as pacman zorder 2:
        default
        xpos 1.35 
        alpha 0.0
    t_ch_cousin "(And so, I met up with Jane on the rooftop." # @t_sjane514.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’ll try to hide it, but I’ve got butterflies in my stomach…" # @t_sjane515.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " Not much else, though. I’m hungry.)" # @t_sjane515.01 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_default_laugh as jane
    t_ch_jane "Thanks for meeting up with me, [slot_playerName]." # @t_sjane516.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha, yeah! I’m happy to…" # @t_sjane517.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Although…" # @t_sjane518.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Er, not to be rude, but- I thought you said you had made food for us?" # @t_sjane518.01 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I didn’t bring anything for myself…" # @t_sjane518.02 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_default_grin as jane
    t_ch_jane "Hmm? Oh yes. I baked a nice cake for you!" # @t_sjane519.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "It’s my way of thanking you for spending so much time with me lately…" # @t_sjane520.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "I just have it stored in my sylladex for safekeeping." # @t_sjane521.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, thanks for baking, but…" # @t_sjane522.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "There you go, talking in Silly Words from Sillytown again." # @t_sjane523.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_armscrossed_grin as jane
    t_ch_jane "Er, here. I’ll show you!" # @t_sjane524.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Huh…? It’s like a computer interface… appearing above her head…" # @t_sjane525.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She’s… pulling objects out of it?" # @t_sjane525.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I can see the other objects in the folder there…" # @t_sjane526.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " A big red spoon… and a fake plastic spider…" # @t_sjane526.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Is this how… she made things appear out of thin air before?" # @t_sjane527.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It must be!)" # @t_sjane527.01 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "I use a Recipe modus." # @t_sjane528.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "It’s pretty new, but works like a charm!" # @t_sjane529.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "See, here’s that cake I made for us…" # @t_sjane530.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "I hope you’ll like it." # @t_sjane531.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "I…" # @t_sjane532.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It looks great, but…" # @t_sjane533.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m sorry Jane, I’m having a really hard time holding my tongue." # @t_sjane534.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_armscrossed_smile as jane
    t_ch_jane "Hmm?" # @t_sjane535.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "What are you talking about, [slot_playerName]?" # @t_sjane536.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You’re… using a freaky magic computer thing…" # @t_sjane537.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " To make things appear out of thin air!" # @t_sjane537.01 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You’ve been using it since I met you!" # @t_sjane538.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How can you say that’s normal?!" # @t_sjane538.01 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "It is normal! All my friends use it…" # @t_sjane539.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_armscrossed_frustrated as jane
    t_ch_jane "I don’t understand this hostility, [slot_playerName]." # @t_sjane540.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Jane, this is WEIRD! It’s almost SUPERNATURAL." # @t_sjane541.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But that doesn’t bother me…" # @t_sjane541.01 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Because it fits in here!" # @t_sjane541.02 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Everyone at this school has something special or different about them…" # @t_sjane542.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How can you just ignore that?!" # @t_sjane542.01 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "How can you say YOUR thing is “just normal”?" # @t_sjane543.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_handonhip_frustrated as jane
    t_ch_jane "[slot_playerName], I’m… trying not to lose my temper here…" # @t_sjane544.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "You keep jibbering on and on about these ridiculous notions…" # @t_sjane545.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "You’re not LISTENING to me!" # @t_sjane546.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "I keep telling you what the deal is with all these so-called “supernatural” things…" # @t_sjane547.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "And it’s like talking to a gosh-darned brick wall!" # @t_sjane548.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "I thought we were friends…" # @t_sjane549.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "Can’t you just trust me?!" # @t_sjane550.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But… that goes both ways, Jane." # @t_sjane551.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m asking YOU to trust ME!" # @t_sjane551.01 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "I told you… I’m not just a normal human." # @t_sjane552.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m a Katamari cousin, from space!" # @t_sjane552.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "The fact that you tell me I can’t actually be who I am…" # @t_sjane553.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It hurts, you know?" # @t_sjane554.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_armscrossed_embarrassed as jane
    t_ch_jane "UGH! You are so STUBBORN!" # @t_sjane555.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "You STILL won’t listen to me!" # @t_sjane556.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I am listening to you!" # @t_sjane557.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I just think you’re wrong!" # @t_sjane557.01 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "Wh-what? How could you?!" # @t_sjane558.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Jane, in my family we have a saying…" # @t_sjane559.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " “If enough people tell you it’s raining, you should bring an umbrella.”" # @t_sjane559.01 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If it was just Terezi and Davesprite, I could maybe understand your confusion…" # @t_sjane560.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    extend " But in our class, we have a cat, and a bird, and a drum, and an incredibly hot spaceship!" # @t_sjane560.01 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Those people are all real, and they’re all telling you it’s raining!" # @t_sjane561.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_default_frustrated as jane
    t_ch_jane "W-well… maybe my family has a saying too…" # @t_sjane562.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "“[slot_playerName], that’s a stupid saying!”" # @t_sjane563.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Your family saying specifically references me?" # @t_sjane564.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_handonhip_embarrassed as jane
    t_ch_jane "M-maybe…" # @t_sjane565.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "...Well, what about me too?" # @t_sjane566.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We’re close enough friends that we spend a lot of time together…" # @t_sjane566.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And you baked this nice cake for me…" # @t_sjane566.02 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But you don’t even trust me enough to believe me when I tell you what I am?" # @t_sjane567.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_default_frustrated as jane
    t_ch_jane "Don’t be ridiculous!" # @t_sjane568.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "Trust has nothing to do with it!" # @t_sjane569.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "What you say doesn’t make sense!" # @t_sjane570.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "It makes sense to me!" # @t_sjane571.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " Shouldn’t that be enough?!" # @t_sjane571.01 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_armscrossed_embarrassed as jane
    t_ch_jane "I… I can’t." # @t_sjane572.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "How am I supposed to believe you’re related to someone called…" # @t_sjane573.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "“King of all Cosmos”?" # @t_sjane574.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "There’s no rhyme or reason to it." # @t_sjane575.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "I can’t tell if you’re trying to trick me…" # @t_sjane576.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "There’s no proof, anyway…" # @t_sjane577.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Proof?! I’m standing right in front of you!" # @t_sjane578.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Don’t you understand?" # @t_sjane579.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Everyone here is special! Especially you!" # @t_sjane579.01 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_armscrossed_embarrassed_blush as jane
    t_ch_jane "No! I’m NOT! Shut UP!" # @t_sjane580.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "…" # @t_sjane581.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_default_embarrassed as jane
    t_ch_jane "...I don’t want to have this conversation anymore." # @t_sjane582.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "I don’t like to yell at my friends…" # @t_sjane583.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(She’s putting the cake she made back into here weird computer storage system…" # @t_sjane584.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s so frustrating that she can accept her computer thing as normal…" # @t_sjane585.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just because it’s what’s familiar to her.)" # @t_sjane585.01 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "I’ll… see you tomorrow, [slot_playerName]." # @t_sjane586.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_jane "I suppose. :|" # @t_sjane587.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Uh, okay." # @t_sjane588.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_jane_default_embarrassed as jane:
        # ShowWithAtl
        linear .333 alpha 0.0
    extend "{w=0.333}{nw}"
    extend " Bye, Jane." # @t_sjane588.01 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin:
        # ShowWithAtl
        linear .333 xpos 0.5 
    extend "{w=0.333}{nw}"
    t_ch_cousin "(Darn, I wanted to eat that cake…)" # @t_sjane589.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Sigh… I know I’m right, but…" # @t_sjane590.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I wish “being right” didn’t mean losing my friend." # @t_sjane590.01 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        easeout 5 xpos 0.7 
    $ renpy.pause(2)
    # <ParallelEvent {'delay': '2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.25 xpos 0.25 
    $ renpy.pause(0.25) # TimedPause
    extend "{w=5.0}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    stop sound
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh, hey Pacman." # @t_sjane591.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Maybe you kids… SHOULDN’T be true to yourselves." # @t_sjane592.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Huh?!" # @t_sjane593.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You mean compromise my beliefs so I can stay friends with Jane?!" # @t_sjane593.01 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Huh? Sure, I guess." # @t_sjane594.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or not. Maybe she’s the one who shouldn’t be true to herself." # @t_sjane594.01 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I dunno. One of those things." # @t_sjane594.02 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "You kids definitely have to compromise somehow though." # @t_sjane595.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I dunno, Pacman, that doesn’t feel right to me…" # @t_sjane596.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Still, I guess you’re right." # @t_sjane597.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Life has to have some kind of compromise in it…" # @t_sjane597.01 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Otherwise nobody would be able to be friends! Because nobody agrees with anyone else about EVERYTHING." # @t_sjane598.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Uh… yeah. Exactly." # @t_sjane599.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s exactly what I meant to say." # @t_sjane599.01 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "You’re so wise, Pacman." # @t_sjane5100.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "You want one of my cherries? You look hungry." # @t_sjane5101.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That would actually be GREAT." # @t_sjane5102.00 self.block='Last'
    # <NHSceneChange {'name': '_1w', 'scene': 's_day5.5'} NHSceneChange ''>
    label s_jane5__1w:
        # <NHSceneChange {'name': '_1w', 'scene': 's_day5.5'} NHSceneChange ''>
        jump s_day5p5