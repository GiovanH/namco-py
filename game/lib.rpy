
transform default:
    # screw you
    xzoom 1.0
    yzoom 1.0
    xalign 0.5
    yalign 0.5

transform flip(duration=0.0, delay=0.0):
    pause delay
    xzoom 1.0
    linear duration xzoom -1.0

transform unflip(duration=0.0, delay=0.0):
    pause delay
    xzoom -1.0
    linear duration xzoom 1.0

define flash = vpunch 
define config.autoreload = False


init -1 python:

    def scaleBestFit(image, tw, th):
        """Returns a scaled version of a displayable, preserving the aspect ratio.
        Args:
            image (displayable): Input image
            tw (int): Maximum target height
            th (int): Maximum target width
        """
        mw, mh = im.image(image).load().get_size()
        mw, mh, tw, th = map(float, [mw, mh, tw, th])
        factor = min(tw / mw, th / mh)
        if factor != 1.0:
            print(image, th, mh, tw, mw, factor, mw*factor, mh*factor)
        return im.FactorScale(image, width=factor, height=factor)
    
    def AudioEvent(layer, volume, duration):
        c = renpy.audio.music.get_channel(layer)
        print("Sorry, can't do it.")

    def nhJsonSave(d):

        pick_count_names = ["amazona", "albatros", "antibravo", "bluemax", 
            "davesprite", "donko", "galaga", "hiromi", "jane", "lolo", "meowkie", 
            "mrdriller", "nidia", "richard", "taira", "terezi", "tomari", "valk"] 
        pick_count = {n: store.__dict__.get("slot_pick_count_" + n, 0) for n in pick_count_names}
        d['pick_count'] = pick_count

        main_char = max(pick_count, key=pick_count.get)
        if pick_count[main_char] == 0:
            main_char = slot_playerName
        main_char = main_char.title()
        d['main_char'] = main_char

        scenename = store.__dict__.get("slot_day_name")

        scenename = scenename.replace("s_", "")
        scenename = scenename.replace("day", "Day ")
        scenename = scenename.replace("p5", ".5")

        d['save_label'] = main_char + " " + scenename


define config.save_json_callbacks = [nhJsonSave]

image ctc_image:
    "gui/scrollbar/horizontal_hover_bar.png"
    xalign 0.5
    yalign 1.0

init python:

    class NamcoChar(ADVCharacter):
        def __init__(self, *args, **kwargs):
            kwargs['ctc'] = kwargs.get("ctc", "ctc_image")
            kwargs['ctc_position'] = kwargs.get("ctc_position", "fixed")
            super(NamcoChar, self).__init__(*args, **kwargs)

        def __call__(self, what, *args, **kwargs):
            super(NamcoChar, self).__call__(what, *args, **kwargs)
            # TODO break multiline statements into subcalls automatically

    def texttag_smallcaps(tag, argument, contents):
        """The text tag {quirk}. Handles most quirk behavior internally.
        Takes a single quirk argument, so syntax is {quirk=id}text{/quirk}
        Only applies one quirk, but can be wrapped recursively."""
        quirklist = [argument]

        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
            #     words = text.split(" ")
            #     words = [
            #         "%s{size=-4}%s{/size}" % (w[0], w[1:])
            #         if len(w) > 1
            #         else w
            #         for w in words
            #     ]
            #     transformed_text = " ".join(words)
                transformed_text = ("{size=+4}%s{/size}%s" % (text[0].upper(), text[1:].upper())) if len(text) > 1 else text.upper()
                rv += renpy.text.textsupport.tokenize(transformed_text)
            else:
                rv.append((kind, text))
        return rv

    config.custom_text_tags["smallcaps"] = texttag_smallcaps

    def unlockedAll():
        return all([
            persistent.got_trueend_amazona,
            persistent.got_trueend_albatros,
            persistent.got_trueend_antibravo,
            persistent.got_trueend_bluemax,
            persistent.got_trueend_davesprite,
            persistent.got_trueend_donko,
            persistent.got_trueend_galaga,
            persistent.got_trueend_hiromi,
            persistent.got_trueend_jane,
            persistent.got_trueend_lolo,
            persistent.got_trueend_meowkie,
            persistent.got_trueend_mrdriller,
            persistent.got_trueend_nidia,
            persistent.got_trueend_richard,
            persistent.got_trueend_taira,
            persistent.got_trueend_terezi,
            persistent.got_trueend_tomari,
            persistent.got_trueend_valk
        ])
