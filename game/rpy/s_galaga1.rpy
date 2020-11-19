# <Scene scene {'id': 's_galaga1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_galaga1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_galaga1"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_galaga1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/romance.ogg" loop
    show i_bg_stage_cardboard as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_donko_default_grin as donko zorder 3:
        default
        xpos 0.7 
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 5:
        default
        xpos 0.2 
    show i_valkyrie_armscrossed_grin as valkyrie zorder 5:
        default
        xpos 0.3 
        xzoom -1.0 
        alpha 0.0
    show i_galaga_script as galaga zorder 2:
        default
        xpos 0.3 
        alpha 0.0
    show i_tomari_notebook_thinking as tomari zorder 3:
        default
        xpos 0.7 
        alpha 0.0
    t_ch_cousin "Wow, look at all these people!" # @t_sgalaga128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Do I really have to audition in front of them?!" # @t_sgalaga129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I was kinda hoping for a more one on one thing." # @t_sgalaga130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "What if I embarrass myself?" # @t_sgalaga131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified_blush as cousin
    t_ch_cousin "What if Galaga Ship sees me!" # @t_sgalaga132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What if Galaga Ship doesn’t notice me…" # @t_sgalaga133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_notebook_thoughtful as tomari:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_dirtomari "If I can have everyone’s attention please!" # @t_sgalaga134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_dirtomari "I’ve eliminated the need for auditions via scientific process." # @t_sgalaga135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_notebook_thinking as tomari
    show i_cousin_exhausted_surprised as cousin
    t_ch_dirtomari "In place of auditions, each of you will simply fill out a short form." # @t_sgalaga136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "(Whew, dodged a bullet there!)" # @t_sgalaga137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_notebook_smile as tomari
    t_ch_dirtomari "The form has six hundred and ninety-two questions." # @t_sgalaga138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(WHAT?!)" # @t_sgalaga139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_dirtomari "I’ll also need to scan your brains." # @t_sgalaga140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_thoughtful as tomari
    t_ch_dirtomari "It might not even hurt." # @t_sgalaga141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Wait, why would it hurt…?)" # @t_sgalaga142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_thinking as tomari
    t_ch_dirtomari "And I’ll need to take a blood sample." # @t_sgalaga143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(MY BLOOD?!)" # @t_sgalaga144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_thoughtful as tomari
    t_ch_dirtomari "Oh, and that will definitely hurt." # @t_sgalaga145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_mortified as tomari
    extend " A LOT." # @t_sgalaga145.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_grin as valkyrie:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_cousin_exhausted_mortified as cousin:
        # FadeEvent
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "Tomari, do you have to be such a weird egghead about everything?" # @t_sgalaga146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_frustrated as tomari
    t_ch_dirtomari "So, suddenly I’m a weird egghead just because I want to direct the most scientifically precise reproduction of Romeo and Juliet ever conceived?!?!" # @t_sgalaga147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_galaga_script as galaga:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_valkyrie_armscrossed_grin as valkyrie:
        # FadeEvent

    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}Yes, Tomari.{/smallcaps}" # @t_sgalaga148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_dirtomari "Oh." # @t_sgalaga149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_frustrated as tomari
    extend " Fine, whatever." # @t_sgalaga149.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_dirtomari "We’ll do auditions instead." # @t_sgalaga150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_dirtomari "Like cavemen." # @t_sgalaga151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_galaga_script as galaga:
        # FadeEvent

    extend "{w=0.5}{nw}"
    t_ch_cousin "Whew. I guess?" # @t_sgalaga152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_thoughtful as tomari
    show i_cousin_default_neutral as cousin:
        # FadeEvent
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_dirtomari "Okay, everyone auditioning for Juliet, please line up on stage." # @t_sgalaga153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Yes, good." # @t_sgalaga153.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_thinking as tomari
    t_ch_dirtomari "Now, if you are not Galaga Ship, then you did not get the part." # @t_sgalaga154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_dirtomari "Better luck next time." # @t_sgalaga155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_bored as valkyrie:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "Whatever. I’m gone." # @t_sgalaga156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_bored as valkyrie:
        # FadeEvent

    show i_tomari_defeated_thinking as tomari:
        # FadeEvent

    show i_donko_ygg_wink as donko:
        xzoom -1.0 
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_galaga_script as galaga:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_donko "Told you!" # @t_sgalaga157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}That’s not fair! None of us read a single line!{/smallcaps}" # @t_sgalaga158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_donko_ygg_wink as donko:
        # FadeEvent

    show i_tomari_alive_smile as tomari:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_dirtomari "I don’t need to rigorously apply the scientific method to realize the most beautiful spaceship in school has to play Juliet." # @t_sgalaga159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}But shouldn’t the role go to the best actor for part?{/smallcaps}" # @t_sgalaga160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_mortified as tomari
    t_ch_dirtomari "Okay, where are our Romeos!" # @t_sgalaga161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_galaga_script as galaga:
        # FadeEvent

    show i_cousin_default_surprised as cousin:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "Gulp!" # @t_sgalaga162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Here goes nothing.)" # @t_sgalaga162.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " Uh, I-I’d, uh." # @t_sgalaga162.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_dirtomari "Anyone?" # @t_sgalaga163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Ah, I, uh um." # @t_sgalaga164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_dirtomari "We need a Romeo, people." # @t_sgalaga165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I, uh, um." # @t_sgalaga166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_frustrated as tomari
    t_ch_dirtomari "Seriously. Anyone. Anyone at all." # @t_sgalaga167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "I’LL ROMEO THE PART!" # @t_sgalaga168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_mortified as tomari
    t_ch_dirtomari "…" # @t_sgalaga169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_mortified as tomari:
        # FadeEvent

    show i_galaga_script as galaga:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}…{/smallcaps}" # @t_sgalaga170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin
    t_ch_cousin "(Oh, man. Guess I’m kinda nervous.)" # @t_sgalaga171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified_blush as cousin
    t_ch_cousin "(Everyone’s looking!)" # @t_sgalaga172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Ahh, what do I say!)" # @t_sgalaga173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_laugh_blush as cousin
    t_ch_cousin "Uh. If that’s okay." # @t_sgalaga174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Bravo, [slot_playerName].)" # @t_sgalaga174.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Bravo.)" # @t_sgalaga174.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_notebook_thoughtful as tomari:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_galaga_script as galaga:
        # FadeEvent

    extend "{w=0.5}{nw}"
    t_ch_dirtomari "Okay, new kid. Give us your Romeo." # @t_sgalaga175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_dirtomari "We’ll start with his first soliloquy." # @t_sgalaga176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Yeah, that’s what we’ll do." # @t_sgalaga177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_dirtomari "Page Five in your script." # @t_sgalaga178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral_blush as cousin
    t_ch_cousin "Sounds good, sure." # @t_sgalaga179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_notebook_thoughtful as tomari
    t_ch_dirtomari "Whenever you’re ready." # @t_sgalaga180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Ready?" # @t_sgalaga181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_dirtomari "To read. Your lines." # @t_sgalaga182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin
    t_ch_cousin "OUT LOUD?!" # @t_sgalaga183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_notebook_thoughtful as tomari:
        # FadeEvent

    show i_galaga_script as galaga:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}That’s usually how we read scripts.{/smallcaps}" # @t_sgalaga184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified_blush as cousin
    t_ch_cousin "Y-yeah. Of course. Yeah." # @t_sgalaga185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Here goes nothing…)" # @t_sgalaga185.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " A-ahem." # @t_sgalaga185.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral_blush as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.5 
    show i_galaga_script as galaga:
        # ShowWithAtl
        linear 0.5 xpos 0.9 
    show i_tomari_notebook_thoughtful as tomari:
        # ShowWithAtl
        linear 0.25 xpos 0.1 
        xzoom -1.0 
        # FadeEvent
        linear 0.25 alpha 1.0
    show i_donko_default_grin as donko:
        # ShowWithAtl
        linear 0.25 xpos 0.95 
        xzoom 1.0 
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.5}{nw}"
    extend " “ALAS!”" # @t_sgalaga185.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin:
        xzoom -1.0 
    show i_tomari_notebook_mortified as tomari
    show i_donko_default_meloncholic as donko
    t_ch_cousin "“THAT LOVE!”" # @t_sgalaga186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_laugh_blush as cousin:
        xzoom 1.0 
    show i_tomari_defeated_mortified as tomari
    show i_donko_akimbo_meloncholic as donko
    t_ch_cousin "“WHOSE VIEW?”" # @t_sgalaga187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Uh…" # @t_sgalaga187.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin
    extend " (Oh man, lost my place!)" # @t_sgalaga187.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Yawn.{/smallcaps}" # @t_sgalaga188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "!!!!!" # @t_sgalaga189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Where was I?)" # @t_sgalaga189.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Ah! This part’s close enough I bet)" # @t_sgalaga190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin:
        xzoom -1.0 
    extend " “WHERE SHALL WE!”" # @t_sgalaga190.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "uh" # @t_sgalaga191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin:
        xzoom 1.0 
    show i_tomari_defeated_frustrated as tomari
    t_ch_cousin "“DINE?!?!?!”" # @t_sgalaga192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_dirtomari "I think you skipped a line and—" # @t_sgalaga193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin:
        xzoom -1.0 
    show i_tomari_alive_mortified as tomari
    t_ch_cousin "“OH ME!”" # @t_sgalaga194.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised_blush as cousin:
        xzoom 1.0 
    show i_donko_phone_meloncholic as donko:
        xzoom -1.0 
    t_ch_cousin "“WHAT FRAY!!! WAS HERE???”" # @t_sgalaga195.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_thinking as tomari
    t_ch_dirtomari "Okay, that’s enou—" # @t_sgalaga196.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_sad_blush as cousin:
        xzoom -1.0 
    t_ch_cousin "“YET TELL ME!!! NOT?”" # @t_sgalaga197.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_frustrated as tomari
    t_ch_dirtomari "OKAY, [slot_playerName]! YOU’RE DONE." # @t_sgalaga198.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Wow, so soon?)" # @t_sgalaga199.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(I MUST’VE NAILED IT!)" # @t_sgalaga1100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_dirtomari "We’ve got our Romeo." # @t_sgalaga1101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_smile as tomari
    t_ch_dirtomari "And it’s Aki!" # @t_sgalaga1102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_thinking as tomari
    t_ch_dirtomari "Even though she didn’t make it to the auditions and is a girl." # @t_sgalaga1103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "!!!" # @t_sgalaga1104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " (I lost the part to empty air?!)" # @t_sgalaga1104.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(After my rousing performance?!)" # @t_sgalaga1105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_galaga_script as galaga:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_donko_phone_meloncholic as donko:
        # FadeEvent
        linear 0.25 alpha 0.0
    show i_cousin_exhausted_mortified as cousin:
        # ShowWithAtl
        linear 0.40 xpos 0.75 
    show i_tomari_defeated_smile as tomari:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    extend "{w=0.5}{nw}"
    t_ch_dirtomari "Okay, people. That’s enough for now." # @t_sgalaga1106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised_blush as cousin
    t_ch_cousin "Hey! What about me!" # @t_sgalaga1107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_thinking as tomari
    t_ch_dirtomari "Oh, yes." # @t_sgalaga1108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_frustrated as tomari
    t_ch_dirtomari "You’re still here." # @t_sgalaga1109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_mortified as tomari
    t_ch_dirtomari "And want to be in the play." # @t_sgalaga1110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_dirtomari "That’s…" # @t_sgalaga1111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_mortified as tomari
    t_ch_dirtomari "That’s great." # @t_sgalaga1112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "(He thinks I’m great! Maybe I’ll get a nice meaty part after all!)" # @t_sgalaga1113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_thinking as tomari
    t_ch_dirtomari "[slot_playerName], you can be Aki's understudy." # @t_sgalaga1114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "!!!!" # @t_sgalaga1115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Un…understudy?" # @t_sgalaga1116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_thoughtful as tomari
    t_ch_dirtomari "You’ll be a heartbeat away from the action!" # @t_sgalaga1117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_smile as tomari
    extend " Aki is the most accomplished and dependable student at Namco High based on fourteen metrics ranging from school spirit to grade point average." # @t_sgalaga1117.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Therefore, making [slot_playerName] her understudy is the best shot I’ve got to make sure [slot_playerName] NEVER GETS ON STAGE." # @t_sgalaga1117.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "I didn’t catch what you said there. It sounded like conspiratorial whispering." # @t_sgalaga1118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_smile as tomari
    t_ch_dirtomari "Oh, uh. I didn’t say anything." # @t_sgalaga1119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_dirtomari "I, um, coughed." # @t_sgalaga1120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Hm, that was some cough then!)" # @t_sgalaga1121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Well, understudy’s…pretty okay." # @t_sgalaga1121.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I guess?" # @t_sgalaga1121.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_smile as tomari:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.65 xpos -0.5 
    extend "{w=0.65}{nw}"
    t_ch_dirtomari "Great. Well, see ya." # @t_sgalaga1122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin:
        linear 0.25 xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.25 
    extend "{w=0.5}{nw}"
    t_ch_cousin "I guess they just wanted a different take on the character." # @t_sgalaga1123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_galaga_script as galaga:
        # ShowWithAtl
        xpos 0.7 
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}Ha! That’s one way to put it, sure.{/smallcaps}" # @t_sgalaga1124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "I…I…uh…" # @t_sgalaga1125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    extend " (AAAAAAAAAAAAA)" # @t_sgalaga1125.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I don’t think I’ve ever seen an audition quite like yours.{/smallcaps}" # @t_sgalaga1126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "(HHHHHHHHHHHHHHHHH!!!)" # @t_sgalaga1127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}But at least they let you do an audition…{/smallcaps}" # @t_sgalaga1128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_grin_blush as cousin
    t_ch_cousin "I-I-uh-yuh. Audition." # @t_sgalaga1129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral_blush as cousin
    extend " (Hang on!)" # @t_sgalaga1129.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Galaga Ship’s upset about something.)" # @t_sgalaga1130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Ahem. Yeah. Audition!" # @t_sgalaga1130.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "But you didn’t even have to audition, right? You must be really good!" # @t_sgalaga1131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Who knows? Everyone else gets to earn or lose parts on their own merits.{/smallcaps}" # @t_sgalaga1132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Or their lack of them. Ahem.{/smallcaps}" # @t_sgalaga1133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Or just wanting a different take!!!)" # @t_sgalaga1134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I’m the only one who didn’t have to earn a part. I only got Juliet because of…{/smallcaps}" # @t_sgalaga1135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}You know.{/smallcaps}" # @t_sgalaga1136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Who I am.{/smallcaps}" # @t_sgalaga1137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(Gosh. That must be some villa!)" # @t_sgalaga1138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I don’t know. Maybe I should just be thankful? Other people have hard lives and here I am complaining that everything in mine is too easy.{/smallcaps}" # @t_sgalaga1139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Well, no, I don’t think so." # @t_sgalaga1140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I mean, sure, it sounds super selfish…" # @t_sgalaga1140.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}!{/smallcaps}" # @t_sgalaga1141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "…but no one likes to feel like they cheated their way through stuff." # @t_sgalaga1142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Except for cheaters, I guess." # @t_sgalaga1142.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "But when they do it, it’s on purpose!" # @t_sgalaga1143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It’s not your fault you live in that villa!" # @t_sgalaga1144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Haha! Oh, [slot_playerName]. You know that’s not what I meant.{/smallcaps}" # @t_sgalaga1145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}But, thanks.{/smallcaps}" # @t_sgalaga1146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "(I know the what now?)" # @t_sgalaga1147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin
    extend " Hey. Yeah." # @t_sgalaga1147.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I sure did know that thing." # @t_sgalaga1148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "That you said and meant." # @t_sgalaga1149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Hey, if it’d make you feel any better, you could do your audition now." # @t_sgalaga1150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Yeah? You don’t think that’s stupid, do you?{/smallcaps}" # @t_sgalaga1151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "No way. It’s what you’re here for!" # @t_sgalaga1152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Really?{/smallcaps}" # @t_sgalaga1153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Well. Okay.{/smallcaps}" # @t_sgalaga1154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I know it’s cliché, but I love the part at the balcony just after Juliet does the “Wherefore art thou.”{/smallcaps}" # @t_sgalaga1155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}And she’s telling Romeo that she doesn’t care about--{/smallcaps}" # @t_sgalaga1156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {smallcaps}Oh, I’ll just do it.{/smallcaps}" # @t_sgalaga1156.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {smallcaps}Ahem.{/smallcaps}" # @t_sgalaga1156.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_galaga "{smallcaps}‘Tis but thy name that is my enemy;{/smallcaps}" # @t_sgalaga1157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Thou art thyself, though not a Montague.{/smallcaps}" # @t_sgalaga1158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}What’s Montague? It is nor hand, nor foot,{/smallcaps}" # @t_sgalaga1159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Nor arm, nor face, nor any other part{/smallcaps}" # @t_sgalaga1160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Belonging to a man. O, be some other name.{/smallcaps}" # @t_sgalaga1161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}What’s in a name? That which we call a rose{/smallcaps}" # @t_sgalaga1162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_galaga "{smallcaps}By any other name would smell as sweet;{/smallcaps}" # @t_sgalaga1163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}So Romeo would, were he not Romeo call’d,{/smallcaps}" # @t_sgalaga1164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Retain that dear perfection which he owes{/smallcaps}" # @t_sgalaga1165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Without that title. Romeo, doff thy name,{/smallcaps}" # @t_sgalaga1166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}And for that name, which is no part of thee,{/smallcaps}" # @t_sgalaga1167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Take all myself.{/smallcaps}" # @t_sgalaga1168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {smallcaps}Was that, y’know, okay?{/smallcaps}" # @t_sgalaga1168.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Hm? What happened? I was totally captivated!!!)" # @t_sgalaga1169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_laugh_blush as cousin
    extend " Y-yeah. That was…" # @t_sgalaga1169.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "That was great!" # @t_sgalaga1170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}You’re just saying that.{/smallcaps}" # @t_sgalaga1171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "No way. If you stunk, you’d be stinking up the play I’m almost in! No way I’d put up with that, lemme tell ya." # @t_sgalaga1172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Yeah?{/smallcaps}" # @t_sgalaga1173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Hm, yeah.{/smallcaps}" # @t_sgalaga1174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Thanks, [slot_playerName].{/smallcaps}" # @t_sgalaga1175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Y’know. For a second there? I felt like I really earned the part.{/smallcaps}" # @t_sgalaga1176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Oh, gosh. Look at the time! Hey, I’ll see you around, okay?{/smallcaps}" # @t_sgalaga1177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_galaga_script as galaga:
        # ShowWithAtl
        linear 0.5 xpos 1.25 
    show i_cousin_default_neutral_blush as cousin
    extend "{w=0.5}{nw}"
    t_ch_cousin "Y-yeah, sure." # @t_sgalaga1178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (I never suspected Galaga Ship might feel like an imposter.)" # @t_sgalaga1178.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified_blush as cousin
    t_ch_cousin "(That’s a pretty sad way to go through life!)" # @t_sgalaga1179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Maybe I can do something to help out…?)" # @t_sgalaga1180.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_2x', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
    label s_galaga1__2x:
        # <NHSceneChange NHSceneChange {'name': '_2x', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
        jump s_day2