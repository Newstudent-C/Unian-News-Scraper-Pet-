import requests
from bs4 import BeautifulSoup
import pandas as pd


def parse_unian():
    url = 'https://www.unian.ua/science'

    # Маскуємося під звичайний браузер (Chrome), щоб сайт не блокував запит
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    print(f"Підключення до {url}...")

    try:
        response = requests.get(url, headers=headers)

        # Перевірка статусу (якщо не 200 - викине помилку)
        if response.status_code != 200:
            print(f"Помилка доступу: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')

        # Знаходимо контейнери новин
        news_items = soup.find_all('div', class_='list-thumbs__item')
        print(f"Знайдено новин: {len(news_items)}")

        data_list = []

        for item in news_items:
            try:
                # 1. Заголовок
                title_tag = item.find('a', class_='list-thumbs__title')
                title = title_tag.text.strip() if title_tag else "Без назви"

                # 2. Час публікації
                time_tag = item.find('div', class_='list-thumbs__time')
                news_time = time_tag.text.strip() if time_tag else "Без часу"

                # 3. Картинка (Пріоритет data-src через lazy loading)
                img_tag = item.find('img')
                img_url = "Немає фото"
                if img_tag:
                    img_url = img_tag.get('data-src') or img_tag.get('src')

                # Додаємо в список
                data_list.append({
                    'Заголовок': title,
                    'Час': news_time,
                    'Фото': img_url
                })
            except Exception as e:
                print(f"Помилка при обробці елемента: {e}")

        # Зберігаємо результат у файл
        if data_list:
            df = pd.DataFrame(data_list)
            # encoding='utf-8-sig' потрібен, щоб Excel коректно читав кирилицю
            df.to_csv('unian_science_news.csv', index=False, encoding='utf-8-sig', sep=';')
            print("Дані успішно збережено у файл 'unian_science_news.csv'")
        else:
            print("Список даних порожній.")

    except Exception as e:
        print(f"Критична помилка: {e}")


if __name__ == '__main__':
    parse_unian()