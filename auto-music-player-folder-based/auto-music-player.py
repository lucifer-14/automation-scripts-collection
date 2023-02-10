import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame.mixer as pgmixer
import threading
import time

SONGS_FOLDER = "songs"          # You can configure it yourself

QUEUE = []                      
HAS_STARTED = True              # Don't do anything here
COUNTER = 0

MUSIC_PLAYER = pgmixer.music    # Don't do anything here
pgmixer.init()
MUSIC_PLAYER.set_volume(0.1)

def requirement_check():
    global SONGS_FOLDER
    check = True
    if not os.path.exists(SONGS_FOLDER):
        check = False
    return check

def file_check(path: str):
    check = True
    if not os.path.isfile(path):
        check = False
    return check


def play_music(song: str):
    music_player = pgmixer.music
    pgmixer.init()
    music_player.load(song)
    music_player.set_volume(0.1)
    music_player.play()
    print(f"\n[+] Playing song: {os.path.basename(song)}\n")


def help_menu(cmd):
    pass


def set_controls(cmd):
    global MUSIC_PLAYER
    _, option, value = cmd.split(" ")
    if option.lower() == "volume":
        MUSIC_PLAYER.set_volume(int(value)/100)
        print(f"\n[+] Volume set to {value}.\n")

def get_controls(cmd):
    global MUSIC_PLAYER
    split_cmd = cmd.split(" ")
    option = split_cmd[1].lower()
    # value = " ".join(split_cmd[2:])
    if option == "volume":
        volume = MUSIC_PLAYER.get_volume()
        print(f"[+] Current Volume {volume*100}")



def show_command(cmd):
    global SONGS_FOLDER
    split_cmd = cmd.split(" ")
    option = split_cmd[1].lower()
    value = " ".join(split_cmd[2:])

    if option == "playlists":
        if value:
            if os.path.exists(os.path.join(SONGS_FOLDER, value)):
                data_list = os.listdir(os.path.join(SONGS_FOLDER, value))
                is_songs_empty = True
                print("\nSongs")
                print("=====")

                for data in data_list:
                    is_songs_empty = False
                    print(os.path.basename(data))

                if is_songs_empty:
                    print("*Empty*")
                print()
            else:
                print("\nPlaylist doesn't exist.\n")

        else:
            is_playlist_empty = True
            data_list = os.listdir(SONGS_FOLDER)
            print("\nPlaylists")
            print("=========")
            
            for data in data_list:
                if not os.path.isfile(os.path.join(SONGS_FOLDER, data)):
                    is_playlist_empty = False
                    print(os.path.basename(data))

            if is_playlist_empty:
                print("*Empty*")
            print()
    elif option == "songs":
        if value:
            if value.lower() == "all":
                any_song_exist = False
                data_list = os.listdir(SONGS_FOLDER)
                songs_list = []
                playlists_list = []
                for data in data_list:
                    new_path = os.path.join(SONGS_FOLDER, data)
                    any_song_exist = True
                    if os.path.isfile(new_path):
                        songs_list.append(new_path)
                    else:
                        playlists_list.append(new_path)
                if any_song_exist:
                    for playlist in playlists_list:
                        is_playlist_empty = True
                        data_list = os.listdir(playlist)
                        print(f"\nPlaylist - {os.path.basename(playlist)}")
                        print("============"+("="*len(os.path.basename(playlist))))

                        for data in data_list:
                            if os.path.isfile(os.path.join(playlist, data)):
                                is_playlist_empty = False
                                print(os.path.basename(data))

                        if is_playlist_empty:
                            print("*Empty*")
                        print()
                    if songs_list != []:
                        print("\nNo Playlist Songs")
                        print("=================")
                        for song in songs_list:
                            if os.path.isfile(song):
                                print(os.path.basename(song))
                        print()

                else:
                    print("\n*Empty*\n")

                


        else:
            is_songs_empty = True
            data_list = os.listdir(SONGS_FOLDER)
            print("\nSongs")
            print("=====")

            for data in data_list:
                if os.path.isfile(os.path.join(SONGS_FOLDER, data)):
                    is_songs_empty = False
                    print(os.path.basename(data))
            
            if is_songs_empty:
                print("*Empty*")
            print()

    elif option.lower() == "queue":
        global QUEUE
        is_queue_empty = True
        print("\nQueue")
        print("=====")
        for i, song in enumerate(QUEUE):
            is_queue_empty = False
            if i == COUNTER:
                print(f"{str(i)}) {os.path.basename(song)} <=")
            else:
                print(f"{str(i)}) {os.path.basename(song)}")

        if is_queue_empty:
            print("\n*Empty*")

        print()
    
    


    # print(value)
    # print(option)


