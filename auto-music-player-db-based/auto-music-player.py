import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame.mixer as pgmixer
import database_connection as dc


def requirement_check():
    check = True
    if not os.path.isfile('songs_db.db'):
        check = False
    return check

def file_check(path: str):
    check = True
    if not os.path.isfile(path):
        check = False
    return check


def play_music(song: tuple):
    music_player = pgmixer.music
    pgmixer.init()
    music_player.load(song[1])
    music_player.set_volume(0.1)
    music_player.play()
    print(f"\n[+] Playing song: {song[0]}\n")


def auto_music_player():
    
    if requirement_check():
        columns = ['SONG_NAME', 'PATH', 'AUTHOR', 'ALBUM', 'IS_FAVOURITE']
        songs_list = dc.extract_data_from_table(table="SONGS", columns=columns)
        for song in songs_list:
            if file_check(song[1]):
                play_music(song)



if __name__ == "__main__":
    auto_music_player()
    
