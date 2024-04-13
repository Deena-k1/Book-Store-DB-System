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
    elif optionSelect == 'view':
        pass # adding pass on any bits for now that will need updated, but just so I can have the rough structure going
    elif optionSelect == 'purchase':
        pass
    elif optionSelect == 'review':
        pass
    else: 
        print('You have input an invalid option, please select the one of the four choices')


def run():
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('Welcome to ReadFirstGirls - your online bookstore')
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print()
    print()
    optionSelect = input('''
                        Would you like to:
                     
                        - view our books
                        - purchase a book 
                        - review a book 
                        - check out our waitlist
                         
                        Please enter: view / purchase / review / waitlist \n'''.lower())
    userOptionSelect(optionSelect)

    
    


if __name__ == '__main__':
    run()
    
    
    
    
    # optionSelect = input('''
    #                  Would you like to:
                     
    #                  - view our books
    #                  - purchase a book 
    #                  - review a book 
    #                  - check out our waitlist
                         
    #                 Please enter: view / purchase / review / waitlist \n'''.lower())
    # print()
    
    # if optionSelect == 'waitlist':
    #     waitlisted_books = get_all_waitlisted_books()
    #     for book in waitlisted_books:
    #         print("Title:", book['title'])
    #         print("Author:", book['author'])
    #         print("Waitlist Date:", book['waitlist_date'])
    #         print("Waiting Days:", book['waiting_days'])
    #         print()
    # elif optionSelect == 'view':
    #     pass # adding pass on any bits for now that will need updated, but just so I can have the rough structure going
    # elif optionSelect == 'purchase':
    #     pass
    # elif optionSelect == 'review':
    #     pass
    # else: 
    #     print('You have input an invalid option, please select the one of the four choices')