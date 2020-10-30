
# transform default:
#     xanchor 0.5
#     yanchor 1.0
#     xalign 0.5
#     yalign 1.0

transform flip(duration=0.0, delay=0.0):
    xzoom 1.0
    ease duration xzoom -1.0

transform unflip(duration=0.0, delay=0.0):
    xzoom -1.0
    ease duration xzoom 1.0
