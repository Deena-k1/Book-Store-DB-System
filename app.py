from flask import Flask, jsonify, request
from db_utils import get_available_books, get_all_waitlisted_books, add_purchase, update_stock_quantity


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

# http://127.0.0.1:5001//booksavailable

#display books on waitlist, how long until they arrive
@app.route("/waitlist")
def get_waitlist():
    res = get_all_waitlisted_books('waitlist')
    return jsonify(res)

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






# add customer review
@app.route("/customerreview")
           


if __name__ == '__main__':
    app.run(debug=True, port=5000)