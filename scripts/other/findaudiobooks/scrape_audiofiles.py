import requests
from bs4 import BeautifulSoup

url = "https://findaudiobook.co/dragon-tears-audiobook-by-dean-koontz/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    audio_tag = soup.find('audio', class_='wp-audio-shortcode')

    if audio_tag:
        source_tag = audio_tag.find('source')
        
        if source_tag:
            source_link = source_tag['src']
            print("Audio Source Link:", source_link)
        else:
            print("Source tag not found within the audio tag.")

    else:
        print("Audio tag not found on the page.")

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
