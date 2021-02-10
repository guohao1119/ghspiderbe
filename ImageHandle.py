import pytesseract


# 图片识别
def handleImage(image_obj):
    img = image_obj.convert("L")  # 转灰度
    pix_data = img.load()
    w, h = img.size
    threshold = 210  # 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pix_data[x, y] < threshold:
                pix_data[x, y] = 0
            else:
                pix_data[x, y] = 255
    return pytesseract.image_to_string(img)
