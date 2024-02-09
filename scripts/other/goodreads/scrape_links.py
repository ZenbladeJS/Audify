import requests
from bs4 import BeautifulSoup

url = 'https://www.goodreads.com/'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    link_dict = {}
    div_containers = soup.find_all('div', class_='gr-listOfLinks u-defaultType')
    
    for div in div_containers:
        links = div.find_all('a', class_='gr-hyperlink')
        for link in links:
            link_text = link.get_text(strip=True)
            link_url = link['href']
            full_url = f"https://www.goodreads.com{link_url}"
            link_dict[link_text] = full_url

    for link_text, link_url in link_dict.items():
        print(f"\"{link_text}\": \"{link_url}\",")
else:
    print(f"Failed to fetch the URL. Status code: {response.status_code}")
