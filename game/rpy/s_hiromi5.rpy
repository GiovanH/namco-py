# <Scene scene {'id': 's_hiromi5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_hiromi5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_hiromi5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_hiromi5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/upbeat_half.ogg" loop
    show i_bg_quad_bleachers as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_tobi_stand_grin as toby zorder 2:
        default
        xpos 0.3 
        alpha 0.0
    show i_cousin_energetic_grin as cousin zorder 2:
        default
        xpos 0.3 
    show i_hiromi_crossed_serious as hiromi zorder 2:
        default
        xpos 0.7 
    show i_pacman_left as pacman zorder 2:
        default
        xpos 0.7 
        alpha 0.0
    t_ch_cousin "(This is it! Hiromi's big day.)" # @t_shiromi511.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_stand_serious as hiromi
    t_ch_hiromi "Oh... Hey, kid." # @t_shiromi512.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_laugh as cousin
    t_ch_cousin "I'm going to be in the stands, cheering for you!" # @t_shiromi513.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "Uh-huh." # @t_shiromi514.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(She's so cool under pressure... )" # @t_shiromi515.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_tool_serious as hiromi
    t_ch_hiromi "I have to the last tune-ups with Tomari, now." # @t_shiromi516.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_laugh as cousin
    t_ch_cousin "Okay! I believe in you!" # @t_shiromi517.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_akimbo_serious as hiromi
    t_ch_hiromi "Kid..." # @t_shiromi518.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "I was going to dedicate my race to ..........." # @t_shiromi519.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "..... To Kissy?" # @t_shiromi520.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_straight_blush as hiromi
    t_ch_hiromi "Y-yeah. But I was thinking......." # @t_shiromi521.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_serious as hiromi
    t_ch_hiromi "..... Maybe I'll dedicate one of my laps to you." # @t_shiromi522.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear 1 alpha 0.0
    show i_cousin_energetic_neutral as cousin
    extend "{w=1.0}{nw}"
    t_ch_cousin "(Wow... That was really sweet, in its own icy, aloof... Extremely distant way." # @t_shiromi523.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear .75 xpos 0.5 
    extend "{w=0.75}{nw}"
    extend " I guess she likes me?" # @t_shiromi523.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    extend " I'd like to think we're friends.)" # @t_shiromi523.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I suppose I'll head down to the track now so I can get a good seat." # @t_shiromi524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I wouldn't want to get stuck all the way in the back!)" # @t_shiromi524.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain:
        # ShowWithAtl
        linear .3 alpha 1.0
    $ renpy.pause(0.3, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain:
        # ShowWithAtl
        linear .3 alpha 0.0
    show i_bg_cliff_night as bg
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(It looks like the race has already started!)" # @t_shiromi525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I'm so small, it's easy to squeeze through the crowd... I got front row seats!)" # @t_shiromi526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(The bikes are all moving so fast... It's hard to tell which one is Hiromi's.)" # @t_shiromi527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Maybe if I squint-- )" # @t_shiromi528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_questionmarks "WHOOOOOOOOOOO!" # @t_shiromi529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_cheering as toby:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
        # ShowWithAtl
        linear .75 alpha 1.0
    extend "{w=0.75}{nw}"
    extend " GO GO GOOOOOOOOOOOO!" # @t_shiromi529.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_questionmarks "FASTER!" # @t_shiromi530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    extend " BEAT THOSE LOSERS!" # @t_shiromi530.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_questionmarks "THEY CAN EAT YOUR DUST!" # @t_shiromi531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_questionmarks "HEY... HEY YOU!" # @t_shiromi532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " YEAH, THAT DUMB RED MOTORCYCLE!" # @t_shiromi532.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " GET OUT OF THE WAY!" # @t_shiromi532.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(What a boisterous, enthusiastic fan... )" # @t_shiromi533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby
    show i_cousin_exhausted_neutral as cousin
    t_ch_questionmarks "Phew! Yelling is hard work!" # @t_shiromi534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "It looks like it!" # @t_shiromi535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby
    t_ch_questionmarks "Are you a racing fan too?!" # @t_shiromi536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "I guess you could say I'm becoming one. I'm here to cheer a friend." # @t_shiromi537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_questionmarks "Me too! What a coincidence!" # @t_shiromi538.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_questionmarks "My name's Toby, by the way!" # @t_shiromi539.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Hi Toby! I'm [slot_playerName]." # @t_shiromi540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "You know, I'm cheering really hard... But honestly, I can't really tell which one she is." # @t_shiromi541.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "They're all kind of blurry huh?" # @t_shiromi542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_toby "Yeah....." # @t_shiromi543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby
    t_ch_toby "To tell you the truth, I always cheer for the prettiest lights." # @t_shiromi544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "They really dazzle me." # @t_shiromi545.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby
    t_ch_toby "[slot_playerName]... Let's cheer together!" # @t_shiromi546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_laugh as cousin
    extend " Ready?" # @t_shiromi546.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_cheering as toby
    t_ch_toby "GO GO GO!!" # @t_shiromi547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " WHOOOOOO!" # @t_shiromi547.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "TWO, FOUR, SIX, EIGHT" # @t_shiromi548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " WHO DO WE APPRECIATE?" # @t_shiromi548.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "UMMM.... WHOEVER INVENTED THE MOTORCYCLE FOR INVENTING THE MOTORCYLE!!!" # @t_shiromi549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Y-YEAH, WHOOO! THAT ONE BIKE.... BEAT THAT OTHER BIKE!" # @t_shiromi550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "YOU'RE DOING IT!" # @t_shiromi551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " YOU'RE GOING REAL FAST!" # @t_shiromi551.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " WOW!" # @t_shiromi551.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " LOOK AT YOU GO!" # @t_shiromi551.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby
    t_ch_toby "Those are pretty good [slot_playerName]..." # @t_shiromi552.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_sad as cousin
    t_ch_cousin "Thanks... I'm sort of a novice at this..." # @t_shiromi553.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "It's okay. You're doing great!" # @t_shiromi554.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "So [slot_playerName]... What do you do?" # @t_shiromi555.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Me? I'm a student at Namco High." # @t_shiromi556.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "I see... Do you like it?" # @t_shiromi557.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "It's not bad. I'm stuck in detention, though." # @t_shiromi558.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "Ohoho, I'm hanging out with a delinquent!" # @t_shiromi559.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "I'm not that bad!" # @t_shiromi560.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby
    t_ch_toby "It's okay... My friend is a delinquent too." # @t_shiromi561.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "Enough of a delinquent to have been held back a few times." # @t_shiromi562.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Her friend? It couldn't be... )" # @t_shiromi563.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What about you, Miss Toby?" # @t_shiromi564.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby
    t_ch_toby "Haha... Toby's fine. I was in the United Galaxy Space Force." # @t_shiromi565.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "O-oh..." # @t_shiromi566.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I guess if Galaga is a spaceship... This isn't much of a stretch.)" # @t_shiromi567.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "I was in the Battle of Baraduke, ‘85… I’m a space fighter.  It’s nice, though… things are pretty calm recently. I’ve been catching up on my stories." # @t_shiromi567.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wow... There are all kinds of people in this crazy world.)" # @t_shiromi568.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "You know..." # @t_shiromi569.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby
    extend " This race is very important to me." # @t_shiromi569.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh?" # @t_shiromi570.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "I've promised to go on a trip... But only if SHE wins this race." # @t_shiromi571.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "(Whoa whoa... Hold on.)" # @t_shiromi572.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby
    t_ch_toby "But I'm a little nervous about it... I'm not used to just... Doing something." # @t_shiromi573.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "I prefer to have a plan. It’s important to always have a battle plan!" # @t_shiromi574.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "You're talking about … like… space battle?" # @t_shiromi575.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "Yeah! Well, not just space battles." # @t_shiromi576.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "It’s good to have an idea of what you’re going to do, but sometimes… There’s more to life than that, right? It's more than just preparing for every possible contingency." # @t_shiromi577.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby
    t_ch_toby "True... But I don’t know! I’m still nervous about it. Maybe I watch too much TV! But aliens are real, so anything could be! I just don’t know if SHE would understand my concerns… she’s somewhere between confident and impetuous, y’know?" # @t_shiromi578.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin ".... We are talking about Hiromi, right?" # @t_shiromi579.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "Yup!" # @t_shiromi580.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_cheering as toby
    t_ch_toby "WAIT, how do you know her name?!" # @t_shiromi581.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I've been hanging out with her at Auto Shop. Although she called you Kissy…" # @t_shiromi582.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby
    t_ch_toby "She’s the only one who does." # @t_shiromi583.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_cheering as toby
    t_ch_toby "OH! You must be the new pal she was talking about!" # @t_shiromi584.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin_blush as cousin
    t_ch_cousin "(Did she call me that?! Gosh... I'm flattered.)" # @t_shiromi585.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby
    t_ch_toby "She's been really happy lately. Usually it's just me and her, and she doesn't complain, but still... I'm so glad she's made a friend!" # @t_shiromi586.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "I used to think Hiromi was a little morose, but that's not her at all. She's just..." # @t_shiromi587.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " very uncomplicated." # @t_shiromi587.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I was always overthinking, trying to decipher what angle she's coming from..." # @t_shiromi587.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " but the truth is, she always takes the shortest path between two points." # @t_shiromi587.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I bet the neurons in her brain are all like little roads, going the shortest distance from point A to point B." # @t_shiromi587.04 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "I've been trying to pick it up from her... It helps me keep focused too... to simplify my thinking and concentrate on the important things." # @t_shiromi588.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "And the most important thing right now is this trip we’re planning!" # @t_shiromi589.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Toby... You should just tell her how you feel. Tell her exactly what's on your mind. If you're nervous... It doesn't hurt to let her know. And likewise… tell her to be clear about her expectations as well." # @t_shiromi590.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby
    t_ch_toby "I know... But she's so cool. Like a lone wolf! Or a pterodactyl!" # @t_shiromi591.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "Sometimes it's hard to tell if she cares. I mean, I know she does... But we're not very similar that way." # @t_shiromi592.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "I can't stop telling people what I'm thinking. Even complete strangers!" # @t_shiromi593.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_sad as cousin
    t_ch_cousin "(Tell me about it..." # @t_shiromi594.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified as cousin
    extend " I've known you for 10 minutes and I already know more about you than Hiromi!)" # @t_shiromi594.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "I think it's just how she is. She's very content with the few things she has... You, her motorcyle, and her dream." # @t_shiromi595.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "If she didn't care, she probably wouldn't even hang around... Y'know?" # @t_shiromi596.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "You... You think so?" # @t_shiromi597.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I do." # @t_shiromi598.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "Hmmmm...." # @t_shiromi599.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby
    show i_cousin_energetic_neutral as cousin
    extend " ......OH!" # @t_shiromi599.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "They're on their final approach! But I can't see who's up front." # @t_shiromi5100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It's a pink and blue streak..." # @t_shiromi5101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Only ONE racer could possibly be that pink.)" # @t_shiromi5101.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_announcer "And the winner is... HIROMI TENGENJI!" # @t_shiromi5102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_cheering as toby
    show i_cousin_energetic_laugh as cousin
    t_ch_toby "[slot_playerName]... SHE WON! SHE WON!!!!!!!!" # @t_shiromi5103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "AHHHHHHHHH!" # @t_shiromi5104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_laugh as cousin
    stop music fadeout 1.0
    t_ch_cousin "AHHHHHHHHHHHH!" # @t_shiromi5105.00 self.block='Last'
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 1 alpha 1.0
    show i_tobi_stand_cheering as toby:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_cousin_energetic_laugh as cousin:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    $ AudioEvent('music', 1.0, 1.0)
    show i_sw_black as curtain zorder 9
    t_ch_cousin "(After that... We headed back to the garage.)" # @t_shiromi5106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I can't believe I ran into Hiromi's partner." # @t_shiromi5107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " What a small world.)" # @t_shiromi5107.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 1 alpha 0.0
    show i_bg_shopclass as bg
    show i_cousin_energetic_laugh as cousin:
        # ShowWithAtl
        linear 0.5 alpha 0.0
        # ShowWithAtl
        linear 0.5 xpos -0.3 
    show i_tobi_stand_sweetsmile as toby:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
        # ShowWithAtl
        linear 0.5 alpha 1.0
    extend "{w=1.0}{nw}"
    t_ch_toby "Hiromi!" # @t_shiromi5108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby:
        # ShowWithAtl
        linear .75 alpha 1.0
    show i_hiromi_stand_smile_blush as hiromi
    extend "{w=0.75}{nw}"
    t_ch_hiromi "Oh, hey Kissy. Did you see?" # @t_shiromi5109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "I saw!" # @t_shiromi5110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby
    t_ch_toby "And look who I found!" # @t_shiromi5111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby:
        # ShowWithAtl
        linear .5 xpos 0.6 
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear .5 xpos 0.8 
    show i_cousin_default_grin as cousin:
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear .3 xpos 0.25 
    extend "{w=0.5}{nw}"
    t_ch_hiromi "........ ?" # @t_shiromi5112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_akimbo_serious as hiromi
    t_ch_hiromi "Whoa. Hey kid." # @t_shiromi5113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_stand_serious as hiromi
    extend " Do you guys know each other?" # @t_shiromi5113.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "We do now!" # @t_shiromi5114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin:
        # ShowWithAtl
        linear .3 xpos 0.15 
    extend "{w=0.3}{nw}"
    t_ch_cousin "Actually... I'll catch up with you in a minute. I think Toby has some things to say to you." # @t_shiromi5115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby:
        # ShowWithAtl
        linear .5 xpos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_toby "........................" # @t_shiromi5116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_akimbo_serious as hiromi
    t_ch_hiromi "........... Toby? What's up?" # @t_shiromi5117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 0.5 xpos -0.38 
    extend "{w=0.5}{nw}"
    t_ch_toby "Hiromi.........." # @t_shiromi5118.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 0.5 alpha 1.0
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
        # ShowWithAtl
        linear 3 xpos 0.2 
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear .5 xpos 0.9 
    show i_tobi_stand_grin as toby:
        # ShowWithAtl
        linear .5 xpos 0.8 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear .5 xpos 0.7 
        # ShowWithAtl
        linear 0.5 xzoom -1.0 
    extend "{w=3.0}{nw}"
    t_ch_pacman "BE TRUE TO YOURSELF...." # @t_shiromi5119.00 self.block='Last'
    stop sound
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 3 xpos -0.38 
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear .5 xpos 0.85 
    show i_tobi_stand_grin as toby:
        # ShowWithAtl
        linear .5 xpos 0.55 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear .5 xpos 0.23 
        # ShowWithAtl
        linear 0.5 xzoom 1.0 
    extend "{w=3.0}{nw}"
    t_ch_cousin "He's right Toby. Tell Hiromi how you feel." # @t_shiromi5120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_straight_blush as hiromi
    t_ch_hiromi "Kissy..." # @t_shiromi5121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "Hiromi... I believed in you today, and I'll totally believe in you..." # @t_shiromi5122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby
    extend " Forever." # @t_shiromi5122.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "But... I want to be honest with you. I'm a little nervous about this trip." # @t_shiromi5123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_stand_straight_blush as hiromi
    t_ch_hiromi "......................" # @t_shiromi5124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby
    t_ch_toby "Hiromi?" # @t_shiromi5125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_smile_blush as hiromi
    t_ch_hiromi "........ I know. I got the prize money... But we should wait a little longer. Let's save up some more money, lay down some plans." # @t_shiromi5126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby
    t_ch_toby "!! Really?" # @t_shiromi5127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_stand_smile_blush as hiromi
    t_ch_hiromi "Yeah. You're right. I should consider your feelings. We can't wait around forever, but this feels like the right thing to do." # @t_shiromi5128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "Hiromi..." # @t_shiromi5129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_smile_blush as hiromi
    t_ch_hiromi "I wouldn't leave you hangin'." # @t_shiromi5130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_sweetsmile as toby zorder 3:
        # ShowWithAtl
        linear .3 xpos 0.62 
    extend "{w=0.3}{nw}"
    t_ch_toby "Thanks." # @t_shiromi5131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_serious as hiromi
    t_ch_toby "Phew... I'm gonna head home. It's been a long day, and all that cheering tuckered me out." # @t_shiromi5132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby:
        # ShowWithAtl
        linear .5 xpos 0.43 
    extend "{w=0.5}{nw}"
    t_ch_toby "[slot_playerName]..." # @t_shiromi5133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(AH! She kissed me on the cheek!)" # @t_shiromi5134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_toby "Thanks for the talk." # @t_shiromi5135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_tobi_stand_grin as toby:
        # ShowWithAtl
        linear .5 alpha 0.0
    $ renpy.pause(0.5, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear .5 xpos 0.3 
    show i_hiromi_crossed_serious as hiromi:
        # ShowWithAtl
        linear .5 xpos 0.7 
    extend "{w=0.5}{nw}"
    t_ch_hiromi "........." # @t_shiromi5136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Sorry if I intruded..." # @t_shiromi5137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "..............." # @t_shiromi5138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "What? Spit it out." # @t_shiromi5139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_crossed_smile as hiromi
    t_ch_hiromi "It can't be fun to be between two people like that." # @t_shiromi5140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "Eh... What're friends for?" # @t_shiromi5141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_hiromi "................." # @t_shiromi5142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_hiromi_akimbo_smile as hiromi
    t_ch_hiromi "Thanks, kiddo." # @t_shiromi5143.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_2f', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_hiromi5__2f:
        # <NHSceneChange NHSceneChange {'name': '_2f', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5