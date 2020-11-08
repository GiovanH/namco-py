# <Scene {'id': 's_galaga1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_galaga1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_galaga1"
    $ renpy.pause(1)
    # <Scene {'id': 's_galaga1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Do I really have to audition in front of them?!" # @t_sgalaga129.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I was kinda hoping for a more one on one thing." # @t_sgalaga130.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "What if I embarrass myself?" # @t_sgalaga131.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified_blush as cousin
    t_ch_cousin "What if Galaga Ship sees me!" # @t_sgalaga132.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What if Galaga Ship doesn’t notice me…" # @t_sgalaga133.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thoughtful as tomari:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_dirtomari "If I can have everyone’s attention please!" # @t_sgalaga134.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_dirtomari "I’ve eliminated the need for auditions via scientific process." # @t_sgalaga135.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    show i_cousin_exhausted_surprised as cousin
    t_ch_dirtomari "In place of auditions, each of you will simply fill out a short form." # @t_sgalaga136.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "(Whew, dodged a bullet there!)" # @t_sgalaga137.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_smile as tomari
    t_ch_dirtomari "The form has six hundred and ninety-two questions." # @t_sgalaga138.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(WHAT?!)" # @t_sgalaga139.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_dirtomari "I’ll also need to scan your brains." # @t_sgalaga140.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_thoughtful as tomari
    t_ch_dirtomari "It might not even hurt." # @t_sgalaga141.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Wait, why would it hurt…?)" # @t_sgalaga142.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thinking as tomari
    t_ch_dirtomari "And I’ll need to take a blood sample." # @t_sgalaga143.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(MY BLOOD?!)" # @t_sgalaga144.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thoughtful as tomari
    t_ch_dirtomari "Oh, and that will definitely hurt." # @t_sgalaga145.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari
    extend " A LOT." # @t_sgalaga145.01 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_armscrossed_grin as valkyrie:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_cousin_exhausted_mortified as cousin:
        # FadeEvent
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "Tomari, do you have to be such a weird egghead about everything?" # @t_sgalaga146.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_frustrated as tomari
    t_ch_dirtomari "So, suddenly I’m a weird egghead just because I want to direct the most scientifically precise reproduction of Romeo and Juliet ever conceived?!?!" # @t_sgalaga147.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_script as galaga:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_valkyrie_armscrossed_grin as valkyrie:
        # FadeEvent
        alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}Yes, Tomari.{/smallcaps}" # @t_sgalaga148.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_dirtomari "Oh." # @t_sgalaga149.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_frustrated as tomari
    extend " Fine, whatever." # @t_sgalaga149.01 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_dirtomari "We’ll do auditions instead." # @t_sgalaga150.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_dirtomari "Like cavemen." # @t_sgalaga151.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_galaga_script as galaga:
        # FadeEvent
        alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "Whew. I guess?" # @t_sgalaga152.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thoughtful as tomari
    show i_cousin_default_neutral as cousin:
        # FadeEvent
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_dirtomari "Okay, everyone auditioning for Juliet, please line up on stage." # @t_sgalaga153.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Yes, good." # @t_sgalaga153.01 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thinking as tomari
    t_ch_dirtomari "Now, if you are not Galaga Ship, then you did not get the part." # @t_sgalaga154.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_dirtomari "Better luck next time." # @t_sgalaga155.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_akimbo_bored as valkyrie:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "Whatever. I’m gone." # @t_sgalaga156.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_valkyrie_akimbo_bored as valkyrie:
        # FadeEvent
        alpha 0.0
    show i_tomari_defeated_thinking as tomari:
        # FadeEvent
        alpha 0.0
    show i_donko_ygg_wink as donko:
        xzoom -1.0 
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_galaga_script as galaga:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_donko "Told you!" # @t_sgalaga157.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}That’s not fair! None of us read a single line!{/smallcaps}" # @t_sgalaga158.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko:
        # FadeEvent
        alpha 0.0
    show i_tomari_alive_smile as tomari:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_dirtomari "I don’t need to rigorously apply the scientific method to realize the most beautiful spaceship in school has to play Juliet." # @t_sgalaga159.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}But shouldn’t the role go to the best actor for part?{/smallcaps}" # @t_sgalaga160.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_mortified as tomari
    t_ch_dirtomari "Okay, where are our Romeos!" # @t_sgalaga161.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_script as galaga:
        # FadeEvent
        alpha 0.0
    show i_cousin_default_surprised as cousin:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "Gulp!" # @t_sgalaga162.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Here goes nothing.)" # @t_sgalaga162.01 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    extend " Uh, I-I’d, uh." # @t_sgalaga162.02 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_dirtomari "Anyone?" # @t_sgalaga163.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ah, I, uh um." # @t_sgalaga164.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_dirtomari "We need a Romeo, people." # @t_sgalaga165.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I, uh, um." # @t_sgalaga166.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_frustrated as tomari
    t_ch_dirtomari "Seriously. Anyone. Anyone at all." # @t_sgalaga167.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "I’LL ROMEO THE PART!" # @t_sgalaga168.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_mortified as tomari
    t_ch_dirtomari "…" # @t_sgalaga169.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_mortified as tomari:
        # FadeEvent
        alpha 0.0
    show i_galaga_script as galaga:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}…{/smallcaps}" # @t_sgalaga170.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified_blush as cousin
    t_ch_cousin "(Oh, man. Guess I’m kinda nervous.)" # @t_sgalaga171.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified_blush as cousin
    t_ch_cousin "(Everyone’s looking!)" # @t_sgalaga172.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Ahh, what do I say!)" # @t_sgalaga173.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_laugh_blush as cousin
    t_ch_cousin "Uh. If that’s okay." # @t_sgalaga174.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Bravo, [slot_playerName].)" # @t_sgalaga174.01 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Bravo.)" # @t_sgalaga174.02 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thoughtful as tomari:
        # FadeEvent
        linear 0.5 alpha 1.0
    show i_galaga_script as galaga:
        # FadeEvent
        alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_dirtomari "Okay, new kid. Give us your Romeo." # @t_sgalaga175.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_dirtomari "We’ll start with his first soliloquy." # @t_sgalaga176.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Yeah, that’s what we’ll do." # @t_sgalaga177.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thinking as tomari
    t_ch_dirtomari "Page Five in your script." # @t_sgalaga178.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral_blush as cousin
    t_ch_cousin "Sounds good, sure." # @t_sgalaga179.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thoughtful as tomari
    t_ch_dirtomari "Whenever you’re ready." # @t_sgalaga180.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ready?" # @t_sgalaga181.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_dirtomari "To read. Your lines." # @t_sgalaga182.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified_blush as cousin
    t_ch_cousin "OUT LOUD?!" # @t_sgalaga183.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_notebook_thoughtful as tomari:
        # FadeEvent
        alpha 0.0
    show i_galaga_script as galaga:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}That’s usually how we read scripts.{/smallcaps}" # @t_sgalaga184.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified_blush as cousin
    t_ch_cousin "Y-yeah. Of course. Yeah." # @t_sgalaga185.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Here goes nothing…)" # @t_sgalaga185.01 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    extend " A-ahem." # @t_sgalaga185.02 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin:
        xzoom -1.0 
    show i_tomari_notebook_mortified as tomari
    show i_donko_default_meloncholic as donko
    t_ch_cousin "“THAT LOVE!”" # @t_sgalaga186.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_laugh_blush as cousin:
        xzoom 1.0 
    show i_tomari_defeated_mortified as tomari
    show i_donko_akimbo_meloncholic as donko
    t_ch_cousin "“WHOSE VIEW?”" # @t_sgalaga187.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh…" # @t_sgalaga187.01 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified_blush as cousin
    extend " (Oh man, lost my place!)" # @t_sgalaga187.02 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Yawn.{/smallcaps}" # @t_sgalaga188.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "!!!!!" # @t_sgalaga189.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Where was I?)" # @t_sgalaga189.01 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Ah! This part’s close enough I bet)" # @t_sgalaga190.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin:
        xzoom -1.0 
    extend " “WHERE SHALL WE!”" # @t_sgalaga190.01 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "uh" # @t_sgalaga191.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin:
        xzoom 1.0 
    show i_tomari_defeated_frustrated as tomari
    t_ch_cousin "“DINE?!?!?!”" # @t_sgalaga192.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_dirtomari "I think you skipped a line and—" # @t_sgalaga193.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin:
        xzoom -1.0 
    show i_tomari_alive_mortified as tomari
    t_ch_cousin "“OH ME!”" # @t_sgalaga194.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_blush as cousin:
        xzoom 1.0 
    show i_donko_phone_meloncholic as donko:
        xzoom -1.0 
    t_ch_cousin "“WHAT FRAY!!! WAS HERE???”" # @t_sgalaga195.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_thinking as tomari
    t_ch_dirtomari "Okay, that’s enou—" # @t_sgalaga196.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_sad_blush as cousin:
        xzoom -1.0 
    t_ch_cousin "“YET TELL ME!!! NOT?”" # @t_sgalaga197.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_frustrated as tomari
    t_ch_dirtomari "OKAY, [slot_playerName]! YOU’RE DONE." # @t_sgalaga198.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Wow, so soon?)" # @t_sgalaga199.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(I MUST’VE NAILED IT!)" # @t_sgalaga1100.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_dirtomari "We’ve got our Romeo." # @t_sgalaga1101.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_smile as tomari
    t_ch_dirtomari "And it’s Aki!" # @t_sgalaga1102.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_alive_thinking as tomari
    t_ch_dirtomari "Even though she didn’t make it to the auditions and is a girl." # @t_sgalaga1103.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "!!!" # @t_sgalaga1104.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " (I lost the part to empty air?!)" # @t_sgalaga1104.01 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(After my rousing performance?!)" # @t_sgalaga1105.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
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
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_blush as cousin
    t_ch_cousin "Hey! What about me!" # @t_sgalaga1107.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_defeated_thinking as tomari
    t_ch_dirtomari "Oh, yes." # @t_sgalaga1108.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_frustrated as tomari
    t_ch_dirtomari "You’re still here." # @t_sgalaga1109.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_mortified as tomari
    t_ch_dirtomari "And want to be in the play." # @t_sgalaga1110.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_dirtomari "That’s…" # @t_sgalaga1111.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_mortified as tomari
    t_ch_dirtomari "That’s great." # @t_sgalaga1112.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "(He thinks I’m great! Maybe I’ll get a nice meaty part after all!)" # @t_sgalaga1113.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thinking as tomari
    t_ch_dirtomari "[slot_playerName], you can be Aki's understudy." # @t_sgalaga1114.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "!!!!" # @t_sgalaga1115.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Un…understudy?" # @t_sgalaga1116.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_thoughtful as tomari
    t_ch_dirtomari "You’ll be a heartbeat away from the action!" # @t_sgalaga1117.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_pondering_smile as tomari
    extend " Aki is the most accomplished and dependable student at Namco High based on fourteen metrics ranging from school spirit to grade point average." # @t_sgalaga1117.01 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Therefore, making [slot_playerName] her understudy is the best shot I’ve got to make sure [slot_playerName] NEVER GETS ON STAGE." # @t_sgalaga1117.02 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "I didn’t catch what you said there. It sounded like conspiratorial whispering." # @t_sgalaga1118.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari
    t_ch_dirtomari "Oh, uh. I didn’t say anything." # @t_sgalaga1119.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_dirtomari "I, um, coughed." # @t_sgalaga1120.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Hm, that was some cough then!)" # @t_sgalaga1121.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Well, understudy’s…pretty okay." # @t_sgalaga1121.01 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I guess?" # @t_sgalaga1121.02 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_tomari_standing_smile as tomari:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.65 xpos -0.5 
    extend "{w=0.65}{nw}"
    t_ch_dirtomari "Great. Well, see ya." # @t_sgalaga1122.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin:
        linear 0.25 xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.25 
    extend "{w=0.5}{nw}"
    t_ch_cousin "I guess they just wanted a different take on the character." # @t_sgalaga1123.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_script as galaga:
        # ShowWithAtl
        xpos 0.7 
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}Ha! That’s one way to put it, sure.{/smallcaps}" # @t_sgalaga1124.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "I…I…uh…" # @t_sgalaga1125.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    extend " (AAAAAAAAAAAAA)" # @t_sgalaga1125.01 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I don’t think I’ve ever seen an audition quite like yours.{/smallcaps}" # @t_sgalaga1126.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "(HHHHHHHHHHHHHHHHH!!!)" # @t_sgalaga1127.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}But at least they let you do an audition…{/smallcaps}" # @t_sgalaga1128.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin_blush as cousin
    t_ch_cousin "I-I-uh-yuh. Audition." # @t_sgalaga1129.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral_blush as cousin
    extend " (Hang on!)" # @t_sgalaga1129.01 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Galaga Ship’s upset about something.)" # @t_sgalaga1130.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Ahem. Yeah. Audition!" # @t_sgalaga1130.01 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "But you didn’t even have to audition, right? You must be really good!" # @t_sgalaga1131.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Who knows? Everyone else gets to earn or lose parts on their own merits.{/smallcaps}" # @t_sgalaga1132.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Or their lack of them. Ahem.{/smallcaps}" # @t_sgalaga1133.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Or just wanting a different take!!!)" # @t_sgalaga1134.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I’m the only one who didn’t have to earn a part. I only got Juliet because of…{/smallcaps}" # @t_sgalaga1135.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You know.{/smallcaps}" # @t_sgalaga1136.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Who I am.{/smallcaps}" # @t_sgalaga1137.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(Gosh. That must be some villa!)" # @t_sgalaga1138.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I don’t know. Maybe I should just be thankful? Other people have hard lives and here I am complaining that everything in mine is too easy.{/smallcaps}" # @t_sgalaga1139.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Well, no, I don’t think so." # @t_sgalaga1140.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean, sure, it sounds super selfish…" # @t_sgalaga1140.01 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}!{/smallcaps}" # @t_sgalaga1141.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…but no one likes to feel like they cheated their way through stuff." # @t_sgalaga1142.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Except for cheaters, I guess." # @t_sgalaga1142.01 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "But when they do it, it’s on purpose!" # @t_sgalaga1143.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s not your fault you live in that villa!" # @t_sgalaga1144.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Haha! Oh, [slot_playerName]. You know that’s not what I meant.{/smallcaps}" # @t_sgalaga1145.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}But, thanks.{/smallcaps}" # @t_sgalaga1146.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "(I know the what now?)" # @t_sgalaga1147.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    extend " Hey. Yeah." # @t_sgalaga1147.01 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I sure did know that thing." # @t_sgalaga1148.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "That you said and meant." # @t_sgalaga1149.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Hey, if it’d make you feel any better, you could do your audition now." # @t_sgalaga1150.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Yeah? You don’t think that’s stupid, do you?{/smallcaps}" # @t_sgalaga1151.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "No way. It’s what you’re here for!" # @t_sgalaga1152.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Really?{/smallcaps}" # @t_sgalaga1153.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Well. Okay.{/smallcaps}" # @t_sgalaga1154.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I know it’s cliché, but I love the part at the balcony just after Juliet does the “Wherefore art thou.”{/smallcaps}" # @t_sgalaga1155.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}And she’s telling Romeo that she doesn’t care about--{/smallcaps}" # @t_sgalaga1156.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}Oh, I’ll just do it.{/smallcaps}" # @t_sgalaga1156.01 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}Ahem.{/smallcaps}" # @t_sgalaga1156.02 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_galaga "{smallcaps}‘Tis but thy name that is my enemy;{/smallcaps}" # @t_sgalaga1157.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Thou art thyself, though not a Montague.{/smallcaps}" # @t_sgalaga1158.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}What’s Montague? It is nor hand, nor foot,{/smallcaps}" # @t_sgalaga1159.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Nor arm, nor face, nor any other part{/smallcaps}" # @t_sgalaga1160.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Belonging to a man. O, be some other name.{/smallcaps}" # @t_sgalaga1161.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}What’s in a name? That which we call a rose{/smallcaps}" # @t_sgalaga1162.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_galaga "{smallcaps}By any other name would smell as sweet;{/smallcaps}" # @t_sgalaga1163.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}So Romeo would, were he not Romeo call’d,{/smallcaps}" # @t_sgalaga1164.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Retain that dear perfection which he owes{/smallcaps}" # @t_sgalaga1165.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Without that title. Romeo, doff thy name,{/smallcaps}" # @t_sgalaga1166.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}And for that name, which is no part of thee,{/smallcaps}" # @t_sgalaga1167.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Take all myself.{/smallcaps}" # @t_sgalaga1168.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}Was that, y’know, okay?{/smallcaps}" # @t_sgalaga1168.01 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hm? What happened? I was totally captivated!!!)" # @t_sgalaga1169.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh_blush as cousin
    extend " Y-yeah. That was…" # @t_sgalaga1169.01 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That was great!" # @t_sgalaga1170.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You’re just saying that.{/smallcaps}" # @t_sgalaga1171.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "No way. If you stunk, you’d be stinking up the play I’m almost in! No way I’d put up with that, lemme tell ya." # @t_sgalaga1172.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Yeah?{/smallcaps}" # @t_sgalaga1173.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Hm, yeah.{/smallcaps}" # @t_sgalaga1174.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Thanks, [slot_playerName].{/smallcaps}" # @t_sgalaga1175.00 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Y’know. For a second there? I felt like I really earned the part.{/smallcaps}" # @t_sgalaga1176.00 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Oh, gosh. Look at the time! Hey, I’ll see you around, okay?{/smallcaps}" # @t_sgalaga1177.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_script as galaga:
        # ShowWithAtl
        linear 0.5 xpos 1.25 
    show i_cousin_default_neutral_blush as cousin
    extend "{w=0.5}{nw}"
    t_ch_cousin "Y-yeah, sure." # @t_sgalaga1178.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (I never suspected Galaga Ship might feel like an imposter.)" # @t_sgalaga1178.01 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified_blush as cousin
    t_ch_cousin "(That’s a pretty sad way to go through life!)" # @t_sgalaga1179.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Maybe I can do something to help out…?)" # @t_sgalaga1180.00 self.block='Last'
    # <NHSceneChange {'name': '_2x', 'scene': 's_day2'} NHSceneChange ''>
    label s_galaga1__2x:
        # <NHSceneChange {'name': '_2x', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2