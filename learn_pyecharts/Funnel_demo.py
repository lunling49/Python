from pyecharts.charts import Funnel
from pyecharts import options as opts
from example.commons import Faker


# 漏斗图
# 1、Funnel-基本示例
def funnel_base():
    f = (Funnel()
         .add("商品", [list(z) for z in zip(Faker.choose(), Faker.values())])
         .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-基本示例"))
         .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}')))
    return f

# funnel_base().render(r'Funnel-基本示例.html')


# 2、Funnel-Label（inside)   --标签在漏斗图里
def funnel_label_inside():
    f = (Funnel()
         .add(
            "商品",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            label_opts=opts.LabelOpts(position="inside", formatter='{b}:{c}'))
         .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Label（inside)")))
    return f

funnel_label_inside().render(r'Funnel-Label（inside).html')


# 3、Funnel-Sort（ascending）
def funnel_sort_ascending():
    f = (Funnel()
         .add(
            "商品",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Sort（ascending）")))
    return f

funnel_sort_ascending().render(r'Funnel-Sort（ascending）.html')

