from flask import Flask, jsonify, request
from db_utils import get_all_waitlisted_books, add_purchase, update_stock_quantity, reader_review, get_available_books

app = Flask(__name__)

#test connection
@app.route("/")
def home():
    return {"Hello": "world"}

#display all books available
@app.route("/booksavailable")
def get_books():
    res = get_available_books()
    return jsonify(res)

# endpoint: http://127.0.0.1:5000/booksavailable


#display books on waitlist, how long until they arrive
@app.route("/waitlist")
def get_waitlist():
    waitlist_data = get_all_waitlisted_books()
    return jsonify(waitlist_data), 200, {'Content-Type': 'application/json; charset=utf-8'}


# http://127.0.0.1:5000/waitlist


#purchase a book
@app.route("/purchase", methods=['POST'])
def purchase_book():
    purchase = request.get_json()
    add_purchase(
        #date=purchase['date'],
        #order_id=purchase['order_id'],
        book_id=purchase['book_id'],
        customer_name=purchase['customer_name'],
        delivery=purchase['delivery'],
    )
    return purchase

#Function to update Quantity of book

@app.route('/update_stock', methods=['PUT'])
def update_stock():
    data = request.get_json()
    book_id = data.get('book_id')

    update_stock_quantity(book_id)

    return jsonify({'Stock quantity updated successfully'}), 200


#add customer review
@app.route("/customerreview", methods=['POST'])
           
def customer_review():
    review = request.get_json()
    customer_name = review['customer_name']
    book_id = review['book_id']
    rating = int(review['rating'])  # Convert rating to integer


    # Check to see if the rating input is within valid range

    if rating is None or not isinstance(rating, int):
        return jsonify({'error': 'Rating must be an integer'}), 400
   

    while True:
        try:
            rating = int(rating)  # Convert rating to integer
            if rating < 1 or rating > 5:
                raise ValueError("Rating must be between 1 and 5")
            break  # Exit the loop if rating is valid
        except ValueError:
            print("Uh oh! Invalid rating. Please enter a number between 1 and 5.")
            rating = input("Enter your rating (1-5): ")

    # Call the function to add the review to the database
    if rating >= 1 and rating <= 5: 
        reader_review(customer_name, book_id, rating)
        return jsonify({'message': 'Review added successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)

