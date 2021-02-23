import json
import os
import shutil
import urllib
import zipfile
from urllib.parse import quote

from bs4 import BeautifulSoup


# 压缩指定文件夹
def zip_dir(dir_path, out_name):
    dir_path = os.getcwd() + dir_path
    zip = zipfile.ZipFile(out_name, 'w', zipfile.ZIP_DEFLATED)
    for path, dirname, filenames in os.walk(dir_path):
        fpath = path.replace(dir_path, '')
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


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
    request = urllib.request.Request(quote(url, safe=";/?:@&=+$,", encoding="utf-8"), headers=head)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    return html


# 如果第三方页面是通过接口获取数据，则直接请求接口, post请求
def postRawData(url):
    head = {  # 模拟代理
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36 '
    }
    data = {}
    data = json.dumps(data)
    data = bytes(data, 'utf8')
    request = urllib.request.Request(url, data=data, headers=head, method='POST')
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    return html
