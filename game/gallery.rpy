init 1000 python:

    def get_all_images():
        """Returns all the images in the global store."""
        return filter(
            lambda i: not isinstance(i[1], renpy.text.extras.ParameterizedText),
            renpy.display.image.images.items()
        )

    def addMyImages(g, target):
        for key, value in get_all_images():
            if key[0].startswith("i_battlepose_" + target):
                g.image(value)
        for key, value in get_all_images():
            if key[0].startswith("i_" + target):
                g.image(value)

    def letMeIn():
        persistent.got_trueend_amazona = True
        persistent.got_trueend_albatros = True
        persistent.got_trueend_antibravo = True
        persistent.got_trueend_bluemax = True
        persistent.got_trueend_davesprite = True
        persistent.got_trueend_donko = True
        persistent.got_trueend_galaga = True
        persistent.got_trueend_hiromi = True
        persistent.got_trueend_jane = True
        persistent.got_trueend_lolo = True
        persistent.got_trueend_meowkie = True
        persistent.got_trueend_mrdriller = True
        persistent.got_trueend_nidia = True
        persistent.got_trueend_richard = True
        persistent.got_trueend_taira = True
        persistent.got_trueend_terezi = True
        persistent.got_trueend_tomari = True
        persistent.got_trueend_valk = True
        persistent.got_trueend_badend = True

    # Step 1. Create the gallery object.
    g = Gallery()

    def galleryInit():
        g.button("Albatros")
        g.condition("persistent.got_trueend_albatros")
        g.image("event/albatross_ending.jpg")
        addMyImages(g, "albatros")

        g.button("Amazona")
        g.condition("persistent.got_trueend_amazona")
        g.image("event/amazona_ending.jpg")
        addMyImages(g, "amazona")

        g.button("Antibravo")
        g.condition("persistent.got_trueend_antibravo")
        g.image("event/antibravo_ending.jpg")
        addMyImages(g, "antibravo")

        g.button("Bad End")
        g.condition("persistent.got_trueend_badend")
        g.image("event/badend.jpg")
        g.image("event/badend_gameover.jpg")
        addMyImages(g, "robotarmy")

        g.button("Bluemax")
        g.condition("persistent.got_trueend_bluemax")
        g.image("event/bluemax_ending.jpg")
        addMyImages(g, "bluemax")

        g.button("Cousin")
        g.condition("persistent.got_trueend_cousin")
        g.image("event/cousin_badend.jpg")
        addMyImages(g, "cousin")

        g.button("Davesprite")
        g.condition("persistent.got_trueend_davesprite")
        g.image("event/davesprite_ending.jpg")
        g.image("event/davesprite_scene1.jpg")
        addMyImages(g, "davesprite")

        g.button("Donko")
        g.condition("persistent.got_trueend_donko")
        g.image("event/donko_ending.jpg")
        g.image("event/donko_scene3.jpg")
        addMyImages(g, "donko")

        g.button("Hiromi")
        g.condition("persistent.got_trueend_hiromi")
        g.image("event/hiromi_ending.jpg")
        g.image("event/hiromi_scene3.png")
        addMyImages(g, "hiromi")

        g.button("Jane")
        g.condition("persistent.got_trueend_jane")
        g.image("event/jane_ending.jpg")
        addMyImages(g, "jane")

        g.button("Lolo")
        g.condition("persistent.got_trueend_lolo")
        g.image("event/lolo_ending.jpg")
        g.image("event/lolo_yearbook.png")
        addMyImages(g, "lolo")

        g.button("Meowkie")
        g.condition("persistent.got_trueend_meowkie")
        g.image("event/meowkie_ending.jpg")
        addMyImages(g, "meowkie")

        g.button("Richard")
        g.condition("persistent.got_trueend_richard")
        g.image("event/miller_ending.jpg")
        addMyImages(g, "richard")

        g.button("Mr Driller")
        g.condition("persistent.got_trueend_mrdriller")
        g.image("event/mrdriller_ending.jpg")
        addMyImages(g, "mrdriller")

        g.button("Nidia")
        g.condition("persistent.got_trueend_nidia")
        g.image("event/nidia_ending.jpg")
        addMyImages(g, "nidia")

        g.button("Taira")
        g.condition("persistent.got_trueend_taira")
        g.image("event/taira_ending.jpg")
        addMyImages(g, "taira")

        g.button("Terezi")
        g.condition("persistent.got_trueend_terezi")
        g.image("event/terezi_ending.jpg")
        g.image("event/terezi_scene3.jpg")
        addMyImages(g, "terezi")

        g.button("Tomari")
        g.condition("persistent.got_trueend_tomari")
        g.image("event/tomari_ending.jpg")
        addMyImages(g, "tomari")

        g.button("Valkyrie")
        g.condition("persistent.got_trueend_valk")
        g.image("event/valkyrie_ending.jpg")
        addMyImages(g, "valk")

        g.button("Galaga")
        g.condition("persistent.got_trueend_galaga")
        addMyImages(g, "galaga")

        g.button("Backgrounds")
        g.condition("unlockedAll()")
        addMyImages(g, "bg_")


    galleryInit()

init offset = 2

screen gallery:
    tag menu
    use game_menu("Gallery"):
        vpgrid:
            xfill True
            yfill True
            cols 2
            xalign 0.5
            yalign 0.5
            spacing 4
            style_prefix "gallery"

            for name in [
                "Albatros", "Antibravo", "Bluemax", "Davesprite", "Donko", "Galaga", 
                "Hiromi", "Jane", "Lolo", "Meowkie", "Mr Driller", "Nidia", "Richard", 
                "Taira", "Terezi", "Tomari", "Valkyrie", "Bad End", "Cousin", "Backgrounds"
            ]:                
                textbutton name action g.Action(name) style "namcohigh_button"

# Override
screen _gallery:
    frame:
        xfill True
        yfill True
        padding (0, 0, 0, 0)
        background Solid("#222")

        key "viewport_leftarrow" action gallery.Previous()
        key "viewport_rightarrow" action gallery.Next()

        if locked:
            add "#000"
            text _("Image [index] of [count] locked.") align (0.5, 0.5)
        else:
            viewport:
                draggable True
                for d in displayables:
                    add d align (0.5, 0.5)

        if gallery.slideshow:
            timer gallery.slideshow_delay action Return("next") repeat True

        key "game_menu" action gallery.Return()

        use gallery_navigation

screen gallery_navigation:
    vbox:
        yalign 1.0
        xalign 0.0

        style_group "gallery"
        # align (.98, .98)

        if quick_menu:
            textbutton _("prev") action gallery.Previous(unlocked=gallery.unlocked_advance)
            textbutton _("next") action gallery.Next(unlocked=gallery.unlocked_advance)
            textbutton _("slideshow") action gallery.ToggleSlideshow()
            textbutton _("return") action gallery.Return()


