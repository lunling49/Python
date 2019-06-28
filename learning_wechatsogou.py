# 基于搜狗微信搜索的微信公众号爬虫接口，可以扩展成基于搜狗搜索的爬虫

import wechatsogou
"""
初始化 API
    可配置参数
    1、直连
    ws_api = wechatsogou.WechatSogouAPI()
    
    2、验证码输入错误的重试次数，默认为 1
    ws_api = wechatsogou.WechatSogouAPI(captcha_break_time=3)
    
    3、所有requests库的参数都能在这用
    如：配置代理，代理列表中至少需包含 1 个 HTTPS 协议的代理，并确保代理可用
    ws_api = wechatsogou.WechatSogouAPI(proxies={
        'http': '127.0.0.1:8888',
        'https': '127.0.0.1:8888',})
    如：设置超时
    ws_api = wechatsogou.WechatSogouAPI(timeout=0.1)
"""

# 获取特定公众号信息 -- get_gzh_info
# ws_api = wechatsogou.WechatSogouAPI()
# ws_api.get_gzh_info('南航青年志愿者')
"""
返回数据结构
{   'open_id': '',
    'profile_url': '',  最近10条群发页链接
    'headimage': '',  头像
    'wechat_name': '',  名称
    'wechat_id': '',  微信id
    'post_perm': int,  最近一月群发数
    'view_perm': int,  最近一月阅读量
    'qrcode': '',  二维码
    'introduction': '',  简介
    'authentication': ''  认证}
"""

# 搜索公众号
# ws_api1 = wechatsogou.WechatSogouAPI()
# a = ws_api1.search_gzh('南京航空航天大学')
# print(next(a))
"""
返回数据结构：list of dict, dict，返回的是迭代对象
{   'open_id': '',
    'profile_url': '',  最近10条群发页链接
    'headimage': '',  头像
    'wechat_name': '',  名称
    'wechat_id': '',  微信id
    'post_perm': int,  最近一月群发数
    'view_perm': int,  最近一月阅读量
    'qrcode': '',  二维码
    'introduction': '',  介绍
    'authentication': ''  认证}
"""

# 搜索微信文章
# ws_api2 = wechatsogou.WechatSogouAPI()
# ws_api2.search_article('南京航空航天大学')
"""
返回数据结构：list of dict, dict
{
    'article': {
        'title': '',  文章标题
        'url': '',  文章链接
        'imgs': '',  文章图片list
        'abstract': '',  文章摘要
        'time': int  文章推送时间 10位时间戳},
    'gzh': {
        'profile_url': '',  公众号最近10条群发页链接
        'headimage': '',  头像
        'wechat_name': '',  名称
        'isv': int,  是否加v 1 or 0}
}
"""

# 解析最近文章页 -- get_gzh_article_by_history
# ws_api3 = wechatsogou.WechatSogouAPI()
# ws_api3.get_gzh_article_by_history('南航青年志愿者')
"""
返回数据结构
{
    'gzh': {
        'wechat_name': '',  名称
        'wechat_id': '',  微信id
        'introduction': '',  简介
        'authentication': '',  认证
        'headimage': ''  头像
    },
    'article': [
        {
            'send_id': int,  群发id，注意不唯一，因为同一次群发多个消息，而群发id一致
            'datetime': int,  群发datatime 10位时间戳
            'type': '',  消息类型，均是49（在手机端历史消息页有其他类型，网页端最近10条消息页只有49），表示图文
            'main': int,  是否是一次群发的第一次消息 1 or 0
            'title': '',  文章标题
            'abstract': '',  摘要
            'fileid': int,  
            'content_url': '',  文章链接
            'source_url': '',  阅读原文的链接
            'cover': '',  封面图
            'author': '',  作者
            'copyright_stat': int,  文章类型，例如：原创啊
        },
        ...
    ]
}
"""

# 解析 首页热门页 -- get_gzh_article_by_hot
from pprint import pprint
from wechatsogou import WechatSogouAPI, WechatSogouConst
ws_api4 = WechatSogouAPI()
gzh_articles = ws_api4.get_gzh_article_by_hot(WechatSogouConst.hot_index.food)
for i in gzh_articles:
    pprint(i)
"""
返回数据结构
{
    'gzh': {
        'headimage': str,  公众号头像
        'wechat_name': str,  公众号名称},
    'article': {
        'url': str,  文章临时链接
        'title': str,  文章标题
        'abstract': str,  文章摘要
        'time': int,  推送时间，10位时间戳
        'open_id': str,  open id
        'main_img': str  封面图片}
}
"""

# 获取关键字联想词
ws_api5 = wechatsogou.WechatSogouAPI()
ws_api5.get_sugg('高考')
"""
返回数据结构：关键词列表
['a', 'b', ...]
"""



