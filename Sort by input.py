import pymysql.cursors # database
from threading import Thread, Event # multithreading
import time
import datetime

# connect to the database
# The database "bartucz_scores" is on mysql.s483.sureserver.com
# The user is gamer / GamesAreGood2me
connection = pymysql.connect(host='mysql.s483.sureserver.com',
                             user='gamer',
                             password='GamesAreGood2me',
                             db='bartucz_scores',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Scores
        
        game=input("What game do you want sorted? ")
        
        sql = "SELECT * FROM `scores` WHERE game = '" +game+ "' ORDER BY score DESC"
       
        
        #execute the SQL command
        cursor.execute(sql)
        
        
        # get the results
        for result in cursor:
            # make sure that people didn't enter blank data into the database
            if (result and result['date'] and result['name'] and result['game'] and result['score']):
                print ("Date: " + result['date'].strftime("%y/%m/%d"))
                print ("Name: " + result['name'])
                print ("Game: " + str(result['game']))
                print ("Score: " + str(result['score']))
                print ("\n")
                
        
        #sql = "INSERT INTO scores(date, game, name, score) VALUES('" + str(date) + "', '" + str(game) + "', '" + str(name) + "','" + score + "')"
        #INSERT INTO `scores`(`date`, `game`, `name`, `score`) VALUES ([date],[game],[name],[score])
        #cursor.execute(sql)
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # Once you run one of those three SQL commands, you must commit to save your changes. 
        connection.commit()
        
finally:
    connection.close()