import requests

def perform_book_search(search_term):
    api_url = f"https://www.googleapis.com/books/v1/volumes?q={search_term}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()

        items = data.get('items', [])
        
        for item in items:
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', '')
            authors = volume_info.get('authors', [])
            publisher = volume_info.get('publisher', '')

            print(f"Title: {title}, Authors: {', '.join(authors)}, Publisher: {publisher}")

    else:
        print(f"Error: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    perform_book_search("python programming")
