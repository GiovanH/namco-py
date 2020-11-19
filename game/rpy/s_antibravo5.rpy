# <Scene scene {'id': 's_antibravo5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_antibravo5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_antibravo5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_antibravo5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/sadtimes.ogg" loop
    show i_bg_quad_bleachers as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 3:
        default
        xpos 0.3 
    show i_abm_backturned_sil as antibravo zorder 2:
        default
        xpos 1.2 
        alpha 1.0
    show i_trio_evil as students zorder 1:
        default
        xpos 1.4 
    t_ch_cousin "(I'm supposed to be in detention, but..." # @t_santibravo516.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I dunno." # @t_santibravo516.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " My heart's just not in it." # @t_santibravo516.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " All I can think about is Anti-Bravoman.)" # @t_santibravo516.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(He's not really a bad guy..." # @t_santibravo517.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Is he?)" # @t_santibravo517.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Sigh." # @t_santibravo518.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Wait... What's that over there? I see some dark figures on the field..." # @t_santibravo519.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Looks suspicious." # @t_santibravo519.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    extend " I better find a good hiding spot.)" # @t_santibravo519.02 self.block='Last'
    show i_cousin_energetic_neutral as cousin:
        # ShowWithAtl
        ease_expo 1 xpos -0.3 
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_trio_evil as students:
        # ShowWithAtl
        pause 0.5 
        ease_expo 1 xpos 0.5 
    extend "{w=1.5}{nw}"
    t_ch_cousin "(They look... Pretty unsavory...)" # @t_santibravo520.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wait... Who's that with them?" # @t_santibravo521.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_trio_evil as students:
        # ShowWithAtl
        ease_expo 1 xpos 0.2 
    show i_abm_backturned_sil as antibravo:
        # ShowWithAtl
        ease_expo 1 xpos 0.75 
    $ renpy.pause(1.0, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_backturned_broody as antibravo
    with Dissolve(.6)
    extend " No! It can't be... )" # @t_santibravo521.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Anti-Bravoman!)" # @t_santibravo522.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_shadowknows_broody as antibravo:
        linear .3 xzoom -1.0 
    show i_cousin_default_neutral as cousin
    t_ch_antibravo "Guys... You can't be here." # @t_santibravo523.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I shouldn't even be talking to you." # @t_santibravo523.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow1 "HAHA... YOU HEAR THAT? ANTI-BRAVOMAN SAID HE DOESN'T WANNA TALK TO US" # @t_santibravo524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow2 "MORE LIKE ANTI-BRAVEMAN" # @t_santibravo525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow2 "BECAUSE HE'S LIKE... NOT BRAVE AT ALL" # @t_santibravo526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow3 "NICE ONE BRO" # @t_santibravo527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Is this what Anti-Bravo meant when he said he was ... Followed by darkness?!)" # @t_santibravo528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Did he mean it LITERALLY?!)" # @t_santibravo529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow3 "LISTEN UP ANTI-BRAVOMAN... YOU'RE GONNA SHUT UP" # @t_santibravo530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow1 "AND YOU'RE GONNA DO WHAT WE SAY" # @t_santibravo531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_broody as antibravo
    t_ch_antibravo "But... I don't want to! It's wrong!" # @t_santibravo532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And besides, I like it here!" # @t_santibravo532.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow2 "YOU LIKE IT? NO ONE LIKES YOU." # @t_santibravo533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow1 "EVERYONE THINKS YOU SUCK" # @t_santibravo534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Yeah... How COULD he be okay wih that? I'd be so mad... )" # @t_santibravo535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "I don't have to be that other person! I can be good. It doesn't matter if people don't like me here..." # @t_santibravo536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_broody as antibravo
    t_ch_antibravo "At least I don't have to be a bad person!" # @t_santibravo537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow3 "HEH... LISTEN TO THIS GUY" # @t_santibravo538.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow2 "HE THINKS HE'S SOOO MUCH BETTER THAN US..." # @t_santibravo539.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow1 "LISTEN ANTI-BRAVOMAN... YOU'RE GONNA SHUT UP AND DO WHAT WE TELL YOU. YOU THINK YOU'RE SO MUCH BETTER NOW BECAUSE YOU'RE NO LONGER OUR CLASSMATE... I HATE IT!" # @t_santibravo540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "But..." # @t_santibravo541.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I don't..." # @t_santibravo541.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow3 "WHO CARES WHAT YOU WANT" # @t_santibravo542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow2 "YOU'RE GONNA HELP US KIDNAP PAC-MAN" # @t_santibravo543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow1 "OR WE'RE GONNA TELL ALL YOUR NEW 'FRIENDS' ALL THE HORRIBLE THINGS YOU DID AT EVIL NAMCO HIGH." # @t_santibravo544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(!!!! THEY'RE FROM EVIL NAMCO HIGH!)" # @t_santibravo545.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_surprised as antibravo
    t_ch_antibravo "I... I won't help you guys. It's wrong!" # @t_santibravo546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow3 "FINE... THEN STAY OUTTA OUR WAY!!!!!" # @t_santibravo547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(They want to kidnap Pac-man... This is terrible... )" # @t_santibravo548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_shadow1 "REMEMBER, IF YOU DON'T KEEP YOU TRAP SHUT... WE'LL BE BACK..." # @t_santibravo549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " FOR YOU........." # @t_santibravo549.01 self.block='Last'
    show i_trio_evil as students:
        # ShowWithAtl
        linear .75 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "This is terrible... I have to do something..." # @t_santibravo550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "But no one will ever believe me..." # @t_santibravo551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        ease_expo .6 xpos 0.25 
    extend "{w=0.6}{nw}"
    t_ch_cousin "I believe you!!" # @t_santibravo552.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_shadowknows_surprised as antibravo:
        xzoom 1.0 
    t_ch_antibravo "[slot_playerName]! Oh no... Did you see it all?!" # @t_santibravo553.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_shadowknows_sad as antibravo
    extend " I'm so sorry... I told you to stay away...." # @t_santibravo553.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " No one will ever believe me..." # @t_santibravo553.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I'll back you up!" # @t_santibravo554.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_sad as antibravo:
        linear .33 xzoom -1.0 
    t_ch_antibravo "They'll just think I brainwashed you or something." # @t_santibravo555.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    show i_pacman_left as pacman zorder 1:
        default
        alpha 1.0
        xpos 1.35 
    t_ch_cousin "(He's despondent... )" # @t_santibravo556.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        pause 0.33 
        linear 3 xpos 0.88 
    extend "{w=3.33}{nw}"
    t_ch_pacman "BE TRUE TO YOURSELF........." # @t_santibravo557.00 self.block='Last'
    stop sound
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_sad as antibravo:
        xzoom 1.0 
        # ShowWithAtl
        linear .25 xpos 0.35 
    show i_cousin_energetic_neutral as cousin:
        # ShowWithAtl
        linear .25 xpos 0.15 
    extend "{w=0.25}{nw}"
    t_ch_cousin "EXcuse you! You're butting in on a private conversation!" # @t_santibravo558.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        pause 0.75 
        ease_expo 2 xpos 1.35 
    extend "{w=2.75}{nw}"
    t_ch_pacman ".... be true to yourself.........." # @t_santibravo559.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_angry as cousin:
        # ShowWithAtl
        linear .25 xpos 0.3 
    show i_abm_default_surprised as antibravo:
        # ShowWithAtl
        linear .25 xpos 0.7 
    extend "{w=0.25}{nw}"
    t_ch_cousin "RUDE!" # @t_santibravo560.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The nerve of this guy...." # @t_santibravo560.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_surprised_blush as antibravo
    t_ch_antibravo "[slot_playerName]..." # @t_santibravo561.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Yeah?" # @t_santibravo562.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_surprised_blush as antibravo:
        linear .33 xzoom -1.0 
    t_ch_antibravo "That was Pac-Man." # @t_santibravo563.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Ah!" # @t_santibravo564.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " ..........." # @t_santibravo564.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "AHHHHHHH!" # @t_santibravo565.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin
    t_ch_cousin "Are you..." # @t_santibravo566.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Are you sure?!" # @t_santibravo566.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "He was big and yellow." # @t_santibravo567.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I think it's a safe bet." # @t_santibravo567.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Oh dear........." # @t_santibravo568.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_default_sad as antibravo
    t_ch_antibravo "[slot_playerName]... When I say I want to be a good guy... You believe me, right?" # @t_santibravo569.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I do. I believe you..." # @t_santibravo570.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " And I believe IN you." # @t_santibravo570.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_shadowknows_sad as antibravo
    t_ch_antibravo "Then I'll try to warn everyone. For Pac-Man, and for you." # @t_santibravo571.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Anti-Bravoman........." # @t_santibravo572.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "?" # @t_santibravo573.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I kind of think that the real you... Is a sincere, thoughtful, kind of vulnerable guy. But there IS another you." # @t_santibravo574.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And it's not the sad, dark you." # @t_santibravo574.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It's a shining, brave, strong you." # @t_santibravo574.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "That's what I think." # @t_santibravo575.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_antibravo "........" # @t_santibravo576.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_abm_backturned_grin as antibravo
    t_ch_antibravo "Thanks." # @t_santibravo577.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...................." # @t_santibravo578.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "" # @t_santibravo579.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(I can't believe I mouthed off at Pac-Man.)" # @t_santibravo580.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(If King were here he'd give me some kind of LEVEL 87: ETERNAL MAZE detention. Or something.)" # @t_santibravo581.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_1T', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_antibravo5__1T:
        # <NHSceneChange NHSceneChange {'name': '_1T', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5