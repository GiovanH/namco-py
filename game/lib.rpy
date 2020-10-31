
transform default:
    # screw you
    xzoom 1.0
    yzoom 1.0
    xalign 0.5
    yalign 0.5

transform flip(duration=0.0, delay=0.0):
    xzoom 1.0
    ease duration xzoom -1.0

transform unflip(duration=0.0, delay=0.0):
    xzoom -1.0
    ease duration xzoom 1.0

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