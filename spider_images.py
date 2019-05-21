import requests, re, time

def get_images(page=1):
    url = 'https://www.mzitu.com/95656/%d' % page
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
              'Referer':'https://www.mzitu.com/180692',}
    res = requests.get(url, headers=header)
    body = res.content.decode('utf-8')
    image_pattern = re.compile(r'<img src="(.*?.jpg)"')
    image_list = re.findall(image_pattern, body)
    pic_max = re.findall(r'<span>(.*?)</span>', body)[7]
    for i in image_list:
        with open(r'E:\crawl_image\%d.jpg' % page, 'wb') as f:
            f.write(requests.get(i, headers=header).content)
            # time.sleep(2)
    return pic_max

if __name__ == '__main__':
    for i in range(1, int(get_images()) + 1):
        get_images(i)






