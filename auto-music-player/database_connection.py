import sqlite3


SONG_DATABASE = "songs_db.db"
CONN = sqlite3.connect(SONG_DATABASE)


def create_table(table: str = "", columns: list = [], query: str = ""):
    global CONN
    if not query:
        query = f"CREATE TABLE {table}("

        for col in columns:
            query += col + ", "
        query = query[:len(query)-2] + ")"

        # print(query)                                                # uncomment to debug
    CONN.execute(query)
    # print("\n[+] Successfully added a table.\n")                    # uncomment to show log


def insert_data_into_table(table: str = "", data_pair: list = [], query: str = ""):
    global CONN
    if not query:
        query = f"INSERT INTO {table}("

        for col, _ in data_pair:
            query += col + ", "
        query = query[:len(query)-2] + ") VALUES ("
        
        for _, data in data_pair:
            query += data + ", "
        query = query[:len(query)-2] + ")"

        # print(query)                                               # uncomment to debug
    CONN.execute(query)
    CONN.commit()
    # print("\n[+] Successfully added data to the table.\n")         # uncomment to show log


def extract_data_from_table(table: str = "", columns: list = [], query: str = "", cond: str = ""):
    global CONN
    if not query:
        query = f"SELECT "

        for col in columns:
            query += col + ", "
        query = query[:len(query)-2] + f" FROM {table}"

        if cond:
            query += " WHERE " + cond


        # print(query)                                               # uncomment to debug
    # print("\n[+] Successfully extracted data from the table.\n")   # uncomment to show log
    cur = CONN.cursor()
    result = cur.execute(query)
    # print(result.fetchall())                                       # uncomment to debug
    return result.fetchall()


if __name__ == "__main__":
    # column_template = ['ID INTEGER PRIMARY KEY     AUTOINCREMENT',
    #             'SONG_NAME           VARCHAR(50)    NOT NULL',
    #             'PATH           VARCHAR(100)    NOT NULL',
    #             'AUTHOR         VARCHAR(70)',
    #             'ALBUM          VARCHAR(50)',
    #             'IS_FAVOURITE   BOOLEAN NOT NULL DEFAULT 0',
    #             'PLAYLIST_ID          INTEGER']

    # create_table(table = "SONGS", columns=column_template)

    # column_template = ['ID INTEGER PRIMARY KEY     AUTOINCREMENT',
    #             'PLAYLIST_NAME           VARCHAR(50)    NOT NULL',
    #             'IS_FAVOURITE   BOOLEAN NOT NULL DEFAULT 0']

    # create_table(table = "PLAYLISTS", columns=column_template)

    # data_pair_template = [  ["SONG_NAME", "'testing2'"],
    #                         ["IS_FAVOURITE", "1"]]

    # insert_data_into_table(table="SONGS", data_pair=data_pair_template)

    # column_template = ["*", "IS_FAVOURITE"]
    # cond_template = "SONG_NAME LIKE '%in%'"
    # extract_data_from_table(table="SONGS", columns=column_template, cond=cond_template)

    pass


# def extract_songs_list():
#     global CONN
#     query = "SELECT * FROM songs"
#     cur = CONN.cursor()
#     result = cur.execute(query)
#     return result.fetchall()


# def add_songs_to_database():
#     global CONN