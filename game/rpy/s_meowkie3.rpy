# <Scene {'id': 's_meowkie3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_meowkie3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_meowkie3"
    $ renpy.pause(1)
    # <Scene {'id': 's_meowkie3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/school.ogg" loop
    show i_bg_classroom_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_nidia_notepad_happy as nidia zorder 3:
        default
        xpos 0.75 
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.25 
    show i_digdug_left as digdug zorder 2:
        default
        xpos 1.35 
        alpha 0.0
    show i_bluemax_stand_smile as bluemax zorder 2:
        default
        xpos 0.75 
        alpha 0.0
    show i_meowkie_normal_happy_badge as meowkie zorder 2:
        default
        xpos 0.75 
        xzoom -1.0 
    t_ch_cousin "Sure, Meowkie!" # @t_smeowkie312.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That sounds really fun, actually." # @t_smeowkie312.01 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "R-really? Wow... Boss, that’s great!" # @t_smeowkie313.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Y’know... you’re bein’ so nice to me an all..." # @t_smeowkie314.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I just wanna say..." # @t_smeowkie314.01 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I’m real glad you wanna spend time with someone like me, Boss." # @t_smeowkie315.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "It’s nothing, Meowkie, really!" # @t_smeowkie316.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " After all... I want to." # @t_smeowkie316.01 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "…" # @t_smeowkie317.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    extend " …" # @t_smeowkie317.01 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(When she gets quiet like that... I’m not sure what to do!)" # @t_smeowkie318.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy_badge as meowkie
    t_ch_meowkie "Okay, Boss! This is gonna be a great day!" # @t_smeowkie319.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You just wait here a minute..." # @t_smeowkie319.01 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    extend " I-if that’s okay." # @t_smeowkie319.02 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "I’ll go get some tasty snacks for us first!" # @t_smeowkie320.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The cafeteria has tuna fish sandwiches today." # @t_smeowkie320.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " AND I brought some tuna snacks from home!" # @t_smeowkie320.02 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(This girl... Really likes tuna...)" # @t_smeowkie321.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    t_ch_meowkie "Uh... Th-that is..." # @t_smeowkie322.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I know tuna might not be… your VERY favorite..." # @t_smeowkie322.01 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "But it ain’t like you HATE it... right?" # @t_smeowkie323.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Actually, the real truth is..." # @t_smeowkie324.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " I really do hate tuna!" # @t_smeowkie324.01 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But what kind of monster would I be to say no to that face?!)" # @t_smeowkie325.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "Tuna... Tuna’s great!" # @t_smeowkie326.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy_badge as meowkie
    t_ch_meowkie "...I knew it!" # @t_smeowkie327.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I knew you were a tuna fan..." # @t_smeowkie327.01 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s no way someone as nice as you wouldn’t be!" # @t_smeowkie327.02 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(“Someone as nice as me”? There’s no moral qualities that come with liking tuna…" # @t_smeowkie328.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " At least I don’t think there are..)" # @t_smeowkie328.01 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "You just sit tight, Boss! I’ll be right back with our snacks!" # @t_smeowkie329.00 self.block='Last'
    show i_meowkie_normal_happy_badge as meowkie:
        # ShowWithAtl
        linear .5 alpha 0.0
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(The prospect of spending the day with Meowkie..." # @t_smeowkie330.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " ...I’m really excited!" # @t_smeowkie330.01 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Hmm, what’s that? Did I hear her name?" # @t_smeowkie331.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It sounds like those other kids over there are talking about her." # @t_smeowkie332.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I know eavesdropping is wrong, but-" # @t_smeowkie332.01 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_trio_preps as students:
        default
        alpha 1.0
        xpos 1.38 
    extend " I can’t help but listen in!)" # @t_smeowkie332.02 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        ease_expo .33 xpos 0.1 
    show i_trio_preps as students:
        # ShowWithAtl
        ease_expo .5 xpos 0.77 
    $ renpy.pause(0.5) # TimedPause
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student1 "That Meowkie..." # @t_smeowkie333.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don’t even get why they let her go to this school." # @t_smeowkie333.01 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Just because her parents moved to this district so she could go to Namco High..." # @t_smeowkie333.02 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student1 "That shouldn’t mean anything, should it?" # @t_smeowkie334.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student2 "I know! This place is for, like, good guys." # @t_smeowkie335.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student2 "Isn’t it dangerous to let someone like Meowkie in?" # @t_smeowkie336.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " No matter where she goes to school..." # @t_smeowkie336.01 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She’s still a henchman for a bad guy!" # @t_smeowkie336.02 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(What? No she’s not!" # @t_smeowkie337.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How could anyone possibly think that about Meowkie?!" # @t_smeowkie337.01 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Have they even MET her?!)" # @t_smeowkie337.02 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student3 "Yeah, the Meowkie family is like, totally villainous!" # @t_smeowkie338.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They used to work for that Big Cat and everything!" # @t_smeowkie338.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student1 "It’s totally unfair that we have to go to school with some evil goon!" # @t_smeowkie339.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What happens when she finally turns on us?" # @t_smeowkie339.01 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Meowkie’s not evil!" # @t_smeowkie340.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Her family’s not that bad either!" # @t_smeowkie340.01 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If they really did move just so they could send her to Namco High..." # @t_smeowkie341.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That means they’re trying really hard to give her a better life!)" # @t_smeowkie341.01 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student2 "The ONLY reason she’s not kicked out yet..." # @t_smeowkie342.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Is because that weird teacher King likes her." # @t_smeowkie342.01 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student3 "Oh, I get it." # @t_smeowkie343.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student3 "It’s a cat thing." # @t_smeowkie344.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(I can’t stand hearing this!" # @t_smeowkie347.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How could they say that?!" # @t_smeowkie347.01 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If King really did give Meowkie special treatment, he’d let her out of detention!" # @t_smeowkie348.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Although..." # @t_smeowkie349.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Now that I think about it..." # @t_smeowkie349.01 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I never found out why she was in detention in the first place." # @t_smeowkie350.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But Meowkie couldn’t REALLY have done something bad..." # @t_smeowkie351.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...could she have?)" # @t_smeowkie351.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student1 "She actually tried to get me in trouble, you know!" # @t_smeowkie352.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    extend " With that phony Hall Monitor act." # @t_smeowkie352.01 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student1 "Just because I was writing on the bathroom walls..." # @t_smeowkie353.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She said it was “vandalism” or something." # @t_smeowkie353.01 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student1 "I thought that was pretty rich, coming from an evil goon who like, probably does stuff like that all the time!" # @t_smeowkie354.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student2 "No way!" # @t_smeowkie355.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What did you do?!" # @t_smeowkie355.01 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student1 "I blamed it on her, of course!" # @t_smeowkie356.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She probably deserved to get detention for SOMETHING..." # @t_smeowkie356.01 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student1 "Serves her right, anyway!" # @t_smeowkie357.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Someone like HER, trying to get ME in trouble?" # @t_smeowkie357.01 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Yeah, right!" # @t_smeowkie357.02 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_student3 "Haha! Nice one!" # @t_smeowkie358.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(..." # @t_smeowkie359.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    extend " So that’s it..." # @t_smeowkie359.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That’s why Meowkie was in detention." # @t_smeowkie360.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It wasn’t even her fault..." # @t_smeowkie361.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But the other kids think she’s bad, so they blame stuff on her." # @t_smeowkie361.01 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I can’t believe it..." # @t_smeowkie362.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Someone as sweet as Meowkie could never deserve that." # @t_smeowkie363.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " I’ve got to say something..." # @t_smeowkie363.01 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ve got to stick up for her!" # @t_smeowkie363.02 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_happy_badge as meowkie:
        # ShowWithAtl
        linear 0.5 xpos 1.3 
        # ShowWithAtl
        linear 0.5 alpha 1.0
    show i_cousin_default_surprised as cousin
    extend "{w=0.5}{nw}"
    t_ch_cousin "I’ve got to-)" # @t_smeowkie364.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_trio_preps as students:
        # ShowWithAtl
        linear .5 alpha 0.0
    show i_meowkie_normal_happy_badge as meowkie:
        # ShowWithAtl
        ease_expo .33 xpos 0.75 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        pause 0.15 
        ease_expo .33 xpos 0.25 
    $ renpy.pause(0.5) # TimedPause
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Nyaa! Hiya boss, I’m back!" # @t_smeowkie365.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "They had plenty of tuna, but..." # @t_smeowkie366.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Since I knew tuna might not be your favorite..." # @t_smeowkie366.01 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I got some salmon for ya too!" # @t_smeowkie367.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    extend " It’s kinda unorthodox, but what can I say?" # @t_smeowkie367.01 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You bring out a crazy side of me, Boss!" # @t_smeowkie367.02 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(For someone who likes tuna so much, that must seem like a really radical act." # @t_smeowkie368.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I wanted to say something to those other kids, but..." # @t_smeowkie369.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It probably wouldn’t do any good to make a scene in front of poor Meowkie." # @t_smeowkie369.01 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It would just hurt her feelings..." # @t_smeowkie369.02 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But I want to stand up for her." # @t_smeowkie370.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What’s the right thing to do?)" # @t_smeowkie370.01 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_normal_badge as meowkie
    t_ch_meowkie "Well Boss? Whaddya say?" # @t_smeowkie371.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "...Thanks, Meowkie." # @t_smeowkie372.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s really nice of you." # @t_smeowkie372.01 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Come on, let’s go on patrol..." # @t_smeowkie373.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Together!" # @t_smeowkie373.01 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_grin_badge as meowkie
    t_ch_meowkie "...Boss!" # @t_smeowkie374.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(That’s right... the best thing to do is..." # @t_smeowkie375.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " To go with her proudly..." # @t_smeowkie375.01 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And show the others that I don’t care where she comes from.)" # @t_smeowkie375.02 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_hallway_a as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_a', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_1r'} SettingChange ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_smeowkie376.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Hey Meowkie?" # @t_smeowkie376.01 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Do you mind if I ask you something?" # @t_smeowkie377.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "Not at all, Boss!" # @t_smeowkie378.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…Even if it’s kinda..." # @t_smeowkie379.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    extend " Personal?" # @t_smeowkie379.01 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    t_ch_meowkie "Nyaa... Boss... wh-what do you mean??" # @t_smeowkie380.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Erk! Sorry! I didn’t mean like that..." # @t_smeowkie381.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, I was just kinda curious..." # @t_smeowkie382.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Do the other kids here ever treat you any different?" # @t_smeowkie383.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_frown_badge as meowkie
    t_ch_meowkie "… Oh..." # @t_smeowkie384.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(There she goes, getting quiet again...)" # @t_smeowkie385.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    t_ch_meowkie "Haha, of course they do, Boss!" # @t_smeowkie386.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m a cat after all!" # @t_smeowkie386.01 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Meowkie, that’s not what I-" # @t_smeowkie387.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I don’t take it personal or nothin’, though!" # @t_smeowkie388.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    extend " After all, some people can’t help bein’ allergic!" # @t_smeowkie388.01 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(She’s being weird and dodging my questions." # @t_smeowkie389.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But I can tell she knows exactly what I’m talking about." # @t_smeowkie389.01 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "By acting this way, she’s telling me she doesn’t want to talk about it." # @t_smeowkie390.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I should really respect that, and not push it right now." # @t_smeowkie390.01 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But... maybe she needs me to push it?" # @t_smeowkie391.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What should I do?)" # @t_smeowkie391.01 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie, cut the innocent act." # @t_smeowkie392.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I heard what the other kids say about you in detention!" # @t_smeowkie392.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "They say mean stuff about you, they pin their rule breaking on you." # @t_smeowkie393.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How can you put up with it??" # @t_smeowkie393.01 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown_badge as meowkie
    t_ch_meowkie "…." # @t_smeowkie394.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Don’t be a coward! You should stand up for yourself!" # @t_smeowkie395.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If you keep letting it happen, it’s as much your fault as theirs!" # @t_smeowkie396.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie397.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...I dunno what you’re talkin about, Boss." # @t_smeowkie397.01 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie..." # @t_smeowkie398.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(She’s speaking very quietly. But somehow, I still get the sense..." # @t_smeowkie399.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " that she’s furious.)" # @t_smeowkie399.01 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Please…" # @t_smeowkie3100.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I don’t mean to be demanding or nothing…" # @t_smeowkie3101.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "But let’s not talk about that stuff." # @t_smeowkie3102.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Okay?" # @t_smeowkie3103.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "...I’m sorry Meowkie… I just wanted to help…" # @t_smeowkie3104.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Are you sure you don’t wanna talk about it?" # @t_smeowkie3104.01 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…Yeah." # @t_smeowkie3105.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I mean it." # @t_smeowkie3106.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I don’t wanna say nothin’..." # @t_smeowkie3107.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Out of… emotion." # @t_smeowkie3108.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_alert_badge as meowkie
    t_ch_meowkie "Ya know?" # @t_smeowkie3109.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "…Meowkie, I’m sorry..." # @t_smeowkie3110.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie3111.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I guess I have no choice..." # @t_smeowkie3112.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I shouldn’t have called her a coward..." # @t_smeowkie3112.01 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I shouldn’t have blamed it on her." # @t_smeowkie3112.02 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s just so unfair that anyone would be so mean to her..." # @t_smeowkie3113.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But if she’s this angry... I should really just let it go.)" # @t_smeowkie3114.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "…Y-yeah... People can’t help being allergic." # @t_smeowkie3115.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie3116.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_smeowkie3117.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(This is a little awkward." # @t_smeowkie3118.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Does she know what I’m thinking?)" # @t_smeowkie3118.01 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie, I’m sorry for getting too personal." # @t_smeowkie3122.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I understand if you’re angry at me." # @t_smeowkie3123.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Nya, wh-what are you talking about, Boss?" # @t_smeowkie3124.00 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_normal_badge as meowkie
    t_ch_meowkie "I ain’t mad at you." # @t_smeowkie3125.00 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Are you sure? You seemed pretty upset there." # @t_smeowkie3126.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Oh, no no. No way!" # @t_smeowkie3127.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I don’t get angry, boss." # @t_smeowkie3128.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Not at you, or anyone!" # @t_smeowkie3128.01 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I just… don’t see the point, ya know?" # @t_smeowkie3129.00 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " After all, everyone’s trying their best." # @t_smeowkie3129.01 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Wait, what are you saying?" # @t_smeowkie3130.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You don’t get angry… ever?" # @t_smeowkie3130.01 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    extend " At anyone or anything?" # @t_smeowkie3130.02 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_grin_badge as meowkie
    t_ch_meowkie "Nope!" # @t_smeowkie3131.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I just don’t see the point, you know?" # @t_smeowkie3132.00 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It don’t exactly accomplish much." # @t_smeowkie3132.01 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Gettin’ angry... is just kinda silly!" # @t_smeowkie3133.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie
    extend " Ha ha…" # @t_smeowkie3133.01 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Wow. I never would have guessed Meowkie was in this much denial…" # @t_smeowkie3134.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She’s a little more… messed up… than I expected her to be." # @t_smeowkie3134.01 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Not that I hold it against her though…" # @t_smeowkie3135.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Poor Meowkie…)" # @t_smeowkie3136.00 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_alert_badge as meowkie
    t_ch_meowkie "Oh! Around the corner!" # @t_smeowkie3137.00 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "What’s that? Are your Hall Monitor senses tingling?" # @t_smeowkie3138.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Thank goodness, a way to change the subject.)" # @t_smeowkie3138.01 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie
    t_ch_meowkie "Yeah! Just over there! Let’s go, Boss!" # @t_smeowkie3139.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie:
        # ShowWithAtl
        linear 0.333 xpos 0.5 
    extend "{w=0.333}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie:
        xzoom 1.0 
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    show i_meowkie_akimbo_alert_badge as meowkie
    t_ch_cousin "(What the- she just... grabbed my hand..." # @t_smeowkie3140.00 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh man..." # @t_smeowkie3141.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Is this her way of showing me she’s not upset that I tried to bring that stuff up?" # @t_smeowkie3141.01 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Or... does it mean something more…" # @t_smeowkie3142.00 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "Wait, her claws aren’t gonna pop out while we’re holding hands, right?!)" # @t_smeowkie3143.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_flustered as bluemax:
        # ShowWithAtl
        linear 0.5 xpos 0.75 
        # ShowWithAtl
        linear 0.333 alpha 1.0
    show i_nidia_resolute_angry as nidia:
        # ShowWithAtl
        linear 0.5 xpos 0.55 
        # ShowWithAtl
        linear 0.333 alpha 1.0
    show i_cousin_energetic_mortified as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.1 
    show i_meowkie_akimbo_alert_badge as meowkie:
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    extend "{w=0.5}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Hey, stop that! Get away from me!" # @t_smeowkie3144.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "I need to hit you with my dragon amulet!" # @t_smeowkie3145.00 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Stop squirming!" # @t_smeowkie3145.01 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Noooooo!" # @t_smeowkie3146.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Yikes, what’s the story here?)" # @t_smeowkie3147.00 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_alert_badge as meowkie
    t_ch_meowkie "HALT, TROUBLEMAKERS!" # @t_smeowkie3148.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_surprised as nidia
    t_ch_nidia "Huh?? What’s the problem?" # @t_smeowkie3149.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Roughhousing in the hallways!" # @t_smeowkie3150.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We won’t allow it!" # @t_smeowkie3150.01 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Right, Boss?" # @t_smeowkie3150.02 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Er... y-yeah, that’s right!" # @t_smeowkie3151.00 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_angry as nidia
    t_ch_nidia "But I must! Destiny commands it!" # @t_smeowkie3152.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Would you defy destiny?" # @t_smeowkie3152.01 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_worried as bluemax
    t_ch_max "Help! She’s crazy!!" # @t_smeowkie3153.00 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Er... I don’t know about destiny... but..." # @t_smeowkie3154.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_forcedsmile_badge as meowkie
    t_ch_meowkie "I do know that dawdling and rough housing are, um, against the rules!" # @t_smeowkie3155.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_max "Oh, who am I kidding! You’re just that evil henchman cat girl..." # @t_smeowkie3156.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Nobody really listens to you!" # @t_smeowkie3156.01 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_flustered as bluemax
    extend " I’m a goner..." # @t_smeowkie3156.02 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_akimbo_frown_badge as meowkie
    t_ch_meowkie "…" # @t_smeowkie3157.00 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    extend " Even y-you think...That I’m..." # @t_smeowkie3157.01 self.block='Last'
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Hey!! What gives? She’s trying to help you!" # @t_smeowkie3158.00 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "An evil henchman? Is that so?" # @t_smeowkie3159.00 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "I’ve dealt with plenty like you in my time!" # @t_smeowkie3160.00 self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_angry as nidia
    t_ch_nidia "Stand aside! Don’t trifle with my destiny!" # @t_smeowkie3161.00 self.block='Last'
    # <ParallelEvent {'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown_badge as meowkie
    t_ch_meowkie "Oh...  I..." # @t_smeowkie3162.00 self.block='Last'
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Meowkie, say something!" # @t_smeowkie3163.00 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_forcedsmile_badge as meowkie
    t_ch_meowkie "…Heh heh..." # @t_smeowkie3164.00 self.block='Last'
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile_badge as meowkie
    extend " It’s okay, Boss..." # @t_smeowkie3164.01 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown_badge as meowkie
    t_ch_cousin "(How is she not getting mad at what they’re saying?!)" # @t_smeowkie3165.00 self.block='Last'
    # <ParallelEvent {'name': 'digdugEnters'} ParallelEvent ''>
    label s_meowkie3_digdugEnters:
        # <ParallelEvent {'name': 'digdugEnters'} ParallelEvent ''>
        # <Events {} events ''>
        show i_bluemax_shock_shocked as bluemax:
            xzoom -1.0 
            # ShowWithAtl
            linear 0.333 xpos 0.5 
        show i_digdug_left as digdug:
            # ShowWithAtl
            linear 0.333 alpha 1.0
            # ShowWithAtl
            linear 0.333 xpos 0.9 
        show i_meowkie_normal_frown_badge as meowkie:
            # ShowWithAtl
            linear 0.333 xpos 0.23 
        show i_nidia_resolute_surprised as nidia:
            # ShowWithAtl
            linear 0.333 xpos 0.6 
        show i_cousin_default_surprised as cousin
        stop music fadeout 1.0
        extend "{w=0.333}{nw}"
        t_ch_digdug "What’s going on here?!" # @t_smeowkie3166.00 self.block='Last'
    # <ParallelEvent {'name': '_3r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_shocked as bluemax
    t_ch_max "AAHHH!" # @t_smeowkie3167.00 self.block='Last'
    # <ParallelEvent {'name': '_3s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "OH!" # @t_smeowkie3168.00 self.block='Last'
    # <ParallelEvent {'name': '_3t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Principal Dig Dug?!" # @t_smeowkie3169.00 self.block='Last'
    # <ParallelEvent {'name': '_3u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie3170.00 self.block='Last'
    # <ParallelEvent {'name': '_3v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "What’s this ruckus out here?" # @t_smeowkie3171.00 self.block='Last'
    # <ParallelEvent {'name': '_3w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Can someone please tell me what’s going on?!" # @t_smeowkie3171.01 self.block='Last'
    # <ParallelEvent {'name': '_3x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "…I was doing nothing wrong!" # @t_smeowkie3172.00 self.block='Last'
    # <ParallelEvent {'name': '_3y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_resolute_angry as nidia
    extend " This so-called “Hall Monitor” is standing in the way of my destiny!" # @t_smeowkie3172.01 self.block='Last'
    # <ParallelEvent {'name': '_3z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_shock_flustered as bluemax
    t_ch_max "I heard she’s evil! Her parents used to work for bad guys!" # @t_smeowkie3173.00 self.block='Last'
    # <ParallelEvent {'name': '_40'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Eek! Don’t let her start picking on me too!" # @t_smeowkie3173.01 self.block='Last'
    # <ParallelEvent {'name': '_41'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_nidia "She was making up reasons to get in my way!" # @t_smeowkie3174.00 self.block='Last'
    # <ParallelEvent {'name': '_42'} ParallelEvent ''>
    # <Events {} events ''>
    show i_nidia_akimbo_angry as nidia
    extend " It’s totally unacceptable! I have a quest to follow!" # @t_smeowkie3174.01 self.block='Last'
    # <ParallelEvent {'name': '_43'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie3175.00 self.block='Last'
    # <ParallelEvent {'name': '_44'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "H-hey! What?? That’s totally unfair!" # @t_smeowkie3176.00 self.block='Last'
    # <ParallelEvent {'name': '_45'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’m trying to argue, but everyone’s shouting over each other..." # @t_smeowkie3177.00 self.block='Last'
    # <ParallelEvent {'name': '_46'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Blaming everyone else besides themselves..." # @t_smeowkie3177.01 self.block='Last'
    # <ParallelEvent {'name': '_47'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Except for Meowkie, who’s just standing there." # @t_smeowkie3178.00 self.block='Last'
    # <ParallelEvent {'name': '_48'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What is she thinking right now?" # @t_smeowkie3179.00 self.block='Last'
    # <ParallelEvent {'name': '_49'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I wish she’d say something..." # @t_smeowkie3179.01 self.block='Last'
    # <ParallelEvent {'name': '_4A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Anything..." # @t_smeowkie3179.02 self.block='Last'
    # <ParallelEvent {'name': '_4B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But I probably wouldn’t even hear it over all this shouting.)" # @t_smeowkie3180.00 self.block='Last'
    # <ParallelEvent {'name': '_4C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    show i_bluemax_cower_shock as bluemax
    show i_nidia_resolute_surprised as nidia
    t_ch_digdug "That’s enough! BE QUIET!" # @t_smeowkie3181.00 self.block='Last'
    # <ParallelEvent {'name': '_4D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_cower_flustered as bluemax
    t_ch_digdug "I’ve heard quite enough." # @t_smeowkie3182.00 self.block='Last'
    # <ParallelEvent {'name': '_4E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I can’t sort out who’s right and who’s wrong." # @t_smeowkie3182.01 self.block='Last'
    # <ParallelEvent {'name': '_4F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "So just to be safe..." # @t_smeowkie3183.00 self.block='Last'
    # <ParallelEvent {'name': '_4G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "You’re ALL in trouble!" # @t_smeowkie3184.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.444 alpha 1.0
    $ renpy.pause(0.444)
    show i_bg_hallway_b as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_b', 'curtainActor': 'curtain', 'curtainFadeTime': '0.444', 'name': '_4H'} SettingChange ''>
    # <Events {} events ''>
    hide nidia
    hide bluemax
    hide digdug
    show i_cousin_exhausted_sad as cousin:
        # ActorEvent
        xpos 0.5 
    show i_meowkie_slouch_frown as meowkie:
        # ActorEvent
        xpos 1.4 
        xzoom -1.0 
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.444 alpha 0.0
    $ renpy.pause(0.444)
    # <ParallelEvent {'name': '_4I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Feels like I’ve been waiting here outside Principal Dig Dug’s office for a long time..." # @t_smeowkie3185.00 self.block='Last'
    # <ParallelEvent {'name': '_4J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He already talked to those other two, and they went on their way." # @t_smeowkie3185.01 self.block='Last'
    # <ParallelEvent {'name': '_4K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "He talked to me too, and I’m on thin ice..." # @t_smeowkie3186.00 self.block='Last'
    # <ParallelEvent {'name': '_4L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I better wait for Meowkie to be done, though." # @t_smeowkie3187.00 self.block='Last'
    # <ParallelEvent {'name': '_4M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s no way I’m leaving without her." # @t_smeowkie3187.01 self.block='Last'
    # <ParallelEvent {'name': '_4N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Poor Meowkie..." # @t_smeowkie3188.00 self.block='Last'
    # <ParallelEvent {'name': '_4O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I can’t believe everyone thinks so poorly of her...  Even people who are otherwise really nice, like Nidia and Blue Max.)" # @t_smeowkie3188.01 self.block='Last'
    # <ParallelEvent {'name': '_4P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But why won’t she say anything about it?!" # @t_smeowkie3189.00 self.block='Last'
    # <ParallelEvent {'name': '_4Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Oh... the door’s opening.)" # @t_smeowkie3190.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_4R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_frown as meowkie:
        # ShowWithAtl
        linear 0.333 xpos 0.7 
    show i_cousin_exhausted_surprised as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    extend "{w=0.333}{nw}"
    # Blank text event <TextEvent {'char': '', 'text': ''} TextEvent ''>
    # <ParallelEvent {'name': '_4S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Meowkie!" # @t_smeowkie3191.00 self.block='Last'
    # <ParallelEvent {'name': '_4T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " H-how’d it go?" # @t_smeowkie3191.01 self.block='Last'
    # <ParallelEvent {'name': '_4U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "O-oh... Fine, Boss..." # @t_smeowkie3192.00 self.block='Last'
    # <ParallelEvent {'name': '_4V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It was fine." # @t_smeowkie3192.01 self.block='Last'
    # <ParallelEvent {'name': '_4W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh, good." # @t_smeowkie3193.00 self.block='Last'
    # <ParallelEvent {'name': '_4X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Except... Principal Digdug..." # @t_smeowkie3194.00 self.block='Last'
    # <ParallelEvent {'name': '_4Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " He kinda..." # @t_smeowkie3194.01 self.block='Last'
    # <ParallelEvent {'name': '_4Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown as meowkie
    t_ch_meowkie "Took away my hall monitor badge." # @t_smeowkie3195.00 self.block='Last'
    # <ParallelEvent {'name': '_4a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "WHAT?!" # @t_smeowkie3196.00 self.block='Last'
    # <ParallelEvent {'name': '_4b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "How could he do that?!" # @t_smeowkie3197.00 self.block='Last'
    # <ParallelEvent {'name': '_4c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie3198.00 self.block='Last'
    # <ParallelEvent {'name': '_4d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " …" # @t_smeowkie3198.01 self.block='Last'
    # <ParallelEvent {'name': '_4e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Meowkie, please... talk to me." # @t_smeowkie3199.00 self.block='Last'
    # <ParallelEvent {'name': '_4f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie3200.00 self.block='Last'
    # <ParallelEvent {'name': '_4g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s okay, Boss... I understand." # @t_smeowkie3200.01 self.block='Last'
    # <ParallelEvent {'name': '_4h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "H-how does it look, after all..." # @t_smeowkie3201.00 self.block='Last'
    # <ParallelEvent {'name': '_4i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " To have a Hall Monitor who’s in detention all the time..." # @t_smeowkie3201.01 self.block='Last'
    # <ParallelEvent {'name': '_4j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "I... I’d probably do the same thing..." # @t_smeowkie3202.00 self.block='Last'
    # <ParallelEvent {'name': '_4k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_forcedsmile as meowkie
    extend " Ha ha..." # @t_smeowkie3202.01 self.block='Last'
    # <ParallelEvent {'name': '_4l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That badge meant so much to you!" # @t_smeowkie3203.00 self.block='Last'
    # <ParallelEvent {'name': '_4m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And no one deserves to have it more than you!" # @t_smeowkie3203.01 self.block='Last'
    # <ParallelEvent {'name': '_4n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " You didn’t even do anything to get in detention all those times!" # @t_smeowkie3203.02 self.block='Last'
    # <ParallelEvent {'name': '_4o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie, you told him that, right?" # @t_smeowkie3204.00 self.block='Last'
    # <ParallelEvent {'name': '_4p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " You told him it’s not your fault you keep getting in trouble?" # @t_smeowkie3204.01 self.block='Last'
    # <ParallelEvent {'name': '_4q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_frown as meowkie
    t_ch_meowkie "…" # @t_smeowkie3205.00 self.block='Last'
    # <ParallelEvent {'name': '_4r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " No way... I can’t do that." # @t_smeowkie3205.01 self.block='Last'
    # <ParallelEvent {'name': '_4s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "Those other students... They just didn’t want to get in trouble." # @t_smeowkie3206.00 self.block='Last'
    # <ParallelEvent {'name': '_4t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_meowkie "…" # @t_smeowkie3207.00 self.block='Last'
    # <ParallelEvent {'name': '_4u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_slouch_forcedsmile as meowkie
    extend " Who..." # @t_smeowkie3207.01 self.block='Last'
    # <ParallelEvent {'name': '_4v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_meowkie_normal_forcedsmile as meowkie
    t_ch_meowkie "Who can blame them?" # @t_smeowkie3208.00 self.block='Last'
    # <ParallelEvent {'name': '_4w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie..." # @t_smeowkie3209.00 self.block='Last'
    # <ParallelEvent {'name': '_4x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(She’s trying so hard to be happy and cheerful..." # @t_smeowkie3210.00 self.block='Last'
    # <ParallelEvent {'name': '_4y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    extend " But this time, it’s obvious... she’s crushed." # @t_smeowkie3210.01 self.block='Last'
    # <ParallelEvent {'name': '_4z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Meowkie, please let me help you..." # @t_smeowkie3211.00 self.block='Last'
    # <ParallelEvent {'name': '_50'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I hope you’ll talk to me soon.)" # @t_smeowkie3211.01 self.block='Last'
    # <NHSceneChange {'name': '_51', 'scene': 's_day4'} NHSceneChange ''>
    label s_meowkie3__51:
        # <NHSceneChange {'name': '_51', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4