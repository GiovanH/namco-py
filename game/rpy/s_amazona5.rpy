# <Scene scene {'id': 's_amazona5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_amazona5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_amazona5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_amazona5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/romance.ogg" loop
    show i_bg_cliff_day as bg zorder 0 at default
    show i_sw_white as white_swatch zorder 15:
        default
        alpha 0.0
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.25 
    show i_aki_default_smile as aki zorder 1:
        default
        xpos 0.75 
    show i_pacman_left as pacman zorder 2:
        default
        alpha 1.0
        xpos 1.49 
    show i_amazona_default_smile as amazona zorder 1:
        default
        alpha 0.0
        xpos 0.7 
    t_ch_aki "Thanks for carrying my notebook, [slot_playerName]!" # @t_samazona523.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "It's no problem! That's what an assistant is for!" # @t_samazona524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_aki_default_nervouslaughter as aki
    t_ch_aki "Hahaha... You want to be my assistant?" # @t_samazona525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I do." # @t_samazona526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What's wrong, Aki?" # @t_samazona527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_aki_default_distracted as aki
    t_ch_aki "Well [slot_playerName]... I just wanted to apologize. I know I've been acting weird for a while now..." # @t_samazona528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And you've been really patient with me." # @t_samazona528.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Well, I did ask a bunch of questions that were maybe a little out of line..." # @t_samazona529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_aki "It's okay." # @t_samazona530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_aki "........................" # @t_samazona531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_aki "[slot_playerName], can you keep a secret?" # @t_samazona532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Of course." # @t_samazona533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_aki "We didn't come out here to get soil samples." # @t_samazona534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "We didn't?" # @t_samazona535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_aki "No... Actually, I wanted to talk to you." # @t_samazona536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_aki_justice_overwhelmed as aki
    t_ch_aki "Can you keep another, bigger secret?" # @t_samazona537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Um... For sure." # @t_samazona538.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_aki_justice_shocked as aki
    t_ch_aki "Like... REALLY BIG. Like HUGE. Like we can't even talk about it over the phone because the NSA will totally get up in my business." # @t_samazona539.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "NSA?" # @t_samazona540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_aki_justice_laughter_nervous as aki
    t_ch_aki "Namco Security Agency." # @t_samazona541.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Right." # @t_samazona542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_aki_default_focus as aki
    t_ch_aki "Anyway, It's A HUGE HUGE DEAL." # @t_samazona543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "AKI! Just tell me!" # @t_samazona544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin ".................." # @t_samazona545.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She just took a really deep breath." # @t_samazona546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_aki_akimbo_focus as aki
    extend " Now she's fiddling with something....)" # @t_samazona546.01 self.block='Last'
    show i_sw_black as white_swatch:
        alpha 0.0
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5) # Curtain fade
    show i_bg_cliff_day as bg # behind white_swatch
    # <SettingChange SettingChange {'bgImage': '@i_bg_cliff_day', 'curtainActor': 'white_swatch', 'curtainFadeTime': '.5', 'name': '_Q', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_akimbo_distracted as amazona
    play sound "sfx/transform2.ogg"
    show i_aki_akimbo_focus as aki:
        # ShowWithAtl
        linear 1 alpha 0.0
    show i_amazona_akimbo_distracted as amazona:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    stop music fadeout 1.0
    show i_sw_black as white_swatch:
        alpha 1.0
        linear 0.5 alpha 0.0
    $ renpy.pause(0.5) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "!!!!" # @t_samazona547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Aki... Is that YOU?!" # @t_samazona548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "It's me, [slot_playerName]." # @t_samazona549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_nervouslaugh as amazona
    t_ch_amazona "I'm Amazona... a superhero who protects the earth from interdimensional aliens." # @t_samazona550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "THERE ARE ALIENS?!" # @t_samazona551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "ALIENS ARE REAL???" # @t_samazona552.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(Besides me, I mean.)" # @t_samazona553.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "You're real?!" # @t_samazona554.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "This is all... Real?!" # @t_samazona555.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_distracted as amazona
    t_ch_amazona "It is." # @t_samazona556.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "But... But how?!" # @t_samazona557.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_focus as amazona
    t_ch_amazona "I'm not the first... I inherited my power from the previous Amazona. With this power comes responsibility." # @t_samazona558.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "[slot_playerName]..." # @t_samazona559.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "Intergalactic aliens known as the Waru are invading the earth, even as we speak." # @t_samazona560.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_amazona "They must be stopped." # @t_samazona561.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "So every time your theme song plays... You're leaving to go defend the earth from alien invaders?" # @t_samazona562.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_akimbo_distracted as amazona
    t_ch_amazona "Yeah... Sorry." # @t_samazona563.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "NO DON'T APOLOGIZE" # @t_samazona564.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "THAT'S A REALLY GOOD REASON" # @t_samazona565.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Don't stop on my account!" # @t_samazona566.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_akimbo_laugh as amazona
    t_ch_amazona "Haha!" # @t_samazona567.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(That's the first genuine laugh I've heard from her... It's nice.)" # @t_samazona568.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_focus as amazona
    t_ch_amazona "I brought you up here to tell you the truth. This city... And Namco High... Are my responsibility. I have to protect them." # @t_samazona569.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "But the Waru attacks have been growing... Between that and trying to maintain a 4.0 and perfect club attendance, my relationships with the people around me suffer." # @t_samazona570.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Aki... Aren't you lonely?" # @t_samazona571.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_distracted as amazona
    t_ch_amazona "I guess I am... But I can't slow down now." # @t_samazona572.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "But Aki... You don't have to be perfect at everything. You can relax sometimes..." # @t_samazona573.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "And it's okay to rely on others! Sometimes two can do more than one ever could!" # @t_samazona574.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "But... All that being said... I want you to know I truly admire how hard you work." # @t_samazona575.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_smile as amazona
    t_ch_amazona "Thanks [slot_playerName]... I wish the others could understand." # @t_samazona576.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "If I can help shoulder the burden in any way... I mean, my shoulders are very small, but I'm strong." # @t_samazona577.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Super strong!" # @t_samazona578.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Don't forget, I rolled Dig Dug's car up just last week!" # @t_samazona578.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_akimbo_laugh as amazona
    t_ch_amazona "Haha..." # @t_samazona579.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Aki..." # @t_samazona580.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I've been wondering... If defending the earth is a priority... Why all the classes? Why all the clubs? What's the point? You could defend the earth... And also have time for friends." # @t_samazona581.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_akimbo_distracted as amazona
    t_ch_amazona "To tell you the truth... Sometimes I DO wonder if I'm doing too much." # @t_samazona582.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "I could be like all the other students... Leading happy, fulfilling lives in this school." # @t_samazona583.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_distracted as amazona
    t_ch_amazona "Instead of living the never-ending life of a perfectionist..." # @t_samazona584.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "?!" # @t_samazona585.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "?!" # @t_samazona586.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_shocked as amazona:
        # ShowWithAtl
        ease_expo .33 xpos 0.39 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        ease_expo .33 xpos 0.11 
    show i_pacman_left as pacman:
        # ShowWithAtl
        pause 0.33 
        linear 3 xpos 0.88 
    $ renpy.pause(3.33, hard=True) # TimedPause
    stop sound
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "BE TRUE TO YOURSELF......." # @t_samazona587.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "What does that mean, Pac-man? What should I do..." # @t_samazona588.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "BE TRUE... TO YOURSELVES..." # @t_samazona589.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        pause 2.0 
        ease_expo .33 xpos 0.25 
    show i_amazona_default_shocked as amazona:
        # ShowWithAtl
        pause 2.0 
        ease_expo .33 xpos 0.75 
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 3 xpos 1.5 
    $ renpy.pause(3.0, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_distracted as amazona
    t_ch_amazona "[slot_playerName]..." # @t_samazona590.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "I was ready to go it alone, but..." # @t_samazona591.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_smile as amazona
    t_ch_amazona "Will you help me?" # @t_samazona592.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "YES!" # @t_samazona593.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Of course! I'll be the best assistant you've ever had. AND I'll keep your secret, too." # @t_samazona594.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "[slot_playerName]... Do you know the number one mistake most superheroes make?" # @t_samazona595.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_akimbo_focus as amazona
    t_ch_amazona "No infrastructure. Fighting aliens doesn't pay the bills." # @t_samazona596.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It doesn't get you the equipment you need to defend the earth..." # @t_samazona596.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_akimbo_distracted as amazona
    extend " It doesn't get you the upgrades you need as those threats become bigger." # @t_samazona596.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_akimbo_focus as amazona
    t_ch_amazona "You're forever barely scraping by, battle after battle, wearing down till you finally lose." # @t_samazona597.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain zorder 1:
        # FadeEvent
        linear 1.5 alpha 1.0
    extend "{w=1.5}{nw}"
    t_ch_amazona "I'll never lose." # @t_samazona598.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "I want to build something for all the Amazonas who come after me. So they'll be more prepared than I am." # @t_samazona599.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "I'm still young... I want to use my time wisely." # @t_samazona5100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "I'm going to build an empire, [slot_playerName]." # @t_samazona5101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_akimbo_focus as amazona:
        # FadeEvent
        linear 0.85 alpha 0.0
    extend "{w=0.85}{nw}"
    t_ch_cousin "(Looking back... Those are still the most amazing words I've ever heard.)" # @t_samazona5102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(The memory of that day has never faded.)" # @t_samazona5103.00 self.block='Last'
    show i_cousin_default_grin as cousin:
        # FadeEvent
        linear 1.0 alpha 0.0
    # <NHSceneChange NHSceneChange {'name': '_1U', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_amazona5__1U:
        # <NHSceneChange NHSceneChange {'name': '_1U', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5