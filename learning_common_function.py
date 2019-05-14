# 获取当前日期和时间
from datetime import datetime, timedelta, timezone
print(datetime.now())
"""
datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类
如果仅导入import datetime，则必须引用全名datetime.datetime
"""

# 获取指定日期和时间
# 要指定某个日期和时间，用参数构造一个datetime
dt = datetime(2019, 5, 14, 21, 44, 34)
print(dt)

# datetime转换为timestamp
"""
在计算机中，时间实际上是用数字表示的。
我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
记为0（1970年以前的时间timestamp为负数），
当前时间就是相对于epoch time的秒数，称为timestamp。
"""
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间
# timestamp = 0 = 1970-1-1 08:00:00 UTC+0:00
"""
可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，
转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前时间是以timestamp表示的，
因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）
"""
# datetime类型转换为timestamp只需调用timestamp()方法
print(dt.timestamp())
"""
注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，
这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。
"""

# timestamp转换为datetime，使用datetime提供的fromtimestamp()方法
t = 1557841474.0
print(datetime.fromtimestamp(t))
"""
注意到timestamp是一个浮点数，它没有时区的概念，
而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
"""
# timestamp也可以直接被转换到UTC标准时区的时间
print(datetime.utcfromtimestamp(t))

# str转换为datetime
"""
用户输入的日期和时间是字符串，
要处理日期和时间，首先必须把str转换为datetime。
转换方法是通过datetime.strptime()实现，# 需要一个日期和时间的格式化字符串
"""
sday = datetime.strptime('2019-5-14 22:32:45', '%Y-%m-%d %H:%M:%S')
print(sday)
# 注意，转换后的datetime是没有时区信息的

# datetime转换为str
"""
有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，
转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串
"""
now = datetime.now()
print(now.strftime('%c'))
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
"""
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
加减可以直接用+和-运算符，不过需要导入timedelta这个类
"""
p = now + timedelta(hours=10)
print(p)
m = now - timedelta(days=1)
print(m)
d = now + timedelta(days=2, hours=12)
print(d)

# 本地时间转换为UTC时间
"""
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
"""
tz_utc_8 = timezone(timedelta(hours=8))     # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)       # 强制设置为UTC+8:00
print(dt)
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

# 时区转换 -- 先通过utcnow()拿到当前UTC时间，在转换为任意时区的时间
# 拿到UTC时间，并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
"""
区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换
"""

"""
小结:
datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关
"""

