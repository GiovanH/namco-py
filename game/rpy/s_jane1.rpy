# <Scene scene {'id': 's_jane1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_jane1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_jane1"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_jane1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/aroundtown.ogg" loop
    show i_bg_library as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_jane_default_smile as jane zorder 2:
        default
        xpos 0.7 
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    t_ch_cousin "(Jane brought me to the library, where we’ll work on the school paper." # @t_sjane117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " Sounds pretty fun! I wonder if there were any articles about my “incident” with the katamari…)" # @t_sjane117.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin as jane
    t_ch_jane "I’m pleased as punch you wanted to join me, [slot_playerName]!" # @t_sjane118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "I love the chance to investigate a good mystery." # @t_sjane119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_grin as jane
    extend " Not to toot my own horn, but I can be quite the gutsy gumshoe when the situation calls for it!" # @t_sjane119.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(That’s an oddly specific phrasing.)" # @t_sjane120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Say Jane, before we get started, could I see some of the back issues?" # @t_sjane121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " I’m curious to see how my… uh, “bowling ball incident” was covered." # @t_sjane121.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_frustrated as jane
    t_ch_jane "Hrrm… :|" # @t_sjane122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "I’m sorry, [slot_playerName]! I do not believe that was actually covered in the school paper." # @t_sjane123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane
    t_ch_jane "It wasn’t exactly an earth-shattering occurrence, now was it?" # @t_sjane124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "I know these things always seem to loom large in one’s own mind, but that doesn’t mean it did for anyone else. There’s no need to keep being so sensitive about it." # @t_sjane125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "But here’s the paper from that day, if you insist. Maybe it can put your poor mind at ease." # @t_sjane126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(How could it not be covered by the school paper?!" # @t_sjane127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I rolled almost EVERYTHING up!" # @t_sjane127.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Let’s see here…)" # @t_sjane127.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Headline: “Tater Tots a hit in the cafeteria”?" # @t_sjane128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin as jane
    t_ch_jane "It’s important to cover events that are relevant to the school at large! :B" # @t_sjane129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "“Editorial by Jane Crocker: ‘Mustaches are Totally Hot’?”" # @t_sjane130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_embarrassed_blush as jane
    t_ch_jane "Um…" # @t_sjane131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_laugh_blush as jane
    extend " Hoo hoo…" # @t_sjane131.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin_blush as jane
    extend " Oh boy! Yes! That sure was a thing I wrote." # @t_sjane131.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Well… you’ve got to admit, [slot_playerName]…" # @t_sjane132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " When it comes to attractive things, mustaches rank pretty high up there!" # @t_sjane132.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_grin_blush as jane
    t_ch_jane "I mean… only if that was a thing you wanted to think about, clearly!!!" # @t_sjane133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Ahahahaha." # @t_sjane134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    with Dissolve(.333)
    t_ch_cousin "(Maybe I should start wearing a fake mustache too.)" # @t_sjane135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Look, I’m not commenting about the hotness or not-hotness of certain facial hair…" # @t_sjane136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " I’m just saying, these things aren’t exactly earth-shattering occurrences either!" # @t_sjane136.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_smile as jane
    t_ch_jane "Yes, I have to admit that’s true." # @t_sjane137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Actually, I’ve been meaning to try to go a little farther with my investigative reporting lately." # @t_sjane137.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "After all, there are plenty of good mysteries afoot at Namco High!" # @t_sjane138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_smile as jane
    extend " You must have noticed, [slot_playerName]." # @t_sjane138.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "!! So you DO know!" # @t_sjane139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "For example, the man who oversees our detention- King!" # @t_sjane139.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This must be about his scary jaguar head!" # @t_sjane140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I knew she must’ve realized that strange things go on here.)" # @t_sjane141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_grin as jane
    t_ch_jane "...If he was such a good wrestler, why did he take up a teaching position here?" # @t_sjane142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s a real head-scratcher, [slot_playerName]!" # @t_sjane142.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "THAT’S what you think the big mystery is about King?!" # @t_sjane143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Or that cat that’s in class with us. How do they make it seem like it’s talking all the time?" # @t_sjane144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_frustrated as jane
    extend " It must be a school mascot, but SHUCKS, they’re sure taking it far!" # @t_sjane144.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Meowkie’s not a mascot! She’s a PERSON!" # @t_sjane145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Jane, how can you just ignore the fact that crazy, weird things are going on at the school?" # @t_sjane146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " It’s starting to creep me out! It’s like you’ve gone so far with skepticism, it’s actually doubled back into naivete again!" # @t_sjane146.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_embarrassed as jane
    t_ch_jane "Wow, WHAT?!" # @t_sjane147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Sheesh! There’s no need to be rude!" # @t_sjane147.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_armscrossed_smile as jane
    t_ch_jane "...Wait, is this another stupid attempt at “pranking” me?" # @t_sjane148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Cats simply do not talk, [slot_playerName]. We both know that!" # @t_sjane148.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "…" # @t_sjane149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I’m starting to think you really must be a master prankster…" # @t_sjane150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Because that’s what this has got to be, right?" # @t_sjane150.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I mean, look at your friends that you sit with in detention!" # @t_sjane151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Who? Terezi and Davesprite?" # @t_sjane152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " They’re good chums, sure. I don’t see what this has to do with them, though!" # @t_sjane152.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Are you kidding me?!" # @t_sjane153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " One’s an orange floaty bird guy and the other is gray and has horns!" # @t_sjane153.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_frustrated as jane
    t_ch_jane "Shut up about them! You don’t understand!" # @t_sjane154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane
    extend " They’re just… COSPLAY ENTHUSIASTS!" # @t_sjane154.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I don’t think so, Jane." # @t_sjane155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Have you ever seen Terezi outside of her “costume”?" # @t_sjane156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Even once?!" # @t_sjane156.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_frustrated as jane
    t_ch_jane "Hmmmm…" # @t_sjane157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane ":|" # @t_sjane158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...So you really don’t believe anything strange is going on at the school?" # @t_sjane159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s not just a prank you’re playing on me?" # @t_sjane159.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I find that hard to believe… a smart girl like Jane, just ignoring what’s right in front of her.)" # @t_sjane160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane
    t_ch_jane "Sorry, [slot_playerName]. I’m a curmudgeonly skeptic, born and bred!" # @t_sjane161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_grin as jane
    extend " Besides, being a lover of pranks myself, I can spot one from a mile away." # @t_sjane161.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "Actually, I find it hard to believe you can’t see through such silly, made-up stuff." # @t_sjane162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You seem like quite the smart cookie!" # @t_sjane164.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "R-really? Thanks…" # @t_sjane165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "I suppose it isn’t really your fault, if you don’t have a lot of experience with pranks to begin with." # @t_sjane166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_laugh as jane
    t_ch_jane "Like… THIS!!!" # @t_sjane167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Huh? What-" # @t_sjane168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin:
        linear 0.20 xzoom -1.0 
    extend " AAAUGH! THERE’S A SPIDER ON MY SHOULDER!!!)" # @t_sjane168.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "HOO HOO HOO! :B" # @t_sjane169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        linear 0.20 xzoom 1.0 
    t_ch_cousin "Oh… it’s only a fake spider." # @t_sjane170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Wait! How did you get it there without me noticing?" # @t_sjane170.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "You really ARE great at pranks!" # @t_sjane171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin as jane
    t_ch_jane "Guilty as charged! ;B" # @t_sjane172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Seriously though, where did that fake spider even come from?" # @t_sjane173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " She doesn’t have a backpack or anything, and it wouldn’t fit in her pocket." # @t_sjane173.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Did she just pull it out of thin air?" # @t_sjane174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Does she have master prankster powers??!!" # @t_sjane174.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Nah… It can’t be…)" # @t_sjane175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane
    t_ch_jane "Okey dokey. Enough of this fooling around." # @t_sjane176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " [slot_playerName], you may be a real babe in the woods, but you’ve given me a good idea…" # @t_sjane176.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Huh? I have?" # @t_sjane177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_handonhip_grin as jane
    t_ch_jane "Yes!! Let’s meet again soon." # @t_sjane178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I have something in mind for a “journalistic excercise” we could do." # @t_sjane178.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_jane "In fact, it might even help curtail those silly thoughts you’re having!" # @t_sjane179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Show you once and for all that all that nonsense you believe in is a hoax, I mean." # @t_sjane179.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That’s… pretty presumptuous of you!" # @t_sjane180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_grin as jane
    t_ch_jane "Oh, shoosh! Get going, you! I have some planning to do!" # @t_sjane181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane
    extend " See you tomorrow, [slot_playerName]!" # @t_sjane181.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(And with that, she pushes me right out of the library, and slams the door shut behind her.)" # @t_sjane182.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # Curtain fade
    show i_bg_hallway_b as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_b', 'curtainActor': 'curtain', 'curtainFadeTime': '0.75', 'name': '_1Z', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_jane_default_smile as jane:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_cousin_default_neutral as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(You know, by refusing to believe in any of the weird stuff going on at Namco High…" # @t_sjane183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Jane Crocker might actually be the weirdest person I’ve met here!" # @t_sjane183.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "I wonder what she’d say if I told her that, haha." # @t_sjane184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Even so…" # @t_sjane184.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I think it would be nice to go along with that “journalistic exercise” she was talking about." # @t_sjane185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " She’s pretty fun to be around…" # @t_sjane185.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    with Dissolve(.333)
    t_ch_cousin "Er, not that I like her or anything!!!" # @t_sjane186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "..." # @t_sjane187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " ...I wonder where I could find a fake mustache to wear…)" # @t_sjane187.01 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_1j', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
    label s_jane1__1j:
        # <NHSceneChange NHSceneChange {'name': '_1j', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
        jump s_day2