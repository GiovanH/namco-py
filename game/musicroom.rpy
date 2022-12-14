define fse_music_data = {}

style musicroom_prefix is default

init 900 python:

    mr = MusicRoom(fadeout=0.0)

    fse_musicroom_tracks = filter(
        lambda f: f.lower()[-4:] in [".ogg"],
        renpy.list_files(common=False))

    print(list(fse_musicroom_tracks))

    for track in fse_musicroom_tracks:
        mr.add(track)

    def formatSongName(filepath):
        # return filepath
        track_meta = fse_music_data.get(filepath)
        if track_meta:
            return "[[{}] {} – {}".format(
                track_meta.get("album") or track_meta.get("package_id"), 
                track_meta.get("artist"), 
                track_meta.get("title"), 
            )
        else:
            filename = filepath.split("/")[-1]
            filesub = filepath.split("/")[0].replace("custom_assets_", "")
            ext = filename.split(".")[-1]
            filenamep = ".".join(filename.split(".")[:-1])
            return "[[{}] {}".format(filesub, filenamep)

    def formatSongPrefix(filepath):
        # Stub, override
        return ""

screen fj_music_room:
    tag menu
    use game_menu(_("Music")):
        vbox:
            spacing 10
            
            hbox:
                xalign 0.5
                # yanchor 0.5
                spacing 18
                imagebutton auto "freshjamz/play_%s.png" action (lambda: renpy.music.set_pause(False, channel='music')) 
                imagebutton auto "freshjamz/pause_%s.png" action (lambda: renpy.music.set_pause(True, channel='music'))
                imagebutton auto "freshjamz/prev_%s.png" action mr.Previous()
                imagebutton auto "freshjamz/next_%s.png" action mr.Next()
                imagebutton auto "freshjamz/single_%s.png" action mr.ToggleSingleTrack() selected mr.single_track
                imagebutton auto "freshjamz/shuffle_%s.png" action mr.ToggleShuffle() selected mr.shuffle
                
                # bar adjustment ui.adjustment(
            #     range=100,
            #     value=1,
            #     adjustable=True
            # )
            viewport:
                mousewheel True
                scrollbars "vertical"
                # The buttons that play each track.
                vbox:
                    ymaximum 5
                    # right_padding 16
                    for track in fse_musicroom_tracks:
                        hbox:
                            text formatSongPrefix(track) style "musicroom_prefix"
                            textbutton formatSongName(track) action mr.Play(track) # text_style fj_songitem

    frame:
        align (1.0, 1.0)
        xoffset -20
        padding (26, 24)
        background Frame("gui/buttonframe.png", 14, 14)
        vbox:
            xsize 220
            label _("Music Volume") text_color "#FFF"
            bar value Preference("music volume")
    # Start the music playing on entry to the music room.
    on "replace" action renpy.music.stop
    # mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action (lambda: renpy.music.set_pause(False, channel='music'))

