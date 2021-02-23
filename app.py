import json
import os
import threading
from flask import Flask, request, send_from_directory, send_file

from utils.infosearch import search_zxgk, search_credit_china, search_gsxt, search_china_tax, search_mem, search_mee, search_miit, search_safe, search_cbirc, search_pbc, search_ndrc, search_nmpa, search_csrc, search_stats, search_mofcom, search_samr, search_ccgp, search_moa, search_customs, search_mohurd, search_mof, get_browser
from utils.utils import zip_dir, getRawHtml, postRawData, getRawData, del_file

app = Flask(__name__)


# 信息查询接口
@app.route('/info_search')
def info_search():
    del_file('result')
    company_name = request.args.get('companyName')
    file_name_arr = []
    search_credit_china(company_name, file_name_arr)
    # search_arr = [
    #     # return search_zxgk(company_name)
    #     # return search_gsxt(company_name)
    #     # return search_nmpa(company_name)
    #     # return search_customs(company_name)
    #     # return search_credit(company_name)
    #
    #     search_credit_china
    #     # search_pbc,
    #     # search_mem,
    #     # search_mee,
    #     # search_miit,
    #     # search_safe,
    #     # search_cbirc,
    #     # search_ndrc,
    #     # search_csrc,
    #     # search_stats,
    #     # search_mofcom,
    #     # search_samr,
    #     # search_ccgp,
    #     # search_moa,
    #     # search_mohurd,
    #     # search_mof,
    #     # search_china_tax
    # ]
    # threads = []
    # file_name_arr = []
    #
    # for item in search_arr:
    #     threads.append(threading.Thread(target=item, args=(company_name, file_name_arr)))
    #
    # threads_count = range(len(threads))
    # for index in threads_count:
    #     threads[index].start()
    # for index in threads_count:
    #     threads[index].join()
    # print('线程执行结束')
    # zip_dir('/result', os.getcwd() + '/zip/all.zip')
    return {
        'code': 0,
        'data': file_name_arr
    }


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
            'rate': item.get('data-score'),
            'poster': item.find('img').get('src')
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


@app.route('/download')
def download():
    directory = os.getcwd()
    filename = request.values.get('filepath')
    return send_from_directory(directory, filename, as_attachment=True)


@app.route('/download_zip')
def download_zip():
    return send_file('zip/all.zip', mimetype='zip', attachment_filename='all.zip', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
