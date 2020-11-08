# <Scene {'id': 's_terezi3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_terezi3:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_terezi3"
    $ renpy.pause(1)
    # <Scene {'id': 's_terezi3', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/privatetimes.ogg" loop
    show i_bg_cliff_night as bg zorder 0 at default
    show i_event_terezi_scene3 as event zorder 6:
        default
        alpha 0.0
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_terezi_default_laugh as terezi zorder 2:
        default
        xpos 0.7 
        alpha 0.0

    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(I think this is where Terezi wanted me to meet her…" # @t_sterezi338.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I keep walking and walking, though, and I haven’t seen anyone yet." # @t_sterezi338.01 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Except for these weird… plush toys?" # @t_sterezi339.00 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Someone seems to have arranged them on the ground…" # @t_sterezi339.01 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    extend " They look like small … lizards? Or dragons or something…" # @t_sterezi339.02 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "And they’re all different bright colors, with beady button eyes." # @t_sterezi340.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " They look almost like they’re… staring at me…" # @t_sterezi340.01 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "Haha, that’s silly. They’re just toys!" # @t_sterezi341.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " Right…?!" # @t_sterezi341.01 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "They’re arranged in rows… almost like a…)" # @t_sterezi342.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_laugh as terezi:
        # FadeEvent
        linear 0.2 alpha 1.0
    extend "{w=0.2}{nw}"
    t_ch_terezi "H3LLO TH3R3 COTTON C4NDY <3" # @t_sterezi343.00 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "1 S33 YOU’V3 NOT1C3D TH3 JURY FOR YOUR TR14L TOD4Y" # @t_sterezi344.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "1’V3 S3L3CT3D 4 NUMB3R OF 1MP4RT14L SC4L3M4T3 JURORS" # @t_sterezi345.00 self.block='Last'
    show i_event_terezi_scene3 as event:
        # ShowWithAtl
        linear 1 alpha 1.0
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "W3 W4NT TO K33P TH1NGS F41R, 4FT3R 4LL >:]" # @t_sterezi346.00 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    show i_terezi_lean_grin as terezi
    t_ch_cousin "“S-scalemates”? Is that what those things are called?" # @t_sterezi347.00 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What are they, iguanas or something?!" # @t_sterezi347.01 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_huh as terezi
    t_ch_terezi "DON’T YOU KNOW TH3 NOBL3 V1S4G3 OF 4 DR4GON WH3N YOU S33 ON3?!" # @t_sterezi348.00 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I… I guess not…" # @t_sterezi349.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " But what did you mean by… “trial”?" # @t_sterezi349.01 self.block='Last'
    # <ParallelEvent {'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "Y3S Y3S, YOUR TR14L" # @t_sterezi350.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "W3 W3R3 WORR13D YOU’D TRY  TO SK1P YOUR COURT D4T3, COTTON C4NDY" # @t_sterezi351.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "TH3N W3’D H4V3 TO PUT OUT 4 W4RR4NT FOR YOUR 4RR3ST WH1CH WOULD B3 NO FUN 4T 4LL… >:P" # @t_sterezi352.00 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "“Court date”???" # @t_sterezi353.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I have no idea what’s going on." # @t_sterezi353.01 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I was kinda hoping this would be a regular date..." # @t_sterezi354.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "H3H3H3!" # @t_sterezi355.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    show i_cousin_exhausted_neutral as cousin
    t_ch_terezi "DON’T TRY TO SW33T T4LK TH3 PROS3CUTOR, COTTON C4NDY" # @t_sterezi356.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_terezi "YOU M4Y B3 3XC3PT1ON4LLY 4DOR4BL3…" # @t_sterezi357.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "(Gulp!!)" # @t_sterezi358.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.65 
    extend "{w=0.2}{nw}"
    t_ch_terezi "BUT TH4T WON’T S4V3 YOU 1N MY COURTROOM" # @t_sterezi359.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "(Aww.)" # @t_sterezi360.00 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_terezi "MY BLOOD T4ST3S L1K3 1C3 COLD BLU3 R4SPB3RRY SLUSH13" # @t_sterezi361.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "WH1CH 1S F1TT1NG B3C4US3, MUCH L1K3 MY BLOOD…" # @t_sterezi362.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "1 4M 4LSO 1C3 COLD!!!" # @t_sterezi363.00 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(How does she know what her own blood tastes like?" # @t_sterezi364.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    extend " You know what… I don’t want to even think about it.)" # @t_sterezi364.01 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "4R3 YOU R34DY TO B3G1N TH3 TR14L?!" # @t_sterezi365.00 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "I don’t even know what the trial is for!" # @t_sterezi366.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_laugh as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.7 
    extend "{w=0.2}{nw}"
    t_ch_terezi "4H4! COTTON C4NDY 4DM1TS TO NOT 3V3N KNOW1NG WH4T TH3 TR14L 1S FOR!" # @t_sterezi367.00 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    show i_cousin_default_mortified as cousin
    t_ch_terezi "4 M4N1C GR1N SL1D3S 4CROSS TH3 PROS3CUTOR’S F4C3" # @t_sterezi368.00 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "H3R PR3Y 1S 4LR34DY SO CLOS3 SH3 C4N T4ST3 1T" # @t_sterezi369.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "ON3 MOR3 F4LS3 MOV3 4ND TH1S C4S3 W1LL B3 4LL WR4PP3D UP" # @t_sterezi370.00 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "TH3 JURORS 4R3 ON TH3 3DG3 OF TH31R S34TS, V1BR4T1NG W1TH TH3 3XC1T3M3NT OF 4 P4CK OF HUNGRY WOLV3S!" # @t_sterezi371.00 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Wh-what is this?! Why are you narrating what’s happening in third person?!" # @t_sterezi372.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "F1RST QU3ST1ON!" # @t_sterezi373.00 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "WH3R3 W3R3 YOU ON TH3 N1GHT OF TH3 G14NT R41NBOW DONUT TR34T 1NC1D3NT?!" # @t_sterezi374.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Rainbow Donut Treat is what she calls my katamari, right??)" # @t_sterezi375.00 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Uh… I guess I was rolling my katamari through the school?" # @t_sterezi376.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Remember?! I’m pretty sure you were there…" # @t_sterezi376.01 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "4-H4! 4NOTH3R 4DM1SS1ON OF GU1LT!" # @t_sterezi377.00 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "TH3 D3F3ND4NT 1S SH4K1NG L1K3 4 L34F" # @t_sterezi378.00 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "TH3 SM3LL OF T3RR1F13D W4T3RM3LON-FL4VOR BUBBL3GUM W4FTS THROUGH TH3 COLD N1GHT 41R…" # @t_sterezi379.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(I am NOT shaking like a leaf!)" # @t_sterezi380.01 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "YOU’R3 NOT YOURS3LF TOD4Y COTTON C4NDY" # @t_sterezi381.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.67 
    extend "{w=0.2}{nw}"
    t_ch_terezi "SOM3TH1NG ON YOUR M1ND P3RH4PS?" # @t_sterezi382.00 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.6 
    extend "{w=0.2}{nw}"
    t_ch_terezi "SOM3 SOURC3 OF GU1LT W31GH1NG OPPR3SS1V3LY ON YOUR SOUL?!" # @t_sterezi383.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "B-but you already knew I rolled the school up with my katamari that day!" # @t_sterezi384.00 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "I-I think you even wanted me to do it again?" # @t_sterezi385.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " You keep suggesting I break it out of the weapons locker…" # @t_sterezi385.01 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Why am I on trial for this?" # @t_sterezi386.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin:
        # ShowWithAtl
        linear 0.20 xpos 0.25 
    extend "{w=0.2}{nw}"
    extend " WHAT’S GOING ON?!" # @t_sterezi386.01 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_laugh as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.55 
    extend "{w=0.2}{nw}"
    t_ch_terezi "S1L3NC3 COTTON C4NDY!!!" # @t_sterezi387.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi:
        # ShowWithAtl
        linear 0.30 xpos 0.65 
    extend "{w=0.3}{nw}"
    t_ch_terezi "L4ST QU3ST1ON…" # @t_sterezi388.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "DO YOU R3COGN1Z3… TH1S P3RSON?!" # @t_sterezi389.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(She’s shoving a photograph in my face…)" # @t_sterezi390.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "It looks like… another one of those Scalemate plush things…" # @t_sterezi391.00 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You know, exactly like all the other ones you have arranged here." # @t_sterezi391.01 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_huh as terezi
    t_ch_terezi "OH Y34H" # @t_sterezi392.00 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "SORRY 4BOUT TH4T" # @t_sterezi393.00 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "TH1S 1S 4 BL4CK 4ND WH1T3 PHOTOGR4PH, SO YOU C4N’T R34LLY T3LL WH1CH ON3 1T 1S" # @t_sterezi394.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "SN1111FFFFFF!" # @t_sterezi395.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Wha?! She shoved the photo into her face to smell it?!)" # @t_sterezi396.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_laugh as terezi
    t_ch_terezi "4HH 1 LOV3 TH3 SM3LL OF GR4Y…" # @t_sterezi397.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "L1K3 TH3 T4ST3 OF R41N ON TH3 41R ON 4 W4RM CLOUDY N1GHT…" # @t_sterezi398.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "OR OF TH3 4SH3S OF 4 D3STROY3D 3N3MY! >:]" # @t_sterezi399.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Oh… Kay…" # @t_sterezi3100.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "So why are you showing me a photo of a Scalemate again?" # @t_sterezi3101.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "1F TH1S PHOTO W3R3 1N COLOR YOU WOULD S33 TH4T TH1S P4RT1CUL4R SC4L3M4T3…" # @t_sterezi3102.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "H4S BUTTON 3Y3S TH3 D3L1C1OUS COLOR OF CH3RRY R3D…" # @t_sterezi3103.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "4ND WH1T3 FL3SH L1K3 CR1SP V4N1LL4 1C3 CR34M" # @t_sterezi3104.00 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_laugh as terezi
    t_ch_terezi "4S YOU C4N PROB4BLY T3LL H3 W4S TH3 MOST D3L1C1OUS SC4L3M4T3 3V3R!" # @t_sterezi3105.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "4ND H3 W4S 4LSO TH3 MOST LOY4L, TH3 MOST LOV1NG…" # @t_sterezi3106.00 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "TH3 B3ST P4RTN3R 4 TROLL COULD 3V3R H4V3" # @t_sterezi3107.00 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "R1NG 4NY B3LLS Y3T COTTON C4NDY?!" # @t_sterezi3108.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Um…" # @t_sterezi3109.00 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " No?" # @t_sterezi3109.01 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "TH1S SC4L3M4T3…" # @t_sterezi3110.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "W4S MY OLD P4RTN3R…" # @t_sterezi3111.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "PYR4LSP1T3!" # @t_sterezi3112.00 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "H3 W4S BY MY S1D3 FOR M4NY SW33PS…" # @t_sterezi3113.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "BUT WH3N 4 C3RT41N 1NC1D3NT B3F3LL N4MCO H1GH" # @t_sterezi3114.00 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_huh as terezi
    t_ch_terezi "H3 D1S4PP34R3D!" # @t_sterezi3115.00 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "1 KNOW MY PYR4LSP1T3 WOULD N3V3R L34V3 M3" # @t_sterezi3116.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "WH3N YOU’V3 B33N P4RTN3RS FOR TH4T LONG, TH3 BOND DO3SN’T D1SSOLV3 SO 34S1LY!" # @t_sterezi3117.00 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "BUT S1NC3 H3 D1S4PP34R3D ON TH3 D4Y OF YOUR R41NBOW DONUT TR34T 1NC1D3NT…" # @t_sterezi3118.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "W3LL YOU PUT TH3 P13C3S TOG3TH3R COTTON C4NDY!" # @t_sterezi3119.00 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "What?!" # @t_sterezi3120.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    extend " THAT’S who your old partner was?!" # @t_sterezi3120.01 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Just another dumb toy? Of which you obviously still have many?!" # @t_sterezi3121.00 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " I thought he was like, an ex-boyfriend or something." # @t_sterezi3121.01 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_laugh as terezi
    t_ch_terezi "H3H3H3!" # @t_sterezi3122.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "TH3 LOV3 PYR4LSP1T3 4ND 1 SH4R3D W3NT F4R D33P3R TH4N 4NY OF TH3 FOUR QU4DR4NTS..." # @t_sterezi3123.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(Quadrants?!" # @t_sterezi3124.00 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "No, I think my policy of not asking about troll stuff has served me pretty well thus far.)" # @t_sterezi3125.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "GOT 4NYTH1NG TO S4Y FOR YOURS3LF, COTTON C4NDY?!" # @t_sterezi3126.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "TH3 CLOCK 1S T1CK1NG!" # @t_sterezi3127.00 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "I don’t even know what you’re talking about!" # @t_sterezi3128.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I had no idea about Pyralspite before, so how can I know what happened to him?!" # @t_sterezi3128.01 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Listen to me. “Him”. It’s a stuffed animal for pete’s sake!" # @t_sterezi3129.00 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_huh as terezi
    t_ch_terezi "YOU SHUT YOUR MOUTH 4BOUT PYR4LSP1T3 OR 1 W1LL HOLD YOU 1N CONT3MPT!!!" # @t_sterezi3130.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "How can that be any worse than what you’re already doing to me?!" # @t_sterezi3131.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_terezi "1 DON’T 3V3N N33D TO FL1P MY CO1N FOR TH1S ON3" # @t_sterezi3132.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "TH3 JURORS 4GR33-" # @t_sterezi3133.00 self.block='Last'
    show i_event_terezi_scene3 as event:
        # ShowWithAtl
        linear .5 alpha 0.0
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "YOU’R3 GU1LTY, COTTON C4NDY" # @t_sterezi3134.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "B3YOND 4 SH4DOW OF 4 DOUBT!" # @t_sterezi3135.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "GU1LTY!" # @t_sterezi3136.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Guilty of WHAT?!" # @t_sterezi3137.00 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "H3H3H3!" # @t_sterezi3138.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "WOULDN’T YOU L1K3 TO KNOW?" # @t_sterezi3139.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "YES!!!" # @t_sterezi3140.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_lean_huh as terezi
    t_ch_terezi "TOO L4T3 COTTON C4NDY" # @t_sterezi3141.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_rope_grin as terezi
    t_ch_terezi "TH3 G4V3L H4S COM3 DOWN!" # @t_sterezi3142.00 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Omigosh… she brought out a length of rope…" # @t_sterezi3143.00 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    extend " IS SHE GOING TO HANG ME LIKE IN THE MOVIES?!" # @t_sterezi3143.01 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "No wait, she’s just tying it around my waist…" # @t_sterezi3144.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It looks like she’s just tying me to one of these trees, so I can’t move." # @t_sterezi3144.01 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    extend " That’s not as bad as hanging." # @t_sterezi3144.02 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "...Wait a minute!" # @t_sterezi3145.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    extend " It’s still bad though!!!)" # @t_sterezi3145.01 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "YOUR S3NT3NC3 H4S B33N D3L1V3R3D" # @t_sterezi3146.00 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_rope_resigned as terezi
    t_ch_terezi "N1C3 TRY, COTTON C4NDY…" # @t_sterezi3147.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_rope_laugh as terezi
    t_ch_terezi "BUT YOU C4N N3V3R 3SC4P3 TH3 LONG 4RM OF TH3 L4W!" # @t_sterezi3148.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "W-wait a minute! Terezi! You’re not gonna just leave me here are you?!" # @t_sterezi3149.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "S33 YOU L4T3R COTTON C4NDY!" # @t_sterezi3150.00 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_terezi "<3 <3 <3" # @t_sterezi3151.00 self.block='Last'
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear .5 alpha 0.0
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "WHAT?! What did I even do?!" # @t_sterezi3152.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " What IS this?!" # @t_sterezi3152.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " You’re crazy!" # @t_sterezi3152.02 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Wait a minute… she’s way too young to have passed the bar already." # @t_sterezi3153.00 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " There’s no way she could be a certified lawyer!" # @t_sterezi3153.01 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " This trial was a farce!)" # @t_sterezi3153.02 self.block='Last'
    # <ParallelEvent {'name': '_2L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "TEREZI!!!" # @t_sterezi3154.00 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75)
    show i_bg_cliff_night as bg # behind curtain
    # <SettingChange {'bgActor': 'bg', 'bgImage': '@i_bg_cliff_night', 'curtainActor': 'curtain', 'curtainFadeTime': '0.75', 'name': '_2M'} SettingChange ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        linear 0.20 xpos 0.3 
    show i_terezi_default_grin as terezi:
        # FadeEvent
        linear 0.2 alpha 0.0
    show i_digdug_left as digdug zorder 1:
        default
        alpha 0.0
        xpos 0.8 
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75)
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "[slot_playerName]? Where are you?" # @t_sterezi3155.00 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Oh thank goodness! Someone finally found me!" # @t_sterezi3156.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_digdug_left as digdug:
        # FadeEvent
        linear 0.2 alpha 1.0
    extend "{w=0.2}{nw}"
    t_ch_digdug "What are you doing, tying yourself to a tree?!" # @t_sterezi3157.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "Trying to get out of detention, eh?" # @t_sterezi3158.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Well, you also missed a few of your classes, too!" # @t_sterezi3158.01 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "That calls for DOUBLE DETENTION!" # @t_sterezi3159.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "How could I have tied myself to a tree?" # @t_sterezi3160.00 self.block='Last'
    # <ParallelEvent {'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " Obviously I didn’t mean for this to happen…" # @t_sterezi3160.01 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Isn’t being left out here for hours punishment enough?" # @t_sterezi3161.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_digdug "Hmm… Good point." # @t_sterezi3162.00 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_digdug "But, no." # @t_sterezi3163.00 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "(...Terezi, you planned this didn’t you!" # @t_sterezi3164.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " You’re either a mastermind…" # @t_sterezi3164.01 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Or totally insane.)" # @t_sterezi3164.02 self.block='Last'
    # <NHSceneChange {'name': '_2b', 'scene': 's_day4'} NHSceneChange ''>
    label s_terezi3__2b:
        # <NHSceneChange {'name': '_2b', 'scene': 's_day4'} NHSceneChange ''>
        jump s_day4