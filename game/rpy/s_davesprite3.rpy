# <Scene scene {'id': 's_davesprite3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_davesprite3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_davesprite3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_davesprite3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_davesprite3_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        play music "bgm/upbeat.ogg" loop
        show i_bg_classroom_a as bg zorder 0 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_jane_default_smile as jane zorder 3:
            default
            xpos 0.9 
            alpha 0.0
        show i_cousin_default_neutral as cousin zorder 2:
            default
            xpos 0.25 
        show i_davesprite_standing_disinterest as davesprite zorder 2:
            default
            xpos 0.65 
        show i_digdug_left as digdug zorder 3:
            default
            xpos 0.8 
            alpha 0.0
        show i_terezi_default_grin as terezi zorder 3:
            default
            xpos 0.9 
            alpha 0.0

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "cool" # @t_sdavesprite35.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "so you wanna sneak out of detention" # @t_sdavesprite36.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What?! No!!" # @t_sdavesprite37.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "aww how come" # @t_sdavesprite38.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Because I’m already in detention! If I got caught sneaking out..." # @t_sdavesprite39.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " Well, I don’t want to get in WORSE trouble." # @t_sdavesprite39.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "cmon kings not even here" # @t_sdavesprite310.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "itll be easy" # @t_sdavesprite311.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Shh! Let’s not talk about this so loud…" # @t_sdavesprite312.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Why do you even want to sneak out of detention, anyway?!" # @t_sdavesprite312.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "thats whats supposed to happen" # @t_sdavesprite313.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "were in event 2 now [slot_playerName]" # @t_sdavesprite314.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "youre supposed to sneak out and get in trouble" # @t_sdavesprite315.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Oh, more of your “omniscient game guide” stuff." # @t_sdavesprite316.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " This is so stupid! I’m not paying any attention." # @t_sdavesprite316.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I don’t have to do anything I don’t want to do." # @t_sdavesprite317.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " And besides, what kind of “guide” would try to get me in trouble?!" # @t_sdavesprite317.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "its not about whether i want you to get in trouble" # @t_sdavesprite318.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "but thats whats gonna happen in this part of the game no matter what" # @t_sdavesprite319.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Okay, this has officially moved from “quirk” to “personality disorder”." # @t_sdavesprite320.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You’re starting to make me angry." # @t_sdavesprite320.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Can we please drop it?!" # @t_sdavesprite320.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "suit yourself kid" # @t_sdavesprite321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "no matter what you do in this part of the game" # @t_sdavesprite322.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "youre gonna get in trouble and get double detention" # @t_sdavesprite323.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "thats just what has to happen in this part for the rest of the game to make sense" # @t_sdavesprite324.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "so sue me for trying to give you a fluid dating sim experience" # @t_sdavesprite325.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "Just shut up already! I don’t want to hear it!" # @t_sdavesprite326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "im overflowing with rich strategy guide goodness and you don’t even have the decency to indulge a little" # @t_sdavesprite327.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "its like when you dont milk a cow and shes  gotta keep all that milk in there" # @t_sdavesprite328.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "and shes like dude come on" # @t_sdavesprite329.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Gross." # @t_sdavesprite330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "yeah that one got away from me sorry" # @t_sdavesprite331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "What if I just sat here in detention?!" # @t_sdavesprite332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What if I just did my homework here quietly…" # @t_sdavesprite333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And didn’t move from my seat the entire time." # @t_sdavesprite333.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "How could I possibly get in trouble that way!" # @t_sdavesprite334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "i dunno [slot_playerName] but it might be kinda cool to find out" # @t_sdavesprite335.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "because you absolutely will" # @t_sdavesprite336.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "sorry kid" # @t_sdavesprite337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Yeah, well…" # @t_sdavesprite338.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " We’ll just see about that!" # @t_sdavesprite338.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "yeah we will" # @t_sdavesprite339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "okay so youre definitely seriously doing this right" # @t_sdavesprite340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Um…" # @t_sdavesprite341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "youre definitely not moving from your chair from now until detention is over" # @t_sdavesprite342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "no matter what possible situation arises" # @t_sdavesprite343.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "thats just whats happening full stop" # @t_sdavesprite344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "no ifs ands or buts" # @t_sdavesprite345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Uh…" # @t_sdavesprite346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (God, he’s so smug. I can’t give him the satisfaction of knowing I’m unsure!)" # @t_sdavesprite346.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Yes! Definitely!" # @t_sdavesprite347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "promise?" # @t_sdavesprite348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    t_ch_davesprite "pinkie swear?" # @t_sdavesprite349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "YES! ABSOLUTELY!" # @t_sdavesprite350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound ["<silence 1>", "sfx/firealarm.ogg"] loop
    t_ch_davesprite "haha cool" # @t_sdavesprite351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Is that… the fire alarm…." # @t_sdavesprite352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane:
        # FadeEvent
        linear 0.2 alpha 1.0
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear .333 xpos 0.2 
    show i_davesprite_standing_smile as davesprite:
        # ShowWithAtl
        linear .333 xpos 0.5 
    extend "{w=0.333}{nw}"
    t_ch_jane "C’mon everyone! That’s the fire alarm!" # @t_sdavesprite353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Let’s get outside!" # @t_sdavesprite354.00 self.block='Last'
    show i_jane_default_smile as jane:
        # FadeEvent
        linear 0.2 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi:
        # FadeEvent
        linear 0.2 alpha 1.0
    extend "{w=0.2}{nw}"
    t_ch_terezi "1S NOBODY GONN4 H3LP TH3 BL1ND G1RL OUT?" # @t_sdavesprite355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "YOU GUYS SUCK >:P" # @t_sdavesprite356.00 self.block='Last'
    show i_terezi_default_grin as terezi:
        # FadeEvent
        linear 0.2 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear .333 xpos 0.3 
    show i_davesprite_standing_smile as davesprite:
        # ShowWithAtl
        linear .333 xpos 0.7 
    extend "{w=0.333}{nw}"
    t_ch_cousin "Everyone’s… getting up…" # @t_sdavesprite357.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    extend " and leaving the classroom…" # @t_sdavesprite357.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i knew that was gonna happen btw" # @t_sdavesprite358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "If you don’t have anything helpful to say, just shut up!!!" # @t_sdavesprite359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "wow" # @t_sdavesprite360.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i have been nothing if not helpful this entire time" # @t_sdavesprite361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "ungrateful imo" # @t_sdavesprite362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I guess I should get up and file out with everyone…" # @t_sdavesprite363.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The classroom is almost empty now.)" # @t_sdavesprite363.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "oh nice try" # @t_sdavesprite364.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "but you promised you would stay in that seat no matter what" # @t_sdavesprite365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "remember" # @t_sdavesprite366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(H-how did he know what I was thinking?!)" # @t_sdavesprite367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Yeah… but this is a different circumstance…" # @t_sdavesprite368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I mean… it’d be pretty stupid of me to just sit here because of some dumb promise I made…" # @t_sdavesprite368.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "suit yourself" # @t_sdavesprite369.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_smile as davesprite
    t_ch_davesprite "here take my hand" # @t_sdavesprite370.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "you can get to the exit faster if i fly you there" # @t_sdavesprite371.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Ugh! Always trying to be “helpful”..." # @t_sdavesprite372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " He’s so… so SMUG!" # @t_sdavesprite372.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Look at that smug face, and those smug SUNGLASSES…" # @t_sdavesprite373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_angry as cousin
    extend " They should call them… SMUG-GLASSES!" # @t_sdavesprite373.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "Haha… nailed it…" # @t_sdavesprite374.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "A-anyway… I don’t need his help!" # @t_sdavesprite375.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I can make my own choices!)" # @t_sdavesprite375.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    t_ch_davesprite "(still havent figured out that i can read it when you do parentheses-talk eh?)" # @t_sdavesprite376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "You go on ahead." # @t_sdavesprite377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I… I made a promise." # @t_sdavesprite377.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "And I can’t get in trouble for just sitting here not bothering anyone, right?!" # @t_sdavesprite378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "uh" # @t_sdavesprite379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "cool" # @t_sdavesprite380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "okay" # @t_sdavesprite381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "later" # @t_sdavesprite382.00 self.block='Last'
    show i_davesprite_standing_eyebrow as davesprite:
        # FadeEvent
        linear 0.2 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Gosh, that’s loud." # @t_sdavesprite383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "...Wait a minute- what am I, some kind of moron?!" # @t_sdavesprite384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Sitting here by myself during a fire drill, just because I want to show up that dumb Davesprite?!" # @t_sdavesprite384.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Have I lost my mind?!" # @t_sdavesprite385.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Maybe his insanity is contagious…" # @t_sdavesprite385.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I better get up and go join the others-)" # @t_sdavesprite386.00 self.block='Last'
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 0.5 xpos 0.65 
        # FadeEvent
        linear 0.5 alpha 1.0
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "[slot_playerName]!" # @t_sdavesprite387.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " What on earth are you doing in here all by yourself!" # @t_sdavesprite387.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Eek!" # @t_sdavesprite388.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I was just- um-" # @t_sdavesprite388.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Think the rules don’t apply to you, eh?!" # @t_sdavesprite389.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Can you imagine what might have happened to you if this had been a REAL fire?!" # @t_sdavesprite389.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "You don’t wanna know." # @t_sdavesprite390.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "But I- I was going to-" # @t_sdavesprite391.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    extend " But then Davesprite-" # @t_sdavesprite391.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Always blaming others for your problems, eh [slot_playerName]?!" # @t_sdavesprite392.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " SOUNDS FAMILIAR!!" # @t_sdavesprite392.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(What?! When have I ever done that before?!)" # @t_sdavesprite393.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "I won’t tolerate misbehavior, [slot_playerName]!" # @t_sdavesprite394.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite:
        # ShowWithAtl
        linear 0.5 xpos 1.3 
    extend "{w=0.5}{nw}"
    t_ch_digdug "Double detention level 3.5- BLAZING INFERNO!" # @t_sdavesprite395.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    show i_davesprite_standing_disinterest as davesprite:
        # FadeEvent
        linear 0.333 alpha 1.0
        # ShowWithAtl
        linear 1 xpos 0.9 
    extend "{w=1.0}{nw}"
    t_ch_cousin "...Um…" # @t_sdavesprite396.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "sorry [slot_playerName]" # @t_sdavesprite397.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i kinda told you so though" # @t_sdavesprite398.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_angry as cousin
    stop sound
    t_ch_cousin "DAVESPRITE!!!" # @t_sdavesprite399.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_20', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_davesprite3__20:
        # <NHSceneChange NHSceneChange {'name': '_20', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4