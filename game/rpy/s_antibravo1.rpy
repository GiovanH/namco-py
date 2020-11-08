# <Scene {'id': 's_antibravo1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_antibravo1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_antibravo1"
    $ renpy.pause(1)
    # <Scene {'id': 's_antibravo1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
    label s_antibravo1_initialize:
        # <ParallelEvent {'auto': 'true', 'name': 'initialize'} ParallelEvent ''>
        # <Events {} events ''>
        play music "bgm/upbeat_half.ogg" loop
        show i_bg_cafe as bg zorder 0 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_sw_black as darkness zorder 1:
            default
            alpha 0.5
        show i_abm_default_sad as antibravo zorder 2:
            default
            xpos 0.7 
            alpha 0.0
        show i_davesprite_standing_disinterest as davesprite zorder 2:
            default
            alpha 0.0
            xpos 0.7 
        show i_hiromi_akimbo_serious as hiromi zorder 2:
            default
            alpha 0.0
            xpos 0.5 
        show i_cousin_default_neutral as cousin zorder 2:
            default
            xpos 0.3 

    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(This is the Cafe... )" # @t_santibravo127.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I followed that guy here, but I lost him as soon as we got inside...)" # @t_santibravo128.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(The whole Cafe is dark, so it's hard to tell just how many people are in the crowd... )" # @t_santibravo129.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(There's a... contemplative silence in the air. Everyone seems to be waiting for something to happen.)" # @t_santibravo130.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    stop music fadeout 1.0
    t_ch_cousin "(There's a stool with a mic at the front of the room. It looks like someone is going up.)" # @t_santibravo131.00 self.block='Last'
    show i_cousin_default_neutral as cousin:
        # FadeEvent
        linear 0.5 alpha 0.0
    show i_mc_normal as mc zorder 2:
        default
        xpos 0.5 
        alpha 0.0
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_sad as antibravo:
        # ActorEvent
        xpos 0.5 
    show i_mc_normal as mc:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_mc "Hi guys... Welcome to open mic night. Our first poet comes from real far out." # @t_santibravo132.00 self.block='Last'
    show i_mc_normal as mc:
        # FadeEvent
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_davesprite_standing_disinterest as davesprite:
        # ActorEvent
        xpos 0.5 
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_davesprite "hey dudes" # @t_santibravo133.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_davesprite "heres my poem" # @t_santibravo134.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " im the best" # @t_santibravo134.01 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " and youre the rest" # @t_santibravo134.02 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " youre the worst" # @t_santibravo134.03 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " and im the hearse" # @t_santibravo134.04 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " of your coolness" # @t_santibravo134.05 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " peace" # @t_santibravo134.06 self.block='Last'
    show i_davesprite_standing_disinterest as davesprite:
        # FadeEvent
        linear 0.5 alpha 0.0
    play sound "sfx/fingersnaps.ogg"
    show i_mc_normal as mc:
        # FadeEvent
        linear 0.5 alpha 1.0
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mc "That was... Really rad." # @t_santibravo135.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mc "Really...." # @t_santibravo136.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " rad." # @t_santibravo136.01 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mc "Anyway," # @t_santibravo137.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Our next poet is from auto club. Give it up for... Hiromi!" # @t_santibravo137.01 self.block='Last'
    show i_mc_normal as mc:
        # FadeEvent
        linear 0.5 alpha 0.0
    show i_hiromi_akimbo_serious as hiromi:
        # FadeEvent
        linear 0.5 alpha 1.0
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi ".............." # @t_santibravo138.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "....................." # @t_santibravo139.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "Girl, when we're alone... I feel like we're going a million miles an hour." # @t_santibravo140.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "When we're together, I don't want to be anywhere else." # @t_santibravo141.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_crossed_serious as hiromi
    t_ch_hiromi "You make me feel so amazing." # @t_santibravo142.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "I wish we could get married." # @t_santibravo143.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi ".................." # @t_santibravo144.00 self.block='Last'
    show i_hiromi_crossed_serious as hiromi:
        # FadeEvent
        linear 0.5 alpha 0.0
    play sound "sfx/fingersnaps.ogg"
    show i_mc_normal as mc:
        # FadeEvent
        linear 0.5 alpha 1.0
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mc "That was Hiromi, with a unique freestyle poem about her beloved motorcycle." # @t_santibravo145.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Er... )" # @t_santibravo146.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mc "Last up is a new addition to Poetry Club, and to Namco High... Anti-Bravoman!" # @t_santibravo147.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mc "Um... He's around here somewhere..." # @t_santibravo148.00 self.block='Last'
    show i_mc_normal as mc:
        # FadeEvent
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(No one's coming up...)" # @t_santibravo149.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wait! There's something moving in the rafters? It's Anti-Bravoman!)" # @t_santibravo150.00 self.block='Last'
    show i_abm_shadowknows_broody as antibravo:
        # FadeEvent
        linear 0.25 alpha 1.0
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(He jumped down... How dramatic.)" # @t_santibravo151.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(So he DID come here! Oh, he's starting... )" # @t_santibravo152.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_broody as antibravo
    t_ch_antibravo "Ahem." # @t_santibravo153.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "I wish I could escape... the murky swamp of my heart." # @t_santibravo154.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Escape the humidity... Of my discontent." # @t_santibravo154.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Abscond from... The sweltering brown soup of my inner garbage." # @t_santibravo154.02 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Flee from... The shadow of the towering castle of shame at the heart of my kingdom of regret." # @t_santibravo154.03 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " My body is a meat prison." # @t_santibravo154.04 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "Thank you." # @t_santibravo155.00 self.block='Last'
    show i_abm_default_broody as antibravo:
        # FadeEvent
        linear 0.5 alpha 0.0
    show i_mc_normal as mc:
        # FadeEvent
        linear 0.5 alpha 1.0
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mc "Gosh, well..." # @t_santibravo156.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We all have to start somewhere, don't we?" # @t_santibravo156.01 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mc "We'll be sure to be a little more careful with our... Curation, next time around." # @t_santibravo157.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_mc "Thanks for coming, everyone!" # @t_santibravo158.00 self.block='Last'
    show i_mc_normal as mc:
        # FadeEvent
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "(Whoa, that was RUDE.)" # @t_santibravo159.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Anti-Bravoman's poem wasn't great, but it had heart.)" # @t_santibravo160.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I can really see his sensitive side, which is more than I can say for the others. He was being really honest.)" # @t_santibravo161.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Maybe a little too honest for these jerks...)" # @t_santibravo162.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_backturned_sad as antibravo:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    show i_cousin_default_neutral as cousin
    extend "{w=0.5}{nw}"
    t_ch_cousin "(I should go say hi to him...)" # @t_santibravo163.00 self.block='Last'
    show i_abm_backturned_sad as antibravo:
        # FadeEvent
        linear 0.5 alpha 1.0
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_cousin "Anti-Bravoman!" # @t_santibravo164.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hmm... He seems lost in some very deep thoughts.)" # @t_santibravo165.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_laugh as cousin
    t_ch_cousin "ANTI-BRAVOMAN!" # @t_santibravo166.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_surprised as antibravo:
        linear 0.2 xzoom -1.0 
    t_ch_antibravo "HUH?! Oh, it's YOU!" # @t_santibravo167.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Were you a victim of my poetry too?" # @t_santibravo167.01 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah! I thought it was... Um... Nice! Really nice." # @t_santibravo168.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "Listen... Whatsyourname..." # @t_santibravo169.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "You don't want to get close to me..." # @t_santibravo170.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I've got dark thoughts." # @t_santibravo170.01 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(This sad atmosphere..." # @t_santibravo171.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " is absolutely ridiculous!!" # @t_santibravo171.01 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " But I should be nice... Maybe I can change the mood.)" # @t_santibravo171.02 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Say..." # @t_santibravo172.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_surprised as antibravo
    t_ch_antibravo "Hmmm?" # @t_santibravo173.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Anti-Bravoman is kind of a mouthful, y'know?" # @t_santibravo174.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "Oh... I'm sorry the very thought of me makes you throw up a little in your mouth..." # @t_santibravo175.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What?" # @t_santibravo176.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    extend " EW!" # @t_santibravo176.01 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " NO!" # @t_santibravo176.02 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I was just asking if you had any nicknames! You... You FREAK!" # @t_santibravo177.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified_blush as cousin
    t_ch_cousin "(Erk." # @t_santibravo178.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Maybe I overreacted... )" # @t_santibravo178.01 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "Freak IS a nickname I have." # @t_santibravo179.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Anti-Bravoman... 'Freak' isn't a nickname. It's an insult." # @t_santibravo180.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I shouldn't have called you that." # @t_santibravo180.01 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I'm sorry." # @t_santibravo180.02 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "It's okay... I'm used to it." # @t_santibravo181.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "A nickname is more like... Something your friends call you. It's not supposed to be mean." # @t_santibravo182.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_surprised as antibravo
    t_ch_antibravo "Ohhh... right. That explains it." # @t_santibravo183.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "It does?" # @t_santibravo184.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "I don't have any friends." # @t_santibravo185.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(This guy... Is really difficult.)" # @t_santibravo186.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Let's try out some nicknames..." # @t_santibravo187.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How about..." # @t_santibravo187.01 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "AB?" # @t_santibravo188.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "Ab?" # @t_santibravo189.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Do I even have abs?" # @t_santibravo189.01 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_shadowknows_surprised as antibravo
    extend " I don't really know what's goin' on in this gut area..." # @t_santibravo189.02 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(He's just... Poking himself in the stomach...)" # @t_santibravo190.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "How about... Anti-bro?" # @t_santibravo191.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "It makes me sound like I hate bros..." # @t_santibravo192.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "True..." # @t_santibravo193.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "...and I'm not really interested in making a political statement or anything." # @t_santibravo194.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(WHAT IS HE TALKING ABOUT)" # @t_santibravo195.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "Okay... Maybe Red Scarf? Scarfy?" # @t_santibravo196.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_shadowknows_broody as antibravo
    t_ch_antibravo "How about xX-D4RkL0Rd99-Xx?" # @t_santibravo197.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I'm not calling you that." # @t_santibravo198.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_darklord "But I like it..." # @t_santibravo199.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Not doing it." # @t_santibravo1100.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_darklord "But--" # @t_santibravo1101.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Nope. Let's just stick with Anti-Bravoman..." # @t_santibravo1102.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_shadowknows_sad as antibravo
    t_ch_antibravo "Aw." # @t_santibravo1103.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Say... What was the poem you recited earlier?" # @t_santibravo1104.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_shadowknows_surprised_blush as antibravo
    t_ch_antibravo "N-nothing!" # @t_santibravo1105.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Aw... I kinda liked it. It was real... Um... Deep." # @t_santibravo1106.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I get the feeling that you have a lot of pent-up emotion... And I was just wondering what the deal with that was." # @t_santibravo1107.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_abm_backturned_sad as antibravo
    t_ch_antibravo ".............." # @t_santibravo1108.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Uh-oh." # @t_santibravo1109.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I may have pushed a little too much.)" # @t_santibravo1109.01 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_antibravo "I..." # @t_santibravo1110.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " I have to go!" # @t_santibravo1110.01 self.block='Last'
    show i_abm_backturned_sad as antibravo:
        # FadeEvent
        linear 0.5 alpha 0.0
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I shouldn't have asked so suddenly... Way to go, [slot_playerName].)" # @t_santibravo1111.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(It seems like there's two Anti-Bravomen." # @t_santibravo1112.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    extend " One that's sad and dark and angsty..." # @t_santibravo1112.01 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And one who's kind of a sweet, sensitive guy.)" # @t_santibravo1112.02 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(There's definitely more to this situation than meets the eye...)" # @t_santibravo1113.00 self.block='Last'
    # <NHSceneChange {'name': '_2C', 'scene': 's_day2'} NHSceneChange ''>
    label s_antibravo1__2C:
        # <NHSceneChange {'name': '_2C', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2