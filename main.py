import requests
import json
from db_utils import get_available_books

from db_utils import get_all_waitlisted_books

### Functions to connect to app endpoints with user input ###




# function to add a new book order to the database
def add_new_order(customer_name, book_id, delivery):

    new_order = {
         "customer_name": customer_name,
         "book_id": book_id,
         "delivery": delivery,
    }

    # post request adds a new row to the database
    result = requests.post(
        'http://127.0.0.1:5000/purchase',  # goes to the endpoint in app.py for the link
        headers={'content-type': 'application/json'},
        data=json.dumps(new_order)
    )

    return result.json()


### Run function that interacts with user in terminal ###



def userOptionSelect(optionSelect):
    if optionSelect == 'waitlist':
        waitlisted_books = get_all_waitlisted_books()
        for book in waitlisted_books:
            print("Title:", book['title'])
            print("Author:", book['author'])
            print("Waitlist Date:", book['waitlist_date'])
            print("Waiting Days:", book['waiting_days'])
            print()
            print('Thanks for viewing our waitlist')
            print()
    elif optionSelect == 'view':
        # Add view books functionality here
        pass
    # purchase books functionality:
    elif optionSelect == 'purchase':
        cust = input('Enter your name: ')
        book_order_id = input('Enter the book ID of the book you would like to purchase: ')
        shipping = input('Choose if you would like the book to be delivered (yes/no): ')
        add_new_order(cust, book_order_id, shipping)
        print("Order is Successful")
        print()
        print('Thank you for your order!')

        pass
    elif optionSelect == 'review':
        # Add review functionality here
        pass
    elif optionSelect == 'exit':
        print('Thanks for stopping by!')
    else: 
        print('You have input an invalid option, please select one of the valid choices')

def run():
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('Welcome to ReadFirstGirls - your online bookstore')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print()
    print()
    while True:
        optionSelect = input('''
             Would you like to:
                         
                * view our books
                * purchase a book 
                * review a book 
                * check out our waitlist
                             
            Please enter: view / purchase / review / waitlist / exit \n'''.lower())
        userOptionSelect(optionSelect)
        if optionSelect == 'exit':
            break


if __name__ == '__main__':
    run()
