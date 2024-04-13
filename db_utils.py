import mysql.connector
from config import USER, PASSWORD, HOST
from datetime import datetime

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

def get_all_waitlisted_books(waitlistbooks):
    waitlist = []
    try: 
        db_name = 'books?'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        
        query = """
            SELECT title, author, waitlistdays
            FROM booktablename
            WHERE waitlist = TRUE
            """
    except Exception:
        raise DbConnectionError('Failed to fetch waitlist books')
        
    finally: 
            if db_connection:
                db_connection.close()
            

def add_purchase(customer_name, book_id, delivery):
    try:
        db_name = 'books?'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        # generating the current date
        date = datetime.now().date().strftime('%Y-%m-%d')

        # query to get the current largest order id (should be the id of the latest entry in the table)
        order_id_query = """
            SELECT MAX(order_id)
            FROM orders
            """
        cur.execute(order_id_query)
        current_order_id = cur.fetchone()[0]  # here we are obtaining the result of the above query

        # now we use the above to set the order id of the new order
        # (we want it to automatically follow the previous order id)
        if current_order_id is None:
            order_id = 1
        else:
            order_id = current_order_id + 1

        # query to add a new row to the orders table
        new_order_query = """
            INSERT INTO orders
            (date, order_id, book_id, customer_name, delivery)
            VALUES
            ('{date}', '{order_id}', '{book_id}', '{customer_name}', '{delivery}')
        """.format(date=date, order_id=order_id, book_id=book_id, customer_name=customer_name, delivery=delivery)
        cur.execute(new_order_query)

        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
     if db_connection:
        db_connection.close()
        print("DB connection is closed")


def update_stock_quantity(book_id):
    try:
     db_name = 'book_store_db'
     db_connection = _connect_to_db(db_name)
     cur = db_connection.cursor()

     update_stock_query = """
     UPDATE book_stock
     SET stock_quantity = stock_quantity - 1
     WHERE book_id = %s
     """

     cur.execute(update_stock_query, (book_id,))
     db_connection.commit()
     cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")



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
    get_all_waitlisted_books('waitlist')