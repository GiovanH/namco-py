# <Scene {'id': 's_galaga3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_galaga3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_galaga3"
    $ renpy.pause(1)
    # <Scene {'id': 's_galaga3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/privatetimes.ogg" loop
    show i_bg_classroom_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_surprised as cousin zorder 3:
        default
        xpos 0.25 
    show i_galaga_default as galaga zorder 2:
        default
        xpos 0.75 
    show i_digdug_left as digdug zorder 2:
        default
        alpha 0.0
        xpos 0.75 
    show i_miller_notebook_serious as miller zorder 1:
        default
        xpos 0.9 
        ypos 1.5 
        alpha 1.0
    show i_king_confident as king zorder 2:
        default
        xpos 0.78 
        alpha 0.0
        xzoom -1.0 
    t_ch_cousin "Okay, so, I am here to make the rehearsing!" # @t_sgalaga30.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Great. Thanks for joining me today, [slot_playerName].{/smallcaps}" # @t_sgalaga31.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh, yeah!" # @t_sgalaga32.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Y’know. Anything to help out with the Drama Club or whatever!" # @t_sgalaga33.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}That’s the spirit!{/smallcaps}" # @t_sgalaga34.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Okay, this is gonna take a while. Partly because you’re so new to acting.{/smallcaps}" # @t_sgalaga35.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I choose to take that positively!)" # @t_sgalaga36.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m gonna do my best, Galaga Ship, don’t you worry!" # @t_sgalaga37.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeah…{/smallcaps}" # @t_sgalaga38.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}That’s good.{/smallcaps}" # @t_sgalaga39.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Great, where should we meet up?" # @t_sgalaga310.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Let’s just head to the auditorium. The only people left are in detention, so we’ll have the place to ourselves.{/smallcaps}" # @t_sgalaga311.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "(A-alone?)" # @t_sgalaga312.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(WITH GALAGA SHIP????)" # @t_sgalaga313.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Breathe, [slot_playerName]. BREEEEAAAATHE!)" # @t_sgalaga314.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}If we go now, I can avoid that creepy Richard Miller. He takes notes.{/smallcaps}" # @t_sgalaga315.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That doesn’t sound too creepy…" # @t_sgalaga316.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}No, like, on the students. Their movements and stuff.{/smallcaps}" # @t_sgalaga317.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_notebook_serious as miller:
        # ShowWithAtl
        ease_expo 0.5 ypos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_richard "Note to self. GALAGA SHIP KNOWS TOO MUCH." # @t_sgalaga318.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "He’s not very sneaky about it, is he?" # @t_sgalaga319.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_miller_notebook_contemplative as miller
    t_ch_richard "Note to self: TURNS OUT NEW KID IS A LITTLE RUDE ACTUALLY." # @t_sgalaga320.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_default as galaga:
        # ShowWithAtl
        ease_expo 1 xpos 0.7 
    extend "{w=1.0}{nw}"
    t_ch_galaga "{smallcaps}Yeah,  I don’t know why he feels the need to narrate the notes he’s taking.{/smallcaps}" # @t_sgalaga321.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain2 zorder 10:
        default
        alpha 0.0
    show i_cousin_default_sad as cousin
    t_ch_cousin "It’s weird. Let’s get out of here!" # @t_sgalaga322.00 self.block='Last'
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear 1 alpha 1.0
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Whew. Turns out rehearsing’s tougher than I thought it’d be!)" # @t_sgalaga323.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_stage_cardboard as bg # behind curtain
    # <SettingChange {'bgImage': '@i_bg_stage_cardboard', 'curtainFadeTime': '1', 'name': '_P'} SettingChange ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_galaga_script as galaga:
        # ShowWithAtl
        linear 0.5 xpos 0.75 
    show i_miller_notebook_contemplative as miller:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_galaga_script as galaga
    t_ch_galaga "{smallcaps}[slot_playerName]? It’s your line now.{/smallcaps}" # @t_sgalaga324.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "!!!!!" # @t_sgalaga325.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Oh, right. Yeah. Ahem." # @t_sgalaga325.01 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    extend " AY!!! YOU HAVE BEEN A MOUSE? HUNT! IN YOUR TIME!!!" # @t_sgalaga325.02 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}[slot_playerName]. That’s the wrong page.{/smallcaps}" # @t_sgalaga326.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}AND the wrong character.{/smallcaps}" # @t_sgalaga327.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(Being a great actor sure is a lot of work!)" # @t_sgalaga328.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh, yeah. It’s hard to keep track of all these lines." # @t_sgalaga328.01 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "There’s just so many of them!" # @t_sgalaga329.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But you’re really good at this acting stuff, Galaga Ship. How do you do it?" # @t_sgalaga330.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I know you’re just saying that. Aki’s better.{/smallcaps}" # @t_sgalaga331.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Well, in theory anyway.{/smallcaps}" # @t_sgalaga332.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If you say so. I hope she has an easier time with Romeo’s lines than me though!" # @t_sgalaga333.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You’d have to find one of Romeo’s lines first.{/smallcaps}" # @t_sgalaga334.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "H-hey! There’s a lot of words in this thing!" # @t_sgalaga335.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And I only understand about half of them!" # @t_sgalaga336.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Well. Almost half of them...)" # @t_sgalaga336.01 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Anyway, it’s easy to get a little lost." # @t_sgalaga336.02 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Haha. I’m just teasing you, [slot_playerName]. Everyone’s skill level is…{/smallcaps}" # @t_sgalaga337.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}…uh{/smallcaps}" # @t_sgalaga337.01 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}…different.{/smallcaps}" # @t_sgalaga337.02 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}And yours is…{/smallcaps}" # @t_sgalaga338.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}…um.{/smallcaps}" # @t_sgalaga339.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Very different.{/smallcaps}" # @t_sgalaga340.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(There’s no bad way to take that!)" # @t_sgalaga341.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Well, I’m just out here tryin’ to do my best like everyone else!" # @t_sgalaga341.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Yes, a very diplomatic response. Well done, [slot_playerName].)" # @t_sgalaga341.02 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}That’s a great attitude.{/smallcaps}" # @t_sgalaga342.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I just wish…{/smallcaps}" # @t_sgalaga343.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}No.{/smallcaps}" # @t_sgalaga344.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I don’t know.{/smallcaps}" # @t_sgalaga345.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "You okay?" # @t_sgalaga346.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}No, it’s stupid. Never mind.{/smallcaps}" # @t_sgalaga347.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But something’s bothering you." # @t_sgalaga348.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Let’s just worry about the play.{/smallcaps}" # @t_sgalaga349.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Well, okay. If you’re sure?" # @t_sgalaga350.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}No, yeah. I’m fine.{/smallcaps}" # @t_sgalaga351.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Let’s pick up with Romeo’s line about night’s cloak. Okay?{/smallcaps}" # @t_sgalaga352.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Right. Okay. Yeah." # @t_sgalaga353.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Night’s cloak, night’s cloak…)" # @t_sgalaga353.01 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}It’s right here, [slot_playerName]. Act 2, Scene 2.{/smallcaps}" # @t_sgalaga354.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Oh, right. Haha! They should make this thing easier to read, am I right!" # @t_sgalaga355.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Ahem." # @t_sgalaga355.01 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    extend " “I HAVE NIGHT’S CLOAK TO HIDE!!! ME? FROM THEIR EYES." # @t_sgalaga355.02 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_sad as cousin
    t_ch_cousin "AND, BUT THOU LOVE? ME! LET THEM FIND ME THERE I mean HERE!!!" # @t_sgalaga356.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_laugh as cousin
    t_ch_cousin "MY LIFE WERE BETTER ENDED BY THEIR HATE???" # @t_sgalaga357.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "THAN DEATH PROLOGUED uh PROROGUED? WANTING OF THY LOVE???”" # @t_sgalaga358.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}…{/smallcaps}" # @t_sgalaga359.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(I knew something was bothering Galaga Ship!)" # @t_sgalaga360.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}That was…well, it was the right line.{/smallcaps}" # @t_sgalaga361.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin_blush as cousin
    t_ch_cousin "(Yeah, makin’ progress!)" # @t_sgalaga362.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}And then Juliet goes…{/smallcaps}" # @t_sgalaga363.00 self.block='Last'
    show i_galaga_wig as galaga
    with Dissolve(.7)
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}“By whose direction thou found’st this place?”{/smallcaps}" # @t_sgalaga363.01 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Hm, that wasn’t quite right, actually!)" # @t_sgalaga364.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Oh, uh, Galaga Ship?" # @t_sgalaga364.01 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Don’t tell me you can’t find your next line, [slot_playerName]!{/smallcaps}" # @t_sgalaga365.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh, no. It’s not that." # @t_sgalaga366.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (But now that Galaga Ship mentions it…)" # @t_sgalaga366.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You, um. That’s not your line." # @t_sgalaga366.02 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}It’s not?{/smallcaps}" # @t_sgalaga367.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ah, well, it is. But it’s different from that. It goes…" # @t_sgalaga368.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Aw, man. Lemme find it." # @t_sgalaga368.01 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Here." # @t_sgalaga369.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    extend " “BY WHOS DIRECTION??? FOUND’ST THOU OUT THIS PLACE!!!”" # @t_sgalaga369.01 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "See? You skipped and moved a couple words." # @t_sgalaga370.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I…Huh. You’re right.{/smallcaps}" # @t_sgalaga371.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Yeah, it’s no big, just FYI." # @t_sgalaga372.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I’ve done that line a half dozen times and never caught myself making that mistake.{/smallcaps}" # @t_sgalaga373.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh, we all make mistakes we don’t notice." # @t_sgalaga374.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Even I’m probably doing some stuff a little wrong without noticing it!" # @t_sgalaga375.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Yeah, definitely!{/smallcaps}" # @t_sgalaga376.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(That was weirdly emphatic!)" # @t_sgalaga377.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}But what I’m saying is…{/smallcaps}" # @t_sgalaga378.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}No one ever corrected me on that before…{/smallcaps}" # @t_sgalaga379.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well, happy to help, Galaga Ship." # @t_sgalaga380.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Everyone else just let me do the line wrong.{/smallcaps}" # @t_sgalaga381.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s a little thing. They might not have noticed it. Galaga Ship, everyone makes mistakes. It’s totally not a big deal!" # @t_sgalaga382.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}No, it’s not, but how can I fix my mistakes if no one points them out?{/smallcaps}" # @t_sgalaga383.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Like, what I mean is, look at how I got this part.{/smallcaps}" # @t_sgalaga384.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Remember? They gave it to me. No audition or anything.{/smallcaps}" # @t_sgalaga385.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}I just got it.{/smallcaps}" # @t_sgalaga385.01 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}It’s like, everyone, my whole life, they’ve treated me different.{/smallcaps}" # @t_sgalaga386.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(A villa is a powerful thing around these parts!)" # @t_sgalaga387.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Like they never cared about me.{/smallcaps}" # @t_sgalaga388.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Who I am. Or what I can offer the world.{/smallcaps}" # @t_sgalaga389.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}It was all about, y’know, my hull.{/smallcaps}" # @t_sgalaga390.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Your, wait what?" # @t_sgalaga391.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I’ve always been defined by my looks. Even in school, the other kids help me study or to just cheat.{/smallcaps}" # @t_sgalaga392.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I skip, I talk during class, I miss homework, and the other kids cover me.{/smallcaps}" # @t_sgalaga393.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I’m just coasting through everything and it’s all because of how I look. And they don’t even care about who I really am!{/smallcaps}" # @t_sgalaga394.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(Wow, I had no idea Galaga Ship was so distraught about this stuff!)" # @t_sgalaga395.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Oh, [slot_playerName]. I’m so sorry. I didn’t mean to…I’m sorry.{/smallcaps}" # @t_sgalaga396.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What? No, don’t be!" # @t_sgalaga397.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You don’t, do you think…Do you think I’m like that?" # @t_sgalaga397.01 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I shouldn’t have…just forget I mentioned anything. Okay?{/smallcaps}" # @t_sgalaga398.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}It’s not your problem, don’t worry about it. We’re here for rehearsal, right? Let’s get back to that.{/smallcaps}" # @t_sgalaga399.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Hey, rehearsal can wait, Galaga Ship. You’re really upset about this. Do you really think your friends don’t care about you? That’s awful." # @t_sgalaga3100.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}You know what’s worse though?{/smallcaps}" # @t_sgalaga3101.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {smallcaps}ME!{/smallcaps}" # @t_sgalaga3101.01 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(I-is Galaga Ship a MONSTER???)" # @t_sgalaga3102.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I’m living with a curse. A terrible, terrible curse.{/smallcaps}" # @t_sgalaga3103.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(WEREWOLVES ARE CURSED!)" # @t_sgalaga3104.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Because, think about it. I know what they’re doing, and I let them so I can get things from them. I’m taking advantage of them!{/smallcaps}" # @t_sgalaga3105.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}That makes me worse!{/smallcaps}" # @t_sgalaga3106.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad_blush as cousin
    t_ch_cousin "Whew, that’s not nearly as bad as a werewolf." # @t_sgalaga3107.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}???{/smallcaps}" # @t_sgalaga3108.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Uh, whoops!)" # @t_sgalaga3109.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Er, by which, I mean, uh, y’know." # @t_sgalaga3109.01 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "It’s bad, okay, but it’s not like you’re literally a monster, i.e. werewolf." # @t_sgalaga3110.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Nailed it!)" # @t_sgalaga3110.01 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Anyway, we can do something about it!" # @t_sgalaga3110.02 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Yeah? Like what? Enroll in Evil Namco High where all the awful kids belong?{/smallcaps}" # @t_sgalaga3111.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "No, that’s going too far!" # @t_sgalaga3112.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Is it though? How do I know you’re any different from the rest of them? All this rehearsal and wanting to help.{/smallcaps}" # @t_sgalaga3113.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}How do I know you’re not just saying what you think I want to hear because I’m the most beautiful spaceship in school?{/smallcaps}" # @t_sgalaga3114.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}How do I know you’re not just trying to impress me?{/smallcaps}" # @t_sgalaga3115.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Wow, this is a conundrum!" # @t_sgalaga3116.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin:
        # ShowWithAtl
        ease_expo .3 xpos 0.13 
    show i_galaga_wig as galaga:
        # ShowWithAtl
        ease_expo .3 xpos 0.3 
    show i_digdug_left as digdug:
        # ShowWithAtl
        pause 0.2 
        linear .33 alpha 1.0
    extend "{w=0.53}{nw}"
    t_ch_digdug "What the--?!" # @t_sgalaga3117.00 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "???" # @t_sgalaga3118.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}!!!{/smallcaps}" # @t_sgalaga3119.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "What’s going on in here? Is this…" # @t_sgalaga3120.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "IS THIS SKIPPING?!" # @t_sgalaga3121.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ah! Uh, it was for a good reason! We’re rehearsing for the play! For drama club! For school spirit!" # @t_sgalaga3122.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "A likely story. I even believe it." # @t_sgalaga3123.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Parts, anyway." # @t_sgalaga3123.01 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "But the law’s the law! And you’ve broken it! Now you must face the ULTIMATE PUNISHMENT" # @t_sgalaga3124.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(DEATH???)" # @t_sgalaga3125.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "DOUBLE DETENTION!" # @t_sgalaga3126.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}NOOOOOOOOO{/smallcaps}" # @t_sgalaga3127.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "OOOOOOOOOO" # @t_sgalaga3128.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Hold on. That doesn’t sound so awful.{/smallcaps}" # @t_sgalaga3129.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "If I’m honest, it’s just regular detention." # @t_sgalaga3130.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ONLY TWICE AS BAD." # @t_sgalaga3130.01 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king zorder 1
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But how could it get any worse? Do you pump in more of that weird wrestling mat smell from King?" # @t_sgalaga3131.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_screaming as king:
        # ShowWithAtl
        linear .33 alpha 1.0
    show i_cousin_energetic_mortified as cousin
    play sound "sfx/kingroar1.ogg"
    extend "{w=0.33}{nw}"
    t_ch_king "RRROOOOOOAR!!!" # @t_sgalaga3132.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king
    t_ch_digdug "Yes, I know. Yes, I’ll tell them." # @t_sgalaga3133.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "King says…" # @t_sgalaga3134.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Ahem." # @t_sgalaga3135.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " “THAT IS THE AROMA OF VICTORY!”" # @t_sgalaga3135.01 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Anyway, his musk is not on trial here. YOU kids are." # @t_sgalaga3136.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The verdict?" # @t_sgalaga3136.01 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "GUILTY!" # @t_sgalaga3137.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}Wait, what? All you did was say “guilty.” That’s not a trial!{/smallcaps}" # @t_sgalaga3138.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_screaming as king
    play sound "sfx/kingroar3.ogg"
    t_ch_king "ROAR!" # @t_sgalaga3139.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_confident as king
    t_ch_digdug "I’m afraid he’s right." # @t_sgalaga3140.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_digdug "Your sass just earned you seventeen years of double detention!" # @t_sgalaga3141.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I’ll only be in high school for a total of three years though." # @t_sgalaga3142.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Time works differently in double detention!" # @t_sgalaga3143.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}I don’t get it. We were told to show school spirit to get less detention, but we earned some kind of bizarre higher level detention by doing it!{/smallcaps}" # @t_sgalaga3144.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Logic works differently there too!" # @t_sgalaga3145.00 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(This is all my fault! What have I done!!!)" # @t_sgalaga3146.00 self.block='Last'
    # <NHSceneChange {'name': '_2s', 'scene': 's_day4'} NHSceneChange ''>
    label s_galaga3__2s:
        # <NHSceneChange {'name': '_2s', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4