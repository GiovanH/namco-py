# <Scene {'id': 's_richard1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_richard1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_richard1"
    $ renpy.pause(1)
    # <Scene {'id': 's_richard1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/upbeat_half.ogg" loop
    show i_bg_hallway_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_miller_aliens_halfgrin as miller zorder 2:
        default
        xpos 0.7 
        alpha 0.0
    t_ch_cousin "(Okay, so Richard’s first impression was…)" # @t_srichard121.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(Uh…)" # @t_srichard122.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Well, it was certainly an impression.)" # @t_srichard123.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (But the Culinary Club sounds like it’d be a fun way to reduce my detention.)" # @t_srichard123.01 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "(Maybe we’ll get to make cakes!)" # @t_srichard124.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Eh, probably start us on something simpler like cookies.)" # @t_srichard125.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But that’s okay too!)" # @t_srichard126.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_classroom_b as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_classroom_b', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_7'} SettingChange ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Wow, there’s so much food! It’s like a banquet. Is it like that in here EVERY DAY???)" # @t_srichard127.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_halfgrin as miller:
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_richard "And now for my finale!" # @t_srichard128.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Did Richard make all that food?)" # @t_srichard129.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_halfgrin as miller
    t_ch_richard "Ta-da!" # @t_srichard130.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(He…)" # @t_srichard131.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (He threw all of it in the trash?!?)" # @t_srichard131.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What’s going on in here?!)" # @t_srichard132.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_laugh as miller
    t_ch_richard "Ah, [slot_playerName]. Glad you could make it." # @t_srichard133.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "You seem awfully busy. I’ll come by later, okay?" # @t_srichard134.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_contemplative as miller
    t_ch_richard "No, no. This is a great opportunity to discern your strengths and weaknesses for my dossiers." # @t_srichard135.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Well, right now my weakness is for cake." # @t_srichard136.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_halfgrin as miller
    t_ch_richard "Cake, you say? Excellent timing. You can start on dessert while I complete the main course!" # @t_srichard137.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "You want me to bake a cake on my first day?!" # @t_srichard138.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_laugh as miller
    t_ch_richard "Oh! Haha, I’m sorry, [slot_playerName]." # @t_srichard139.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Sometimes I forget everyone else isn’t up to my speed." # @t_srichard140.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Even so! You can make us some cupcakes instead." # @t_srichard141.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Are those easier because they’re smaller?" # @t_srichard142.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_serious as miller
    t_ch_richard "No. Furthermore, that’s an absurd conclusion to come to. You’re really new to this cooking stuff aren’t you!" # @t_srichard143.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Hey! You don’t have to make fun of me for it. Everyone has to learn sometime, y’know…" # @t_srichard144.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_halfgrin as miller
    t_ch_richard "Ah, too true. There’s a box of cupcake mix somewhere over there." # @t_srichard145.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Got it." # @t_srichard146.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "That’ll get you started. Just follow the directions. It’s completely idiot proof, so you’ll do fine." # @t_srichard147.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_angry as cousin
    t_ch_cousin "Tha--HEY!" # @t_srichard148.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Oh, no. You’re not an idiot." # @t_srichard149.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Just sayin’! You’ve got nothing to worry about because even an idiot, which you are not, couldn’t screw it up." # @t_srichard150.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified_blush as cousin
    t_ch_cousin "Okay, then." # @t_srichard151.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Uh-oh. But what if I DO screw it up?)" # @t_srichard151.01 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(He’ll think I’m an idiot!!!)" # @t_srichard152.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Hmm, maybe I’ll say the instructions were misprinted. Yeah! That’s the ticket.)" # @t_srichard153.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hold up though. Maybe first I should try to make the darn things before I worry about a cover story.)" # @t_srichard154.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Okay, first up. Add some stuff to other stuff. That’s easy enough.)" # @t_srichard155.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_halfgrin as miller
    t_ch_richard "Looks like you’re doing pretty good so far, [slot_playerName]." # @t_srichard156.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yup, nothing’s on fire." # @t_srichard157.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Always a good sign in the kitchen!" # @t_srichard158.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Oh, hand me that, will you?" # @t_srichard159.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Okay." # @t_srichard160.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Uh, which that? There’s like a dozen utensils and pots and pans and stuff over here!)" # @t_srichard161.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "The spatula?" # @t_srichard162.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "No, but I haven’t time to correct you!" # @t_srichard163.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wouldn’t it have taken just as long to say that as to correct me???)" # @t_srichard164.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, okay, here!" # @t_srichard165.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller
    t_ch_richard "Now I must prepare the duck confit with nothing but a spatula and a piece of string. It’s daring. Possibly never so much as attempted before." # @t_srichard166.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "But that’s what we’ve got and there’s no time to change course now!" # @t_srichard167.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I don’t know anything about how to cook stuff other than what this box of cupcake mix is telling me, but you might want to use some cookware?" # @t_srichard168.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And some heat? Like from an oven?" # @t_srichard169.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "No time!" # @t_srichard170.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I think I’d make the time if it was me!" # @t_srichard171.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "There’s no time to make time! Because I’m making five other dishes." # @t_srichard172.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_shocked as miller
    t_ch_richard "AT THE SAME TIME!" # @t_srichard173.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Wh-what?!" # @t_srichard174.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "No one can cook at these speeds!" # @t_srichard175.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(At least, I think you can’t…?)" # @t_srichard176.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "Ordinarily, no." # @t_srichard177.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "But everything is connected, [slot_playerName]." # @t_srichard178.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Literally, or figuratively, or directly, or indirectly, or sympathetically, or spatially." # @t_srichard179.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_serious as miller
    t_ch_richard "BUT ALWAYS CHRONOLOGICALLY." # @t_srichard180.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Uh, okay then…" # @t_srichard181.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (I guess the question of whether or not the fact that everything must exist in time means that everything is ALSO connected THROUGH the medium of time is beyond the scope of this conversation…)" # @t_srichard181.01 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I think I hurt myself thinking about that…)" # @t_srichard182.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But it basically it sounds right?)" # @t_srichard183.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_halfgrin as miller
    t_ch_richard "Therefore, with precision timing, ANYTHING IS POSSIBLE!" # @t_srichard184.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I’m not sure that conclusion follows from your premise." # @t_srichard185.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Wow, I sound like a college professor!)" # @t_srichard185.01 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Maybe it does and maybe it doesn’t." # @t_srichard186.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_laugh as miller
    t_ch_richard "But you can’t argue with these results!!!" # @t_srichard187.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What the--?!" # @t_srichard188.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (How did he cook a whole meal right in front of me without an oven WHILE WE WERE TALKING?!?!)" # @t_srichard188.01 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Oh, speaking of which! I need to put my cupcakes in the oven…)" # @t_srichard189.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Like so!)" # @t_srichard190.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Wow, Richard." # @t_srichard190.01 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Your duck-whatever-it-was smells delicious too!" # @t_srichard191.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "Does it? How irrelevant." # @t_srichard192.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Hm?" # @t_srichard193.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But good smelling food is GREAT!" # @t_srichard194.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It makes you anticipate getting to eat it and that makes it taste that much better when you do!" # @t_srichard195.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "That’s a weird way to look at it, [slot_playerName]." # @t_srichard196.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_shocked as miller
    t_ch_richard "ACK! We’ve wasted precious seconds talking about food!" # @t_srichard197.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What’s he talking about?)" # @t_srichard198.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And why did he put that duck thing in the trash?!)" # @t_srichard199.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    extend " Hey! What’re you doing?!" # @t_srichard199.01 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_serious as miller
    t_ch_richard "What do you mean? I’m making room for the next dish." # @t_srichard1100.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "It’s not like we have time to sit around ENJOYING the food." # @t_srichard1101.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Much less eating it!" # @t_srichard1102.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh. Then what’s the point of making it?" # @t_srichard1103.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_contemplative as miller
    t_ch_richard "Why, to get the best time, of course!" # @t_srichard1104.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Best time?!" # @t_srichard1105.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What does that even mean?" # @t_srichard1106.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "It’s not like you can can bake a cake faster than the time it takes to bake that cake!" # @t_srichard1107.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    extend " (I sure am thinking about cake a lot.)" # @t_srichard1107.01 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Dangit, why did he have to throw away all that food! Now I’m hungry and still thinking about cakes!)" # @t_srichard1108.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    extend " If you throw away all the food you make, then what do you eat?" # @t_srichard1108.01 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_aliens_halfgrin as miller
    t_ch_richard "Why, fast food, of course." # @t_srichard1109.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(Ugh, I should’ve seen that one coming from a mile away…)" # @t_srichard1110.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_serious as miller
    t_ch_richard "But drive-thru only. No one has time to park, walk inside, wait in line, order, wait for it, walk to a table, sit down, eat, and then throw away the trash, and walk ALL THE WAY BACK to the car, AND THEN leave." # @t_srichard1111.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "That’d be crazy!" # @t_srichard1112.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "No, you do the drive-thru." # @t_srichard1113.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "And the food can only be eaten while driving to wherever it is you’re going, and you can only drive at maximum speed because what’s the point of going any slower UNLESS you’re on your way to going as fast as you possibly can." # @t_srichard1114.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Isn’t that dangerous?" # @t_srichard1115.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_halfgrin as miller
    t_ch_richard "Heh, not with my reflexes!" # @t_srichard1116.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What about the food though?" # @t_srichard1117.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Fast food’s not as bad for us with fast metabolism. We can eat anything, really. Who’s stoppin’ us!" # @t_srichard1118.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(That’s an... interesting point…)" # @t_srichard1119.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But, no, I mean DRIVING and EATING at the same time?" # @t_srichard1119.01 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_contemplative as miller
    t_ch_richard "Oh, that." # @t_srichard1120.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Yeah, it’s big time dangerous." # @t_srichard1121.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_serious as miller
    t_ch_richard "But that’s what CONTINUES are for." # @t_srichard1122.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I feel like that can’t be the right answer…)" # @t_srichard1123.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(And yet I don’t have an argument against it!)" # @t_srichard1124.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_oven "DING!" # @t_srichard1125.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Ack! What’s that mean? Did I do it wrong?" # @t_srichard1126.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_halfgrin as miller
    t_ch_richard "That’s the oven. Your cupcakes are done." # @t_srichard1127.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "PERFECTLY TIMED to happen after my duck confit was finished." # @t_srichard1128.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_serious as miller
    t_ch_richard "Anyway, time to throw them in the trash!" # @t_srichard1129.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Hey, wait! I didn’t make those to NOT have one!" # @t_srichard1130.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " (Man, I want some kinda cake before I leave here or I’ll go nuts.)" # @t_srichard1130.01 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Anyway, they’re not done. They need icing." # @t_srichard1130.02 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_standing_contemplative as miller
    t_ch_richard "A fair point." # @t_srichard1131.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_contemplative as miller
    t_ch_richard "But do it quickly!" # @t_srichard1132.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "There. That’s the first one done." # @t_srichard1133.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "And into the trash it goes." # @t_srichard1134.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "WAAAIIIIIIIIT!!!" # @t_srichard1135.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_akimbo_shocked as miller
    t_ch_richard "ARGH!" # @t_srichard1136.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Make it fast! I can’t wait for long!" # @t_srichard1137.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Try EATING that one." # @t_srichard1138.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "I just told you there isn’t time for that sort of thing!" # @t_srichard1139.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But look at it." # @t_srichard1140.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s BITE-SIZED." # @t_srichard1141.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If it helps, just think of it as throwing it into the trashcan of your own organs." # @t_srichard1142.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "…" # @t_srichard1143.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "……………………." # @t_srichard1144.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_shocked as miller
    t_ch_richard "Whoa, it does help!" # @t_srichard1145.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller
    t_ch_richard "GULP." # @t_srichard1146.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Uh-oh! His face is all...uh...weird.)" # @t_srichard1147.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(HE SAID IT WAS IDIOT PROOF THOUGH C’MON!)" # @t_srichard1148.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "This is…" # @t_srichard1149.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(C’MON C’MON C’MON!)" # @t_srichard1150.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "It’s like…" # @t_srichard1151.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller
    t_ch_richard "There’s a happiness in my mouth." # @t_srichard1152.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(?!?!?)" # @t_srichard1153.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh. Happiness?" # @t_srichard1153.01 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Do you mean, like, a flavor?" # @t_srichard1154.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "So." # @t_srichard1155.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "“Food” can have “flavor.”" # @t_srichard1156.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_richard "Huh. I didn’t know that was possible." # @t_srichard1157.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(And I didn’t know it was possible not to know that!!!)" # @t_srichard1158.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Yeah. Pretty much all food has a flavor, Richard." # @t_srichard1158.01 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_contemplative as miller
    t_ch_richard "Not true! I eat all kinds of fast food and when you’re lucky there’s no real taste at all." # @t_srichard1159.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Probably swallows it whole because chewing would take too long!)" # @t_srichard1160.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " Well, yeah, that stuff’s not the best tasting. Or good for you in any way." # @t_srichard1160.01 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_pondering_serious as miller
    t_ch_richard "Why am I still waiting for the second cupcake!" # @t_srichard1161.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(Darn it, I want some of these too!)" # @t_srichard1162.00 self.block='Last'
    # <NHSceneChange {'name': '_2Z', 'scene': 's_day2'} NHSceneChange ''>
    label s_richard1__2Z:
        # <NHSceneChange {'name': '_2Z', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2