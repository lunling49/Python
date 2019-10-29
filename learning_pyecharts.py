from pyecharts.charts import Bar, EffectScatter, Pie
from pyecharts import options as opts
from example.commons import Faker
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.globals import ThemeType

# bar = Bar()
# bar.add_xaxis([3.3, 3.25, 4.4, 4.10, 5.10, 5.26, 6.5, 6.25, 7.5, 7.20, 8.7, 8.25])
# bar.add_yaxis('还款金额', [42491, 34627, 18280, 12168, 5740, 6348, 6642, 3744, 2893, 4206, 3624, 2126])
# # render 会生成本地 html 文件，默认在当前目录生成render.html 文件
# # 也可以传入路径参数，如bar.render(r'd:\mycharts.html')
# bar.render()

# pyecharts 所有方法均支持链式调用
# bar = (Bar().add_xaxis([3.3, 3.25, 4.4, 4.10, 5.10, 5.26, 6.5, 6.25, 7.5, 7.20, 8.7, 8.25])
#             .add_yaxis('还款金额', [42491, 34627, 18280, 12168, 5740, 6348, 6642, 3744, 2893, 4206, 3624, 2126])
# bar.render()

# 使用options配置项，在pyecharts中，一切皆为options
# c = (Bar()
#         .add_xaxis(Faker.choose())
#         .add_yaxis("商家A", Faker.values())
#         .add_yaxis("商家B", Faker.values())
#         .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题")))
#         # 或者直接使用字典参数
#         # .set_global_opts(title_opts={"text":"主标题", "subtext":"副标题"})
# c.render()

# 渲染成图片文件
# bar = (Bar()
#        .add_xaxis(Faker.choose())
#        .add_yaxis("商家", Faker.values()))
# make_snapshot(snapshot, bar.render(),"bar.png")

# 使用主题
c = (Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题，可以写y轴数量单位")))
c.render()





