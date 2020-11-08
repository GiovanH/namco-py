# <Scene {'id': 's_albatros5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_albatros5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_albatros5"
    $ renpy.pause(1)
    # <Scene {'id': 's_albatros5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/privatetimes.ogg" loop
    show i_bg_library as bg zorder 0 at default
    show i_sw_black as curtain zorder 10:
        default
        alpha 0.7
    show i_albatross_toocool_smirk as albatros zorder 2:
        default
        alpha 1.0
        xpos 1.25 
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.25 
    t_ch_cousin "(The library isn’t usually this dark.)" # @t_salbatros50.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Hello?" # @t_salbatros50.01 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smirk as albatros:
        # ShowWithAtl
        linear 0.2 xpos 0.7 
    extend "{w=0.2}{nw}"
    t_ch_albatros "Ah, [slot_playerName]. I’m glad you could make it." # @t_salbatros51.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What’s..." # @t_salbatros52.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Is that you, Al?" # @t_salbatros53.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Have a seat." # @t_salbatros54.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What were you doing in the dark, Al?" # @t_salbatros55.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You can’t read in the dark!" # @t_salbatros56.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_staredown as albatros
    t_ch_albatros "I’m not here to read." # @t_salbatros57.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Except your rights!" # @t_salbatros58.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain:
        # FadeEvent
        linear 0.2 alpha 0.0
    extend "{w=0.2}{nw}"
    extend " TO YOU!" # @t_salbatros58.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Ah, so another criminal justice club meeting?)" # @t_salbatros59.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I can play along.)" # @t_salbatros510.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " My rights? You got nuthin’ on me, N.A.R.C.!" # @t_salbatros510.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " (Ha! That sounded pretty good! If I didn’t know any better, I might think I’m a criminal.)" # @t_salbatros510.02 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "We can do this the hard way or the easy way." # @t_salbatros511.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "It’s up to you, [slot_playerName]." # @t_salbatros512.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Bring it on, copper." # @t_salbatros513.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Do they say copper? Is that good slang?)" # @t_salbatros513.01 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_distraught as albatros
    t_ch_albatros "I didn’t want to have to do this, but…" # @t_salbatros514.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_distraught as albatros
    t_ch_albatros "YOU LEAVE ME NO OTHER CHOICE!" # @t_salbatros515.00 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Our agents have been tailing you for days. We know all about your vast criminal empire that you’ve expertly made to look exactly like the routine of a perfectly innocent Namco High student." # @t_salbatros516.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pictures "*INCRIMINATION LEVEL 300% COMBO BREAKER!!!*" # @t_salbatros517.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Those are just pictures of me walking to class." # @t_salbatros518.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pictures "*INCRIMINATION LEVEL 97%...?*" # @t_salbatros519.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m using the drinking fountain in this one." # @t_salbatros520.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " (And I look kinda cute in it too!)" # @t_salbatros520.01 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pictures "*INCRIMINATION LEVEL 3.7% :(*" # @t_salbatros521.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "This one is me sitting down at this table." # @t_salbatros522.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pictures "*INCRIMINATION LEVEL 75%!!!*" # @t_salbatros523.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And this one is appears to be an artist’s rendering of me selling crates full of “ammo hack cheat codes” to a gang of olde timey bank robbers, some banditos, what appears to be a vampire king, and a skeleton in a cape?" # @t_salbatros524.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_smirk as albatros
    t_ch_albatros "That’s Emperor Dracula and Super Skeleton." # @t_salbatros525.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_smirk_wink as albatros
    t_ch_albatros "They’re the main bad guys in my fanfic." # @t_salbatros526.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "And I’m not sure how that got in with those..." # @t_salbatros527.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_smug as albatros
    t_ch_pictures "*INCRIMINATION LEVEL 0.000%*" # @t_salbatros528.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Anyway. Besides that stuff, there’s even more evidence!" # @t_salbatros529.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "I’ll beat your wrap, fuzz." # @t_salbatros530.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Or is it a rap?)" # @t_salbatros530.01 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Well, whatever, it sounds the same! He’ll never know which one I meant!)" # @t_salbatros531.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_staredown as albatros
    t_ch_albatros "Ha! The sweet irony of it all. Everything you say digs you that much deeper." # @t_salbatros532.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "If you aren’t a big old crime kingpin, then why do you keep using criminal slang?" # @t_salbatros533.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Hmmm, that’s a good question!)" # @t_salbatros534.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’m playing the part of the criminal for this mock interrogation, so I’ve got to talk like a criminal.)" # @t_salbatros535.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(But if I was being interrogated for real, I couldn’t say that.)" # @t_salbatros536.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Gotta think like a criminal too!)" # @t_salbatros536.01 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I watch a lot of old gangster movies." # @t_salbatros537.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "A likely story." # @t_salbatros538.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Yeah, that’s why I used it!)" # @t_salbatros539.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Perhaps you would care to explain why you repeatedly thwarted the undercover operations of the top agents of the world’s top crime fighting agency?" # @t_salbatros540.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_inquisitive as albatros
    t_ch_albatros "Or do you expect us to believe that was all a big misunderstanding?" # @t_salbatros541.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Wow, I must be playing the part of some kinda international crime genius!)" # @t_salbatros542.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Like what’s-his-name from Sherlock Holmes.)" # @t_salbatros543.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Watson.)" # @t_salbatros544.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Kind of ambitious for a high school club...)" # @t_salbatros545.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Are you telling me my crime is that you can’t figure out if I did a crime?" # @t_salbatros545.01 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That hardly seems fair, Officer Tross." # @t_salbatros546.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Oh, man. Really feel like I’m nailing this part.)" # @t_salbatros546.01 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Maybe I should’ve joined the Drama Club!)" # @t_salbatros547.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "I..." # @t_salbatros548.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "We…" # @t_salbatros549.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "You did it, [slot_playerName]." # @t_salbatros550.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_distraught as albatros
    t_ch_albatros "You defeated the World Crime Police Organization." # @t_salbatros551.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Moreover, you defeated…" # @t_salbatros552.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    extend " THEIR TOP AGENT!" # @t_salbatros552.01 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…?" # @t_salbatros553.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "ME!" # @t_salbatros554.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…?!" # @t_salbatros555.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_distraught as albatros
    t_ch_albatros "I don’t think you appreciate the depth of this reveal." # @t_salbatros556.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "This would be the moment where, if I was wearing a mask, I’d take it off." # @t_salbatros557.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "That’d probably help you process how dramatic it is right now." # @t_salbatros558.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Are we still doing the mock interrogation?" # @t_salbatros559.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_staredown as albatros
    t_ch_albatros "You can drop the act, [slot_playerName]." # @t_salbatros560.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "We don’t have a case against you. You’ve defeated our every effort to build one." # @t_salbatros561.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Al? What are you saying?" # @t_salbatros562.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smug as albatros
    t_ch_albatros "I’m not ORDINARY STUDENT Alfonso “Al” B. Tross of the N.A.R.C. club." # @t_salbatros563.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smug as albatros
    t_ch_albatros "I am AGENT ALBATROSS!" # @t_salbatros564.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "I’ve been on a sting operation to crack down on the cheat code trafficking ring centered on Namco High." # @t_salbatros565.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Our intel put you at the center of that ring." # @t_salbatros566.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "So, you…" # @t_salbatros567.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "You were lying to me all along?" # @t_salbatros568.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_inquisitive as albatros
    t_ch_albatross "Undercover work is never simple." # @t_salbatros569.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Loyalties are tested." # @t_salbatros570.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Friendships are formed." # @t_salbatros571.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "And then..." # @t_salbatros572.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_distraught as albatros
    extend " ...betrayed." # @t_salbatros572.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "At first I was merely collecting evidence to use against you." # @t_salbatros573.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "But in time…" # @t_salbatros574.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "I…" # @t_salbatros575.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_distraught as albatros
    t_ch_albatross "I almost fell for the [slot_playerName] you pretend to be." # @t_salbatros576.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "That persona you hide behind to mastermind all the cheat code crimes in Namco Land with impunity!" # @t_salbatros577.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "But that’s not a persona." # @t_salbatros578.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m just me." # @t_salbatros579.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I only pretended to know about cheat codes or whatever because I thought it was part of the criminal justice club!" # @t_salbatros580.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Also, uh…" # @t_salbatros581.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " For some of it?" # @t_salbatros581.01 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral_blush as cousin
    extend " I thought it was flirting." # @t_salbatros581.02 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Ahem. But yeah." # @t_salbatros582.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I, uh, you got the wrong person. I’m just a student." # @t_salbatros583.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Heck, I’m new here! I don’t know enough people in school to organize a vast student criminal empire." # @t_salbatros584.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_inquisitive as albatros
    t_ch_albatross "The wrong person?" # @t_salbatros585.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Could it be?" # @t_salbatros586.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Was the intel wrong?" # @t_salbatros587.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "Uh. Sorry?" # @t_salbatros588.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "No! No, don’t be." # @t_salbatros589.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "If the mission parameters were wrong from the start, then the operation’s failure isn’t on my shoulders!" # @t_salbatros590.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smirk as albatros
    t_ch_albatross "And, more importantly, I wasn’t outsmarted by a high school student!" # @t_salbatros591.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But, sort of, you totally were." # @t_salbatros592.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "And not even on purpose!" # @t_salbatros593.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smug as albatros
    t_ch_albatross "That’s...true." # @t_salbatros594.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Isn’t it?" # @t_salbatros595.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Ack! I should’ve said that to myself.)" # @t_salbatros596.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Change the subject!)" # @t_salbatros597.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    extend " Um, were you really falling for me though?" # @t_salbatros597.01 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smug as albatros
    t_ch_albatross "Well." # @t_salbatros598.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smirk_wink as albatros
    t_ch_albatross "Maybe a little?" # @t_salbatros599.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_staredown as albatros
    t_ch_albatross "It’s unprofessional though!" # @t_salbatros5100.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Anyway, I don’t even go to this high school anymore." # @t_salbatros5101.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You used to be a student here?" # @t_salbatros5102.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_inquisitive as albatros
    t_ch_albatross "Of course. It’s why I was selected for this operation." # @t_salbatros5103.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "I came back under the completely plausible but false identity of ALFONSO “AL” B. TROSS." # @t_salbatros5104.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "So...you’re not much older than me…?" # @t_salbatros5105.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "I graduated last year." # @t_salbatros5106.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "So, uh. No." # @t_salbatros5107.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Not much at all." # @t_salbatros5108.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "That’s cool." # @t_salbatros5109.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Oh, man. Am I gonna go for it?)" # @t_salbatros5109.01 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Is this even the right time to go for it?)" # @t_salbatros5110.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I should wait.)" # @t_salbatros5111.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (But what if I wait too long!)" # @t_salbatros5111.01 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_inquisitive as albatros
    t_ch_albatross "The cheat code kingpin is still out there. Somewhere." # @t_salbatros5112.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_staredown as albatros
    t_ch_albatross "Outsmarting me." # @t_salbatros5113.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_distraught as albatros
    t_ch_albatross "Like you did." # @t_salbatros5114.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Except on purpose probably." # @t_salbatros5115.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_distraught as albatros
    t_ch_albatross "Guess I’ve still got a lot to learn about being a superspy…" # @t_salbatros5116.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "I must look like a complete idiot and nothing like an incredibly dashing hero who saved the world once." # @t_salbatros5117.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well." # @t_salbatros5118.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You look a little dashing." # @t_salbatros5119.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smirk as albatros
    t_ch_albatross "Heh." # @t_salbatros5120.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "That’s just the jacket." # @t_salbatros5121.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Also the hair and smile!)" # @t_salbatros5122.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Maybe it’s time to face the facts." # @t_salbatros5123.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral_blush as cousin
    t_ch_cousin "(And the eyes.)" # @t_salbatros5124.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_distraught as albatros
    t_ch_albatross "I’m not cut out for this dangerous game of undercover cat and mouse where you infiltrate the mouse hole to get to the head mouse behind all the cheese smuggling." # @t_salbatros5125.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "And then, uh, eat that mouse?" # @t_salbatros5126.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How do you work arresting into this metaphor?" # @t_salbatros5126.01 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "What are you saying, Al?" # @t_salbatros5127.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "The cheat code kingpin has won." # @t_salbatros5128.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Whomever it is..." # @t_salbatros5128.01 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Because I’m giving up the case." # @t_salbatros5129.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_albatross "Because…" # @t_salbatros5130.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_distraught as albatros
    extend " I AM A SECRET AGENT NO MORE!" # @t_salbatros5130.01 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You can’t just give up!" # @t_salbatros5131.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You’re really good at agent-ing around!" # @t_salbatros5132.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "If that were true, I would’ve captured the cheat coder by now!" # @t_salbatros5133.00 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_pacman_left as pacman:
        default
        xpos 1.35 
        # ShowWithAtl
        easeout 5 xpos 0.8 
    $ renpy.pause(2)
    # <ParallelEvent {'delay': '2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_inquisitive as albatros:
        # ShowWithAtl
        linear .25 xpos 0.3 
    $ renpy.pause(0.25) # TimedPause
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear .25 xpos 0.15 
    extend "{w=5.0}{nw}"
    t_ch_cousin "(?!?)" # @t_salbatros5134.00 self.block='Last'
    stop sound
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(What’s Pac-Man doing here???)" # @t_salbatros5135.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "I heard what Albatross said." # @t_salbatros5136.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Did Pac-Man just answer my thoughts?)" # @t_salbatros5137.00 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Can he read minds?!?!?)" # @t_salbatros5138.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "(Yes, [slot_playerName]. I can.)" # @t_salbatros5139.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(?!?!?!?!?!?)" # @t_salbatros5140.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_distraught as albatros
    t_ch_albatross "Not even you can talk me out of it, Pac-Man." # @t_salbatros5141.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "I hereby renounce being a really cool spy!" # @t_salbatros5142.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "Be true to yourself." # @t_salbatros5143.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "I’m gonna get some shabby clothes!" # @t_salbatros5144.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Pac-Man, don’t let him!" # @t_salbatros5145.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "And not style my hair at all." # @t_salbatros5146.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "And…" # @t_salbatros5147.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "And other stuff too." # @t_salbatros5148.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "You can’t do any of that." # @t_salbatros5149.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_pacman "It’s not who you are." # @t_salbatros5150.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_distraught as albatros
    t_ch_albatross "It might be." # @t_salbatros5151.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "I might enjoy looking like a slob. And not going on adventures." # @t_salbatros5152.00 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "And not saving the world and looking great while I do it." # @t_salbatros5153.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Al, listen to yourself!" # @t_salbatros5154.00 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "It might not be the living nightmare it sounds like!" # @t_salbatros5155.00 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "It might actually be the best!" # @t_salbatros5156.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But if you do all that, you’ll become a gross guy with no confidence instead of the suave man of action I fell for!" # @t_salbatros5157.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "You…" # @t_salbatros5158.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_inquisitive as albatros
    t_ch_albatross "Really?" # @t_salbatros5159.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Uh. Whoops?)" # @t_salbatros5160.00 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    extend " Well!" # @t_salbatros5160.01 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh. Kinda. Yeah." # @t_salbatros5161.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "I’m not sure how I feel about that…" # @t_salbatros5162.00 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_smirk as albatros
    t_ch_albatross "But I know I could never interest someone like [slot_playerName] if I thought so little of myself that I’d go around in public with a neckbeard and unwashed hair!" # @t_salbatros5163.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "No!" # @t_salbatros5164.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "I won’t do it!" # @t_salbatros5165.00 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk_wink as albatros
    t_ch_albatross "I AM ALBATROSS! THE BEST SECRET AGENT IN THE ENTIRE WORLD CRIME POLICE ORGANIZATION!" # @t_salbatros5166.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "Well, but that’s twice now you’ve yelled about it." # @t_salbatros5167.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Not too sure how secret it is anymore." # @t_salbatros5168.00 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Hm, right." # @t_salbatros5169.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_smirk_wink as albatros
    t_ch_albatross "I’ll have to work on that." # @t_salbatros5170.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Thank you, Pac-Man." # @t_salbatros5171.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatross "Being true to myself is great!" # @t_salbatros5172.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        easein 5 xpos 1.35 
    show i_cousin_default_mortified as cousin
    extend "{w=5.0}{nw}"
    t_ch_pacman "You were a fool to doubt me." # @t_salbatros5173.00 self.block='Last'
    # <NHSceneChange {'name': '_3B', 'scene': 's_day5.5'} NHSceneChange ''>
    label s_albatros5__3B:
        # <NHSceneChange {'name': '_3B', 'scene': 's_day5.5'} NHSceneChange ''>
        jump s_day5p5