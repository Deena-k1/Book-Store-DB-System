from flask import Flask, jsonify, request
from db_utils import get_all_waitlisted_books

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
@app.route("/purchase")

# add customer review
@app.route("/customerreview")
           


if __name__ == '__main__':
    app.run(debug=True, port=5000)