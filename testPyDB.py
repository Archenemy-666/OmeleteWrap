import sqlite3
con = sqlite3.connect("testAnime.db")
cur = con.cursor()
#if the table exists then pass an exception
try: 
    cur.execute("CREATE TABLE AnimeWishList(AnimeName, genre, language, release)")
except sqlite3.OperationalError as e:
    print("table exists", e)

#create 

#read 

#update 

#delete


