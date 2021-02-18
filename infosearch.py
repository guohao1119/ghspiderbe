import platform
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
from ImageHandle import handleImage

system = platform.system()
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('lang=zh_CN.UTF-8')
# chrome_options.add_argument('Referer=https://www.nmpa.gov.cn1/')
# chrome_options.add_argument('sec-ch-ua="Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"')


# 查询中国执行信息公开网（http://zxgk.court.gov.cn/shixin）
def search_zxgk(company_name):
    browser = get_browser()
    browser.get('http://zxgk.court.gov.cn/shixin')
    # 被执行人姓名/名称
    p_name = browser.find_element_by_id('pName')
    # 验证码输入框
    yzm = browser.find_element_by_id('yzm')
    # 验证码图片
    captcha_img = browser.find_element_by_id('captchaImg')
    # 查询按钮
    search_btn = browser.find_element_by_class_name('btn-zxgk')
    image_obj = get_check_code(browser, captcha_img)
    # 提取验证码中的字符
    image_str = handleImage(image_obj)
    if len(image_str) != 4:
        image_str = '1234'

    # 在输入框中输入内容
    p_name.send_keys(company_name)
    yzm.send_keys(image_str)
    search_btn.click()
    # 查询结果
    result_text = browser.find_element_by_id('tbody-result')
    print('result_text', result_text.text)
    # tip = result_text.find_element_by_tag_name('span')
    #
    # print(tip)
    # print('aa', tip.text)
    browser.execute_script('window.scrollBy(0, 200)')
    browser.save_screenshot('./result/中国执行信息公开网查询.png')
    return {'code': 0, 'img_url': 'url'}


def get_check_code(browser, captcha_img):
    browser.save_screenshot('pictures.png')
    page_snap_obj = Image.open('pictures.png')
    location = captcha_img.location
    size = captcha_img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    return page_snap_obj.crop((left, top, right, bottom))


# 查询信用中国网站（https://www.creditchina.gov.cn）
def search_credit_china(company_name):
    browser = get_browser()
    browser.get('https://www.creditchina.gov.cn')
    # 公司名称输入框
    search_input = browser.find_element_by_id('search_input')
    search_input.send_keys(company_name)

    # 查询按钮
    search_btn = browser.find_element_by_class_name('search_btn')
    search_btn.click()


# 查询国家企业信用信息公示系统 http://www.gsxt.gov.cn
def search_gsxt(company_name):
    browser = get_browser()
    browser.get('http://www.gsxt.gov.cn')
    # 公司名称输入框
    keyword = browser.find_element_by_id('keyword')
    keyword.send_keys(company_name)
    # 查询按钮
    btn_query = browser.find_element_by_id('btn_query')
    btn_query.click()


# 查询国家税务总局 http://www.chinatax.gov.cn/s
def search_china_tax(company_name):
    browser = get_browser()
    browser.get('http://www.chinatax.gov.cn/s')

    # 公司名称输入框
    search_word = browser.find_element_by_id('qt')
    search_word.send_keys(company_name)
    # 查询按钮
    btn_query = browser.find_element_by_id('searchBtn')
    btn_query.click()
    file_name = '国家税务总局网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 查询应急管理部网站 http://www.mem.gov.cn
def search_mem(company_name):
    browser = get_browser()
    website = 'https://www.mem.gov.cn/was5/web/sousuo/index.html?sw='
    website = website + company_name + '&date1=&date2=&stype=0'
    browser.get(website)
    file_name = '应急管理部网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中华人民共和国生态环境部网站 http://www.mee.gov.cn
def search_mee(company_name):
    browser = get_browser()
    browser.get('http://www.mee.gov.cn/qwjs2019/?searchword=' + company_name)
    file_name = '生态环境部网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中华人民共和国工业和信息化部网站（http://www.miit.gov.cn）
def search_miit(company_name):
    browser = get_browser()
    locator = (By.CLASS_NAME, 'yyfw')
    try:
        browser.get('https://www.miit.gov.cn/search/index.html?websiteid=110000000000000&q=' + company_name)
        # 等待搜索结果出现后再截图
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))
        file_name = '工业和信息化部网站查询结果'
        browser.save_screenshot('./result/' + file_name + '.png')
    except Exception as e:
        print(e)
    return file_name


# 国家外汇管理局网站（http://www.safe.gov.cn）
def search_safe(company_name):
    browser = get_browser()
    browser.get('http://www.safe.gov.cn/safe/search/index.html?q=' + company_name + '&siteid=safe&order=releasetime')
    file_name = '国家外汇管理局网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中国银保监会网站（http://www.cbirc.gov.cn）
def search_cbirc(company_name):
    browser = get_browser()
    browser.get('http://www.cbirc.gov.cn/cn/view/pages/index/jiansuo.html?keyWords=' + company_name)
    file_name = '中国银保监会网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中国人民银行网站（http://www.pbc.gov.cn）
def search_pbc(company_name):
    browser = get_browser()
    browser.get('http://wzdig.pbc.gov.cn:8080/search/pcRender?pageId=fa445f64514c40c68b1c8ffe859c649e')
    # 公司名称输入框
    search_word = browser.find_element_by_id('q')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('search_btn')
    query_btn.click()
    file_name = '中国人民银行网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 国家发改委网站（https://www.ndrc.gov.cn）
def search_ndrc(company_name):
    browser = get_browser()
    browser.get('https://so.ndrc.gov.cn/s?siteCode=bm04000007&ssl=1&token=&qt=' + company_name)
    file_name = '国家发改委网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中国证监会网站（http://www.csrc.gov.cn/pub/newsite）
