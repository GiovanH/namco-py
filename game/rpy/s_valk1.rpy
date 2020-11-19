# <Scene scene {'id': 's_valk1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_valk1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_valk1"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_valk1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/upbeat_half.ogg" loop
    show i_bg_shopclass as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_sw_black as darkness zorder 3:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_valkyrie_default_grin as valkyrie zorder 2:
        default
        xpos 0.7 
        alpha 0.0
    show i_prop_sword_good as sword1 zorder 5:
        default
        xpos 0.5 
        ypos 0.4 
        xzoom 0.65 
        yzoom 0.65 
        alpha 0.0
    show i_prop_sword_wood as sword2 zorder 5:
        default
        xpos 0.5 
        ypos 0.4 
        xzoom 0.65 
        yzoom 0.65 
        alpha 0.0
    t_ch_cousin "Valkyrie said to meet her in wood shop..." # @t_svalk117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(......)" # @t_svalk118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It's dusty in here... There's sawdust everywhere..." # @t_svalk119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But it smells really good.)" # @t_svalk119.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Everyone's making something." # @t_svalk120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " No one in my family really makes anything." # @t_svalk120.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " We all just roll it up." # @t_svalk120.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I wonder what making something is like... )" # @t_svalk121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grin as valkyrie:
        # ShowWithAtl
        linear .5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "Heyyyy. Couldn't stay away, huh?" # @t_svalk122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "........." # @t_svalk123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_wink as valkyrie
    t_ch_valkyrie "That's called ATTRACTION." # @t_svalk124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin ".................." # @t_svalk125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "The strong silent type, eh?" # @t_svalk126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Absolutely not." # @t_svalk127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_grin as valkyrie
    t_ch_valkyrie "Good. Strong and silent is pretty boring. Wanna see my Hiromi impression?" # @t_svalk128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_bored as valkyrie
    t_ch_valkyrie "........" # @t_svalk129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "..........." # @t_svalk130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_bored as valkyrie
    t_ch_valkyrie "................." # @t_svalk131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_bored as valkyrie
    t_ch_valkyrie ".................................." # @t_svalk132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin ".................................................." # @t_svalk133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_grin as valkyrie
    t_ch_valkyrie "LOL, yours is pretty good too." # @t_svalk134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised_blush as cousin
    t_ch_cousin "I wasn't trying to make fun of her!" # @t_svalk135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie
    t_ch_valkyrie "Relaaaax. I kid because I love." # @t_svalk136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "O-oh. What're you working on?" # @t_svalk137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Oh..." # @t_svalk138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_melancholy as valkyrie
    extend " It's a sword. They took away my real one." # @t_svalk138.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Your REAL one?!" # @t_svalk139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified as cousin
    extend " Are you in detention because you killed someone with it?!" # @t_svalk139.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Like you stabbed them through the heart ..." # @t_svalk140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " And then you chopped them up into little pieces..." # @t_svalk140.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_angry as cousin
    extend " And fed them to Pac-Man?!" # @t_svalk140.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_grin as valkyrie
    t_ch_valkyrie "Whoaaa, pretty good imagination on this one." # @t_svalk141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad_blush as cousin
    t_ch_cousin "Sorry... I get carried away. Why DID you get your sword taken away?" # @t_svalk142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_wink as valkyrie
    t_ch_valkyrie "…. You're really cute when you're serious." # @t_svalk143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(She evaded the question?!)" # @t_svalk144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie
    t_ch_valkyrie "You get this crease in your forehead zone... It makes you look really thoughtful." # @t_svalk145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(WAS IT DETENTION... FOR MURDER?!)" # @t_svalk146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(That seems... Lenient... )" # @t_svalk147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_thoughtful as valkyrie
    t_ch_valkyrie "They took my sword away to punish me... I don't like being separated from it, so I figured I'd just make a temp blade to hold me over." # @t_svalk148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Like a really sharp teddy bear... )" # @t_svalk149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Oh, she's showing me the sword. Wow. It's really nice. I was thinking that she's a little flighty, but..." # @t_svalk150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " This is really expertly crafted. It must've taken a lot of dedication and concentration.)" # @t_svalk150.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral_blush as cousin
    t_ch_cousin "(I wonder what's really going on in her head... Besides all the flirting.)" # @t_svalk151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "This sword looks great." # @t_svalk152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " Can I tell you something? I'm a little jealous..." # @t_svalk152.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I've never made anything like this. I've definitely never worked with wood before." # @t_svalk153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie
    t_ch_valkyrie "You haven't?! OMG, it's super fun!" # @t_svalk154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Is it?" # @t_svalk155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Totally. You should try it out." # @t_svalk156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I don't know... I have these tiny Katamari hands... They're not good for much besides rolling." # @t_svalk157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        pause 1.0 
        linear .3 xpos 0.6 
    extend "{w=1.3}{nw}"
    t_ch_valkyrie "Aw, I like your hands. They're all small and delicate. You should see mine!" # @t_svalk158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Whoa... They're really strong looking. She's definitely worked with her hands for a very long time.)" # @t_svalk159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie:
        # ShowWithAtl
        linear .2 xpos 0.55 
    extend "{w=0.2}{nw}"
    t_ch_valkyrie "Touch them!" # @t_svalk160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "Is it ok?" # @t_svalk161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I said so, didn't I?" # @t_svalk162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I'm going to touch them!)" # @t_svalk163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Her fingers are long and thin, and ... they're so rough. Her palm feels like warm leather!" # @t_svalk164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    extend " Like a crocodile or something." # @t_svalk164.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I rolled one of those up once.)" # @t_svalk164.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_thoughtful as valkyrie
    t_ch_valkyrie "Ahem..." # @t_svalk165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Hmmm?" # @t_svalk166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "I said you could touch them..." # @t_svalk167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "?" # @t_svalk168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grinblush as valkyrie
    t_ch_valkyrie "But you might be taking too long." # @t_svalk169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin:
        # ShowWithAtl
        linear .1 xpos 0.2 
    extend "{w=0.1}{nw}"
    t_ch_cousin "OH! Sorry!" # @t_svalk170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_default_grinblush as valkyrie
    t_ch_valkyrie "It's okay. I don't mind." # @t_svalk171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "........" # @t_svalk172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin
    t_ch_cousin "(Am I blushing? I hope not... )" # @t_svalk173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Will you show me how to make a sword... ? It looks fun." # @t_svalk174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie:
        # ShowWithAtl
        linear .5 xpos 0.8 
    extend "{w=0.5}{nw}"
    t_ch_valkyrie "Sure! Just grab some wood from the pile there and bring it to the table saw." # @t_svalk175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear .5 xpos 0.45 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(Whoa, that spinny saw thing looks dangerous... )" # @t_svalk176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/circularsaw.ogg" loop
    t_ch_valkyrie "Just lay it down and run it through..." # @t_svalk177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Like this?" # @t_svalk178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_bored as valkyrie
    t_ch_valkyrie "..........." # @t_svalk179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "LOL, uhhh… Wow, that's really crooked." # @t_svalk180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I've never seen someone cut so crooked." # @t_svalk180.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_wink as valkyrie
    t_ch_valkyrie "It's gotta be a special talent of yours." # @t_svalk181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "..............." # @t_svalk182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie
    extend " Oh, I think I see what happened." # @t_svalk182.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You have to use the rail as a guide." # @t_svalk182.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " If you wait too long it'll burn up, so you gotta do it quick." # @t_svalk182.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "It's pretty difficult..." # @t_svalk183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_grin as valkyrie
    t_ch_valkyrie "Yeah... It took me a few tries to learn it. We don't have any of this stuff back home." # @t_svalk184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "It's also kind of scary..." # @t_svalk185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grin as valkyrie
    t_ch_valkyrie "It's not THAT scary. Just line it up and push it through, really steady-like. Try it again." # @t_svalk186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Okay..." # @t_svalk187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grin as valkyrie zorder 1:
        # ShowWithAtl
        linear .7 xpos 0.25 
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
    extend "{w=0.7}{nw}"
    t_ch_valkyrie "No you need to... Like this!" # @t_svalk188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "!!" # @t_svalk189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "(She got behind me and put her hands on mine..." # @t_svalk190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Her hands are really steady. That rugged texture is suddenly so reassuring... It's comforting to know she's done this so many times before.)" # @t_svalk190.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "........." # @t_svalk191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(She's so warm... And her hair smells really nice..." # @t_svalk192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Like a whole rolled up forest... Oak and ash and elm and pine and spruce.)" # @t_svalk192.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Her hands are so sure on mine..." # @t_svalk193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " .............." # @t_svalk193.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Wasn't there a movie like this?)" # @t_svalk193.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_forjustice_grinblush as valkyrie
    t_ch_valkyrie "....................." # @t_svalk194.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "......... What?" # @t_svalk195.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_valkyrie "Everyone's looking." # @t_svalk196.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin:
        # ShowWithAtl
        linear .5 xpos 0.7 
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
    stop sound
    extend "{w=0.5}{nw}"
    t_ch_cousin "AHHH!" # @t_svalk197.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified_blush as cousin
    t_ch_cousin "(They totally are!)" # @t_svalk198.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "We should stop!" # @t_svalk199.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_akimbo_grinblush as valkyrie
    t_ch_valkyrie "Ahhh, let them look. They WISH they were having this much fun." # @t_svalk1100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "............." # @t_svalk1101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Making the rest of the sword is fuzzy. All I could think about was the people looking at us.)" # @t_svalk1102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(But Valkyrie didn't mind at all. She wasn't bothered in the least!)" # @t_svalk1103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(She's confident and fearless.)" # @t_svalk1104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(.... I ... like it. I know we're both in high school, but she seems much more worldly.)" # @t_svalk1105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I wonder why that is... And what it has to do with her stint in detention... )" # @t_svalk1106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_grin as valkyrie
    t_ch_valkyrie "It's done!" # @t_svalk1107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Oh!" # @t_svalk1108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_wink as valkyrie
    extend "{w=1.0}{nw}"
    t_ch_valkyrie "Sorry, I could only help so much... You definitely have a knack for being bad at this!" # @t_svalk1109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "HEY! How'd YOURS come out?" # @t_svalk1110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_thoughtful as valkyrie
    t_ch_valkyrie "Maybe we shouldn't compare..." # @t_svalk1111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh, come on! How different could they be?" # @t_svalk1112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_prop_sword_good as sword1:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
        # ShowWithAtl
        linear .8 alpha 1.0
    show i_prop_sword_wood as sword2:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
        # ShowWithAtl
        linear .8 alpha 1.0
    show i_sw_black as darkness:
        # ShowWithAtl
        linear .5 alpha 0.5
    $ renpy.pause(0.8, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_grin as valkyrie
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "You ARE really good at this..." # @t_svalk1113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_prop_sword_good as sword1:
        # ShowWithAtl
        linear .333 alpha 0.0
    show i_prop_sword_wood as sword2:
        # ShowWithAtl
        linear .333 alpha 0.0
    show i_sw_black as darkness:
        # ShowWithAtl
        linear .5 alpha 0.0
    $ renpy.pause(0.5, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} '<ActorFade duration=".6" opacity="0" target="sword" />'>
    show i_sw_black as curtain:
        # ShowWithAtl
        linear .6 alpha 0.0
    extend "{w=0.6}{nw}"
    t_ch_valkyrie "Next time we hang out, we should go to the roof. We can do some really neat stuff up there!" # @t_svalk1114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised_blush as cousin
    t_ch_cousin "Just us? Alone?" # @t_svalk1115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_wink as valkyrie
    t_ch_valkyrie "LOL, sure! It's more fun that way!" # @t_svalk1116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_valkyrie_armscrossed_wink as valkyrie:
        # ShowWithAtl
        linear 1 alpha 0.0
    extend "{w=1.0}{nw}"
    extend " Bye!" # @t_svalk1116.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "(Just what 'fun stuff' is she talking about?!)" # @t_svalk1117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...................." # @t_svalk1118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(My face feels warm. Is this what they call....." # @t_svalk1119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " a crush?!" # @t_svalk1119.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I'm too young! I'm not ready!)" # @t_svalk1120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "............." # @t_svalk1121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "....................." # @t_svalk1122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "................................." # @t_svalk1123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Her laugh is really cute... )" # @t_svalk1124.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_27', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
    label s_valk1__27:
        # <NHSceneChange NHSceneChange {'name': '_27', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
        jump s_day2