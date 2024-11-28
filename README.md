# Google_Url_crawler

## 注意事项

如抓取不到链接，google搜索任意关键字，查看元素，修改a标签的属性
<img width="1185" alt="image" src="https://github.com/user-attachments/assets/b64bc88f-e355-40a6-946f-d63eb595cbd5">
<img width="999" alt="image" src="https://github.com/user-attachments/assets/ab5b7f89-a15b-4ce5-9945-f9b90a0ee606">

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