def search_csrc(company_name):
    browser = get_browser()
    browser.get('http://www.csrc.gov.cn/pub/newsite/')
    # 公司名称输入框
    search_word = browser.find_element_by_id('schword')
    search_word.clear()
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('so_btn')
    query_btn.click()
    file_name = '中国证监会网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 国家食品药品监督管理总局网站（http://www.nmpa.gov.cn）
def search_nmpa(company_name):
    browser = get_browser()
    browser.get('http://www.nmpa.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_id('qt')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_id('sosbtn')
    query_btn.click()
    file_name = '国家食品药品监督管理总局网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中华人民共和国国家统计局网站（http://www.stats.gov.cn）
def search_stats(company_name):
    browser = get_browser()
    browser.get('http://www.stats.gov.cn/was5/web/search?channelid=288041&andsen=' + company_name)
    # 公司名称输入框
    search_word = browser.find_element_by_id('search')
    search_word.send_keys(company_name)
    file_name = '国家统计局网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中华人民共和国商务部网站（http://www.mofcom.gov.cn）
def search_mofcom(company_name):
    browser = get_browser()
    try:
        browser.get('http://search.mofcom.gov.cn/swb/swb_search/searchList_main.jsp')
        # 公司名称输入框
        search_word = browser.find_element_by_id('searchValue')
        search_word.send_keys(company_name)
        # 查询按钮
        query_div = browser.find_element_by_class_name('st-input')
        query_btn = query_div.find_element_by_tag_name('span')
        query_btn.click()
        # 等待搜索结果出现后再截图
        locator = (By.CLASS_NAME, 'search-result-row')
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(locator))
        file_name = '商务部网站查询结果'
        browser.save_screenshot('./result/' + file_name + '.png')
    except Exception as e:
        print(e)
    return file_name


# 国家市场监督管理总局（http://www.samr.gov.cn）
def search_samr(company_name):
    browser = get_browser()
    browser.get('http://www.samr.gov.cn/search4/s?searchWord=' + company_name + '&x=12&y=10&column=全部&siteCode=bm30000012')
    file_name = '市场监督管理总局网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中国政府采购网（http://www.ccgp.gov.cn）
def search_ccgp(company_name):
    browser = get_browser()
    website = 'http://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index=1&timeType=2&searchchannel=0&kw='
    browser.get(website + company_name + '&bidSort=0&pinMu=0&bidType=0')
    file_name = '中国政府采购网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中华人民共和国农业农村部网站（http://www.moa.gov.cn/）
def search_moa(company_name):
    browser = get_browser()
    website = 'http://www.moa.gov.cn/was5/web/search?searchword='
    browser.get(website + company_name + '&channelid=233424&prepage=10&orderby=-DOCRELTIME')
    browser.save_screenshot('./result/.png')
    file_name = '农业农村部网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中华人民共和国海关总署网站（http://www.customs.gov.cn/）
def search_customs(company_name):
    browser = get_browser()
    browser.get('http://search.customs.gov.cn/search/pcRender?pageId=f5261418ddc74f03b27e3590c531102b')
    # 公司名称输入框
    search_word = browser.find_element_by_id('q')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('search_btn')
    query_btn.click()
    file_name = '海关总署网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中华人民共和国住房和城乡建设部网站（http://www.mohurd.gov.cn/）
def search_mohurd(company_name):
    browser = get_browser()
    try:
        browser.get('http://search.mohurd.gov.cn')
        # 公司名称输入框
        search_word = browser.find_element_by_class_name('search-input__ele')
        search_word.send_keys(company_name)
        # 查询按钮
        query_btn = browser.find_element_by_class_name('search-button__ele')
        query_btn.click()
        locator = (By.CLASS_NAME, 'loading-message')
        # 等待搜索结果出现后再截图
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located(locator))
        file_name = '住房和城乡建设部网站查询结果'
        browser.save_screenshot('./result/' + file_name + '.png')
    except Exception as e:
        print(e)
    return file_name


# 中国海关企业进出口信用信息公示平台（http://credit.customs.gov.cn/）
def search_credit(company_name):
    browser = get_browser()
    browser.get('http://credit.customs.gov.cn/')
    # 公司名称输入框
    search_word = browser.find_element_by_id('ID_codeName')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('serch_ico1')
    query_btn.click()
    file_name = '海关企业进出口信用信息公示平台网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 中华人民共和国财政部网站（http://www.mof.gov.cn/index.htm）
def search_mof(company_name):
    browser = get_browser()
    browser.get('http://www.mof.gov.cn/index.htm')
    # 公司名称输入框
    search_word = browser.find_element_by_id('andsen')
    search_word.send_keys(company_name)
    # 查询按钮
    query_form = browser.find_element_by_id('searchform')
    query_btn = query_form.find_element_by_tag_name('a')
    query_btn.click()
    browser.switch_to.window(browser.window_handles[1])
    file_name = '财政部网站查询结果'
    browser.save_screenshot('./result/' + file_name + '.png')
    return file_name


# 根据不同操作系统获取浏览器
def get_browser():
    print(chrome_options)
    if system == 'Windows':
        browser = webdriver.Chrome(chrome_options=chrome_options)
    elif system == 'Darwin':
        browser = webdriver.Chrome(executable_path=r'/usr/local/bin/chromedriver', chrome_options=chrome_options)
    browser.maximize_window()
    return browser
