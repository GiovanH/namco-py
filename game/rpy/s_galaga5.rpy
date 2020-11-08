# <Scene {'id': 's_galaga5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_galaga5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_galaga5"
    $ renpy.pause(1)
    # <Scene {'id': 's_galaga5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/romance.ogg" loop
    show i_bg_galaga_house as bg zorder 0 at default
    show i_prop_parents as parents zorder 2:
        default
        xpos 0.85 
        alpha 0.0
    show i_sw_white as white_swatch zorder 9:
        default
        alpha 0.0
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_sw_black as darkness zorder 1:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 3:
        default
        xpos 0.25 
    show i_galaga_default as galaga zorder 1:
        default
        xpos 0.75 
        alpha 0.0
    show i_pacman_left as pacman zorder 1:
        default
        xpos 1.35 
    t_ch_cousin "WOW." # @t_sgalaga50.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Maybe Galaga Ship is wrong and they really got the part because of the villa…" # @t_sgalaga51.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "Anyway, I need to talk to Galaga Ship!" # @t_sgalaga52.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But how!" # @t_sgalaga52.01 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ah! I’ll just throw some rocks at its window." # @t_sgalaga53.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh." # @t_sgalaga53.01 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Which window though???" # @t_sgalaga53.02 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Obvious solution:" # @t_sgalaga54.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "THROW ROCKS AT ALL WINDOWS AT ONCE!" # @t_sgalaga55.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " No, wait. That’s crazy." # @t_sgalaga55.01 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "The courtyard is so immaculate I’d never find enough rocks to do that. Duh!" # @t_sgalaga56.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Wow, is that a hedge maze?" # @t_sgalaga57.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_default as galaga:
        # ShowWithAtl
        linear .5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_galaga "{smallcaps}Who’s out there?{/smallcaps}" # @t_sgalaga58.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh crap! No, wait. That’s good!" # @t_sgalaga59.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}[slot_playerName]? Is that you?{/smallcaps}" # @t_sgalaga510.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "No!" # @t_sgalaga511.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Wait. Yes, though. How’d you know I was out here?" # @t_sgalaga512.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You’re talking to yourself right outside my window.{/smallcaps}" # @t_sgalaga513.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified_blush as cousin
    t_ch_cousin "Oh, right." # @t_sgalaga514.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Darn it, [slot_playerName]! Internal monologue! Like this!)" # @t_sgalaga514.01 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}It’s late. What are you doing?{/smallcaps}" # @t_sgalaga515.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "I came to apologize!" # @t_sgalaga516.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}For what? Waking me up? You could’ve stayed home and saved some time!{/smallcaps}" # @t_sgalaga517.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "No, not that." # @t_sgalaga518.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh, sorry about that too though." # @t_sgalaga518.01 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But I meant about the double detention." # @t_sgalaga519.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}It’s not your fault.{/smallcaps}" # @t_sgalaga520.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah, well…" # @t_sgalaga521.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral_blush as cousin
    t_ch_cousin "I just wanted to say, um, my bad anyway!" # @t_sgalaga522.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Who says “my bad” anymore?{/smallcaps}" # @t_sgalaga523.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_blush as cousin
    t_ch_cousin "Lots of people!" # @t_sgalaga524.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Where I’m from." # @t_sgalaga525.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Well, they used to. So many years ago…)" # @t_sgalaga525.01 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s making a comeback!" # @t_sgalaga525.02 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}No, I doubt that. Donko would’ve mentioned it to me.{/smallcaps}" # @t_sgalaga526.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Anyway, I accept your anachronistic and unnecessary apology all the same.{/smallcaps}" # @t_sgalaga527.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Great! Because I really wanted to talk about that stuff you mentioned earlier." # @t_sgalaga528.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Oh. What, about not earning the part?{/smallcaps}" # @t_sgalaga529.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You should just ignore whatever I said.{/smallcaps}" # @t_sgalaga530.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad_blush as cousin
    t_ch_cousin "But it’s a real problem! And you shouldn’t have to feel that way." # @t_sgalaga531.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Oh, [slot_playerName]. Don’t you know how insidious it is? I can’t be sure you’re not pretending to care just to get close to me.{/smallcaps}" # @t_sgalaga532.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wow, that’s pretty twisted! Hadn’t thought of it like that.)" # @t_sgalaga533.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Do you understand now? It’s hopeless. Just forget about me and get home before it starts to rain.{/smallcaps}" # @t_sgalaga534.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(What choice do I have…?)" # @t_sgalaga535.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(There’s no way through it.)" # @t_sgalaga536.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Except…)" # @t_sgalaga536.01 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You leave me no choice, Galaga Ship." # @t_sgalaga536.02 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "There’s nothing left for me to do but…" # @t_sgalaga537.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    extend " USE TOTAL HONESTY!" # @t_sgalaga537.01 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}!!!!{/smallcaps}" # @t_sgalaga538.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Here goes nuthin’!)" # @t_sgalaga539.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I admit I was completely taken with your beautiful hull and that’s what brought me to the Drama Club. No, it’s true! It was just a lucky coincidence I happen to possess amazing  innate acting skills that made possible my unique take on Romeo that was, I guess, too avant garde for a mere high school production!" # @t_sgalaga539.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But then I got to know you! And I saw the lonely spaceship lost in a crowd of admirers. That’s no way to go through life! You need a true friend and I can do that for you, Galaga Ship, if you’ll let me." # @t_sgalaga540.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "But…" # @t_sgalaga541.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But I understand if you can’t. Some people need to find their own way, spaceships too I guess, and that’s okay." # @t_sgalaga542.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}…{/smallcaps}" # @t_sgalaga543.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}You…{/smallcaps}" # @t_sgalaga543.01 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You mean it?{/smallcaps}" # @t_sgalaga544.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m a little nervous right now, so don’t quiz me on every little thing I said exactly, but yeah I meant all of it." # @t_sgalaga545.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You really think you’re a good actor?{/smallcaps}" # @t_sgalaga546.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified_blush as cousin
    t_ch_cousin "(That’s a weird thing to focus on!)" # @t_sgalaga547.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But this is an emotional time and it’s easy to lose focus on stuff.)" # @t_sgalaga548.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}If you were truly doing things only to impress me…{/smallcaps}" # @t_sgalaga549.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You wouldn’t have DARED to get up on stage.{/smallcaps}" # @t_sgalaga550.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You gave it your best most honest shot and it turned out, uh…{/smallcaps}" # @t_sgalaga551.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}…the way that it did.{/smallcaps}" # @t_sgalaga552.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Yes, those of us on the cutting edge of culture are often ridiculed for our brave expeditions into uncharted territory!)" # @t_sgalaga553.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You would have done anything else rather than allow yourself to be embarrassed like that.{/smallcaps}" # @t_sgalaga554.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Maybe…maybe you are being genuine with me. Is..is it even possible?{/smallcaps}" # @t_sgalaga555.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You’re a wonderful young spaceship and, I mean, I’m open to something more, but I’d be honored to be a part of your life that makes you happy. And if that means being a true friend..." # @t_sgalaga556.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "…I’M THERE!" # @t_sgalaga557.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Oh…oh, [slot_playerName]!{/smallcaps}" # @t_sgalaga558.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    stop music fadeout 1.0
    show i_cousin_energetic_surprise_blush as cousin:
        # ShowWithAtl
        ease_expo .3 xpos 0.13 
    show i_galaga_default as galaga:
        # ShowWithAtl
        ease_expo .3 xpos 0.5 
    show i_prop_parents as parents:
        # ShowWithAtl
        pause 0.3 
        linear .5 alpha 1.0
    extend "{w=0.8}{nw}"
    t_ch_parents "What’s all this racket?" # @t_sgalaga559.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}MOM!!! DAD!!!{/smallcaps}" # @t_sgalaga560.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Ack!" # @t_sgalaga561.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}It’s not what it looks like!{/smallcaps}" # @t_sgalaga562.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "It looks like this hooligan is trespassing!" # @t_sgalaga563.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Hooligan?! WHERE!" # @t_sgalaga564.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "Don’t get smart with me, kid. You think you’re the first suitor to throw rocks at my spaceship’s window in the middle of the night?" # @t_sgalaga565.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "That’s why we don’t have any rocks in the garden!" # @t_sgalaga566.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "Heck, what do you think the hedge maze is for?" # @t_sgalaga567.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "Aesthetics, yes, but also TO LEAD YOU KIDS AWAY!" # @t_sgalaga568.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_default as galaga:
        # ShowWithAtl
        pause 0.75 
        ease_expo 1 xpos 1.49 
    extend "{w=1.75}{nw}"
    t_ch_galaga "{smallcaps}You guys are so embarrassing!{/smallcaps}" # @t_sgalaga569.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "Shut the window and get back to your docking bay!" # @t_sgalaga570.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        ease_expo .2 xpos 0.25 
    extend "{w=0.2}{nw}"
    t_ch_parents "As for you, shorty." # @t_sgalaga571.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Hey!" # @t_sgalaga572.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "I forbid you from visiting my spaceship in school and especially in the middle of the night!" # @t_sgalaga573.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "Mrs. Galaga Ship and I have work in the morning!" # @t_sgalaga574.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "Our spaceship has school in the morning!" # @t_sgalaga575.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "Even a delinquent like yourself with all kinds of extra detention has to show up to cause more trouble for innocent school kids at some point!" # @t_sgalaga576.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "That is not a fair assessment of my average morning!" # @t_sgalaga577.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " (Although I did kind of roll up everything that wasn’t nailed down and most of the stuff that was on my first day…)" # @t_sgalaga577.01 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(And he’s not wrong about the extra detention thing either…)" # @t_sgalaga578.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(And now I’ve gone and woke up the whole Galaga Ship family! I ruined a whole day for all of them before it ever started!)" # @t_sgalaga579.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Gosh, maybe I should just leave Galaga Ship alone. I’ve done nothing but cause grief!)" # @t_sgalaga580.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "Go on now, get out of here! I don’t ever want to see you again!" # @t_sgalaga581.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/thunderclap.ogg"
    show i_sw_white as white_swatch:
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        pause 0.1 
        linear .2 alpha 0.0
    show i_sw_black as darkness:
        # ShowWithAtl
        linear 0.3 alpha 0.5
    extend "{w=0.5}{nw}"
    t_ch_thunder "KABOOOOM!" # @t_sgalaga582.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/rushingwater.ogg" loop
    t_ch_rain "TORRENTIAL!!!" # @t_sgalaga583.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_parents "And stay away from our spaceship forever!" # @t_sgalaga584.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/slam.ogg"
    show i_prop_parents as parents:
        # ShowWithAtl
        linear .1 alpha 0.0
    extend "{w=0.1}{nw}"
    t_ch_door "slam!" # @t_sgalaga585.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_prop_parents as parents:
        # ShowWithAtl
        linear .33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_parents "We’re glad it’s raining on you!" # @t_sgalaga586.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    stop sound fadeout 1.0
    play sound "sfx/slam.ogg"
    show i_prop_parents as parents:
        # ShowWithAtl
        linear .1 alpha 0.0
    extend "{w=0.1}{nw}"
    t_ch_door "SLAM!!!" # @t_sgalaga587.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "Nothing left to do but walk home in the rain and be super sad about everything." # @t_sgalaga588.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Times like this I wish I could just roll up all my problems, but emotions won’t stick to a katamari!" # @t_sgalaga589.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Though more immediately, it’d be nice if rain clouds did so I could be super sad but dry." # @t_sgalaga590.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Maybe I could stumble upon a cliff on my way home. And then fall over the cliff." # @t_sgalaga591.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "No, that’s going too far. I’ll just be super sad." # @t_sgalaga592.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        ease_expo 5 xpos 0.75 
    extend "{w=5.0}{nw}"
    t_ch_pacman "[slot_playerName]." # @t_sgalaga593.00 self.block='Last'
    stop sound
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh, Pac-Man? What are you doing out here in the rain?" # @t_sgalaga594.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Be true to yourself, [slot_playerName]." # @t_sgalaga595.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I don’t know what that means…" # @t_sgalaga596.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Be true to yourself." # @t_sgalaga597.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Yeah, but could you be a little less vague about what the means? It’s raining and I’m super sad." # @t_sgalaga598.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "[slot_playerName]." # @t_sgalaga599.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Be true to yourself." # @t_sgalaga5100.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That doesn’t really help me right now, Pac-Man." # @t_sgalaga5101.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Unless…" # @t_sgalaga5102.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Unless you mean that being super sad is a way of lying to myself." # @t_sgalaga5103.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "A way to wallow in negativity and to deny my true self: the part of me that says YES!" # @t_sgalaga5104.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Yes, some people seem to think I’m a bad actor, but really I’m quite naturally gifted and just do a different take than most!" # @t_sgalaga5105.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And that doesn’t mean I shouldn’t try to be anything less than the best actor I can be!" # @t_sgalaga5106.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I kinda screwed up apologizing to Galaga Ship, and now its parents hate me, but that doesn’t mean it’s the end of the world, does it?" # @t_sgalaga5107.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "All I have to do is stop TRYING to be a part of Galaga Ship’s life and to SIMPLY be who I am. To take a step back and let Galaga Ship make the next move!" # @t_sgalaga5108.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    extend " IT COULDN’T BE SIMPLER!" # @t_sgalaga5108.01 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Pac-Man, you are a true inspiration!" # @t_sgalaga5109.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m gonna go straight home and be the best [slot_playerName] there is!" # @t_sgalaga5110.00 self.block='Last'
    show i_cousin_energetic_grin as cousin:
        # ShowWithAtl
        linear .5 alpha 0.0
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "What an odd youngster. I would have been happy to share my umbrella..." # @t_sgalaga5111.00 self.block='Last'
    # <NHSceneChange {'name': '_26', 'scene': 's_day5.5'} NHSceneChange ''>
    label s_galaga5__26:
        # <NHSceneChange {'name': '_26', 'scene': 's_day5.5'} NHSceneChange ''>
        jump s_day5p5