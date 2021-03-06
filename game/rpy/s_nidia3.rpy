# <Scene scene {'id': 's_nidia3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_nidia3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_nidia3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_nidia3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/school.ogg" loop
    show i_bg_library as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_nidia_resolute_happy as nidia zorder 3:
        default
        xpos 0.7 
    show i_miller_akimbo_laugh as miller zorder 1:
        default
        xpos 0.85 
        ypos 1.5 
        xzoom -1.0 
    t_ch_nidia "Thanks for coming!" # @t_snidia315.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I really appreciate your help, [slot_playerName]." # @t_snidia315.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It's not a problem but..." # @t_snidia316.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " How am I going to be helping, exactly?" # @t_snidia316.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "We're going to combine!" # @t_snidia317.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    $ renpy.pause(0, hard=True) # Image change
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What-- !" # @t_snidia318.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Wait," # @t_snidia319.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I mean," # @t_snidia320.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I've NEVER combined--" # @t_snidia321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "..................." # @t_snidia322.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(I just... Said too much.)" # @t_snidia323.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I... Need to take a deep breath here. Okay.)" # @t_snidia324.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Nidia... I think this is what Principal Dig Dug was talking about..." # @t_snidia325.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "I don't get it..." # @t_snidia326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You're very direct." # @t_snidia327.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Not everyone is ready to just dive into something like that...especially when they don't know the details." # @t_snidia327.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And furthermore..." # @t_snidia327.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Is it really fair to try to involve someone in your destiny without being completely open with them?" # @t_snidia328.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "There's nothing wrong with being direct, but I think you also need to be up front about the whole truth. Saving the world is a huge--" # @t_snidia329.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_nidia "-- Burden." # @t_snidia330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "... I was going to say responsibility." # @t_snidia331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia ".............." # @t_snidia332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Her destiny really bothers her for some reason... )" # @t_snidia333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Anyway, what I'm trying to say is... If there's someone you have in mind, I can help you talk to them." # @t_snidia334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " I'm no King of All Cosmos, but... Talking can be one of my good points." # @t_snidia334.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_happy as nidia
    t_ch_nidia "Really? You mean that?!" # @t_snidia335.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Of course." # @t_snidia336.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Um... Did you have anyone in mind?" # @t_snidia336.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_happy as nidia
    t_ch_nidia "Tomari helped me put together a method for determining compatibility. He calls it the Tomari Personality Compatibility Matrix!" # @t_snidia337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "Using the matrix, I've narrowed it down to 3 people." # @t_snidia338.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "First... Richard Miller." # @t_snidia339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That guy? He's so... Twitchy..." # @t_snidia340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_happy as nidia
    t_ch_nidia "But he's good-looking! The only thing better than tall, dark and handsome is a man in glasses." # @t_snidia341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She seems really into glasses... )" # @t_snidia342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_happy as nidia
    t_ch_nidia "Second... Hiromi Tengenji." # @t_snidia343.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oooh. She's so... Unapproachable. Do you think you have a chance?" # @t_snidia344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "I have my sources! And that cool, confident exterior... The strong, silent type is definitely attractive!" # @t_snidia345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "What does a person's appearance have to do with combining..." # @t_snidia346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_angry as nidia:
        xzoom -1.0 
    t_ch_nidia "I'VE MADE THE CALCULATIONS" # @t_snidia347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She's very sure of her tastes... )" # @t_snidia348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_happy as nidia
    t_ch_nidia "Lastly... Galaga ship." # @t_snidia349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Well, obviously." # @t_snidia350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_happy_blush as nidia
    t_ch_nidia "I know... My heart fluttered a little bit just thinking about that sleek, Allurium exterior..." # @t_snidia351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(Me too... )" # @t_snidia352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "................." # @t_snidia353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "........................." # @t_snidia354.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "Sure got warm in here........" # @t_snidia355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_surprised_blush as nidia
    t_ch_nidia "Tell me about it... I should have worn my summer armor........." # @t_snidia356.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "OKAY! Let's get focused here. Where does Richard Miller usually hang out?" # @t_snidia357.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_happy as nidia
    t_ch_nidia "He's always where you least suspect him..." # @t_snidia358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "................" # @t_snidia359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "................" # @t_snidia360.00 self.block='Last'
    show i_miller_akimbo_laugh as miller:
        # ShowWithAtl
        easeout .33 ypos 0.5 
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_richard "HELLO!" # @t_snidia361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_surprised as nidia:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.333 xpos 0.25 
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.05 
    extend "{w=0.333}{nw}"
    t_ch_nidiacousins "AAAAAAAAAAAAH!" # @t_snidia362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_serious as miller:
        # ShowWithAtl
        linear 0.75 xpos 0.8 
    extend "{w=0.75}{nw}"
    t_ch_richard "Now... I don't want to sound suspicious..." # @t_snidia363.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_serious as miller:
        # ShowWithAtl
        linear 0.75 xpos 0.75 
    extend "{w=0.75}{nw}"
    extend " But I happened to be in the area..." # @t_snidia363.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And I thought I heard my name." # @t_snidia363.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Being behind a mystic veil in the biology section of the library isn't 'just happening to be in the area' you psycho!!)" # @t_snidia364.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_happy as nidia
    t_ch_nidia "We were just talking about you!" # @t_snidia365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_notebook_serious as miller
    t_ch_richard "You were? I see..." # @t_snidia366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_notepad_happy as nidia
    t_ch_cousin "(He's writing furiously in a notebook... His pencil is a blur.)" # @t_snidia367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Nidia's checking her notes... Maybe these two ARE compatible." # @t_snidia368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " They sure are studious, in their own ways.)" # @t_snidia368.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_nidia "Richard... What do you think of me?" # @t_snidia369.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_serious as miller
    t_ch_richard "Suspicious!" # @t_snidia370.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_surprised_blush as nidia
    t_ch_nidia "!! So quickly?!" # @t_snidia371.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_shocked as miller
    t_ch_richard "Everyone is suspicious until proven unsuspicious!" # @t_snidia372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "Ummm... What do I say to that?" # @t_snidia373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I think he just needs to get to know you... Tell him about yourself." # @t_snidia374.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "Okay... Richard, do you believe in prophecy?" # @t_snidia375.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_notebook_serious as miller
    t_ch_richard "I suspect she's in... a shadowy cult..." # @t_snidia376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_surprised as nidia:
        xzoom -1.0 
    t_ch_nidia "What? No! I'm not in any cult!" # @t_snidia377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_pondering_serious as miller
    t_ch_richard "Is this one of those prank shows, then?" # @t_snidia378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_pondering_shocked as miller
    extend " Where are the hidden cameras?!" # @t_snidia378.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_pondering_contemplative as miller
    show i_nidia_clasped_worried as nidia:
        xzoom 1.0 
    t_ch_nidia "There are no hidden cameras!" # @t_snidia379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "Just the magic, all-seeing eye of my amulet. Which I can use to combine with another person... to become a dragon! I want your help!" # @t_snidia380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_notebook_serious as miller
    t_ch_richard "DEFINITELY shadowy cult..." # @t_snidia381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_aliens_serious as miller
    t_ch_richard "Where's the rest of your cult?" # @t_snidia382.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_aliens_shocked as miller
    extend " I know they're here!" # @t_snidia382.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Waiting!" # @t_snidia382.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_aliens_serious as miller
    extend " Waiting..................." # @t_snidia382.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_worried as nidia
    t_ch_nidia "There's no cult.........." # @t_snidia383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_akimbo_shocked as miller:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 1.25 
    extend "{w=0.5}{nw}"
    t_ch_richard "That's just what someone in a cult would say!!" # @t_snidia384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    hide miller
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    show i_nidia_akimbo_worried as nidia:
        # ShowWithAtl
        linear 0.333 xpos 0.7 
    extend "{w=0.333}{nw}"
    t_ch_cousin "He ran away." # @t_snidia385.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "There he goes." # @t_snidia386.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "Do you see what I mean? Nobody likes me..." # @t_snidia387.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I wouldn't base your view of humanity on him if I were you..." # @t_snidia388.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "...................." # @t_snidia389.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She looks so bummed out...)" # @t_snidia390.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Um....." # @t_snidia391.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_grin as cousin
    extend " Let's go find Hiromi!" # @t_snidia391.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_happy as nidia
    stop music fadeout 1.0
    t_ch_nidia "Y-yeah! Let's go!" # @t_snidia392.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5) # Curtain fade
    show i_bg_shopclass as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_shopclass', 'curtainActor': 'curtain', 'curtainFadeTime': '0.5', 'name': '_1V', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_prop_hiromi_bike as bike zorder 1:
        default
        xpos 0.16 
        ypos 0.74 
        xzoom -1.0 
    show i_hiromi_crossed_serious as hiromi zorder 2:
        default
        xpos -0.5 
        alpha 1.0
    show i_cousin_default_neutral as cousin:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.9 
    show i_nidia_akimbo_happy as nidia:
        # ShowWithAtl
        linear 0.5 xpos 0.65 
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.5 alpha 0.0
    $ renpy.pause(0.5) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_nidia "This is her motorcyle..." # @t_snidia393.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Whoa... It's really cool." # @t_snidia394.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    extend "{w=0.5}{nw}"
    t_ch_hiromi "..............." # @t_snidia395.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_surprised as nidia:
        xzoom -1.0 
    show i_cousin_default_surprised as cousin
    t_ch_nidia "OH! Hi Hiromi!" # @t_snidia396.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " We were just talking about your bike!" # @t_snidia396.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "........................" # @t_snidia397.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_surprised as nidia:
        xzoom 1.0 
    show i_cousin_default_neutral as cousin
    t_ch_nidia "Ummmm...." # @t_snidia398.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi ".................................." # @t_snidia399.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She's definitely the strong silent type... )" # @t_snidia3100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi ".................. What's up." # @t_snidia3101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "OH! You talked." # @t_snidia3102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "....................." # @t_snidia3103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_surprised as nidia
    t_ch_nidia "Um... I was just wondering..." # @t_snidia3104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Ask her if she's free later! Keep it casual." # @t_snidia3105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_happy as nidia
    t_ch_nidia "Are you free later?" # @t_snidia3106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_stand_serious as hiromi
    t_ch_hiromi "................ I'm busy." # @t_snidia3107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And spoken for." # @t_snidia3107.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_surprised as nidia:
        xzoom -1.0 
    t_ch_nidia "Spoken for?" # @t_snidia3108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_smile as hiromi
    t_ch_hiromi "You're cute." # @t_snidia3109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_serious as hiromi
    t_ch_hiromi "But just because I like fast motorcycles..." # @t_snidia3110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Doesn't mean I like fast relationships." # @t_snidia3110.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(A shockingly decisive statement!)" # @t_snidia3111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_worried_blush as nidia:
        xzoom 1.0 
    t_ch_nidia "Relationship? Oh no! I think we're having two different conversations here." # @t_snidia3112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Oh. Are we?" # @t_snidia3113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_surprised_blush as nidia
    extend " I'm definitely not interested, then." # @t_snidia3113.01 self.block='Last'
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear 0.5 xpos -0.5 
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    show i_nidia_akimbo_surprised_blush as nidia:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    hide hiromi
    extend "{w=0.5}{nw}"
    t_ch_cousin "............. Wow." # @t_snidia3114.00 self.block='Last'
    show i_nidia_akimbo_surprised_blush as nidia:
        xzoom -1.0 
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " What an unusual person..." # @t_snidia3114.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Nidia?" # @t_snidia3114.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia ".............." # @t_snidia3115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "......................" # @t_snidia3116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia:
        xzoom 1.0 
    t_ch_nidia ".................. No one wants to combine with me......" # @t_snidia3117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " They won't even listen..............." # @t_snidia3117.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Nidia..." # @t_snidia3118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "..............." # @t_snidia3119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Don't give up! I'm sure the next time will go better." # @t_snidia3120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    extend " Who's next?" # @t_snidia3120.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "S-sniff... G-galaga......" # @t_snidia3121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(WE'VE DEFINITELY SET OUR SIGHTS TOO HIGH)" # @t_snidia3122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "Come on... Let's get this over with..." # @t_snidia3123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Nidia..." # @t_snidia3124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " She's really hurting..." # @t_snidia3124.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    stop music fadeout 1.0
    extend " I think there's more going on here than I thought..." # @t_snidia3124.02 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5) # Curtain fade
    show i_bg_stage_cardboard as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_stage_cardboard', 'curtainActor': 'curtain', 'curtainFadeTime': '0.5', 'name': '_2E', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_galaga_default as galaga zorder 2:
        default
        xpos 0.8 
    hide bike
    show i_nidia_akimbo_worried as nidia:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.35 
    show i_cousin_default_neutral as cousin:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.1 
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.5 alpha 0.0
    $ renpy.pause(0.5) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_cousin "(Maybe this isn't such a good idea... )" # @t_snidia3125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "GALAGA!" # @t_snidia3126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}WHAT DO YOU WANT MORTAL{/smallcaps}" # @t_snidia3127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "COMBINE WITH ME!" # @t_snidia3128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}EVERYONE WANTS A PIECE OF GALAGA... BECAUSE GALAGA IS MADE OF ALLURIUM, THE RAREST, MOST PASSIONATE METAL IN THE UNIVERSE.{/smallcaps}" # @t_snidia3129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}BUT GALAGA IS NOT JUST SOME TROPHY, TO BE PRIZED LIKE AN OBJECT.{/smallcaps}" # @t_snidia3130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}GALAGA HAS SEEN THINGS ON THE GALACTIC FRONTIER... DONE THINGS THAT YOU CANNOT IMAGINE.{/smallcaps}" # @t_snidia3131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}YOU THINK GALAGA IS A THING, TO BE OWNED...{/smallcaps}" # @t_snidia3132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}BUT YOU CANNOT OWN GALAGA'S EXPERIENCES.{/smallcaps}" # @t_snidia3133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}GALAGA HAS FEELINGS TOO! GALAGA... HAS FEELINGS... TOO.{/smallcaps}" # @t_snidia3134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_worried as nidia:
        xzoom 1.0 
    t_ch_nidia "Well... I..." # @t_snidia3135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "T-tell Galaga what you're thinking!" # @t_snidia3136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_akimbo_worried as nidia:
        xzoom -1.0 
    t_ch_nidia "I can't do this." # @t_snidia3137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " This is so stupid." # @t_snidia3137.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "I'm exhausted." # @t_snidia3138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I just want to be alone for a while." # @t_snidia3138.01 self.block='Last'
    show i_nidia_akimbo_worried as nidia:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos -0.5 
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Nidia... Wait!" # @t_snidia3139.00 self.block='Last'
    show i_cousin_default_surprised as cousin:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos -0.5 
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_galaga_default as galaga:
        # ShowWithAtl
        linear 1 xpos 0.5 
    extend "{w=1.0}{nw}"
    t_ch_galaga "{smallcaps}ONCE AGAIN... GALAGA BECOMES EMBROILED IN YOUR...{/smallcaps}" # @t_snidia3140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {smallcaps}EARTH DRAMA{/smallcaps}" # @t_snidia3140.01 self.block='Last'
    show i_galaga_default as galaga:
        # ShowWithAtl
        easein 1 ypos -0.5 
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5) # Curtain fade
    show i_bg_hallway_a as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_a', 'curtainActor': 'curtain', 'curtainFadeTime': '0.5', 'name': '_2d', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug zorder 4:
        default
        xpos 0.7 
        alpha 0.0
    hide galaga
    show i_nidia_akimbo_worried as nidia:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    show i_cousin_energetic_neutral as cousin:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.5 alpha 0.0
    $ renpy.pause(0.5) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Nidia, wait!" # @t_snidia3141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I'm sorry!" # @t_snidia3141.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia
    t_ch_nidia "Sorry? What're YOU sorry for?" # @t_snidia3142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I just... I wanted to help, but I was no help at all." # @t_snidia3143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I--" # @t_snidia3144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_surprised as nidia:
        xzoom 1.0 
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.15 
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_digdug "STUDENTS! IN THE HALL?!" # @t_snidia3145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "You two! YOU... DELINQUENTS!" # @t_snidia3146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_worried as nidia:
        xzoom -1.0 
    t_ch_nidia "Yeah... I'm a delinquent!" # @t_snidia3147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I'm not good at anything!" # @t_snidia3147.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Except being alone!" # @t_snidia3147.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "I'm a no good," # @t_snidia3148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Irresponsible," # @t_snidia3148.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Duty-shirking," # @t_snidia3148.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Dumb" # @t_snidia3148.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Selfish" # @t_snidia3148.04 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Um...." # @t_snidia3149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "Useless" # @t_snidia3150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Dumb" # @t_snidia3150.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_clasped_angry as nidia
    extend " IDIOT!!" # @t_snidia3150.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "I'm putting myself in SEPTUPLE SPIRIT DUNGEON DETENTION!" # @t_snidia3151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Whoa... that's a little excessive......." # @t_snidia3152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Y-yeah........." # @t_snidia3153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_30', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_nidia_resolute_angry as nidia
    t_ch_nidia "If I have to spend forever in detention, then I don't have to worry about some stupid prophecy!!!!!" # @t_snidia3154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_31', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_nidia "BY THE COILS OF JÃRMUNGANDR... I should have put more points into charisma!!" # @t_snidia3155.00 self.block='Last'
    show i_nidia_resolute_angry as nidia:
        # ShowWithAtl
        linear 0.5 xpos -0.5 
    # <ParallelEvent ParallelEvent {'name': '_33', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_sad as cousin
    t_ch_cousin "Nidia!" # @t_snidia3156.00 self.block='Last'
    show i_cousin_energetic_sad as cousin:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos -0.5 
    # <ParallelEvent ParallelEvent {'name': '_36', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear 1 xpos 0.5 
    extend "{w=1.0}{nw}"
    t_ch_digdug "...sheesh." # @t_snidia3157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_37', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " YOUTHS." # @t_snidia3157.01 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_38', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_nidia3__38:
        # <NHSceneChange NHSceneChange {'name': '_38', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4