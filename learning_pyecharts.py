from pyecharts.charts import Bar, EffectScatter, Pie, Line, Funnel, Page, Grid
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
# f = (Funnel()
#      .add('商品a',[list(z) for z in zip(Faker.choose(), Faker.values())])
#      .set_global_opts(title_opts=(opts.TitleOpts(title='Funnel漏斗图基本示例'))))
# f.render(r'漏斗图.html')

# 组合图表
x_data = ["{}月".format(i) for i in range(1, 13)]
zengfaliang =  [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
jiangshuiliang = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
average_wendu = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

grid = Grid()

bar = Bar()
grid.theme = ThemeType.PURPLE_PASSION
line = Line()

bar.add_xaxis(x_data)
bar.add_yaxis("蒸发量",zengfaliang)
bar.add_yaxis("降水量",jiangshuiliang)
bar.set_global_opts(title_opts=opts.TitleOpts("Grid-多Y轴展示")
                   ,tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross") # 交叉指向工具
                   )
bar.extend_axis(yaxis=opts.AxisOpts(type_="value",
                                     name="温度",
                                     min_=0,
                                     max_=25,
                                     position="right",
                                     axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                                     ))
# 在bar上增加Y轴，在line图上选择对应的轴向
line.add_xaxis(x_data)
line.add_yaxis("平均温度",average_wendu,yaxis_index = 1)
# 把line添加到bar上
bar.overlap(line)
# 这里如果不需要grid也可以，直接设置bar的格式，然后显示bar即可
#bar.render()
grid.add(chart = bar,grid_opts = opts.GridOpts(),is_control_axis_index = True)
grid.render(r'组合图.html')



