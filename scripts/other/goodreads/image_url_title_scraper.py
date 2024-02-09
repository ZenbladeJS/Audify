# for goodreads website only

import requests
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/choiceawards/best-fiction-books-2023"

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

            print("Alt text:", alt_text)
            print("Image URL:", image_url)
            print()
        else:
            print("No image tag found in this div.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
