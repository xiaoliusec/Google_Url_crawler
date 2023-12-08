import requests
import argparse
from bs4 import BeautifulSoup


def get_search_results(query, page=0):
    url = f"https://www.google.com.hk/search?q={query}&newwindow=1&rlz=1C1GCEA_en__1035__1035&ei=ahyVZMPNF97mkPIPiYaTwAs&start={page}&sa=N&ved=2ahUKEwjDqtmGxNj_AhVeM0QIHQnDBLg4ChDy0wN6BAgCEAc&biw=1536&bih=714&dpr=1.25"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = [link.get('href') for link in soup.findAll('a', {'jscontroller': 'M9mgyc'}) if "google.com" not in link.get('href')]
    return links


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Google URL爬虫')
    parser.add_argument('-s', '--search-term', type=str, help='搜索关键词(注意：有空格要用引号引起来！)', required=True)
    parser.add_argument('-n', '--num', type=int, help='要爬取的页数', required=True)

    args = parser.parse_args()

    search_term = args.search_term
    query = requests.utils.quote(f'{search_term}')
    num = args.num

    with open('links.txt', 'w') as f:
        for i in range(0, num):
            links = get_search_results(query, page=i * 10)
            for link in links:
                f.write(link + '\n')

    print(f'所有链接已保存到 links.txt 文件中')