"""
@author: william
"""

import sqlite3
from flask import Flask
from contextlib import closing


'''
# the way we want to name the file
DATABASE = './mooovies.db'
DEBUG = True


app = Flask(__name__)
app.config.from_object(__name__)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('mooovies.sql', mode='r') as f:#open the sql file and read it
            db.cursor().executescript(f.read())
        db.commit()# save the modifications into the database

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

'''
class Data_Base():

    def __init__(self,DB_Name : str ):# To create the database
        
        self.db = sqlite3.connect(DB_Name)
        self.cur = self.db.cursor()

    def Table_creator(self, Table_name : str, column : str ):# To cleate a table where Data will be store

        self.cur.execute('CREATE table IF NOT EXISTS' + name + ' ( ' + column + ' )' )
        self.db.commit()


    def Print_Data_Table(self, column : str , Table : str):#print All the Data that is inside the table


        self.cur.execute("SELECT " + column + " FROM " + Table ) #taking all the data contained in the table

        for ligne in self.cur :# displaying all the data from the table
            print("FilmName : {0}  | Genre : {1} | Year : {2} | Rating : {4} | ID : {3}".format(ligne[0],ligne[1],ligne[2],ligne[3],ligne[4]))

    def Data_Adder(self,Table : str ,Column_List : str ,data): #to add data to the Table

        Column_Number = ""# calculate the number of the column. this part of the code can be used for an unidentified number of columns
        for i in range(0,len(Column_List.split(',')) - 1 ,1) :
            Column_Number = Column_Number + ("?,")
        Column_Number = Column_Number + ("?")

        request = 'INSERT INTO ' + Table + ' ( ' + Column_List + ' ) VALUES ( ' + Column_Number + ')'#put the data in the request that you whant to add to the table
        self.cur.execute(request, data)
        self.db.commit()


    def Data_Updater(self, Table : str , New_Data : str , Modif_Condition : str):# to update 1 type of data from the Table
                
        self.cur.execute("UPDATE " + Table + " SET " + New_Data + " WHERE " + Modif_Condition)
        self.db.commit()

        
    def Data_Eraser(self, Table : str , Modif_Condition : str):   # to erase the data 
        
        self.cur.execute("DELETE FROM " + Table + " WHERE " + Modif_Condition)
        self.db.commit()

          
    def __del__(self):
        
        self.db.close()
        print("\n Object Deleted !")



if __name__ == "__main__":
    #init_db()
    
    Test_DB = Data_Base("mooovies.db") #I create my object that contain the data from the database mooovies
    print("\n Original Data \n")
    Test_DB.Print_Data_Table("*","mooovies") 
    
    
    print("\n Part 1 : Adding Data \n")
    Test_DB.Data_Adder("mooovies","FilmName,Year,Genre,Rating,ID",("prend la ciboulette et tire toi",2016,"Drama",5.0,"aaca0baa-0faa-4daa-aa28-aaae86faaaf6") )# I add some data
    Test_DB.Print_Data_Table("*","mooovies") 
    
    print("\n Part 2 : Updating Data  \n")
    #first update : changing movie name (1 record change)
    Test_DB.Data_Updater("mooovies","ID = '1219e67a-bfe3-4893-8a0f-ddd09a6fffff',FilmName = 'La Boucherie Martin'","FilmName = '5x2'")# i update some data
    #second update : changing Genre Horror to Comedy  (10 records changed)
    Test_DB.Data_Updater("mooovies","Genre = 'Comedy'","Genre = 'Horror'")# i update some data
    #third update : changing Rating of animations films (4 records changed)
    Test_DB.Data_Updater("mooovies","Rating = 8.5","Genre = 'Animation'")# i update some data
    #fourth update : making all films from 2012 Fantasy films (5 records)
    Test_DB.Data_Updater("mooovies","Genre = 'Fantasy'","Year = 2012")# i update some data
    Test_DB.Print_Data_Table("*","mooovies") 
    
    print("\n Part 3 : Deleting Data \n")
    #deleting 1 film by name
    Test_DB.Data_Eraser("mooovies","FilmName = 'Motel, The'") 
    #deleting by genre (5 movies)
    Test_DB.Data_Eraser("mooovies","Genre = 'Thriller'") 
    #deleting by raitng (3 movies)
    Test_DB.Data_Eraser("mooovies","Rating = 5.9") 
    #deleting by ID (1 movie)
    Test_DB.Data_Eraser("mooovies","ID = '32cbc778-0b8d-4e7a-960f-ca185079fa6b'") 
    Test_DB.Print_Data_Table("*","mooovies")
    
    del Test_DB 
    
    