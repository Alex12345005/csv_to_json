from flask import Flask, request, jsonify, render_template
from tinydb import TinyDB, Query
import json

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    Books = db.table('books')
    file = request.files['jsonFile']
    data = json.load(file)
    if isinstance(data, list):
        Books.insert_multiple(data)
    else:
        Books.insert(data)
    return jsonify({"message": "Datei erfolgreich hochgeladen und Daten gespeichert"})

@app.route('/books', methods=['GET'])
def get_books():
    Books = db.table('books')
    books = Books.all()
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
