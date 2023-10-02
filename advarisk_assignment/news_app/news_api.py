import requests
from datetime import datetime

NEWS_API_KEY = 'b9cd7dd983ef460caa6978335aa402a6'
NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything'


def fetch_news(keyword):
    params = {
        'q': keyword,
        'apiKey': NEWS_API_KEY,
    }

    response = requests.get(NEWS_API_BASE_URL, params=params)

    if response.status_code == 200:
        articles = response.json().get('articles', [])

        # Extract relevant information from each article
        search_results = []
        for article in articles:
            title = article.get('title', 'N/A')
            url = article.get('url', '#')
            date_published_str = article.get('publishedAt', '')
            date_published = parse_date(date_published_str)

            result = {
                'title': title,
                'url': url,
                'date': date_published,
            }
            search_results.append(result)

        return search_results
    else:
        # Handle API request error
        print(f"Error fetching news. Status code: {response.status_code}")
        return []


def parse_date(date_str):
    # Parse date string to a datetime object
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return None
