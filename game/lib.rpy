
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
        print(image, th, mh, th/mh, tw, mw, tw/mw,  factor, mw*factor, mh*factor)
        return im.FactorScale(image, width=factor, height=factor)
    
    def AudioEvent(layer, volume, duration):
        c = renpy.audio.music.get_channel(layer)
        print("Sorry, can't do it.")

init python:

    class NamcoChar(ADVCharacter):
        def __call__(self, what, *args, **kwargs):
            print(self, what, kwargs)
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
                transformed_text = ("%s{size=-4}%s{/size}" % (text[0], text[1:])) if len(text) > 1 else text
                rv += renpy.text.textsupport.tokenize(transformed_text)
            else:
                rv.append((kind, text))
        return rv

    config.custom_text_tags["smallcaps"] = texttag_smallcaps
