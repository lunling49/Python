# Faker--生成随机数据


from faker import Faker
from faker import Factory       # 导入工厂类

"""
from example.commons import Faker
from faker import Faker as f

不同faker之间的差别
fake = f('zh_CN')
a = Faker.values()      --生成的数据是一个list
b = fake.pyint()        --生成的数据是单个或者是自己设定的
print(a)
print(b)
"""


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
print('区：', fake1.district())
print('市或县：', fake1.city_suffix())
print('省份名：', fake1.province())
print('邮编：', fake1.postcode())
print('国家：', fake1.country())
print('国家编号：', fake1.country_code())
print('经度：', fake1.longitude())
print('纬度：', fake1.latitude())
# print('地理坐标：', fake1.geo_coordinate())
print('建筑编号：', fake1.building_number())

# 公司信息类
print('company'.center(20, '-'))
print('公司名：', fake1.company())
print('公司名后缀（公司性质）：', fake1.company_suffix())
print('公司名前缀：', fake1.company_prefix())

# 日期类
print('date'.center(20, '-'))
print('随机日期时间：', fake1.date_time(tzinfo=None))
print('以iso8601标准输出的日期：', fake1.iso8601(tzinfo=None))
print('本月随机日期：', fake1.date_time_this_month(before_now=True, after_now=False, tzinfo=None))
print('本年随机日期：', fake1.date_time_this_year(before_now=True, after_now=False, tzinfo=None))
print('本年代随机日期：', fake1.date_time_this_decade(before_now=True, after_now=False, tzinfo=None))
print('本世纪随机日期：', fake1.date_time_this_century(before_now=True, after_now=False, tzinfo=None))
print('两个时间内的随机时间：', fake1.date_time_between(start_date="-30y", end_date="now", tzinfo=None))
print('随机时区：', fake1.timezone())
print('随机日期：', fake1.date(pattern='%Y-%m-%d', end_datetime=None))       # pattern--可自定义格式
print('公元后随机日期：', fake1.date_time_ad(tzinfo=None))
print('随机上下午：', fake1.am_pm())
print('随机年份：', fake1.year())
print('随机月份：', fake1.month())
print('随机月份名字：', fake1.month_name())
print('随机月中某一天：', fake1.day_of_month())
print('随机星期数：', fake1.day_of_week())
print('随机时间：', fake1.time(pattern='%H:%M:%S', end_datetime=None))
print('随机时间延迟：', fake1.time_delta())
print('随机日期对象：', fake1.date_object())
print('随机时间对象：', fake1.time_object())
print('随机unix时间（时间戳）：', fake1.unix_time())

# 网络类
print('internet'.center(20, '-'))
print('用户名：', fake1.user_name())
print('伪造UA：', fake1.user_agent())      # 常用在伪造浏览器信息
print('企业邮箱：', fake1.company_email())
print('免费邮箱：', fake1.free_email())
print('安全邮箱：', fake1.safe_email())
print('邮箱：', fake1.email())
print('ipv4地址：', fake1.ipv4(network=False))
print('ipv6地址：', fake1.ipv6(network=False))
print('MAC地址：', fake1.mac_address())
print('uri路径：', fake1.uri_path(deep=None))
print('uri拓展名：', fake1.uri_extension())
print('uri：', fake1.uri())
print('url：', fake1.url())
print('图片url：', fake1.image_url(width=None, height=None))
print('域名主体：', fake1.domain_word())
print('域名：', fake1.domain_name())
print('域名后缀：', fake1.tld())

# 个人信息类
print('person'.center(20, '-'))
print('姓名：', fake1.name())
print('姓：', fake1.last_name())
print('名：', fake1.first_name())
print('男性姓名：', fake1.name_male())
print('男性姓：', fake1.last_name_male())
print('男性名：', fake1.first_name_male())
print('女性姓名：', fake1.name_female())
print('女性姓：', fake1.last_name_female())
print('女性名：', fake1.first_name_female())
print('电话号码：', fake1.phone_number())
print('运营商号段，手机号码前三位：', fake1.phonenumber_prefix())
print('身份证号码：', fake1.ssn())
print('简略个人信息：', fake1.simple_profile())        # 包括用户名，姓名，性别，地址，邮箱，出生日期
print('详略个人信息：', fake1.profile())           # 比简略个人信息多公司名、血型、工作、位置、域名等
print('密码：', fake1.password())      # 参数:length:密码长度；special_chars:是否能使用特殊字符；digits:是否包含数字；upper_case:是否包含大写字母；lower_case:是否包含小写字母
print('工作：', fake1.job())
print('车牌号：', fake1.license_plate())

