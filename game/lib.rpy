
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
    
    def AudioEvent(layer, volume, duration):
        c = renpy.audio.music.get_channel(layer)
        print("Sorry, can't do it.")

init python:

    class NamcoChar(ADVCharacter):
        def __call__(self, what, *args, **kwargs):
            print(self, what, kwargs)
            super(NamcoChar, self).__call__(what, *args, **kwargs)

    
label BadEndMacro:
    $ throw NotImplementedError()
        # curtainactor == curtain (???)
        # imageevent actor badEnd with image i_event_badend 1sec fadein
        # imageevent actor badEndText with image i_event_badend_gameover 1sec fadein

        # bgm a_bgm_namcotheme then fadeout .5 secs

label BattleMacro:
    $ throw NotImplementedError()



    #     # Zoom in on evil namco
    #     self.children.append(ActorEvent("ActorEvent", attrs={
    #         "target": cousin_id,
    #         "duration": 0.5,
    #     }, children=[
    #         Styles("styles", attrs={"scaleX": scalex}),
    #         Transitions("transitions", attrs={"x": cousinx})
    #     ]))

    # pass

    # Thunderclap!
    # ease out

    # Fade in evil namco robots
    # evil linear move left

    # on thunderclaps:
    # Fade in partner, right top
    # Fade in cousin, right bottom

    # Move together, fade to white
    # Fade to black