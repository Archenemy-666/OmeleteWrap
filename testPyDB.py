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
def insertRows(tableName,Anime):   
    insertQuery = """INSERT INTO %s values(?,?,?,?)"""%(tableName)
    cur.executemany("insert into AnimeWishList values(?,?,?,?)",Anime)
    return  readTable(tableName)
#Creating test data for DB.
Anime = [('DBZ' , 'shonen', 'JAP', 1996), ('Naruto',  'shonen', 'jap', 1998)]
#inserting elements 

#read 
def readTable(TableName):
    selectQuery = """SELECT * FROM %s"""%(TableName)
    for row in cur.execute(selectQuery):
        print(row)


Anime = [('DBZ' , 'shonen', 'JAP', 1996), ('Naruto',  'shonen', 'jap', 1998)]
createTable()
insertRows('AnimeWishList',Anime)
readTable('AnimeWishList')
con.commit()
con.close()
name = "siddharth"
row = """siddharth %s"""%(name)
print(row)
#inserting elements 

#update 

#delete


