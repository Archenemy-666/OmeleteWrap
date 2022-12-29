import sqlite3
con = sqlite3.connect("testAnime.db")
cur = con.cursor()


#if the table exists then pass an exception
#Creating test data for DB.

def createTable():
    try: 
        cur.execute("CREATE TABLE AnimeWishList (AnimeName, genre, language, release)")
    except sqlite3.OperationalError as e:
        print("table exists", e)


#inserting elements 
def insertRows(Anime):
    cur.executemany("insert into AnimeWishList values(?,?,?,?)",Anime)
    return  readTable()
#Creating test data for DB.
Anime = [('DBZ' , 'shonen', 'JAP', 1996), ('Naruto',  'shonen', 'jap', 1998)]
#inserting elements 

#read 
def readTable():
    for row in cur.execute("select * from AnimeWishList"):
        print(row)


Anime = [('DBZ' , 'shonen', 'JAP', 1996), ('Naruto',  'shonen', 'jap', 1998)]
createTable()
insertRows(Anime)
con.commit()
con.close()
#inserting elements 

#update 

#delete


