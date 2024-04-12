import mysql.connector
from config import USER, PASSWORD, HOST

class DbConnectionError(Exception):

    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


#functions to interact with SQL databases go here. Includes SQL queries





#function to get all records for books currently available and not on waitlist
def get_available_books():
    try:
        db_name = 'tests'  # UPDATE THIS
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        #SQL query to select all books that are not on the waitlist
        query = """
            SELECT book_id, title, author, date, stock_quantity, price 
            FROM table_3 
            WHERE waitlist = no
            """  # UPDATE TABLE NAME AND WHERE CLAUSE
        
        cur.execute(query)   #execute query within connection to db defined in cur
        
        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        
        #tranform tuple into a readable list
        for book in result:
        print(F"Book ID: {book[0]}. {book[1]} by {book[2]}. Published {book[3]}. {book[4]} in stock. Price: {book[5]}")
      
        cur.close()

    except Exception:     #if any errors in try block raise this exception
        raise DbConnectionError("Failed to read data from DB")

    finally:   #code to be executed anyway
        if db_connection:  #if connection to db successful, clost connection and print message
            db_connection.close()
            print("DB connection is closed")



if __name__ == '__main__':
