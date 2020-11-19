# <Scene scene {'id': 's_lolo3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_lolo3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_lolo3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_lolo3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/school.ogg" loop
    show i_bg_hallway_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_energetic_surprise as cousin zorder 3:
        default
        xpos 0.3 
    show i_lolo_default_grin as lolo zorder 2:
        default
        xpos 0.7 
    show i_king_screaming as king zorder 2:
        default
        xpos 1.5 
        alpha 0.0
        xzoom -1.0 
    show i_digdug_left as digdug zorder 3:
        default
        xpos 1.5 
        alpha 0.0
    t_ch_cousin "Lolo! Wait!" # @t_slolo39.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Oh, so you came after all." # @t_slolo310.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "…" # @t_slolo311.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Why’s she acting all aloof?" # @t_slolo312.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Did she actually want me to come along or what?)" # @t_slolo312.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I go to the nurse’s office sometimes, so King won’t be too suspicious right away." # @t_slolo313.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Let’s go." # @t_slolo313.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "The nurse’s office…?" # @t_slolo314.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Lolo, what’s wrong?!" # @t_slolo314.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy as lolo
    t_ch_lolo "Oh [slot_playerName]…" # @t_slolo315.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I should’ve told you…" # @t_slolo315.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I’m really sick." # @t_slolo316.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "!!" # @t_slolo317.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Lolo-!" # @t_slolo318.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_slumped_grin as lolo
    t_ch_lolo "...Really sick…" # @t_slolo319.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_grin as lolo
    t_ch_lolo "Of sitting in detention." # @t_slolo320.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " So we’re skipping it today." # @t_slolo320.01 self.block='Last'
    show i_lolo_shrug_grin as lolo:
        linear 0.5 xzoom -1.0 
        linear 0.5 xzoom 1.0 
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And now I’m cured! It’s a miracle." # @t_slolo320.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "…" # @t_slolo321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "What? Don’t just stare like that." # @t_slolo322.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Don’t tell me you got fooled by such an obvious joke." # @t_slolo322.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "No, it’s just…" # @t_slolo323.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "You’re smiling a little." # @t_slolo324.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "So?" # @t_slolo325.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "You have a sense of humor…" # @t_slolo326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It really is a miracle." # @t_slolo326.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Well, I’m definitely not smiling anymore." # @t_slolo327.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Congrats on ruining it." # @t_slolo327.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "So why do you go to the nurse’s office?" # @t_slolo328.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "It’s just an easy way to get out of stuff." # @t_slolo329.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_grin as lolo
    extend " Even if they suspect you’re faking, nobody really argues." # @t_slolo329.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Sometimes sitting in class just gets so overwhelming, you know?" # @t_slolo330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "What…" # @t_slolo331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You mean like the homework and stuff?" # @t_slolo332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "No… I mean…" # @t_slolo333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "Of everyone looking at you…" # @t_slolo334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Thinking you’re stupid…" # @t_slolo335.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Seeing you in that gross classroom fluorescent light…" # @t_slolo335.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "As if you didn’t look ugly enough already." # @t_slolo336.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I don’t think anyone’s looking at you." # @t_slolo337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Or thinking about you that much." # @t_slolo337.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I mean, no offense, but isn’t that kinda self-centered?" # @t_slolo338.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Why would anyone care, even if you were ugly?" # @t_slolo338.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_raisedbrow as lolo
    t_ch_lolo "I guess you’re right. Nobody really cares." # @t_slolo339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_frustrated as lolo
    extend " About anything else…" # @t_slolo339.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "They’re all just trying to pass the time." # @t_slolo340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " That’s all anyone does." # @t_slolo340.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    extend " What good is time anyway, if people are always just looking for ways to kill it?" # @t_slolo340.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(I’m starting to get annoyed at all her talking like this…" # @t_slolo341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I mean, even she’s gotta see it’s overkill, right?)" # @t_slolo342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_grin as lolo
    t_ch_lolo "Anyway… let’s get going." # @t_slolo343.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Why’d you even ask me to come along?" # @t_slolo344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I mean… I don’t even know what we’re doing yet…" # @t_slolo344.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_melancholy as lolo
    t_ch_lolo "You ask so many questions all the time…" # @t_slolo345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_melancholy_blush as lolo
    with Dissolve(0.5)
    t_ch_lolo "I just thought you would come because I thought you were cool." # @t_slolo346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Y-you…" # @t_slolo347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You thought I was…" # @t_slolo347.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Cool?" # @t_slolo348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Not cool-cool." # @t_slolo349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy as lolo
    extend " Just…. chill." # @t_slolo349.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_grin as lolo
    extend " You know, cool." # @t_slolo349.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "…" # @t_slolo350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I totally understand what you’re talking about!" # @t_slolo351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Heh." # @t_slolo352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_grin as lolo
    extend " Don’t hurt yourself, cupcake." # @t_slolo352.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "…" # @t_slolo353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Oh, come on." # @t_slolo354.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_grin as lolo
    t_ch_lolo "Anyway… my friend should be meeting us here soon to give me some stuff." # @t_slolo355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    extend " But you have to promise not to tell anyone." # @t_slolo355.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Okay?" # @t_slolo355.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Uh…" # @t_slolo356.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " Do you really trust me that much?" # @t_slolo356.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "..." # @t_slolo357.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(I’m not gonna get a real answer from her, am I.)" # @t_slolo358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "...Okay, Lolo." # @t_slolo359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Tell me." # @t_slolo359.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " I can keep a secret." # @t_slolo359.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Well…" # @t_slolo360.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "You know how school is totally pointless?" # @t_slolo361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "And how everything we’re supposed to learn here is just stupid propaganda?" # @t_slolo362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " And how it only rewards nerds who can memorize endless trivial details…" # @t_slolo362.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That don’t actually have anything to do with anything?" # @t_slolo362.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(School… is it pointless?)" # @t_slolo363.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I dunno…" # @t_slolo364.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " I kinda like school." # @t_slolo364.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I even enjoy math, sometimes!" # @t_slolo365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s like rolling up numbers," # @t_slolo365.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " but with your mind instead of a ball." # @t_slolo365.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Why am I not surprised." # @t_slolo366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Eh heh." # @t_slolo367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_raisedbrow as lolo
    t_ch_lolo "Even you have to get bored in class sometimes though, right?" # @t_slolo368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "...Please tell me you do." # @t_slolo369.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well…" # @t_slolo370.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    extend " Sure, but that doesn’t mean-" # @t_slolo370.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "What if you could skip through your classes easily…" # @t_slolo371.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " With no effort at all?" # @t_slolo371.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Perfect grades without having done any homework…" # @t_slolo372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Perfect attendance without ever going to class." # @t_slolo372.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "Wouldn’t you want to do that?" # @t_slolo373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh, I dunno." # @t_slolo374.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The only way to do that, I think…" # @t_slolo374.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Would be to enter a cheat code." # @t_slolo375.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Haha." # @t_slolo376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_grin as lolo
    extend " You even whispered the word “cheat code”." # @t_slolo376.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_grin as lolo
    extend " [slot_playerName], are you seriously even real?" # @t_slolo376.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "So that is what you’re talking about?" # @t_slolo377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Lolo, you wouldn’t actually do that, right?!" # @t_slolo378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "…" # @t_slolo379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Why do you think I was in detention in the first place?" # @t_slolo380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Cheat codes?!" # @t_slolo381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Lolo!" # @t_slolo381.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified as cousin
    extend " You could really mess yourself up that way!" # @t_slolo381.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_raisedbrow as lolo
    t_ch_lolo "Hey, calm down." # @t_slolo382.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I didn’t actually get a chance to enter the code." # @t_slolo382.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I got caught in the act." # @t_slolo382.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "But…" # @t_slolo383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But I heard the other detention kids talking about some guy who used cheat codes last year!" # @t_slolo383.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "He got unlimited recess…" # @t_slolo384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But when Principal DigDug found out, the guy got expelled from Namco High!" # @t_slolo384.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "For good!" # @t_slolo385.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_raisedbrow as lolo
    show i_cousin_energetic_neutral as cousin
    t_ch_lolo "So what?" # @t_slolo386.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    extend " I know a guy who can get me a way better cheat code than that." # @t_slolo386.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "And that kid was so dumb!" # @t_slolo387.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_raisedbrow as lolo
    extend " Of course somebody’s gonna notice if you’re in recess all the time." # @t_slolo387.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "But if I can godmode my way through class…" # @t_slolo388.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "I dunno." # @t_slolo389.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    extend " The teachers will just think I’m studying harder." # @t_slolo389.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Just because you think everyone is stupid doesn’t mean they actually are!" # @t_slolo390.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "People are gonna notice you’re using cheat codes." # @t_slolo391.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    extend " You’d be expelled for sure!" # @t_slolo391.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_slumped_frustrated as lolo
    t_ch_lolo "What do you care?" # @t_slolo392.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Maybe that’d at least be interesting." # @t_slolo393.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "Lolo! Shut up!" # @t_slolo394.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_frustrated as lolo
    t_ch_lolo "… !!" # @t_slolo395.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "Sorry- I just-" # @t_slolo396.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "How can you talk about yourself that way?!" # @t_slolo397.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Don’t you care about yourself at all?!" # @t_slolo397.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "I dunno." # @t_slolo398.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Do I?" # @t_slolo398.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "...What?" # @t_slolo399.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Why are you asking me that..." # @t_slolo399.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Do I care about myself?" # @t_slolo3100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " I really can’t tell anymore." # @t_slolo3100.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Sometimes it feels more like…" # @t_slolo3101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m only watching myself." # @t_slolo3101.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Waiting to see if I ever do anything cool." # @t_slolo3101.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "...Is that why you invited me along?" # @t_slolo3102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " To be an audience?" # @t_slolo3102.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " To see you do something “cool”?" # @t_slolo3102.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Yeah, right." # @t_slolo3103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_raisedbrow as lolo
    extend " C’mon, [slot_playerName]. Give me some credit." # @t_slolo3103.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I really don’t care about seeming cool." # @t_slolo3104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I really did just want some cheat codes for easy A’s." # @t_slolo3104.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "It just doesn’t seem like you…" # @t_slolo3105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Oh, no?" # @t_slolo3106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "You’re a sweet girl, Lolo…" # @t_slolo3107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I can tell." # @t_slolo3107.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I think you wanted me here…" # @t_slolo3108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Because you think of me as a nice person…" # @t_slolo3109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And you knew I would stop you." # @t_slolo3110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "…" # @t_slolo3111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "You don’t really want to use cheat codes." # @t_slolo3112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But you’re stuck playing this stupid “I don’t care” game." # @t_slolo3112.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "But you figured I’m such a do-gooder," # @t_slolo3113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " you could count on me to stop you instead." # @t_slolo3113.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Is that it?" # @t_slolo3114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "You…" # @t_slolo3115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "You’re just like Klonoa." # @t_slolo3116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "You keep talking about Klonoa…" # @t_slolo3117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Who is he?" # @t_slolo3117.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Did he do something bad?" # @t_slolo3117.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_raisedbrow as lolo
    t_ch_lolo "No!" # @t_slolo3118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " He didn’t do anything." # @t_slolo3118.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "But he was like you… always nice to me." # @t_slolo3119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Totally just taking pity because of how dumb I was." # @t_slolo3119.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "But he had no idea, and neither do you…" # @t_slolo3120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "How much worse all that nice stuff made me feel." # @t_slolo3121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Whatever he did to you…" # @t_slolo3122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    extend " You didn’t deserve it!" # @t_slolo3122.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_raisedbrow as lolo
    t_ch_lolo "It wasn’t his fault!" # @t_slolo3123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    show i_cousin_energetic_neutral as cousin
    extend " He just made me realize…" # @t_slolo3123.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "That sometimes people try their hardest," # @t_slolo3124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    extend " but it never matters, because it never works out." # @t_slolo3124.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Just like me, working so hard to be a priestess." # @t_slolo3125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_30', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But I never got any better." # @t_slolo3125.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_31', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_slumped_frustrated as lolo
    extend " I was always so hopeless at it, but…" # @t_slolo3125.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_32', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I actually believed I could do it…" # @t_slolo3126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_33', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Just like all the other dumb students in this school." # @t_slolo3127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_34', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_shrug_raisedbrow as lolo
    t_ch_lolo "Working so hard to learn!" # @t_slolo3128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_35', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Not knowing it’ll never take them anywhere." # @t_slolo3128.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_36', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_raisedbrow as lolo
    t_ch_lolo "It just makes me so sad, okay?!" # @t_slolo3129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_37', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "And maybe I wanted to skip over that with a cheat code." # @t_slolo3130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_38', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_raisedbrow as lolo
    extend " Is that so bad?!" # @t_slolo3130.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_39', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Well…" # @t_slolo3131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Maybe this isn’t what Klonoa would’ve done, but..." # @t_slolo3131.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I’m not going to try to stop you." # @t_slolo3132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I believe you can do that yourself." # @t_slolo3133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "…" # @t_slolo3134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    show i_lolo_crossed_frustrated as lolo:
        xzoom -1.0 
    show i_king_screaming as king:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    play sound "sfx/kingroar1.ogg"
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.15 
    show i_lolo_crossed_frustrated as lolo:
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    show i_king_screaming as king:
        # ShowWithAtl
        linear 0.333 xpos 0.85 
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.333 xpos 0.7 
    stop music fadeout 1.0
    extend "{w=0.5}{nw}"
    t_ch_king "ROAR!!" # @t_slolo3135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_confident as king
    t_ch_digdug "WHAT’S GOING ON HERE?!" # @t_slolo3136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "GAH!" # @t_slolo3137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " How long have you been standing behind me!" # @t_slolo3137.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Long enough to know you two are SKIPPING DETENTION!" # @t_slolo3138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And for that…" # @t_slolo3138.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You will have…" # @t_slolo3138.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_screaming as king
    play sound "sfx/kingroar3.ogg"
    t_ch_digdug "DOUBLE DETENTION!" # @t_slolo3139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_confident as king
    t_ch_lolo "(Sigh)." # @t_slolo3140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_king "ROAR!" # @t_slolo3141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "You two shall face DETENTION LEVEL SEVEN:" # @t_slolo3142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " ABSTRACT CONCEPT OF DETENTION!" # @t_slolo3142.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "AUGH!" # @t_slolo3143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Wait, I mean-" # @t_slolo3144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What?" # @t_slolo3145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "You two…" # @t_slolo3146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Will spend 20 minutes…" # @t_slolo3147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "DOING WHATEVER YOU WANT!" # @t_slolo3148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Um…" # @t_slolo3149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "How is that detention, exactly?" # @t_slolo3150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "AHA! THAT’S WHY ITS SO BRILLIANT!" # @t_slolo3151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Anything you do in the next 20 minutes…" # @t_slolo3151.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "BECOMES detention…" # @t_slolo3152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Simply because I said it was!" # @t_slolo3153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Pushing the boundaries of what society calls “detention”!" # @t_slolo3154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "…" # @t_slolo3155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "…" # @t_slolo3156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_king "ROAarrr…." # @t_slolo3157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "I know, right?!" # @t_slolo3158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "…" # @t_slolo3159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...Okay…" # @t_slolo3160.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5) # Curtain fade
    show i_bg_rooftop_sunset as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_rooftop_sunset', 'curtainActor': 'curtain', 'curtainFadeTime': '0.5', 'name': '_3j', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    $ AudioEvent('music', 1.0, 1.0)
    show i_lolo_default_grin as lolo
    hide digdug
    hide king
    show i_lolo_default_grin as lolo:
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.5 alpha 0.0
    $ renpy.pause(0.5) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_3k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(And so, we had some time to ourselves to talk." # @t_slolo3161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Lolo suggested we do our detention on the roof." # @t_slolo3162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It seemed as good a place as any.)" # @t_slolo3162.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "This spot is pretty, isn’t it." # @t_slolo3163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Oh!" # @t_slolo3164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    extend " Is it a place you actually like?" # @t_slolo3164.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy as lolo
    t_ch_lolo "Not exactly…" # @t_slolo3165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It just feels like the kinda place that I should like." # @t_slolo3165.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "So…" # @t_slolo3166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "If King and Principal Dig Dug hadn’t stopped us…" # @t_slolo3167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Would you have still tried to get the cheat code?" # @t_slolo3167.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated_blush as lolo
    t_ch_lolo "...Think whatever you want." # @t_slolo3168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Whatever makes you feel better." # @t_slolo3168.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Or not, I guess." # @t_slolo3169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Lolo…" # @t_slolo3170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Were you always like this?" # @t_slolo3171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_40', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "...Well…" # @t_slolo3172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_41', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "No. But I didn’t change exactly, either. It’s hard to explain." # @t_slolo3173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_42', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Was it because of… that person?" # @t_slolo3174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_43', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_grin as lolo
    t_ch_lolo "Heh. What, are you jealous? He wasn’t my boyfriend or anything." # @t_slolo3175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_44', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "N-no!" # @t_slolo3176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_45', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "I just…" # @t_slolo3177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_46', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Want to understand." # @t_slolo3177.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_47', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_melancholy_blush as lolo
    t_ch_lolo "...Yeah." # @t_slolo3178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_48', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Because of Klonoa." # @t_slolo3178.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_49', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "But…" # @t_slolo3179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Not really in the way you’re thinking." # @t_slolo3179.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "In what way, then?" # @t_slolo3180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "Why are you asking so many stupid questions?" # @t_slolo3181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I’m sorry." # @t_slolo3182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I just want to understand you." # @t_slolo3183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_raisedbrow as lolo
    t_ch_lolo "Well, join the club." # @t_slolo3184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Do you have a picture of Klonoa?" # @t_slolo3185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_crossed_frustrated as lolo
    t_ch_lolo "…" # @t_slolo3186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_lolo_default_grin as lolo
    t_ch_lolo "Yeah…" # @t_slolo3187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "It’s here in the pocket of my dress actually." # @t_slolo3188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain2 zorder 8:
        default
        alpha 0.0
        linear 0.333 alpha 1.0
    show i_event_lolo_yearbook as yearbook zorder 9:
        default
        alpha 0.0
        linear 0.333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_cousin "...This looks like… It was cut out of a yearbook." # @t_slolo3189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Yeah." # @t_slolo3190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "From when I was studying magic at the priestess school." # @t_slolo3191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I thought you…" # @t_slolo3192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Didn’t like yearbooks…" # @t_slolo3192.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "…" # @t_slolo3193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I wish you’d just give me a straight answer." # @t_slolo3194.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "I bet you’re really regretting following me out to the hall right now." # @t_slolo3195.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "…" # @t_slolo3196.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Actually…" # @t_slolo3197.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Not really." # @t_slolo3197.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Heh." # @t_slolo3198.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "You’re…" # @t_slolo3199.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_lolo "Pretty stupid, [slot_playerName]." # @t_slolo3200.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_4Y', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_lolo3__4Y:
        # <NHSceneChange NHSceneChange {'name': '_4Y', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4