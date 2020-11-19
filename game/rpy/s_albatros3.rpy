# <Scene scene {'id': 's_albatros3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_albatros3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_albatros3"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_albatros3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/upbeat.ogg" loop
    show i_bg_rooftop as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_albatross_welcome_smirk_wink as albatros zorder 2:
        default
        alpha 1.0
        xpos 1.4 
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    t_ch_cousin "(Hmm, Al said he’d be up here…)" # @t_salbatros30.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Maybe I missed him.)" # @t_salbatros31.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Unless he’s in disguise!)" # @t_salbatros32.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(As a, uh, hmm. One of those twirly roof vent things?)" # @t_salbatros33.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    show i_albatross_welcome_smirk_wink as albatros:
        # ShowWithAtl
        linear .5 xpos 0.7 
    extend "{w=0.5}{nw}"
    t_ch_albatros "[slot_playerName]." # @t_salbatros34.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Or I was a little early.)" # @t_salbatros35.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_smirk as albatros
    t_ch_albatros "I thought you’d be here." # @t_salbatros36.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "You told me to meet you here, so yeah." # @t_salbatros37.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "You always do what you’re told?" # @t_salbatros38.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Sometimes I never do what I’m told." # @t_salbatros39.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Some other times, I always do." # @t_salbatros310.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Yeah, way to sound mysterious, [slot_playerName]!)" # @t_salbatros311.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(That makes you all kinds of alluring.)" # @t_salbatros312.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "You’re quite a mystery, [slot_playerName]." # @t_salbatros313.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Ha! I knew it!)" # @t_salbatros314.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_inquisitive as albatros
    t_ch_albatros "I brought you up here for a reason." # @t_salbatros315.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Probably for his criminal justice club.)" # @t_salbatros316.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Ooh, maybe we’re doing a stakeout!)" # @t_salbatros317.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "I wanted you to meet a “friend” of mine." # @t_salbatros318.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Whoa, introducing me to his friends already?)" # @t_salbatros319.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Things are moving so fast!)" # @t_salbatros320.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "Only problem is…" # @t_salbatros321.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_welcome_staredown as albatros
    extend " ...SHE’S A CRIMINAL!" # @t_salbatros321.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Oh no! And you’re in the criminal justice club!" # @t_salbatros322.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "SO CONFLICTED!" # @t_salbatros323.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Being conflicted is a very romantic and grown up thing to do.)" # @t_salbatros323.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "(It’s like Al is a film noir protagonist!)" # @t_salbatros324.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I guess! Dunno, film studies is more like a college thing after all.)" # @t_salbatros325.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(But it sounds good!)" # @t_salbatros326.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_welcome_smug as albatros
    t_ch_albatros "So, when you meet, you’ll have to give her the secret criminal handshake or she won’t trust you." # @t_salbatros327.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wow, I was right the first time.)" # @t_salbatros328.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This is so a stakeout!)" # @t_salbatros329.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "I brought you up here so you could show me the handshake in private." # @t_salbatros330.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_fistinhand_inquisitive as albatros:
        linear .2 xzoom -1.0 
    t_ch_albatros "Where no one else in school would see it and then enter the world of crime." # @t_salbatros331.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "The secret criminal handshake..." # @t_salbatros332.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (How am I supposed to show Al how to do a thing I don’t even know?!)" # @t_salbatros332.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Um. Sure." # @t_salbatros333.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It goes like…" # @t_salbatros334.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin:
        # ShowWithAtl
        linear .2 xpos 0.35 
    extend "{w=0.2}{nw}"
    extend " (Uh, ummmmmmm. Just make it up! Here goes nothing.)" # @t_salbatros334.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "You start by going up." # @t_salbatros335.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "And then, um. Further up." # @t_salbatros336.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "That’s the key to it. So you know something is “UP.” Like the jig maybe. That’s criminal talk." # @t_salbatros337.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.1 xpos 0.34 
    extend "{w=0.1}{nw}"
    t_ch_cousin "And then, uh, because you’re so high up now, you have to bring it back down." # @t_salbatros338.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Can’t believe I’m holding hands with Al already!)" # @t_salbatros338.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I guess technically we’re not REALLY holding hands…)" # @t_salbatros339.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(But technically we are too!)" # @t_salbatros340.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    extend " (Um. Where was I with the handshake?)" # @t_salbatros340.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Oh, right!)" # @t_salbatros341.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    extend " Uh, yeah. So, then you take it down a notch." # @t_salbatros341.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_fistinhand_inquisitive as albatros:
        # ShowWithAtl
        linear .2 xpos 0.65 
    extend "{w=0.2}{nw}"
    t_ch_albatros "Down again?" # @t_salbatros342.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Uh, sure. Yeah." # @t_salbatros343.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Did I do two downs by accident? Oh, whatever!)" # @t_salbatros343.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.1 xpos 0.32 
    extend "{w=0.1}{nw}"
    t_ch_cousin "And then you sort of go to the left with it." # @t_salbatros344.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.1 xpos 0.34 
    extend "{w=0.1}{nw}"
    t_ch_cousin "Uh, and then back right." # @t_salbatros345.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Because if you kept going left it’d look a little weird." # @t_salbatros346.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.1 xpos 0.32 
    extend "{w=0.1}{nw}"
    t_ch_cousin "But then you do it again so they know it wasn’t a fluke." # @t_salbatros347.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_fistinhand_distraught as albatros
    t_ch_albatros "What, left and right twice then?" # @t_salbatros348.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Uh…?" # @t_salbatros349.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Yeah." # @t_salbatros350.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (I guess!)" # @t_salbatros350.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "And then you finish it up by going “Big Another Start.”" # @t_salbatros351.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And, like, normal people will just think it’s nonsense. But another criminal would know what you meant was the same words only reversed." # @t_salbatros352.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_notebook_staredown as albatros:
        linear 0.25 xzoom 1.0 
    t_ch_cousin "“Start Another Big.”" # @t_salbatros353.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "And the response they give to that is “Crime.”" # @t_salbatros354.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "And THAT is your criminal code." # @t_salbatros355.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Hey, that sounded pretty good!)" # @t_salbatros356.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Boy, Al sure is taking a lot of notes.)" # @t_salbatros357.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_staredown as albatros
    t_ch_albatros "Even the handshake of crime is devious!" # @t_salbatros358.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(I will just assume I randomly guessed it completely right!)" # @t_salbatros359.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(WHAT WERE THE ODDS!)" # @t_salbatros360.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_smirk as albatros
    t_ch_albatros "I think you’re ready to meet my “friend.”" # @t_salbatros361.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "Let’s go to the secret criminal meeting place." # @t_salbatros362.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Skipping school AND leaving school grounds?!)" # @t_salbatros363.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This is truly dangerous stuff we’re up to.)" # @t_salbatros364.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0) # Curtain fade
    show i_bg_cafe as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_cafe', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_1C', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_fistinhand_smirk as albatros:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Are we stopping for a latte?" # @t_salbatros365.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_welcome_smirk as albatros
    t_ch_albatros "This is the secret criminal hangout spot." # @t_salbatros366.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "It’s why we hold all the criminal justice club meetings here." # @t_salbatros367.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(That makes sense.)" # @t_salbatros368.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(In a way…?)" # @t_salbatros369.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "I’ll introduce you to my “friend.”" # @t_salbatros370.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_smug as albatros
    t_ch_albatros "You’ll give her the criminal code handshake." # @t_salbatros371.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "And then you guys just...talk." # @t_salbatros372.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "Freely and as if no one is recording you for evidence." # @t_salbatros373.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Ha! That’s easy. I talk like that all the time!)" # @t_salbatros374.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin:
        # ShowWithAtl
        linear 0.25 xpos 0.22 
    show i_albatross_toocool_smug as albatros:
        # ShowWithAtl
        linear 0.25 xpos 0.78 
    show i_connie_neutral as connie zorder 1:
        default
        alpha 0.0
        xpos 0.55 
    extend "{w=0.25}{nw}"
    t_ch_albatros "Here she is." # @t_salbatros375.00 self.block='Last'
    show i_connie_neutral as connie:
        # FadeEvent
        linear 0.33 alpha 1.0
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "[slot_playerName]. Meet Codename Condor." # @t_salbatros376.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Sheesh, and I thought Galaga Ship was a dumb name.)" # @t_salbatros377.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_smirk_wink as albatros
    t_ch_condor "You know that’s not my name, AL." # @t_salbatros378.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_distraught as albatros
    t_ch_albatros "I MEAN CONNIE!" # @t_salbatros379.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_condorconnie "Hrm." # @t_salbatros380.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_toocool_inquisitive as albatros
    t_ch_condorconnie "Anyway. Hello, [slot_playerName]." # @t_salbatros381.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Pleased to meet you." # @t_salbatros382.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Wait! Maybe I shouldn’t be so polite.)" # @t_salbatros382.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Are criminals polite to one another as a matter of course?)" # @t_salbatros383.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Honor among thieves, that’s totally a saying, right?)" # @t_salbatros384.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Maybe that extends to basic manners too?)" # @t_salbatros385.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "I’ll just leave you two alone. I’m sure you and Codename Connie have a lot to talk about." # @t_salbatros386.00 self.block='Last'
    show i_albatross_fistinhand_smirk_wink as albatros:
        # ShowWithAtl
        linear 2 xpos 1.06 
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_codenameconnie "It’s JUST Connie, ALFONSO." # @t_salbatros387.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "Right. Yes. Sorry." # @t_salbatros388.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_albatros "My friend. Connie." # @t_salbatros389.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_conniequestion "Thank you." # @t_salbatros390.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_conniequestion "We can speak without reservation now that Al left us alone and is not hiding with remote listening devices to pick up on criminal activity." # @t_salbatros391.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Ha! She doesn’t suspect a thing!)" # @t_salbatros392.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "[slot_playerName], I’m just a fellow student of your Namco High." # @t_salbatros393.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Really? I haven’t seen you in class..." # @t_salbatros394.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Because er, ah, I skip…" # @t_salbatros395.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " EVERY CLASS!" # @t_salbatros395.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Whoa! Connie must be one of those troublemakers!)" # @t_salbatros396.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (And that’s why she has all those aliases!)" # @t_salbatros396.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified as cousin
    extend " (And since Al’s club is all about stopping troublemakers…)" # @t_salbatros396.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "(I bet he’s gonna take her down!)" # @t_salbatros397.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "(And he’s brought me along for back up!)" # @t_salbatros398.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wow!)" # @t_salbatros399.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Better play it cool.)" # @t_salbatros3100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Yeah? That’s no big deal." # @t_salbatros3100.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I skip classes I don’t even have." # @t_salbatros3101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Wow. Hard core. I figured we would have a lot in common." # @t_salbatros3102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Therefore, I feel very comfortable talking with you about..." # @t_salbatros3103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " CHEAT CODES!" # @t_salbatros3103.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Ah-ha! Now I get it!)" # @t_salbatros3104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Al wants me to play the part of a cheat code dealer.)" # @t_salbatros3105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(And then we’ll catch Connie in the act of trying to trade cheat codes with me.)" # @t_salbatros3106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(And then we’ll have her arrested and make the club look really productive!)" # @t_salbatros3107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wow, this is so high-stakes! Al must really trust and like me.)" # @t_salbatros3108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Uh, yeah." # @t_salbatros3108.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Cheat codes." # @t_salbatros3109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I totally know so much about those." # @t_salbatros3110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Good." # @t_salbatros3111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Knowing about those is what I was hoping to hear." # @t_salbatros3112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "But let’s do the criminal code handshake before we get down to business." # @t_salbatros3113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I don’t remember what I did for the handshake at all!)" # @t_salbatros3114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Um." # @t_salbatros3114.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "No." # @t_salbatros3115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "No?" # @t_salbatros3116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Hahaha!" # @t_salbatros3117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "[slot_playerName], you passed the final criminal code test." # @t_salbatros3118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " USING RUDENESS!" # @t_salbatros3118.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(I KNEW IT!!!)" # @t_salbatros3119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Okay, then. My gang could use some cheat codes." # @t_salbatros3120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(SHE’S IN A GANG?????)" # @t_salbatros3121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(This is serious business!)" # @t_salbatros3122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "And then we would use the cheat codes like weapons against other gangs and maybe the police." # @t_salbatros3123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Because we’re bad." # @t_salbatros3124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(You said it, lady!)" # @t_salbatros3125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(No wonder Al wants to put her behind bars.)" # @t_salbatros3126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Therefore as a plausible result of the things I just said, I’d be willing to pay top coin for cheat codes." # @t_salbatros3127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "For my criminal gang." # @t_salbatros3128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "If someone knew where to get them, that is." # @t_salbatros3129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(It’s all on me now!)" # @t_salbatros3130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " (Gosh, this is such a cool club.)" # @t_salbatros3130.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(And Al’s such a cool guy. And he’s really into me and oh crud.)" # @t_salbatros3131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Need to keep my head in the game!)" # @t_salbatros3132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Ahem.)" # @t_salbatros3133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Yeah. Cheat codes. Sure." # @t_salbatros3133.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I’ve heard of those and know how they work." # @t_salbatros3134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Yes. Good. I’d like some." # @t_salbatros3135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Um. Bad ones." # @t_salbatros3136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Well, I mean, GOOD ones. Like, they should work." # @t_salbatros3137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "But you’d only use them if you’re a bad person trying to get away with a big ol’ crime is what I’m saying." # @t_salbatros3138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Like MURDER?!?!)" # @t_salbatros3139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Like ripping the tag off a mattress." # @t_salbatros3140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Oh." # @t_salbatros3141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Or something bigger." # @t_salbatros3142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Like...embezzling pensions." # @t_salbatros3143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Or committing mail fraud." # @t_salbatros3144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Or “retiring” from a high paying corporate position only to receive a hefty “consultation” fee from the same firm in perpetuity while courting the very politicians who determine the policy that regulates the same industry you used to blah blah blah" # @t_salbatros3145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(I’m not following any of this! But it sure sounds dangerous but also like something that’d be on the news probably?)" # @t_salbatros3146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Connie is the most mature criminal I’ve ever met!)" # @t_salbatros3147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Also the only one.)" # @t_salbatros3148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Yeah, sure." # @t_salbatros3148.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You want to equip your gang with the cheat codes." # @t_salbatros3148.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "So you can break the law some more." # @t_salbatros3149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I dig it, daddio." # @t_salbatros3150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Is that even a criminal lingo???)" # @t_salbatros3150.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_connie "Then let’s deal some cheat codes with one another." # @t_salbatros3151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Yes. Let us." # @t_salbatros3152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Yes, I ordered the latte." # @t_salbatros3153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Thank you." # @t_salbatros3154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Wait, what’s Principal Dig Dug doing here?!)" # @t_salbatros3155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_digdug_left as digdug zorder 3:
        default
        xpos 1.3 
        alpha 1.0
    t_ch_cousin "(An innocent life is caught in the middle of our criminal dealings!)" # @t_salbatros3156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_albatross_fistinhand_smirk_wink as albatros:
        # ShowWithAtl
        linear .2 xpos 1.2 
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear .2 xpos 0.22 
    show i_connie_neutral as connie:
        # ShowWithAtl
        linear .2 xpos 0.06 
        xzoom -1.0 
    show i_digdug_left as digdug:
        # ShowWithAtl
        linear .2 xpos 0.75 
    extend "{w=0.2}{nw}"
    t_ch_digdug "[slot_playerName]?" # @t_salbatros3157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Oh no!)" # @t_salbatros3158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_30', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Don’t panic, [slot_playerName]!)" # @t_salbatros3159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_31', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Just use your criminal mind to construct a lie.)" # @t_salbatros3160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_32', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(You can do this!)" # @t_salbatros3161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_33', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Uh. Nope?" # @t_salbatros3161.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_34', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Hm. That lie could’ve been a little more fleshed out I guess.)" # @t_salbatros3161.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_35', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "This is the most flagrant instance of skipping I’ve seen in all my years of principal-ing!" # @t_salbatros3162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_36', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_connie_neutral as connie:
        # ShowWithAtl
        linear .2 xpos 0.02 
    extend "{w=0.2}{nw}"
    t_ch_digdug "You’re in for the deadliest detention of them all." # @t_salbatros3163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_37', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "BATTLEDOME DETENTION!" # @t_salbatros3164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_38', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(WHAT?!?!)" # @t_salbatros3165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_39', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_connie_neutral as connie:
        # ShowWithAtl
        linear .2 xpos -0.03 
    extend "{w=0.2}{nw}"
    t_ch_digdug "You probably haven’t heard of it because…" # @t_salbatros3166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " NO ONE HAS EVER SURVIVED ITS RIGORS!" # @t_salbatros3166.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Or been sent to it yet. It’s new." # @t_salbatros3167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_connie_neutral as connie:
        # ShowWithAtl
        linear .2 xpos -0.06 
    extend "{w=0.2}{nw}"
    t_ch_cousin "You can’t do this to me!" # @t_salbatros3168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Oh, man. I hate to disappoint Al and blow the whole sting operation, but I can’t duel to the death. I like living too much!)" # @t_salbatros3168.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    extend " I’m here on official school club spirit building business!" # @t_salbatros3168.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_connie_neutral as connie:
        # ShowWithAtl
        linear .2 xpos -0.08 
    extend "{w=0.2}{nw}"
    t_ch_digdug "I am suspicious but listening." # @t_salbatros3169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "For the Namco Anti Real Crime club!" # @t_salbatros3170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_connie_neutral as connie:
        # ShowWithAtl
        linear .2 xpos -0.25 
    extend "{w=0.2}{nw}"
    t_ch_cousin "I’m doing a sting!" # @t_salbatros3171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        linear .2 xzoom -1.0 
    t_ch_cousin "Sorry, Connie." # @t_salbatros3172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    extend " (What the--!!!)" # @t_salbatros3172.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (She’s already gone???)" # @t_salbatros3172.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin:
        linear .2 xzoom 1.0 
    t_ch_digdug "Namco Anti Real Crime club, eh?" # @t_salbatros3173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_digdug "It’s a shame there isn’t a fiction club. Because you could be its president!" # @t_salbatros3174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Well, vice president, because of Aki." # @t_salbatros3175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "But the takeaway is that there is no such thing as a Namco Anti Real Crime club!" # @t_salbatros3176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "That’s crazy! Al B. Tross is in the club too." # @t_salbatros3177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "You think piling lie on top of lie will make the original lie stick." # @t_salbatros3178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "But it won’t work for one very simple but incredibly dramatic reason." # @t_salbatros3179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " THERE HASN’T BEEN AN AL B. TROSS ENROLLED AT NAMCO HIGH FOR THIRTY YEARS!!!" # @t_salbatros3179.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(WAS AL A GHOST ALL ALONG?!?!?!)" # @t_salbatros3180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Nor has there ever been an Al B. Tross enrolled at Namco High. Ever." # @t_salbatros3181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(So…)" # @t_salbatros3182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Wait, not a ghost? What?)" # @t_salbatros3183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Yes, one of my hobbies is to memorize enrollment records." # @t_salbatros3184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "You might think that’s crazy. Plenty do." # @t_salbatros3185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "But I couldn’t have cracked the Case Of The [slot_playerName] Who Lies About Clubs While Skipping Class without that knowledge!" # @t_salbatros3186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(There’s clearly some kind of confusion here about attendance and record keeping practices. But that’s a mystery for another time.)" # @t_salbatros3187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Right now I JUST DON’T WANNA DO A BATTLEDOME!!!)" # @t_salbatros3188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Uh, er. You can’t take me in for skipping class." # @t_salbatros3188.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "We’re off school grounds. You have no authority here!" # @t_salbatros3189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Ah-ha! The ol’ legal mumbo jumbo trick!)" # @t_salbatros3189.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "That’s true…" # @t_salbatros3190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Whew!)" # @t_salbatros3191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Off of school grounds, I have no legal right to invoke THE BATTLEDOME." # @t_salbatros3192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Despite my frequent lobbying to the contrary..." # @t_salbatros3193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "In light of these findings, I shall commute your sentence to a mere Double Detention." # @t_salbatros3194.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_3k', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
    label s_albatros3__3k:
        # <NHSceneChange NHSceneChange {'name': '_3k', 'scene': 's_day4', 'kind': 'NHSceneChange'} ''>
        jump s_day4