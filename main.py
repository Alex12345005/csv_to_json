import pandas as pd

data = pd.read_csv('books.csv')

data['ISBN'] = None
data['Bewertung'] = None

json_data = data.to_json(orient='records', force_ascii=False, indent=4)

with open('conv_json.json', 'w', encoding='utf-8') as conv_json:
    conv_json.write(json_data)