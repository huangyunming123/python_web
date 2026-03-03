# import requests
#
# url = 'https://necaptcha.nosdn.127.net/05645be6e58d4629adf90336b1ee979e@2x.jpg'
# res = requests.get(url)
# open('bg.png', 'wb').write(res.content)
#
# url = 'https://necaptcha.nosdn.127.net/5311f323a5124ca79b5512276ba7a685@2x.png'
# res = requests.get(url)
# open('full.png', 'wb').write(res.content)

import ddddocr


def text_dis():
    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)

    with open('bg.png', 'rb') as f:
        background_bytes = f.read()

    with open('full.png', 'rb') as f:
        target_bytes = f.read()

    res = det.slide_match(target_bytes, background_bytes)

    print(res)


if __name__ == '__main__':
    text_dis()