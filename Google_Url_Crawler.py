import requests
import argparse
from bs4 import BeautifulSoup


def get_search_results(query, page=0):
    """
    获取Google搜索结果中的链接

    Args:
        query: 搜索关键词(URL编码后)
        page: 页码偏移(0开始,每页10条结果)

    Returns:
        list: 搜索结果中的链接列表
    """
    # 构建Google搜索URL,page参数控制结果偏移量
    url = f"https://www.google.com.hk/search?q={query}&newwindow=1&rlz=1C1GCEA_en__1035__1035&ei=ahyVZMPNF97mkPIPiYaTwAs&start={page}&sa=N&ved=2ahUKEwjDqtmGxNj_AhVeM0QIHQnDBLg4ChDy0wN6BAgCEAc&biw=1536&bih=714&dpr=1.25"
    # 伪装为Chrome浏览器避免被拦截
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    # 发起HTTP请求,verify=False跳过SSL证书验证
    res = requests.get(url=url, headers=headers, verify=False, timeout=10)
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(res.text, 'html.parser')
    # 提取搜索结果链接(jsname='UWckNb'是Google搜索结果链接的特征)
    # 过滤掉google.com自身的链接
    links = [link.get('href') for link in soup.findAll('a', {'jsname': 'UWckNb'}) if "google.com" not in link.get('href')]
    return links


if __name__ == '__main__':
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Google URL爬虫')
    parser.add_argument('-s', '--search-term', type=str, help='搜索关键词(注意：有空格要用引号引起来！)', required=True)
    parser.add_argument('-n', '--num', type=int, help='要爬取的页数', required=True)

    args = parser.parse_args()

    search_term = args.search_term
    # 对搜索关键词进行URL编码(处理特殊字符和中文)
    query = requests.utils.quote(f'{search_term}')
    num = args.num

    # 打开输出文件,循环爬取指定页数的搜索结果
    with open('links.txt', 'w') as f:
        for i in range(0, num):
            # 每页10条结果,通过page参数控制偏移
            links = get_search_results(query, page=i * 10)
            # 逐条写入文件
            for link in links:
                f.write(link + '\n')

    print(f'所有链接已保存到 links.txt 文件中')
