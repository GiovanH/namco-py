# <Scene scene {'id': 's_tomari5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_tomari5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_tomari5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_tomari5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/privatetimes.ogg" loop
    show i_bg_hallway_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_tomari_standing_mortified as tomari zorder 2:
        default
        xpos 0.7 
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.5 
    t_ch_cousin "(I haven’t seen Tomari all day.)" # @t_stomari50.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(He was so distraught about what happened to the Super Robot…)" # @t_stomari51.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I’ve got to find some way to help him!)" # @t_stomari52.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Maybe...I dunno. Maybe Dr. Kubota’s shadowy figure left something useful in the engineering room and I can, um, well, show it to Tomari.)" # @t_stomari53.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(Okay, that’s a terrible plan.)" # @t_stomari54.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (But it’s all I’ve got!)" # @t_stomari54.01 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0) # Curtain fade
    show i_bg_shopclass as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_shopclass', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_6', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_tomari_standing_mortified as tomari:
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "…" # @t_stomari55.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Oh, Tomari! I wonder how long he’s been here. All day?)" # @t_stomari56.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Uh. Ahem." # @t_stomari56.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "Hm? Oh, [slot_playerName]." # @t_stomari57.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "It’s you." # @t_stomari58.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "I was just scavenging for anything useful they might have left behind." # @t_stomari59.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Ha! It wasn’t such a bad idea after all!)" # @t_stomari510.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_frustrated as tomari
    t_ch_tomari "SO I CAN THROW IT AWAY!" # @t_stomari511.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What?!" # @t_stomari512.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_tomari "I used to think the only thing that separated player characters from common drone enemies and power ups was our capacity for rational thought." # @t_stomari513.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "We do more than move in pre-described patterns." # @t_stomari514.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "We can react to the environment. We learn about it. We can create change upon it." # @t_stomari515.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_thoughtful as tomari
    t_ch_tomari "But I was never any kind of inventor, [slot_playerName]." # @t_stomari516.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "I wasn’t even cut out to be the engineering club janitor’s assistant’s probationary trainee." # @t_stomari517.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I used to think Tomari only needed to get over his weird intensity to become a happier person with lots of friends…)" # @t_stomari518.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(And maybe me as something a bit more than friends.)" # @t_stomari519.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    extend " (Hey, it could happen!)" # @t_stomari519.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " (But now that I see him without it, he’s so much worse off than before!)" # @t_stomari519.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(So much more alone!)" # @t_stomari520.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_tomari "I wasted my life, [slot_playerName]." # @t_stomari521.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "I hereby renounce inventing." # @t_stomari522.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "ENTIRELY." # @t_stomari523.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Gasp!" # @t_stomari524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "Today I begin my new life." # @t_stomari525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_mortified as tomari
    extend " AS A LAW STUDENT!" # @t_stomari525.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "NNNNNNNNNNNNNNNNNNNNNNNNNNNNN" # @t_stomari526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "OOOOOOOOOOOOOOOOOOOOOOOOOO!" # @t_stomari527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    extend " Hang on." # @t_stomari527.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Will we really need lawyers during the ten thousand years of apocalyptic horror?" # @t_stomari528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "It will be an age of darkness and evil." # @t_stomari529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "I want to fit in." # @t_stomari530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "But a lawyer, Tomari?" # @t_stomari531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "That’s going too far!" # @t_stomari532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_tomari "Is it? I was never cut out for inventing anyway." # @t_stomari533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "If it weren’t for your brilliant suggestions I probably would’ve managed to blow up that Super Robot instead of fixing it." # @t_stomari534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "It was you, [slot_playerName]." # @t_stomari535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_frustrated as tomari
    t_ch_tomari "You were the true inventor." # @t_stomari536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "Maybe with your ingenious mind YOU can defeat Dr. Kubota at the Robot Battle Brawl and save all of Namco Land." # @t_stomari537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(AUGH! What can I do?)" # @t_stomari538.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I didn’t invent a darn thing. It was all Tomari. He’s the genius! I just said random stuff that he made into coherent solutions.)" # @t_stomari539.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (But can I tell him I was lying all along?)" # @t_stomari539.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(That I’m not the tech wizard he thinks I am?)" # @t_stomari540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Would he hate me for not being a genius?)" # @t_stomari541.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Would he hate me for being a liar?)" # @t_stomari542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Could I even blame him?)" # @t_stomari543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "But not me. I can’t save them. I’m worse than scum." # @t_stomari544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This is all my fault! If only I knew what to do!)" # @t_stomari545.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        default
        xpos 1.45 
        easeout 5 xpos 0.8 
    $ renpy.pause(2) # ParallelEvent Delay
    # <ParallelEvent ParallelEvent {'delay': '2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        easeout 0.333 xpos 0.15 
    show i_tomari_pondering_thinking as tomari:
        xzoom -1.0 
        # ShowWithAtl
        easeout 0.333 xpos 0.35 
    $ renpy.pause(0.333, hard=True) # TimedPause
    $ renpy.pause(5.0, hard=True) # TimedPause
    stop sound
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Be true to yourself." # @t_stomari546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(How convenient he should show up and tell me exactly what I needed to hear!)" # @t_stomari547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I don’t want to be Liar [slot_playerName].)" # @t_stomari548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(How can I do anything but tell Tomari the truth!)" # @t_stomari549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "Pac-Man." # @t_stomari550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_smile as tomari
    t_ch_tomari "Your impeccably timed wisdom has not escaped me!" # @t_stomari551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wait.)" # @t_stomari552.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Will Tomari abandon this abhorrent lawyer talk?)" # @t_stomari553.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Maybe I won’t have to reveal the truth after all…?)" # @t_stomari554.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "To lie to oneself is to lie to the world." # @t_stomari555.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "I must be true to myself." # @t_stomari556.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "You’ve made me see that, Pac-Man." # @t_stomari557.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "I must fulfill my destiny." # @t_stomari558.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_frustrated as tomari
    extend " AND BECOME A LAWYER!" # @t_stomari558.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "NO, TOMARI, NOTHING IS AS BAD AS THAT!!!!" # @t_stomari559.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " I…" # @t_stomari559.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I’m not the engineering genius you think I am." # @t_stomari560.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "The truth is that I don’t know ANYTHING about technology or inventing." # @t_stomari562.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_tomari "[slot_playerName]?" # @t_stomari563.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "You’re not making any sense." # @t_stomari564.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "In the parlance of my new life…" # @t_stomari565.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_alive_frustrated as tomari
    extend " ...YOU’RE OUT OF ORDER!" # @t_stomari565.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(Oh no! The transformation has already begun! I just hope I’m not too late!)" # @t_stomari566.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Tomari, I didn’t join the engineering club because of any interest in engineering or robotics or inventing or whatever it is you do there." # @t_stomari566.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I joined…" # @t_stomari567.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    show i_tomari_defeated_mortified as tomari
    t_ch_cousin "I joined to get closer to you!" # @t_stomari568.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Every time you talked about an engineering problem, I’d panic and blurt out the first nonsense that came to mind!" # @t_stomari569.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "But…" # @t_stomari570.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "That can’t be, [slot_playerName]." # @t_stomari571.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It’s true! And I don’t blame you if you hate me for it!" # @t_stomari572.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I was lying to you all along. I’m the scum of the Earth, not you! I should become the lawyer!" # @t_stomari573.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_thinking as tomari
    t_ch_tomari "But everything you suggested worked." # @t_stomari574.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "[slot_playerName], how could it have been nonsense if it worked?" # @t_stomari575.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Don’t you see, young Tomari? The solutions were inside you all along." # @t_stomari576.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_thinking as tomari
    t_ch_tomari "Is...is it possible?" # @t_stomari577.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_smile as tomari
    t_ch_tomari "Am I even MORE brilliant than I actually am???" # @t_stomari578.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "*nods sagaciously*" # @t_stomari579.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_mortified as tomari
    t_ch_tomari "But, [slot_playerName]…" # @t_stomari580.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "You lied to me? All this time?" # @t_stomari581.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I was only trying to help you!" # @t_stomari582.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "Uh, and also to date you." # @t_stomari583.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_thinking as tomari
    t_ch_tomari "I don’t know what to say." # @t_stomari584.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Don’t say anything. I know it was screwed up to pretend like I was something I wasn’t." # @t_stomari585.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "You built the Super Robot once, Tomari." # @t_stomari586.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You can represent Namco High at the Robot Battle Brawl and you can defeat the forces of Evil Namco High!" # @t_stomari587.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m not entirely convinced it’ll have the impact on all of society you predict, but…" # @t_stomari587.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I KNOW YOU CAN DO IT!" # @t_stomari588.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And I know I can’t take back what I did. I can only…" # @t_stomari588.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "BE TRUE TO MYSELF" # @t_stomari589.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...and help you!" # @t_stomari590.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "[slot_playerName]?" # @t_stomari591.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_smile as tomari
    t_ch_tomari "That was the first time since we met that you said “Robot Battle Brawl” the right way." # @t_stomari592.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(Was it? Huh!)" # @t_stomari593.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_smile as tomari
    t_ch_tomari "But...did you really want to go on a date with me?" # @t_stomari594.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "H-hey, now’s not the time." # @t_stomari595.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Y’know, with Pac-Man right here and all." # @t_stomari596.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "*nods sagaciously*" # @t_stomari597.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_mortified as tomari
    t_ch_tomari "…" # @t_stomari598.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "…" # @t_stomari599.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "…" # @t_stomari5100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "………………………" # @t_stomari5101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "…………………………………………..." # @t_stomari5102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "I don’t think he’s gonna leave…" # @t_stomari5103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Dang it, Pac-Man." # @t_stomari5104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin
    t_ch_cousin "YES, I was thinking, y’know, we could go out sometime." # @t_stomari5105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_thinking as tomari
    t_ch_tomari "Why?" # @t_stomari5106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad_blush as cousin
    t_ch_cousin "Ugh. You’re even kinda cute when you’re clueless." # @t_stomari5107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral_blush as cousin
    t_ch_cousin "Tomari. It turns out once you get past the obsessive inventor stuff, you’re nice." # @t_stomari5108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And a little cool. But only a very little." # @t_stomari5109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "I’m not sure I’d be ready for a lot of cool, so that works out." # @t_stomari5110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Also you’re kind of handsome." # @t_stomari5111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_mortified as tomari
    t_ch_tomari "Hmm." # @t_stomari5112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "I’d never considered the possibility that I might fulfill a satisfactory number of conditions to achieve a state of “the hotness.”" # @t_stomari5113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_thinking as tomari
    t_ch_tomari "This is quite intriguing and should be studied in more detail." # @t_stomari5114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "I’ll require a control group of course." # @t_stomari5115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "Perhaps some sort of Tomari clone is in order..." # @t_stomari5116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "Cloning?!" # @t_stomari5117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_smile as tomari
    t_ch_tomari "Ah, but I digress." # @t_stomari5118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "Do you really think I can rebuild the Super Robot?" # @t_stomari5119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "I know you can." # @t_stomari5120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_smile as tomari
    t_ch_tomari "I might need your help." # @t_stomari5121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "My help?" # @t_stomari5122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "Does...do you mean...you don’t hate me?" # @t_stomari5123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "You did lie to me…" # @t_stomari5124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_defeated_frustrated as tomari
    t_ch_tomari "A LOT." # @t_stomari5125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_standing_smile as tomari
    show i_pacman_left as pacman:
        # ShowWithAtl
        ease_expo 0.25 xpos 0.85 
    extend "{w=0.25}{nw}"
    t_ch_tomari "But, you meant no harm." # @t_stomari5126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        ease_expo 0.25 xpos 0.9 
    extend "{w=0.25}{nw}"
    t_ch_tomari "And, somehow against all the odds, it actually helped me." # @t_stomari5127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        ease_expo 0.25 xpos 1.0 
    extend "{w=0.25}{nw}"
    t_ch_tomari "There’s no denying we make a great engineering club team! But let’s start over." # @t_stomari5128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        ease_expo 0.25 xpos 1.1 
    extend "{w=0.25}{nw}"
    t_ch_tomari "And this time we’ll be true to ourselves the whole time!" # @t_stomari5129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        ease_expo 0.25 xpos 1.35 
    show i_cousin_default_grin as cousin
    extend "{w=0.25}{nw}"
    t_ch_cousin "Yes! Being true to yourself is super!" # @t_stomari5130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "THANK YOU PAC-MAN!" # @t_stomari5131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    extend " !!!!" # @t_stomari5131.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Wh-where did he go…?" # @t_stomari5131.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_thinking as tomari
    t_ch_tomari "Pac-Man is like the wind." # @t_stomari5132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "He goes where he’s needed." # @t_stomari5133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tomari_pondering_mortified as tomari
    t_ch_tomari "And then he hangs around a little too long and that makes things kind of weird." # @t_stomari5134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_tomari "But then, just as the wind that brought him there, he’s gone." # @t_stomari5135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Thank you, Pac-Man." # @t_stomari5136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman zorder 9:
        # ActorEvent
        alpha 0.0
        xpos 0.5 
        xzoom 1.5 
        yzoom 1.5 
    show i_sw_black as curtain2 zorder 8:
        default
        alpha 0.0
    t_ch_cousin "Wherever you are!" # @t_stomari5137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear 1 alpha 0.5
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 1 alpha 0.5
    extend "{w=1.0}{nw}"
    t_ch_pacman "I think those kids are gonna be okay." # @t_stomari5138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear 1 alpha 1.0
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 1 alpha 1.0
    extend "{w=1.0}{nw}"
    t_ch_pacman "As long as they stay true to themselves." # @t_stomari5139.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_2Y', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_tomari5__2Y:
        # <NHSceneChange NHSceneChange {'name': '_2Y', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5