from flask import Flask, jsonify, request
from db_utils import get_available_books

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

#purchase a book
@app.route("/purchase")

# add customer review
@app.route("/customerreview)
           


if __name__ == '__main__':
    app.run(debug=True, port=5000)