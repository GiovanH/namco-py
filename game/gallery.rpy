init python:

    def get_all_images():
        """Returns all the images in the global store."""
        return filter(
            lambda i: not isinstance(i[1], renpy.text.extras.ParameterizedText),
            renpy.display.image.images.items()
        )

    def addMyImages(g, target):
        my_prefix = "i_" + target
        print("for", target)
        for key, value in get_all_images():
            if key[0].startswith(my_prefix):
                print("adding", key, value)
                g.image(value)
            else:
                print("missing", key, value)



    # Step 1. Create the gallery object.
    g = Gallery()

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

    g.button("Bad End")
    g.condition("persistent.got_truend_badend")
    g.image("event/badend.jpg")
    g.image("event/badend_gameover.jpg")

    g.button("Bluemax")
    g.condition("persistent.got_trueend_bluemax")
    g.image("event/bluemax_ending.jpg")

    g.button("Cousin")
    g.condition("persistent.got_trueend_cousin")
    g.image("event/cousin_badend.jpg")

    g.button("Davesprite")
    g.condition("persistent.got_trueend_davesprite")
    g.image("event/davesprite_ending.jpg")
    g.image("event/davesprite_scene1.jpg")

    g.button("Donko")
    g.condition("persistent.got_trueend_donko")
    g.image("event/donko_ending.jpg")
    g.image("event/donko_scene3.jpg")

    g.button("Hiromi")
    g.condition("persistent.got_trueend_hiromi")
    g.image("event/hiromi_ending.jpg")
    g.image("event/hiromi_scene3.png")

    g.button("Jane")
    g.condition("persistent.got_trueend_jane")
    g.image("event/jane_ending.jpg")

    g.button("Lolo")
    g.condition("persistent.got_trueend_lolo")
    g.image("event/lolo_ending.jpg")
    g.image("event/lolo_yearbook.png")

    g.button("Meowkie")
    g.condition("persistent.got_trueend_meowkie")
    g.image("event/meowkie_ending.jpg")

    g.button("Richard")
    g.condition("persistent.got_trueend_miller")
    g.image("event/miller_ending.jpg")

    g.button("Mr Driller")
    g.condition("persistent.got_trueend_mrdriller")
    g.image("event/mrdriller_ending.jpg")

    g.button("Nidia")
    g.condition("persistent.got_trueend_nidia")
    g.image("event/nidia_ending.jpg")

    g.button("Taira")
    g.condition("persistent.got_trueend_taira")
    g.image("event/taira_ending.jpg")

    g.button("Terezi")
    g.condition("persistent.got_trueend_terezi")
    g.image("event/terezi_ending.jpg")
    g.image("event/terezi_scene3.jpg")

    g.button("Tomari")
    g.condition("persistent.got_trueend_tomari")
    g.image("event/tomari_ending.jpg")

    g.button("Valkyrie")
    g.condition("persistent.got_trueend_valkyrie")
    g.image("event/valkyrie_ending.jpg")

    g.button("Galaga")
    g.condition("persistent.got_trueend_galaga")
    g.image("portrait/galaga/default.jpg")

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

            textbutton "Amazona" action g.Action("Amazona") style "namcohigh_button"
            textbutton "Albatros" action g.Action("Albatros") style "namcohigh_button"
            textbutton "Antibravo" action g.Action("Antibravo") style "namcohigh_button"
            textbutton "Bluemax" action g.Action("Bluemax") style "namcohigh_button"
            textbutton "Davesprite" action g.Action("Davesprite") style "namcohigh_button"
            textbutton "Donko" action g.Action("Donko") style "namcohigh_button"
            textbutton "Galaga" action g.Action("Galaga") style "namcohigh_button"
            textbutton "Hiromi" action g.Action("Hiromi") style "namcohigh_button"
            textbutton "Jane" action g.Action("Jane") style "namcohigh_button"
            textbutton "Lolo" action g.Action("Lolo") style "namcohigh_button"
            textbutton "Meowkie" action g.Action("Meowkie") style "namcohigh_button"
            textbutton "Mr Driller" action g.Action("Mr Driller") style "namcohigh_button"
            textbutton "Nidia" action g.Action("Nidia") style "namcohigh_button"
            textbutton "Richard" action g.Action("Richard") style "namcohigh_button"
            textbutton "Taira" action g.Action("Taira") style "namcohigh_button"
            textbutton "Terezi" action g.Action("Terezi") style "namcohigh_button"
            textbutton "Tomari" action g.Action("Tomari") style "namcohigh_button"
            textbutton "Valkyrie" action g.Action("Valkyrie") style "namcohigh_button"
            textbutton "Bad End" action g.Action("Bad End") style "namcohigh_button"
            textbutton "Cousin" action g.Action("Cousin") style "namcohigh_button"
