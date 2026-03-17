import mysql.connector
import os 

SQL_HOST = os.getenv('SQL_HOST', 'localhost')
conf = {
  "host": SQL_HOST,
  "port": 3306,
  "user": "root",
  "password": "root",
  "database": "digital_hunter"
}

class SQL:
  cnx = None
  cursor = None

  @classmethod
  def get_cnx(cls):
    if cls.cnx is None:
      try:
        cls.cnx = mysql.connector.connect(**conf)
      except mysql.connector.Error as err:
        print(err)
    return cls.cnx
  
  @classmethod
  def get_cursor(cls):
    # if cls.cursor is None:
    #     try:
    #         cnx = cls.get_cnx()
    #         cls.cursor = cnx.cursor(dictionary=True)
    #     except mysql.connector.Error as err:
    #         print(err)
    cnx = cls.get_cnx()
    cls.cursor = cnx.cursor(dictionary=True)
    return cls.cursor
      
