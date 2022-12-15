style creditRoll:
    xalign 0.5
    color "#fff"
    background "#000"
    text_align 0.5


style creditRoll_h1 is creditRoll:
    size 60
    # line_leading 60
    bold False

style creditRoll_h2 is creditRoll:
    size 50
    # line_leading 50
    bold True

style creditRoll_h3 is creditRoll:
    size 30
    bold True
    # line_leading 40

style creditRoll_div is creditRoll:
    size 25

style creditRoll_andyou is creditRoll_div
style creditRoll_copyrights is creditRoll_div

transform creditRoll_image:
    xalign 0.5

transform creditRoll_scroll(dur):
    yalign 0.0
    linear (dur - 2.0) yalign 1.0

        
define credits_pacman = scaleBestFit("portrait/pacman/left.png", 400, 400)

screen credits_content():

    style_prefix "creditRoll"
    vbox:

        null height 20
        add "ui/logo_namcohigh.png" at creditRoll_image
        null height 20

        text "\nNAMCO BANDAI Games Inc. Presents" style_suffix "h2"
        text "\nIn Association With\nWhat Pumpkin Studios" style_suffix "h2"
        text "\nA ShiftyLook Game" style_suffix "h2"
        text "\nDeveloped by\nDate Nighto LLC" style_suffix "h2"
        text "\n“NAMCO HIGH”" style_suffix "h1"

        text "\nCreative Director & Original Concept" style_suffix "h3"
        text "Andrew Hussie" style_suffix "div"

        text "\nHead Writer" style_suffix "h3"
        text "Ananth Panagariya" style_suffix "div"

        text "\nWriters" style_suffix "h3"
        text "Brian Clevinger" style_suffix "div"
        text "Magnolia Porter" style_suffix "div"

        text "\nCharacter Artists" style_suffix "h3"
        text "Cousin, Taira ...... Yuko Ota" style_suffix "div"
        text "  " style_suffix "div"
        text "Valkyrie ...... Ashley Davis" style_suffix "div"
        text "Anti-Bravoman ...... Dax Gordine" style_suffix "div"
        text "Meowkie ...... Geneva Hodgson" style_suffix "div"
        text "Galaga ...... Rich Stevens" style_suffix "div" 
        text "Albatross, Richard Miller ...... Tessa Stone" style_suffix "div"
        text "Lolo, Jane Crocker ...... J.N. Wiedle" style_suffix "div"
        text "  " style_suffix "div"
        text "Terezi Pyrope ...... Alexandra Douglass" style_suffix "div"
        text "Blue Max ...... Audra Furuichi" style_suffix "div"
        text "Mr. Driller ...... Gigi D.G." style_suffix "div"
        text "Tomari ...... Der-Shing Helmer" style_suffix "div"
        text "Aki Matsuo ...... Tyson Hesse" style_suffix "div"
        text "Davespite, Donko ...... E.N." style_suffix "div"
        text "Hiromi ...... OMOCAT" style_suffix "div"
        text "Nidia ...... Noelle Stevenson" style_suffix "div"

        text "\nBackgrounds" style_suffix "h3"
        text "Lindsay Woods" style_suffix "div"

        text "\nUI Design" style_suffix "h3"
        text "Cat Sze" style_suffix "div"

        text "\nLead Developer" style_suffix "h3"
        text "Conrad Kreyling" style_suffix "div"

        text "\nAssociate Producer" style_suffix "h3"
        text "Ritsuko Aoyagi" style_suffix "div"

        text "\nCo-Producer" style_suffix "h3"
        text "George Rohac" style_suffix "div"

        text "\nProducer" style_suffix "h3"
        text "Rob Pereyda" style_suffix "div"

        text "\nExecutive Producer" style_suffix "h3"
        text "Yutaro Ikegaya" style_suffix "div"

        text "\nMUSIC" style_suffix "h2"
        text "\nScore" style_suffix "h3"
        text "Ryan Francis" style_suffix "div"

        text "\n“Namco High Credits Theme”" style_suffix "h3"
        hbox:
            xfill True
            null width 200
            vbox:
                xalign 0.5
                text "Composed by:" style_suffix "div" xalign 0.5
                text "Ryan Francis" style_suffix "div" xalign 0.5
            vbox:
                xalign 0.5
                text "Vocals by:" style_suffix "div" xalign 0.5
                text "Mary Thomas" style_suffix "div" xalign 0.5
            null width 200

        text "\nAll Other Songs Composed and Produced by" style_suffix "h3"
        text "Ryan Francis" style_suffix "div"

        text "\nSFX Editing" style_suffix "h3"
        text "George Rohac" style_suffix "div"
        text "Some sound effects acquired from SoundSnap.com" style_suffix "div"

        text "\nNAMCO HIGH Logo Design by" style_suffix "h3"
        text "Ananth Panagariya" style_suffix "div"

        text "\nTEAM\nDATE NIGHTO" style_suffix "h2"
        null height 20
        add "credits/dnlogo.png" at creditRoll_image
        null height 20


        hbox:
            xfill True
            null width 200
            vbox:
                xalign 0.5
                text "Founder,\nLead Developer" style_suffix "h3"
                text "Conrad Kreyling" style_suffix "div"
            vbox:
                xalign 0.5
                text "Co-Founder,\nLead Artist" style_suffix "h3"
                text "Lindsay Woods" style_suffix "div"
            null width 200
        

        text "\nProduction Intern" style_suffix "h3"
        text "Kasey Van Hise" style_suffix "div"

        text "\nScene Direction" style_suffix "h3"
        text "Kasey Van Hise" style_suffix "div"
        text "Conrad Kreyling" style_suffix "div"
        text "Yuko Ota" style_suffix "div"
        text "Ananth Panagariya" style_suffix "div"
        text "George Rohac" style_suffix "div"
        text "Lindsay Woods" style_suffix "div"

        text "\nQA & Testing" style_suffix "h3"
        text "Amanda Cosmos" style_suffix "div"
        text "Kasey Van Hise" style_suffix "div"
        text "Yuko Ota" style_suffix "div"
        text "Magnolia Porter" style_suffix "div"
        text "J.N. Wiedle" style_suffix "div"

        text "\nTEAM WHAT PUMPKIN STUDIOS" style_suffix "h2"
        text "Cindy Dominguez; Andrew Hussie;" style_suffix "div"
        text "Byron Hussie; George Rohac; Julian Dominguez" style_suffix "div"

        text "\nTEAM SHIFTY" style_suffix "h2"
        text "Shigetaka Kurita · Rob Pereyda · Yutaro Ikegaya" style_suffix "div"
        text "Cory Casoni · Ritsuko Aoyagi" style_suffix "div"
        text "Ash Paulsen · Kaori Ito" style_suffix "div"

        text "\nBACKEND BY MOOVE-IT" style_suffix "h2"
        null height 20
        add "credits/mooveit.png" at creditRoll_image
        null height 20

        # text "\n{s}Built Using{/s}\nPainstakingly converted from" style_suffix "h2"
        text "\nBuilt Using" style_suffix "h2"
        text "htmlVN, by Date Nighto" style_suffix "div"
        text "Ren'py" style_suffix "div"
        # text "'s undocumented proprietary format into" style_suffix "div"
        # text "Ren'py" style_suffix "h2"

        text "\nPRODUCTION BABIES" style_suffix "h2"
        text "Rook · Cricket" style_suffix "div"
        text "George Rohac" style_suffix "div"

        text "\nSPECIAL THANKS" style_suffix "h2"
        text "Shin Unozawa · Makoto Asanuma · Tomoaki" style_suffix "div"
        text "Katsuhiro Harada · Ken Nakadate" style_suffix "div"
        text "Guy Brand · Evan Rowe" style_suffix "div"
        text "Mark Hatcher · Makoto Tachibana" style_suffix "div"
        text "Esabelle Ryngin · Christine Love" style_suffix "div"
        text "Rebecca Robinson · My Brother, My Brother and Me" style_suffix "div"
        text "WeLoveFine · more communication" style_suffix "div"

        text "and YOU!" style_suffix "andyou"

        text "Homestuck, Davesprite, Jane Crocker,and Terezi Pyrope\n© 2013 Andrew Hussie." style_suffix "copyrights"

        text "NAMCO BANDAI Games, Namco, and ShiftyLook\nlogos ™& © 2013 NAMCO BANDAI Games Inc.\nNAMCO™ HIGH © 2013 NAMCO BANDAI Games Inc." style_suffix "copyrights"

        null height 20
        add "credits/shiftylook.png" at creditRoll_image
        null height 20

        text "\nDESKTOP PORT" style_suffix "h1"
        text "\n{color=#FD0}GiovanH{/color}" style_suffix "h2"
        text "love ya!" style_suffix "div"

        null height 780
        text "\nProduced by" style_suffix "h2"
        text "NAMCO BANDAI Games Inc." style_suffix "div"

        null height 780
        text "BE TRUE TO YOURSELF" style_suffix "h2"
        null height 20
        add credits_pacman at creditRoll_image

label _credits:
    play music "bgm/credits.ogg"
    call screen credits(_with_none=False) # disable implicit with_none to enable hide transition
    with dissolve # hide
    return

screen credits():

    tag menu
    default crawl_time = (2*60 + 43)
    
    # on "show" action Play("music", "bgm/namcotheme.ogg", loop=True)
    # on "replace" action [
    #     # Play("music", "sfx/pacman.ogg", loop=False),
    #     # Stop("music"),
    #     Play("music", "bgm/credits.ogg", loop=False),
    #     lambda: renpy.music.set_queue_empty_callback(Return(), channel="music"),
    # ]

    add Solid("#000")

    vbox:
        at creditRoll_scroll(crawl_time)

        null height 780
        use credits_content()

    # secret skip
    key "hide_windows" action [Stop("music"), Return()]
    # panik
    timer crawl_time action [Stop("music"), Return()]
    

screen credits_manual():

    tag menu


    window:
        background Solid("#000")
        viewport:
            scrollbars "vertical"
            mousewheel "vertical"
            draggable True
            vbox:
                use credits_content()

                textbutton "<==" action Return() style "namcohigh_button"
