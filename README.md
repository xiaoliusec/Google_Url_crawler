# Google_Url_crawler

## 使用方法

```
>python3 Google_Url_Crawler.py -h
usage: Google_Url_Crawler.py [-h] -s SEARCH_TERM -n NUM

Google URL爬虫

options:
  -h, --help            show this help message and exit
  -s SEARCH_TERM, --search-term SEARCH_TERM
                        搜索关键词(注意：有空格要用引号引起来！)
  -n NUM, --num NUM     要爬取的页数
```

以"学校"为关键字搜索，爬取2页url链接

```
python3 Google_Url_Crawler.py -s 学校 -n 2
```

Google语法搜索

```
python3 Google_Url_Crawler.py -s "inurl:php?id=10" -n 3
```

```
python3 Google_Url_Crawler.py -s "inurl:php?id=10 上海" -n 3
```

```
python3 Google_Url_Crawler.py -s "site:baidu.com filetype:pdf" -n 3
```



