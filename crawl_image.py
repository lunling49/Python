import re
from urllib import request


def crawl_image(image_url, image_local_path):
    """
    爬取图片
    :param image_url: 图片的地址
    :param image_local_path: 本地的图片路径
    :return:
    """
    # 图片流也是二进制，要加上stream = true
    r = request.urlopen(image_url, stream=True)
    with open(image_local_path, 'wb') as f:
        f.write(r.content)

def crawl(page):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    url = 'https://www.qiushibaike.com/imgrank/page/' + str(page)
    req = request.Request(url, headers=headers)
    res = request.urlopen(req).read().decode('utf-8')
    content_list = re.findall('<div class=\"thumb\">(.*?)</div>', res, re.S)
    for content in content_list:
        image_list = re.findall('<img src=\"(.*?)\"', content)
        for image_url in image_list:
            crawl_image(image_url, './images/' + image_url.strip().split('/')[-1])

if __name__ == '__main__':
    crawl(1)