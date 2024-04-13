# import requests
# import json
from db_utils import get_all_waitlisted_books

#functions to connect to app endpoints with user input


#run function that interacts with user in terminal



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
    elif optionSelect == 'purchase':
        # Add purchase functionality here
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
