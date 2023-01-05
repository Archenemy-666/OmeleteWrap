""" module is providing functions to run sqlite using python"""
import sqlite3

class Anime:
    """Class representing an Anime entity"""
    table_name = "AnimeWishList"

    def connect():
        """Connect with the Database"""
        con = sqlite3.connect("testAnime.db")
        return con

    def adding(new_row):
        """Inserting Anime entries to the table AnimeWishList"""
        con = Anime.connect()
        cur = con.cursor()
        cur.execute("INSERT INTO AnimeWishList VALUES(?,?,?,?)", new_row)
        con.commit()

    def read():
        """Reading through the table AnimeWishList"""
        con = Anime.connect()
        cur = con.cursor()
        select_query = f"SELECT * FROM {Anime.table_name}"
        #select_query = "SELECT * FROM %s"%(Anime.table_name)
        return cur.execute(select_query)

    def print():
        """looking at the table AnimeWishList"""
        table = []
        for each in Anime.read():
            table.append(each)
            print (each)
        return table
