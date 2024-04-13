from flask import Flask, jsonify, request
from db_utils import get_all_waitlisted_books, add_purchase

app = Flask(__name__)

#test connection
@app.route("/")
def home():
    return {"Hello": "world"}

#display all books available
@app.route("/bookavailable")

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

# add customer review
@app.route("/customerreview")
           


if __name__ == '__main__':
    app.run(debug=True, port=5000)