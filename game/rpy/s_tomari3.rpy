# <Scene {'id': 's_tomari3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_tomari3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_tomari3"
    $ renpy.pause(1)
    # <Scene {'id': 's_tomari3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/school.ogg" loop
    show i_bg_library as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_tomari_standing_smile as tomari zorder 2:
        default
        xpos 0.7 
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_miller_aliens_serious as miller zorder 3:
        default
        xpos 0.5 
        ypos 1.5 
    show i_digdug_left as digdug zorder 2:
        default
        xpos 1.35 
        alpha 0.0
    t_ch_cousin "(Tomari said he’d be in the library.)" # @t_stomari30.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wonder where he is.)" # @t_stomari31.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Or if he’s hiding!)" # @t_stomari32.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(With an axe!)" # @t_stomari33.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(No, no. No. Don’t be ridiculous.)" # @t_stomari34.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Just because he’s super intense, and a bit of a loner, and kinda weird doesn’t mean he’s an axe murderer.)" # @t_stomari35.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (But it doesn’t help his case either…)" # @t_stomari35.01 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        # ShowWithAtl
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_tomari "Hey, [slot_playerName]!" # @t_stomari36.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "AH!" # @t_stomari37.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " I mean, um…" # @t_stomari37.01 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " AH wondered where you were." # @t_stomari37.02 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Good cover!)" # @t_stomari37.03 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Keep thinking on your toes like that and you’ll get through this no problem.)" # @t_stomari38.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Sorry if I kept you waiting. We can’t leave any stone unturned with the threat of ten thousand years of darkness hanging over all of Namco Land." # @t_stomari39.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Right. Yeah. That’s completely sane." # @t_stomari310.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "So, I pulled every book on advanced robotics in the library." # @t_stomari311.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Advanced?! What happened to basic?? I’m up debris creek without a katamari!)" # @t_stomari312.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Uh, super. Yeah. Maybe we could get a couple books on the basic stuff too though." # @t_stomari312.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Is there a Robots For Complete Idiots?)" # @t_stomari313.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Y’know, like a beginner’s guide. Or Baby’s First Robot. Something like that." # @t_stomari314.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "So we don’t, um, lose sight of the fundamentals, that is." # @t_stomari315.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thoughtful as tomari
    t_ch_tomari "Hmmmm…" # @t_stomari316.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(I think he’s going for it!)" # @t_stomari317.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "Ha, yeah, we should do that. We might lose our heads and forget to check the actuator fluid, or to lubricate the processor cores. Haha!" # @t_stomari318.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Exactly." # @t_stomari319.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I guess?)" # @t_stomari320.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "That was a joke, [slot_playerName]." # @t_stomari321.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Joke? WHERE????)" # @t_stomari322.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "Anyway, let’s get started!" # @t_stomari323.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Oh, boy. I can’t wait." # @t_stomari324.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thinking as tomari
    t_ch_tomari "[slot_playerName]?" # @t_stomari325.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah?" # @t_stomari326.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "You’re just standing there." # @t_stomari327.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Am I?" # @t_stomari328.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Yeah. C’mon!" # @t_stomari329.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Better follow him, I guess.)" # @t_stomari330.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(On the bright side, maybe I’ll break my legs before we get to the books!)" # @t_stomari331.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "Okay, here we are." # @t_stomari332.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(DARN MY STURDY LEGS! DARN THEM I SAY!)" # @t_stomari333.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "To save time we should divide the books in two and then compare notes afterward." # @t_stomari334.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Yeah. That’s what we should do." # @t_stomari335.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_mortified as tomari
    t_ch_tomari "Okay, I call this stack! Good luck." # @t_stomari336.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Great!" # @t_stomari337.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " (Maybe I’ll go blind and get to excuse myself?)" # @t_stomari337.01 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Meanwhile, may as well get comfortable and crack open one of these books…)" # @t_stomari338.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wait a second.)" # @t_stomari339.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(This is a cookbook. Hm, must’ve gotten in with the robot stuff by mistake.)" # @t_stomari340.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’ll just quietly go to the next one in the stack. No reason to interrupt Tomari’s reading.)" # @t_stomari341.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Uh, even if he IS holding his book upside-down…?)" # @t_stomari341.01 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Whatever, he’s a genius. They’re eccentric like that.)" # @t_stomari342.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Okay, next book in my stack is…)" # @t_stomari342.01 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(The Pictorial History of the Bridges of Namco Land County?)" # @t_stomari343.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Isn’t there just the one bridge though?)" # @t_stomari344.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Maybe not? I’m new here afterall.)" # @t_stomari345.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Anyway, once is a mistake, twice is a coincidence. Next book will definitely be about robot engineering.)" # @t_stomari346.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    extend " (On the Reproductive Cycles of the Space Insectia???)" # @t_stomari346.01 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Okay, what is going on here?)" # @t_stomari347.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_smile as tomari
    t_ch_tomari "Wow, [slot_playerName]. You’re really flying through those books!" # @t_stomari348.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    show i_tomari_notebook_mortified as tomari
    t_ch_cousin "Oh, uh. Yup! That’s what I’m doing." # @t_stomari349.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " (Half of my books are on random subjects and the rest are cookbooks!)" # @t_stomari349.01 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_serious as miller:
        # ShowWithAtl
        linear 0.5 ypos 1.2 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(Huh. The cookbooks were all checked out by Richard Miller. About a hundred times each.)" # @t_stomari350.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_serious as miller:
        # ShowWithAtl
        linear 0.75 ypos 1.5 
    extend "{w=0.75}{nw}"
    t_ch_cousin "(And then returned ten minutes later. Weird.)" # @t_stomari351.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Anyway, none of this stuff is about robots! What gives?)" # @t_stomari352.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hooooooooold on.)" # @t_stomari353.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Tomari’s still holding his book upside-down.)" # @t_stomari354.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And it’s about breeds of horses!)" # @t_stomari355.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Horses are almost never robots!)" # @t_stomari356.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And he’s taking tons of notes!)" # @t_stomari357.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(It’s his GLASSES! He’s practically blind without ‘em! He has no idea what books he picked out.)" # @t_stomari358.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Or what he’s reading.)" # @t_stomari358.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Or what he’s writing down.)" # @t_stomari358.02 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Or what I’m reading…)" # @t_stomari358.03 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "(This could work for me!)" # @t_stomari359.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " Yup. Makin’ all kinds of progress like crazy over here. How’re you doing?" # @t_stomari359.01 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "It’s a little difficult to parse the relevant info from the larger framework of the central thesis." # @t_stomari360.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Uh-huh, I bet.)" # @t_stomari361.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Looks like you’re taking lots of notes though." # @t_stomari362.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Hm? Oh, no. Just doodling in the margins." # @t_stomari363.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But you’re not even looking at it. Your hand’s just going." # @t_stomari364.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Yeah, it’s a method I employ on occasion. Gives form to the formless via the subconscious mind. It’s like, your conscious mind sees everything, but it doesn’t notice everything." # @t_stomari365.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "If that makes sense." # @t_stomari366.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Clear as mud, just like everything else he says!)" # @t_stomari367.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "And doodling like this allows for the free form association of ideas to occur before rational thought can get in the way." # @t_stomari368.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Mostly you get nonsense, of course." # @t_stomari369.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ah, yes, of course!" # @t_stomari370.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thoughtful as tomari
    t_ch_tomari "But every so often it can illuminate connections previously hidden in the shadows of the mind." # @t_stomari371.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Pretty sure this is how serial killers talk???)" # @t_stomari372.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, yeah. I do that myself sometimes." # @t_stomari373.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Technically that’s not a lie.)" # @t_stomari373.01 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(But he doesn’t have to know that the stuff I doodle is, like, homework getting all rolled up by a katamari ball that falls off the edge of the world!)" # @t_stomari374.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Really it’s just that I reach the edge of the paper though.)" # @t_stomari375.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_smile as tomari
    t_ch_tomari "Ha! I don’t think you need to use dumb tricks like that to get your brain working. You already powered through half a dozen of those advanced robotics books!" # @t_stomari376.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh." # @t_stomari377.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeeeeaaaaaaaah." # @t_stomari378.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Hey, you stopped doodling. Did you finish? Let’s see what you came up with!" # @t_stomari379.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_mortified as tomari
    t_ch_tomari "Hm? I’m sure it’s nothing." # @t_stomari380.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Yeah, it’s just a big blurry mess. See?" # @t_stomari381.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(!!!!!)" # @t_stomari382.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What’s he talking about?)" # @t_stomari383.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I don’t know the first thing about robot stuff, but he just accidentally drew up a big ol robot blueprint!)" # @t_stomari384.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Freehanded!)" # @t_stomari385.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Without looking!)" # @t_stomari386.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(With black ink on white paper!)" # @t_stomari387.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_tomari "I’m just gonna throw it away." # @t_stomari388.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Wait!" # @t_stomari389.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari
    t_ch_tomari "We can’t afford to waste time on useless stuff like this while the fate of all Namco Land hangs in the balance." # @t_stomari390.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_robotprint "*IS THROOOOOWN!*" # @t_stomari391.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "There. Gone forever." # @t_stomari392.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(I think he thinks he threw it in the trash basket, but actually it’s a water fountain.)" # @t_stomari393.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Sheesh, he’s as blind as a bat!)" # @t_stomari394.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Anyway, I’m betting he misjudged those blueprints entirely since he can’t see them clearly enough.)" # @t_stomari395.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’ll just sneak on over there and grab the designs before they’re ruined!)" # @t_stomari396.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Hey, um." # @t_stomari397.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Oof!" # @t_stomari398.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "WHAT THIRST BE THIS?" # @t_stomari399.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " (Dang, I’m a pretty good actor. Who knew!)" # @t_stomari399.01 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m just gonna go over there now." # @t_stomari399.02 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "To the water fountain." # @t_stomari3100.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Hm? Oh, sure. There used to be one around here." # @t_stomari3101.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Somewhere." # @t_stomari3102.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin:
        # ShowWithAtl
        ease_expo 0.25 xpos 0.25 
    extend "{w=0.25}{nw}"
    t_ch_cousin "Uh, I’ll just use the one over there. Near the trash can." # @t_stomari3103.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin:
        # ShowWithAtl
        ease_expo 0.25 xpos 0.2 
    extend "{w=0.25}{nw}"
    t_ch_cousin "And relieve it." # @t_stomari3104.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin:
        # ShowWithAtl
        ease_expo 0.25 xpos 0.15 
    extend "{w=0.25}{nw}"
    t_ch_cousin "The thirst, I mean." # @t_stomari3105.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Yeah! It’s totally working! He doesn’t suspect a thing!)" # @t_stomari3105.01 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Just grab those blueprints…)" # @t_stomari3106.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin:
        # ShowWithAtl
        ease_expo 0.333 xpos 0.3 
    extend "{w=0.333}{nw}"
    t_ch_cousin "(...Like so!)" # @t_stomari3107.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And then...uh. Hm. I could stuff it in my pocket if I had any.)" # @t_stomari3108.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(I didn’t think this through did I?)" # @t_stomari3109.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_thinking as tomari
    t_ch_tomari "What’cha got there, [slot_playerName]?" # @t_stomari3110.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(!!!!)" # @t_stomari3111.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Think fast, [slot_playerName]!)" # @t_stomari3112.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh, um." # @t_stomari3112.01 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    extend " (FASTER THAN THAT!)" # @t_stomari3112.02 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s." # @t_stomari3112.03 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uhhhhhhhhhhhh." # @t_stomari3113.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "Nothing?" # @t_stomari3114.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Don’t be silly. Anyone could see it’s a little blurry but very important." # @t_stomari3115.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Darn it, how does a blind guy see so well!)" # @t_stomari3116.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Well, it’s uh blueprints I kinda guess." # @t_stomari3116.01 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_frustrated as tomari
    t_ch_tomari "Yeah. I can just about make ‘em out from here." # @t_stomari3117.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Sort of a…" # @t_stomari3118.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Robot, I’d say. A super robot." # @t_stomari3119.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I guess he’s a little LESS blind at a distance.)" # @t_stomari3120.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It, well, uh." # @t_stomari3120.01 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It is what it is." # @t_stomari3121.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_smile as tomari
    t_ch_tomari "It looks brilliant!" # @t_stomari3122.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(Seriously? He doesn’t know he drew it?!)" # @t_stomari3123.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "I used to think I was a great inventor, but those designs of yours revolutionized my best work in a matter of minutes!" # @t_stomari3124.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Hrm, well, I kind of did. He would’ve thrown the blueprints away if it weren’t for me?)" # @t_stomari3125.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And if letting him think I’m a little more responsible for them than I actually am is what lets me hang out with Tomari a little more," # @t_stomari3126.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " and to keep him out of trouble a little longer, and to maybe get to know him a little better," # @t_stomari3126.00a self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " and then spin it into a date or something once he finally settles down about this ridiculous ten thousand years of darkness stuff…)" # @t_stomari3126.00b self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(...then where’s the harm?)" # @t_stomari3127.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    with Dissolve(0.5)
    t_ch_cousin "(Right?)" # @t_stomari3128.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh, yeah." # @t_stomari3128.01 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    extend " (WHY AM I PRETENDING TO BE THE ONE WHO DREW IT?!)" # @t_stomari3128.02 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Doing so can only get me into more wacky hijinks!)" # @t_stomari3129.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(It’s the law of the stupid universe!)" # @t_stomari3130.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "We should take those designs to the garage to implement them straight away!" # @t_stomari3131.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "They’re your designs and well beyond anything I could’ve come up with. I’ll just watch and let you do everything. I’d hate to get in your way." # @t_stomari3132.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "(SEE?!?!)" # @t_stomari3133.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " Eheh, uhh, no, you could help." # @t_stomari3133.01 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "You SHOULD help!" # @t_stomari3134.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "A lot." # @t_stomari3135.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I mean, er, the best way to learn is by doing!" # @t_stomari3136.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "[slot_playerName], I know you just don’t want me to think you’re showing off." # @t_stomari3137.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "That’s really not it though!" # @t_stomari3138.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Haha, [slot_playerName]. You’re being much too modest! Let’s go!" # @t_stomari3139.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain zorder 9:
        # ActorEvent
        linear 0.75 alpha 1.0
    extend "{w=0.75}{nw}"
    t_ch_cousin "(WAAAAAHHH!)" # @t_stomari3140.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "(His hand…)" # @t_stomari3141.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(On MY hand…)" # @t_stomari3142.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Um. It’s kind of nice…?)" # @t_stomari3143.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bg_hallway_a as bg
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_tomari "Without my glasses, I’m afraid I won’t be able to see the improvements you’ve made to my super robot." # @t_stomari3144.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain zorder 15
    t_ch_cousin "(AH-HA! That’s how I’ll fake it! He can’t see a thing and I’ll just pretend to fix his robot.)" # @t_stomari3145.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "So, I hope you don’t mind talking me through everything you’re doing." # @t_stomari3146.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "(I CAN’T WIN!)" # @t_stomari3147.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " Uh, y-yeah. Sure I can." # @t_stomari3147.01 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Maybe when we finally get to the garage the whole place will be inexplicably ransacked, and Tomari’s super robot will be destroyed, and I won’t have to do anything because he’ll be too distraught for us to work on it!)" # @t_stomari3147.02 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hm, no, that’s going too far. I shouldn’t hope for horrible things to happen to other people!)" # @t_stomari3148.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’ll stick to hoping for personal crippling tragedies. Like…)" # @t_stomari3149.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Maybe my spine will spontaneously liquefy!)" # @t_stomari3150.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And then I’d have to go to the Nurse’s Office.)" # @t_stomari3151.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Problem solved!)" # @t_stomari3152.00 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Except for needing a spine to live.)" # @t_stomari3152.01 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_frustrated as tomari
    t_ch_tomari "Hey, who’s that blurry figure of shadows?" # @t_stomari3153.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Huh, wha?" # @t_stomari3154.00 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "He just came out of the engineering club!" # @t_stomari3155.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_shadowfigure "Nyahaha!" # @t_stomari3156.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "Anyone who laughs like a vaudeville bad guy is up to no good!" # @t_stomari3157.00 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari
    t_ch_tomari "He’s getting away!" # @t_stomari3158.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_shadowfigure "Nyahaha!" # @t_stomari3159.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "And then he got totally away!" # @t_stomari3160.00 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_frustrated as tomari
    t_ch_tomari "[slot_playerName]! The engineering club!" # @t_stomari3161.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Oh no! You don’t think--!" # @t_stomari3162.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    stop music fadeout 1.0
    t_ch_tomari "I don’t want to say what I think." # @t_stomari3163.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5)
    show i_bg_shopclass as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_shopclass', 'curtainActor': 'curtain', 'curtainFadeTime': '0.5', 'name': '_39'} SettingChange ''>
    # <Events {} events ''>
    show i_tomari_defeated_mortified as tomari
    show i_cousin_exhausted_sad as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.5 alpha 0.0
    $ renpy.pause(0.5)
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "He…" # @t_stomari3164.00 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "He took everything." # @t_stomari3165.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Not everything, Tomari!" # @t_stomari3166.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Some stuff he just...smashed up beyond repair." # @t_stomari3167.00 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "It had to be Dr. Kubota!" # @t_stomari3168.00 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Or one of his agents!" # @t_stomari3169.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Are you sure?" # @t_stomari3170.00 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "That Taira is a bit of a bully." # @t_stomari3171.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "And there’s something about that Anti-Bravoman I just don’t trust!" # @t_stomari3172.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "No. It couldn’t be anyone but Dr. Kubota." # @t_stomari3173.00 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "No one else possesses the breadth of genius to know which technologies to target." # @t_stomari3174.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, they targeted everything though…?" # @t_stomari3175.00 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "We can still catch them if we hurry!" # @t_stomari3176.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_mortified as tomari:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.333 xpos 0.35 
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear 0.3333 xpos 0.7 
    show i_cousin_exhausted_neutral as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.15 
    extend "{w=0.5}{nw}"
    t_ch_digdug "Where are you two going in such a rush!" # @t_stomari3177.00 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "GULP!" # @t_stomari3178.00 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "“Gulp,” eh? That’s troublemakers talk!" # @t_stomari3179.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_frustrated as tomari
    t_ch_tomari "What?! No it isn’t! It’s not even a word!" # @t_stomari3180.00 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Onomatopoeia is, by definition, a word!" # @t_stomari3181.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Thought you were supposed to be some kind of brainiac, Tomari." # @t_stomari3182.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari
    t_ch_tomari "We haven’t time for this!" # @t_stomari3183.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Hm, yes, rushing. Another telltale sign of the troublemaker." # @t_stomari3184.00 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I can’t see into the future." # @t_stomari3185.00 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Not yet anyway." # @t_stomari3186.00 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "So, I can’t know where you’re going." # @t_stomari3187.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "But I can see where you came FROM!" # @t_stomari3188.00 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "And it’s the engineering club room." # @t_stomari3189.00 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "And what’s this???" # @t_stomari3190.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "It’s been completely ransacked and then also destroyed a little in some parts!" # @t_stomari3191.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "Surely you can’t think we did it!" # @t_stomari3192.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "No, I don’t think you did it." # @t_stomari3193.00 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I KNOW YOU MUST HAVE DONE IT!" # @t_stomari3194.00 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "WHAT?!" # @t_stomari3195.00 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    show i_cousin_default_neutral as cousin
    t_ch_tomari "It wasn’t us! It was the shadowy figure!" # @t_stomari3196.00 self.block='Last'
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "The shadowy figure, eh?" # @t_stomari3197.00 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Am I to believe this ALLEGED shadowy figure is an agent from Evil Namco High..." # @t_stomari3198.00 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " who was sent here by your arch nemesis to destroy everything you’ve done in the engineering club..." # @t_stomari3198.00a self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " to set into motion events that will inevitably plunge all of Namco Land into a ten thousand year long reign of darkness?" # @t_stomari3198.00b self.block='Last'
    # <ParallelEvent {'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wow, maybe Tomari really was on to something…)" # @t_stomari3199.00 self.block='Last'
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_smile as tomari
    t_ch_tomari "Yes, that! It’s exactly that!" # @t_stomari3200.00 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "After all this time, and all my warnings, someone finally gets it!" # @t_stomari3201.00 self.block='Last'
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    show i_cousin_default_surprised as cousin
    t_ch_digdug "HAW! WRONG." # @t_stomari3202.00 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "I just made all that up. It’s pure crazy talk." # @t_stomari3203.00 self.block='Last'
    # <ParallelEvent {'name': '_3q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "And that’s how I know you kids are lying." # @t_stomari3204.00 self.block='Last'
    # <ParallelEvent {'name': '_3r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "?!?!?" # @t_stomari3205.00 self.block='Last'
    # <ParallelEvent {'name': '_3s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari
    t_ch_tomari "Why would we destroy our own work?!?" # @t_stomari3206.00 self.block='Last'
    # <ParallelEvent {'name': '_3t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "If you’re asking me to understand what drives troublemakers to indulge in their various debaucheries, then you’re barking up the wrong guy." # @t_stomari3207.00 self.block='Last'
    # <ParallelEvent {'name': '_3u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "There’s only one place for the likes of you." # @t_stomari3208.00 self.block='Last'
    # <ParallelEvent {'name': '_3v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "THE GRAVE!!!" # @t_stomari3209.00 self.block='Last'
    # <ParallelEvent {'name': '_3w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(WHAT?!?)" # @t_stomari3210.00 self.block='Last'
    # <ParallelEvent {'name': '_3x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_digdug "But that’s not until you die eventually." # @t_stomari3211.00 self.block='Last'
    # <ParallelEvent {'name': '_3y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Probably a long time from now. Until then you’ll be in Secret Detention." # @t_stomari3212.00 self.block='Last'
    # <ParallelEvent {'name': '_3z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "What’s so secret about it?" # @t_stomari3213.00 self.block='Last'
    # <ParallelEvent {'name': '_40'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Every moment of your life will be transformed into a detention..." # @t_stomari3214.00 self.block='Last'
    # <ParallelEvent {'name': '_41'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "...OF THE SOUL." # @t_stomari3215.00 self.block='Last'
    # <ParallelEvent {'name': '_42'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(Is that even legal?!?!)" # @t_stomari3216.00 self.block='Last'
    # <ParallelEvent {'name': '_43'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Or possible?)" # @t_stomari3217.00 self.block='Last'
    # <ParallelEvent {'name': '_44'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "But we didn’t do anything wrong!" # @t_stomari3218.00 self.block='Last'
    # <ParallelEvent {'name': '_45'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_tomari "[slot_playerName], tell him!" # @t_stomari3219.00 self.block='Last'
    # <ParallelEvent {'name': '_46'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Tomari’s right!" # @t_stomari3220.00 self.block='Last'
    # <ParallelEvent {'name': '_47'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_digdug "Yeah? Then what’s this!" # @t_stomari3221.00 self.block='Last'
    # <ParallelEvent {'name': '_48'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "(The blueprints! He grabbed them right out of my hand with principal swiftness!)" # @t_stomari3222.00 self.block='Last'
    # <ParallelEvent {'name': '_49'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Hmm. Looks like plans." # @t_stomari3223.00 self.block='Last'
    # <ParallelEvent {'name': '_4A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "BLUE plans." # @t_stomari3224.00 self.block='Last'
    # <ParallelEvent {'name': '_4B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Most likely blue sabotage plans." # @t_stomari3225.00 self.block='Last'
    # <ParallelEvent {'name': '_4C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "No, no, no! They’re for the engineering club’s super robot and I--" # @t_stomari3226.00 self.block='Last'
    # <ParallelEvent {'name': '_4D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Sorry, kids. I don’t speak DETENTIONESE." # @t_stomari3227.00 self.block='Last'
    # <ParallelEvent {'name': '_4E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Not fluently anyway." # @t_stomari3228.00 self.block='Last'
    # <NHSceneChange {'name': '_4F', 'scene': 's_day4'} NHSceneChange ''>
    label s_tomari3__4F:
        # <NHSceneChange {'name': '_4F', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4