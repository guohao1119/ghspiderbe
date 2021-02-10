import webbrowser
from selenium import webdriver
from PIL import Image
from ImageHandle import handleImage

co = webdriver.ChromeOptions()
co.headless = True


def search_zxgk(company_name):
    # browser = webdriver.Chrome(options=co)
    browser = webdriver.Chrome()
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
    browser.save_screenshot('pictures.png')
    page_snap_obj = Image.open('pictures.png')
    location = captcha_img.location
    size = captcha_img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    return page_snap_obj.crop((left, top, right, bottom))