# <Scene {'id': 's_donko3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_donko3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_donko3"
    $ renpy.pause(1)
    # <Scene {'id': 's_donko3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/upbeat_half.ogg" loop
    show i_bg_classroom_a as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_sw_white as white_swatch zorder 9:
        default
        alpha 0.0
    show i_donko_default_meloncholic as donko zorder 6:
        default
        xpos 0.75 
    show i_cousin_default_neutral as cousin zorder 7:
        default
        xpos 0.25 
    show i_digdug_left as digdug zorder 2:
        default
        xpos 0.85 
        alpha 0.0
    t_ch_cousin "Alright, I’ll bite." # @t_sdonko311.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What’s up?" # @t_sdonko311.01 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "It’s just so, like, unfair…" # @t_sdonko312.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "…" # @t_sdonko313.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "There’s a REALLY great sale going on at the mall today!" # @t_sdonko314.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_crying_comic as donko
    t_ch_donko "I really wanted to go, but I’ve got DETENTION, ugh…" # @t_sdonko315.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s today only and there’s SUCH great deals and I’m MISSING it!" # @t_sdonko315.01 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "My life is like, over…." # @t_sdonko316.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Are you serious? That’s all this is about?" # @t_sdonko317.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_crying_comic as donko
    t_ch_donko "Just because it’s not important to you, doesn’t mean it can’t be important to me!" # @t_sdonko318.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I wouldn’t make fun of you if there was like, a discount on rolling up stuff you were missing." # @t_sdonko318.01 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(That doesn’t really make sense, but I guess I see her point.)" # @t_sdonko319.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "… Okay, okay…" # @t_sdonko320.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How can I help?" # @t_sdonko320.01 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_grin as donko
    t_ch_donko "Oh, [slot_playerName]!" # @t_sdonko321.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I knew you’d want to help me!" # @t_sdonko321.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "It’s because I’m so cute and personable." # @t_sdonko322.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Everyone in Namco High wants to help me!" # @t_sdonko322.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "That just makes it sound like you could’ve asked ANYONE, and left me out of this!" # @t_sdonko323.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Tee-hee! Oh, hush." # @t_sdonko324.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Okay, here’s the plan…" # @t_sdonko324.01 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_grin as donko
    t_ch_donko "You lift me up to the window. I’m too small to reach without you!" # @t_sdonko325.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Then I can sneak out…" # @t_sdonko326.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Too bad there’s nothing to per-cushion me if I fall." # @t_sdonko326.01 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(...I can’t take much more of this…)" # @t_sdonko327.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Once I’m out, I can totally go check out the sale, no problem!" # @t_sdonko328.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh, maybe I’m missing something, but…" # @t_sdonko329.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How the heck are we gonna do this without anyone noticing?" # @t_sdonko329.01 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    t_ch_donko "Just do it already!" # @t_sdonko330.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Well, I guess I’m in it now." # @t_sdonko331.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Here goes nothing…" # @t_sdonko331.01 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain zorder 10:
        # FadeEvent
        linear 0.5 alpha 1.0
    $ renpy.pause(0.5) # TimedPause
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Huh! Donko is surprisingly light. I have no trouble lifting her up to the window." # @t_sdonko332.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But wait… as she’s going through the window… She’s still grabbing my hands…" # @t_sdonko333.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m being pulled through, too!" # @t_sdonko333.01 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "AAAAHHHHHH….)" # @t_sdonko334.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Yay, we’re out! See? Easy as do-re-mi." # @t_sdonko335.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_quad_bleachers as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_quad_bleachers', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_b'} SettingChange ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Donko!" # @t_sdonko336.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Did you do that on purpose!" # @t_sdonko336.01 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Of course I did, honey!" # @t_sdonko337.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I sneak out of detention on my own all the time. I just wanted you to come with me!" # @t_sdonko337.01 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " How could I let you miss out on such an amazing sale!" # @t_sdonko337.02 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Especially since it’s the perfect place to get you a new outfit…" # @t_sdonko338.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Which will help you get TOTALLY POPULAR!" # @t_sdonko338.01 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Sigh. I guess now that I’ve already snuck out of school, I have no choice..." # @t_sdonko339.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "...Besides…" # @t_sdonko340.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s sorta flattering that Donko would go so far…" # @t_sdonko340.01 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "For my sake.)" # @t_sdonko341.00 self.block='Last'
    show i_event_donko_scene3 as event zorder 9:
        default
        alpha 0.0
        linear 1 alpha 1.0
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Ahh, we made it to the mall!" # @t_sdonko342.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "See? That was cymbal enough!" # @t_sdonko343.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Now let’s drum up some cute outfits!" # @t_sdonko343.01 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Please, Donko…" # @t_sdonko344.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Enough with the drum puns already!" # @t_sdonko344.01 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They’re starting to get a little labored." # @t_sdonko344.02 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Huh?" # @t_sdonko345.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "What do you mean?!" # @t_sdonko346.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Does she really not notice that she's saying those things?!)" # @t_sdonko347.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "[slot_playerName], what did I tell you about being weird?" # @t_sdonko348.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Um, don’t be it?" # @t_sdonko349.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Ta-don! That’s right!" # @t_sdonko350.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    extend " See, honey? You’re learning about popularity already." # @t_sdonko350.01 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "But the first step towards popularity is looking your best!" # @t_sdonko351.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Isn’t that kinda shallow?" # @t_sdonko352.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "What?! Of course not!" # @t_sdonko353.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "How you dress is like, a total expression of what’s inside you!" # @t_sdonko354.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Like your personality, and stuff you like, and whatever." # @t_sdonko354.01 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "If you don’t take the effort to show that stuff to the world with how you dress…" # @t_sdonko355.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That means you don’t care about what’s inside!" # @t_sdonko355.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And that’s terrible!" # @t_sdonko355.02 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I’m not sure I totally agree with what Donko is saying, but…" # @t_sdonko356.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " She’s obviously not just some airhead." # @t_sdonko356.01 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " ...Although… she might literally be full of air..." # @t_sdonko356.02 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Anyway, this seems to really be important to her.)" # @t_sdonko356.03 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Now, let’s see! What would like nice on you…" # @t_sdonko357.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Hats are in this year!" # @t_sdonko358.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But I don’t see any that would fit on your big weird head…" # @t_sdonko358.01 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Speak for yourself!" # @t_sdonko359.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Hmm, this is harder than I thought." # @t_sdonko360.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "…" # @t_sdonko361.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "What do you think, honey?" # @t_sdonko362.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    extend " OMG, this is like, totally PERFECT!" # @t_sdonko364.01 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "[slot_playerName], please, you’ve GOT to try on this amazing scarf!" # @t_sdonko365.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Whoah, Donko’s just throwing that scarf around my neck, without waiting for an answer.)" # @t_sdonko366.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "H-hey now… I’m not sure I need…." # @t_sdonko367.00 self.block='Last'
    show i_sw_black as curtain2 zorder 2:
        default
        alpha 1.0
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    show i_donko_akimbo_grin as donko
    t_ch_donko "Oh, WOW…." # @t_sdonko368.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "[slot_playerName]…" # @t_sdonko369.00 self.block='Last'
    show i_event_donko_scene3 as event:
        # FadeEvent
        linear 0.75 alpha 0.0
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You look so, so GOOD in this!" # @t_sdonko369.01 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It totally brings out your pretty eyes!" # @t_sdonko369.02 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "I almost can’t even believe it!" # @t_sdonko370.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s a whole new YOU!" # @t_sdonko370.01 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf_blush as cousin
    t_ch_cousin "I, uh… Um…" # @t_sdonko371.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (I was going to say something, but…" # @t_sdonko371.01 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "The way Donko is looking at me in this scarf…" # @t_sdonko372.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It makes me feel…" # @t_sdonko372.01 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Really good.)" # @t_sdonko373.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    t_ch_donko "Sorry, I totally spaced!" # @t_sdonko374.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You were going to say something about how you’re “not sure you need...”?" # @t_sdonko374.01 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh-" # @t_sdonko375.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf_blush as cousin
    extend " Nevermind." # @t_sdonko375.01 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Teehee." # @t_sdonko376.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I thought so." # @t_sdonko376.01 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_grin as donko
    t_ch_donko "...Y’know, honey…" # @t_sdonko377.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Now that I’ve picked out something cute for YOU to wear…" # @t_sdonko377.01 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "It’s only fair if you get to pick out something you’d like to see ME in." # @t_sdonko378.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Huh? What do you have in mind?" # @t_sdonko379.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "It’s no fun if I tell you what to pick! Anything you want, honey!" # @t_sdonko380.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Honestly, Donko…" # @t_sdonko381.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_scarf_blush as cousin
    t_ch_cousin "I think you’re the cutest wearing nothing at all!" # @t_sdonko382.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "…" # @t_sdonko383.00 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_meloncholic as donko
    $ renpy.pause(0) # Image change
    show i_donko_ygg_meloncholic as donko
    $ renpy.pause(0) # Image change
    show i_donko_default_meloncholic as donko:
        # ShowWithAtl
        pause 1.0 
        ease_expo .15 xpos 0.62 
    show i_cousin_exhausted_surprised_scarf as cousin
    play sound ["<silence .9>", "sfx/slap.ogg"]
    show i_sw_white as white_swatch:
        # ShowWithAtl
        pause 1.0 
        linear 0.5 alpha 1.0
        # ShowWithAtl
        pause 1.1 
        linear 0.5 alpha 0.0
    show i_donko_default_meloncholic as donko:
        # ShowWithAtl
        pause 1.2 
        ease_expo .2 xpos 0.75 
    extend "{w=2.7}{nw}"
    narrator "*SLAP*" # *SLAP* self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(AUGH! SHE SLAPPED ME IN THE FACE!" # @t_sdonko384.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What’d I say?!)" # @t_sdonko384.01 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko
    t_ch_donko "Hee hee hee!" # @t_sdonko385.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You get right to the point, don’t you~?" # @t_sdonko385.01 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Whaa?! She slapped me, and now she’s giggling?" # @t_sdonko386.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And what does she mean, “get right to the…”" # @t_sdonko387.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_sdonko388.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified_scarf as cousin
    extend " OH MY GOD…" # @t_sdonko388.01 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " SHE THOUGHT I MEANT…." # @t_sdonko388.02 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified_scarf_blush as cousin
    t_ch_cousin "OH NO, NO!" # @t_sdonko389.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I DIDN’T MEAN IT LIKE THAT..." # @t_sdonko389.01 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I MEAN, I THOUGHT DONKO DOESN’T WEAR ANYTHING ANYWAY…" # @t_sdonko390.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I MEAN…SHE’S A DRUM, SO… WHAT’S... CLOTHES..." # @t_sdonko390.01 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "OH NOOOOOOOO!)" # @t_sdonko391.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Tee hee hee! Don’t get any ideas, honey!" # @t_sdonko392.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m not that kind of drum!" # @t_sdonko392.01 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I…" # @t_sdonko393.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I didn’t…" # @t_sdonko393.01 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wait, so…" # @t_sdonko394.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_scarf_blush as cousin
    t_ch_cousin "IS Donko wearing clothes now?" # @t_sdonko395.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Which part is the clothes?" # @t_sdonko395.01 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Is it wrapped around her body…?" # @t_sdonko395.02 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified_scarf_blush as cousin
    t_ch_cousin "AUGH! What am I saying!" # @t_sdonko396.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ve gotta stop thinking about this!" # @t_sdonko396.01 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’m so embarrassed...)" # @t_sdonko396.02 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_grin as donko
    t_ch_donko "I guess I don’t really need to get anything today." # @t_sdonko397.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_grin as donko
    extend " You can’t mess with perfect style like mine." # @t_sdonko397.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf_blush as cousin
    t_ch_cousin "(Thank goodness she changed the subject.)" # @t_sdonko398.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "But you, [slot_playerName]!" # @t_sdonko399.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " PLEASE tell me you’re getting that scarf." # @t_sdonko399.01 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    extend " You like, SO need the fashion boost." # @t_sdonko399.02 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "You know what, don’t EVEN say another word." # @t_sdonko3100.00 self.block='Last'
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I’m totally getting you that scarf." # @t_sdonko3101.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’d be, like, a fashion crime to let you walk out of here without it." # @t_sdonko3101.01 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf_blush as cousin
    t_ch_cousin "Wh-what!" # @t_sdonko3102.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Donko, no… I can’t ask you to do that for me." # @t_sdonko3103.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_grin as donko
    t_ch_donko "Tee-hee! You’re not asking me, honey!" # @t_sdonko3104.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I, like, insist." # @t_sdonko3105.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " After all, I did sorta kinda force you to sneak out of detention with me…" # @t_sdonko3105.01 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I totally owe you one." # @t_sdonko3106.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf_blush as cousin
    t_ch_cousin "(Normally, I’d protest more, but…" # @t_sdonko3107.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "That’s kind of a good point." # @t_sdonko3108.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Besides, if I can keep wearing this scarf, and it makes Donko look at me like that…" # @t_sdonko3109.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I can’t really complain about that.)" # @t_sdonko3110.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    t_ch_donko "Oh, yikes." # @t_sdonko3111.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We’d better be getting back to school soon…" # @t_sdonko3111.01 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I’ll go ring this up, honey!" # @t_sdonko3111.02 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Th-Thanks." # @t_sdonko3112.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cashier "Thanks for your purchase! Have a great day!" # @t_sdonko3113.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cashier "And don’t forget to come back over the weekend!" # @t_sdonko3114.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Our sale is going on until Monday!" # @t_sdonko3114.01 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_grin as donko
    t_ch_donko "Cool! Thanks!" # @t_sdonko3115.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 1.0 alpha 1.0
    $ renpy.pause(1.0)
    show i_bg_cafe as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_cafe', 'curtainActor': 'curtain', 'curtainFadeTime': '1', 'name': '_2g'} SettingChange ''>
    # <Events {} events ''>
    show i_sw_black as curtain2:
        # FadeEvent
        alpha 0.0
    show i_cousin_default_laugh_scarf as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 1.0 alpha 0.0
    $ renpy.pause(1.0)
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Haha! That was actually pretty fun…" # @t_sdonko3116.00 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Thanks again, Donko." # @t_sdonko3117.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko
    t_ch_donko "Just you wait, honey- with that scarf, people will start to notice you!" # @t_sdonko3118.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It expresses your, like, totally earnest, sensitive side…" # @t_sdonko3118.01 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " And to top it all off, it was on sale- 50% off! Score!" # @t_sdonko3118.02 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Haha, gosh… Earnest and sensitive…" # @t_sdonko3119.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_sdonko3120.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    extend " Hey, wait a minute." # @t_sdonko3120.01 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You said…" # @t_sdonko3121.00 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " About the sale…" # @t_sdonko3121.01 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Did you… lie to me?" # @t_sdonko3121.02 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Hmm? Well, maybe it was more like 49% off…" # @t_sdonko3122.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_meloncholic as donko
    t_ch_donko "I rounded up! So sue me!" # @t_sdonko3123.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Don’t be such, like, a math geek." # @t_sdonko3123.01 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "No, I mean…" # @t_sdonko3124.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You told me the sale was only happening today." # @t_sdonko3124.01 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You were almost crying, saying you were going to miss it…" # @t_sdonko3124.02 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But the cashier said… She said the sale was going on until Monday." # @t_sdonko3125.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That means you’d have the whole weekend to shop…" # @t_sdonko3125.01 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral_scarf as cousin
    t_ch_cousin "You lied to me… to get me to help you to sneak out." # @t_sdonko3126.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Mmm…" # @t_sdonko3127.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_grin as donko
    t_ch_donko "SIGH. Yes, that’s totally true." # @t_sdonko3128.00 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_scarf as cousin
    t_ch_cousin "You’re just admitting it?" # @t_sdonko3129.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "No reason to deny it…" # @t_sdonko3130.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I like, REALLY wanted you to shop with me." # @t_sdonko3130.01 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I kinda thought it was the only way to get you to come…" # @t_sdonko3131.00 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Sorry." # @t_sdonko3132.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    t_ch_cousin "That really sucks, Donko..." # @t_sdonko3133.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But at least you’re being honest with me now…" # @t_sdonko3133.01 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And… you did buy me a nice scarf… without getting anything for yourself." # @t_sdonko3134.00 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Plus, it’s all to make you super popular!" # @t_sdonko3135.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "You’ll thank me when all is said and done." # @t_sdonko3136.00 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf as cousin
    t_ch_cousin "Haha… I guess-" # @t_sdonko3137.00 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprise_scarf as cousin:
        # ShowWithAtl
        linear .2 xpos 0.11 
    show i_donko_ygg_grin as donko:
        # ShowWithAtl
        linear .2 xpos 0.3 
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.33 alpha 1.0
    $ renpy.pause(0.33) # TimedPause
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "What’s going on here?!" # @t_sdonko3138.00 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Why aren’t you two in detention?" # @t_sdonko3138.01 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Ahhh! Principal Dig Dug!" # @t_sdonko3139.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko
    t_ch_donko "Hee hee, oops!" # @t_sdonko3140.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "WELL?!" # @t_sdonko3141.00 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad_scarf as cousin
    t_ch_cousin "Donko… can I talk to you privately for a moment?" # @t_sdonko3142.00 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_wink as donko:
        # ShowWithAtl
        linear .2 xpos 0.75 
    show i_cousin_default_sad_scarf as cousin:
        # ShowWithAtl
        linear .2 xpos 0.25 
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.33 alpha 0.0
    $ renpy.pause(0.33) # TimedPause
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You said you sneak out all the time…" # @t_sdonko3143.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_scarf as cousin
    extend " Don’t you have a plan for not getting caught, or something?!" # @t_sdonko3143.01 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_akimbo_grin as donko
    t_ch_donko "Uh, like, where’d you get that idea?" # @t_sdonko3144.00 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I do sneak out all the time…" # @t_sdonko3145.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I just always get caught, silly!" # @t_sdonko3145.01 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "…" # @t_sdonko3146.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified_scarf as cousin
    t_ch_cousin "W h a t" # @t_sdonko3147.00 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "Getting in trouble is like, no big deal!" # @t_sdonko3148.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "I’ll flash em my cutest puppy-dog eyes and we’ll be off the hook." # @t_sdonko3149.00 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "LOL! It’s easy!" # @t_sdonko3150.00 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified_scarf as cousin
    t_ch_cousin "(...I can’t believe this..." # @t_sdonko3151.00 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Donko really thinks she can get away with anything, just because she’s cute." # @t_sdonko3152.00 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I might’ve been okay with the lying…" # @t_sdonko3153.00 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " But this kind of thing makes me angry…)" # @t_sdonko3153.01 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_donko "What?" # @t_sdonko3154.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_default_wink as donko
    t_ch_donko "Oh come on! Don’t give me that look." # @t_sdonko3155.00 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What’s the point of being so charming if you don’t use it?" # @t_sdonko3155.01 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(..." # @t_sdonko3156.00 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad_scarf as cousin
    t_ch_cousin "I wish she’d just shut up already…)" # @t_sdonko3157.00 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Alright, that’s enough jabbering amongst yourselves!" # @t_sdonko3158.00 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_donko_ygg_wink as donko:
        # ShowWithAtl
        linear .2 xpos 0.3 
    show i_cousin_default_neutral_scarf as cousin:
        # ShowWithAtl
        linear .2 xpos 0.11 
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.33 alpha 1.0
    $ renpy.pause(0.33) # TimedPause
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " My office! NOW!" # @t_sdonko3158.01 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain2 zorder 9
    t_ch_cousin "(That day…" # @t_sdonko3159.00 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_sw_black as curtain2:
        # FadeEvent
        linear 1.0 alpha 1.0
    extend "{w=1.0}{nw}"
    extend " Principal Dig Dug was even angrier than he was the day I rolled up the school." # @t_sdonko3159.01 self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And the worst part is, it’s all Donko’s fault I’m in trouble again." # @t_sdonko3160.00 self.block='Last'
    # <ParallelEvent {'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I don’t care about being popular, but I liked the excuse to spend time with her." # @t_sdonko3160.01 self.block='Last'
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But is she really being nice? Is she only pretending to help me?" # @t_sdonko3161.00 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Does she know I’ll be charmed by her cuteness, and I’ll just do whatever she wants?" # @t_sdonko3162.00 self.block='Last'
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "After all, Dig Dug said he was going to give us “double detention” for sneaking out, but Donko flashed a cute smile, and it seems like we got off pretty easy…" # @t_sdonko3163.00 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " …" # @t_sdonko3163.01 self.block='Last'
    # <ParallelEvent {'name': '_3q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Donko… do you really care, or what?" # @t_sdonko3163.02 self.block='Last'
    # <ParallelEvent {'name': '_3r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I guess she did buy me this scarf…" # @t_sdonko3164.00 self.block='Last'
    # <ParallelEvent {'name': '_3s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I don’t know if I even want to wear it now." # @t_sdonko3165.00 self.block='Last'
    # <ParallelEvent {'name': '_3t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "But the memory of buying it with her is still a good one…" # @t_sdonko3166.00 self.block='Last'
    # <ParallelEvent {'name': '_3u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I just wish I knew if it was real.)" # @t_sdonko3167.00 self.block='Last'
    # <NHSceneChange {'name': '_3v', 'scene': 's_day4'} NHSceneChange ''>
    label s_donko3__3v:
        # <NHSceneChange {'name': '_3v', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4