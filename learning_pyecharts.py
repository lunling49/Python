from pyecharts.charts import Bar, EffectScatter, Pie, Line, Funnel, Page
from pyecharts import options as opts
from example.commons import Faker
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.globals import ThemeType


# 柱状图--Bar
# bar = Bar()
# bar.add_xaxis([3.3, 3.25, 4.4, 4.10, 5.10, 5.26, 6.5, 6.25, 7.5, 7.20, 8.7, 8.25])
# bar.add_yaxis('还款金额', [42491, 34627, 18280, 12168, 5740, 6348, 6642, 3744, 2893, 4206, 3624, 2126])
# # render 会生成本地 html 文件，默认在当前目录生成render.html 文件
# # 也可以传入路径参数，如bar.render(r'd:\mycharts.html')
# bar.render(r'bar1.html')

# pyecharts 所有方法均支持链式调用
# bar = (Bar().add_xaxis([3.3, 3.25, 4.4, 4.10, 5.10, 5.26, 6.5, 6.25, 7.5, 7.20, 8.7, 8.25])
#             .add_yaxis('还款金额', [42491, 34627, 18280, 12168, 5740, 6348, 6642, 3744, 2893, 4206, 3624, 2126])
# bar.render(r'bar2.html')

# 使用options配置项，在pyecharts中，一切皆为options
# c = (Bar()
#         .add_xaxis(Faker.choose())
#         .add_yaxis("商家A", Faker.values())
#         .add_yaxis("商家B", Faker.values())
#         .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题")))
#         # 或者直接使用字典参数
#         # .set_global_opts(title_opts={"text":"主标题", "subtext":"副标题"})
# c.render(r'bar3.html')

# 渲染成图片文件
# bar = (Bar()
#        .add_xaxis(Faker.choose())
#        .add_yaxis("商家", Faker.values()))
# make_snapshot(snapshot, bar.render(),"bar.png")

# 使用主题
# c = (Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
#         .add_xaxis(Faker.choose())
#         .add_yaxis("商家A", Faker.values())
#         .add_yaxis("商家B", Faker.values())
#         .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题，可以写y轴数量单位")))
# c.render(r'bar4.html')

# 散点图--EffectScatter
# e = (EffectScatter()
#      .add_xaxis(Faker.choose())
#      .add_yaxis('数量', Faker.values()))
# e.render(r'散点图.html')

# 饼状图--Pie
# p = (Pie()
#      .add('',[list(z) for z in zip(Faker.choose(),Faker.values())])
#      .set_global_opts(title_opts=opts.TitleOpts(title='饼图示例'))
#      .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}')))
# p.render(r'饼状图基本示例.html')

# 线性图--Line
# l = (Line()
#      .add_xaxis(Faker.choose())
#      .add_yaxis('one',Faker.values())
#      .add_yaxis('two',Faker.values()))
# l.render(r'线性图.html')

# 漏斗图
f = (Funnel()
     .add('商品a',[list(z) for z in zip(Faker.choose(), Faker.values())])
     .set_global_opts(title_opts=(opts.TitleOpts(title='Funnel漏斗图基本示例'))))
f.render(r'漏斗图.html')


