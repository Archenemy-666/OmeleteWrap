import sqlite3


class anime:
    table_name = "AnimeWishList"

    def connect(commit=False):
        con = sqlite3.connect("testAnime.db")
        return con
    
    #adding rows
    def adding(newRow):
        con = anime.connect()
        cur = con.cursor()
        insertQuery = cur.execute("INSERT INTO AnimeWishList VALUES(?,?,?,?)", newRow)
        con.commit()
    
    #read 
    def read():
        con = anime.connect()
        cur = con.cursor()
        selectQuery = "SELECT * FROM %s"%(anime.table_name)
        return cur.execute(selectQuery)
           
    def print():
        table = []
  
        for each in anime.read():
            table.append(each)
            print (each)
        return table

 
