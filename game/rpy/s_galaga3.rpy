# <Scene scene {'id': 's_galaga3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_galaga3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_galaga3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_galaga3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
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
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Great. Thanks for joining me today, [slot_playerName].{/smallcaps}" # @t_sgalaga31.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Uh, yeah!" # @t_sgalaga32.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Y’know. Anything to help out with the Drama Club or whatever!" # @t_sgalaga33.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}That’s the spirit!{/smallcaps}" # @t_sgalaga34.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Okay, this is gonna take a while. Partly because you’re so new to acting.{/smallcaps}" # @t_sgalaga35.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I choose to take that positively!)" # @t_sgalaga36.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I’m gonna do my best, Galaga Ship, don’t you worry!" # @t_sgalaga37.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyeah…{/smallcaps}" # @t_sgalaga38.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}That’s good.{/smallcaps}" # @t_sgalaga39.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Great, where should we meet up?" # @t_sgalaga310.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Let’s just head to the auditorium. The only people left are in detention, so we’ll have the place to ourselves.{/smallcaps}" # @t_sgalaga311.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "(A-alone?)" # @t_sgalaga312.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(WITH GALAGA SHIP????)" # @t_sgalaga313.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Breathe, [slot_playerName]. BREEEEAAAATHE!)" # @t_sgalaga314.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}If we go now, I can avoid that creepy Richard Miller. He takes notes.{/smallcaps}" # @t_sgalaga315.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That doesn’t sound too creepy…" # @t_sgalaga316.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}No, like, on the students. Their movements and stuff.{/smallcaps}" # @t_sgalaga317.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_notebook_serious as miller:
        # ShowWithAtl
        ease_expo 0.5 ypos 0.5 
    extend "{w=0.5}{nw}"
    t_ch_richard "Note to self. GALAGA SHIP KNOWS TOO MUCH." # @t_sgalaga318.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "He’s not very sneaky about it, is he?" # @t_sgalaga319.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_miller_notebook_contemplative as miller
    t_ch_richard "Note to self: TURNS OUT NEW KID IS A LITTLE RUDE ACTUALLY." # @t_sgalaga320.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_galaga_default as galaga:
        # ShowWithAtl
        ease_expo 1 xpos 0.7 
    extend "{w=1.0}{nw}"
    t_ch_galaga "{smallcaps}Yeah,  I don’t know why he feels the need to narrate the notes he’s taking.{/smallcaps}" # @t_sgalaga321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain2 zorder 10:
        default
        alpha 0.0
    show i_cousin_default_sad as cousin
    t_ch_cousin "It’s weird. Let’s get out of here!" # @t_sgalaga322.00 self.block='Last'
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear 1 alpha 1.0
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Whew. Turns out rehearsing’s tougher than I thought it’d be!)" # @t_sgalaga323.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0) # Curtain fade
    show i_bg_stage_cardboard as bg # behind curtain
    # <SettingChange SettingChange {'bgImage': '@i_bg_stage_cardboard', 'curtainFadeTime': '1', 'name': '_P', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
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
    $ renpy.pause(1.0) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_galaga_script as galaga
    t_ch_galaga "{smallcaps}[slot_playerName]? It’s your line now.{/smallcaps}" # @t_sgalaga324.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "!!!!!" # @t_sgalaga325.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Oh, right. Yeah. Ahem." # @t_sgalaga325.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    extend " AY!!! YOU HAVE BEEN A MOUSE? HUNT! IN YOUR TIME!!!" # @t_sgalaga325.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}[slot_playerName]. That’s the wrong page.{/smallcaps}" # @t_sgalaga326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}AND the wrong character.{/smallcaps}" # @t_sgalaga327.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(Being a great actor sure is a lot of work!)" # @t_sgalaga328.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Uh, yeah. It’s hard to keep track of all these lines." # @t_sgalaga328.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "There’s just so many of them!" # @t_sgalaga329.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But you’re really good at this acting stuff, Galaga Ship. How do you do it?" # @t_sgalaga330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I know you’re just saying that. Aki’s better.{/smallcaps}" # @t_sgalaga331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Well, in theory anyway.{/smallcaps}" # @t_sgalaga332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "If you say so. I hope she has an easier time with Romeo’s lines than me though!" # @t_sgalaga333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}You’d have to find one of Romeo’s lines first.{/smallcaps}" # @t_sgalaga334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "H-hey! There’s a lot of words in this thing!" # @t_sgalaga335.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And I only understand about half of them!" # @t_sgalaga336.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Well. Almost half of them...)" # @t_sgalaga336.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Anyway, it’s easy to get a little lost." # @t_sgalaga336.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Haha. I’m just teasing you, [slot_playerName]. Everyone’s skill level is…{/smallcaps}" # @t_sgalaga337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {smallcaps}…uh{/smallcaps}" # @t_sgalaga337.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {smallcaps}…different.{/smallcaps}" # @t_sgalaga337.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}And yours is…{/smallcaps}" # @t_sgalaga338.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}…um.{/smallcaps}" # @t_sgalaga339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Very different.{/smallcaps}" # @t_sgalaga340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(There’s no bad way to take that!)" # @t_sgalaga341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Well, I’m just out here tryin’ to do my best like everyone else!" # @t_sgalaga341.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Yes, a very diplomatic response. Well done, [slot_playerName].)" # @t_sgalaga341.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}That’s a great attitude.{/smallcaps}" # @t_sgalaga342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I just wish…{/smallcaps}" # @t_sgalaga343.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}No.{/smallcaps}" # @t_sgalaga344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I don’t know.{/smallcaps}" # @t_sgalaga345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "You okay?" # @t_sgalaga346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}No, it’s stupid. Never mind.{/smallcaps}" # @t_sgalaga347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "But something’s bothering you." # @t_sgalaga348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Let’s just worry about the play.{/smallcaps}" # @t_sgalaga349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Well, okay. If you’re sure?" # @t_sgalaga350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}No, yeah. I’m fine.{/smallcaps}" # @t_sgalaga351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Let’s pick up with Romeo’s line about night’s cloak. Okay?{/smallcaps}" # @t_sgalaga352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Right. Okay. Yeah." # @t_sgalaga353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Night’s cloak, night’s cloak…)" # @t_sgalaga353.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}It’s right here, [slot_playerName]. Act 2, Scene 2.{/smallcaps}" # @t_sgalaga354.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Oh, right. Haha! They should make this thing easier to read, am I right!" # @t_sgalaga355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Ahem." # @t_sgalaga355.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    extend " “I HAVE NIGHT’S CLOAK TO HIDE!!! ME? FROM THEIR EYES." # @t_sgalaga355.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_sad as cousin
    t_ch_cousin "AND, BUT THOU LOVE? ME! LET THEM FIND ME THERE I mean HERE!!!" # @t_sgalaga356.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_laugh as cousin
    t_ch_cousin "MY LIFE WERE BETTER ENDED BY THEIR HATE???" # @t_sgalaga357.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "THAN DEATH PROLOGUED uh PROROGUED? WANTING OF THY LOVE???”" # @t_sgalaga358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}…{/smallcaps}" # @t_sgalaga359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(I knew something was bothering Galaga Ship!)" # @t_sgalaga360.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}That was…well, it was the right line.{/smallcaps}" # @t_sgalaga361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_grin_blush as cousin
    t_ch_cousin "(Yeah, makin’ progress!)" # @t_sgalaga362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}And then Juliet goes…{/smallcaps}" # @t_sgalaga363.00 self.block='Last'
    show i_galaga_wig as galaga
    with Dissolve(.7)
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {smallcaps}“By whose direction thou found’st this place?”{/smallcaps}" # @t_sgalaga363.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Hm, that wasn’t quite right, actually!)" # @t_sgalaga364.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Oh, uh, Galaga Ship?" # @t_sgalaga364.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Don’t tell me you can’t find your next line, [slot_playerName]!{/smallcaps}" # @t_sgalaga365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh, no. It’s not that." # @t_sgalaga366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (But now that Galaga Ship mentions it…)" # @t_sgalaga366.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You, um. That’s not your line." # @t_sgalaga366.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}It’s not?{/smallcaps}" # @t_sgalaga367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Ah, well, it is. But it’s different from that. It goes…" # @t_sgalaga368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Aw, man. Lemme find it." # @t_sgalaga368.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Here." # @t_sgalaga369.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    extend " “BY WHOS DIRECTION??? FOUND’ST THOU OUT THIS PLACE!!!”" # @t_sgalaga369.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "See? You skipped and moved a couple words." # @t_sgalaga370.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I…Huh. You’re right.{/smallcaps}" # @t_sgalaga371.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Yeah, it’s no big, just FYI." # @t_sgalaga372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I’ve done that line a half dozen times and never caught myself making that mistake.{/smallcaps}" # @t_sgalaga373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Oh, we all make mistakes we don’t notice." # @t_sgalaga374.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Even I’m probably doing some stuff a little wrong without noticing it!" # @t_sgalaga375.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Yeah, definitely!{/smallcaps}" # @t_sgalaga376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(That was weirdly emphatic!)" # @t_sgalaga377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}But what I’m saying is…{/smallcaps}" # @t_sgalaga378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}No one ever corrected me on that before…{/smallcaps}" # @t_sgalaga379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Well, happy to help, Galaga Ship." # @t_sgalaga380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Everyone else just let me do the line wrong.{/smallcaps}" # @t_sgalaga381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It’s a little thing. They might not have noticed it. Galaga Ship, everyone makes mistakes. It’s totally not a big deal!" # @t_sgalaga382.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}No, it’s not, but how can I fix my mistakes if no one points them out?{/smallcaps}" # @t_sgalaga383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Like, what I mean is, look at how I got this part.{/smallcaps}" # @t_sgalaga384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Remember? They gave it to me. No audition or anything.{/smallcaps}" # @t_sgalaga385.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {smallcaps}I just got it.{/smallcaps}" # @t_sgalaga385.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}It’s like, everyone, my whole life, they’ve treated me different.{/smallcaps}" # @t_sgalaga386.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(A villa is a powerful thing around these parts!)" # @t_sgalaga387.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Like they never cared about me.{/smallcaps}" # @t_sgalaga388.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Who I am. Or what I can offer the world.{/smallcaps}" # @t_sgalaga389.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}It was all about, y’know, my hull.{/smallcaps}" # @t_sgalaga390.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Your, wait what?" # @t_sgalaga391.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I’ve always been defined by my looks. Even in school, the other kids help me study or to just cheat.{/smallcaps}" # @t_sgalaga392.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I skip, I talk during class, I miss homework, and the other kids cover me.{/smallcaps}" # @t_sgalaga393.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I’m just coasting through everything and it’s all because of how I look. And they don’t even care about who I really am!{/smallcaps}" # @t_sgalaga394.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(Wow, I had no idea Galaga Ship was so distraught about this stuff!)" # @t_sgalaga395.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Oh, [slot_playerName]. I’m so sorry. I didn’t mean to…I’m sorry.{/smallcaps}" # @t_sgalaga396.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What? No, don’t be!" # @t_sgalaga397.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You don’t, do you think…Do you think I’m like that?" # @t_sgalaga397.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I shouldn’t have…just forget I mentioned anything. Okay?{/smallcaps}" # @t_sgalaga398.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}It’s not your problem, don’t worry about it. We’re here for rehearsal, right? Let’s get back to that.{/smallcaps}" # @t_sgalaga399.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Hey, rehearsal can wait, Galaga Ship. You’re really upset about this. Do you really think your friends don’t care about you? That’s awful." # @t_sgalaga3100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}You know what’s worse though?{/smallcaps}" # @t_sgalaga3101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " {smallcaps}ME!{/smallcaps}" # @t_sgalaga3101.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(I-is Galaga Ship a MONSTER???)" # @t_sgalaga3102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I’m living with a curse. A terrible, terrible curse.{/smallcaps}" # @t_sgalaga3103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(WEREWOLVES ARE CURSED!)" # @t_sgalaga3104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Because, think about it. I know what they’re doing, and I let them so I can get things from them. I’m taking advantage of them!{/smallcaps}" # @t_sgalaga3105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}That makes me worse!{/smallcaps}" # @t_sgalaga3106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad_blush as cousin
    t_ch_cousin "Whew, that’s not nearly as bad as a werewolf." # @t_sgalaga3107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}???{/smallcaps}" # @t_sgalaga3108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Uh, whoops!)" # @t_sgalaga3109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Er, by which, I mean, uh, y’know." # @t_sgalaga3109.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "It’s bad, okay, but it’s not like you’re literally a monster, i.e. werewolf." # @t_sgalaga3110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Nailed it!)" # @t_sgalaga3110.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Anyway, we can do something about it!" # @t_sgalaga3110.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Yeah? Like what? Enroll in Evil Namco High where all the awful kids belong?{/smallcaps}" # @t_sgalaga3111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "No, that’s going too far!" # @t_sgalaga3112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Is it though? How do I know you’re any different from the rest of them? All this rehearsal and wanting to help.{/smallcaps}" # @t_sgalaga3113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}How do I know you’re not just saying what you think I want to hear because I’m the most beautiful spaceship in school?{/smallcaps}" # @t_sgalaga3114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}How do I know you’re not just trying to impress me?{/smallcaps}" # @t_sgalaga3115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Wow, this is a conundrum!" # @t_sgalaga3116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
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
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "???" # @t_sgalaga3118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}!!!{/smallcaps}" # @t_sgalaga3119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "What’s going on in here? Is this…" # @t_sgalaga3120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "IS THIS SKIPPING?!" # @t_sgalaga3121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Ah! Uh, it was for a good reason! We’re rehearsing for the play! For drama club! For school spirit!" # @t_sgalaga3122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "A likely story. I even believe it." # @t_sgalaga3123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Parts, anyway." # @t_sgalaga3123.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "But the law’s the law! And you’ve broken it! Now you must face the ULTIMATE PUNISHMENT" # @t_sgalaga3124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(DEATH???)" # @t_sgalaga3125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "DOUBLE DETENTION!" # @t_sgalaga3126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}NOOOOOOOOO{/smallcaps}" # @t_sgalaga3127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "OOOOOOOOOO" # @t_sgalaga3128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Hold on. That doesn’t sound so awful.{/smallcaps}" # @t_sgalaga3129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "If I’m honest, it’s just regular detention." # @t_sgalaga3130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " ONLY TWICE AS BAD." # @t_sgalaga3130.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_confident as king zorder 1
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But how could it get any worse? Do you pump in more of that weird wrestling mat smell from King?" # @t_sgalaga3131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_screaming as king:
        # ShowWithAtl
        linear .33 alpha 1.0
    show i_cousin_energetic_mortified as cousin
    play sound "sfx/kingroar1.ogg"
    extend "{w=0.33}{nw}"
    t_ch_king "RRROOOOOOAR!!!" # @t_sgalaga3132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_confident as king
    t_ch_digdug "Yes, I know. Yes, I’ll tell them." # @t_sgalaga3133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "King says…" # @t_sgalaga3134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Ahem." # @t_sgalaga3135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " “THAT IS THE AROMA OF VICTORY!”" # @t_sgalaga3135.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Anyway, his musk is not on trial here. YOU kids are." # @t_sgalaga3136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " The verdict?" # @t_sgalaga3136.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "GUILTY!" # @t_sgalaga3137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}Wait, what? All you did was say “guilty.” That’s not a trial!{/smallcaps}" # @t_sgalaga3138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_screaming as king
    play sound "sfx/kingroar3.ogg"
    t_ch_king "ROAR!" # @t_sgalaga3139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_king_confident as king
    t_ch_digdug "I’m afraid he’s right." # @t_sgalaga3140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_digdug "Your sass just earned you seventeen years of double detention!" # @t_sgalaga3141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I’ll only be in high school for a total of three years though." # @t_sgalaga3142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Time works differently in double detention!" # @t_sgalaga3143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_galaga "{smallcaps}I don’t get it. We were told to show school spirit to get less detention, but we earned some kind of bizarre higher level detention by doing it!{/smallcaps}" # @t_sgalaga3144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Logic works differently there too!" # @t_sgalaga3145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(This is all my fault! What have I done!!!)" # @t_sgalaga3146.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_2s', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_galaga3__2s:
        # <NHSceneChange NHSceneChange {'name': '_2s', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4