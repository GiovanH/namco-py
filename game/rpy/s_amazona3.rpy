# <Scene {'id': 's_amazona3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_amazona3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_amazona3"
    $ renpy.pause(1)
    # <Scene {'id': 's_amazona3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
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
        xpos 0.25 
    show i_aki_default_distracted as aki zorder 1:
        default
        xpos 0.75 
    show i_digdug_left as digdug zorder 2:
        default
        alpha 0.0
        xpos 0.8 
    show i_amazona_default_smile as amazona zorder 2:
        default
        alpha 0.0
        xpos 0.7 
    show i_king_screaming as king zorder 2:
        default
        xpos 0.3 
        alpha 0.0
    t_ch_aki "[slot_playerName]... Honestly... I'm surprised you came to see me." # @t_samazona314.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "Most people give up because I'm always so busy." # @t_samazona315.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well... I admire that. I'm hoping that I'll pick up some pointers!" # @t_samazona316.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And you let me know if you need any tips for rolling stuff up. I'm pretty good at that!" # @t_samazona317.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_smile as aki
    t_ch_aki "Oh, thank you [slot_playerName]... But I've actually won the Namco City Rolling Trophy 3 years running." # @t_samazona318.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Wow... She IS good at everything... )" # @t_samazona319.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I didn't even know there was a Rolling Competition!" # @t_samazona320.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "Oh... Well, I started it. Three years ago." # @t_samazona321.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "Anyway! I should really get started... I need to memorize these lines." # @t_samazona322.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "How can I help?" # @t_samazona323.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "Just hold the book and let me know if I get something wrong." # @t_samazona323.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Great!" # @t_samazona324.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_justice_focus as aki
    t_ch_aki "But, soft! what light through yonder window breaks?" # @t_samazona325.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "It is the east, and Juliet is the sun." # @t_samazona325.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "Arise, fair sun, and kill the envious moon," # @t_samazona325.02 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "Who is already sick and pale with grief," # @t_samazona326.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Whoa! She's pretty into that part about killing the moon.)" # @t_samazona326.01 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And she IS a lot like the sun... Like bright and intense and ready to sear the eyes of the enemy.)" # @t_samazona327.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(... Whoa... Is this feeling... what they call 'hero worship'?!)" # @t_samazona327.01 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "That thou her maid art far more fair--" # @t_samazona328.00 self.block='Last'
    play sound "sfx/sentaisignal.ogg"
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_shocked as aki
    t_ch_aki "AH! Um... Don't go anywhere! I'll only be a moment!" # @t_samazona329.00 self.block='Last'
    show i_aki_default_shocked as aki:
        # FadeEvent
        linear 0.33 alpha 0.0
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Aww... I was in the middle of a monologue.)" # @t_samazona329.01 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Maybe that's her schedule alarm?)" # @t_samazona329.02 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But it always seems to ring at inopportune times..." # @t_samazona330.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It always surprises her.)" # @t_samazona330.01 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And why does she always seem so tired when she gets back?)" # @t_samazona331.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Is she... An undercover cop?!" # @t_samazona332.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or maybe she has some crazy workout regimen for the Wrestleball team." # @t_samazona332.01 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " But I've never seen any other Wrestleball players run off like that.)" # @t_samazona333.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(MAYBE IT'S AN AFFAIR..." # @t_samazona334.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    extend " How steamy.)" # @t_samazona335.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(No... She definitely doesn't seem to have time for love." # @t_samazona335.01 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " In fact, she doesn't seem to have time for people, period.)" # @t_samazona336.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(And really... It doesn't seem like any of those.)" # @t_samazona336.01 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But it's not any normal part of her schedule for sure." # @t_samazona337.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She's so regimented... Except for this one thing." # @t_samazona338.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She drops everything for the mysterious ringtone.)" # @t_samazona339.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_nervouslaughter as aki:
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_aki "Sorry... Something came up." # @t_samazona339.01 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Thanks for waiting." # @t_samazona340.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Okay [slot_playerName]... Play it cool. Just be real casual.)" # @t_samazona341.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "You ever think about if... Like... Shakespeare ever had a ringtone?" # @t_samazona342.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And if he had one, which one he'd use?" # @t_samazona343.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "(I am a mastermind.)" # @t_samazona344.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_laughter_nervous as aki
    t_ch_aki "Uh... HAHAHAHAHAHAHA! Ringtones?! Why do you want to talk about ringtones?!" # @t_samazona345.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "(That... Is the most desperate laughter I've ever heard." # @t_samazona346.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " I'm definitely onto something.)" # @t_samazona347.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "That ringtone. You're a busy person..." # @t_samazona348.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ... But every time that ringtone plays, you drop everything you're doing." # @t_samazona349.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I just thought it was strange." # @t_samazona350.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_justice_laughter_nervous as aki
    t_ch_aki "Ahahahahaa! HAHAHAHA! It's just a CRAZY coincidence. Nidia says that coincidence is destiny... Maybe it's like a ... Coincidestiny!" # @t_samazona351.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Is she just... Saying whatever comes to mind?!" # @t_samazona352.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She's obviously not president of the Making Excuses Club.)" # @t_samazona353.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "Come on, let's get back to practicing..." # @t_samazona353.01 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    play sound "sfx/sentaisignal.ogg"
    t_ch_aki ".................." # @t_samazona354.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "......................" # @t_samazona355.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Go ahead. I'll be right here." # @t_samazona356.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "....................." # @t_samazona357.00 self.block='Last'
    show i_aki_justice_laughter_nervous as aki:
        # FadeEvent
        linear 0.33 alpha 0.0
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Siiigh. I guess I'll just read this play while I wait.)" # @t_samazona357.01 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Man... I can't believe I read Romeo & Juliet from cover to cover.)" # @t_samazona358.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(That Shakespeare dude was pretty messed up. And people talk about violence on TV... )" # @t_samazona359.00 self.block='Last'
    show i_amazona_default_smile as amazona:
        # FadeEvent
        linear 0.33 alpha 1.0
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "..................." # @t_samazona360.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(WHO IS THIS WARRIOR??!)" # @t_samazona361.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_amazona "Whew... Hey [slot_playerName]. Listen, I'm really sorry I took off like that. I wish I could explain it to you." # @t_samazona362.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "............." # @t_samazona363.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "...................AKI??!!!!!!!!" # @t_samazona364.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_akiquestion "Of course it is! Who else would..." # @t_samazona365.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...I be............" # @t_samazona366.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_amazona_default_shocked as amazona
    t_ch_akiquestion "AAAAAAAAAAAGH!" # @t_samazona367.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What" # @t_samazona368.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "What" # @t_samazona369.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What....." # @t_samazona370.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_blush as cousin
    with Dissolve(0.5)
    extend " Are you WEARING?!" # @t_samazona371.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It's very daring..." # @t_samazona372.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_akiquestion "I HAVE TO GO!" # @t_samazona373.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_amazona_default_shocked as amazona:
        # FadeEvent
        linear 0.33 alpha 0.0
    extend "{w=0.33}{nw}"
    t_ch_cousin "Aki!! Wait!" # @t_samazona374.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "AKI!" # @t_samazona375.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_laughter_nervous as aki:
        # FadeEvent
        linear 0.33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_aki "Oh.... HAHAHHAAHA! HI [slot_playerName]!" # @t_samazona376.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Aki... Why are you yelling?" # @t_samazona377.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "I'M NOT YELLING!" # @t_samazona378.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_distracted as aki
    t_ch_aki ".... Sorry." # @t_samazona379.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What was that all about?!" # @t_samazona380.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki ".................." # @t_samazona381.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "........................" # @t_samazona382.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.33 alpha 1.0
    show i_aki_akimbo_distracted as aki:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.35 
    show i_cousin_energetic_surprise_blush as cousin:
        # ShowWithAtl
        pause 0.33 
        ease_expo .33  xpos 0.12 
    extend "{w=0.66}{nw}"
    t_ch_digdug "STUDENTS... LOITERING IN THE HALL?!" # @t_samazona383.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Are you SKIPPING DETENTION?!" # @t_samazona384.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Erk!" # @t_samazona385.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_shocked as aki
    t_ch_aki "AHH!" # @t_samazona386.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "[slot_playerName]... I'm not surprised that a troublemaker like you is rejecting the very moral pillars of society..." # @t_samazona387.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "But dragging Aki into it... INSIDIOUS! DIABOLICAL!" # @t_samazona388.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_focus as aki
    t_ch_aki "Actually... I'm the one who's in detention for too many tardies and absences. It's more likely that it's my fault, isn't it?" # @t_samazona389.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "...................." # @t_samazona389.01 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "....... [slot_playerName]! Are you blackmailing this young lady?!" # @t_samazona389.02 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Why else would she give up her bright, shining future to defend your criminal acts?!" # @t_samazona389.03 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "No, actually I followed her out here--" # @t_samazona389.04 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_king_screaming as king zorder 0:
        xzoom -1.0 
        # ShowWithAtl
        linear 0.5 xpos 0.85 
        # FadeEvent
        linear 0.33 alpha 1.0
    play sound "sfx/kingroar2.ogg"
    extend "{w=0.5}{nw}"
    t_ch_king "(DETENTION!)" # @t_samazona389.06 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "King has passed judgement on you." # @t_samazona389.07 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Both of you get DETENTION LEVEL XV: CRYOGENIC SUSPENSION DETENTION!" # @t_samazona389.08 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But--" # @t_samazona389.09 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "LEVEL XVI!" # @t_samazona389.10 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin ".................." # @t_samazona389.11 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Are we done here?" # @t_samazona389.12 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "..................." # @t_samazona389.13 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_distracted as aki
    t_ch_aki "...... [slot_playerName].........." # @t_samazona389.14 self.block='Last'
    # <NHSceneChange {'name': '_1j', 'scene': 's_day4'} NHSceneChange ''>
    label s_amazona3__1j:
        # <NHSceneChange {'name': '_1j', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4