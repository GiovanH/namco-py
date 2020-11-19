# <Scene scene {'id': 's_terezi1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_terezi1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_terezi1"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_terezi1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/aroundtown.ogg" loop
    show i_bg_classroom_b as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_terezi_default_grin as terezi zorder 2:
        default
        xpos 0.7 
    t_ch_terezi "H3R3 W3 4R3" # @t_sterezi124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "W3LCOM3 TO CR1M1N4L JUST1C3 CLUB" # @t_sterezi125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1T’S RUN BY M3 SO YOU OBV1OUSLY M4D3 TH3 R1GHT CHO1C3!" # @t_sterezi126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Yeah, but you basically forced me into it!!!" # @t_sterezi127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "D3T41LS D3T41LS" # @t_sterezi128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "4NYW4Y TH4T’S BOR1NG L3T’S G3T TO TH3 GOOD STUFF" # @t_sterezi129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " L1K3…" # @t_sterezi129.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "JUST1C3 >:]" # @t_sterezi130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " 1N TH1S CLUB JUST1C3 1S WH4T W3’R3 4LL 4BOUT" # @t_sterezi130.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1F YOU C4N’T H4NDL3 TH4T…" # @t_sterezi131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "TOO B4D FOR YOU!" # @t_sterezi132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " NO M3RCY FOR W34KL1NGS OR CR1M1N4LS!" # @t_sterezi132.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Are you saying you’ll…" # @t_sterezi133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " Actually KILL me?!" # @t_sterezi133.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "H3H3H3 OF COURS3 NOT" # @t_sterezi134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    show i_cousin_default_mortified as cousin
    t_ch_terezi "1’M JUST PL4Y1NG 4ROUND" # @t_sterezi135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "DONT B3 SUCH 4 ST1CK 1N TH3 MUD!" # @t_sterezi136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1T’S JUST" # @t_sterezi137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "Y’KNOW" # @t_sterezi138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "FL4VOR T3XT TO M4K3 1T F33L MOR3 4UTH3NT1C" # @t_sterezi139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "TH1S CLUB 1S JUST 4 PL4C3 TO GOOF 4ROUND 4ND H4V3 FUN >:P" # @t_sterezi140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "...1N TH3 N4M3 OF JUST1C3 OF COURS3!" # @t_sterezi141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Oh… okay." # @t_sterezi142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Well, that’s a relief." # @t_sterezi142.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I still don’t feel like I can let my guard down around her, though.)" # @t_sterezi143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_laugh as terezi
    t_ch_terezi "H3H3H3H3! YOU’R3 FUN" # @t_sterezi144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "…Eh heh… Yeah…" # @t_sterezi145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But you know, if you’re really that interested in “justice”..." # @t_sterezi146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You could’ve just joined Meowkie on the Hall Monitor squad!" # @t_sterezi146.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "Y34H TH3 C4T S33MS PR3TTY COOL" # @t_sterezi147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "SH3 K1ND4 R3M1NDS M3 OF 4N OLD FR13ND OF M1N3" # @t_sterezi148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "BUT NO" # @t_sterezi149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "1 H4V3 4 D1FF3R3NT BR4ND OF JUST1C3 >:]" # @t_sterezi150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(What does THAT mean…)" # @t_sterezi151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "SO [slot_playerName]" # @t_sterezi152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.40 xzoom 2.5 yzoom 2.5 ypos 0.85 
    extend "{w=0.4}{nw}"
    t_ch_terezi "L3T’S T4LK 4BOUT YOU" # @t_sterezi153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin:
        # ShowWithAtl
        linear 0.20 xpos 0.28 
    extend "{w=0.2}{nw}"
    t_ch_cousin "(Eep! She’s awfully close…" # @t_sterezi154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified_blush as cousin
    extend " I can see myself reflected in those spooky red glasses…)" # @t_sterezi154.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi:
        # ActorEvent
        # ActorEvent (Transition only)
        linear 0.40 xzoom 1.0 yzoom 1.0 ypos 0.5 
    extend "{w=0.4}{nw}"
    t_ch_terezi "HOW 4BOUT YOUR CR1M1N4L P4ST?" # @t_sterezi155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " YOU D1DN’T R34LLY TH1NK YOU COULD G3T 4W4Y W1TH 1T D1D YOU" # @t_sterezi155.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "OR M4YB3 YOU’R3 TH3 OV3RCONF1D3NT TYP3" # @t_sterezi156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.53 
    extend "{w=0.2}{nw}"
    t_ch_terezi "SO SUR3 TH3Y C4N G3T 4W4Y W1TH 4NYTH1NG…" # @t_sterezi157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.5 
    extend "{w=0.2}{nw}"
    extend " N3V3R NOT1C1NG TH4T JUST1C3 1S R1GHT ON TH31R H33LS!" # @t_sterezi157.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "What?! No, no!" # @t_sterezi158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " It was an accident! Well, sort of…" # @t_sterezi158.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "I certainly didn’t mean for any of it to happen, at least." # @t_sterezi159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " When I rolled up the whole school…" # @t_sterezi159.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "4H4! YOU 4DM1T 1T!" # @t_sterezi160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "YOU ROLL3D UP TH3 SCHOOL" # @t_sterezi161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " COLL3CT1NG 3V3RY S1NGL3 D3L1C1OUS COLOR 4ND SH4D3" # @t_sterezi161.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " 4ND ROLL1NG TH3M 4LL UP 1NTO 4 B1G R41NBOW B4LL" # @t_sterezi161.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "SP4RKL1NG W1TH COLOR 4ND HUG3 3NOUGH FOR 3V3RYON3 TO G3T 4 GOOD WH1FF!" # @t_sterezi162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " 4 G14NT R41NBOW-SPR1NKL3 DONUT TR34T…" # @t_sterezi162.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "SO D3C4D3NT! 1T 4LMOST F33LS WRONG TO T4LK 4BOUT 1T" # @t_sterezi163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "H3H3H3H3" # @t_sterezi164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "That… went to a weird place." # @t_sterezi165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.7 
    extend "{w=0.2}{nw}"
    t_ch_terezi "DON’T D3NY 1T!" # @t_sterezi166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "MY DR4GON MOM T4UGHT M3 TO 3XP3R13NC3 TH3 WORLD THROUGH SC3NT 4ND T4ST3" # @t_sterezi167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_laugh as terezi
    t_ch_terezi "1 C4N SM3LL R1GHT THROUGH YOUR D3C3PT1ON!!!" # @t_sterezi168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "I-I’m not denying it!!" # @t_sterezi169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " I did it. It was a terrible mistake." # @t_sterezi169.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " I’ll definitely never try anything like that again!" # @t_sterezi169.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(Jeez, is this a club, or an interrogation?! I didn’t sign up for this!)" # @t_sterezi170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Anyway… “dragon mom”?" # @t_sterezi171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "TH4T’S NOT 1MPORT4NT R1GHT NOW" # @t_sterezi172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I think name dropping your “dragon mom” definitely warrants further-" # @t_sterezi173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_huh as terezi
    t_ch_terezi "1 S41D TH4T’S NOT 1MPORT4NT R1GHT NOW!!!" # @t_sterezi174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Okay okay, geez." # @t_sterezi175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Are all trolls as scary as you?!" # @t_sterezi175.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "H3H3! TH3Y W1SH >:]" # @t_sterezi176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha! Of course they do." # @t_sterezi177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " (Say what you will about Terezi… she’s definitely confident.)" # @t_sterezi177.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "SO YOU S4Y YOU W1LL N3V3R ROLL UP YOUR B1G R41NBOW DONUT 4G41N…" # @t_sterezi178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    extend " H4! 4 L1K3LY STORY!!!" # @t_sterezi178.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "By “rainbow donut”, you mean my katamari, right?" # @t_sterezi179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "SHUT UP" # @t_sterezi180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Yes ma’am." # @t_sterezi181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "YOUR WORDS 4R3 HOLLOW, COTTON C4NDY" # @t_sterezi182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    extend " FULL OF HOL3S… JUST L1K3 YOUR B1G D3L1C1OUS DONUT!" # @t_sterezi182.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "YOU S4Y 1T’S B3H1ND YOU BUT 1 B3T YOU’R3 JUST 1TCH1NG TO DO 1T 4G41N" # @t_sterezi183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " BR34K 1T OUT OF TH3 W34PONS V4ULT 4ND GO CR4ZY ON3 MOR3 T1M3" # @t_sterezi183.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "ROLL1NG UP 4LL THOS3 MOUTHW4T3R1NG COLORS 1NTO 4 G14NT…" # @t_sterezi184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " 1RR3S1ST4BL3…" # @t_sterezi184.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " MOUNT41N OF FL4VOR…" # @t_sterezi184.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "1’M S4L1V4T1NG JUST TH1NK1NG 4BOUT 1T" # @t_sterezi185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "It… kinda sounds like you actually WANT me to do it." # @t_sterezi186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "H3H3H3 NOW WH3R3 WOULD YOU G3T TH4T 1D34" # @t_sterezi187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "B-but… but this is the Criminal Justice club!" # @t_sterezi188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " Why would you suggest I do something so CLEARLY against the rules?!" # @t_sterezi188.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "DON’T T4K3 TH1NGS SO L1T3R4LLY COTTON C4NDY" # @t_sterezi189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    extend " DON’T YOU KNOW FL1RT1NG WH3N YOU S33 1T?" # @t_sterezi189.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "1 DO 4ND 1 C4N’T 3V3N S33!" # @t_sterezi190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(How often is she gonna play that card?!)" # @t_sterezi191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "CUT3 G1RLS L1K3 TO M3SS W1TH COOLK1DS L1K3 YOU" # @t_sterezi192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified_blush as cousin
    with Dissolve(.333)
    extend " 1T G3TS TH3M 4LL FLUST3R3D WH1CH 1S PR3TTY CUT3 <3" # @t_sterezi192.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "UNFORTUN4T3LY YOU’R3 4LMOST TOO 34SY OF 4 T4RG3T" # @t_sterezi193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " YOU M3LT F4ST3R TH4N 4 HOOFB34ST 1N 4N 4DH3S1V3 F4CTORY" # @t_sterezi193.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "WH1CH 1S TOO B4D B3C4US3 1 LOV3 TH3 THR1LL OF TH3 CH4S3 >:P" # @t_sterezi194.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(I have… a lot… of mixed feelings...about...this converstion.)" # @t_sterezi195.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Listen, Terezi… I don’t know what you’ve heard, or smelled, or what…" # @t_sterezi198.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " But I seriously promise I won’t do my katamari stuff again! Okay?!" # @t_sterezi198.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_huh as terezi
    t_ch_terezi "UGGGGHHH! YOU’R3 SO BOR1NG!!!" # @t_sterezi199.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "JUST L1K3 MY OLD P4RTN3R" # @t_sterezi1100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    extend " YOU R3M1ND M3 OF H1M 1N 4 LOT OF W4YS…" # @t_sterezi1100.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " H3 THOUGHT H3 W4S TH3 L34D3R, TH3 VO1C3 OF R34SON" # @t_sterezi1100.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "OBV1OUSLY TH4T W4S JUST WH4T 1 4LLOW3D H1M TO TH1NK >:P" # @t_sterezi1101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    extend " ST1LL 3V3N THOUGH H3 W4S SO STUFFY..." # @t_sterezi1101.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "1 K1ND4 M1SS H1M SOM3T1M3S" # @t_sterezi1102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Old partner?!" # @t_sterezi1103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised_blush as cousin
    with Dissolve(.333)
    extend " Does she mean, like, an ex?!" # @t_sterezi1103.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Wait a minute! Come to think of it-)" # @t_sterezi1104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "W-wait… are you implying we’re already “partners”?!" # @t_sterezi1105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_huh as terezi
    t_ch_terezi "WHO C4R3S" # @t_sterezi1106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " H3’S LONG GON3 NOW 4NYW4Y…" # @t_sterezi1106.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "B3S1D3S HOW COULD 4N 4G3NT OF JUST1C3 L1K3 M3 P4RTN3R UP W1TH 4 D3T3ST4BL3 CR1M1N4L L1K3 YOU? >:]" # @t_sterezi1107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Wait, but…" # @t_sterezi1108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    extend " Aren’t you a “criminal” too?" # @t_sterezi1108.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "We met in detention, after all." # @t_sterezi1109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "NOT TH3 S4M3" # @t_sterezi1110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    extend " 1 W4S 4 POL1T1C4L PR1SON3R" # @t_sterezi1110.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Whaaat?!" # @t_sterezi1111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "Y34H TH3Y GOT M3 ON CH4RG3S OF V4ND4L1SM" # @t_sterezi1112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "SOOOOOOOO R1D1CULOUS!" # @t_sterezi1113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " CH4LK W4SH3S R1GHT OFF 4NYW4Y" # @t_sterezi1113.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "4SP3C14LLY WH3N YOU US3 YOUR OWN TONGU3 >:P" # @t_sterezi1114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(How does that… make her… a “political prisoner”..." # @t_sterezi1115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " You know what, no. I’m not touching any part of that statement with a ten foot pole.)" # @t_sterezi1115.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "4NYW4Y W3’R3 G3TT1NG OFF TOP1C" # @t_sterezi1116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " TH3 PO1NT 1S" # @t_sterezi1116.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "1M DY1NG TO S33 TH4T R41NBOW DONUT TR34T OF YOURS!" # @t_sterezi1117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " JUST DYYYYY1NG!" # @t_sterezi1117.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "SO HURRY UP 4ND BR34K YOUR B1G COLOR-B4LL TH1NGY FR33 4ND DO 1T 4G41N!" # @t_sterezi1118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_laugh as terezi
    t_ch_terezi "1T W4S TOO D3L1C1OUS TO R3S1ST…" # @t_sterezi1119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " 4ND 1 N3V3R GOT 4 CH4NC3 TO T4ST3 1T MYS3LF!" # @t_sterezi1119.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "S-some “Criminal Justice” club this is!" # @t_sterezi1120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You keep encouraging me to break the rules!" # @t_sterezi1120.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    show i_cousin_default_mortified as cousin
    t_ch_terezi "4W C’MON COTTON C4NDY" # @t_sterezi1121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    extend " DO 1T FOR M3??" # @t_sterezi1121.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1 KNOW YOU DON’T W4NT TO S33 4 B34UT1FUL TROLL G1RL S4D >:]" # @t_sterezi1122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "You have literally never stopped grinning the entire time I’ve known you." # @t_sterezi1123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "S3R1OUSLY THOUGH" # @t_sterezi1124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " 1’M NOT M3SS1NG W1TH YOU TH1S T1M3" # @t_sterezi1124.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1’D R34LLY L1K3 TO S33 1T 4G41N…" # @t_sterezi1125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " SO TH1NK 4BOUT 1T, OK4Y?" # @t_sterezi1125.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "…" # @t_sterezi1126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "TH4T’S 1T! JUST1C3 CLUB 1S OV3R" # @t_sterezi1127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.50 xpos 0.4 
    extend "{w=0.5}{nw}"
    extend " OUT OUT OUT!" # @t_sterezi1127.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.20 xpos 0.2 
    extend "{w=0.2}{nw}"
    t_ch_cousin "(Whaa? That was fast! She’s shoving me right out the door!)" # @t_sterezi1128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.50 xpos -0.5 
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.50 xpos -0.5 
    $ renpy.pause(0.5, hard=True) # TimedPause
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # Curtain fade
    show i_bg_hallway_b as bg # behind curtain
    # <SettingChange SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_hallway_b', 'curtainActor': 'curtain', 'curtainFadeTime': '.75', 'name': '_2P', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.5 xpos 0.3 
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.5 xpos 0.7 
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "TH1NK 1T OV3R, OK4Y COTTON C4NDY?" # @t_sterezi1129.00 self.block='Last'
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.40 xpos 0.44 
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_mortified_blush as cousin
    t_ch_cousin "(OH MY GOD NOW SHE'S LICKING ME RIGHT ON THE FACE WHAT DO I DO WHAT DO I DO?!?!)" # @t_sterezi1130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.5 
    extend "{w=0.2}{nw}"
    t_ch_terezi "…" # @t_sterezi1131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified_blush as cousin
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.7 
    extend "{w=0.2}{nw}"
    t_ch_terezi "SM3LL YOU L4T3R <3" # @t_sterezi1132.00 self.block='Last'
    show i_terezi_default_grin as terezi:
        # FadeEvent
        linear 0.6 alpha 0.0
    play sound ["<silence 0.3>", "sfx/slam.ogg"]
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "She slammed the door right in my face…" # @t_sterezi1133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "Man, what a confusing day." # @t_sterezi1134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Why does the leader of the Criminal Justice Club want me to break rules so bad?" # @t_sterezi1134.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "She says it's just for the colors she loves…" # @t_sterezi1135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " She does seem to go nuts for that stuff." # @t_sterezi1135.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And… of course I’d love to make her happy, but…" # @t_sterezi1135.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Can I trust her? She’s not exactly giving me a whole lot of reasons to." # @t_sterezi1136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad_blush as cousin
    t_ch_cousin "And what’s the deal with that “old partner” anyway?!" # @t_sterezi1137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " ...Not that I’m jealous or anything…" # @t_sterezi1137.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral_blush as cousin
    t_ch_cousin "Sigh… I can’t believe she actually licked me." # @t_sterezi1138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise_blush as cousin
    t_ch_cousin "...Omigosh!!!" # @t_sterezi1139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Does that mean we’re married in Troll World?!)" # @t_sterezi1140.00 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_2j', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
    label s_terezi1__2j:
        # <NHSceneChange NHSceneChange {'name': '_2j', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
        jump s_day2