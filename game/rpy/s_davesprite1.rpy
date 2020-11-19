# <Scene scene {'id': 's_davesprite1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_davesprite1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_davesprite1"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_davesprite1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_davesprite1_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        play music "bgm/upbeat_half.ogg" loop
        show i_bg_classroom_b as bg zorder 0 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_sw_black as darkness zorder 1:
            default
            alpha 0.5
        show i_cousin_default_neutral as cousin zorder 2:
            default
            xpos 0.3 
        show i_davesprite_standing_disinterest as davesprite zorder 2:
            default
            xpos 0.7 
        show i_event_davesprite_scene1 as event zorder 9:
            default
            alpha 0.0

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "so yeah lets get this romance started i guess" # @t_sdavesprite132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...I know you’re just doing your whole weird “this is all a game” stuff, but…" # @t_sdavesprite133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Man, that’s kinda rude to just come out and say!" # @t_sdavesprite134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I just wanted to join a cool club." # @t_sdavesprite135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "yeah youre right" # @t_sdavesprite136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "just cuz youre playing a game doesnt mean i should be all creepy or whatever" # @t_sdavesprite137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "but here let me give you a hint" # @t_sdavesprite138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "when i say the phrase “so is that what you really think of me” later" # @t_sdavesprite139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "say “i think i love you davesprite” to trigger the right thing so you can do the next event with me" # @t_sdavesprite141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i know it sounds weird but im just doing you a favor" # @t_sdavesprite142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "You want me to say that when you ask “So is that what you really think of me”, huh?" # @t_sdavesprite143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "well i mean whatever you wanna do" # @t_sdavesprite144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "its just the best option straight-up" # @t_sdavesprite145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Uh huh, okay. I’ll remember." # @t_sdavesprite146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "So, like… let’s say I’m playing along, and I buy this whole “game” thing." # @t_sdavesprite147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Are you experiencing this like you’re actually playing a game?" # @t_sdavesprite147.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    extend " Pressing buttons and stuff?" # @t_sdavesprite147.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "nah i experience stuff the same way you do" # @t_sdavesprite148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "grass and trees around" # @t_sdavesprite149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "all that good stuff" # @t_sdavesprite150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "pretty much the same way i experienced stuff in the uh" # @t_sdavesprite151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "the other game i was a part of" # @t_sdavesprite152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That’s another thing I wanted to ask you about." # @t_sdavesprite153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " If you were in another game before, when did you come here?" # @t_sdavesprite153.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Do you remember that?" # @t_sdavesprite154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Did you come to, uh, “this game” on purpose?" # @t_sdavesprite154.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "look [slot_playerName] that stuff is basically pointless to worry about" # @t_sdavesprite155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "its kinda best not to examine this situation too closely" # @t_sdavesprite156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "well get into a whole worlds within worlds psychological warp deal" # @t_sdavesprite157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "im not too interested in going that direction with this" # @t_sdavesprite158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "For someone who’s supposed to have “omniscient game knowledge”..." # @t_sdavesprite159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " You sure like being obtuse when I actually ask you questions!" # @t_sdavesprite159.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "yeah youre really peeling away the layers here" # @t_sdavesprite160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "falling in love with me yet" # @t_sdavesprite161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha, shut up." # @t_sdavesprite162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Okay, so what do we do in “Webcomics club” anyway?" # @t_sdavesprite163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "haha i didnt really think that far ahead" # @t_sdavesprite164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "i guess we could make some comics or something" # @t_sdavesprite165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "is that a dumb idea?" # @t_sdavesprite166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i dont really know what to do here" # @t_sdavesprite167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "im basically just waiting for this event to end so we can move on" # @t_sdavesprite168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Um! Well, it doesn’t sound dumb exactly…" # @t_sdavesprite169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s just that I’ve never really drawn much before." # @t_sdavesprite169.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    extend " But if that’s what Webcomics Club is all about, then sure!" # @t_sdavesprite169.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "thats the spirit" # @t_sdavesprite170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "webcomics arent really about drawing well anyway" # @t_sdavesprite171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "you should see some of the garbage out there" # @t_sdavesprite172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "put two characters in a panel and make it look like they might kiss and people will trip over themselves to throw money at you" # @t_sdavesprite173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "its a pretty sweet gig" # @t_sdavesprite174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "lets see what should i make a comic about" # @t_sdavesprite175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "some kind of video game thing probably" # @t_sdavesprite176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "okay here we go done" # @t_sdavesprite177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "That was fast…." # @t_sdavesprite178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "okay ill wait for you to finish yours" # @t_sdavesprite179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(Jeez, I have no idea what to do here…" # @t_sdavesprite180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " … Um… Wow… This is harder than I thought it would be." # @t_sdavesprite180.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well, this idea is kinda dumb, but it’ll have to do.)" # @t_sdavesprite181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Okay, I’m done." # @t_sdavesprite182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "cool" # @t_sdavesprite183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    stop music fadeout 1.0
    t_ch_davesprite "okay check it" # @t_sdavesprite184.00 self.block='Last'
    show i_event_davesprite_scene1 as event:
        # FadeEvent
        linear 0.2 alpha 1.0
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Huh… there’s something familiar about that comic…" # @t_sdavesprite185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "careful" # @t_sdavesprite186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "dont you start getting meta now" # @t_sdavesprite187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "thats my thing" # @t_sdavesprite188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Huh??!" # @t_sdavesprite189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " No, I mean…" # @t_sdavesprite189.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Well, it’s probably better to just show you…" # @t_sdavesprite190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Boy, this is pretty weird." # @t_sdavesprite190.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "what" # @t_sdavesprite191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "whats going on" # @t_sdavesprite192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "if youre trying to mess with me" # @t_sdavesprite193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "well dont" # @t_sdavesprite194.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "youre freaking me out" # @t_sdavesprite195.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Here! This is the comic I made!" # @t_sdavesprite196.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "whoah" # @t_sdavesprite197.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I know, right?!" # @t_sdavesprite198.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Isn’t it weird that we thought of the same thing?!" # @t_sdavesprite198.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "it would be pretty weird" # @t_sdavesprite199.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "except for the fact" # @t_sdavesprite1100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "that we are obviously soulmates" # @t_sdavesprite1101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "WHAT?! Really?!" # @t_sdavesprite1102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You think we’re soulmates?!" # @t_sdavesprite1103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "yeah" # @t_sdavesprite1104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "completely" # @t_sdavesprite1105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "the prophets foretold of our meeting" # @t_sdavesprite1106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "and said it was gonna be hella kawaii" # @t_sdavesprite1107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "I, uh… Um, that is..." # @t_sdavesprite1108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "relax [slot_playerName] im just messin with you" # @t_sdavesprite1109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "we just both have scarily impeccable taste in webcomics is all" # @t_sdavesprite1110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Oh… haha. Yeah." # @t_sdavesprite1111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " I knew you were just kidding." # @t_sdavesprite1111.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I can’t believe I’m actually a little disappointed.)" # @t_sdavesprite1112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "(haha yeah i bet you are)" # @t_sdavesprite1113.00 self.block='Last'
    show i_event_davesprite_scene1 as event:
        # FadeEvent
        linear 0.2 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "So uh… your comic is pretty, um…" # @t_sdavesprite1114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Interesting." # @t_sdavesprite1115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Is that something you do as a hobby, or what…?" # @t_sdavesprite1116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    t_ch_davesprite "uh i dont really know" # @t_sdavesprite1117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i guess its something the original dave liked to do" # @t_sdavesprite1118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "the guy i was copied from i mean" # @t_sdavesprite1119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "im basically a second version of that guy" # @t_sdavesprite1120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "so its hard to know whats actually unique about me" # @t_sdavesprite1121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "its kind of a drag but whatever" # @t_sdavesprite1122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i guess sometimes i do bird stuff" # @t_sdavesprite1123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "because im part bird or something?" # @t_sdavesprite1124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "its hard to explain i guess but sometimes i get urges" # @t_sdavesprite1125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "like some bird seed would seriously hit the spot right now" # @t_sdavesprite1126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Maybe you could ask Blue Max if he has any…?" # @t_sdavesprite1127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "yeah i thought about it but like" # @t_sdavesprite1128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i figure hes the bird guy right" # @t_sdavesprite1129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "he probably has people asking where they can get some fresh hot birdseed all the time" # @t_sdavesprite1130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "like every day" # @t_sdavesprite1131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "hes probably sick of it" # @t_sdavesprite1132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "so ill try to be cool and not ask" # @t_sdavesprite1133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Somehow I doubt that  too many people are asking about birdseed here." # @t_sdavesprite1134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_davesprite "i wish i had better stuff to tell you [slot_playerName]" # @t_sdavesprite1135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "but i guess the reason i try to talk about game stuff all the time" # @t_sdavesprite1136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_disinterest as davesprite
    t_ch_davesprite "is cuz its kinda the only thing i have to talk about" # @t_sdavesprite1137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "im hardly even a real person" # @t_sdavesprite1138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i was created to help the original dave through his game" # @t_sdavesprite1139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "and now that im not in that game anymore i dunno how useful my existence is anymore" # @t_sdavesprite1140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "thats pretty much all i think about actually because the more i turn it over in my brain the more it seems like theres really no answer to that question" # @t_sdavesprite1141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_davesprite "im straight up totally pointless" # @t_sdavesprite1142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "i dont even know why youre hanging out with me because it must be pretty boring to hear a guy just go on and on about a bunch of what seems like nonsense" # @t_sdavesprite1143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "sorry" # @t_sdavesprite1144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i dont even know what im saying really" # @t_sdavesprite1145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well, even though I don’t really know what you’re talking about half the time…" # @t_sdavesprite1146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " I’m having fun hanging out with you." # @t_sdavesprite1146.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I don’t really care if you’re the “original” or whatever." # @t_sdavesprite1147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "yeah but its gotta be a downer to hear about right" # @t_sdavesprite1148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i mean the only thing i really have to offer is a quick path to the best ending" # @t_sdavesprite1149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "you dont wanna hear all my dumb angsty drama" # @t_sdavesprite1150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Actually, I’m really glad I asked you about your “drama”!" # @t_sdavesprite1151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s the only way I could get you to shut up about the game stuff." # @t_sdavesprite1151.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "It even kinda makes me wonder if you keep pretending to be a game guide who knows everything..." # @t_sdavesprite1152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " So you don’t have to talk about your real issues." # @t_sdavesprite1152.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_defeated_eyebrow as davesprite
    t_ch_davesprite "wow really cutting to the heart of it arent you" # @t_sdavesprite1153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "did you come to that conclusion in armchair psychology 101" # @t_sdavesprite1154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I just like talking to you, Davesprite." # @t_sdavesprite1155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " You’re… kinda inscrutable, but pretty cool." # @t_sdavesprite1155.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "so" # @t_sdavesprite1156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "is that what you really think of me?" # @t_sdavesprite1157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "… ... \"I love you, Davesprite.\"" # @t_sdavesprite1158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_eyebrow as davesprite
    show i_cousin_default_grin as cousin
    t_ch_davesprite "man its pretty depressing to hear you just say it like that" # @t_sdavesprite1159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "not meaning it just" # @t_sdavesprite1160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "rotely going through the motions because i told you to" # @t_sdavesprite1161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "i feel like a huge jerk now actually" # @t_sdavesprite1162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "no its more than that" # @t_sdavesprite1163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "whats this" # @t_sdavesprite1164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "emotions coursing through my digital body" # @t_sdavesprite1165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_sad as davesprite
    t_ch_davesprite "im just a game sprite…" # @t_sdavesprite1166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "i was never meant to feel…" # @t_sdavesprite1167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "this……" # @t_sdavesprite1168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_glitched as davesprite:
        # ShowWithAtl
        pause 0.15 
        linear 0.5 alpha 0.0
        # ShowWithAtl
        pause 0.225 
        linear 0.5 alpha 1.0
        # ShowWithAtl
        pause 0.55 
        linear 0.5 alpha 0.0
        # ShowWithAtl
        pause 0.65 
        linear 0.5 xpos 0.65 
        # ShowWithAtl
        pause 0.675 
        linear 0.5 alpha 1.0
    $ renpy.pause(4.75, hard=True) # Image change
    show i_davesprite_shrug_grin as davesprite:
        # ShowWithAtl
        pause 0.85 
        linear 0.5 xpos 0.7 
    $ renpy.pause(1.35, hard=True) # Image change
    show i_davesprite_shrug_disinterest as davesprite
    $ renpy.pause(0, hard=True) # Image change
    show i_davesprite_glitched as davesprite:
        # ShowWithAtl
        pause 1.45 
        linear 0.5 xpos 0.75 
        # ShowWithAtl
        pause 1.55 
        linear 0.5 alpha 0.0
        # ShowWithAtl
        pause 1.675 
        linear 0.5 alpha 1.0
        pause 1.75
        xzoom -1.0 
        # ShowWithAtl
        pause 1.75 
        linear 0.5 xpos 0.6 
    $ renpy.pause(10.175, hard=True) # Image change
    show i_davesprite_standing_disinterest as davesprite:
        pause 1.85
        xzoom 1.0 
    $ renpy.pause(1.85, hard=True) # Image change
    show i_davesprite_defeated_disinterest as davesprite
    $ renpy.pause(0, hard=True) # Image change
    show i_davesprite_glitched as davesprite:
        # ShowWithAtl
        pause 2.15 
        linear 0.5 xpos 0.65 
        # ShowWithAtl
        pause 2.25 
        linear 0.5 xpos 0.7 
    $ renpy.pause(2.75, hard=True) # Text delay
    t_ch_davesprite "{cps=*0.21}emotions OVERLOADING MY PROGRAMMING{/cps}" # @t_sdavesprite1169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "{cps=*0.21}Davesprite!{/cps}" # @t_sdavesprite1170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {cps=*0.21}Are you okay?!{/cps}" # @t_sdavesprite1170.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    t_ch_davesprite "{cps=*0.21}haha just messin with you that stuffs fake{/cps}" # @t_sdavesprite1171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "{cps=*0.21}…{/cps}" # @t_sdavesprite1172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    show i_cousin_default_neutral as cousin
    t_ch_davesprite "{cps=*0.21}okay i think thats enough{/cps}" # @t_sdavesprite1180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "{cps=*0.21}we may have just been passing time in the event but at least it was kinda fun{/cps}" # @t_sdavesprite1181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "{cps=*0.21}so thanks i guess{/cps}" # @t_sdavesprite1182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "{cps=*0.21}Thank you, Davesprite. I had fun too.{/cps}" # @t_sdavesprite1183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "{cps=*0.21}Although, I wonder…{/cps}" # @t_sdavesprite1184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " {cps=*0.21}If you’re just a game guide, can you, uh…{/cps}" # @t_sdavesprite1184.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "{cps=*0.21}Can you actually like me, or do you just think I’m some kind of..{/cps}" # @t_sdavesprite1185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " {cps=*0.21}Fictional … video game thing?{/cps}" # @t_sdavesprite1185.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_shrug_eyebrow as davesprite
    t_ch_davesprite "{cps=*0.21}look dont worry about it{/cps}" # @t_sdavesprite1186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "{cps=*0.21}thinking too much about the logistics of this will just mess you up{/cps}" # @t_sdavesprite1187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_disinterest as davesprite
    t_ch_davesprite "{cps=*0.21}ill see you next time{/cps}" # @t_sdavesprite1188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "{cps=*0.21}unless you pick another character to chill with{/cps}" # @t_sdavesprite1189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "{cps=*0.21}which is totally cool btw{/cps}" # @t_sdavesprite1190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "{cps=*0.21}(Darn, I was actually hoping for a real answer on that one.){/cps}" # @t_sdavesprite1191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "{cps=*0.21}(i know you were buddy){/cps}" # @t_sdavesprite1192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*0.21}...Davesprite, you’re just staring at me blankly again.{/cps}" # @t_sdavesprite1193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_davesprite "{cps=*0.21}sorry about that{/cps}" # @t_sdavesprite1194.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_davesprite_standing_smile as davesprite
    t_ch_davesprite "{cps=*0.21}see you later [slot_playerName]{/cps}" # @t_sdavesprite1195.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_2s', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
    label s_davesprite1__2s:
        # <NHSceneChange NHSceneChange {'name': '_2s', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
        jump s_day2