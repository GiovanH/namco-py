# <Scene scene {'id': 's_hiromi3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_hiromi3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_hiromi3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_hiromi3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_hiromi3_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        play music "bgm/upbeat_half.ogg" loop
        show i_bg_shopclass as bg zorder 0 at default
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_sw_black as darkness zorder 9:
            default
            alpha 0.0
        show i_prop_hiromi_bike as bike zorder 1:
            default
            xpos 0.2 
            ypos 0.85 
            xzoom -1.0 
        show i_cousin_default_grin as cousin zorder 2:
            default
            xpos 0.3 
        show i_hiromi_crossed_serious as hiromi zorder 2:
            default
            xpos 0.7 
        show i_digdug_left as digdug zorder 2:
            default
            xpos 0.3 
            alpha 0.0

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Hey Hiromi." # @t_shiromi37.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Hey kid." # @t_shiromi38.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(She concentrating really hard on her bike's display... Oh, she pushed a button.)" # @t_shiromi39.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She doesn't seem like she wants to talk just now... I better not distract her.)" # @t_shiromi310.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Her expression when she concentrates is really intense. In fact, it's a little scary.)" # @t_shiromi311.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "...................." # @t_shiromi312.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Even the force of her silence is impressive. It's like there's a whole other language there.)" # @t_shiromi313.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Like... A language of stoicism.)" # @t_shiromi314.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_akimbo_serious as hiromi
    t_ch_hiromi "C'mon." # @t_shiromi315.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(She threw me a helmet!)" # @t_shiromi316.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Huh?" # @t_shiromi317.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_serious as hiromi
    t_ch_hiromi "We're gonna ride." # @t_shiromi318.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Um... Won't you get in trouble?" # @t_shiromi319.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_akimbo_serious as hiromi
    t_ch_hiromi "If we get caught, I'll just say I kidnapped you." # @t_shiromi320.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(THAT'S A LITTLE EXTREME)" # @t_shiromi321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "N-no, that's okay. Still..." # @t_shiromi322.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    show i_hiromi_crossed_serious as hiromi
    t_ch_hiromi "You can stay if you like." # @t_shiromi323.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "No..." # @t_shiromi324.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " I'll go." # @t_shiromi324.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # FadeEvent

    show i_hiromi_crossed_serious as hiromi:
        # FadeEvent

    show i_prop_hiromi_bike as bike:
        # FadeEvent

    show i_bg_dayride as bg
    with Dissolve(1)
    show i_sw_black as darkness:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    stop music fadeout 1.0
    extend "{w=0.5}{nw}"
    # Blank text event <TextEvent TextEvent {'char': '', 'text': '', 'kind': 'TextEvent'} ''>
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(We get onto the bike. The seat is surprisingly plush, but there's clearly a divet where Hiromi usually sits. She definitely rides this thing a lot.)" # @t_shiromi325.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Despite the initial roar of the engine... The actual hum of the bike after it settles is surprisingly even.)" # @t_shiromi326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This must be what they call good tuning.)" # @t_shiromi327.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(When the bike first moves, it's a surprise... Hiromi's hands at the controls are swift and precise and sure and the machine reflects that perfectly.)" # @t_shiromi328.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Sitting where I am, I can see the small display in front of her. There's a wave... She pushes a button, and another wave appears, running alongside the first for a moment... )" # @t_shiromi329.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(... Then it suddenly inverts and flattens out. The sound of the bike vanishes almost completely. I can't believe it.)" # @t_shiromi330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(We emerge from the garage with nothing more than the sound of gravel underneath us.)" # @t_shiromi331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(We glide down a back alley, avoiding line of sight with the school.)" # @t_shiromi332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Hiromi skillfully guides the bike up the narrow path until it merges with the highway.)" # @t_shiromi333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_event_hiromi_scene3 as ev:
        default
        xpos 0.5 
        ypos 0.6 
    $ AudioEvent('music', 1.0, 1.0)
    show i_sw_black as curtain:
        # FadeEvent
        linear 1.0 alpha 0.0
    extend "{w=1.0}{nw}"
    t_ch_cousin "(She pushes that mysterious button again, and suddenly the sound of the engine is all there, growing to a roar as she opens up the throttle.)" # @t_shiromi334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as darkness:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "(I hold on for my dear, tiny life. Out here, on the road, moving so fast..." # @t_shiromi335.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I suddenly feel smaller than usual.)" # @t_shiromi335.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I didn't realize my heart was beating so fast! It's scary, but it's also... Exhilarating.)" # @t_shiromi336.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Once you get used to the sound of the bike, it's almost... Peaceful.)" # @t_shiromi337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I try to get a look at Hiromi..." # @t_shiromi338.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And for the briefest moment, I glimpse her smiling from ear to ear.)" # @t_shiromi338.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It's truthfully not an expression I ever thought I'd see on her face.)" # @t_shiromi339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This is her favorite place to be... And rather than try to explain it, she wanted me to experience it with her.)" # @t_shiromi340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Wow..." # @t_shiromi341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I thought you might understand." # @t_shiromi342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "AHHH! How can you hear me?!" # @t_shiromi343.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Oh, sorry... Dr. Tomari made it so we can communicate through these helmets." # @t_shiromi344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh... I'm glad I didn't say anything embarrassing." # @t_shiromi345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I was kind of hoping." # @t_shiromi346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Did she just... Make a joke?)" # @t_shiromi347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It seems when she opens up the throttle..." # @t_shiromi348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " She opens up her heart.)" # @t_shiromi348.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Hiromi... Why'd you bring me out here?" # @t_shiromi349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Not that I mind..." # @t_shiromi349.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I'm not... Much for words." # @t_shiromi350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Sometimes it's easier to show a person." # @t_shiromi350.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I got held back a year at Namco High... 'You don't apply yourself', they said." # @t_shiromi351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I feel trapped at school. I just want to graduate so I can leave, but Namco High keeps pulling me back." # @t_shiromi352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Meanwhile..." # @t_shiromi353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "The road is always here... Going on forever." # @t_shiromi354.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I want to take it out of Namco City. See the world." # @t_shiromi355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Eat new foods." # @t_shiromi356.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Meet new people." # @t_shiromi357.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Experience new cultures." # @t_shiromi358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Ride new bikes." # @t_shiromi359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Drive new roads." # @t_shiromi360.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "The world is too big..." # @t_shiromi361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And I want to make it smaller." # @t_shiromi361.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "In order to achieve this... I'm going to become the best biker in the world." # @t_shiromi362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Wow... I had no idea." # @t_shiromi363.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "My partner, Kissy, said she'd come with me...She's really sweet and supportive." # @t_shiromi364.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "But Kissy's a planner. She wants to make sure we can survive out there on our own." # @t_shiromi365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh... That makes sense. But what do you think... ?" # @t_shiromi366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I have a habit of just going for it..." # @t_shiromi367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "That's how she and I became friends. Friendly. Um." # @t_shiromi368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "She said she'd been planning to say something for months, but 'it never felt like the right time'." # @t_shiromi369.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "You want to know the secret, kid?" # @t_shiromi370.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...?" # @t_shiromi371.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "The secret is..." # @t_shiromi372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It's always the right time." # @t_shiromi372.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I can't see her face just now... But I can tell she's blushing.)" # @t_shiromi373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Anyway... She says that if I win the next race, we can use the reward money to get our journey started." # @t_shiromi374.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Oh... That's a little sad. We just met... And she's nice, in her own way, once you get to know her.)" # @t_shiromi375.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(But... She's not the type to lay down roots. Nothing can hold her back from the open road... And I just want her to be happy, I think.)" # @t_shiromi376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain2 zorder 9:
        default
        alpha 0.0
        linear 1 alpha 1.0
    extend "{w=1.0}{nw}"
    t_ch_hiromi "This is our exit." # @t_shiromi377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    hide ev
    stop music fadeout 1.0
    t_ch_cousin "(I felt strange as we pulled back into the parking lot at Namco High..." # @t_shiromi378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # FadeEvent

        # ShowWithAtl
        linear 0.5 xpos 0.22 
    show i_hiromi_stand_serious as hiromi:
        # FadeEvent

        # ShowWithAtl
        linear 0.5 xpos 0.8 
    show i_prop_hiromi_bike as bike:
        # FadeEvent

        # ShowWithAtl
        linear 0.5 xzoom 1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.95 
    show i_bg_school_front as bg
    show i_sw_black as curtain2:
        # FadeEvent
        linear 1.0 alpha 0.0
    extend "{w=1.0}{nw}"
    extend " That great building that represented my whole life was suddenly very, very small.)" # @t_shiromi378.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_digdug "IS THIS... SKIPPING?!" # @t_shiromi379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear 0.5 xpos -0.3 
        # FadeEvent

    extend "{w=0.5}{nw}"
    t_ch_cousin "Hoo boy..." # @t_shiromi380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin:
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
        # ShowWithAtl
        linear .3 xpos 0.6 
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear .3 xpos 0.7 
    show i_digdug_right as digdug:
        # ShowWithAtl
        linear .75 xpos 0.15 
    extend "{w=0.75}{nw}"
    t_ch_digdug "What do you lawless youths have to say for yourself?!" # @t_shiromi381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "...................." # @t_shiromi382.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Nothing! Just as I suspected! I'm giving the both of you..." # @t_shiromi383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_digdug "DETENTION LEVEL 82: SUPERPOSITION DETENTION" # @t_shiromi384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "It's my fault." # @t_shiromi385.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I kidnapped [slot_playerName]." # @t_shiromi386.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "WHAT?!" # @t_shiromi387.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "WHAT!" # @t_shiromi388.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_cousin "(It took a while to sort that out... I guess she meant well, but I wasn't going to let her take the blame for all that.)" # @t_shiromi389.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Dig Dug confiscated her keys..." # @t_shiromi390.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But when he left, Hiromi took out another pair and parked the bike in the garage.)" # @t_shiromi390.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She really has no fear.)" # @t_shiromi391.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_1Z', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_hiromi3__1Z:
        # <NHSceneChange NHSceneChange {'name': '_1Z', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4