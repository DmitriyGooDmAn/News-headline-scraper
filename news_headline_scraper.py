import requests
from bs4 import BeautifulSoup
import time

def scrape_news_headlines(url):
    start_time = time.time()  # Record the start time

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check the success of the request
    if response.status_code == 200:
        
        # Use BeautifulSoup for HTML parsing
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find news headlines
        headlines = soup.find_all('h2')

        # Display the headlines
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline.text}")

        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        print(f"\nProgram execution time: {elapsed_time:.4f} seconds")

    else:
        print(f"Error retrieving the page. Error code: {response.status_code}")

# Replace the URL with the news site you want to use
news_url = 'https://www.technewsworld.com/'
scrape_news_headlines(news_url)

