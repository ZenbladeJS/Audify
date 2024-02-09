import requests
from bs4 import BeautifulSoup

# List of URLs for different categories
category_urls = {
    "Best Books 2023": "https://www.goodreads.com/choiceawards/best-books-2023",
    "Best Fiction": "https://www.goodreads.com/choiceawards/best-fiction-books-2023",
    "Best Historical Fiction": "https://www.goodreads.com/choiceawards/best-historical-fiction-books-2023",
    "Best Mystery & Thriller": "https://www.goodreads.com/choiceawards/best-mystery-thriller-books-2023",
    "Best Romance": "https://www.goodreads.com/choiceawards/best-romance-books-2023",
    "Best Romantasy": "https://www.goodreads.com/choiceawards/best-romantasy-books-2023",
    "Best Fantasy": "https://www.goodreads.com/choiceawards/best-fantasy-books-2023",
    "Best Science Fiction": "https://www.goodreads.com/choiceawards/best-science-fiction-books-2023",
    "Best Horror": "https://www.goodreads.com/choiceawards/best-horror-books-2023",
    "Best Young Adult Fantasy & Science Fiction": "https://www.goodreads.com/choiceawards/best-young-adult-fantasy-books-2023",
    "Best Young Adult Fiction": "https://www.goodreads.com/choiceawards/best-young-adult-fiction-books-2023",
    "Best Debut Novel": "https://www.goodreads.com/choiceawards/best-debut-novel-2023",
    "Best Nonfiction": "https://www.goodreads.com/choiceawards/best-nonfiction-books-2023",
    "Best Memoir & Autobiography": "https://www.goodreads.com/choiceawards/best-memoir-autobiography-books-2023",
    "Best History & Biography": "https://www.goodreads.com/choiceawards/best-history-biography-books-2023",
    "Best Humor": "https://www.goodreads.com/choiceawards/best-humor-books-2023",
}

# Dictionary to store book information
book_dict = {}

with open("scraped_results.txt", "w", encoding="utf-8") as file:
    for category, url in category_urls.items():
        file.write(f"Scraping data for category: {category}\n")

        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            div_containers = soup.find_all('div', class_='answerWrapper')

            for div_container in div_containers:
                img_tag = div_container.find('img')

                if img_tag:

                    alt_text = img_tag.get('alt')
                    image_url = img_tag.get('src')
                    book_info = alt_text.split(" by ")
                    book_name = book_info[0].strip()
                    author_name = book_info[1].strip() if len(book_info) > 1 else ""

                    if category not in book_dict:
                        book_dict[category] = []
                    
                    book_dict[category].append({
                        "Book Name": book_name,
                        "Author": author_name,
                        "ImageURL": image_url
                    })

                    file.write(f"Book Name: {book_name}\n")
                    file.write(f"Author Name: {author_name}\n")
                    file.write(f"Image URL: {image_url}\n\n")

                else:
                    file.write("No image tag found in this div.\n")

            file.write("-------------------------------------------\n")
        else:
            file.write(f"Failed to retrieve the webpage for category {category}. Status code: {response.status_code}\n")

print("Book Dictionary:")
for category, books in book_dict.items():
    print(f"Category: {category}")
    for book in books:
        print(f"Book Name: {book['Book Name']}")
        print(f"Author: {book['Author']}")
        print(f"Image URL: {book['ImageURL']}")
        print("-------------------------------------------")
