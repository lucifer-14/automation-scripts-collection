import pygame.mixer as pgmixer
import sqlite3





    


def auto_music_player():
    songs_list = extract_song_list()

    music_player = pgmixer.music
    music_player.init()
    music_player.load()
    music_player.set_volume(0.1)
    music_player.play()


if __name__ == "__main__":
    auto_music_player()
    
