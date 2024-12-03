<<<<<<< HEAD
# import mysql.connector

# #from dotenv import load_dotenv

# #load_dotenv()

# import os
=======
import mysql.connector

#from dotenv import load_dotenv

#load_dotenv()

import os
>>>>>>> 22ce99b8fc8905e6660966527b0ba0a01324eaad





<<<<<<< HEAD
# connection = mysql.connector.connect(host=os.environ["DATABASE_HOST"],
#                                          database=os.environ["DATABASE"],
#                                          user=os.environ["DATABASE_USER"],
#                                          password=os.environ["DATABASE_PASSWORD"])





# def create_table_if_not_exist():
#     try:
        

#         mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS user_table  ( 
#                              Id int NOT NULL AUTO_INCREMENT,
#                              prenom varchar(250) NOT NULL,
#                              nom varchar(250) NOT NULL,
#                              age int NOT NULL,
#                              fonction varchar(250) NOT NULL,
#                              PRIMARY KEY (Id)) """

#         cursor = connection.cursor()
#         cursor.execute(mySql_Create_Table_Query)
#         print("User Table created successfully ")

#     except mysql.connector.Error as error:
#         print("Failed to create table in MySQL: {}".format(error))
#     finally:
#         cursor.close()

    
# def user_struct(user):
#     return {
#         "id" : user[0],
#         "prenom" : user[1],
#         "nom" : user[2],
#         "age" : user[3],
#         "fonction" : user[4]

#     }

# def get_users():
#     #create_table_if_not_exist()
#     with connection.cursor() as cursor:
#         cursor.execute("select * from user_table ")
#         users = cursor.fetchall()
#         cursor.close()
#         #print(users)
#         return [user_struct(user) for user in users]

# def create_user(user_data):
#     create_table_if_not_exist()
#     with connection.cursor() as cursor:
#         query = """
#                 INSERT INTO user_table(prenom, nom, age, fonction)
#                 VALUES(%s,%s,%s,%s)
#                 """
#         print(user_data.age)
#         cursor.execute(query,(
#             user_data.prenom,
#             user_data.nom,
#             user_data.age,
#             user_data.fonction
#         ))
#         connection.commit()
#         cursor.close()
#         return "user created successfully"

# def get_user_prenom(prenom):
#     with connection.cursor() as cursor:
#         q = "select * from user_table where prenom = %s"
#         cursor.execute(q,(prenom,))
#         user = cursor.fetchone()
#         cursor.close()
#         return user
    
# def get_user_id(id):
#     with connection.cursor() as cursor:
#         q = "select * from user_table where Id = %s"
#         cursor.execute(q,(id,))
#         user = cursor.fetchone()
#         cursor.close()
#         return user
=======
connection = mysql.connector.connect(host=os.environ["DATABASE_HOST"],
                                         database=os.environ["DATABASE"],
                                         user=os.environ["DATABASE_USER"],
                                         password=os.environ["DATABASE_PASSWORD"])


def create_table_if_not_exist():
    try:
        

        mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS user_table  ( 
                             Id int NOT NULL AUTO_INCREMENT,
                             prenom varchar(250) NOT NULL,
                             nom varchar(250) NOT NULL,
                             age int NOT NULL,
                             fonction varchar(250) NOT NULL,
                             PRIMARY KEY (Id)) """

        cursor = connection.cursor()
        cursor.execute(mySql_Create_Table_Query)
        print("User Table created successfully ")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        cursor.close()

    
def user_struct(user):
    return {
        "id" : user[0],
        "prenom" : user[1],
        "nom" : user[2],
        "age" : user[3],
        "fonction" : user[4]

    }

def get_users():
    #create_table_if_not_exist()
    with connection.cursor() as cursor:
        cursor.execute("select * from user_table ")
        users = cursor.fetchall()
        cursor.close()
        #print(users)
        return [user_struct(user) for user in users]

def create_user(user_data):
    create_table_if_not_exist()
    with connection.cursor() as cursor:
        query = """
                INSERT INTO user_table(prenom, nom, age, fonction)
                VALUES(%s,%s,%s,%s)
                """
        print(user_data.age)
        cursor.execute(query,(
            user_data.prenom,
            user_data.nom,
            user_data.age,
            user_data.fonction
        ))
        connection.commit()
        cursor.close()
        return "user created successfully"

def get_user_prenom(prenom):
    with connection.cursor() as cursor:
        q = "select * from user_table where prenom = %s"
        cursor.execute(q,(prenom,))
        user = cursor.fetchone()
        cursor.close()
        return user
    
def get_user_id(id):
    with connection.cursor() as cursor:
        q = "select * from user_table where Id = %s"
        cursor.execute(q,(id,))
        user = cursor.fetchone()
        cursor.close()
        return user
>>>>>>> 22ce99b8fc8905e6660966527b0ba0a01324eaad
