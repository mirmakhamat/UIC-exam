import requests
import bs4


def search_news(query, count=10):
    """
    search news by query from kun.uz
    """
    news = []
    url = f'https://kun.uz/news/search?q={query}'
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    news_list = soup.select(".news")

    if not news_list:
        return []

    for i in range(count):
        try:
            title = news_list[i].select_one('.news__title').text.strip()
            date = news_list[i].select_one('.news-meta span').text.strip()
            link = news_list[i].select_one('.news__title').get('href')
        except IndexError:
            break

        news.append({'title': title, 'date': date, 'link': link})

    return news
