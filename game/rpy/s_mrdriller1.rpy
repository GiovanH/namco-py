# <Scene scene {'id': 's_mrdriller1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
label s_mrdriller1:
    scene i_sw_black with dissolve
    stop music fadeout 1.0
    $ slot_day_name = "s_mrdriller1"
    $ renpy.pause(1) # buffer
    # <Scene scene {'id': 's_mrdriller1', 'xsi:schemaLocation': 'http://datenighto.com/schemas/htmlvn/0.1 ./htmlvn.xsd', 'xmlns': 'http://datenighto.com/schemas/htmlvn/0.1', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'kind': 'scene'} ''>
    # Pass (assets)
    # <Events events {'kind': 'events'} ''>
    # <ParallelEvent ParallelEvent {'name': '_0', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play music "bgm/upbeat_half.ogg" loop
    show i_bg_quad_bleachers as bg zorder 0 at default
    show i_sw_black as curtain zorder 15:
        default
        alpha 0.0
    show i_cousin_default_neutral as cousin zorder 4:
        default
        xpos 0.25 
    show i_mrdriller_drillup_happy as mrdriller zorder 2:
        default
        xpos 0.73 
    show i_mrdriller_standing_smug_sil as drillersil zorder 4:
        default
        xpos 0.73 
        alpha 0.0
    show i_sw_black as curtain2 zorder 3:
        default
        alpha 0.0
    t_ch_mrdriller "This looks like a great spot to start digging!" # @t_smrdriller119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Uh, sure, I guess so." # @t_smrdriller120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " There’s plenty of dirt around, anyway." # @t_smrdriller120.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "What are we digging for, exactly?" # @t_smrdriller121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_4', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "Haha, what?" # @t_smrdriller122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_5', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That’s silly…" # @t_smrdriller122.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_6', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Digging for…" # @t_smrdriller122.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_7', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Um…" # @t_smrdriller122.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_8', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_confused as mrdriller
    t_ch_mrdriller "What do you mean?" # @t_smrdriller123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_9', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I don’t understand the question." # @t_smrdriller123.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(I guess he just digs for the sake of it?)" # @t_smrdriller124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_happy as mrdriller
    t_ch_mrdriller "Well, since you left all your digging supplies at home, you can borrow one of my shovels." # @t_smrdriller125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s pretty amateur hour, no real options for specialized excavation techniques or anything…" # @t_smrdriller125.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "But it might be fun to do some old-school digging, like when you were a kid, huh?" # @t_smrdriller126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(I never did any digging when I was a kid!" # @t_smrdriller127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " I don’t HAVE any digging tools either…" # @t_smrdriller127.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_sad as cousin
    extend " In fact, I’ve never dug anything before in my entire life." # @t_smrdriller127.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Maybe I should get some digging tools when I get home…" # @t_smrdriller128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    extend " Jeez, how much is this little crush gonna cost me?!)" # @t_smrdriller128.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_excited as mrdriller
    show i_sw_black as curtain zorder 9:
        # ShowWithAtl
        linear 1 alpha 1.0
    extend "{w=1.0}{nw}"
    t_ch_mrdriller "Ok! Let’s get started! Boy, I’m so excited!" # @t_smrdriller129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/drill1.ogg"
    play sound "sfx/shovel.ogg"
    t_ch_cousin "(This digging thing…" # @t_smrdriller130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m not sure I’m so good at it." # @t_smrdriller130.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/shovel.ogg"
    extend " The shovel is pretty awkward to use!" # @t_smrdriller130.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/drill2.ogg"
    play sound "sfx/shovel.ogg"
    t_ch_cousin "Still, Mr. Driller is having a lot of fun…" # @t_smrdriller131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s very nice to see him less stressed." # @t_smrdriller131.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    play sound "sfx/drill2.ogg"
    play sound "sfx/shovel.ogg"
    t_ch_cousin "Although it seems a little like he’s destroying as much as he’s digging." # @t_smrdriller132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Well, c’est la vie!)" # @t_smrdriller133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 1 alpha 0.0
    extend "{w=1.0}{nw}"
    t_ch_mrdriller "Phew! That’s a wrap, Digging Club!" # @t_smrdriller134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "What a great first day!" # @t_smrdriller135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_surprised as cousin
    t_ch_cousin "Phew! What a workout!" # @t_smrdriller136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_excited as mrdriller
    t_ch_mrdriller "Ha! OH YEAH!" # @t_smrdriller137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It feels so good to finally get digging again!" # @t_smrdriller137.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "How could Dad ever give this up?!" # @t_smrdriller138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_smug as mrdriller
    t_ch_mrdriller "Haha… if I didn’t love my dad so much I’d probably say it was because he’s a washed up coward who’s afraid to really LIVE!" # @t_smrdriller139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_excited as mrdriller
    show i_cousin_exhausted_mortified as cousin
    t_ch_mrdriller "Ha ha… Ha!" # @t_smrdriller140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "…" # @t_smrdriller141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_confused as mrdriller
    t_ch_mrdriller "...Yeah… Dads. Always telling you what to do..." # @t_smrdriller142.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Embarrassing you in front of your friends…" # @t_smrdriller142.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    extend "{w=1.0}{nw}"
    extend " Trying to crush your spirit into little tiny molecules of gravel, even though they don’t have the stones to work with REAL gravel anymore…" # @t_smrdriller142.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "That’s the way it is with every family!" # @t_smrdriller143.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_excited as mrdriller
    extend " I’m sure you know the drill." # @t_smrdriller143.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "(...Yikes.)" # @t_smrdriller144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Alright! Shall we forget about how horrible our stupid ugly dads are…" # @t_smrdriller145.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_happy as mrdriller
    extend " and get back to DIGGING?!" # @t_smrdriller145.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Hey, I like my family!" # @t_smrdriller146.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I have the feeling that’s not what he wants to hear, though." # @t_smrdriller146.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " And anyway, I have… less depressing things to discuss. Well, hopefully.)" # @t_smrdriller146.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Mr. Driller… before you say anymore, I-" # @t_smrdriller147.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I have to confess something to you!" # @t_smrdriller148.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_shock as mrdriller
    t_ch_mrdriller "A post-digging confession??" # @t_smrdriller149.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_drillup_happy as mrdriller
    extend " That’s the best kind!" # @t_smrdriller149.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "The truth is… digging with you out there…" # @t_smrdriller150.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It’s the first time I’ve ever dug anything in my whole life!" # @t_smrdriller151.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I  don’t actually have any of my own digging supplies." # @t_smrdriller152.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Not even like, a plastic shovel for a sandbox." # @t_smrdriller152.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "… Oh…" # @t_smrdriller153.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_happy as mrdriller
    extend " Then…" # @t_smrdriller153.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_confused as mrdriller
    t_ch_mrdriller "Why did you found the Digging Club with me?" # @t_smrdriller154.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Well… because you needed my help!" # @t_smrdriller155.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " And you asked so nicely…" # @t_smrdriller155.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "[slot_playerName]!" # @t_smrdriller156.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You…" # @t_smrdriller156.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_10', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_excited as mrdriller
    t_ch_mrdriller "You are a true friend!" # @t_smrdriller157.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_11', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    with Dissolve(0.5)
    extend " Any treasure I could find would never be better than true friendship!" # @t_smrdriller157.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_12', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "Except maybe a huge diamond…" # @t_smrdriller158.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_13', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Those are worth like a million points I think." # @t_smrdriller158.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_14', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Aw, well." # @t_smrdriller159.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_15', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin_blush as cousin
    extend " I was happy to do it!" # @t_smrdriller159.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_16', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "But if you joined a club to help MY passion…" # @t_smrdriller160.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_17', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Is there some other club you’d have rather pursued?" # @t_smrdriller160.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_18', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "What’s YOUR passion, [slot_playerName]?" # @t_smrdriller161.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_19', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_happy as mrdriller
    extend " Everyone’s got one! Everyone in the WHOLE WORLD!" # @t_smrdriller161.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    show i_sw_black as curtain zorder 3:
        # ShowWithAtl
        linear 0.5 alpha 0.5
    extend "{w=0.5}{nw}"
    t_ch_cousin "(Hmmm, I’ve got to think hard about that before I answer him." # @t_smrdriller162.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...Now that I stop to think of it…" # @t_smrdriller163.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I think I really have a passion for rolling my katamari." # @t_smrdriller163.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "I’m not as good as my cousin the Prince, but…" # @t_smrdriller164.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " When I was rolling it the other day-" # @t_smrdriller164.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It was just so much fun! It felt right." # @t_smrdriller164.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But I caused so much trouble and hurt so many people…" # @t_smrdriller165.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " As much as it saddens me, I don’t think I should ever roll my katamari again." # @t_smrdriller165.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s just not worth the pain it causes." # @t_smrdriller165.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But I don’t want to say that in front of Mr. Driller." # @t_smrdriller166.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " A passionate guy like him…" # @t_smrdriller166.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "He keeps finding ways to do what he loves, even though his dad won’t let him…" # @t_smrdriller167.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I can’t help but think he’d look down on me, for quitting so easily.)" # @t_smrdriller167.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_sw_black as curtain:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    show i_mrdriller_slumped_confused as mrdriller
    extend "{w=0.5}{nw}"
    t_ch_mrdriller "What’s wrong? Is it too much of a personal question?" # @t_smrdriller168.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Heh, n-no, not at all…" # @t_smrdriller169.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s just…" # @t_smrdriller169.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "That I don’t know what my passion is yet!" # @t_smrdriller170.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I’m kind of envious of you, Mr. Driller." # @t_smrdriller171.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_excited as mrdriller
    t_ch_mrdriller "Oh! Well… maybe your passion can be digging, too!" # @t_smrdriller172.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_excited as mrdriller
    t_ch_mrdriller "Maybe it was FATE that led you to found the Digging Club with me!" # @t_smrdriller173.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "And if my dad says no-" # @t_smrdriller174.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "(Why would his dad say no to ME?!)" # @t_smrdriller175.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_excited as mrdriller
    t_ch_mrdriller "We can just smack him right in the mouth!" # @t_smrdriller176.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "With our heavy, heavy shovels." # @t_smrdriller177.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_smug as mrdriller
    t_ch_mrdriller "…Heh..." # @t_smrdriller178.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Um…" # @t_smrdriller179.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "Oh relax [slot_playerName]! It’s a joke!" # @t_smrdriller180.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I love my Dad! He’s family!" # @t_smrdriller180.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I love him so much you might even say I…" # @t_smrdriller181.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "dig" # @t_smrdriller182.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_smug as mrdriller
    t_ch_mrdriller "him!" # @t_smrdriller183.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "..." # @t_smrdriller184.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "Even though he disapproves of my digging anything ever for the rest of my life." # @t_smrdriller185.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(This guy…" # @t_smrdriller186.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " He’s cute, but…" # @t_smrdriller186.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    t_ch_cousin "It looks like my impression that he’s a big pile of issues was 100% correct." # @t_smrdriller187.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...Well, nobody’s perfect! I’m sure I have issues with stuff too." # @t_smrdriller188.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Maybe if I try to understand him a little better, I’ll understand why he gets so… dark.)" # @t_smrdriller188.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "This might be a silly question, but…" # @t_smrdriller189.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " Why do you love digging so much, anyway?" # @t_smrdriller189.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_excited as mrdriller
    t_ch_mrdriller "OH MY GOODNESS!" # @t_smrdriller190.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_shock as mrdriller
    extend " What’s NOT to love about digging?!" # @t_smrdriller190.01 self.block='Last'
    show i_sw_black as curtain:
        alpha 0.0
        linear 0.75 alpha 1.0
    $ renpy.pause(0.75) # Curtain fade
    show i_bg_quad_bleachers as bg # behind curtain
    # <SettingChange SettingChange {'bgImage': '@i_bg_quad_bleachers', 'curtainFadeTime': '.75', 'name': '_1q', 'kind': 'SettingChange'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    show i_sw_black as curtain:
        alpha 1.0
        linear 0.75 alpha 0.0
    $ renpy.pause(0.75) # Curtain fade
    # <ParallelEvent ParallelEvent {'name': '_1r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_mortified as cousin
    show i_mrdriller_standing_excited as mrdriller
    t_ch_mrdriller "...And, there’s SO many tools you can use for digging!" # @t_smrdriller191.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But that’s not even the MAIN reason I love digging so much…" # @t_smrdriller191.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Well, what IS the main reason?" # @t_smrdriller192.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " (C’mon, you’ve been talking FOREVER…)" # @t_smrdriller192.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "Well, it’s…" # @t_smrdriller193.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s just that digging…" # @t_smrdriller193.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " It’s about…" # @t_smrdriller193.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Discovery." # @t_smrdriller194.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_1z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "!!" # @t_smrdriller195.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_20', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " (Something in his face changed…" # @t_smrdriller195.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_21', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I feel weirdly inspired just seeing his eyes light up like that.)" # @t_smrdriller195.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_22', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "When you dig, you’re going under the surface…" # @t_smrdriller196.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_23', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Past it." # @t_smrdriller196.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_24', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " You dig further and further." # @t_smrdriller196.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_25', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Most people walk around on the ground and never even once think about what’s under there." # @t_smrdriller197.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_26', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_excited as mrdriller
    extend " But there’s a whole world of amazing things waiting for you to find!" # @t_smrdriller197.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_27', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Uh, really?" # @t_smrdriller198.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_28', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    extend " It kinda looked like you were just…" # @t_smrdriller198.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_29', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Destroying stuff by digging through it." # @t_smrdriller198.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_shock as mrdriller
    t_ch_mrdriller "But don’t you get it? That’s about discovery too!" # @t_smrdriller199.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " If you dig into something, and you break it open-" # @t_smrdriller199.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "You get to find out what’s inside of it." # @t_smrdriller1100.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "See? And…" # @t_smrdriller1101.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " There’s always more inside of it than you ever imagined." # @t_smrdriller1101.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Yeah…" # @t_smrdriller1102.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Actually, I see what you mean." # @t_smrdriller1102.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Mr. Driller… that’s really cool." # @t_smrdriller1103.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I wish…" # @t_smrdriller1104.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2J', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_exhausted_neutral as cousin
    extend " I wish I could hold onto my passion like you." # @t_smrdriller1104.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2K', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "...It was my dad, DigDug, who encouraged me…" # @t_smrdriller1105.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2L', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Huh? The guy you hate so much, the one that’s stressing you out…" # @t_smrdriller1106.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2M', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "He’s the one who made you want to dig stuff in the first place?!" # @t_smrdriller1107.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2N', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_shock as mrdriller
    t_ch_mrdriller "Whoah whoah! I don’t hate my dad!" # @t_smrdriller1108.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2O', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "It’s just… Isn’t it normal for teenagers to clash with their parents?" # @t_smrdriller1109.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2P', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I’m sure you’ve gotten mad and shut yourself in a room before…" # @t_smrdriller1109.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Or snuck out to meet friends…" # @t_smrdriller1109.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2R', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_smug_sil as drillersil:
        # ShowWithAtl
        linear 3 alpha 0.25
    show i_cousin_default_mortified as cousin
    extend "{w=3.0}{nw}"
    extend " Or just got so upset over something he said that you dug a big big hole, six feet deep, and sat there just staring desperately into it until the sun came up…" # @t_smrdriller1109.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2S', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_happy as mrdriller
    show i_mrdriller_standing_smug_sil as drillersil:
        # ShowWithAtl
        linear 0.5 alpha 0.0
    extend "{w=0.5}{nw}"
    t_ch_mrdriller "That’s all normal stuff!" # @t_smrdriller1110.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2T', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_mortified as cousin
    t_ch_cousin "Ummm…" # @t_smrdriller1111.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2U', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Sure…" # @t_smrdriller1111.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2V', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But still, it’s surprising that your dad used to be into digging too." # @t_smrdriller1112.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2W', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "(Although, come to think of it, his name IS “Dig Dug”.)" # @t_smrdriller1113.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2X', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_sad as mrdriller
    t_ch_mrdriller "Yeah, I don’t know what to do about that…" # @t_smrdriller1114.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I keep thinking… if Dad would just remember how important it is to dig!" # @t_smrdriller1114.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2Z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " After all… he was a digging LEGEND once." # @t_smrdriller1114.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2a', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " He was even kinda my hero." # @t_smrdriller1114.03 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2b', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_surprised as cousin
    t_ch_cousin "Just keep digging in secret!" # @t_smrdriller1115.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2c', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "If he’s forbidding you, maybe it’s okay to lie about it, given the circumstances." # @t_smrdriller1116.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2d', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_sad as mrdriller
    t_ch_mrdriller "...But… he’s my father." # @t_smrdriller1117.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2e', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Didn’t I just tell you, he’s the one you encouraged me to dig in the first place?" # @t_smrdriller1118.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2f', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "Well, I mean…" # @t_smrdriller1119.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2g', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Yeah, but…" # @t_smrdriller1119.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2h', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I want to dig up my problems and break them open." # @t_smrdriller1120.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2i', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Not bury them down where they’ll stay forever…" # @t_smrdriller1120.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2j', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I don’t want to lie to my dad. He’s important to me." # @t_smrdriller1121.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2k', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_handsup_sad as mrdriller
    t_ch_mrdriller "Besides… you shouldn’t have to hide your passion!" # @t_smrdriller1122.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2l', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That’s… a disrespect…" # @t_smrdriller1122.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2m', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " to the art of digging!" # @t_smrdriller1122.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2n', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "I… I guess so." # @t_smrdriller1123.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2o', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "But isn’t that what your dad did? Buried his passion for digging away?" # @t_smrdriller1124.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2p', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " N-not that you should disrespect the art of digging or anything, but…" # @t_smrdriller1124.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2q', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "It’d be pretty hypocritical of him to give you flak for that, right?" # @t_smrdriller1125.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2r', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_confused as mrdriller
    t_ch_mrdriller "…" # @t_smrdriller1126.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2s', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I never thought of it exactly like that before…" # @t_smrdriller1126.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2t', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I guess that’s true… he DID disrespect the art." # @t_smrdriller1126.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2u', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "..." # @t_smrdriller1127.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2v', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_slumped_happy as mrdriller
    t_ch_mrdriller "Heh! Classic Dad." # @t_smrdriller1128.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2w', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Every time you think he can’t disappoint you any further, he finds a way!" # @t_smrdriller1128.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2x', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Like a hole you keep digging and digging and you’ll never ever find the bottom!" # @t_smrdriller1128.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2y', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_mrdriller_standing_happy as mrdriller
    t_ch_mrdriller "You know how it is." # @t_smrdriller1129.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_2z', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Uh… yeah…" # @t_smrdriller1130.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_30', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "Exactly?" # @t_smrdriller1131.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_31', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "But no… I can’t do it." # @t_smrdriller1132.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_32', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I love digging too much to hide it." # @t_smrdriller1132.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_33', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I don’t exactly know what to do next." # @t_smrdriller1133.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_34', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " But… maybe I’ll discover it as I dig along!" # @t_smrdriller1133.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_35', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    t_ch_cousin "(This guy’s... really out of his depth, to say the least." # @t_smrdriller1134.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_36', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "But his passion is pretty cool. Maybe I could help…)" # @t_smrdriller1135.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_37', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_cousin "...I’m glad you have such strong convictions, Mr. Driller." # @t_smrdriller1136.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_38', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "Don’t worry, [slot_playerName]." # @t_smrdriller1137.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_39', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " Even if you haven’t found your passion yet…" # @t_smrdriller1137.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3A', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " That’s kinda what highschool is for, isn’t it?" # @t_smrdriller1137.02 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3B', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "But you know, if you liked digging…" # @t_smrdriller1138.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3C', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    t_ch_mrdriller "I highly recommend it!" # @t_smrdriller1139.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3D', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_grin as cousin
    t_ch_cousin "Haha, yeah…" # @t_smrdriller1140.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3E', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I know you do." # @t_smrdriller1140.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3F', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    show i_sw_black as curtain2:
        # ShowWithAtl
        linear .75 alpha 0.5
    extend "{w=0.75}{nw}"
    t_ch_cousin "(Is it healthy to be that consumed with just one thing?" # @t_smrdriller1141.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3G', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_sad as cousin
    extend " Maybe Mr. Driller doesn’t have room in his heart for digging AND… someone special." # @t_smrdriller1143.01 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3H', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    show i_cousin_default_neutral as cousin
    t_ch_cousin "...Well, it’s like he said… digging is about discovery." # @t_smrdriller1144.00 self.block='Last'
    # <ParallelEvent ParallelEvent {'name': '_3I', 'kind': 'ParallelEvent'} ''>
    # <Events events {'kind': 'events'} ''>
    extend " I won’t find out if I don’t keep digging, too.)" # @t_smrdriller1144.01 self.block='Last'
    # <NHSceneChange NHSceneChange {'name': '_3J', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
    label s_mrdriller1__3J:
        # <NHSceneChange NHSceneChange {'name': '_3J', 'scene': 's_day2', 'kind': 'NHSceneChange'} ''>
        jump s_day2