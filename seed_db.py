import mysql.connector
import names
from mysql.connector import Error
from mysql.connector import errorcode
from numpy import random


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='db_name',
                                         user='username',
                                         password='password')
    name = str(names.get_first_name())
    student_number = random.randint(500000)
    date_of_birth = "20-12-2020"
    course = "SNE" 
    state = "Kazan"
    village = "Innopolis"
    apartment = "D5"
    house = "Dorms"
    country = "Russia"

    i = 2
    while i <= 500000:
        mySql_insert_query = """INSERT INTO table_one (id, name, student_number, date_of_birth, course, state, village, apartment, house, country) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, (i, name, student_number, date_of_birth, course, state, village, apartment, house, country))
        connection.commit()
        cursor.close()
        i += 1
    
    print(cursor.rowcount, "500,000 records inserted successfully into table")
    

except mysql.connector.Error as error:
    print("Failed to insert record into table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")