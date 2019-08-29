# Faker--生成随机数据


from faker import Faker
from faker import Factory       # 导入工厂类


# Faker里不填，默认输出美国英文；填本地化提供商，则显示对应的语言
fake = Faker()      # 创建和初始化生成器
fake1 = Faker('zh_CN')      # 可以在初始化时设置本地化，即是设定区域
print(fake.name())
print(fake1.name())

# 地址信息类
print('address'.center(20, '-'))
print('完整地址：', fake1.address())
print('街道+地址：', fake1.street_address())
print('街道名：', fake1.street_name())
print('街道后缀：', fake1.street_suffix())
print('城市名：', fake1.city())
print('市：', fake1.city_suffix())
print('省份名：', fake1.province())
print('邮编：', fake1.postcode())
print('国家：', fake1.country())
print('国家编号：', fake1.country_code())
print('经度：', fake1.longitude())
print('纬度：', fake1.latitude())
print('建筑编号：', fake1.building_number())

# 公司信息类
print('company'.center(20, '-'))
print('公司名：', fake1.company())
print('公司名后缀（公司性质）：', fake1.company_suffix())
print('公司名前缀：', fake1.company_prefix())

# 日期类
print('date'.center(20, '-'))
print('随机日期时间：', fake1.date_time(tzinfo=None))
print('随机日期：', fake1.date(pattern='%Y-%m-%d', end_datetime=None))
print('随机年份：', fake1.year())
print('随机星期数：', fake1.day_of_week())
print('随机时间：', fake1.time(pattern='%H:%M:%S', end_datetime=None))

# 网络类
print('企业邮箱：', fake1.company_email())
print('邮箱：', fake1.email())
print('ipv4地址：', fake1.ipv4(network=False))

# 个人信息类
print('姓名：', fake1.name())
print('用户名：', fake1.user_name())
print('电话号码：', fake1.phone_number())
print('简略个人信息：', fake1.simple_profile())        # 包括用户名，姓名，性别，地址，邮箱，出生日期
print('详略个人信息：', fake1.profile())           # 比简略个人信息多公司名、血型、工作、位置、域名等
print('密码：', fake1.password())      # 参数:length:密码长度；special_chars:是否能使用特殊字符；digits:是否包含数字；upper_case:是否包含大写字母；lower_case:是否包含小写字母
print('工作：', fake1.job())
print('车牌号：', fake1.license_plate())
print('信用卡卡号：', fake1.credit_card_number(card_type=None))

# 文章类
print('随机词语：', fake1.word())        # 参数:ext_word_list可以是一个列表，那么词语会从列表中取
print('随机多个词语：', fake1.words(nb=3))     # 参数:ext_word_list；nb是数量
print('随机短语（包含结束标点号）：', fake1.sentence(nb_words=6, variable_nb_words=True,ext_word_list=None))
print('随机段落：', fake1.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None))
print('多个随机段落：', fake1.paragraphs(nb=3, ext_word_list=None))
print('文件扩展信息：', fake1.file_extension(category=None))

# 数据类
print('自定义长度的随机字符串：', fake1.pystr(min_chars=None, max_chars=15))
print('随机整数：', fake1.pyint())

# 其他类
print('颜色RGB：', fake1.rgb_css_color())
print('颜色名称：', fake1.safe_color_name())
