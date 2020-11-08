# <Scene {'id': 's_hiromi1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_hiromi1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_hiromi1"
    $ renpy.pause(1)
    # <Scene {'id': 's_hiromi1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/upbeat_half.ogg" loop
    show i_bg_shopclass as bg zorder 0 at default
    show i_prop_hiromi_bike as bike zorder 1:
        default
        xpos 0.2 
        ypos 0.85 
        xzoom -1.0 
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_sw_black as darkness zorder 2:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 3:
        default
        xpos 0.7 
        xzoom -1.0 
    show i_hiromi_tool_serious as hiromi zorder 2:
        default
        xpos 0.3 
        alpha 0.0
    t_ch_cousin "(Oh, I guess I got here ahead of her.)" # @t_shiromi112.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wow... Look at this bike! I've never seen anything like it...)" # @t_shiromi113.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(It's very unusual..." # @t_shiromi114.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And it seems like it'd take a lot of skill to ride it." # @t_shiromi114.01 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There are way more buttons on the display than one would expect.)" # @t_shiromi114.02 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It looks so cool..." # @t_shiromi115.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    show i_hiromi_tool_serious as hiromi:
        # FadeEvent
        linear 0.5 alpha 1.0
    extend "{w=0.5}{nw}"
    t_ch_hiromi "...................." # @t_shiromi116.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(She's just... Staring at me." # @t_shiromi117.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    extend " This is kind of uncomfortable." # @t_shiromi117.01 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " Her gaze is really intense.)" # @t_shiromi117.02 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_hiromi ".........Oh. It's you." # @t_shiromi118.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(That's it?!)" # @t_shiromi119.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "Yup... Hello." # @t_shiromi120.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "Mind if I work?" # @t_shiromi121.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Conversation over, just like that?!)" # @t_shiromi122.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(Gosh, that wrench she's holding is really big... With her personality, maybe I better not push her.)" # @t_shiromi123.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(She's very abrupt. To tell the truth, I don't exactly find her to be rude..." # @t_shiromi124.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just a little distant.)" # @t_shiromi124.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Her social skills could definitely use some work.)" # @t_shiromi125.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But she's basically a stranger... I probably shouldn't say anything.)" # @t_shiromi126.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_hiromi "Hey, kid... you got a dream?" # @t_shiromi127.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(SO PERSONAL ALL OF A SUDDEN?!)" # @t_shiromi128.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "N-no....... Not really." # @t_shiromi129.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_stand_serious as hiromi
    show i_cousin_exhausted_neutral as cousin
    t_ch_hiromi "It's okay. You'll figure it out." # @t_shiromi130.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "I definitely have one." # @t_shiromi131.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "..........................." # @t_shiromi132.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(She went quiet again?" # @t_shiromi133.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    extend " IS SHE GOING TO LEAVE THE CONVERSATION THERE?!)" # @t_shiromi133.01 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Should I ask? But maybe I'd be prying..." # @t_shiromi134.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But I'm so curious." # @t_shiromi134.01 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Sigh.)" # @t_shiromi134.02 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I'm gonna do it." # @t_shiromi135.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I'm gonna ask..." # @t_shiromi135.01 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Right now..." # @t_shiromi135.02 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ... Just gotta wait for that perfect moment........)" # @t_shiromi135.03 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "......................." # @t_shiromi136.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_crossed_serious as hiromi
    t_ch_hiromi "I saw you checking her out." # @t_shiromi137.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "I WOULD NEVER-- wait what?" # @t_shiromi138.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "My bike." # @t_shiromi139.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You like her?" # @t_shiromi139.01 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Yeah. It's... Unlike any bike I've ever seen." # @t_shiromi140.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I wasn't even sure it was a motorcyle at first." # @t_shiromi140.01 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "Yeah... When I first started riding, it was on hogs and sports bikes." # @t_shiromi141.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "But at some point I started doing stunts..." # @t_shiromi142.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_hiromi "And then I began test-driving prototypes." # @t_shiromi143.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Wow... That's really intense." # @t_shiromi144.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "........" # @t_shiromi145.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Wait, Hiromi... If you're in high school now... Just when did you start riding?!" # @t_shiromi146.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi ".................." # @t_shiromi147.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Somehow that's answer enough...)" # @t_shiromi148.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Wait… how old are you?" # @t_shiromi149.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "19. I was held back a year." # @t_shiromi150.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "When I came to Namco High, my bike was broken." # @t_shiromi151.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "I can do basic maintenance, but the problem was too complicated... Dr. Tomari helped me fix it. I owe him one." # @t_shiromi152.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "Anyway... Ever since then, he's been helping me calibrate it." # @t_shiromi153.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Calibrate?" # @t_shiromi154.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_hiromi "Yeah. For racing. That's why I'm in detention." # @t_shiromi155.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_akimbo_serious as hiromi
    t_ch_hiromi "I was street racing to get the data he needed." # @t_shiromi156.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Street racing? That sounds really cool... And a little dangerous.)" # @t_shiromi157.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "You also think I'm a troublemaker, huh?" # @t_shiromi158.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "I get a lot of that from people with normal jobs." # @t_shiromi159.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don't think they understand me." # @t_shiromi159.01 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(You definitely don't make it easy for people to understand you... )" # @t_shiromi160.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Honestly... I was just thinking that it sounded really cool. And kind of dangerous. Which is also kind of cool." # @t_shiromi161.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_stand_serious as hiromi
    t_ch_hiromi "Hmph." # @t_shiromi162.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin ".......um... So...." # @t_shiromi163.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(C'mon [slot_playerName]... Think of something to say.)" # @t_shiromi164.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "You got a.... Favorite food?" # @t_shiromi165.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "Beef jerky." # @t_shiromi166.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(..... Just a one-word answer, huh... )" # @t_shiromi167.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What's your, uh... Favorite subject?" # @t_shiromi168.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_akimbo_serious as hiromi
    t_ch_hiromi "Physics." # @t_shiromi169.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Favorite play?" # @t_shiromi170.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "Twelfth Night." # @t_shiromi171.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Favorite kind of music?" # @t_shiromi172.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "Jazz." # @t_shiromi173.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "....favorite color......." # @t_shiromi174.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_crossed_straight_blush as hiromi
    t_ch_hiromi "....yellow........." # @t_shiromi175.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_crossed_serious as hiromi
    t_ch_cousin "...............favorite animal................" # @t_shiromi176.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "Human." # @t_shiromi177.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "......" # @t_shiromi178.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "................." # @t_shiromi179.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "......................" # @t_shiromi180.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi ".............................." # @t_shiromi181.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "I gotta go." # @t_shiromi182.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_hiromi "I have to pick up my … data collection partner... and collect some more data." # @t_shiromi183.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(...partner..................)" # @t_shiromi184.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Wait... I thought you weren't supposed to ride your bike. Didn't they take your keys?" # @t_shiromi185.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "I always keep a few spares." # @t_shiromi186.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_crossed_smile as hiromi
    extend " And I'm not riding my bike... I'm 'collecting data'." # @t_shiromi186.01 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_crossed_serious as hiromi
    t_ch_hiromi "I'll see you when I see you." # @t_shiromi187.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_crossed_serious as hiromi:
        # FadeEvent
        linear 0.5 alpha 0.0
    show i_prop_hiromi_bike as bike:
        # FadeEvent
        linear 0.5 alpha 0.0
    play sound "sfx/motorcycleaway.ogg"
    extend "{w=0.5}{nw}"
    t_ch_cousin "(When she says 'collecting data', she definitely means... )" # @t_shiromi188.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as darkness:
        # ShowWithAtl
        linear 0.5 alpha 0.5
    extend "{w=0.5}{nw}"
    t_ch_cousin "(... Of course... )" # @t_shiromi189.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear .5 xpos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_cousin "(Hiromi's definitely not a talker..." # @t_shiromi190.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But once you get her going she's very direct.)" # @t_shiromi190.01 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Sometimes that makes her a little obtuse..." # @t_shiromi191.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(That bluntness is a little refreshing.)" # @t_shiromi192.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Still... I wonder what she meant about her dream.)" # @t_shiromi193.00 self.block='Last'
    # <NHSceneChange {'name': '_1a', 'scene': 's_day2'} NHSceneChange ''>
    label s_hiromi1__1a:
        # <NHSceneChange {'name': '_1a', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2