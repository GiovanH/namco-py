# <Scene scene {'id': 's_terezi5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_terezi5:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_terezi5"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_terezi5', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/romance.ogg" loop
    show i_bg_quad_bleachers as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.3 
    show i_terezi_default_grin as terezi zorder 2:
        default
        xpos 0.7 
    show i_pacman_left as pacman zorder 2:
        default
        xpos -0.49 

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(And so, once detention was over, we both took a walk down in the quad.)" # @t_sterezi524.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.65 
    extend "{w=0.2}{nw}"
    t_ch_terezi "H3R3, 1 BROUGHT YOU SOM3TH1NG TO SN4CK ON" # @t_sterezi525.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...Um…" # @t_sterezi526.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "This is just a fistful of brightly-colored chalk." # @t_sterezi527.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_laugh as terezi
    t_ch_terezi "Y34H!" # @t_sterezi528.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "1T’S MY F4VOR1T3 FOR WH3N 1 H4V3 TO TH1NK SOM3TH1NG OV3R" # @t_sterezi529.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_laugh as terezi
    t_ch_terezi "...OR WH3N 1’M JUST PL41N HUNGRY >:]" # @t_sterezi530.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    show i_terezi_default_grin as terezi
    t_ch_cousin "Um. Thanks, I guess." # @t_sterezi531.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    show i_terezi_default_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.7 
    extend "{w=0.2}{nw}"
    t_ch_terezi "1’M SORRY 4BOUT TH3 OTH3R D4Y, COTTON C4NDY" # @t_sterezi532.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "W3LL 4CTU4LLY" # @t_sterezi533.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "1’M NOT SORRY TH4T 1T H4PP3N3D" # @t_sterezi534.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "4NYON3 W1TH H4LF 4 M1ND COULD S33 TH4T TH3 3V3NTS 4S TH3Y UNFOLD3D W3R3 ULT1M4T3LY 1N3V1T4BL3" # @t_sterezi535.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "...Uh huh." # @t_sterezi536.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "BUT 1 4M SORRY 1 H4D TO B3 TH3 1NSTRUM3NT THROUGH WH1CH YOUR JUST1C3 W4S D3L1V3R3D >:]" # @t_sterezi537.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "4LTHOUGH YOU D1D LOOK 4WFULLY CUT3 SQU1RM1NG 4W4Y DUR1NG YOUR 1NT3RROG4T1ON" # @t_sterezi538.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Terezi, I-" # @t_sterezi539.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I don’t get it?" # @t_sterezi539.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_huh as terezi
    t_ch_terezi "HUH? WH4T DO YOU M34N?" # @t_sterezi540.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "WH4T’S NOT TO G3T?" # @t_sterezi541.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "You do all this mean stuff to me…" # @t_sterezi542.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You declare me guilty for a crime that I’m pretty sure I didn’t commit…" # @t_sterezi542.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " In fact, I don’t even know what the crime really WAS!" # @t_sterezi542.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "Something to do with your old Scalemate, or something?!" # @t_sterezi543.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_huh as terezi
    t_ch_terezi "PYR4LSP1T3 >:|" # @t_sterezi544.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Yeah, him." # @t_sterezi545.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    with Dissolve(.333)
    show i_terezi_default_grin as terezi
    t_ch_cousin "But then, you act all… flirty with me?" # @t_sterezi546.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You call me cutesy nicknames…" # @t_sterezi546.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified_blush as cousin
    extend " You LICK me…" # @t_sterezi546.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    extend " You bring me presents and want to spend time with me…" # @t_sterezi546.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "I have no idea what’s going on!" # @t_sterezi547.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "Can you please just…" # @t_sterezi548.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " Say what’s on your mind?" # @t_sterezi548.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And not just dance around it?" # @t_sterezi548.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "[slot_playerName]" # @t_sterezi549.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "4R3 YOU R34LLY TH1S D3NS3?!" # @t_sterezi550.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1… 1 R34LLY F33L TH4T 1 COULD NOT H4V3 B33N MOR3 CL34R 1F 1 TR13D!" # @t_sterezi551.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_pout as terezi
    t_ch_terezi "M4YB3 YOU JUST DON’T F33L TH3 S4M3?" # @t_sterezi552.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "If… if you’re asking me if I like you…" # @t_sterezi553.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I mean, kinda, yeah!" # @t_sterezi554.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral_blush as cousin
    extend " But I’m so confused right now…" # @t_sterezi554.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin:
        # ShowWithAtl
        linear 0.20 xpos 0.25 
    extend "{w=0.2}{nw}"
    extend " And kinda scared of you." # @t_sterezi554.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "I don’t know what to think." # @t_sterezi555.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "…" # @t_sterezi556.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_huh as terezi
    t_ch_terezi "OH" # @t_sterezi557.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "OOOOOOOHH" # @t_sterezi558.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "OH, NO!!!" # @t_sterezi559.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_pout as terezi
    t_ch_terezi "[slot_playerName] D1D YOU TH1NK TH1S W4S…" # @t_sterezi560.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_huh as terezi
    t_ch_terezi "4 R3D TH1NG?!" # @t_sterezi561.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Red?" # @t_sterezi562.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You mean like your glasses?" # @t_sterezi562.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "NO DUMMY" # @t_sterezi563.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1 M34N L1K3 R3D-R3D" # @t_sterezi564.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "YOU KNOW, TH3 FLUSH3D QU4DR4NT?" # @t_sterezi565.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Flushed… quad…?" # @t_sterezi566.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "…" # @t_sterezi567.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Is this another one of those times…" # @t_sterezi567.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Where you say a bunch of stuff I don’t understand…" # @t_sterezi568.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " And then do something really awful to me? :(" # @t_sterezi568.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_terezi "OH [slot_playerName]!" # @t_sterezi569.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1 THOUGHT YOU UND3RSTOOD!" # @t_sterezi570.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_huh as terezi
    t_ch_terezi "M4N 1’V3 B33N GO1NG 4BOUT TH1S TOT4LLY TH3 WRONG W4Y >:\\" # @t_sterezi571.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_pout as terezi
    t_ch_terezi "1’M SO SO SORRY!" # @t_sterezi572.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "4ND 1 M34N… R34LLY SORRY" # @t_sterezi573.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "NOT JUST PR3T3ND1NG TO B3 SORRY SO YOU L3T YOUR GU4RD DOWN!" # @t_sterezi574.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "…" # @t_sterezi576.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_huh as terezi
    t_ch_terezi "DO YOU NOT H4V3 QU4DR4NTS WH3R3 YOU COM3 FROM?" # @t_sterezi577.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Um…" # @t_sterezi578.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I don’t THINK so?" # @t_sterezi578.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "H3R3 1’LL TRY TO K33P TH1S S1MPL3" # @t_sterezi579.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "ON MY PL4N3T…" # @t_sterezi580.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "W3 H4V3 FOUR D1FF3R3NT K1NDS OF ROM4NC3" # @t_sterezi581.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "FOUR QU4DR4NTS, YOU S33?" # @t_sterezi582.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "TWO OF TH3M 4R3 SORT OF PL4TON1C" # @t_sterezi583.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "1T’D B3 TOO MUCH TO G3T 1NTO TH3M 4LL R1GHT NOW" # @t_sterezi584.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "BUT TH3 ON3S YOU N33D TO KNOW 4BOUT 4R3 R3D ROM4NC3…" # @t_sterezi585.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "WH1CH 1S WH4T NORM4L HUM4NS F33L 4ND WH4T 1 TH1NK YOU’V3 B33N F33L1NG FOR M3…" # @t_sterezi586.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "4ND BL4CK ROM4NC3" # @t_sterezi587.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "WH1CH 1S WH4T 1’V3 B33N F33L1NG FOR YOU" # @t_sterezi588.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Is that as scary as it sounds…" # @t_sterezi589.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "K1ND OF?" # @t_sterezi590.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    show i_cousin_default_neutral as cousin
    t_ch_terezi "1 DON’T R34LLY KNOW HOW TO D3SCR1B3 1T TO SOM3ON3 WHO D1DN’T GROW UP W1TH 1T" # @t_sterezi591.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "B4S1C4LLY R3D LOV3 1S B4S3D ON H4V1NG N1C3 F33L1NGS 4ND LOV1NG 34CH OTH3R" # @t_sterezi592.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "BUT BL4CK ROM4NC3 1S B4S3D ON H4T1NG 34CH OTH3R!" # @t_sterezi593.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "BUT 1N 4 MOR3 1NT3NS3, FOCUS3D W4Y…" # @t_sterezi594.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1T’S TWO P3OPL3 H4T1NG 34CH OTH3R TH3 S4M3 W4Y TWO P3OPL3 M1GHT LOV3 34CH OTH3R" # @t_sterezi595.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "4ND BU1LD1NG 4 R3L4T1ONSH1P B4S3D ON TH4T!" # @t_sterezi596.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Like… an arch rival or something?" # @t_sterezi597.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_laugh as terezi
    show i_cousin_default_neutral as cousin
    t_ch_terezi "SORT OF!" # @t_sterezi598.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "1 GU3SS TH4T’S TH3 CLOS3ST 3QU1V4L3NT" # @t_sterezi599.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "BUT K1ND4 MOR3 SP3C14L TH4N TH4T TOO" # @t_sterezi5100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "WH3N YOU H4V3 BL4CK F33L1NGS FOR SOM3ON3…" # @t_sterezi5101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "TH3Y’R3 C4LL3D YOUR “K1SM3S1S”" # @t_sterezi5102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.65 
    extend "{w=0.2}{nw}"
    t_ch_terezi "1’V3 B33N W4NT1NG TO M4K3 YOU MY K1SM3S1S FOR 4 LONG T1M3 NOW!" # @t_sterezi5103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "1F 1 H4D KNOWN YOU D1DN’T UND3RST4ND WH4T TH4T M34NT…" # @t_sterezi5104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1 WOULD H4V3 B33N 4 LOT MOR3 UP FRONT 4BOUT MY F33L1NGS" # @t_sterezi5105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1’M SORRY!" # @t_sterezi5106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral_blush as cousin
    t_ch_cousin "Gosh, this is all so confusing…" # @t_sterezi5107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Terezi, I’m sorry, I’m trying to understand, but…" # @t_sterezi5108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad_blush as cousin
    extend " I don’t think I can return your feelings." # @t_sterezi5108.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I like you, but … not in that way?" # @t_sterezi5109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Er, a hate way?" # @t_sterezi5109.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_pout as terezi
    t_ch_terezi "4WW, 4R3 YOU SUR3?" # @t_sterezi5110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "YOU H4V3N’T F3LT L1K3 YOU H4T3D M3 4T 4LL" # @t_sterezi5111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_pout as terezi:
        # ShowWithAtl
        linear 0.20 xpos 0.6 
    extend "{w=0.2}{nw}"
    t_ch_terezi "NOT ONC3" # @t_sterezi5112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "1N 4LL TH3 T1M3S W3 W3R3 H4NG1NG OUT? >:P" # @t_sterezi5113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Well… maybe a little, but…" # @t_sterezi5114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " I think it might be something only an alien can feel." # @t_sterezi5114.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I don’t think it would be very healthy for me to have a “kismesis”..." # @t_sterezi5115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " I can’t even begin to imagine what it would mean to have a “hate romance” with someone!" # @t_sterezi5115.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Anyway… what does all this have to do with my katamari and Pyralspite?" # @t_sterezi5116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "1 SUPPOS3 1 M1GHT 4S W3LL JUST COM3 CL34N..." # @t_sterezi5117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "R3M3MB3R 1 TOLD YOU TH4T PYR4LSP1T3 D1S4PP34R3D ON TH3 V3RY S4M3 N1GHT YOU ROLL3D UP TH3 SCHOOL?" # @t_sterezi5118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "...Oh. I see." # @t_sterezi5119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "I accidentally rolled up Pyralspite too…" # @t_sterezi5120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And now he’s locked up in the principal’s office with my katamari." # @t_sterezi5120.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "Is that it?!" # @t_sterezi5121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_laugh as terezi
    t_ch_terezi "WOW! TH4T TOOK YOU FOR3V3R TO F1GUR3 OUT" # @t_sterezi5122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "YOU D3F1N1T3LY DON’T H4V3 COOL M1ND POW3RS L1K3 M3!" # @t_sterezi5123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "So that’s why you were interrogating me about Pyralspite…" # @t_sterezi5124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And why you wanted me to break my katamari out of the weapons vault." # @t_sterezi5124.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "But… why didn’t you just TELL me that in the first place?!" # @t_sterezi5125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend " Why did you have to play these weird games with me?!" # @t_sterezi5125.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "B3C4US3, COTTON C4NDY…" # @t_sterezi5126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_terezi "B31NG HON3ST 4ND OP3N 4BOUT YOUR F33L1NGS?" # @t_sterezi5127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_resigned as terezi
    t_ch_terezi "TH4T’S SOM3TH1NG YOU DO 1N 4 R3D ROM4NC3" # @t_sterezi5128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "BUT M4N1PUL4T1NG 4ND T3RR1FY1NG 4 P3RSON 1NTO DO1NG WH4T YOU W4NT…" # @t_sterezi5129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_grin as terezi
    t_ch_terezi "TH4T’S WH4T YOU DO 1N 4 BL4CK ROM4NC3 >:]" # @t_sterezi5130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Um." # @t_sterezi5131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I guess that’s…" # @t_sterezi5131.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    with Dissolve(.333)
    extend " Flattering?" # @t_sterezi5131.02 self.block='Last'
    play sound "sfx/pacman.ogg" loop
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 6 xpos 0.9 
    show i_cousin_energetic_surprise as cousin:
        # ShowWithAtl
        pause 2.1 
        linear 0.20 xpos 0.2 
    show i_terezi_default_huh as terezi:
        # ShowWithAtl
        pause 3.6 
        linear 0.20 xpos 0.5 
    $ renpy.pause(6.0, hard=True) # TimedPause
    stop sound
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "...Wow. I don’t think my normal advice applies here." # @t_sterezi5132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Pac-Man?!" # @t_sterezi5133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    extend " H-how long have you been standing there?!" # @t_sterezi5133.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_lean_huh as terezi
    t_ch_terezi "TH1S 1S 4 PR1V4T3 CONV3RS4T1ON!!!" # @t_sterezi5134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Maybe you kids… SHOULDN’T be true to yourselves." # @t_sterezi5135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Farewell!" # @t_sterezi5136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'allowInterrupt': 'false', 'auto': 'true', 'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_pacman_left as pacman:
        # ShowWithAtl
        linear 3 xpos 1.5 
    $ renpy.pause(3.0, hard=True) # TimedPause
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_terezi_default_grin as terezi
    t_ch_terezi "H3H3H3, H3 SM3LLS L1K3 L3MON T4RTS >:]" # @t_sterezi5137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(Hmm… what did Pac-Man mean by that?" # @t_sterezi5138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Does he mean… that I should forget what I’ve learned about normal romance…" # @t_sterezi5138.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "And embrace Terezi’s way of life…" # @t_sterezi5139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral_blush as cousin
    with Dissolve(.333)
    extend " For a love that crosses the boundaries of space?!" # @t_sterezi5139.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "...Er, a “hate”, that is." # @t_sterezi5140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "I have no idea what to do…" # @t_sterezi5141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " I’m not sure I’m ready for all this…)" # @t_sterezi5141.01 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_2P', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
    label s_terezi5__2P:
        # <NHSceneChange NHSceneChange {'name': '_2P', 'scene': 's_day5.5', 'kind': 'NHSceneChange'} ''>
        jump s_day5p5