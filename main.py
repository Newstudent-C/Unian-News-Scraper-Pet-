import requests
from bs4 import BeautifulSoup
import pandas as pd

def parse_unian():
    url = 'https://www.unian.ua/science'
    
    # Mimic a real browser to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    print(f"Connecting to {url}...")
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check connection status
        if response.status_code != 200:
            print(f"Connection error: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all news items containers
        news_items = soup.find_all('div', class_='list-thumbs__item')
        print(f"News items found: {len(news_items)}")

        data_list = []

        for item in news_items:
            try:
                # 1. Extract Title
                title_tag = item.find('a', class_='list-thumbs__title')
                title = title_tag.text.strip() if title_tag else "No Title"

                # 2. Extract Timestamp
                time_tag = item.find('div', class_='list-thumbs__time')
                news_time = time_tag.text.strip() if time_tag else "No Time"

                # 3. Extract Image (Handle Lazy Loading)
                # 'data-src' usually holds the real image URL, 'src' is a placeholder
                img_tag = item.find('img')
                img_url = "No Image"
                if img_tag:
                    img_url = img_tag.get('data-src') or img_tag.get('src')

                # Append to list
                data_list.append({
                    'Title': title,
                    'Time': news_time,
                    'Image_URL': img_url
                })
            except Exception as e:
                print(f"Error processing item: {e}")

        # Save data to CSV
        if data_list:
            df = pd.DataFrame(data_list)
            # Use sep=';' for better compatibility with Excel in Europe/UA regions
            # encoding='utf-8-sig' fixes Cyrillic display issues
            df.to_csv('unian_science_news.csv', index=False, encoding='utf-8-sig', sep=';')
            print("Data successfully saved to 'unian_science_news.csv'")
        else:
            print("No data collected.")

    except Exception as e:
        print(f"Critical error: {e}")

if __name__ == '__main__':
    parse_unian()
