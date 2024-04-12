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
            


if __name__ == '__main__':
    get_all_waitlisted_books('waitlist')