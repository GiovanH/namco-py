# <Scene scene {'id': 's_valk5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_valk5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_valk5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_valk5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_valk5_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        play music "bgm/romance.ogg" loop
        show i_bg_cliff_day as bg zorder 0 at default
        show i_event_valkyrie_ending as event zorder 11:
            default
            alpha 0.0
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_cousin_default_neutral as cousin zorder 2:
            default
            xpos 0.3 
        show i_valkyrie_default_grin as valkyrie zorder 2:
            default
            xpos 0.7 
        show i_pacman_left as pacman zorder 2:
            default
            xpos 1.35 
            alpha 0.0

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I couldn't do anything else today... I just kept thinking of how I was meeting Valkyrie here.)" # @t_svalk50.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    with Dissolve(0.5)
    t_ch_cousin "(My heart is pounding. I've got butterflies in my stomach... I wish I could roll them up.)" # @t_svalk51.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Hey cutie." # @t_svalk52.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Hey ... Cutie." # @t_svalk53.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "LOL... I think it's better when I say it." # @t_svalk54.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "M-me too. It's kind of embarrassing to say..." # @t_svalk55.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_grin as valkyrie
    t_ch_valkyrie "Heyyy, what's that supposed to mean!" # @t_svalk56.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified_blush as cousin
    t_ch_cousin "No no, when I say it!" # @t_svalk57.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_wink as valkyrie
    t_ch_valkyrie "I'll let it slide." # @t_svalk58.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grin as valkyrie:
        # ShowWithAtl
        linear .333 xpos 0.54 
    show i_cousin_default_surprised_blush as cousin
    extend "{w=0.333}{nw}"
    t_ch_cousin "(She took my hand in hers. It's probably okay if I lean against her, right?)" # @t_svalk59.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I..." # @t_svalk510.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " I'm gonna do it." # @t_svalk510.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Phew." # @t_svalk510.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Here I go.)" # @t_svalk510.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin:
        # ShowWithAtl
        linear .333 xpos 0.32 
    extend "{w=0.333}{nw}"
    t_ch_cousin "(Is... Is this okay?!)" # @t_svalk511.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie:
        # ShowWithAtl
        linear .333 xpos 0.52 
    extend "{w=0.333}{nw}"
    t_ch_cousin "(Oh... She leaned into me, too.)" # @t_svalk512.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This is nice.)" # @t_svalk513.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wait... )" # @t_svalk514.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie:
        # ShowWithAtl
        linear .333 xpos 0.51 
    extend "{w=0.333}{nw}"
    t_ch_cousin "(Is she... Is she turning her head?)" # @t_svalk515.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin:
        # ShowWithAtl
        linear .333 xpos 0.33 
    extend "{w=0.333}{nw}"
    t_ch_cousin "(Now... Now I'm doing it... )" # @t_svalk516.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Are we doing this?" # @t_svalk517.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " IS THIS HAPPENING?)" # @t_svalk517.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_event_valkyrie_ending as event:
        # ShowWithAtl
        linear .5 alpha 1.0
    extend "{w=0.5}{nw}"
    # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_bg_cliff_night_fireflies as bg
    show i_event_valkyrie_ending as event:
        # ShowWithAtl
        pause 3.0 
        linear 0.333 alpha 0.0
    show i_cousin_default_neutral_blush as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.38 
    show i_valkyrie_default_grinblush as valkyrie:
        # ShowWithAtl
        linear 0.5 xpos 0.62 
    extend "{w=6.333}{nw}"
    t_ch_cousin "(Now she's just looking at me quietly... )" # @t_svalk518.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I... I've never actually kissed anyone before." # @t_svalk519.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "That was my first kiss." # @t_svalk520.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Whoa." # @t_svalk521.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Haha. I guess that's pretty special..." # @t_svalk522.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It totally is." # @t_svalk523.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_melancholy as valkyrie
    t_ch_valkyrie "Yeah..." # @t_svalk524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Valkyrie... Is something wrong?" # @t_svalk525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_melancholy as valkyrie
    t_ch_valkyrie "I just feel... A little guilty about pwning you the other day." # @t_svalk526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I shouldn't have done that." # @t_svalk526.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "Oh, that? I don't mind at all." # @t_svalk527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_melancholy as valkyrie
    t_ch_valkyrie "You should!" # @t_svalk528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Valkyrie..." # @t_svalk529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I lost control because I didn't want to tell you why I was REALLY in detention." # @t_svalk530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Whoa... Here it comes.)" # @t_svalk531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I DID try to turn the clock back..." # @t_svalk532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But the real reason is because I have to get home." # @t_svalk532.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "........" # @t_svalk533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    extend " ......whaaaaaat?" # @t_svalk533.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What do you mean? This IS your home." # @t_svalk534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You and me and everyone at Namco High!" # @t_svalk534.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "No... It's not. [slot_playerName], I come from a place far far away..." # @t_svalk535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " A place called Marvel Land." # @t_svalk535.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "In Marvel Land, there was a clock that had sealed away an evil wizard named Zouna." # @t_svalk536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Zouna can use his magic to pwn time itself." # @t_svalk536.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Someone accidentally unsealed the clock with a magic key..." # @t_svalk537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Zouna was freed, and he sent me to the future so I couldn't stop is plans… whatever they are." # @t_svalk537.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Who knows what he's doing to Marvel Land right now..." # @t_svalk538.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_melancholy as valkyrie
    t_ch_valkyrie "Ever since then, I've been trying to get back." # @t_svalk539.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The big clock at Namco High looked familiar, so I asked that bookworm Nidia to help me research it." # @t_svalk539.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "It turns out that the clock at Namco High is built with parts from the clock that trapped Zouna in my time..." # @t_svalk540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "So I thought I could use it to get back." # @t_svalk541.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That's why I tried turning the hands back." # @t_svalk541.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It didn't work, and I got detention." # @t_svalk541.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "But it did convince Nidia that I need the key in order to get back to Marvel Land..." # @t_svalk542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_melancholy as valkyrie
    t_ch_valkyrie "I have to go back." # @t_svalk543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " To save everyone." # @t_svalk543.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "....." # @t_svalk544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "........." # @t_svalk545.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "................." # @t_svalk546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "............................" # @t_svalk547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin ".................................." # @t_svalk548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Wow." # @t_svalk549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Does this mean that one day... You'll have to leave?" # @t_svalk550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_melancholy as valkyrie
    t_ch_valkyrie "Yes..." # @t_svalk551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But I thought..." # @t_svalk552.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I know... I'm sorry." # @t_svalk553.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I wanted to take my time here to see what it's like to be a normal teenager... But I shouldn't have let it go so far." # @t_svalk554.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " IDK… You must be..." # @t_svalk554.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_melancholy as valkyrie
    extend " Really mad at me." # @t_svalk554.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I don't know what I am..." # @t_svalk555.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " This is a lot." # @t_svalk555.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I'm really sorry. I guess you hold something in for too long and suddenly it all comes out at once..." # @t_svalk556.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Yeah... Valkyrie, I really like you. Like, a lot... More than the biggest katamari I've ever rolled." # @t_svalk557.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I'm so sorry... I should have said something sooner. I didn't think it would go this far." # @t_svalk558.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_melancholy as valkyrie
    t_ch_valkyrie "OMG, [slot_playerName]… This is all my fault." # @t_svalk559.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It's okay if you hate me." # @t_svalk559.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "[slot_playerName]... What am I going to do?" # @t_svalk560.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        easeout 5 xpos 0.8 
    $ renpy.pause(2) # ParallelEvent Delay
    # <ParallelEvent ParallelEvent {'delay': '2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_melancholy as valkyrie:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.25 xpos 0.32 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.25 xpos 0.1 
    $ renpy.pause(0.25, hard=True) # TimedPause
    extend "{w=5.0}{nw}"
    # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
    stop sound
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "... BE TRUE TO YOURSELF" # @t_svalk561.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        easeout 5 xpos 1.35 
    $ renpy.pause(5.0, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_melancholy as valkyrie:
        # ShowWithAtl
        linear 0.25 xpos 0.65 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.25 xpos 0.35 
    extend "{w=0.25}{nw}"
    t_ch_cousin "Valkyrie... Pac-Man's right." # @t_svalk562.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_melancholy as valkyrie:
        linear .333 xzoom 1.0 
    extend " I can't say I'm happy." # @t_svalk562.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad_blush as cousin
    t_ch_cousin "But the things you've been holding in... You're a fun person. I'm amazed at how fun you are." # @t_svalk563.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "And now I know that you're the kind of person who can shoulder a burden with a smile." # @t_svalk564.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin:
        # ShowWithAtl
        linear .25 xpos 0.45 
    extend "{w=0.25}{nw}"
    t_ch_cousin "(I give her a kiss on the cheek.)" # @t_svalk565.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin:
        # ShowWithAtl
        linear .25 xpos 0.4 
    extend "{w=0.25}{nw}"
    t_ch_cousin "It's very brave. So I can be brave too." # @t_svalk566.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_laugh_blush as cousin
    t_ch_cousin "I don't know what the future holds... But I'll be here to help you, however you need me." # @t_svalk567.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie:
        # ShowWithAtl
        linear .25 xpos 0.62 
    extend "{w=0.25}{nw}"
    t_ch_valkyrie "[slot_playerName]..." # @t_svalk568.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(She's holding my hand again. It feels so nice... I hold it tight. As tight as I can, like I can keep her from floating away.)" # @t_svalk569.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "The fireflies... Are really beautiful tonight." # @t_svalk570.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "They're pretty cute." # @t_svalk571.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_1a', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_valk5__1a:
        # <NHSceneChange NHSceneChange {'name': '_1a', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5