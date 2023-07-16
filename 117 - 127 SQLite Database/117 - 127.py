# 01

# Numeric          => Int , Float
# Character String => Char , Varchar
# Date And Time 
# xml , json 

import sqlite3

db = sqlite3.connect("elzero.db") 

cr = db.cursor()

cr.execute("INSERT INTO Users Values(1,\"Ahmed\",'26/5/2000','ahmed12@gmail.com')")
cr.execute("INSERT INTO Users Values(2,\"eska\",'2/5/2000','ahmed123@gmail.com')")
cr.execute("INSERT INTO Users Values(3,\"rania\",'20/5/2000','ahmed1234@gmail.com')")
cr.execute("INSERT INTO Users Values(4,\"mahmoud\",'21/5/2000','ahmed12345@gmail.com')")
cr.execute("INSERT INTO Users Values(5,\"mahmoud2\",'25/5/2000','ahmed1245@gmail.com')")

cr.execute("SELECT * FROM Users")

print(cr.fetchmany(5)[4]) 

cr.execute("SELECT * FROM Users WHERE ID = 5")

print(cr.fetchone())

# 02

# Add Unique Constrain
cr.execute("CREATE TABLE if not exists Users(ID INTEGER UNIQUE , Name TEXT UNIQUE , DOB TEXT UNIQUE , Email TEXT UNIQUE)")

try :
    
    cr.execute("SELECT ID FROM Users")
    
    iDs = []

    for ID in cr.fetchall() :
        
        iDs.append(ID[0])

    ID = int(input("Enter The ID : "))

    if ID in iDs :
        
        cr.execute(f"DELETE FROM Users WHERE ID = '{ID}'")

        print("User Deleted Successfully")

        print("Show Other Data:")

        cr.execute("SELECT * FROM Users")

        for row in cr.fetchall() :
            print(f"ID => {row[0]} , Name => '{row[1]}' , Date Of Birth => '{row[2]}' , Email => {row[3]} ")

    else :
        
        print("User Not Found.")


except sqlite3.Error : 
    
    pass


finally:
    
    db.commit()
    db.close()