from reader import read_csv
from writer import write_json

def convert_csv_to_json(csv_file, json_file):
    
    books = read_csv(csv_file)
    
    for book in books:
        book['ISBN'] = None
        book['Bewertung'] = None

    write_json(books, json_file)

csv_filename = 'books.csv' 
json_filename = 'books.json' 

convert_csv_to_json(csv_filename, json_filename)
