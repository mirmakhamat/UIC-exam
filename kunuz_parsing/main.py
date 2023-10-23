import requests
import bs4


def get_last_news(count=10):
    """
    get last news from kun.uz 
    """
    news = []
    url = 'https://kun.uz/news/list'
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    news_list = soup.select("a.daily-block")

    if not news_list:
        return []

    for i in range(count):
        try:
            title = news_list[i].select_one('.news-title').text.strip()
            date = news_list[i].select_one('.news-date').text.strip()
            link = news_list[i].get('href')
        except IndexError:
            break

        news.append({'title': title, 'date': date, 'link': link})
    return news


def main():
    news = get_last_news()
    print(news)


if __name__ == '__main__':
    main()
