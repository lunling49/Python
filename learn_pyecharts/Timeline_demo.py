from pyecharts.charts import Timeline, Bar, Line, Pie, Scatter, Map
from example.commons import Faker
from pyecharts import options as opts

# 时间线轮播多图
# 1、Bar 图 Timeline 效果
def timeline_bar():
    x = Faker.choose()
    t1 = Timeline()
    for i in range(2016, 2021):
        bar = (Bar()
               .add_xaxis(x)
               .add_yaxis("商家A", Faker.values())
               .add_yaxis("商家B", Faker.values())
               .set_global_opts(title_opts=opts.TitleOpts("商店{}年营业额".format(i))))
        t1.add(bar, "{}年".format(i))
    return t1

# timeline_bar().render(r'Timeline-bar轮播多图.html')


# 2、Pie 图 Timeline 效果
def timeling_pie():
    attr = Faker.choose()
    t1 = Timeline()
    for i in range(2016, 2021):
        pie = (Pie()
               .add("商家",
                    [list(z) for z in zip(attr, Faker.values())],
                    rosetype='radius',
                    radius=['30%', '55%'])
               .set_global_opts(title_opts=opts.TitleOpts("商店{}年营业额".format(i))))
        t1.add(pie, "{}年".format(i))
    return t1

# timeling_pie().render(r'Timeline-pie轮播多图.html')


# 3、Map 图 Timeline 效果
def timeline_map():
    t1 = Timeline()
    for i in range(2016,2021):
        map = (Map()
               .add("人流", [list(z) for z in zip(Faker.provinces, Faker.values())])
               .set_global_opts(title_opts=opts.TitleOpts(title="各省{}年人流数据".format(i)),
                                visualmap_opts=opts.VisualMapOpts(max_=200)))
        t1.add(map, "{}年".format(i))
    return t1

timeline_map().render(r'Timeline-map轮播多图.html')

