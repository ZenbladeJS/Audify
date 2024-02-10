import json
import csv
from urllib.parse import quote

with open('data.json', 'r') as file:
    books_data = json.load(file)

base_url = 'https://findaudiobook.co/?s='

with open('books_info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Author', 'Audiobook_URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for key, item in books_data['items'].items():
        book_info = item['info']
        book_title = book_info['Title']
        book_author = book_info['Author']
        encoded_title = quote(book_title).replace("%20", "+")
        search_url = base_url + encoded_title

        writer.writerow({'Title': book_title, 'Author': book_author, 'Audiobook_URL': search_url})