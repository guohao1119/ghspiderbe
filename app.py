import json
import urllib.error  # 指定URL，获取网页数据
import urllib.request
import re  # 正则表达式
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 获取最新电影排行
@app.route('/movielist')
def movielist():
    html = getRawHtml('https://movie.douban.com/cinema/nowplaying')
    datalist = []
    for item in html.find_all('li', class_='list-item'):
        datalist.append({
            'title': item.get('data-title'),
            'rate': item.get('data-score')
        })
    result = {'data': datalist}
    return result

# 获取最新电视剧排行
@app.route('/tvlist')
def tvlist():
    return getRawData('https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0')


# 获取电影电视轮播列表
@app.route('/sliderdatalist')
def slider_data_list():
    html = getRawHtml('https://movie.douban.com/cinema/nowplaying')
    datalist = []
    for item in html.find_all('li', class_='list-item'):
        datalist.append({
            'img_url': item.find('img').get('src')
        })
        if len(datalist) == 10:
            break
    tv_data = getRawData('https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0')
    tv_data = json.loads(tv_data)
    for item in tv_data['subjects']:
        datalist.append({
            'img_url': item['cover']
        })
        if len(datalist) == 20:
            break
    result = {'data': datalist}
    return result


# 获取微博热门排行
@app.route('/weibolist')
def weibolist():
    html = getRawHtml('https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6')
    datalist = []
    for item in html.find_all('tr', class_=''):
        print(item)
        title = item.find('td', class_='td-02').find('a')
        rate = item.find('td', class_='td-03').find('i')
        if title:
            title = title.string
        if rate:
            rate = rate.string
        datalist.append({
            'title': title,
            'rate': rate
        })
    datalist.pop(0)
    result = {'data': datalist}
    return result


# 获取知乎日报
@app.route('/zhihulist')
def zhihulist():
    html = getRawHtml('https://daily.zhihu.com/')
    datalist = []
    for item in html.find_all('div', class_='box'):
        datalist.append({'title': item.find('span').string})
    return {'data': datalist}


# 获取掘金列表
@app.route('/juejinlist', methods=['post'])
def juejinlist():
    data = postRawData('https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed')
    data = json.loads(data)['data']
    datalist = []
    for item in data:
        if item['item_type'] == 2:
            datalist.append({'title': item['item_info']['article_info']['title']})
        elif item['item_type'] == 14:
            datalist.append({'title': item['item_info']['title']})
    return {'data': datalist}


# 获取网页html源码
def getRawHtml(url):
    head = {  # 模拟代理
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36 '
    }
    request = urllib.request.Request(url, headers=head)

    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        html = BeautifulSoup(html, 'html.parser')
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


# 如果第三方页面是通过接口获取数据，则直接请求接口, get请求
def getRawData(url):
    head = {  # 模拟代理
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36 '
    }
    request = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    return html


# 如果第三方页面是通过接口获取数据，则直接请求接口, post请求
def postRawData(url):
    head = {  # 模拟代理
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36 '
    }
    data = {
        'a': '1'
    }
    data = json.dumps(data)
    data = bytes(data, 'utf8')
    request = urllib.request.Request(url, data=data, headers=head, method='POST')
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    return html

# 根据指定正则获取数据
# def findData(exp, data):
#     info = re.findall(exp, data)
#     if len(info) > 0:
#         return info[0]
#     return ''


if __name__ == '__main__':
    app.run()
