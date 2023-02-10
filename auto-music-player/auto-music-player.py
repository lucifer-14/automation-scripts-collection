import os
import pygame.mixer as pgmixer
import database_connection as dc


def requirement_check():
    check = True
    if not os.path.isfile('songs_db.db'):
        check = False
    return check


def auto_music_player():
    
    if requirement_check():

        music_player = pgmixer.music
        music_player.init()
        music_player.load()
        music_player.set_volume(0.1)
        music_player.play()


if __name__ == "__main__":
    auto_music_player()
    
