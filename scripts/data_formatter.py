import json
import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(filename='info.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

base_url = "https://thegreatestbooks.org/"

def scrape_book_data(book_number):
    url = base_url + f"books/{book_number}"
    response = requests.get(url)
    
    try:

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            # First anchor tag on the website is the book title
            title_anchor = soup.find("h1").find("a")
            title = title_anchor.text.strip()
            
            # Second anchor tag on the website is the author's name
            author_anchor = soup.find("h1").find_all("a")[1]
            author = author_anchor.text.strip()
            
            # Extract summary from paragraph tag
            summary_paragraph = soup.find("div", class_="ps-3").find("p")
            summary = summary_paragraph.text.strip()
            
            # Extract image
            image_tag = soup.find("div", class_="me-3").find("img")
            image_link = image_tag['src']

            # Publish year can be found in the sidebar-content
            details_section = soup.find("div", class_="sidebar-content")
            year_published = details_section.find(text="Year Published").find_next("dd").text.strip()
            
            # Extract genres
            genres = []
            genres_div = soup.find("div", class_="sidebar-content").find_all("div", class_="align-items-center mt-2 mb-2")[1]
            genre_anchors = genres_div.find_all("a")
            for anchor in genre_anchors:
                genre_text = anchor.text.strip()
                genre_href = "https://thegreatestbooks.org" + anchor['href']
                genres.append((genre_text, genre_href))

            # Dictionary for containing scraped data
            book_data = {
                "ID": book_number,
                "Title": title,
                "Author": author,
                "Summary": summary,
                "Image Link": image_link,
                "Year Published": year_published,
                "Genres": genres
            }

            return book_data

        else:
            logging.warning(f'Failed to fetch data for book {book_number}')
            print(f'Failed to fetch data for book {book_number}')
            return None

    except Exception as e:
        logging.error(f'An error occured while scraping data for book {book_number}: {e}')
        return None

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

scraped_data = []

for i in range(1, 10474):
    book_data = scrape_book_data(i)
    if book_data:
        scraped_data.append(book_data)
        logging.info(f'Data for book {i} successfully scraped and dumped.')
        print(f'Data for book {i} successfully scraped and dumped.')

save_to_json(scraped_data, 'books.json')
