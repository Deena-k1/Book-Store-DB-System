import requests
import json
from db_utils import all_books, reader_review, update_stock_quantity, get_available_books

### Functions to connect to app endpoints with user input ###

def get_available_books_data():
        endpoint = 'http://127.0.0.1:5000/booksavailable'
        response = requests.get(endpoint)   #get response from endpoint using requests module
        return response.json()  #convert to json format

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


    if result.status_code == 200:
        update_stock_quantity(book_id)
    return result.json()   

#function to add in endpoint for the user to access the waitlisted books information
def get_waitlist_books_data():
        endpoint = 'http://127.0.0.1:5000/waitlist'
        response = requests.get(endpoint)  
        return response.json()

#function to transform available books data into a readable list
def display_available_books():
    books = get_available_books_data()    #assign result from endpoint as variable books
    for book in books:    #iterate through data from endpoint
            print(F"{book['title']} by {book['author']}.\nPublished {book['year']}. Book ID: {book['book_id']}. Currently {book['stock_quantity']} in stock. Price: £{book['price']}\n")  #insert data from enpoint into a readable string


### Run function that interacts with user in terminal ###

#function that will recieve review input from user 
def handle_review():
    print("\n" + "ɷ" * 25 + " Review a Book " + "ɷ" * 25) #printing a border for a bit of visualisation
    all_books()
    valid_book_ids = [f'b{i}' for i in range(1, 12)] # created a variable fore book id, since the book id was a string, validation posed an issue so I iterated through the int part
    print("\nPlease select a book from our collection to review:")
    while True:
        book_id = input("Please enter the ID of the book that you'd like to review, e.g., 'b1': ")
        if book_id in valid_book_ids:
            break
        else:
            print("Uh Oh! Invalid book ID. Please enter a valid book ID.")

    customer_name = input("Please enter your name: ")
    while True:
        ratingstr = input("Enter your rating (1-5): ")
        try:
            rating = int(ratingstr)
            if 1 <= rating <= 5:  #more data validation
                break
            else:
                print("Book rating must be between 1 and 5.")# data validation that expects input to be between 1 and 5.
        except ValueError:
            print("Please enter a valid number")

    if rating >= 1 and rating <= 5: 
        reader_review(customer_name, book_id, rating)
        print("Review added successfully!")  # Display success message when correct input is submitted.
    else: 
        print('You have input an invalid option, please select one of the four choices')


# This is our main function that will run through the logic of the users choices.
# Using if elif else statements for the different options and to validate the user input as a correct option
def userOptionSelect(optionSelect):
    if optionSelect == 'waitlist':
        waitlisted_books = get_waitlist_books_data()
        for book in waitlisted_books:
            print("Title:", book['title'])
            print("Author:", book['author'])
            print("Waitlist Date:", book['waitlist_date'])
            print("Waiting Days:", book['waiting_days'])
            print()
        print('Thanks for viewing our waitlist')
        print()
    elif optionSelect == 'view':
       print("\nOur books: \n")
       display_available_books()
    # purchase books functionality:
    elif optionSelect == 'purchase':
        cust = input('Enter your name: ')
        book_order_id = input('Enter the book ID of the book you would like to purchase: ')
        
        available_books = get_available_books()
        if any(book['book_id'] == book_order_id and book['stock_quantity'] > 0 for book in available_books):
                shipping = input('Choose if you would like the book to be delivered (yes/no): ')
                add_new_order(cust, book_order_id, shipping)
                print("Order is Successful")
                print()
                print('Thank you for your order!')
        else:
                print("Book is unfortunately not available for purchase or out of stock.")   

    
    elif optionSelect == 'review':
        handle_review()
       
    
    elif optionSelect == 'exit':
        print('Thanks for stopping by!')
    else: 
        print('You have input an invalid option, please select one of the valid choices')

#Our run function and what the user sees as their greeting
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
    
#Adding a small comment so we can do a pull request on our finished files.