def queue_command(cmd):
    global QUEUE
    global HAS_STARTED
    global SONGS_FOLDER
    global COUNTER
    split_cmd = cmd.split(" ")
    main_cmd = split_cmd[0].lower()
    option = split_cmd[1].lower()
    value = " ".join(split_cmd[2:])
    if main_cmd == "add":

        if option == "playlist":
            if value:
                if os.path.exists(os.path.join(SONGS_FOLDER, value)):
                    data_list = os.listdir(os.path.join(SONGS_FOLDER, value))
                    if data_list != []:
                        print(f"\n[+] Songs added -")
                        for data in data_list:
                            QUEUE.append(os.path.join(SONGS_FOLDER, value, data))
                            print(f"{os.path.basename(data)}")
                        print()
                    else:
                        print(f"\n[+] Empty Playlist. No Songs Added.\n")

                else:
                    print(f"\n[-] Cannot Find the Playlist: {value}\n")
            else:
                print("\n[-] Error. Need to Specify Playlist Name.\n")
        elif option == "song":
            if value:
                if os.path.isfile(os.path.join(SONGS_FOLDER, value)):
                    QUEUE.append(os.path.join(SONGS_FOLDER, value))
                    print(f"\n[+] Songs added - {os.path.basename(value)}\n")
                else:
                    print(f"\n[-] Cannot Find the Song: {value}\n")
            else:
                print("\n[-] Error. Need to Specify Song Name.\n")

    elif main_cmd == "remove":

        if option == "all":
            QUEUE.clear()
            print(f"\n[-] Removed All Songs from Queue.\n")
        else:
            try:
                tmp = QUEUE[int(option)]
                QUEUE.pop(int(option))
                if int(option) <= COUNTER:
                    COUNTER -= 1
                print(f"\n[-] Removed `{os.path.basename(tmp)}` Song from Queue.\n")
            except IndexError:
                print(f"\n[-] Index Error. Total Songs in Queue: {len(QUEUE)}\n")

        if QUEUE == []:
            HAS_STARTED = True
    # if QUEUE == []:
    #     HAS_STARTED = False
    # else:
    #     HAS_STARTED = True
    if HAS_STARTED:
        # if QUEUE != []:
            t1 = threading.Thread(target=auto_music_player)
            HAS_STARTED = False
            t1.start()
            


def player_controls(cmd):
    global MUSIC_PLAYER
    split_cmd = cmd.split(" ")
    main_cmd = split_cmd[0].lower()
    # option = split_cmd[1].lower()
    # value = " ".join(split_cmd[2:])
    if main_cmd == "pause":
        MUSIC_PLAYER.pause()
    elif main_cmd == "unpause":
        MUSIC_PLAYER.unpause()


def auto_music_player():
    global HAS_STARTED
    global QUEUE
    global COUNTER
    if QUEUE == []:
        HAS_STARTED = True
        # print("true")
    else:
        while COUNTER < len(QUEUE):
            MUSIC_PLAYER.load(QUEUE[COUNTER])
            MUSIC_PLAYER.play()
            print(f"\n[+] Playing song: {os.path.basename(QUEUE[COUNTER])}\n")
            while MUSIC_PLAYER.get_busy():
                time.sleep(2)
                # print('playing')
            COUNTER += 1
            if QUEUE == []:
                break
            # print(QUEUE)
            
        # print('ok')

def auto_music_player_old_v():
    global SONGS_FOLDER
    if requirement_check():
        data_list = os.listdir(SONGS_FOLDER)
        for data in data_list:
            if os.path.isfile(os.path.join(SONGS_FOLDER, data)):
                if data.endswith == ".mp4":
                    play_music(os.path.join(SONGS_FOLDER, data))
            else:
                songs_list = os.listdir(os.path.join(SONGS_FOLDER, data))
                for song in songs_list:
                    if os.path.isfile(song):
                        if song.endswith == ".mp4":
                            play_music(song)
        # columns = ['SONG_NAME', 'PATH', 'AUTHOR', 'ALBUM', 'IS_FAVOURITE']
        # songs_list = dc.extract_data_from_table(table="SONGS", columns=columns)
        # for song in songs_list:
        #     if file_check(song[1]):
        #         play_music(song)
        pass

if __name__ == "__main__":
    print("\nAUTO MUSIC PLAYER")
    print("=================\n")
    while True:
        try:
            cmd = input("cmd> ")
            main_cmd = cmd.split(" ")[0].lower()
            if cmd == "":
                pass
            elif main_cmd == "help":
                help_menu(cmd)
            elif main_cmd == "set":
                set_controls(cmd)
            elif main_cmd == "get":
                get_controls(cmd)
            elif main_cmd == "show":
                show_command(cmd)
            elif main_cmd == "add" or main_cmd == "remove":
                queue_command(cmd)
            elif main_cmd == "next" or main_cmd == "back" or main_cmd == "pause" or main_cmd == "unpause" or main_cmd == "stop":
                player_controls(cmd)
            else:
                print('Try `help` for more information. Ctrl+C or `exit` to quit program.')
        except KeyboardInterrupt:
            QUEUE = []
            MUSIC_PLAYER.stop()
            # t1.join()
            print("\n\n[+] Auto Music Player terminated.\n")
            break

    # auto_music_player()
    
