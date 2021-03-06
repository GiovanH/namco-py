# <Scene scene {'id': 's_valk3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_valk3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_valk3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_valk3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/romance.ogg" loop
    show i_bg_hallway_b as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.4 
    show i_valkyrie_default_grin as valkyrie zorder 2:
        default
        xpos 0.6 
    t_ch_cousin "(Holding her hand like this... It's so nice." # @t_svalk321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    extend " But why does she want to go to the roof with me… and alone?!)" # @t_svalk321.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(It's making me nervous... )" # @t_svalk322.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It's just that she's so flirtatious and I wonder how much she assumes... )" # @t_svalk323.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified_blush as cousin
    t_ch_cousin "(And also... I can't control my imagination!)" # @t_svalk324.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0) # Curtain fade
    show i_bg_rooftop as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_rooftop', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_5', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.25 
    show i_valkyrie_default_thoughtful as valkyrie:
        # ShowWithAtl
        linear 0.5 xpos 0.75 
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "OMG! Look at that sky!" # @t_svalk325.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie
    extend " I love it up here." # @t_svalk325.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Y-yeah..." # @t_svalk326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Listen..." # @t_svalk326.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie
    t_ch_valkyrie "It's time..." # @t_svalk330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Oh dear..." # @t_svalk331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie
    t_ch_valkyrie ".... FOR PWNAGE!" # @t_svalk332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "WHAT?!" # @t_svalk333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She took out two practice swords!)" # @t_svalk334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_bored as valkyrie
    t_ch_valkyrie "Wait..." # @t_svalk335.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_bored as valkyrie
    extend " What'd you think I was going to say?!" # @t_svalk335.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "NOTHING! I had no preconceptions!!" # @t_svalk336.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin
    extend " I'M A BLANK SLATE" # @t_svalk336.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " TOTALLY INNOCENT" # @t_svalk336.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " PURE THOUGHTS" # @t_svalk336.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " PURE AS UNTREAD SNOW" # @t_svalk336.04 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " AH HA HA HA" # @t_svalk336.05 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Hmmm." # @t_svalk337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(What is this twinge? Is it... Disappointment?)" # @t_svalk338.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie
    t_ch_valkyrie "Arm yourself, noob!" # @t_svalk339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "AH!" # @t_svalk340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She threw it at me! I barely caught it.)" # @t_svalk341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It... It's made of wood! I really think we should be using foam... It's much safer, you know.)" # @t_svalk342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        linear .3 xpos 0.2 
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear .3 xpos 0.8 
    extend "{w=0.3}{nw}"
    t_ch_cousin "(Also, NOT sword-fighting is a lot safer than sword-fighting.)" # @t_svalk343.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Valkyrie is looking down the blade and holding it kind of lightly... I think she's checking the balance? That's a sword thing, right?)" # @t_svalk344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Now she's doing all kinds of warm-ups? Sword warm-ups? I don't even know what they're called... )" # @t_svalk345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    extend "{w=1.3}{nw}"
    t_ch_cousin "(She threw it up into the air! It's spinning... Oh wow, she snatched it up before it hit the ground. How did she even know which end to catch?!)" # @t_svalk346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie
    t_ch_valkyrie "Ready, noob?" # @t_svalk347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "ABSOLUTELY NOT!" # @t_svalk348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Sometimes... You have to live in the moment, [slot_playerName]. Give yourself to the present!" # @t_svalk349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie
    t_ch_valkyrie "NO HESITATION!" # @t_svalk350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I'M FULL OF HESITATION! AND FEELINGS! SOMETIMES AN UNCOMFORTABLE MIX OF THE TWO!" # @t_svalk351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin
    t_ch_cousin "ADOLESCENCE IS A HORRIFYING COCKTAIL OF HIGHS AND LOWS!" # @t_svalk352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "AHHHHH!" # @t_svalk353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        linear .5 xpos 0.5 
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear .1 xpos 0.15 
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
        # ShowWithAtl
        pause 0.2 
        linear .05 xpos 0.25 
    play sound "sfx/swordclank2.ogg"
    extend "{w=0.5}{nw}"
    t_ch_cousin "(SHE'S CHARGING! Which end do I hold?! I think it's backwards!)" # @t_svalk354.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/swordclank1.ogg"
    play sound "sfx/swordclank2.ogg"
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .1 xpos 0.85 
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .1 xpos 0.15 
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
        # ShowWithAtl
        pause 0.2 
        linear .05 xpos 0.3 
        # ShowWithAtl
        pause 0.3 
        linear .1 xpos 0.75 
        # ShowWithAtl
        pause 0.5 
        linear 0.5 xzoom 1.0 
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        pause 0.4 
        linear 0.5 xzoom -1.0 
    $ renpy.pause(1.0, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I DID IT! I blocked! AH, she's coming again!)" # @t_svalk355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She's clearly going all out!)" # @t_svalk356.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/swordclank2.ogg"
    play sound "sfx/swordclank2.ogg"
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .1 xpos 0.15 
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .1 xpos 0.85 
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
        # ShowWithAtl
        pause 0.2 
        linear .05 xpos 0.7 
        # ShowWithAtl
        pause 0.3 
        linear .1 xpos 0.25 
        # ShowWithAtl
        pause 0.5 
        linear 0.5 xzoom -1.0 
    show i_cousin_energetic_mortified as cousin:
        # ShowWithAtl
        pause 0.4 
        linear 0.5 xzoom 1.0 
    $ renpy.pause(1.0, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/swordclank1.ogg"
    play sound "sfx/swordclank2.ogg"
    play sound "sfx/swordclank2.ogg"
    play sound "sfx/swordclank1.ogg"
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .1 xpos 0.85 
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .1 xpos 0.15 
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
        # ShowWithAtl
        pause 0.2 
        linear .05 xpos 0.3 
        # ShowWithAtl
        pause 0.3 
        linear .1 xpos 0.75 
        # ShowWithAtl
        pause 0.5 
        linear 0.5 xzoom 1.0 
    show i_cousin_energetic_mortified as cousin:
        # ShowWithAtl
        pause 0.4 
        linear 0.5 xzoom -1.0 
    extend "{w=1.0}{nw}"
    t_ch_valkyrie "Step it up! I'm not even going all out!" # @t_svalk357.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(I'M GOING TO DIE HERE)" # @t_svalk358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin:
        # ShowWithAtl
        linear 1 xpos 0.25 
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
    extend "{w=1.0}{nw}"
    t_ch_valkyrie "Are you having fun?!" # @t_svalk359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_angry as cousin
    t_ch_cousin "WHAT IS YOUR DEFINITION OF FUN" # @t_svalk360.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie
    t_ch_valkyrie "Why are you yelling?" # @t_svalk361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_angry as cousin
    t_ch_cousin "I'M NOT YELLING" # @t_svalk362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Okay, I'm yelling a little bit. Valkyrie, I'm not very good at this!" # @t_svalk363.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Nonsense! You're starting to get the basics down." # @t_svalk364.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And don't worry..." # @t_svalk364.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie
    extend " I'm being gentle!" # @t_svalk364.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "THERE'S NOTHING GENTLE ABOUT SWORDFIGHTING" # @t_svalk365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "The only thing I'm good at is rolling!" # @t_svalk366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie
    t_ch_valkyrie "So pretend like it's rolling!" # @t_svalk367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "IT'S NOTHING LIKE ROLLING" # @t_svalk368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_grin as valkyrie
    t_ch_valkyrie "Is rolling what got you into detention?" # @t_svalk369.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin ".........." # @t_svalk370.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Yeah......" # @t_svalk370.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grin as valkyrie
    t_ch_valkyrie "I knew it! I was sure it was you I saw." # @t_svalk371.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie
    extend " That was awesome!" # @t_svalk371.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "You did?! It was?!" # @t_svalk372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Yeah, I LOLed so hard." # @t_svalk373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Dig Dug was pretty mad, but he was stuck to the outside of your Katamari so all he could do was flail his little arms and legs." # @t_svalk373.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_wink as valkyrie
    t_ch_valkyrie "It was awesome! You ARE really good at rolling." # @t_svalk374.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Somehow... I'm a little happy that she saw me roll up all that stuff." # @t_svalk375.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    extend " And she said it made her laugh... )" # @t_svalk375.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie:
        # ShowWithAtl
        linear .3 xpos 0.7 
    extend "{w=0.3}{nw}"
    t_ch_valkyrie "Hey, you're blushing! What're you thinking about!" # @t_svalk376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "(AH! She intensified her attack!" # @t_svalk377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin
    extend "{w=0.7}{nw}"
    extend " Maybe it's time for me to go... On the offensive.)" # @t_svalk377.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin:
        # ShowWithAtl
        linear .3 xpos 0.35 
    extend "{w=0.3}{nw}"
    t_ch_cousin "Say, Valkyrie... Why are YOU in detention?" # @t_svalk378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_bored as valkyrie
    t_ch_valkyrie "You're 1000 years too early to get me, [slot_playerName]!" # @t_svalk379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral_blush as cousin
    t_ch_cousin "Valkyrie, really. I've been wondering." # @t_svalk380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_melancholy as valkyrie
    t_ch_valkyrie "................" # @t_svalk381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_melancholy as valkyrie:
        # ShowWithAtl
        linear .5 xpos 0.75 
    extend "{w=0.5}{nw}"
    extend " I tried to turn back the big school clock." # @t_svalk381.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "Why would you do that?!" # @t_svalk382.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "It's because......." # @t_svalk383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_wink as valkyrie
    extend " I love the 80s! And I thought that big clock could take me back!" # @t_svalk383.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised_blush as cousin
    t_ch_cousin "O-oh." # @t_svalk384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(That's... Weird.)" # @t_svalk385.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What do you like so much about the 80s?" # @t_svalk386.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_melancholy as valkyrie
    t_ch_valkyrie "I just liked it okay?! It's the perfect decade!" # @t_svalk387.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "You just seem really desperate to get back there..." # @t_svalk388.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "It just seems like maybe there's a little more to it...." # @t_svalk389.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie
    t_ch_valkyrie "Prepare yourself for PWNAGE, [slot_playerName]!!" # @t_svalk390.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin:
        # ShowWithAtl
        linear .3 xpos 0.5 
    play sound "sfx/swordclank1.ogg"
    play sound "sfx/swordclank1.ogg"
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .05 xpos 0.85 
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .05 xpos 0.15 
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
        # ShowWithAtl
        pause 0.2 
        linear .05 xpos 0.3 
        # ShowWithAtl
        pause 0.05 
        linear .1 xpos 0.75 
        # ShowWithAtl
        pause 0.5 
        linear 0.5 xzoom -1.0 
    extend "{w=1.0}{nw}"
    t_ch_cousin "(Uh-oh... The atmosphere changed somehow... )" # @t_svalk391.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/swordclank1.ogg"
    play sound "sfx/swordclank2.ogg"
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .05 xpos 0.15 
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .05 xpos 0.85 
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
        # ShowWithAtl
        pause 0.1 
        linear .02 xpos 0.7 
        # ShowWithAtl
        pause 0.1 
        linear .1 xpos 0.1 
        # ShowWithAtl
        pause 0.1 
        linear 0.5 xzoom -1.0 
    show i_cousin_default_mortified as cousin:
        # ShowWithAtl
        linear .4 xpos 0.65 
        # ShowWithAtl
        pause 0.4 
        linear 0.5 xzoom 1.0 
    extend "{w=0.9}{nw}"
    t_ch_cousin "(Did her attacks become... Faster?)" # @t_svalk392.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin:
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
    extend "{w=0.5}{nw}"
    t_ch_cousin "Valkyrie... You're hurting me!" # @t_svalk393.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/swordclank1.ogg"
    play sound "sfx/swordclank1.ogg"
    play sound "sfx/swordclank2.ogg"
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear .1 xpos -0.3 
        # ShowWithAtl
        linear .4 xpos 0.6 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos -0.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
    play sound "sfx/swordclank2.ogg"
    play sound "sfx/swordclank1.ogg"
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear .3 xpos 0.6 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos -0.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
    play sound "sfx/swordclank2.ogg"
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear .2 xpos 0.6 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos -0.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
    play sound "sfx/swordclank1.ogg"
    play sound "sfx/swordclank1.ogg"
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear .1 xpos 0.6 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos -0.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .05 xpos 0.6 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos -0.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .05 xpos 0.6 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos -0.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .05 xpos 0.8 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos 1.3 
        # ShowWithAtl
        pause 1.5 
        linear 0.5 xzoom 1.0 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .05 xpos 0.8 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos 1.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .05 xpos 0.8 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos 1.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .05 xpos 0.8 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos 1.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .05 xpos 0.8 
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear .01 xpos 1.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        pause 2.0 
        linear 0.5 xzoom -1.0 
        # ShowWithAtl
        easeout 1.5 xpos 0.2 
    $ renpy.pause(2.5, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(Something hit me in the head? I think... I'm gonna take a nap....)" # @t_svalk394.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0) # Curtain fade
    show i_bg_hallway_a as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_a', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_1V', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_melancholy as valkyrie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear 0.5 xpos 0.7 
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
    show i_cousin_exhausted_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
        # ShowWithAtl
        linear 0.5 alpha 0.0
    stop music fadeout 1.0
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oogh..." # @t_svalk395.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I'm lying down? What happened?)" # @t_svalk396.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(We were sword-fighting, and then... )" # @t_svalk397.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Oh yeah." # @t_svalk398.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin:
        # ShowWithAtl
        linear 1 alpha 1.0
    extend "{w=1.0}{nw}"
    extend " Oof, my head... )" # @t_svalk398.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_melancholy as valkyrie:
        # ShowWithAtl
        linear 2.5 alpha 1.0
    extend "{w=2.5}{nw}"
    t_ch_valkyrie "Hey champ." # @t_svalk3100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Oof... Hah. I'm not sure that applies here." # @t_svalk3101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I like cutie better, anyway." # @t_svalk3102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "......" # @t_svalk3103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Me too." # @t_svalk3104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_melancholy as valkyrie
    t_ch_valkyrie "Are you okay?" # @t_svalk3105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I think so." # @t_svalk3106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "That's good. I'm sorry… SMH. Sometimes I get into this, like... Sword fugue... And ..." # @t_svalk3107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Anyway, I'm sorry." # @t_svalk3108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It's okay. I have to say... You're pretty handy with a sword." # @t_svalk3109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_thoughtful as valkyrie
    t_ch_valkyrie "It's how I flirt..." # @t_svalk3110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin:
        # ShowWithAtl
        linear .5 xpos 0.35 
    extend "{w=0.5}{nw}"
    t_ch_cousin "Is THAT what we were doing?" # @t_svalk3111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie zorder 1:
        # ShowWithAtl
        linear .5 xpos 0.65 
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "IDK… I was if you were." # @t_svalk3112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(We sit quietly for a while... Just looking at each other.)" # @t_svalk3113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin ".............." # @t_svalk3114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "......................." # @t_svalk3115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "....... You got me pretty good." # @t_svalk3116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grinblush as valkyrie
    t_ch_valkyrie "Sorry... I like to play rough." # @t_svalk3117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I could get used to it." # @t_svalk3118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_thoughtful as valkyrie
    t_ch_valkyrie "Haha! You don't say." # @t_svalk3119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie
    t_ch_cousin "(Maybe it's because she clocked me, but..." # @t_svalk3120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Valkyrie is... really magical.)" # @t_svalk3120.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I don't have another word for it." # @t_svalk3121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I thought she was cute at first... And she totally is..." # @t_svalk3121.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But I really like how engaging she is. If she likes a person, she goes for it." # @t_svalk3121.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " There are so many little things about her that make her her.)" # @t_svalk3121.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(I want to learn all of them.)" # @t_svalk3122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I really, really like her. Sitting here, with her, right now... I think my feelings for her are becoming clear.)" # @t_svalk3123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_thoughtful as valkyrie
    t_ch_valkyrie "[slot_playerName]..." # @t_svalk3124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_thoughtful as valkyrie:
        # ShowWithAtl
        linear .2 xpos 0.55 
        # ShowWithAtl
        pause 0.5 
        linear .4 xpos 0.65 
    show i_cousin_default_surprised_blush as cousin
    extend "{w=0.9}{nw}"
    t_ch_cousin "AH!" # @t_svalk3125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She kissed me! On the cheek, but still... )" # @t_svalk3126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised_blush as cousin
    t_ch_cousin "Whaaaa..." # @t_svalk3127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie
    t_ch_valkyrie "When you think that hard, you get a really cute look on your face." # @t_svalk3128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "--Aaaaaaaaaaaaaaaaaa" # @t_svalk3129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I wanted to." # @t_svalk3130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grinblush as valkyrie
    extend " So I did." # @t_svalk3130.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "I don't mind..." # @t_svalk3131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_thoughtful as valkyrie
    t_ch_valkyrie "Oh...." # @t_svalk3132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Hm?" # @t_svalk3133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Dig Dug came by while you were out... He sentenced us to Detention Level 99: Infinite Ragnarok Detention for fighting on the roof." # @t_svalk3134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    $ renpy.pause(0, hard=True) # Image change
    show i_cousin_default_grin_blush as cousin
    $ renpy.pause(1.0, hard=True) # Text delay
    t_ch_cousin "AH! Oh well... I guess I'll see you soon then, huh?" # @t_svalk3135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie
    t_ch_valkyrie "I know that's gonna be tough for you." # @t_svalk3136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(We sit quietly until the bell rings. It's nice.)" # @t_svalk3137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I can't wait til tomorrow... )" # @t_svalk3138.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_2J', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_valk3__2J:
        # <NHSceneChange NHSceneChange {'name': '_2J', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4