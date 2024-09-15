import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape articles from a sample news website
def scrape_articles(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []

    # Example: Scraping article titles and publication dates
    for article in soup.find_all('div', class_='article'):
        title = article.find('h2').text.strip()
        date = article.find('time').get('datetime')
        articles.append({
            'title': title,
            'date': date
        })

    return articles

# Function to save data to a CSV file
def save_to_csv(articles, filename):
    keys = articles[0].keys() if articles else ['title', 'date']
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(articles)

    print(f"Data saved to {filename}")

# Analyze data: For example, find the most recent article
def analyze_articles(articles):
    if not articles:
        print("No articles to analyze.")
        return

    # Find the most recent article
    articles_sorted = sorted(articles, key=lambda x: x['date'], reverse=True)
    latest_article = articles_sorted[0]
    print(f"Most recent article: {latest_article['title']} on {latest_article['date']}")

def main():
    url = "https://example.com/news"  # Replace with actual URL
    articles = scrape_articles(url)

    if articles:
        save_to_csv(articles, 'articles.csv')
        analyze_articles(articles)
    else:
        print("No articles found or scraping failed.")

if __name__ == "__main__":
    main()
