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

        # print(query)                                              # uncomment to debug
    CONN.execute(query)
    #print("\n[+] Successfully added a table.\n")                    # uncomment to show log


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

        # print(query)                                              # uncomment to debug
    CONN.execute(query)
    CONN.commit()
    #print("\n[+] Successfully added data to the table.\n")         # uncomment to show log



def extract_data_from_table(table: str = "", columns: list = [], query: str = "", cond: str = ""):
    global CONN
    if not query:
        query = f"SELECT "

        for col in columns:
            query += col + ", "
        query = query[:len(query)-2] + " FROM {table}"

        if cond:
            query += " WHERE " + cond


        # print(query)                                              # uncomment to debug
    #print("\n[+] Successfully added data to the table.\n")         # uncomment to show log
    cur = CONN.cursor()
    result = cur.execute(query)
    print(result)
    return result.fetchall()





# def extract_songs_list():
#     global CONN
#     query = "SELECT * FROM songs"
#     cur = CONN.cursor()
#     result = cur.execute(query)
#     return result.fetchall()


# def add_songs_to_database():
#     global CONN