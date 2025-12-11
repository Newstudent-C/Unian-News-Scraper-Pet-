# Unian Science News Scraper 🔬

A robust Python script designed to scrape the latest science and technology news from [Unian.ua](https://www.unian.ua/science).

This tool automates the process of data collection, handling dynamic image loading, and exporting the data into an Excel-friendly format.

## 🚀 Key Features

* **Smart Parsing:** Extracts news titles, publication timestamps, and preview image URLs.
* **Lazy Loading Handler:** Correctly identifies and retrieves images hidden behind lazy loading attributes (`data-src`), ignoring low-quality placeholders.
* **Excel-Ready Export:** Saves data to `.csv` using a semicolon (`;`) separator and `utf-8-sig` encoding. This ensures Cyrillic characters are displayed correctly in Microsoft Excel without additional configuration.
* **Anti-Bot Protection:** Utilizes custom `User-Agent` headers to mimic real browser behavior and avoid 403 Forbidden errors.

## 🛠️ Tech Stack

* **Python 3.x**
* **Requests:** For handling HTTP requests.
* **BeautifulSoup4:** For parsing HTML structure.
* **Pandas:** For data manipulation and CSV export.

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Unian-News-Scraper.git](https://github.com/your-username/Unian-News-Scraper.git)
    cd Unian-News-Scraper
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♂️ Usage

Run the script via terminal:

```bash
python main.py
