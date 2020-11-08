# <Scene {'id': 's_albatros1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_albatros1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_albatros1"
    $ renpy.pause(1)
    # <Scene {'id': 's_albatros1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/aroundtown.ogg" loop
    show i_bg_cafe as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_albatross_watch_inquisitive as albatros zorder 2:
        default
        xpos 0.7 
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    t_ch_cousin "(Hm, don’t see Al anywhere.)" # @t_salbatros134.00 self.block='Last'
    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Or anyone else who might be a teenage crime fighter.)" # @t_salbatros135.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Oh!)" # @t_salbatros136.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Maybe they’re undercover???)" # @t_salbatros136.01 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Then again a cafe seems like a strange place for these guys to meet.)" # @t_salbatros137.00 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Unless it’s a sting!)" # @t_salbatros138.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smug as albatros:
        # FadeEvent
        linear 0.25 alpha 1.0
    extend "{w=0.25}{nw}"
    t_ch_albatros "[slot_playerName]! Welcome to the Namco Anti Real Crime Group. Namco High’s own criminal justice club." # @t_salbatros139.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Uh, yeah. Happy to be here!" # @t_salbatros140.00 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " (Ack, no! Play it cool, [slot_playerName]!)" # @t_salbatros140.01 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I mean, y’know." # @t_salbatros141.00 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "I wasn’t up to any other capers." # @t_salbatros142.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    with Dissolve(0.333)
    t_ch_cousin "Today." # @t_salbatros143.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Do they call them capers?!)" # @t_salbatros143.01 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smirk as albatros
    t_ch_albatros "Ha! Taking it easy, then? Well, glad you could make it." # @t_salbatros144.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_fistinhand_staredown as albatros
    t_ch_albatros "Let’s get down to business." # @t_salbatros145.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Al doesn’t waste any time, does he!)" # @t_salbatros146.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_albatros "This semester the club is raising awareness of cheat code trafficking." # @t_salbatros147.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "They’re dangerous weapons, and that’s why they have to be heavily regulated." # @t_salbatros148.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smirk_wink as albatros
    t_ch_albatros "But you wouldn’t know anything about cheat codes. Would you, [slot_playerName]?" # @t_salbatros149.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smirk as albatros
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Did Al just wink at me?)" # @t_salbatros150.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " (That’s totally a flirt thing!)" # @t_salbatros150.01 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh, yeah. No, of course “not.”" # @t_salbatros150.02 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (And I’ll cap that off with my OWN wink…)" # @t_salbatros150.03 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_laugh_blush as cousin
    t_ch_cousin "(Bam!)" # @t_salbatros151.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    show i_albatross_toocool_smug as albatros
    t_ch_albatros "Hmm." # @t_salbatros152.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_staredown as albatros
    t_ch_albatros "I thought so." # @t_salbatros153.00 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Wonder what Al’s writing.)" # @t_salbatros154.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Bet it’s the official minutes of the meeting.)" # @t_salbatros155.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " (But shouldn’t the club secretary be doing that?)" # @t_salbatros155.01 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Good, good." # @t_salbatros156.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_inquisitive as albatros
    t_ch_albatros "This being a criminal justice club, let’s talk about our firsthand experiences with crime." # @t_salbatros157.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_staredown as albatros
    t_ch_albatros "And criminals." # @t_salbatros158.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "And, for example, cheat code trafficking." # @t_salbatros159.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Why don’t we start with…" # @t_salbatros160.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Hmmmmmmm…" # @t_salbatros160.01 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_inquisitive as albatros
    t_ch_albatros "Our newest member. [slot_playerName]?" # @t_salbatros161.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Oh, there are other members?" # @t_salbatros162.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Because I only see you and me." # @t_salbatros163.00 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk as albatros
    t_ch_albatros "Ah." # @t_salbatros164.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smug as albatros
    t_ch_albatros "Er." # @t_salbatros165.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk_wink as albatros
    t_ch_albatros "No. See. Everyone in this cafe?" # @t_salbatros166.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk_wink as albatros
    t_ch_albatros "They’re in the club too." # @t_salbatros167.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Wow, everyone?" # @t_salbatros168.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Er, yeah" # @t_salbatros169.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Even the baristas and the super elderly couple in the back corner?" # @t_salbatros170.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "And the guy who was begging for change earlier?" # @t_salbatros171.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "And that dog?" # @t_salbatros172.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Yup, sure. Yes. All of them." # @t_salbatros173.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "They’re all practicing undercover. Deep cover. Under deep cover." # @t_salbatros174.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_staredown as albatros
    t_ch_albatros "So, when did you start wall clipping?" # @t_salbatros175.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(What’s he...how does a wall get clipped?)" # @t_salbatros176.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Your favorite ammo hack?" # @t_salbatros177.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "You can hack ammo?" # @t_salbatros178.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_inquisitive as albatros
    t_ch_albatros "You know." # @t_salbatros179.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Infinite ammo or infinite clip." # @t_salbatros180.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Is that different from the wall clip?" # @t_salbatros181.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_smirk_wink as albatros
    t_ch_albatros "Heh." # @t_salbatros182.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Good one, [slot_playerName]." # @t_salbatros183.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "You’re clever." # @t_salbatros184.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "But then you have to be in this business, don’t you." # @t_salbatros185.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised_blush as cousin
    t_ch_cousin "(?????)" # @t_salbatros186.00 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Man, Al goes from zero to SUPER FLIRTING in like two seconds.)" # @t_salbatros186.01 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin_blush as cousin
    t_ch_cousin "(Well, when in Namco Rome!)" # @t_salbatros187.00 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Uh yeah. Yeah you do." # @t_salbatros187.01 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Big time." # @t_salbatros188.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It’s how I get away with all the ~bad~ stuff I do." # @t_salbatros189.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_inquisitive as albatros
    t_ch_albatros "So." # @t_salbatros190.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_smirk_wink as albatros
    t_ch_albatros "You do bad stuff." # @t_salbatros191.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(It’s a little weird that he takes notes while flirting…)" # @t_salbatros192.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Flaunting convention, that’s classic Al!)" # @t_salbatros193.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Uh, as far as I know.)" # @t_salbatros194.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    extend " Well, I didn’t wind up in detention by helping old ladies across the street." # @t_salbatros194.01 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "If you get my meaning." # @t_salbatros195.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (I’m not sure I do!)" # @t_salbatros195.01 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh_blush as cousin
    t_ch_cousin "(I guess sometimes that’s how flirting goes.)" # @t_salbatros196.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Bad stuff like…" # @t_salbatros197.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_staredown as albatros
    t_ch_albatros "...skipping levels?" # @t_salbatros198.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(How do you skip a level?)" # @t_salbatros199.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Does he mean like a GRADE level?)" # @t_salbatros1100.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "(But, wait, that’s like, from being smart, isn’t it? How is that bad?)" # @t_salbatros1101.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "(Flirting is hard work!)" # @t_salbatros1102.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Sure. I skipped a level." # @t_salbatros1102.01 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Level skipping, huh?" # @t_salbatros1103.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Pretty dangerous, that." # @t_salbatros1104.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Ohhhhhh!)" # @t_salbatros1105.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(He must mean, like, sociologically.)" # @t_salbatros1106.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Because skipping ahead can alienate you from both your original peer group as well as the new one you find yourself in.)" # @t_salbatros1107.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "(That’s very sensitive of Al.)" # @t_salbatros1108.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(He has such a dangerous loner tough guy persona I never would have suspected it.)" # @t_salbatros1109.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(And that he’d show me his softer side so quickly...gosh!)" # @t_salbatros1110.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Well, that’s just how I roll." # @t_salbatros1110.01 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_angry_blush as cousin
    extend " DANGEROUSLY." # @t_salbatros1110.02 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    extend " (At least, that’s what Principal Dig-Dug says…)" # @t_salbatros1110.03 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_distraught as albatros
    t_ch_albatros "You help other kids skip levels?" # @t_salbatros1111.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Uh, how do I do this one all flirty???)" # @t_salbatros1112.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Well. Y’know." # @t_salbatros1112.01 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "I’ll try anything once." # @t_salbatros1113.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (Did that do it?)" # @t_salbatros1113.01 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hm, I guess so. Al’s taking tons of notes.)" # @t_salbatros1114.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Seems like you’re the beating heart of the underbelly of this town." # @t_salbatros1115.00 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Uh, okay. I guess that one just got away from him!)" # @t_salbatros1116.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Even a suave guy like Al is gonna have a fumble every now and then.)" # @t_salbatros1117.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Well, you can’t prove nothin’." # @t_salbatros1117.01 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " (There. Maybe that got the train back on track!)" # @t_salbatros1117.02 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_staredown as albatros
    t_ch_albatros "You think you can stay one step ahead forever, [slot_playerName]?" # @t_salbatros1118.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Hey." # @t_salbatros1119.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "I’ve lasted this long." # @t_salbatros1120.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral_blush as cousin
    extend " (Wow, this is so much fun!)" # @t_salbatros1120.01 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    t_ch_cousin "(I am so gonna order a coffee when the club meeting is over and feel like a total grown up.)" # @t_salbatros1121.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_smug as albatros
    t_ch_albatros "The thing about cheat codes, [slot_playerName], is…" # @t_salbatros1122.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "one day…" # @t_salbatros1123.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "you put them in wrong." # @t_salbatros1124.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_toocool_staredown as albatros
    extend " And then what?" # @t_salbatros1124.01 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "You tell me." # @t_salbatros1125.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " (Seriously. What???)" # @t_salbatros1125.01 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Cheat codes are a deadly business, [slot_playerName]." # @t_salbatros1126.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "They break the rules." # @t_salbatros1127.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "And without rules, there’s only chaos." # @t_salbatros1128.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "They hurt people. There’s no way around that." # @t_salbatros1129.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "If you criminalize cheat codes, then only criminals will have cheat codes." # @t_salbatros1130.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_staredown as albatros
    t_ch_albatros "You’ve got an answer for everything, don’t you." # @t_salbatros1131.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Maybe I do." # @t_salbatros1132.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "Try me." # @t_salbatros1133.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    extend " (Ha! At this rate maybe I’ll make it a latte!)" # @t_salbatros1133.01 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "You won’t get away from me forever." # @t_salbatros1134.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "Maybe I want to get caught." # @t_salbatros1135.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Eventually." # @t_salbatros1136.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_notebook_inquisitive as albatros
    t_ch_albatros "Oh? And what about until then?" # @t_salbatros1137.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "What about the innocent people trapped in the crossfire?" # @t_salbatros1138.00 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "They knew the risks." # @t_salbatros1139.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "You’re enjoying this aren’t you." # @t_salbatros1140.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "….." # @t_salbatros1141.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "(Hm? Should I have played hard to get there?)" # @t_salbatros1142.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk as albatros
    t_ch_albatros "You’re a tough nut to crack, [slot_playerName]." # @t_salbatros1143.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "That’s what they call me!" # @t_salbatros1144.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    extend " (What the heck did I mean by that?!?)" # @t_salbatros1144.01 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Hm, walk it off! Do better on the next one.)" # @t_salbatros1145.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_smirk_wink as albatros
    t_ch_albatros "But I won’t give up." # @t_salbatros1146.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "Unfortunately, I can’t legally detain you any longer." # @t_salbatros1147.00 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_albatros "But it won’t end here." # @t_salbatros1148.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_albatross_welcome_staredown as albatros
    t_ch_albatros "I will get you." # @t_salbatros1149.00 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "You can try!" # @t_salbatros1150.00 self.block='Last'
    # <NHSceneChange {'name': '_2I', 'scene': 's_day2'} NHSceneChange ''>
    label s_albatros1__2I:
        # <NHSceneChange {'name': '_2I', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2