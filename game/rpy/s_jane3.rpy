# <Scene scene {'id': 's_jane3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_jane3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_jane3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_jane3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/aroundtown.ogg" loop
    show i_bg_hallway_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 3:
        default
        xpos 0.3 
    show i_king_screaming as king zorder 2:
        default
        xpos 1.49 
        xzoom -1.0 
    show i_jane_default_grin as jane zorder 3:
        default
        xpos 0.7 
    show i_terezi_default_grin as terezi zorder 2:
        default
        xpos 1.49 
    show i_meowkie_akimbo_alert_badge as meowkie zorder 2:
        default
        xpos -0.49 
    show i_amazona_default_focus as amazona zorder 2:
        default
        xpos -0.49 
    t_ch_cousin "Huh. It was pretty easy to sneak out of detention…" # @t_sjane317.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_grin as jane
    t_ch_jane "Of course it’s easy for a pair of super sleuths like us!" # @t_sjane318.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...I was gonna say…" # @t_sjane319.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " Almost TOO easy." # @t_sjane319.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane
    t_ch_jane "Oh, nonsense. Don’t worry too much!" # @t_sjane320.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I brought disguises for us both, in case someone were to discover us roaming the halls when we shouldn’t." # @t_sjane320.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin as jane
    extend " Here you are! ;B" # @t_sjane320.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(Fake… mustaches…)" # @t_sjane321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral_blush as cousin
    t_ch_cousin "I don’t know if I feel comfortable wearing this in front of you now…" # @t_sjane322.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_laugh_blush as jane
    t_ch_jane "Ahahaha! Ha. Ha…" # @t_sjane323.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin_mustache as jane
    t_ch_jane "Sh-shut up!" # @t_sjane324.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "So where are we going anyway?" # @t_sjane325.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin_mustache as jane
    t_ch_jane "Hoo hoo hoo! That would be telling!" # @t_sjane326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Uh, yeah!" # @t_sjane327.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That’s what I’m asking you to do." # @t_sjane327.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Well, I can maybe give you a little hint." # @t_sjane328.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_grin_mustache as jane
    t_ch_jane "I asked a friend of mine to meet us in the library, which should be empty at this hour…" # @t_sjane328.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Well, as long as we don’t run into the hall monitor, we should be fine." # @t_sjane329.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_meowkie_akimbo_alert_badge as meowkie:
        # ShowWithAtl
        linear 0.70 xpos 0.3 
    show i_jane_default_grin_mustache as jane:
        # ShowWithAtl
        pause 0.5 
        linear 0.20 xpos 0.85 
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        pause 0.5 
        linear 0.20 xpos 0.58 
    extend "{w=0.7}{nw}"
    t_ch_meowkie "H-halt, students!" # @t_sjane330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Shouldn’t you be in detention?" # @t_sjane330.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin:
        linear 0.20 xzoom -1.0 
    t_ch_cousin "Oh no…" # @t_sjane331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Hmm? What is it?" # @t_sjane332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "There’s Meowkie…" # @t_sjane333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "the hall monitor…" # @t_sjane334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin_mustache as jane
    t_ch_jane "Oh pish posh. It’s that silly “talking” cat again." # @t_sjane335.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Perhaps it’s a puppet of some kind…?" # @t_sjane336.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "I think Davesprite knows a thing or two about puppets…" # @t_sjane337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_meowkie_normal_frown_badge as meowkie
    t_ch_meowkie "E-excuse me?!" # @t_sjane338.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_focus as amazona:
        # ShowWithAtl
        linear 0.70 xpos 0.15 
    extend "{w=0.7}{nw}"
    t_ch_amazona "HALT, CITIZENS! You should be in detention!" # @t_sjane339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Omigosh! Who is that amazing superhero?!" # @t_sjane340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’ve never seen her around the school before!" # @t_sjane340.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_grin_mustache as jane
    t_ch_jane "Superhero? Come on, [slot_playerName]. Do you have a pumpkin for a brain?" # @t_sjane341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_laugh_mustache as jane
    t_ch_jane "It’s obviously just a ridiculous costume." # @t_sjane342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_shocked as amazona
    t_ch_amazona "R-Rude…!" # @t_sjane343.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_meowkie_slouch_frown_badge as meowkie
    t_ch_meowkie "I know, right!" # @t_sjane344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Jane, aren’t you at least worried that we’ve been caught?!" # @t_sjane345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " We’re gonna be in SO much trouble…" # @t_sjane345.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin_mustache as jane
    t_ch_jane "Oh, please!" # @t_sjane346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "We can take ‘em ;B" # @t_sjane347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/kingroar3.ogg"
    show i_king_screaming as king:
        # ShowWithAtl
        linear 0.70 xpos 1.0 
    show i_jane_default_grin_mustache as jane:
        # ShowWithAtl
        pause 0.25 
        linear 0.20 xpos 0.65 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        pause 0.25 
        linear .25 xpos 0.4 
        linear .25 xzoom 1.0 
    show i_amazona_default_focus as amazona:
        # ShowWithAtl
        pause 0.25 
        linear .25 xpos 0.05 
    show i_meowkie_slouch_frown_badge as meowkie:
        # ShowWithAtl
        pause 0.25 
        linear .25 xpos 0.2 
    extend "{w=0.7}{nw}"
    t_ch_king "ROOOOAAARRRR!" # @t_sjane348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "GAH!" # @t_sjane349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Don’t tell me you think we can take HIM…?" # @t_sjane349.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Sure, he’s just a normal guy in a mask after all!" # @t_sjane350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_confident as king
    t_ch_king "Roar?!" # @t_sjane351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(How can anyone look at that guy and think “normal”...)" # @t_sjane352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Not to worry, [slot_playerName]." # @t_sjane353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_grin_mustache as jane
    t_ch_jane "I may look like a bespectacled nerdy girl…" # @t_sjane354.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_laugh_mustache as jane
    t_ch_jane "But I can certainly hold my own in a fight!" # @t_sjane355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Watch and learn :B" # @t_sjane356.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "I don’t think fighting a teacher is such a good idea…" # @t_sjane357.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    show i_jane_spoon_grin_mustache as jane
    t_ch_cousin "(Whoah! She just pulled out … what looks like a giant red spoon?!" # @t_sjane358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Where did that come from? Did she just pull it from nowhere?!" # @t_sjane358.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " What on Earth is going on with this girl?!)" # @t_sjane358.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Strife specibus… SPOONKIND!" # @t_sjane359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_spoon_grin_mustache as jane
    t_ch_jane "Aggress!!!" # @t_sjane360.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She’s grabbing my hand and running towards the others…" # @t_sjane361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " I wish she wouldn’t drag me into her death wish!)" # @t_sjane361.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_meowkie_normal_alert_badge as meowkie
    t_ch_meowkie "S-stop!" # @t_sjane362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_amazona_default_shocked as amazona
    t_ch_amazona "Halt!" # @t_sjane363.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_screaming as king
    t_ch_king "ROAR!" # @t_sjane364.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "AUGH!" # @t_sjane365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_spoon_laugh_mustache as jane
    t_ch_jane "Hoo! :B" # @t_sjane366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(She’s just sweeping them aside with her big red spoon thing…" # @t_sjane367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I still don’t know where the heck that came from!" # @t_sjane367.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Or how she can use it so effectively as a weapon!)" # @t_sjane367.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_spoon_grin_mustache as jane
    t_ch_jane "Have at you!" # @t_sjane368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_meowkie "Nyaa-!" # @t_sjane369.00 self.block='Last'
    show i_meowkie_normal_alert_badge as meowkie:
        # FadeEvent
        linear 0.2 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_amazona "Argh!" # @t_sjane370.00 self.block='Last'
    show i_amazona_default_shocked as amazona:
        # FadeEvent
        linear 0.2 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_king "Roar…" # @t_sjane371.00 self.block='Last'
    show i_king_screaming as king:
        # FadeEvent
        linear 0.2 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(I can’t watch…" # @t_sjane372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Omigosh, she actually made it past them??" # @t_sjane373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And she’s still running…" # @t_sjane373.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Looks like… we’re actually in the clear now..)" # @t_sjane374.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # Curtain fade
    show i_bg_library as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_library', 'curtainActor': 'curtain', 'curtainFadeTime': '0.75', 'name': '_1E', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    show i_jane_handonhip_laugh as jane:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    # UNHANDLED TAG <ActorTransform ActorTransform {'name': '_3', 'scaleX': '1', 'target': 'cousin', 'x': '-20%', 'kind': 'ActorTransform'} ''>
    # UNHANDLED TAG <ActorTransform ActorTransform {'name': '_4', 'scaleX': '-1', 'target': 'king', 'x': '100%', 'kind': 'ActorTransform'} ''>
    show i_king_screaming as king:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    show i_meowkie_normal_alert_badge as meowkie:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    # UNHANDLED TAG <ActorTransform ActorTransform {'name': '_7', 'scaleX': '-1', 'target': 'meowkie', 'x': '100%', 'kind': 'ActorTransform'} ''>
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_laugh as jane
    show i_cousin_exhausted_mortified as cousin
    t_ch_jane "Hoo hoo! Nothing like a skirmish to get the blood pumping, huh?" # @t_sjane375.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_smile as jane
    t_ch_jane "How are you doing, [slot_playerName]? Are you alright?" # @t_sjane376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Jane… that was amazing!" # @t_sjane377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But… I don’t understand at all!" # @t_sjane378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " What was that giant spoon thing?!" # @t_sjane378.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    extend " How did you fight with it so well?" # @t_sjane378.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Where is it now?! That thing was huge…" # @t_sjane379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " You couldn’t have just put it in your pocket!" # @t_sjane379.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin as jane
    t_ch_jane "Huh? I’ve had that thing for forever…" # @t_sjane380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "It’s not anything special." # @t_sjane381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_smile as jane
    t_ch_jane "I just captchalogued it. Are you quite sure you’re alright?" # @t_sjane382.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "??!!" # @t_sjane383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Whaa…?" # @t_sjane384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_frustrated as jane
    t_ch_jane "Don’t you have a fetch modus or anything? :|" # @t_sjane385.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Why are you talking silly talk." # @t_sjane386.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Use real words." # @t_sjane386.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_smile as jane
    t_ch_jane "Maybe they call it something different where you’re from…" # @t_sjane387.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "How can you deny that anything weird is going on in this school?!" # @t_sjane388.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Especially now!" # @t_sjane388.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    extend " You’re like… the weirdest person I’ve ever met!" # @t_sjane388.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_frustrated as jane
    t_ch_jane "Hey now! Shut up!" # @t_sjane389.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " There’s no call for language like that." # @t_sjane389.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "I’ve been listening to you jabber on and on about how “strange things” are going on…" # @t_sjane390.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Just because you refuse to use your brain and think about how implausible those things really are!" # @t_sjane390.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "And now, you call ME weird, just because I use a technology you’re unfamiliar with?!" # @t_sjane391.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_embarrassed as jane
    extend " I try to keep my temper under control, but [slot_playerName], really…" # @t_sjane391.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "How would you feel if I called YOU weird?!" # @t_sjane392.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But Jane…" # @t_sjane393.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " I AM WEIRD!!!" # @t_sjane393.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I’m a little cousin of the Prince of All Cosmos…" # @t_sjane394.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I roll things up into stars and planets…" # @t_sjane394.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And I come from space!" # @t_sjane394.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "See my antenna and my space suit thing?!" # @t_sjane395.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I wouldn’t mind being called weird!" # @t_sjane395.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_smile as jane
    t_ch_jane "Nonsense, [slot_playerName]!" # @t_sjane396.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s futile to try to trick me. I have the sharp eye of a master investigator, you know!" # @t_sjane396.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_grin as jane
    t_ch_jane "It’s obvious that if I were to take that space suit off you, you’d just look like a normal human!" # @t_sjane397.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "…???" # @t_sjane398.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_embarrassed_blush as jane
    t_ch_jane "...Um! Not like that!" # @t_sjane399.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Er, nevermind!" # @t_sjane399.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Just forget I said anything!" # @t_sjane3100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_laugh_blush as jane
    extend " HOO HOO! (Stupid, stupid…)" # @t_sjane3100.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane:
        # ShowWithAtl
        pause 0.333 
        linear 0.20 xpos 0.5 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        pause 0.5 
        linear .25 xpos 0.2 
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.5 xpos 0.85 
    extend "{w=0.75}{nw}"
    t_ch_terezi "H3Y J4N3" # @t_sjane3101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "YOU 4SK3D M3 TO M33T YOU 1N TH3 L1BR4RY?" # @t_sjane3102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "WH4T’S UP" # @t_sjane3103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin as jane
    t_ch_jane "A-HA! Perfect timing, Terezi!" # @t_sjane3104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "See, [slot_playerName]! Now I’ll prove to you how silly all your little delusions are!" # @t_sjane3105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Every single person at this school is just as normal as you or I…" # @t_sjane3106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_laugh as jane
    t_ch_jane "Even my old chum Terezi!" # @t_sjane3107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_huh as terezi
    t_ch_terezi "WHO4H, WH4T…" # @t_sjane3108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_grin as jane:
        # ShowWithAtl
        linear .25 xpos 0.6 
    extend "{w=0.25}{nw}"
    t_ch_jane "YAH!" # @t_sjane3109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(OH MY GOSH! Jane just jumped on top on Terezi!" # @t_sjane3110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I think… I think she’s trying to yank her horns off??)" # @t_sjane3111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_frustrated as jane
    t_ch_jane "Hmm, these are being awfully stubborn…" # @t_sjane3112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Must be some kind of… intensely strong…" # @t_sjane3113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Cosplay… glue?!" # @t_sjane3114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "H-H3Y! G3T OFF!" # @t_sjane3115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1 DON’T L1K3 TO F1GHT MY FR13NDS…" # @t_sjane3116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "BUT YOU L34V3 M3 NO CHO1C3!" # @t_sjane3117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Whoah! That cane Terezi uses…" # @t_sjane3118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It’s also a sword?!" # @t_sjane3119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    extend " That’s gotta be against school rules…)" # @t_sjane3119.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_spoon_frustrated as jane
    t_ch_jane "GAH! Honestly…" # @t_sjane3120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Wow! Jane blocked Terezi’s sword-cane with her giant spoon…" # @t_sjane3121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " Seriously, where does that thing keep coming from?!" # @t_sjane3121.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Now they’re sparring with their weapons…" # @t_sjane3122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It looks like fighting to this is as natural to them as breathing…" # @t_sjane3122.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "This is kind of awesome…" # @t_sjane3123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "But also… SCARY!!!" # @t_sjane3124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    extend " Please, someone come stop this…" # @t_sjane3124.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Please!)" # @t_sjane3125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_screaming as king:
        # ShowWithAtl
        linear 0.70 xpos 1.0 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        pause 0.1 
        linear 0.20 xpos 0.2 
        # ShowWithAtl
        pause 0.1 
        linear .25 xpos 0.15 
    show i_jane_default_smile as jane:
        # ShowWithAtl
        pause 0.1 
        linear 0.20 xpos 0.4 
    show i_terezi_default_huh as terezi:
        # ShowWithAtl
        pause 0.1 
        linear 0.20 xpos 0.6 
    play sound "sfx/kingroar2.ogg"
    stop music fadeout 1.0
    extend "{w=0.7}{nw}"
    t_ch_king "ROOOARRR!" # @t_sjane3126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_meowkie_normal_alert_badge as meowkie:
        # ShowWithAtl
        linear 0.70 xpos 0.85 
    extend "{w=0.7}{nw}"
    t_ch_meowkie "H-he says “You’re all in big trouble!”" # @t_sjane3127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(...Be careful what you wish for.)" # @t_sjane3128.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # Curtain fade
    show i_bg_hallway_b as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_b', 'curtainActor': 'curtain', 'curtainFadeTime': '0.75', 'name': '_2R', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    # UNHANDLED TAG <ActorTransform ActorTransform {'name': '_0', 'target': 'cousin', 'x': '-20%', 'kind': 'ActorTransform'} ''>
    # UNHANDLED TAG <ActorTransform ActorTransform {'name': '_1', 'target': 'jane', 'x': '20%', 'kind': 'ActorTransform'} ''>
    show i_terezi_default_huh as terezi:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_meowkie_normal_alert_badge as meowkie:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_king_screaming as king:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_cousin_default_mortified as cousin
    show i_jane_armscrossed_frustrated as jane
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(So we all got in big trouble." # @t_sjane3129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Terezi’s in there with Principal Dig Dug now, explaining what happened…" # @t_sjane3129.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " King said Jane and I have double detention now." # @t_sjane3129.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Whatever that means..)" # @t_sjane3130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "...Maybe it’s a full-body suit with the hair and horns attached?" # @t_sjane3131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That would explain why pulling on the horns wouldn’t loosen them." # @t_sjane3131.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_smile as jane
    t_ch_jane "It would also explain why the gray bodypaint doesn’t get rubbed off from time to time!" # @t_sjane3132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Seriously?!" # @t_sjane3133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You STILL don’t think anything’s abnormal?!" # @t_sjane3133.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You fought one of your friends with a SWORD today!" # @t_sjane3134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_grin as jane
    t_ch_jane "What’s abnormal about that…?" # @t_sjane3135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Don’t be ridiculous." # @t_sjane3135.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "AUGH! You are the most frustrating person I’ve ever met…" # @t_sjane3136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_embarrassed as jane
    t_ch_jane "…" # @t_sjane3137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "I’m sorry…" # @t_sjane3138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_frustrated as jane
    t_ch_jane "I’m not trying to frustrate anyone. :|" # @t_sjane3139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "I’m just trying to show you what’s what." # @t_sjane3140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "But… I already feel like I know what’s what." # @t_sjane3141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Can’t you trust what I have to say?" # @t_sjane3141.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_smile as jane
    t_ch_jane "...I’m not going to change what I think just because you tell me you see things differently." # @t_sjane3142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(...I guess that’s fair.)" # @t_sjane3143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_frustrated as jane
    t_ch_jane "…" # @t_sjane3144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "In any case…" # @t_sjane3145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "I’m sorry we got in trouble, but…" # @t_sjane3146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane
    t_ch_jane "I’m glad you came with me today." # @t_sjane3147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_embarrassed_blush as jane
    t_ch_jane "I hope, er… Well, that is…" # @t_sjane3148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "This sort of thing is hard for me to say…" # @t_sjane3149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane
    t_ch_jane "I hope you, um… had fun too?" # @t_sjane3150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin as jane
    t_ch_jane "At least a little bit…" # @t_sjane3151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "…" # @t_sjane3152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Are you kidding?" # @t_sjane3153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Of course I did." # @t_sjane3154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "…" # @t_sjane3155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_laugh as jane
    t_ch_jane "You’re a good friend, [slot_playerName]. :B" # @t_sjane3156.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_30', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_jane3__30:
        # <NHSceneChange NHSceneChange {'name': '_30', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4