import csv

def read_csv(csv_file):
    
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)
