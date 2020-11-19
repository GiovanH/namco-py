# <Scene scene {'id': 's_supersecret', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_supersecret:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_supersecret"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_supersecret', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
    label s_supersecret_initialize:
        # <ParallelEvent ParallelEvent {'auto': 'true', 'name': 'initialize', 'kind': 'ParallelEvent'} ''>
        # <Events events {'kind': 'events'} ''>
        show i_sw_black as curtain zorder 15:
            default
            alpha 0.0
        show i_pacman_left as pacman zorder 2:
            default
            xpos 0.7 
            alpha 0.0
        show i_digdug_right as digdug zorder 2:
            default
            alpha 0.0
            xpos 0.3 

    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "It's been 3 weeks since [slot_playerName] rescued you and Evil Namco High was reduced to burning rubble." # @t_ssupersecret0.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Yes." # @t_ssupersecret1.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "That leaves the question of what to do with the students of Evil Namco High. Who will teach them? Who will keep them in line?" # @t_ssupersecret2.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_digdug "Who... will give them detention?" # @t_ssupersecret3.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman ".............." # @t_ssupersecret4.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_pacman "Be true to yourself............." # @t_ssupersecret5.00 self.block='Last'
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 5 alpha 1.0
    return