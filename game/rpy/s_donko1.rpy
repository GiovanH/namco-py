# <Scene {'id': 's_donko1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_donko1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_donko1"
    $ renpy.pause(1)
    # <Scene {'id': 's_donko1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/school.ogg" loop
    show i_bg_hallway_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_sw_black as darkness zorder 3:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 4:
        default
        xpos 0.25 
    show i_hiromi_stand_smile as hiromi zorder 2:
        default
        alpha 0.0
        xpos 0.75 
    show i_donko_default_wink as donko zorder 2:
        default
        xpos 0.75 
        alpha 1.0
    show i_galaga_default as galaga zorder 2:
        default
        xpos 0.75 
        alpha 0.0
    show i_aki_default_smile as aki zorder 2:
        default
        xpos 0.75 
        alpha 0.0
    show i_bluemax_stand_smile as bluemax zorder 2:
        default
        xpos 0.75 
        alpha 0.0
    t_ch_donko "If you INSIST on joining me at Band Club…" # @t_sdonko122.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ll have to show you where it is. They hold it in the auditorium." # @t_sdonko122.01 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "You probably don’t even know where that is yet!" # @t_sdonko123.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_grin as donko
    extend " Poor little new kid. Don’t worry, I’ll show you around!" # @t_sdonko123.01 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I know where it is! I had to go through it to roll up all that equipment on my katamari." # @t_sdonko124.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "[slot_playerName], when a cute and popular girl is saying she’ll show you around…" # @t_sdonko125.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "You don’t turn it down!" # @t_sdonko126.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I might think Donko is full of herself…" # @t_sdonko127.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " But she actually is super adorable.)" # @t_sdonko127.01 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Now [slot_playerName]…" # @t_sdonko128.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    extend " I totally know what you’re thinking." # @t_sdonko128.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "WHAT?! You do?!" # @t_sdonko129.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Yeah! You’re thinking…" # @t_sdonko130.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_grin as donko
    extend " “Why is the most popular student at Namco High in a dorky club like Band?!”" # @t_sdonko130.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Well… the truth is… I just like it, okay?!" # @t_sdonko131.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And besides, I’m so cute and popular, I can actually pull off dorky stuff once in a while." # @t_sdonko131.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic as donko
    t_ch_donko "Now YOU being in Band, on the other hand…" # @t_sdonko132.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_crying_comic as donko
    extend " Poor [slot_playerName]! Who knows if your reputation will ever recover!" # @t_sdonko132.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Band isn’t THAT dorky, is it?" # @t_sdonko133.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko
    t_ch_donko "Tee-hee! You poor lost little lamb." # @t_sdonko134.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    extend " You really don’t know anything about what’s cool and uncool, do you?" # @t_sdonko134.01 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Don’t worry! I’ll sort you out." # @t_sdonko134.02 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Besides… do you really expect people to be surprised that, um…" # @t_sdonko135.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Someone like YOU is in Band?" # @t_sdonko136.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic as donko
    t_ch_donko "What…" # @t_sdonko137.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What’s THAT supposed to mean?!" # @t_sdonko137.01 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "...Oh!" # @t_sdonko138.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Nothing!" # @t_sdonko138.01 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Nevermind!" # @t_sdonko138.02 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Omigosh, was that totally offensive of me?!)" # @t_sdonko139.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Don’t be weird, [slot_playerName]!" # @t_sdonko140.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Weird kids are NEVER popular!" # @t_sdonko140.01 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_stage_cardboard as bg # behind curtain
    # <SettingChange {'auto': 'true', 'bgImage': '@i_bg_stage_cardboard', 'curtainFadeTime': '1', 'name': '_W'} SettingChange ''>
    # <Events {} events ''>
    show i_donko_ygg_grin as donko:
        # ShowWithAtl
        linear 0.5 xpos 0.37 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.13 
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Okay… here we are." # @t_sdonko141.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_smile as aki:
        # ShowWithAtl
        linear .33 alpha 1.0
    extend "{w=0.33}{nw}"
    t_ch_donko "Hiiii, Aki!" # @t_sdonko142.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We’re not late, are we?" # @t_sdonko142.01 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I brought a new recruit!" # @t_sdonko142.02 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "Hi Donko!" # @t_sdonko143.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I love what you’ve been doing with your hair lately." # @t_sdonko143.01 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Oh wait- you don’t have any!" # @t_sdonko143.02 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(That’s pretty rude...)" # @t_sdonko144.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "Oh girl! At least I don’t have a horrible dye job like you!" # @t_sdonko145.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_laughter_nervous as aki
    t_ch_aki "I heard Wada-Don dumped you again! I’m so sorry! Not that anyone is surprised…" # @t_sdonko146.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(YIKES!)" # @t_sdonko147.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Oh, it was mutual. We’re still buds!" # @t_sdonko148.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But it’s not your fault you don’t understand- you’ve only dated LOSERS after all!!!" # @t_sdonko148.01 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_akimbo_laughter as aki
    show i_donko_ygg_grin as donko
    t_ch_donkoandaki "Ha ha ha ha ha ha ha!" # @t_sdonko149.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Oh, you’re so FUNNY!" # @t_sdonko150.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_aki "No way, YOU’RE so funny!" # @t_sdonko151.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Is this what they call… Frenemies?!)" # @t_sdonko152.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_smile as aki
    t_ch_aki "I can’t stay too long today." # @t_sdonko153.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Very busy with homework." # @t_sdonko153.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Would it be acceptable if I performed my solo now, to get it out of the way?" # @t_sdonko153.02 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Go ahead, girl! Do what you gotta do!" # @t_sdonko154.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    show i_aki_tuba_focus as aki
    t_ch_cousin "(Aki’s taking out her instrument… a tuba?!" # @t_sdonko155.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s huge… I would’ve expected something small and classy, like a violin…)" # @t_sdonko156.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_tuba_smile as aki
    stop music fadeout 1.0
    t_ch_aki "Ahem!" # @t_sdonko157.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_tuba_shocked as aki
    $ renpy.pause(0) # Image change
    show i_aki_tuba_focus as aki
    $ renpy.pause(0) # Image change
    show i_aki_tuba_smile as aki
    $ renpy.pause(0) # Image change
    show i_aki_tuba_focus as aki
    $ renpy.pause(0) # Image change
    show i_aki_tuba_overwhelmed as aki
    play sound "sfx/tubasolo.ogg"
    show i_sw_black as darkness:
        # ShowWithAtl
        pause 0.4 
        linear 0.333 alpha 0.5
    extend "{w=0.7330000000000001}{nw}"
    t_ch_cousin "(Whoah! She’s playing the tuba…" # @t_sdonko158.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "As fast as she possibly can?!" # @t_sdonko159.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Performing an entire solo in…" # @t_sdonko159.01 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Less than a second?" # @t_sdonko159.02 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "How is it possible…" # @t_sdonko160.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She really IS good at everything…)" # @t_sdonko160.01 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as darkness:
        # ShowWithAtl
        linear 0.333 alpha 0.0
    show i_aki_default_smile as aki
    extend "{w=0.333}{nw}"
    t_ch_aki "...Finished. Thank you." # @t_sdonko161.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "Woo! That was awesome!" # @t_sdonko162.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Take a bow, girl!" # @t_sdonko162.01 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_nervouslaughter as aki
    t_ch_aki "No time for bowing, I’m afraid." # @t_sdonko163.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ve got too much to attend to." # @t_sdonko163.01 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_smile as aki
    t_ch_aki "[slot_playerName], why don’t you take over on the tuba for me?" # @t_sdonko164.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Thanks! Donko, lovely to see you!" # @t_sdonko164.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_aki_default_smile as aki:
        # ShowWithAtl
        linear .5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_aki "Ciao!" # @t_sdonko165.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "She just left… with the tuba in my hands…" # @t_sdonko166.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How am I supposed to follow an amazing solo like that?!" # @t_sdonko166.01 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’ve never even so much as rolled up a tuba with my katamari before…" # @t_sdonko167.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Relax, honey." # @t_sdonko168.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Everybody starts somewhere!" # @t_sdonko168.01 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’ll do great!" # @t_sdonko168.02 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Even if it sounds bad…" # @t_sdonko169.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s how it’s supposed to sound, if you’re just starting!" # @t_sdonko169.01 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "So just have fun with it, kay~?" # @t_sdonko170.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Donko’s hand…" # @t_sdonko171.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    extend " Paw?" # @t_sdonko171.01 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Drum-foot?" # @t_sdonko171.02 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Anyway, it’s on my shoulder…" # @t_sdonko172.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " To reassure me…" # @t_sdonko172.01 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It feels really warm..?????" # @t_sdonko173.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s nice, but… why is a drum-foot warm?)" # @t_sdonko174.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "Alright! Let’s get started!" # @t_sdonko175.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain2 zorder 1:
        default
        alpha 0.0
        # ShowWithAtl
        linear .5 alpha 1.0
    show i_cousin_default_neutral as cousin
    extend "{w=0.5}{nw}"
    t_ch_cousin "(With that, Donko pulls out… well, a big drum." # @t_sdonko176.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m not surprised." # @t_sdonko177.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "To be honest, I wouldn’t have thought a drum could sound beautiful…" # @t_sdonko178.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But as Donko begins to play it, I realize it can, and it does." # @t_sdonko178.01 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "The beats perfectly in rhythm, loose and fast…" # @t_sdonko179.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And then, suddenly building to a thunderous, passionate roar." # @t_sdonko179.01 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I can barely make any sound come out of this tuba…" # @t_sdonko180.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    extend " I wish I could be as good at this… at ANYTHING… as Donko is on that drum." # @t_sdonko180.01 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But Donko keeps glancing over and smiling in my direction-" # @t_sdonko181.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " As though I’m doing a great job." # @t_sdonko181.01 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It almost makes me believe that I am." # @t_sdonko181.02 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Everyone else in Band has stopped what they’re doing to listen, too…" # @t_sdonko182.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Donko is the obvious star of the club.)" # @t_sdonko182.01 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear .5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_donko "Phew! Good job, everyone~!" # @t_sdonko183.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "You all sounded great! Miranda, your violin was TOTES AMAZING!" # @t_sdonko184.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "And Del, remember last week you were worried about your piano?" # @t_sdonko185.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Such an improvement this time! I’m serious!" # @t_sdonko185.01 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(She’s so… gracious?! That DOES surprise me.)" # @t_sdonko186.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I’m so glad you all can live up to my awesome example! Tee-hee!" # @t_sdonko187.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(...Well, almost gracious.)" # @t_sdonko188.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "As for YOU, honey!" # @t_sdonko189.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Wha? Me?!" # @t_sdonko190.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "If that was REALLY your first time on the tuba…" # @t_sdonko191.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I’m like, seriously way impressed!" # @t_sdonko192.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I told you- you’ve got potential!" # @t_sdonko192.01 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Oh! Gosh! But I didn’t-" # @t_sdonko193.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I mean, haha-" # @t_sdonko193.01 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It was… nothing…" # @t_sdonko193.02 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Oh, look... Everybody else is here too..." # @t_sdonko194.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Huh? More kids from detention?" # @t_sdonko195.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Are they all in Band, too?" # @t_sdonko195.01 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Uh, no, not really… they’re here because of-" # @t_sdonko196.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_bluemax_stand_smile as bluemax:
        # ShowWithAtl
        pause 0.1 
        linear .2 alpha 1.0
    extend "{w=0.30000000000000004}{nw}"
    t_ch_max "Wow, Donko!" # @t_sdonko197.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That was SO GREAT!" # @t_sdonko197.01 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " If I were marching off to battle, I’d want you to beat the drums of war beside me!" # @t_sdonko197.02 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Oh Blue Max, you are SUCH the sweetest!" # @t_sdonko198.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin zorder 3
    show i_donko_ygg_wink as donko zorder 2
    show i_galaga_default as galaga zorder 1
    extend " Keep rockin’ the vintage look, ‘kay?" # @t_sdonko198.01 self.block='Last'
    # UNHANDLED TAG <HardSwap {'auto': 'true', 'lastActor': 'bluemax', 'name': '_21', 'nextActor': 'galaga'} HardSwap ''>
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}YES VERY GOOD{/smallcaps}" # @t_sdonko199.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_galaga "{smallcaps}GALAGA APPRECIATES TRUE TALENT{/smallcaps}" # @t_sdonko1100.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Heehee… Coming from you…" # @t_sdonko1101.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That means, like, sooo much!" # @t_sdonko1101.01 self.block='Last'
    # UNHANDLED TAG <HardSwap {'auto': 'true', 'lastActor': 'galaga', 'name': '_26', 'nextActor': 'hiromi'} HardSwap ''>
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_hiromi "…" # @t_sdonko1102.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    extend " …" # @t_sdonko1102.01 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Nice playing." # @t_sdonko1102.02 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Thanks girl! Love your whole “still waters run deep” vibe!" # @t_sdonko1103.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wow… So many people came to enjoy Donko’s music!" # @t_sdonko1104.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_hiromi_stand_smile as hiromi:
        # ShowWithAtl
        linear .5 alpha 0.0
    extend "{w=0.5}{nw}"
    extend " It looks like she’s really soaking up all the adoration, haha." # @t_sdonko1104.01 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well, I guess when you’re that talented, you should be able to enjoy the rewards!)" # @t_sdonko1105.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_meloncholic as donko
    t_ch_donko "…" # @t_sdonko1106.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_cousin "(Wait… Just for a second there…" # @t_sdonko1107.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " When nobody was talking to her…" # @t_sdonko1107.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Donko looked kind of sad." # @t_sdonko1108.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I wonder what’s up?)" # @t_sdonko1109.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "Thanks for coming by to listen, y’all!" # @t_sdonko1110.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " XOXO!" # @t_sdonko1110.01 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko:
        # ShowWithAtl
        linear .2 xpos 0.75 
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear .2 xpos 0.25 
    extend "{w=0.2}{nw}"
    t_ch_cousin "Hey Donko…" # @t_sdonko1111.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Can we talk outside for a minute?" # @t_sdonko1112.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Yeah…" # @t_sdonko1113.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That would actually be super nice." # @t_sdonko1113.01 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_quad_bleachers as bg # behind curtain
    # <SettingChange {'bgImage': '@i_bg_quad_bleachers', 'curtainFadeTime': '1', 'name': '_2P'} SettingChange ''>
    # <Events {} events ''>
    show i_donko_default_grin as donko
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "For a moment there…" # @t_sdonko1114.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Maybe I’m crazy, but you seemed kinda down." # @t_sdonko1114.01 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What’s going on?" # @t_sdonko1115.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I thought you’d be the kinda person who’d love attention like that." # @t_sdonko1115.01 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko
    t_ch_donko "Hee hee…" # @t_sdonko1116.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You always say what’s on your mind, don’t you?" # @t_sdonko1116.01 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’re honest… or maybe you just have no tact!" # @t_sdonko1116.02 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Either way…" # @t_sdonko1117.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "If I ask you something…" # @t_sdonko1118.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’ll tell me the truth, won’t you?" # @t_sdonko1118.01 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "S-sure…" # @t_sdonko1119.00 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Everyone tells me I’m really good at the drum." # @t_sdonko1120.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "But… people always seem to tell me…" # @t_sdonko1121.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " that I’m really good at EVERYTHING…" # @t_sdonko1121.01 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Because I’m so cute, and they want to be my friend." # @t_sdonko1122.00 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(I’m a bit taken aback by this bragging…" # @t_sdonko1123.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But it seems Donko is being honest and sincere." # @t_sdonko1124.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I guess… it’s easy to see that her cuteness and popularity are real." # @t_sdonko1125.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " So why shouldn’t she acknowledge that?" # @t_sdonko1125.01 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s nothing wrong with that, I guess.)" # @t_sdonko1125.02 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic as donko
    t_ch_donko "Because of that…" # @t_sdonko1126.00 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I can’t really tell if I’m ACTUALLY any good at drumming…" # @t_sdonko1126.01 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or if people are just saying that so they can be my friend." # @t_sdonko1126.02 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_grin as donko
    t_ch_donko "But I want to really be good at it!" # @t_sdonko1127.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I want that really, really badly…" # @t_sdonko1127.01 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(She’s looking right at me without blinking…" # @t_sdonko1128.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Eyes shining with courage…" # @t_sdonko1128.01 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Donko…)" # @t_sdonko1129.00 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "So please, [slot_playerName]!" # @t_sdonko1130.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Tell me the truth, so I can know for sure…" # @t_sdonko1130.01 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Am I really any good at playing the drum?" # @t_sdonko1131.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Or…" # @t_sdonko1132.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Are they all just telling me what I want to hear?" # @t_sdonko1132.01 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Donko is showing me her heart right now…" # @t_sdonko1133.00 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I have to answer truthfully and not play around.)" # @t_sdonko1133.01 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "…" # @t_sdonko1134.00 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Honestly…" # @t_sdonko1135.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "You are really very good!" # @t_sdonko1136.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    extend " I loved hearing you play." # @t_sdonko1136.01 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_crying_comic as donko
    t_ch_donko "WAAAHHHHHHHHH!" # @t_sdonko1137.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Augh, you must have misheard me!" # @t_sdonko1138.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I said you’re GOOD! I swear!" # @t_sdonko1138.01 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_crying as donko
    t_ch_donko "Sniff… No no, silly, it’s happy tears…" # @t_sdonko1139.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    extend " BWAAAAAHHH!!" # @t_sdonko1139.01 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "U-um…" # @t_sdonko1140.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There, there?" # @t_sdonko1140.01 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I guess I should pat her back in sympathy…" # @t_sdonko1141.00 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.35 
    extend "{w=0.5}{nw}"
    extend " Which part is her back, though? She’s kinda… cylindrical…" # @t_sdonko1141.01 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.4 
    extend "{w=0.5}{nw}"
    t_ch_cousin "So isn’t her back also part of her stomach?" # @t_sdonko1142.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.45 
    extend "{w=0.5}{nw}"
    extend " ...I’ll play it safe and pat her face instead.)" # @t_sdonko1142.01 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.46 
        # ShowWithAtl
        pause 0.5 
        linear 0.5 xpos 0.45 
        # ShowWithAtl
        pause 1.0 
        linear 0.5 xpos 0.46 
        # ShowWithAtl
        pause 1.5 
        linear 0.5 xpos 0.42 
    extend "{w=2.0}{nw}"
    t_ch_donko "Th-thank you…" # @t_sdonko1143.00 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I know you wouldn’t lie to me…" # @t_sdonko1143.01 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s, like, such a relief to hear that…" # @t_sdonko1143.02 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Well, it’s the truth!" # @t_sdonko1144.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If you sucked, I would just…" # @t_sdonko1145.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Try to find a way to politely avoid answering you, haha." # @t_sdonko1145.01 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "SNIFF…" # @t_sdonko1146.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Hoooooo!" # @t_sdonko1146.01 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_crying as donko
    extend " Shake it off, shake it off…" # @t_sdonko1146.02 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko
    t_ch_donko "Okay, I’m done." # @t_sdonko1147.00 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Now listen up! If you ever tell anyone you saw me crying my eyes out…" # @t_sdonko1148.00 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I’ll ruin your reputation at this school before you can say “Gene Krupa”!" # @t_sdonko1149.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha, okay, okay." # @t_sdonko1150.00 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You know, to tell the truth…" # @t_sdonko1151.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I’m a little jealous of your talent!" # @t_sdonko1152.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s nothing that I’m really good at like that." # @t_sdonko1152.01 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "But, like, it’s not “talent”!" # @t_sdonko1153.00 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ve worked, like, TOTALLY hard to try to be good." # @t_sdonko1153.01 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "You could do the same thing and get as good as me!" # @t_sdonko1154.00 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Yeah yeah, I know…" # @t_sdonko1155.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But honestly, I wouldn’t even mind if people told me I was good, just because they wanted me to like them." # @t_sdonko1156.00 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I can see why you might be worried about that, but me…" # @t_sdonko1156.01 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I don’t really have many friends here. I’m not popular, like you are." # @t_sdonko1157.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_grin as donko
    t_ch_donko "NO!" # @t_sdonko1158.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_grin as donko
    t_ch_donko "Being cute and cool and popular is something ANYBODY can do!" # @t_sdonko1159.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "It’s just like music-" # @t_sdonko1160.00 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You only have to work at it!" # @t_sdonko1160.01 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Well, that’s easy for YOU to say." # @t_sdonko1161.00 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_meloncholic as donko
    t_ch_donko "No! Shush!" # @t_sdonko1162.00 self.block='Last'
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You shush now!" # @t_sdonko1162.01 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Drumroll, please…." # @t_sdonko1163.00 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_grin as donko
    t_ch_donko "I’ve just had, like, the absolute BEST idea EVER!" # @t_sdonko1164.00 self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "???" # @t_sdonko1165.00 self.block='Last'
    # <ParallelEvent {'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "If I tell you now, it’ll like, spoil the surprise!" # @t_sdonko1166.00 self.block='Last'
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "You stay right here and don’t do ANYTHING until I come back!" # @t_sdonko1167.00 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Capische?!" # @t_sdonko1167.01 self.block='Last'
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "What…" # @t_sdonko1168.00 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Literally just stay sitting right here?" # @t_sdonko1168.01 self.block='Last'
    # <ParallelEvent {'name': '_3q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Okay, I guess…" # @t_sdonko1169.00 self.block='Last'
    # <ParallelEvent {'name': '_3r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Okay, it’s too exciting! I can’t hold it in!" # @t_sdonko1170.00 self.block='Last'
    # <ParallelEvent {'name': '_3s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " [slot_playerName], it’s totes your lucky day!" # @t_sdonko1170.01 self.block='Last'
    # <ParallelEvent {'name': '_3t'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I, Donko, the most popular student Namco High has EVER had…" # @t_sdonko1170.02 self.block='Last'
    # <ParallelEvent {'name': '_3u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    t_ch_donko "Am going to take YOU, the cute new kid, under my wing!" # @t_sdonko1171.00 self.block='Last'
    # <ParallelEvent {'name': '_3v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "With my help, you’re going to be just as popular as me!" # @t_sdonko1172.00 self.block='Last'
    # <ParallelEvent {'name': '_3w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And then you’ll see that ANYBODY can do it!" # @t_sdonko1172.01 self.block='Last'
    # <ParallelEvent {'name': '_3x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "...Oh." # @t_sdonko1173.00 self.block='Last'
    # <ParallelEvent {'name': '_3y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That’s very nice of you, but I’m not sure I-" # @t_sdonko1174.00 self.block='Last'
    # <ParallelEvent {'name': '_3z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Shh! Don’t question it, silly!" # @t_sdonko1175.00 self.block='Last'
    # <ParallelEvent {'name': '_40'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’ll thank me in the end!" # @t_sdonko1175.01 self.block='Last'
    # <ParallelEvent {'name': '_41'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Okay, bye honey!" # @t_sdonko1176.00 self.block='Last'
    # <ParallelEvent {'name': '_42'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ve got a ton of planning to do!" # @t_sdonko1176.01 self.block='Last'
    show i_donko_akimbo_wink as donko:
        # ShowWithAtl
        linear .4 alpha 0.0
    # <ParallelEvent {'name': '_44'} ParallelEvent ''>
    # <Events {} events ''>
    extend " See you tomorrow!" # @t_sdonko1176.02 self.block='Last'
    # <ParallelEvent {'name': '_45'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Heh…" # @t_sdonko1177.00 self.block='Last'
    # <ParallelEvent {'name': '_46'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Donko is SO confident, she just does whatever she likes without thinking." # @t_sdonko1177.01 self.block='Last'
    # <ParallelEvent {'name': '_47'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But… I can see that she really does think about other people, too." # @t_sdonko1178.00 self.block='Last'
    # <ParallelEvent {'name': '_48'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She’s not just self-centered and vain…" # @t_sdonko1178.01 self.block='Last'
    # <ParallelEvent {'name': '_49'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Okay, she’s ALSO those things, but not JUST that…" # @t_sdonko1179.00 self.block='Last'
    # <ParallelEvent {'name': '_4A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s a good heart in that drum somewhere." # @t_sdonko1179.01 self.block='Last'
    # <ParallelEvent {'name': '_4B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Donko is a little over-the-top…" # @t_sdonko1180.00 self.block='Last'
    # <ParallelEvent {'name': '_4C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But she’s definitely popular and well-liked for a reason." # @t_sdonko1180.01 self.block='Last'
    # <ParallelEvent {'name': '_4D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m starting to like Donko a lot, too.)" # @t_sdonko1180.02 self.block='Last'
    # <NHSceneChange {'name': '_4E', 'scene': 's_day2'} NHSceneChange ''>
    label s_donko1__4E:
        # <NHSceneChange {'name': '_4E', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2