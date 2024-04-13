import requests
import json
from db_utils import get_available_books

#functions to connect to app endpoints with user input



#run function that interacts with user in terminal

def run():
    print(get_available_books())

if __name__ == '__main__':
    run()