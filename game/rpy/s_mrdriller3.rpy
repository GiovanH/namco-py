# <Scene scene {'id': 's_mrdriller3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_mrdriller3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_mrdriller3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_mrdriller3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_mrdriller3_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        play music "bgm/aroundtown.ogg" loop
        show i_bg_quad_bleachers as bg zorder 0 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha -0.0
        show i_cousin_energetic_surprise as cousin zorder 4:
            default
            xpos 0.25 
        show i_mrdriller_drillup_happy as mrdriller zorder 3:
            default
            xpos 0.7 
            alpha 1.0
        show i_taira_steveholt_happy as taira zorder 1:
            default
            xpos 0.9 
            alpha 0.0
        show i_albatross_toocool_smirk as albatros zorder 0:
            default
            xpos 0.5 
            alpha 0.0
        show i_aki_default_smile as aki zorder 2:
            default
            xpos 0.7 
            alpha 0.0
        show i_meowkie_normal_happy as meowkie zorder 3:
            default
            xpos 0.85 
            alpha 0.0
        show i_digdug_left as digdug zorder 2:
            default
            alpha 0.0
            xpos 0.8 
        show i_sw_black as curtain2 zorder 9:
            default
            alpha 0.0

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Mr. Driller!" # @t_smrdriller39.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Thank goodness I found you." # @t_smrdriller39.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What are you doing?" # @t_smrdriller310.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Aren’t you afraid someone’s going to see you?" # @t_smrdriller310.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I’ll be done really quick!" # @t_smrdriller311.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_smug as mrdriller
    extend " All the teachers are gone now, so I bet they won’t notice me." # @t_smrdriller311.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "You know, there’s such a thing as taking your passion too far…" # @t_smrdriller312.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "Nonsense!" # @t_smrdriller313.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_excited as mrdriller
    t_ch_mrdriller "Oh haha, wow, you were right!" # @t_smrdriller314.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " There’s TONS of great dirt out today." # @t_smrdriller314.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_happy as mrdriller
    t_ch_mrdriller "How did you know?" # @t_smrdriller315.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You must be like, a secret digging sage or something." # @t_smrdriller315.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Oh haha… Gosh.. Wow… I wouldn’t go that far...." # @t_smrdriller316.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified_blush as cousin
    extend " (Wh- Seriously?! THAT’S making me blush?!)" # @t_smrdriller318.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "You know… I bet if Dad could see me now…" # @t_smrdriller319.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " He’d be proud of what a good job I’m doing, you know?" # @t_smrdriller319.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I mean… how can you not appreciate this?" # @t_smrdriller319.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_happy as mrdriller
    t_ch_mrdriller "The sun on your back… The drills happily buzzing away…" # @t_smrdriller320.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s like heaven!" # @t_smrdriller320.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Er, don’t look now, but I think your father…" # @t_smrdriller321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "CAN see you now…" # @t_smrdriller322.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_shock as mrdriller
    t_ch_mrdriller "WHAAAT?!" # @t_smrdriller323.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "Right over there, see?" # @t_smrdriller324.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That’s Principal DigDug standing there, isn’t it?" # @t_smrdriller324.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "If we hurry, we can get back to detention before he gets here!" # @t_smrdriller325.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "Oh…." # @t_smrdriller326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Phew!" # @t_smrdriller326.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " [slot_playerName], you’re silly." # @t_smrdriller326.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "That’s not my dad!" # @t_smrdriller327.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_smug as mrdriller
    t_ch_mrdriller "That’s the STATUE of my dad." # @t_smrdriller328.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The one I, uh…" # @t_smrdriller328.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Kinda sorta defaced." # @t_smrdriller328.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Oh… Yeah." # @t_smrdriller329.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Now that I’m looking a little more closely…" # @t_smrdriller329.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That’s definitely just a statue." # @t_smrdriller329.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And he has a big fat mustache dug right into his face." # @t_smrdriller330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Looks pretty suave, actually.)" # @t_smrdriller330.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_happy as mrdriller
    t_ch_mrdriller "Although wouldn’t it be great if I could do that to my dad for real? Haha!" # @t_smrdriller331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "!!!!" # @t_smrdriller332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Mr. Driller! That’s taking it too far!" # @t_smrdriller332.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "I… I only meant metaphorically!" # @t_smrdriller333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What would that even be a metaphor for, anyway?!" # @t_smrdriller334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I dunno, some kinda emotional trauma roughly equal to the one he’s inflicting on me?" # @t_smrdriller335.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You know… father-son stuff." # @t_smrdriller335.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "… Mr. Driller…" # @t_smrdriller336.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I know you don’t like to admit it, but…" # @t_smrdriller336.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "You’ve got some really dark thoughts in that helmet of yours." # @t_smrdriller337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Can’t you admit that your relationship with your dad is…" # @t_smrdriller338.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    extend " Not exactly typical?" # @t_smrdriller338.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_shock as mrdriller
    t_ch_mrdriller "…" # @t_smrdriller339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "Yeah…" # @t_smrdriller340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I know." # @t_smrdriller341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I’m not trying to be nosy, it’s just…" # @t_smrdriller342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " It’s not healthy to keep stuff bottled up like that." # @t_smrdriller342.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "...It’s not like I...actually HATE my dad or anything..." # @t_smrdriller343.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I just get so angry, you know?" # @t_smrdriller343.04 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_sad as mrdriller
    t_ch_mrdriller "He shouldn’t have just… given up." # @t_smrdriller344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Mr. Driller…" # @t_smrdriller345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Why did your dad give up digging?" # @t_smrdriller345.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You said something about your mom…" # @t_smrdriller345.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Did she not like it, or something?" # @t_smrdriller345.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "He said he got too…" # @t_smrdriller346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_confused as mrdriller
    t_ch_mrdriller "“Obsessive”..." # @t_smrdriller347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/drill1.ogg"
    t_ch_mrdriller "But I don’t know." # @t_smrdriller348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_confused as mrdriller:
        # ShowWithAtl
        linear .2 ypos 0.55 
    play sound "sfx/drill2.ogg"
    extend "{w=0.2}{nw}"
    extend " What’s wrong with putting what you love above everything else?" # @t_smrdriller348.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_confused as mrdriller:
        # ShowWithAtl
        linear .2 ypos 0.6 
    play sound "sfx/drill1.ogg"
    extend "{w=0.2}{nw}"
    extend " Isn’t that how you achieve greatness in life?" # @t_smrdriller348.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    show i_mrdriller_slumped_confused as mrdriller:
        # ShowWithAtl
        linear .2 ypos 0.7 
    play sound "sfx/drill2.ogg"
    extend "{w=0.2}{nw}"
    t_ch_cousin "Hey, watch it!" # @t_smrdriller349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_confused as mrdriller:
        # ShowWithAtl
        linear .2 ypos 0.8 
    play sound "sfx/drill1.ogg"
    extend "{w=0.2}{nw}"
    extend " You’re digging faster and faster…" # @t_smrdriller349.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_confused as mrdriller:
        # ShowWithAtl
        linear .2 ypos 0.85 
    play sound "sfx/drill2.ogg"
    extend "{w=0.2}{nw}"
    extend " Don’t you think that’s a little too much?" # @t_smrdriller349.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller:
        # ShowWithAtl
        linear .2 ypos 0.9 
    play sound "sfx/drill1.ogg"
    extend "{w=0.2}{nw}"
    t_ch_mrdriller "That’s what Dad said…" # @t_smrdriller350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller:
        # ShowWithAtl
        linear .2 ypos 0.95 
    play sound "sfx/drill2.ogg"
    extend "{w=0.2}{nw}"
    extend " That he dug “too much”." # @t_smrdriller350.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller:
        # ShowWithAtl
        linear .2 ypos 1.0 
    play sound "sfx/drill1.ogg"
    extend "{w=0.2}{nw}"
    t_ch_mrdriller "But he was also the one who told me…" # @t_smrdriller351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller:
        # ShowWithAtl
        linear .4 ypos 1.1 
    play sound "sfx/drill2.ogg"
    extend "{w=0.4}{nw}"
    t_ch_mrdriller "That if you never stopped digging, you could get all the way to the other side of the world!" # @t_smrdriller352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller:
        # ShowWithAtl
        linear .4 ypos 1.3 
    extend "{w=0.4}{nw}"
    t_ch_cousin "Mr. Driller!" # @t_smrdriller353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    extend " You have to stop!" # @t_smrdriller353.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You’re digging way too far and way too fast!" # @t_smrdriller353.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_cry as mrdriller
    t_ch_mrdriller "Don’t tell me what to do, [slot_playerName]!" # @t_smrdriller354.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I thought you understood how I feel about digging!" # @t_smrdriller354.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Of course I do! It’s kinda impossible to miss!" # @t_smrdriller355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But..." # @t_smrdriller356.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " This seems more like anger than passion…" # @t_smrdriller356.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And besides, if you’re not careful, you’re going to hit a-" # @t_smrdriller357.00 self.block='Last'
    play sound "sfx/drill1.ogg"
    play sound "sfx/crashwall.ogg"
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...Pipe." # @t_smrdriller358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/rushingwater.ogg" loop
    show i_mrdriller_slumped_confused as mrdriller
    stop music fadeout 1.0
    t_ch_mrdriller "Uh oh." # @t_smrdriller359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain zorder 10:
        # FadeEvent
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Suddenly, a huge geyser of water bursts from the pipe where it was pierced by the drill." # @t_smrdriller360.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Mr. Driller and I are both getting flung high into the air!)" # @t_smrdriller361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "WAAAAUUUUGGGHHH!" # @t_smrdriller362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "AUUUUGGGGHHH!!!" # @t_smrdriller363.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I think we landed…." # @t_smrdriller364.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Yeah… it feels like we’re on…" # @t_smrdriller365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " A pile of rocks or something." # @t_smrdriller365.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Oh no…" # @t_smrdriller366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Oh no." # @t_smrdriller366.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Oh no oh no oh no oh NO!" # @t_smrdriller366.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_confused as mrdriller:
        # ShowWithAtl
        linear 0.5 ypos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(I open my eyes, and all of a sudden…" # @t_smrdriller367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I can see why Mr. Driller is so upset." # @t_smrdriller367.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.1 
    show i_mrdriller_slumped_cry as mrdriller:
        # ShowWithAtl
        linear 0.5 xpos 0.35 
        xzoom -1.0 
    extend "{w=0.5}{nw}"
    extend " This pile of rocks…" # @t_smrdriller367.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain:
        # FadeEvent
        linear 0.5 alpha 0.0
    $ renpy.pause(0.5, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain zorder 15
    t_ch_cousin "Is the rubble of what used to be the statue of Principal DigDug." # @t_smrdriller368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "The water gushed right down on top of it, and it was destroyed." # @t_smrdriller369.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Mr. Driller looks like he’s about to cry…" # @t_smrdriller370.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Oh no, now some of the other students are gathering around!" # @t_smrdriller371.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_taira_steveholt_happy as taira:
        xzoom -1.0 
    stop sound fadeout 1.0
    extend " ...I might cry, too.)" # @t_smrdriller371.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    stop sound
    show i_taira_steveholt_happy as taira:
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_taira "WHOAH! Look what Little D did to the statue of Big D!" # @t_smrdriller372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "AWESOME!" # @t_smrdriller373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_aki_akimbo_shocked as aki:
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_aki "Taira! What is WRONG with you?!" # @t_smrdriller374.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "Yeah, you’re right…" # @t_smrdriller375.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_taira "It was TOTALLY awesome." # @t_smrdriller376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_aki "Destruction of school property is most certainly not awesome!" # @t_smrdriller377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_meowkie_normal_happy as meowkie:
        xzoom -1.0 
    extend " Where was the Hall Monitor during all of this?! Honestly…" # @t_smrdriller377.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_meowkie_akimbo_frown as meowkie:
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_meowkie "H-hey! D-don’t look at me!" # @t_smrdriller378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_smug as albatros
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Guys… can you… give us some space, please?" # @t_smrdriller379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_smug as albatros:
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_albatros "Hey, groovy! Vandalism of beloved school property!" # @t_smrdriller380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I really enjoy that sort of edgy illegal activity. Any of you want to have a conversation about that?" # @t_smrdriller380.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_aki_akimbo_focus as aki
    t_ch_aki "Are you all insane?!" # @t_smrdriller381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m getting the principal." # @t_smrdriller381.01 self.block='Last'
    show i_aki_akimbo_focus as aki:
        # FadeEvent
        linear 0.33 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Hey, wait-" # @t_smrdriller382.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Ugh! She’s gone already. How does that girl move so fast?" # @t_smrdriller382.01 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0) # Curtain fade
    show i_bg_hallway_b as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_b', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_1z', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    show i_mrdriller_slumped_sad as mrdriller:
        # ShowWithAtl
        linear 0.5 xpos 0.4 
    show i_taira_steveholt_happy as taira:
        # FadeEvent

    show i_meowkie_akimbo_frown as meowkie:
        # FadeEvent

    show i_albatross_toocool_smug as albatros:
        # FadeEvent

    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "[slot_playerName]… My dad’s gotta know I didn’t mean to do that, right…?" # @t_smrdriller383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I mean..." # @t_smrdriller383.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I never thought…" # @t_smrdriller383.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "...I’m going to be in sooo much trouble." # @t_smrdriller384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_digdug "Son, don’t worry, I’m not mad at you." # @t_smrdriller385.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_confused as mrdriller:
        xzoom 1.0 
    t_ch_mrdriller "Y-you’re not? That’s a relief." # @t_smrdriller386.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Well, no, not really." # @t_smrdriller387.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I actually am extremely mad at you." # @t_smrdriller387.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "I guess what I meant to say is, I’m mad, but also happy." # @t_smrdriller388.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Because what you’ve done today has finally shown you that I was right to tell you not to dig." # @t_smrdriller389.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I just want what’s best for you, my son." # @t_smrdriller389.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And what’s best is squashing the one thing that brings you true fulfillment in this miserable life!" # @t_smrdriller389.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You know, like I did." # @t_smrdriller389.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin_exhausted_neutral at default
    t_ch_cousin "Um…" # @t_smrdriller390.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " What about me?" # @t_smrdriller390.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " I was there too..." # @t_smrdriller390.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "You, I’m just plain mad at." # @t_smrdriller391.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Wait your turn, though." # @t_smrdriller391.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_sad as mrdriller
    t_ch_mrdriller "[slot_playerName]… [slot_playerName] didn’t do anything." # @t_smrdriller392.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "That’s exactly right, boy." # @t_smrdriller393.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " [slot_playerName] didn’t do anything." # @t_smrdriller393.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " [slot_playerName] just watched you drill your way to kingdom come." # @t_smrdriller393.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_crying as mrdriller
    t_ch_mrdriller "…" # @t_smrdriller394.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Man, this is kinda unfair.)" # @t_smrdriller395.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Son, I want you to know…" # @t_smrdriller396.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m not trying to make your life miserable." # @t_smrdriller396.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m trying to make it better." # @t_smrdriller396.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug:
        xzoom -1.0 
    t_ch_digdug "Your mother left because I couldn’t stop obsessing about digging." # @t_smrdriller397.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "But ever since I put away my drills and shovels for good…" # @t_smrdriller398.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " My life has gotten so much better." # @t_smrdriller398.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug:
        xzoom 1.0 
    extend " I just want the same for you." # @t_smrdriller398.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(He lives alone…" # @t_smrdriller399.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " He seems angry all the time…" # @t_smrdriller399.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And he seems to be putting a wedge between himself and his son…" # @t_smrdriller399.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    extend " Is his life really that much better?" # @t_smrdriller399.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Jeez. This is really depressing.)" # @t_smrdriller3100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Dad..." # @t_smrdriller3101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller:
        xzoom -1.0 
    t_ch_mrdriller "I just wanted to dig…" # @t_smrdriller3102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "I know, son." # @t_smrdriller3103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But the only good digging you can do now…" # @t_smrdriller3103.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Is digging a hole to bury that part of yourself in." # @t_smrdriller3104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I promise, son. You’ll feel so much better." # @t_smrdriller3104.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Are you sure that’s good advice to give your son?!" # @t_smrdriller3105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Mr. Driller doesn’t just like digging…" # @t_smrdriller3105.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " He LIVES it." # @t_smrdriller3105.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You’re asking him to bury his whole life!" # @t_smrdriller3106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Watch it, [slot_playerName]." # @t_smrdriller3107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You’re on thin ice already." # @t_smrdriller3107.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.5 ypos 0.35 
    extend "{w=0.5}{nw}"
    t_ch_digdug "You’ve already been in trouble twice!" # @t_smrdriller3108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.5 ypos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_digdug "Three strikes, [slot_playerName], and you’re out." # @t_smrdriller3109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "…" # @t_smrdriller3110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I guess he’s right…" # @t_smrdriller3111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I better keep my mouth shut.)" # @t_smrdriller3111.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "…" # @t_smrdriller3112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Dad…" # @t_smrdriller3112.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_sad as mrdriller:
        xzoom 1.0 
    t_ch_mrdriller "I think you’re right." # @t_smrdriller3113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’ve got to get free of these stupid drills" # @t_smrdriller3113.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " …" # @t_smrdriller3113.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Please… take them… and put them somewhere where they can’t do anything bad anymore." # @t_smrdriller3114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Mr. Driller?! No!" # @t_smrdriller3115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I can’t believe it…" # @t_smrdriller3116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_sad as mrdriller
    extend " I’m watching Mr. Driller turn in his drills with my own eyes." # @t_smrdriller3116.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_30', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " ...Is he gonna call himself something different now?" # @t_smrdriller3116.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_31', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Mr. Nothing-er?)" # @t_smrdriller3116.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_32', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_digdug "I’m proud of you, son…" # @t_smrdriller3117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_33', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You’re doing the right thing." # @t_smrdriller3117.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_34', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You’re already avoiding all the mistakes I made." # @t_smrdriller3117.02 self.block='Last'
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.33 alpha 0.0
    show i_mrdriller_standing_sad as mrdriller:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.75 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.25 
    # <ParallelEvent ParallelEvent {'name': '_38', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Mr. Driller…" # @t_smrdriller3118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_39', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " How could you do that?" # @t_smrdriller3118.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " How could you give up your passion like that?" # @t_smrdriller3118.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Because of those drills, I got you in trouble." # @t_smrdriller3119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "You could be expelled…" # @t_smrdriller3120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Just because I couldn’t stop myself from digging." # @t_smrdriller3120.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You… just got a little excited, that’s all." # @t_smrdriller3121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Actually he did seem kinda obsessed…" # @t_smrdriller3122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But that isn’t what he needs to hear right now.)" # @t_smrdriller3122.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I told you about how digging is about discovery." # @t_smrdriller3123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Well, I never considered the fact that…" # @t_smrdriller3124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "If you dig deep enough, you might find something you wish you hadn’t." # @t_smrdriller3125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...Yeah…" # @t_smrdriller3126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I see what you’re saying…" # @t_smrdriller3126.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "And I’m not just talking about the pipe." # @t_smrdriller3127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Yeah." # @t_smrdriller3128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "I’m talking about… something deeper." # @t_smrdriller3129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Like, emotions-wise." # @t_smrdriller3129.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Uh huh. I got it." # @t_smrdriller3130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I mean to say it’s a metaphor." # @t_smrdriller3131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I don’t know what metaphor means, but it sounds deep and meaningful…)" # @t_smrdriller3132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "I get it already! A metaphor for what exactly?" # @t_smrdriller3133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "…[slot_playerName], when I saw that destroyed statue, I was horrified…" # @t_smrdriller3134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "But also a part of me felt happy." # @t_smrdriller3135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And that horrified me even more." # @t_smrdriller3135.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_cry as mrdriller
    t_ch_mrdriller "I think a part of me really wanted to destroy it…" # @t_smrdriller3136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " There really is something destructive in me, and the drills let it out." # @t_smrdriller3136.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I did that on purpose, to my own father! …" # @t_smrdriller3137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_sad as mrdriller
    extend " Or at least, a statue of my own father…" # @t_smrdriller3137.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I never realized how deep my anger went." # @t_smrdriller3138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Well, he’s late to the party on that particular discovery…" # @t_smrdriller3139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But still..." # @t_smrdriller3139.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "This is awful." # @t_smrdriller3140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’ve gotta say something to cheer him up.)" # @t_smrdriller3140.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "So, uh…" # @t_smrdriller3141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "...Yeah?" # @t_smrdriller3142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Pretty good… dirt today, huh?" # @t_smrdriller3143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Just like I said." # @t_smrdriller3143.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_3k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller:
        # ShowWithAtl
        pause 1.0 
        ease_expo .7 xpos 0.4 
    extend "{w=1.7}{nw}"
    t_ch_mrdriller "[slot_playerName]… let me give you a hug…" # @t_smrdriller3144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Whoah…)" # @t_smrdriller3145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I’m so sorry about what happened today!" # @t_smrdriller3146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I hope you can forgive me..." # @t_smrdriller3146.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It… It’s okay…" # @t_smrdriller3147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (I hope he can’t tell that I’m blushing.)" # @t_smrdriller3147.01 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_3q', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_mrdriller3__3q:
        # <NHSceneChange NHSceneChange {'name': '_3q', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4