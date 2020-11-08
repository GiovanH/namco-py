# <Scene {'id': 's_taira1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
label s_taira1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_taira1"
    $ renpy.pause(1)
    # <Scene {'id': 's_taira1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance'} scene ''>
    # Pass (assets)
    # <Events {} events ''>
    # <ParallelEvent {'auto': 'true', 'name': '_0'} ParallelEvent ''>
    # <Events {} events ''>
    play music "bgm/upbeat_half.ogg" loop
    show i_bg_quad_bleachers as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_taira_akimbo_happy as taira zorder 2:
        default
        xpos 0.3 
        xzoom 1.0 
    show i_cousin_default_neutral as cousin zorder 2:
        default
        xpos 0.7 
        xzoom -1.0 

    # <ParallelEvent {'name': '_1'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "(Somehow, Taira dragged me into this Wrestleball thing." # @t_staira115.00 self.block='Last'
    # <ParallelEvent {'name': '_2'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "To be honest, I’m not that crazy about sports..." # @t_staira116.00 self.block='Last'
    # <ParallelEvent {'name': '_3'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Unless rolling up stuff is a sport." # @t_staira116.01 self.block='Last'
    # <ParallelEvent {'name': '_4'} ParallelEvent ''>
    # <Events {} events ''>
    extend " Which I’m pretty sure it isn’t." # @t_staira116.02 self.block='Last'
    # <ParallelEvent {'name': '_5'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "Anyway, at least it’ll get me out of having to sit in detention for a while.)" # @t_staira117.00 self.block='Last'
    # <ParallelEvent {'name': '_6'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_happy as taira
    t_ch_taira "Yo [slot_playerName]! I’m so PUMPED that you joined the team!" # @t_staira118.00 self.block='Last'
    # <ParallelEvent {'name': '_7'} ParallelEvent ''>
    # <Events {} events ''>
    extend " We needed a new Ninja Player for the left field." # @t_staira118.01 self.block='Last'
    # <ParallelEvent {'name': '_8'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "“Ninja” player?" # @t_staira119.00 self.block='Last'
    # <ParallelEvent {'name': '_9'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " What kind of game is this, anyway?" # @t_staira119.01 self.block='Last'
    # <ParallelEvent {'name': '_A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Never played Wrestleball?!" # @t_staira120.00 self.block='Last'
    # <ParallelEvent {'name': '_B'} ParallelEvent ''>
    # <Events {} events ''>
    extend " The game they call..." # @t_staira120.01 self.block='Last'
    # <ParallelEvent {'name': '_C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_angry as taira
    t_ch_taira "“the sport of only the coolest toughest RAD POWER-WARRIORS?!”" # @t_staira121.00 self.block='Last'
    # <ParallelEvent {'name': '_D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "(Do “they” call it that, or is it just him?)" # @t_staira122.00 self.block='Last'
    # <ParallelEvent {'name': '_E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "What are you, some kinda dumb baby?" # @t_staira123.00 self.block='Last'
    # <ParallelEvent {'name': '_F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_happy as taira
    extend " Did you move here from Baby Town?!" # @t_staira123.01 self.block='Last'
    # <ParallelEvent {'name': '_G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " HAW!" # @t_staira123.02 self.block='Last'
    # <ParallelEvent {'name': '_H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "Yes, Taira." # @t_staira124.00 self.block='Last'
    # <ParallelEvent {'name': '_I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " I moved here from Baby Town." # @t_staira124.01 self.block='Last'
    # <ParallelEvent {'name': '_J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "Well, don’t worry buddy." # @t_staira125.00 self.block='Last'
    # <ParallelEvent {'name': '_K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_happy as taira
    t_ch_taira "I’ll explain Wrestleball to you." # @t_staira126.00 self.block='Last'
    # <ParallelEvent {'auto': 'true', 'name': '_L'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Two teams of roughly a dozen players square off the goal of moving the ball into the endzone, either with a power kick or by running with it. Obviously power kicks are WAY more rad. Anyway- the game begins with a scramble and the ball is dropped at the center between five of the starting players from each side. Offensive and defensive players can use any number of wrestling moves to get the ball from the other team and usually have a signature style that earns extra points. The players can obstruct or knock out opponents when trying to get the ball. That’s the basics but it gets tricky when you start to factor in the ninja and wing players whose function is to blah blah blah blah blah blah blah blah....{/cps}" # @t_staira127.00 self.block='Last'
    # <ParallelEvent {'name': '_M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}(Okay, he’s not REALLY saying “blah blah blah.”{/cps}" # @t_staira128.00 self.block='Last'
    # <ParallelEvent {'name': '_N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    extend " {cps=*1.67}That’s kinda all I can hear at this point though.{/cps}" # @t_staira128.01 self.block='Last'
    # <ParallelEvent {'name': '_O'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I really, really don’t get sports...{/cps}" # @t_staira129.00 self.block='Last'
    # <ParallelEvent {'name': '_P'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}The rules for this one seem even more complicated than usual.{/cps}" # @t_staira129.01 self.block='Last'
    # <ParallelEvent {'name': '_Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Still, if Taira can actually understand all this?{/cps}" # @t_staira130.00 self.block='Last'
    # <ParallelEvent {'name': '_R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "{cps=*1.67}Maybe he’s not such a dumb meathead after all.){/cps}" # @t_staira131.00 self.block='Last'
    # <ParallelEvent {'name': '_S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}...and kicked goals are worth double but only when the ball is in a powerzone and handled by a non-defensive player.{/cps}" # @t_staira132.00 self.block='Last'
    # <ParallelEvent {'name': '_T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "{cps=*1.67}YO, THAT’S WHY WRESTLEBALL TOTALLY RUUUULES!{/cps}" # @t_staira133.00 self.block='Last'
    # <ParallelEvent {'name': '_U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Uh huh....{/cps}" # @t_staira134.00 self.block='Last'
    # <ParallelEvent {'name': '_V'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}So now that I’ve explained Wrestleball to you...{/cps}" # @t_staira135.00 self.block='Last'
    # <ParallelEvent {'name': '_W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}It’s totally your favorite thing in the whole world FOREVER, right?!{/cps}" # @t_staira135.01 self.block='Last'
    # <ParallelEvent {'name': '_X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Er...{/cps}" # @t_staira136.00 self.block='Last'
    # <ParallelEvent {'name': '_Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}What am I saying.{/cps}" # @t_staira137.00 self.block='Last'
    # <ParallelEvent {'name': '_Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_happy as taira
    extend " {cps=*1.67}How could anyone NOT love Wrestleball?!{/cps}" # @t_staira137.01 self.block='Last'
    # <ParallelEvent {'name': '_a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}I guess I’m just feelin’ nervous or something,{/cps}" # @t_staira138.00 self.block='Last'
    # <ParallelEvent {'name': '_b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}since it’s my favorite thing and...{/cps}" # @t_staira138.01 self.block='Last'
    # <ParallelEvent {'name': '_c'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_happy_blush as taira
    with Dissolve(0.5)
    extend " {cps=*1.67}it’d be really cool if you liked it too.{/cps}" # @t_staira138.02 self.block='Last'
    # <ParallelEvent {'name': '_d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}Uh... y-yeah, totally, Taira.{/cps}" # @t_staira139.00 self.block='Last'
    # <ParallelEvent {'name': '_e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}It’s my favorite thing, um, forever.{/cps}" # @t_staira139.01 self.block='Last'
    # <ParallelEvent {'name': '_f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " {cps=*1.67}And all those other things you said.{/cps}" # @t_staira139.02 self.block='Last'
    # <ParallelEvent {'name': '_g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "{cps=*1.67}[slot_playerName]...{/cps}" # @t_staira140.00 self.block='Last'
    # <ParallelEvent {'name': '_h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Hearing that...{/cps}" # @t_staira140.01 self.block='Last'
    # <ParallelEvent {'name': '_i'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Makes me...{/cps}" # @t_staira140.02 self.block='Last'
    # <ParallelEvent {'name': '_j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "{cps=*1.67}TOTALLY PUMPED!{/cps}" # @t_staira141.00 self.block='Last'
    # <ParallelEvent {'name': '_k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}YEAAAHHHH!!!! NAMCO HIGH WRESTLEBALL SQUAD FOREVER!!!!{/cps}" # @t_staira141.01 self.block='Last'
    # <ParallelEvent {'name': '_l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Haha...{/cps}" # @t_staira142.00 self.block='Last'
    # <ParallelEvent {'name': '_m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}What can I say?{/cps}" # @t_staira142.01 self.block='Last'
    # <ParallelEvent {'name': '_n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Your enthusiasm is kinda infectious...{/cps}" # @t_staira143.00 self.block='Last'
    # <ParallelEvent {'name': '_o'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_serious as taira
    t_ch_taira "{cps=*1.67}[slot_playerName]! Listen to me.{/cps}" # @t_staira144.00 self.block='Last'
    # <ParallelEvent {'name': '_p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I’m gonna be real with you now, okay?{/cps}" # @t_staira144.01 self.block='Last'
    # <ParallelEvent {'name': '_q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    extend " {cps=*1.67}Real. Talk.{/cps}" # @t_staira144.02 self.block='Last'
    # <ParallelEvent {'name': '_r'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira:
        # ShowWithAtl
        linear 0.333 xpos 0.45 
    show i_cousin_default_neutral as cousin
    extend "{w=0.333}{nw}"
    t_ch_cousin "{cps=*1.67}(He’s grabbing my hands....){/cps}" # @t_staira145.00 self.block='Last'
    # <ParallelEvent {'name': '_s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Okay...{/cps}" # @t_staira146.00 self.block='Last'
    # <ParallelEvent {'name': '_t'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Even though you’re tiny and small...{/cps}" # @t_staira147.00 self.block='Last'
    # <ParallelEvent {'name': '_u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Like a little baby bird with hollow bones...{/cps}" # @t_staira147.01 self.block='Last'
    # <ParallelEvent {'name': '_v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}All delicate and small and unable to defend yourself...{/cps}" # @t_staira148.00 self.block='Last'
    # <ParallelEvent {'name': '_w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Because you’re a wimpy nerd who never played sports before and you probably lived in your mom’s basement or something....{/cps}" # @t_staira148.01 self.block='Last'
    # <ParallelEvent {'name': '_x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "{cps=*1.67}What?! I’m not that bad.{/cps}" # @t_staira149.00 self.block='Last'
    # <ParallelEvent {'name': '_y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Am I?{/cps}" # @t_staira149.01 self.block='Last'
    # <ParallelEvent {'name': '_z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}And even though the other Wrestleball team is full of huge guys...{/cps}" # @t_staira150.00 self.block='Last'
    # <ParallelEvent {'name': '_10'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Guys who will absolutely crush you in one second...{/cps}" # @t_staira150.01 self.block='Last'
    # <ParallelEvent {'name': '_11'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "{cps=*1.67}I promise I’ll protect you!{/cps}" # @t_staira151.00 self.block='Last'
    # <ParallelEvent {'name': '_12'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "{cps=*1.67}(Wh... What have I gotten myself into...){/cps}" # @t_staira152.00 self.block='Last'
    # <ParallelEvent {'name': '_13'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira:
        # ShowWithAtl
        linear 0.333 xpos 0.3 
    stop music fadeout 1.0
    play sound "sfx/arenacrowd.ogg" loop
    extend "{w=0.333}{nw}"
    t_ch_taira "{cps=*1.67}Alright! GET PSYCHED!{/cps}" # @t_staira153.00 self.block='Last'
    # <ParallelEvent {'name': '_14'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_happy as taira
    t_ch_cousin "{cps=*1.67}(The ref’s coming out onto the field...{/cps}" # @t_staira154.00 self.block='Last'
    # <ParallelEvent {'name': '_15'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}And there’s the other team.{/cps}" # @t_staira154.01 self.block='Last'
    # <ParallelEvent {'name': '_16'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "{cps=*1.67}Yikes, he wasn’t kidding!{/cps}" # @t_staira155.00 self.block='Last'
    # <ParallelEvent {'name': '_17'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I’m even a little scared of OUR team.{/cps}" # @t_staira155.01 self.block='Last'
    # <ParallelEvent {'name': '_18'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}They’re all huge.{/cps}" # @t_staira155.02 self.block='Last'
    # <ParallelEvent {'name': '_19'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Still...{/cps}" # @t_staira156.00 self.block='Last'
    # <ParallelEvent {'name': '_1A'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}Taira is way bigger than any of them.{/cps}" # @t_staira157.00 self.block='Last'
    # <ParallelEvent {'name': '_1B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I have to admit, I feel safe knowing he’s on my side.){/cps}" # @t_staira158.00 self.block='Last'
    # <ParallelEvent {'name': '_1C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mc_ref as mc zorder 2:
        default
        xpos 0.5 
        alpha 0.0
        linear 0.5 alpha 1.0
    show i_cousin_default_neutral as cousin:
        # ShowWithAtl
        ease 0.333 xpos 0.8 
    show i_taira_default_happy as taira:
        # ShowWithAtl
        ease 0.333 xpos 0.2 
    extend "{w=0.5}{nw}"
    t_ch_referee "{cps=*1.67}WRESTLEBALL TEAMS!{/cps}" # @t_staira159.00 self.block='Last'
    # <ParallelEvent {'name': '_1D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_referee "{cps=*1.67}Namco High versus....{/cps}" # @t_staira160.00 self.block='Last'
    # <ParallelEvent {'name': '_1E'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_referee "{cps=*1.67}EVIL Namco High!{/cps}" # @t_staira161.00 self.block='Last'
    # <ParallelEvent {'name': '_1F'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_referee "{cps=*1.67}5... 4... 3... 2...{/cps}" # @t_staira162.00 self.block='Last'
    # <ParallelEvent {'name': '_1G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_referee "{cps=*1.67}SCRAMBLE!{/cps}" # @t_staira163.00 self.block='Last'
    # <ParallelEvent {'name': '_1H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mc_ref as mc:
        # ShowWithAtl
        linear .333 alpha 0.0
    show i_taira_steveholt_angry as taira
    extend "{w=0.333}{nw}"
    t_ch_taira "{cps=*1.67}YEAAAHHH!{/cps}" # @t_staira164.00 self.block='Last'
    # <ParallelEvent {'name': '_1I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.5 
    show i_taira_steveholt_angry as taira:
        # ShowWithAtl
        linear .333 alpha 0.0
    extend "{w=0.333}{nw}"
    t_ch_cousin "{cps=*1.67}(Whoah! Everyone’s running out onto the field at once!{/cps}" # @t_staira165.00 self.block='Last'
    # <ParallelEvent {'name': '_1J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I can’t even see where the ball is...{/cps}" # @t_staira165.01 self.block='Last'
    # <ParallelEvent {'name': '_1K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "{cps=*1.67}Augh! That guy almost stepped on my head!{/cps}" # @t_staira166.00 self.block='Last'
    # <ParallelEvent {'name': '_1L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I think he was even on MY team!{/cps}" # @t_staira166.01 self.block='Last'
    # <ParallelEvent {'name': '_1M'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Okay, what am I supposed to do again?{/cps}" # @t_staira166.02 self.block='Last'
    # <ParallelEvent {'name': '_1N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Taira said something about... power kicks...{/cps}" # @t_staira167.00 self.block='Last'
    # <ParallelEvent {'name': '_1O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}And... end zones??{/cps}" # @t_staira167.01 self.block='Last'
    # <ParallelEvent {'name': '_1P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    t_ch_cousin "{cps=*1.67}What does any of that even mean?{/cps}" # @t_staira168.00 self.block='Last'
    # <ParallelEvent {'name': '_1Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}What am I supposed to do?{/cps}" # @t_staira169.00 self.block='Last'
    # <ParallelEvent {'name': '_1R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "{cps=*1.67}AUGH! WHAT’S THAT COMING TOWARD ME!{/cps}" # @t_staira170.00 self.block='Last'
    # <ParallelEvent {'name': '_1S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I CAN’T WATCH!){/cps}" # @t_staira170.01 self.block='Last'
    # <ParallelEvent {'name': '_1T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}(...Huh?{/cps}" # @t_staira171.00 self.block='Last'
    # <ParallelEvent {'name': '_1U'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I... I did it?{/cps}" # @t_staira171.01 self.block='Last'
    # <ParallelEvent {'name': '_1V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I caught the ball!{/cps}" # @t_staira171.02 self.block='Last'
    # <ParallelEvent {'name': '_1W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_grin as cousin
    t_ch_cousin "{cps=*1.67}I CAUGHT THE BALL!{/cps}" # @t_staira172.00 self.block='Last'
    # <ParallelEvent {'name': '_1X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_laugh as cousin
    extend " {cps=*1.67}YEAH!{/cps}" # @t_staira172.01 self.block='Last'
    # <ParallelEvent {'name': '_1Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Wait a minute...{/cps}" # @t_staira173.00 self.block='Last'
    # <ParallelEvent {'name': '_1Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    extend " {cps=*1.67}Didn’t Taira say...{/cps}" # @t_staira173.01 self.block='Last'
    # <ParallelEvent {'name': '_1a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}That players are allowed to use...{/cps}" # @t_staira174.00 self.block='Last'
    # <ParallelEvent {'name': '_1b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin
    extend " {cps=*1.67}Wrestling moves...{/cps}" # @t_staira174.01 self.block='Last'
    # <ParallelEvent {'name': '_1c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}To get the ball away from the other team?{/cps}" # @t_staira174.02 self.block='Last'
    # <ParallelEvent {'name': '_1d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}That explains why all those big guys are coming towards me...{/cps}" # @t_staira175.00 self.block='Last'
    # <ParallelEvent {'name': '_1e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Oh, no.){/cps}" # @t_staira176.00 self.block='Last'
    # <ParallelEvent {'name': '_1f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "{cps=*1.67}[slot_playerName]!{/cps}" # @t_staira177.00 self.block='Last'
    # <ParallelEvent {'name': '_1g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_mortified as cousin:
        # ShowWithAtl
        linear 0.333 xpos 0.7 
    show i_taira_akimbo_serious as taira:
        # ShowWithAtl
        linear .333 alpha 1.0
    extend "{w=0.333}{nw}"
    extend " {cps=*1.67}[slot_playerName]!{/cps}" # @t_staira177.01 self.block='Last'
    # <ParallelEvent {'name': '_1h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Yoooo, are you alright?{/cps}" # @t_staira178.00 self.block='Last'
    # <ParallelEvent {'name': '_1i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I...{/cps}" # @t_staira179.00 self.block='Last'
    # <ParallelEvent {'name': '_1j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I...{/cps}" # @t_staira179.01 self.block='Last'
    # <ParallelEvent {'name': '_1k'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "{cps=*1.67}I can’t feel my antenna....{/cps}" # @t_staira180.00 self.block='Last'
    # <ParallelEvent {'name': '_1l'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_angry as taira
    t_ch_taira "{cps=*1.67}[slot_playerName]!{/cps}" # @t_staira181.00 self.block='Last'
    # <ParallelEvent {'name': '_1m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}NOOOOOOOOOOOO!{/cps}" # @t_staira181.01 self.block='Last'
    # <ParallelEvent {'name': '_1n'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}I WILL...{/cps}" # @t_staira182.00 self.block='Last'
    # <ParallelEvent {'name': '_1o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}HAVE....{/cps}" # @t_staira183.00 self.block='Last'
    # <ParallelEvent {'name': '_1p'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_revenge as taira
    t_ch_taira "{cps=*1.67}MY REVENGE!!{/cps}" # @t_staira184.00 self.block='Last'
    # <ParallelEvent {'name': '_1q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_grin as cousin
    t_ch_cousin "{cps=*1.67}Haha, I was just messin’ with ya, bro.{/cps}" # @t_staira185.00 self.block='Last'
    # <ParallelEvent {'name': '_1r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I’m fine-{/cps}" # @t_staira186.00 self.block='Last'
    # <ParallelEvent {'name': '_1s'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_revenge as taira
    t_ch_taira "{cps=*1.67}REVENNNNNNNGE!!!{/cps}" # @t_staira187.00 self.block='Last'
    # <ParallelEvent {'name': '_1t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "{cps=*1.67}AUGH!{/cps}" # @t_staira188.00 self.block='Last'
    # <ParallelEvent {'name': '_1u'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}(It’s like he’s in some kind of...{/cps}" # @t_staira189.00 self.block='Last'
    # <ParallelEvent {'name': '_1v'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Rage-trance!{/cps}" # @t_staira189.01 self.block='Last'
    # <ParallelEvent {'name': '_1w'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_revenge as taira:
        # ShowWithAtl
        linear .333 alpha 0.0
    show i_cousin_default_surprised as cousin:
        # ShowWithAtl
        linear .333 xpos 0.5 
    extend "{w=0.333}{nw}"
    t_ch_cousin "{cps=*1.67}There he goes running off, before I could say any more...{/cps}" # @t_staira190.00 self.block='Last'
    # <ParallelEvent {'name': '_1x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Oh gosh! He’s slamming into all the other players!{/cps}" # @t_staira191.00 self.block='Last'
    # <ParallelEvent {'name': '_1y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}He’s taking them out one by one!{/cps}" # @t_staira192.00 self.block='Last'
    # <ParallelEvent {'name': '_1z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Urk!{/cps}" # @t_staira193.00 self.block='Last'
    # <ParallelEvent {'name': '_20'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Augh!{/cps}" # @t_staira193.01 self.block='Last'
    # <ParallelEvent {'name': '_21'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " {cps=*1.67}I can’t watch!{/cps}" # @t_staira193.02 self.block='Last'
    # <ParallelEvent {'name': '_22'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}This can’t be legal...){/cps}" # @t_staira194.00 self.block='Last'
    # <ParallelEvent {'name': '_23'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}REVENNNNNNGE!{/cps}" # @t_staira195.00 self.block='Last'
    # <ParallelEvent {'name': '_24'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}FOR [slot_playerName]!{/cps}" # @t_staira195.01 self.block='Last'
    # <ParallelEvent {'name': '_25'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}AND FOR MY CLANNNN!!{/cps}" # @t_staira196.00 self.block='Last'
    # <ParallelEvent {'name': '_26'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}(Clan? What Clan?{/cps}" # @t_staira197.00 self.block='Last'
    # <ParallelEvent {'name': '_27'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Does he mean his team?{/cps}" # @t_staira198.00 self.block='Last'
    # <ParallelEvent {'name': '_28'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}But he’s knocking his own teammates out too...{/cps}" # @t_staira198.01 self.block='Last'
    # <ParallelEvent {'name': '_29'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Maybe there’s more going on with him than I realized.){/cps}" # @t_staira199.00 self.block='Last'
    # <ParallelEvent {'name': '_2A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}YEAHHH!! REVENGE!!{/cps}" # @t_staira1100.00 self.block='Last'
    # <ParallelEvent {'name': '_2B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}(Something horrible must’ve happened to him...{/cps}" # @t_staira1101.00 self.block='Last'
    # <ParallelEvent {'name': '_2C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}If he can be driven into blind rages like this.{/cps}" # @t_staira1101.01 self.block='Last'
    # <ParallelEvent {'name': '_2D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}...Although I can’t help but notice...{/cps}" # @t_staira1102.00 self.block='Last'
    # <ParallelEvent {'name': '_2E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " {cps=*1.67}He’s still making sure to score all the goals, even in his “blind rage.”){/cps}" # @t_staira1102.01 self.block='Last'
    # <ParallelEvent {'name': '_2F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_mc_ref as mc:
        # ShowWithAtl
        linear 0.5 xpos 0.25 
        # ShowWithAtl
        linear 0.5 alpha 1.0
    show i_cousin_exhausted_neutral as cousin:
        # ShowWithAtl
        ease_expo .5 xpos 0.7 
    extend "{w=0.5}{nw}"
    t_ch_referee "{cps=*1.67}TIME!{/cps}" # @t_staira1103.00 self.block='Last'
    # <ParallelEvent {'name': '_2G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}THIS WRESTLEBALL MATCH IS OVER!{/cps}" # @t_staira1103.01 self.block='Last'
    # <ParallelEvent {'name': '_2H'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_referee "{cps=*1.67}TAIRA NO KAGEKIYO WINS SINGLEHANDEDLY-{/cps}" # @t_staira1104.00 self.block='Last'
    # <ParallelEvent {'name': '_2I'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}AND IN RECORD-BREAKING TIME!{/cps}" # @t_staira1104.01 self.block='Last'
    # <ParallelEvent {'name': '_2J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_referee "{cps=*1.67}GOOD GAME, EVERYONE!{/cps}" # @t_staira1105.00 self.block='Last'
    # <ParallelEvent {'name': '_2K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_happy as taira
    extend " {cps=*1.67}WELL, MOSTLY JUST TAIRA.{/cps}" # @t_staira1105.01 self.block='Last'
    show i_mc_ref as mc:
        # ShowWithAtl
        linear .5 alpha 0.0
    # <ParallelEvent {'name': '_2M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin:
        # ShowWithAtl
        linear .333 xpos 0.7 
    show i_taira_akimbo_happy as taira:
        # ShowWithAtl
        linear .333 alpha 1.0
    extend "{w=0.333}{nw}"
    t_ch_taira "{cps=*1.67}YEAH!{/cps}" # @t_staira1106.00 self.block='Last'
    # <ParallelEvent {'name': '_2N'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}HAW HAW HAW HAW!{/cps}" # @t_staira1106.01 self.block='Last'
    # <ParallelEvent {'name': '_2O'} ParallelEvent ''>
    # <Events {} events ''>
    stop sound
    t_ch_taira "{cps=*1.67}REVENGE RULES!{/cps}" # @t_staira1107.00 self.block='Last'
    # <ParallelEvent {'name': '_2P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    t_ch_cousin "{cps=*1.67}...I really do not understand sports.{/cps}" # @t_staira1108.00 self.block='Last'
    # <ParallelEvent {'name': '_2Q'} ParallelEvent ''>
    # <Events {} events ''>
    $ AudioEvent('music', 1.0, 1.0)
    t_ch_cousin "{cps=*1.67}Well, at least the match is over early...{/cps}" # @t_staira1109.00 self.block='Last'
    # <ParallelEvent {'name': '_2R'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}HEY [slot_playerName]!{/cps}" # @t_staira1110.00 self.block='Last'
    # <ParallelEvent {'name': '_2S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Didja see me?{/cps}" # @t_staira1111.00 self.block='Last'
    # <ParallelEvent {'name': '_2T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_happy as taira
    extend " {cps=*1.67}Didja see me get revenge for you?{/cps}" # @t_staira1111.01 self.block='Last'
    # <ParallelEvent {'allowInterrupt': 'false', 'name': '_2U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    $ renpy.pause(0) # Image change
    show i_taira_akimbo_happy as taira:
        # ShowWithAtl
        pause 0.5 
        ease_expo .5 xpos 0.5 
    extend "{w=1.0}{nw}"
    t_ch_taira "{cps=*1.67}I did good, didn’t I? HAW!{/cps}" # @t_staira1112.00 self.block='Last'
    # <ParallelEvent {'name': '_2V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "{cps=*1.67}TAIRA!{/cps}" # @t_staira1113.00 self.block='Last'
    # <ParallelEvent {'name': '_2W'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Stop squeezing me so hard!{/cps}" # @t_staira1113.01 self.block='Last'
    # <ParallelEvent {'name': '_2X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_mortified as cousin
    extend " {cps=*1.67}I got hurt in the match, remember?!{/cps}" # @t_staira1113.02 self.block='Last'
    # <ParallelEvent {'name': '_2Y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_happy as taira:
        # ShowWithAtl
        ease_expo .5 xpos 0.3 
    extend "{w=0.5}{nw}"
    t_ch_taira "{cps=*1.67}Whoah! Oops!{/cps}" # @t_staira1114.00 self.block='Last'
    # <ParallelEvent {'name': '_2Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Sorry, Cuz!{/cps}" # @t_staira1114.01 self.block='Last'
    # <ParallelEvent {'name': '_2a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I forgot how, like, gentle and delicate you are.{/cps}" # @t_staira1114.02 self.block='Last'
    # <ParallelEvent {'name': '_2b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_sad as cousin
    t_ch_cousin "{cps=*1.67}There you go again with that “delicate” stuff...{/cps}" # @t_staira1115.00 self.block='Last'
    # <ParallelEvent {'name': '_2c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}But that’s not important right now.{/cps}" # @t_staira1116.00 self.block='Last'
    # <ParallelEvent {'name': '_2d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}You saw me, right? During the game?{/cps}" # @t_staira1117.00 self.block='Last'
    # <ParallelEvent {'name': '_2e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}You noticed, didn’t you?{/cps}" # @t_staira1117.01 self.block='Last'
    # <ParallelEvent {'name': '_2f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}Uh... noticed what?{/cps}" # @t_staira1118.00 self.block='Last'
    # <ParallelEvent {'name': '_2g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "{cps=*1.67}My muscles!{/cps}" # @t_staira1119.00 self.block='Last'
    # <ParallelEvent {'name': '_2h'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}While I was avenging my clan and stuff back there!{/cps}" # @t_staira1119.01 self.block='Last'
    # <ParallelEvent {'name': '_2i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Yo, they looked hot, right?!{/cps}" # @t_staira1120.00 self.block='Last'
    # <ParallelEvent {'name': '_2j'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Don’t deny it, [slot_playerName]!{/cps}" # @t_staira1121.00 self.block='Last'
    # <ParallelEvent {'name': '_2k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Unless you wanna look like an IDIOT! Haw haw!{/cps}" # @t_staira1121.01 self.block='Last'
    # <ParallelEvent {'name': '_2l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}…{/cps}" # @t_staira1122.00 self.block='Last'
    # <ParallelEvent {'name': '_2m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    with Dissolve(0.5)
    t_ch_cousin "{cps=*1.67}I don’t have to answer that!{/cps}" # @t_staira1123.00 self.block='Last'
    # <ParallelEvent {'name': '_2n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_happy as taira
    t_ch_taira "{cps=*1.67}Aw yeah!{/cps}" # @t_staira1124.00 self.block='Last'
    # <ParallelEvent {'name': '_2o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}You totally noticed!{/cps}" # @t_staira1124.01 self.block='Last'
    # <ParallelEvent {'name': '_2p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I knew you would!{/cps}" # @t_staira1124.02 self.block='Last'
    # <ParallelEvent {'name': '_2q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "{cps=*1.67}...Hey!{/cps}" # @t_staira1125.00 self.block='Last'
    # <ParallelEvent {'name': '_2r'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Wait just a minute!{/cps}" # @t_staira1125.01 self.block='Last'
    # <ParallelEvent {'name': '_2s'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}You mean all that revenge stuff...{/cps}" # @t_staira1126.00 self.block='Last'
    # <ParallelEvent {'name': '_2t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "{cps=*1.67}That was just an act?!{/cps}" # @t_staira1127.00 self.block='Last'
    # <ParallelEvent {'name': '_2u'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "{cps=*1.67}Huh?{/cps}" # @t_staira1128.00 self.block='Last'
    # <ParallelEvent {'name': '_2v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}All that stuff about caring about me...{/cps}" # @t_staira1129.00 self.block='Last'
    # <ParallelEvent {'name': '_2w'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}About getting revenge for me being hurt...{/cps}" # @t_staira1129.01 self.block='Last'
    # <ParallelEvent {'name': '_2x'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}That was all just...{/cps}" # @t_staira1130.00 self.block='Last'
    # <ParallelEvent {'name': '_2y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}A ruse?!{/cps}" # @t_staira1131.00 self.block='Last'
    # <ParallelEvent {'name': '_2z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}So you could show off your, your...{/cps}" # @t_staira1131.01 self.block='Last'
    # <ParallelEvent {'name': '_30'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_angry as cousin
    t_ch_cousin "{cps=*1.67}Your stupid, stupid, attractive body?!{/cps}" # @t_staira1132.00 self.block='Last'
    # <ParallelEvent {'name': '_31'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_angry as taira
    t_ch_taira "{cps=*1.67}Whoah whoah WHOAH!{/cps}" # @t_staira1133.00 self.block='Last'
    # <ParallelEvent {'name': '_32'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}No WAY!{/cps}" # @t_staira1133.01 self.block='Last'
    # <ParallelEvent {'name': '_33'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Of course I cared!{/cps}" # @t_staira1134.00 self.block='Last'
    # <ParallelEvent {'name': '_34'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused as taira
    t_ch_taira "{cps=*1.67}To think of you getting hurt like that...{/cps}" # @t_staira1135.00 self.block='Last'
    # <ParallelEvent {'name': '_35'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}It’s just not cool, yo!{/cps}" # @t_staira1135.01 self.block='Last'
    # <ParallelEvent {'name': '_36'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}It’s like, totally the not coolest thing ever!{/cps}" # @t_staira1135.02 self.block='Last'
    # <ParallelEvent {'name': '_37'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_neutral as cousin
    t_ch_cousin "{cps=*1.67}…{/cps}" # @t_staira1136.00 self.block='Last'
    # <ParallelEvent {'name': '_38'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Once I saw you get knocked out...{/cps}" # @t_staira1137.00 self.block='Last'
    # <ParallelEvent {'name': '_39'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_angry as taira
    t_ch_taira "{cps=*1.67}I had to get revenge!{/cps}" # @t_staira1138.00 self.block='Last'
    # <ParallelEvent {'name': '_3A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}For you, and for my clan!{/cps}" # @t_staira1138.01 self.block='Last'
    # <ParallelEvent {'name': '_3B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}(There’s that stuff about “my clan” again...{/cps}" # @t_staira1139.00 self.block='Last'
    # <ParallelEvent {'name': '_3C'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I’d better not ask.{/cps}" # @t_staira1139.01 self.block='Last'
    # <ParallelEvent {'name': '_3D'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Sounds like it might be a touchy subject.){/cps}" # @t_staira1139.02 self.block='Last'
    # <ParallelEvent {'name': '_3E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_pleading as taira
    t_ch_taira "{cps=*1.67}Please, [slot_playerName]!{/cps}" # @t_staira1140.00 self.block='Last'
    # <ParallelEvent {'name': '_3F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}If you thought I didn’t care...{/cps}" # @t_staira1140.01 self.block='Last'
    # <ParallelEvent {'name': '_3G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}That’d be SUCH a bummer.{/cps}" # @t_staira1140.02 self.block='Last'
    # <ParallelEvent {'name': '_3H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "{cps=*1.67}Okay, okay...{/cps}" # @t_staira1141.00 self.block='Last'
    # <ParallelEvent {'name': '_3I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Besides... I could never fake revenge!{/cps}" # @t_staira1142.00 self.block='Last'
    # <ParallelEvent {'name': '_3J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Revenge is like...{/cps}" # @t_staira1142.01 self.block='Last'
    # <ParallelEvent {'name': '_3K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    extend " {cps=*1.67}My thing!{/cps}" # @t_staira1142.02 self.block='Last'
    # <ParallelEvent {'name': '_3L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}It’s my passion!{/cps}" # @t_staira1142.03 self.block='Last'
    # <ParallelEvent {'name': '_3M'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}I try super hard to incorporate revenge into every part of my life!{/cps}" # @t_staira1143.00 self.block='Last'
    # <ParallelEvent {'name': '_3N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}(Sounds unhealthy.{/cps}" # @t_staira1144.00 self.block='Last'
    # <ParallelEvent {'name': '_3O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}But, at least he knows what he likes, I guess?){/cps}" # @t_staira1144.01 self.block='Last'
    # <ParallelEvent {'name': '_3P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}And... just because I’m getting revenge...{/cps}" # @t_staira1145.00 self.block='Last'
    # <ParallelEvent {'name': '_3Q'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Doesn’t mean I don’t want you to think I look hot.{/cps}" # @t_staira1146.00 self.block='Last'
    # <ParallelEvent {'name': '_3R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused as taira
    t_ch_taira "{cps=*1.67}Because if you think I look hot...{/cps}" # @t_staira1147.00 self.block='Last'
    # <ParallelEvent {'name': '_3S'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Maybe...{/cps}" # @t_staira1147.01 self.block='Last'
    # <ParallelEvent {'name': '_3T'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused_blush as taira
    with Dissolve(0.5)
    t_ch_taira "{cps=*1.67}You might want to date me.{/cps}" # @t_staira1148.00 self.block='Last'
    # <ParallelEvent {'name': '_3U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised_blush as cousin
    t_ch_cousin "{cps=*1.67}...Wow.{/cps}" # @t_staira1149.00 self.block='Last'
    # <ParallelEvent {'name': '_3V'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}(Okay, keep it together, [slot_playerName].){/cps}" # @t_staira1149.01 self.block='Last'
    # <ParallelEvent {'name': '_3W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral_blush as cousin
    t_ch_cousin "{cps=*1.67}Taira...{/cps}" # @t_staira1150.00 self.block='Last'
    # <ParallelEvent {'name': '_3X'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}That’s really sweet.{/cps}" # @t_staira1150.01 self.block='Last'
    # <ParallelEvent {'name': '_3Y'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}And, you’re a nice guy and all...{/cps}" # @t_staira1150.02 self.block='Last'
    # <ParallelEvent {'name': '_3Z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_serious_blush as taira
    t_ch_taira "{cps=*1.67}Yeah?!{/cps}" # @t_staira1151.00 self.block='Last'
    # <ParallelEvent {'name': '_3a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I’m just not sure you’re...{/cps}" # @t_staira1152.00 self.block='Last'
    # <ParallelEvent {'name': '_3b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    extend " {cps=*1.67}Really my type, is all.{/cps}" # @t_staira1152.01 self.block='Last'
    # <ParallelEvent {'name': '_3c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I’m sorry.{/cps}" # @t_staira1153.00 self.block='Last'
    # <ParallelEvent {'name': '_3d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}But...{/cps}" # @t_staira1154.00 self.block='Last'
    # <ParallelEvent {'name': '_3e'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I don’t get it.{/cps}" # @t_staira1154.01 self.block='Last'
    # <ParallelEvent {'name': '_3f'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}You said I have a cool face and hot muscles.{/cps}" # @t_staira1154.02 self.block='Last'
    # <ParallelEvent {'name': '_3g'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}Yeah, but there’s more to it than that!{/cps}" # @t_staira1155.00 self.block='Last'
    # <ParallelEvent {'name': '_3h'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}We don’t have much in common, do we?{/cps}" # @t_staira1156.00 self.block='Last'
    # <ParallelEvent {'name': '_3i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_angry as taira
    t_ch_taira "{cps=*1.67}Uh, DUH?!{/cps}" # @t_staira1157.00 self.block='Last'
    # <ParallelEvent {'name': '_3j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}We totally do!{/cps}" # @t_staira1157.01 self.block='Last'
    # <ParallelEvent {'name': '_3k'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}That’s, um, news to me.{/cps}" # @t_staira1158.00 self.block='Last'
    # <ParallelEvent {'name': '_3l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Yeah!{/cps}" # @t_staira1159.00 self.block='Last'
    # <ParallelEvent {'name': '_3m'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}You already said you love Wrestleball so much, that it’s your favorite thing forever!{/cps}" # @t_staira1159.01 self.block='Last'
    # <ParallelEvent {'name': '_3n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "{cps=*1.67}..Uh... huh...{/cps}" # @t_staira1160.00 self.block='Last'
    # <ParallelEvent {'name': '_3o'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I did say that... Didn’t I...{/cps}" # @t_staira1160.01 self.block='Last'
    # <ParallelEvent {'name': '_3p'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Well, you’re not gonna believe this, but...{/cps}" # @t_staira1161.00 self.block='Last'
    # <ParallelEvent {'name': '_3q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "{cps=*1.67}That’s EXACTLY how I feel about Wrestleball, too!{/cps}" # @t_staira1162.00 self.block='Last'
    # <ParallelEvent {'name': '_3r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}You...{/cps}" # @t_staira1163.00 self.block='Last'
    # <ParallelEvent {'name': '_3s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Don’t say...{/cps}" # @t_staira1163.01 self.block='Last'
    # <ParallelEvent {'name': '_3t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "{cps=*1.67}And let’s see.{/cps}" # @t_staira1164.00 self.block='Last'
    # <ParallelEvent {'name': '_3u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}What else?{/cps}" # @t_staira1164.01 self.block='Last'
    # <ParallelEvent {'name': '_3v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}OH! I know!{/cps}" # @t_staira1165.00 self.block='Last'
    # <ParallelEvent {'name': '_3w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Do you like...{/cps}" # @t_staira1166.00 self.block='Last'
    # <ParallelEvent {'name': '_3x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_angry as taira
    extend " {cps=*1.67}Revenge?{/cps}" # @t_staira1166.01 self.block='Last'
    # <ParallelEvent {'name': '_3y'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}Oh. Well.{/cps}" # @t_staira1167.00 self.block='Last'
    # <ParallelEvent {'name': '_3z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I haven’t really thought about it before.{/cps}" # @t_staira1167.01 self.block='Last'
    # <ParallelEvent {'name': '_40'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I guess if someone did something bad to me...{/cps}" # @t_staira1168.00 self.block='Last'
    # <ParallelEvent {'name': '_41'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I’d probably want to get revenge for it.{/cps}" # @t_staira1169.00 self.block='Last'
    # <ParallelEvent {'name': '_42'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "{cps=*1.67}See?!{/cps}" # @t_staira1170.00 self.block='Last'
    # <ParallelEvent {'name': '_43'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}We totally get each other!{/cps}" # @t_staira1170.01 self.block='Last'
    # <ParallelEvent {'name': '_44'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}But on the other hand...{/cps}" # @t_staira1171.00 self.block='Last'
    # <ParallelEvent {'name': '_45'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "{cps=*1.67}In stories and stuff, revenge always seems so empty, you know?{/cps}" # @t_staira1172.00 self.block='Last'
    # <ParallelEvent {'name': '_46'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}The person who got revenge never really feels satisfied...{/cps}" # @t_staira1172.01 self.block='Last'
    # <ParallelEvent {'name': '_47'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Sometimes they even ruin their lives trying to get it.{/cps}" # @t_staira1172.02 self.block='Last'
    # <ParallelEvent {'name': '_48'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Doesn’t really seem like the best idea, does it?{/cps}" # @t_staira1173.00 self.block='Last'
    # <ParallelEvent {'name': '_49'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_angry as taira
    t_ch_taira "{cps=*1.67}Whaaaa?!{/cps}" # @t_staira1174.00 self.block='Last'
    # <ParallelEvent {'name': '_4A'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Basically...{/cps}" # @t_staira1175.00 self.block='Last'
    # <ParallelEvent {'name': '_4B'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}It’s kind of a moral gray area.{/cps}" # @t_staira1176.00 self.block='Last'
    # <ParallelEvent {'name': '_4C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused as taira
    t_ch_taira "{cps=*1.67}…{/cps}" # @t_staira1177.00 self.block='Last'
    # <ParallelEvent {'name': '_4D'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}…{/cps}" # @t_staira1178.00 self.block='Last'
    # <ParallelEvent {'name': '_4E'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_serious as taira
    t_ch_taira "{cps=*1.67}Does that mean you like revenge?{/cps}" # @t_staira1179.00 self.block='Last'
    # <ParallelEvent {'name': '_4F'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "{cps=*1.67}(SIGH.){/cps}" # @t_staira1180.00 self.block='Last'
    # <ParallelEvent {'name': '_4G'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Sure, Taira.{/cps}" # @t_staira1181.00 self.block='Last'
    # <ParallelEvent {'name': '_4H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    extend " {cps=*1.67}I like revenge.{/cps}" # @t_staira1181.01 self.block='Last'
    # <ParallelEvent {'name': '_4I'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "{cps=*1.67}YES! HAW HAW!{/cps}" # @t_staira1182.00 self.block='Last'
    # <ParallelEvent {'name': '_4J'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I knew it!{/cps}" # @t_staira1182.01 self.block='Last'
    # <ParallelEvent {'name': '_4K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_energetic_surprise as cousin
    t_ch_cousin "{cps=*1.67}W-wait!{/cps}" # @t_staira1183.00 self.block='Last'
    # <ParallelEvent {'name': '_4L'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Don’t get too excited.{/cps}" # @t_staira1183.01 self.block='Last'
    # <ParallelEvent {'name': '_4M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    extend " {cps=*1.67}That doesn’t mean I-{/cps}" # @t_staira1183.02 self.block='Last'
    # <ParallelEvent {'name': '_4N'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}YO! That’s two out of three...{/cps}" # @t_staira1184.00 self.block='Last'
    # <ParallelEvent {'name': '_4O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Of my top favorite awesomest interests!{/cps}" # @t_staira1184.01 self.block='Last'
    # <ParallelEvent {'name': '_4P'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "{cps=*1.67}[slot_playerName]!{/cps}" # @t_staira1185.00 self.block='Last'
    # <ParallelEvent {'name': '_4Q'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Here it is!{/cps}" # @t_staira1185.01 self.block='Last'
    # <ParallelEvent {'name': '_4R'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Let’s go for a threefer!{/cps}" # @t_staira1185.02 self.block='Last'
    # <ParallelEvent {'name': '_4S'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Do you...{/cps}" # @t_staira1186.00 self.block='Last'
    # <ParallelEvent {'name': '_4T'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Like...{/cps}" # @t_staira1187.00 self.block='Last'
    # <ParallelEvent {'name': '_4U'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_angry as taira
    t_ch_taira "{cps=*1.67}to EAT FOOD?!{/cps}" # @t_staira1188.00 self.block='Last'
    # <ParallelEvent {'name': '_4V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "{cps=*1.67}Of...{/cps}" # @t_staira1189.00 self.block='Last'
    # <ParallelEvent {'name': '_4W'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    extend " {cps=*1.67}Course I do?{/cps}" # @t_staira1189.01 self.block='Last'
    # <ParallelEvent {'name': '_4X'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}…{/cps}" # @t_staira1190.00 self.block='Last'
    # <ParallelEvent {'name': '_4Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}…{/cps}" # @t_staira1191.00 self.block='Last'
    # <ParallelEvent {'name': '_4Z'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}…{/cps}" # @t_staira1192.00 self.block='Last'
    # <ParallelEvent {'name': '_4a'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}(He’s... just standing there.{/cps}" # @t_staira1193.00 self.block='Last'
    # <ParallelEvent {'name': '_4b'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Did I upset him?){/cps}" # @t_staira1193.01 self.block='Last'
    # <ParallelEvent {'name': '_4c'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}…{/cps}" # @t_staira1194.00 self.block='Last'
    # <ParallelEvent {'name': '_4d'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}…{/cps}" # @t_staira1195.00 self.block='Last'
    # <ParallelEvent {'name': '_4e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}…{/cps}" # @t_staira1196.00 self.block='Last'
    # <ParallelEvent {'name': '_4f'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Uh...{/cps}" # @t_staira1197.00 self.block='Last'
    # <ParallelEvent {'name': '_4g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Taira...?{/cps}" # @t_staira1197.01 self.block='Last'
    # <ParallelEvent {'name': '_4h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "{cps=*1.67}YEAH!!!{/cps}" # @t_staira1198.00 self.block='Last'
    # <ParallelEvent {'name': '_4i'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "{cps=*1.67}GAH!{/cps}" # @t_staira1199.00 self.block='Last'
    # <ParallelEvent {'name': '_4j'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_serious as taira
    t_ch_taira "{cps=*1.67}For thousands of years,{/cps}" # @t_staira1200.00 self.block='Last'
    # <ParallelEvent {'name': '_4k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I have walked this cruel earth alone.{/cps}" # @t_staira1200.01 self.block='Last'
    # <ParallelEvent {'name': '_4l'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}A vengeful spirit of war,{/cps}" # @t_staira1200.02 self.block='Last'
    # <ParallelEvent {'name': '_4m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "{cps=*1.67}With my pure, fighting heart beating flames in my tireless chest.{/cps}" # @t_staira1201.00 self.block='Last'
    # <ParallelEvent {'name': '_4n'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}Um....{/cps}" # @t_staira1202.00 self.block='Last'
    # <ParallelEvent {'name': '_4o'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}But a powerful fighting heart...{/cps}" # @t_staira1203.00 self.block='Last'
    # <ParallelEvent {'name': '_4p'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Needs a soul of beauty and grace at its side.{/cps}" # @t_staira1203.01 self.block='Last'
    # <ParallelEvent {'name': '_4q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious_blush as taira
    with Dissolve(0.5)
    t_ch_taira "{cps=*1.67}Beauty, grace, and mutual awesome interests and hobbies.{/cps}" # @t_staira1204.00 self.block='Last'
    # <ParallelEvent {'name': '_4r'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}A gentle soul to protect...{/cps}" # @t_staira1205.00 self.block='Last'
    # <ParallelEvent {'name': '_4s'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}And give purpose to the fighting heart’s toil.{/cps}" # @t_staira1205.01 self.block='Last'
    # <ParallelEvent {'name': '_4t'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_angry as taira
    t_ch_taira "{cps=*1.67}I, TAIRA NO KAGEKIYO,{/cps}" # @t_staira1206.00 self.block='Last'
    # <ParallelEvent {'name': '_4u'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}have been awaiting the day I meet...{/cps}" # @t_staira1206.01 self.block='Last'
    # <ParallelEvent {'name': '_4v'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}A beautiful, delicate, tiny, gentle, frail soul.{/cps}" # @t_staira1207.00 self.block='Last'
    # <ParallelEvent {'name': '_4w'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Like a single, trembling sakura petal in the palm of a warrior’s hand.{/cps}" # @t_staira1208.00 self.block='Last'
    # <ParallelEvent {'name': '_4x'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "{cps=*1.67}Sakura petal?! Do I really seem like that much of a wimp?!{/cps}" # @t_staira1209.00 self.block='Last'
    # <ParallelEvent {'name': '_4y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}The fighting heart...{/cps}" # @t_staira1210.00 self.block='Last'
    # <ParallelEvent {'name': '_4z'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    extend " {cps=*1.67}Must guard and protect the delicate soul!{/cps}" # @t_staira1210.01 self.block='Last'
    # <ParallelEvent {'name': '_50'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Keep it safe from the dangers of this cruel world!{/cps}" # @t_staira1210.02 self.block='Last'
    # <ParallelEvent {'name': '_51'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused_blush as taira
    t_ch_taira "{cps=*1.67}And also maybe...{/cps}" # @t_staira1211.00 self.block='Last'
    # <ParallelEvent {'name': '_52'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_angry as taira
    t_ch_taira "{cps=*1.67}TAKE IT ON A DATE!{/cps}" # @t_staira1212.00 self.block='Last'
    # <ParallelEvent {'name': '_53'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "{cps=*1.67}Wow.{/cps}" # @t_staira1213.00 self.block='Last'
    # <ParallelEvent {'name': '_54'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I guess this is happening.{/cps}" # @t_staira1213.01 self.block='Last'
    # <ParallelEvent {'name': '_55'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "{cps=*1.67}What do you say, [slot_playerName]?{/cps}" # @t_staira1214.00 self.block='Last'
    # <ParallelEvent {'name': '_56'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Do you want to date...{/cps}" # @t_staira1214.01 self.block='Last'
    # <ParallelEvent {'name': '_57'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_angry as taira
    t_ch_taira "{cps=*1.67}An awesome, fighting soul like me?!{/cps}" # @t_staira1215.00 self.block='Last'
    # <ParallelEvent {'name': '_58'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I guess it’s not impossible, but don’t hold your breath{/cps}" # @t_staira1215.00a self.block='Last'
    # <ParallelEvent {'name': '_59'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_happy as taira
    t_ch_taira "{cps=*1.67}HAW! Joke’s on you!{/cps}" # @t_staira1216.00 self.block='Last'
    # <ParallelEvent {'name': '_5A'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I never hold my breath! I’m undead.{/cps}" # @t_staira1216.01 self.block='Last'
    # <ParallelEvent {'name': '_5B'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}My hot bod and food-eating is gonna win you over, I bet!{/cps}" # @t_staira1217.00 self.block='Last'
    # <ParallelEvent {'name': '_5C'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "{cps=*1.67}Haha... whatever you say, buddy.{/cps}" # @t_staira1218.00 self.block='Last'
    # <ParallelEvent {'name': '_5D'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    with Dissolve(0.5)
    t_ch_cousin "{cps=*1.67}(It is a pretty hot bod...{/cps}" # @t_staira1219.00 self.block='Last'
    # <ParallelEvent {'name': '_5E'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}But I don’t have to admit that!{/cps}" # @t_staira1219.01 self.block='Last'
    # <ParallelEvent {'name': '_5F'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Wait, why does he eat food if he’s undead?{/cps}" # @t_staira1219.02 self.block='Last'
    # <ParallelEvent {'name': '_5G'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Oh, whatever.){/cps}" # @t_staira1219.03 self.block='Last'
    # <ParallelEvent {'name': '_5H'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "{cps=*1.67}Well, Taira, it’s been fun.{/cps}" # @t_staira1244.00 self.block='Last'
    # <ParallelEvent {'name': '_5I'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}(You know what? It actually has.){/cps}" # @t_staira1245.00 self.block='Last'
    # <ParallelEvent {'name': '_5J'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I’m gonna go home now though...{/cps}" # @t_staira1246.00 self.block='Last'
    # <ParallelEvent {'name': '_5K'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_mortified as cousin
    extend " {cps=*1.67}I definitely need an icepack after today.{/cps}" # @t_staira1246.01 self.block='Last'
    # <ParallelEvent {'name': '_5L'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_serious as taira
    t_ch_taira "{cps=*1.67}[slot_playerName]! Wait!{/cps}" # @t_staira1247.00 self.block='Last'
    # <ParallelEvent {'name': '_5M'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "{cps=*1.67}…?{/cps}" # @t_staira1248.00 self.block='Last'
    # <ParallelEvent {'name': '_5N'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_confused as taira
    t_ch_taira "{cps=*1.67}Look, not to get all emotional or nothin’...{/cps}" # @t_staira1249.00 self.block='Last'
    # <ParallelEvent {'name': '_5O'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}I just wanted to say...{/cps}" # @t_staira1249.01 self.block='Last'
    # <ParallelEvent {'name': '_5P'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Even though you’re a puny nerd...{/cps}" # @t_staira1250.00 self.block='Last'
    # <ParallelEvent {'name': '_5Q'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_confused as taira
    extend " {cps=*1.67}Like, seriously, the puniest I’ve ever seen, probably...{/cps}" # @t_staira1250.01 self.block='Last'
    # <ParallelEvent {'name': '_5R'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_default_serious as taira
    extend " {cps=*1.67}And even though you suck at Wrestleball...{/cps}" # @t_staira1250.02 self.block='Last'
    # <ParallelEvent {'name': '_5S'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_akimbo_happy as taira
    t_ch_taira "{cps=*1.67}You should TOTALLY keep doing it!{/cps}" # @t_staira1251.00 self.block='Last'
    # <ParallelEvent {'name': '_5T'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Everybody should get to do the stuff they love to do!{/cps}" # @t_staira1251.01 self.block='Last'
    # <ParallelEvent {'name': '_5U'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}Even if they suck at it!{/cps}" # @t_staira1252.00 self.block='Last'
    # <ParallelEvent {'name': '_5V'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_happy as taira
    extend " {cps=*1.67}In fact, it’s kinda even MORE hardcore that way!{/cps}" # @t_staira1252.01 self.block='Last'
    # <ParallelEvent {'name': '_5W'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_taira "{cps=*1.67}And if anyone tells you different...{/cps}" # @t_staira1253.00 self.block='Last'
    # <ParallelEvent {'name': '_5X'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_revenge_angry as taira
    t_ch_taira "{cps=*1.67}I’ll get revenge for you and PULVERIZE ‘EM!!!{/cps}" # @t_staira1254.00 self.block='Last'
    # <ParallelEvent {'name': '_5Y'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}(I don’t have the heart to tell him I don’t really like Wrestleball.{/cps}" # @t_staira1255.00 self.block='Last'
    # <ParallelEvent {'name': '_5Z'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}But that’s not really the point, is it?{/cps}" # @t_staira1255.01 self.block='Last'
    # <ParallelEvent {'name': '_5a'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}He’s right... except maybe about the pulverizing part){/cps}" # @t_staira1255.02 self.block='Last'
    # <ParallelEvent {'name': '_5b'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_laugh as cousin
    t_ch_cousin "{cps=*1.67}Thank you, Taira!{/cps}" # @t_staira1256.00 self.block='Last'
    # <ParallelEvent {'name': '_5c'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}That was really cool of you to say.{/cps}" # @t_staira1256.01 self.block='Last'
    # <ParallelEvent {'name': '_5d'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin as cousin
    extend " {cps=*1.67}Let’s both keep trying our best, okay?{/cps}" # @t_staira1256.02 self.block='Last'
    # <ParallelEvent {'name': '_5e'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}Especially if we suck at it!{/cps}" # @t_staira1257.00 self.block='Last'
    # <ParallelEvent {'name': '_5f'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira
    t_ch_taira "{cps=*1.67}YEAH! WOO!{/cps}" # @t_staira1258.00 self.block='Last'
    # <ParallelEvent {'name': '_5g'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}TRYING OUR BEST RUUUULES!{/cps}" # @t_staira1258.01 self.block='Last'
    # <ParallelEvent {'name': '_5h'} ParallelEvent ''>
    # <Events {} events ''>
    show i_taira_steveholt_happy as taira:
        # ShowWithAtl
        linear .333 alpha 0.0
    show i_cousin_default_grin as cousin:
        # ShowWithAtl
        linear .333 xpos 0.5 
    extend "{w=0.333}{nw}"
    t_ch_taira "{cps=*1.67}SEE YOU TOMORROW, [slot_playerName]!{/cps}" # @t_staira1259.00 self.block='Last'
    # <ParallelEvent {'name': '_5i'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}(That guy...{/cps}" # @t_staira1260.00 self.block='Last'
    # <ParallelEvent {'name': '_5j'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}It’s kinda cute how excited he gets.{/cps}" # @t_staira1260.01 self.block='Last'
    # <ParallelEvent {'name': '_5k'} ParallelEvent ''>
    # <Events {} events ''>
    extend " {cps=*1.67}Like a big dog or something.{/cps}" # @t_staira1260.02 self.block='Last'
    # <ParallelEvent {'name': '_5l'} ParallelEvent ''>
    # <Events {} events ''>
    t_ch_cousin "{cps=*1.67}I guess he’s not so bad...{/cps}" # @t_staira1261.00 self.block='Last'
    # <ParallelEvent {'name': '_5m'} ParallelEvent ''>
    # <Events {} events ''>
    show i_cousin_default_grin_blush as cousin
    with Dissolve(0.5)
    t_ch_cousin "{cps=*1.67}For a meathead.){/cps}" # @t_staira1262.00 self.block='Last'
    # <NHSceneChange {'name': '_5n', 'scene': 's_day2'} NHSceneChange ''>
    label s_taira1__5n:
        # <NHSceneChange {'name': '_5n', 'scene': 's_day2'} NHSceneChange ''>
        jump s_day2