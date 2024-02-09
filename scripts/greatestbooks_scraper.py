import requests
from bs4 import BeautifulSoup

base_url = "https://thegreatestbooks.org/"

def scrape_book_data(book_number):
    url = base_url + f"books/{book_number}"
    response = requests.get(url)
    
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

        # Publish year can be founded in the sidebar-content
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

        print(f"\n")
        print(f"Scraped data for book {book_number}:")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Summary: {summary}")
        print(f"Image link: {image_link}")
        print(f"Year Published: {year_published}")
        print(f"Genres:")
        for genre_text in genres:
            print(f"{genre_text}")
        print(f"\n")
        print(f"------------------------------------")

    else:
        print(f"Failed to fetch data for book {book_number}")

# Loop through book numbers and scrape data
for i in range(1, 10474):
    scrape_book_data(i)
