import webbrowser
from selenium import webdriver
from PIL import Image
from ImageHandle import handleImage


# 查询中国执行信息公开网（http://zxgk.court.gov.cn/shixin/）
def search_zxgk(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://zxgk.court.gov.cn/shixin/')
    browser.maximize_window()
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
    browser.save_screenshot('./result/zxgk.png')
    return {'code': 0, 'img_url': 'url'}


def get_check_code(browser, captcha_img):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.save_screenshot('pictures.png')
    page_snap_obj = Image.open('pictures.png')
    location = captcha_img.location
    size = captcha_img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    return page_snap_obj.crop((left, top, right, bottom))


# 查询信用中国网站（https://www.creditchina.gov.cn/）
def search_credit_china(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('https://www.creditchina.gov.cn/')
    # 公司名称输入框
    search_input = browser.find_element_by_id('search_input')
    search_input.send_keys(company_name)

    # 查询按钮
    search_btn = browser.find_element_by_class_name('search_btn')
    search_btn.click()

# 查询国家企业信用信息公示系统http://www.gsxt.gov.cn/
def search_gsxt(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.gsxt.gov.cn/')
    # 公司名称输入框
    keyword = browser.find_element_by_id('keyword')
    keyword.send_keys(company_name)
    # 查询按钮
    btn_query = browser.find_element_by_id('btn_query')
    btn_query.click()


# 查询国家税务总局 http://www.chinatax.gov.cn
def search_china_tax(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.chinatax.gov.cn')

    # # 公司名称输入框
    # ipt_sword = browser.find_element_by_id('iptSword')
    # ipt_sword.send_keys(company_name)
    # # 查询按钮
    # btn_query = browser.find_element_by_id('btn_query')
    # btn_query.click()
    return company_name


# 查询应急管理部网站 http://www.mem.gov.cn/
def search_mem(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.mem.gov.cn')
    # 公司名称输入框
    ipt_sword = browser.find_element_by_id('iptSword')
    ipt_sword.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_id('query_btn')
    query_btn.click()
    return ''


# 中华人民共和国生态环境部网站 http://www.mee.gov.cn
def search_mee(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.mee.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_id('searchword')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('searchSubmit2')
    query_btn.click()
    return ''


# 中华人民共和国工业和信息化部网站（http://www.miit.gov.cn/）
def search_miit(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.miit.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_id('q')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_id('user-defined02')
    query_btn.click()
    return ''


# 国家外汇管理局网站（http://www.safe.gov.cn/）
def search_safe(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.safe.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_id('title')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('btn')
    query_btn.click()
    return ''


# 中国银保监会网站（http://www.cbirc.gov.cn）
def search_cbirc(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.cbirc.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_id('search')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_id('goJiansuo')
    query_btn.click()
    return ''


# 中国人民银行网站（http://www.pbc.gov.cn/）
def search_pbc(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.pbc.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_id('q')
    search_word.send_keys(company_name)
    # 查询按钮
    # query_btn = browser.find_element_by_id('goJiansuo')
    # query_btn.click()
    return ''


# 国家发改委网站（https://www.ndrc.gov.cn/）
def search_ndrc(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.ndrc.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_id('qt')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('btn_search1')
    query_btn.click()
    return ''


# 中国证监会网站（http://www.csrc.gov.cn/pub/newsite/）
def search_csrc(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.csrc.gov.cn/pub/newsite/')
    # 公司名称输入框
    search_word = browser.find_element_by_id('schword')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('so_btn')
    query_btn.click()
    return ''


# 国家食品药品监督管理总局网站（http://www.nmpa.gov.cn/）
def search_nmpa(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.nmpa.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_id('qt')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_id('sosbtn')
    query_btn.click()
    return ''


# 国家市场监督管理总局（http://www.samr.gov.cn/）
def search_samr(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.samr.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_id('qt')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('search_btn')
    query_btn.click()
    return ''


# 中华人民共和国住房和城乡建设部网站（http://www.mohurd.gov.cn/）
def search_mohurd(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.mohurd.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_name('query')
    search_word.send_keys(company_name)
    # 查询按钮
    # query_btn = browser.find_element_by_class_name('search_btn')
    # query_btn.click()
    return ''


# 中华人民共和国海关总署网站（http://www.customs.gov.cn/）
def search_customs(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.customs.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_class_name('SearchTextBox')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('searchBtn')
    query_btn.click()
    return ''


# 中国海关企业进出口信用信息公示平台（http://credit.customs.gov.cn/）
def search_credit(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://credit.customs.gov.cn/')
    # 公司名称输入框
    search_word = browser.find_element_by_id('ID_codeName')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_class_name('serch_ico1')
    query_btn.click()
    return ''


# 中华人民共和国农业农村部网站（http://www.moa.gov.cn/）
def search_moa(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.moa.gov.cn')
    # 公司名称输入框
    search_word = browser.find_element_by_name('searchword')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_id('search_btn')
    query_btn.click()
    return ''


# 中华人民共和国财政部网站（http://www.mof.gov.cn/index.htm）
def search_mof(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.mof.gov.cn/index.htm')
    # 公司名称输入框
    search_word = browser.find_element_by_id('andsen')
    search_word.send_keys(company_name)
    # 查询按钮
    # query_btn = browser.find_element_by_id('search_btn')
    # query_btn.click()
    return ''


# 中国政府采购网（http://www.ccgp.gov.cn/）
def search_ccgp(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.ccgp.gov.cn/')
    # 公司名称输入框
    search_word = browser.find_element_by_id('kw')
    search_word.send_keys(company_name)
    # 查询按钮
    query_btn = browser.find_element_by_id('doSearch2')
    query_btn.click()
    return ''


# 中华人民共和国商务部网站（http://www.mofcom.gov.cn/）
def search_mofcom(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.mofcom.gov.cn/')
    # 公司名称输入框
    search_word = browser.find_element_by_id('searchValue')
    search_word.send_keys(company_name)
    # 查询按钮
    # query_btn = browser.find_element_by_id('doSearch2')
    # query_btn.click()
    return ''


# 中华人民共和国国家统计局网站（http://www.stats.gov.cn/）
def search_stats(company_name):
    browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
    browser.get('http://www.stats.gov.cn/')
    # 公司名称输入框
    search_word = browser.find_element_by_id('search')
    search_word.send_keys(company_name)
    # 查询按钮
    # query_btn = browser.find_element_by_id('doSearch2')
    # query_btn.click()
    return ''