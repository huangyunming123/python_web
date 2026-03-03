import base64
import requests

# www.jfbym.com  注册后登录去用户中心

with open('full.png', 'rb') as f:
    slide_image_base64 = base64.b64encode(f.read()).decode()  ## 图片二进制流base64字符串
with open('bg.png', 'rb') as f:
    background_image_base64 = base64.b64encode(f.read()).decode()  ## 图片二进制流base64字符串

def verify():
    url = "http://api.jfbym.com/api/YmServer/customApi"
    data = {
        ## 关于参数,一般来说有3个;不同类型id可能有不同的参数个数和参数名,找客服获取
        "token": "0oWZV2h0zoDYR_8R9l1QrCIFI-FeGCpmktdCNziXWCk",
        "type": "20111",
        "slide_image": slide_image_base64,
        "background_image":background_image_base64
    }
    _headers = {
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, headers=_headers, json=data).json()
    print(response)


if __name__ == '__main__':
    verify()

