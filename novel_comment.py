from math import ceil
import requests, re, time

# 获取评论及回复
url = 'https://xiaoshuo.sm.cn/sc/2/comment/book/?format=json&size=10&novelid=%E5%BE%88%E6%98%AF%E7%9F%AB%E6%83%85%2F%E5%BF%AB%E7%A9%BF%E4%B9%8B%E7%82%AE%E7%81%B0%E5%A5%B3%E9%85%8D%E9%80%86%E8%A2%AD%E8%AE%B0&page=1'
res = requests.get(url)
comments_data = res.json()
total_comments = comments_data['info']['total']
total_pages = ceil(total_comments/100)
last_page_comments = total_comments % 100
print('总评论数：{}'.format(total_comments))
print('总页数：{}'.format(total_pages))
print('最后一页的评论数量：{}'.format(last_page_comments))
for page in range(1, total_pages+1):
    url1 = 'https://xiaoshuo.sm.cn/sc/2/comment/book/?format=json&size=100&novelid=%E5%BE%88%E6%98%AF%E7%9F%AB%E6%83%85%2F%E5%BF%AB%E7%A9%BF%E4%B9%8B%E7%82%AE%E7%81%B0%E5%A5%B3%E9%85%8D%E9%80%86%E8%A2%AD%E8%AE%B0&page={}'.format(page)
    respone = requests.get(url1)
    comments_list = respone.json()
    print(page)
    # if page == total_pages:
    #     page_nums = last_page_comments
    # else:
    #     page_nums = 100
    # 使用三元表达式简化代码
    page_nums = last_page_comments if page == total_pages else 100
    if comments_list['info']['total'] != 0:
        with open(r'e:/快穿之炮灰女配逆袭记的评论.txt', 'r', encoding='utf-8') as open_f:
            list_comments = open_f.read()
            with open(r'e:/快穿之炮灰女配逆袭记的评论.txt', 'a+', encoding='utf-8') as f:
                for i in range(0, page_nums):
                    comment = comments_list['data']['list'][i]['text']
                    reply_nums = int(comments_list['data']['list'][i]['replynum'])
                    if comment not in list_comments:
                        f.write(comment+'\n')
                        if reply_nums == 0:
                            f.write('\n')
                        if reply_nums > 0:
                            mid = comments_list['data']['list'][i]['mid']
                            get_reply_url = 'https://xiaoshuo.sm.cn/sc/2/comment/getReplyListByMid/?format=json&mid={}'.format(mid)
                            reply = requests.get(get_reply_url)
                            reply_data = reply.json()
                            for y in range(0, len(reply_data['list'])):
                                if y == len(reply_data['list'])-1:
                                    f.write('   {}、'.format(y+1) + reply_data['list'][y]['text']+'\n\n')
                                else:
                                    f.write('   {}、'.format(y+1) + reply_data['list'][y]['text']+'\n')
    # time.sleep(1)
print('finished'.center(30, '-'))