# 银行信用卡类
print('credit'.center(20, '-'))
print('信用卡卡号：', fake1.credit_card_number(card_type=None))
print('卡的提供者：', fake1.credit_card_provider(card_type=None))
print('卡的安全密码：', fake1.credit_card_security_code(card_type=None))
print('卡的有效期：', fake1.credit_card_expire())
print('完整的卡信息：', fake1.credit_card_full(card_type=None))

# 文章类
print('随机词语：', fake1.word())        # 参数:ext_word_list可以是一个列表，那么词语会从列表中取
print('随机多个词语：', fake1.words(nb=3))     # 参数:ext_word_list；nb是数量
print('随机短语（包含结束标点号）：', fake1.sentence(nb_words=6, variable_nb_words=True,ext_word_list=None))
print('随机多个短语：', fake1.sentences(nb=3))
print('随机段落：', fake1.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None))
print('多个随机段落：', fake1.paragraphs(nb=3, ext_word_list=None))

# 文件类
print('file'.center(20, '-'))
print('文件扩展信息（文件后缀）：', fake1.file_extension(category=None))
print('文件名：', fake1.file_name(category='image', extension='png'))       # 指定文件类型和后缀名
print('随机生成各类文件：', fake1.file_name())
print('mime-type：', fake1.mime_type())

# 数据类
print('data'.center(20, '-'))
print('自定义长度的随机字符串：', fake1.pystr(min_chars=None, max_chars=15))
print('随机整数：', fake1.pyint())
print('随机浮点数：', fake1.pyfloat(left_digits=None, right_digits=None, positive=False))
print('随机高精度数：', fake1.pydecimal(left_digits=None, right_digits=None, positive=False))
print('随机bool值：', fake1.pybool())
print('随机iterable：', fake1.pyiterable(nb_elements=10, variable_nb_elements=True))
print('随机list：', fake1.pylist(nb_elements=10, variable_nb_elements=True))
print('随机dict：', fake1.pydict(nb_elements=10, variable_nb_elements=True))
print('随机set：', fake1.pyset(nb_elements=10, variable_nb_elements=True))
print('随机tuple：', fake1.pytuple(nb_elements=10, variable_nb_elements=True))
print('随机生成3个有10个元素的python数据结构：', fake1.pystruct())

# 颜色类
print('颜色RGB：', fake1.rgb_css_color())
print('安全颜色名字：', fake1.safe_color_name())
print('颜色名字：', fake1.color_name())
print('16进制表示的颜色：', fake1.hex_color())
print('安全16进制色：', fake1.safe_hex_color())
print('rgb色的字符串：', fake1.rgb_color())

# 条码类
print('code'.center(20, '-'))
print('8位条码：', fake1.ean8())
print('13位条码：', fake1.ean13())
print('自定义位数条码：', fake1.ean(length=8))      # 只能选8或者13

# 货币类
print('currency'.center(20, '-'))
print('货币代码：', fake1.currency_code())

# 其他类
print('misc'.center(20, '-'))
print('二进制字符串：', fake1.binary(length=10))       # 可自定义长度
print('语言代码：', fake1.language_code())
print('随机md5，16进制字符串：', fake1.md5(raw_output=False))
print('随机sha1，16进制字符串：', fake1.sha1(raw_output=False))
print('随机sha256，16进制字符串：', fake1.sha256(raw_output=False))
print('随机真假值：', fake1.boolean(chance_of_getting_true=50))       # 得到True的机率是50%
print('随机真假值和null：', fake1.null_boolean())
print('随机本地代码：', fake1.locale())
print('随机uuid：', fake1.uuid4())

# 平台类
print('platform'.center(20, '-'))
print(fake.linux_platform_token())
print(fake.linux_processor)
print(fake.windows_platform_token())
print(fake.mac_platform_token())
print(fake.mac_processor())

# 浏览器类
print('browser'.center(20, '-'))
print('IE浏览器：', fake1.internet_explorer())
print('opera浏览器：', fake1.opera())
print('firefox浏览器：', fake1.firefox())
print('safari浏览器：', fake1.safari())
print('chrome浏览器：', fake1.chrome())

