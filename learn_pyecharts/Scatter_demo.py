from pyecharts.charts import Scatter
from pyecharts import options as opts
from example.commons import Faker
from pyecharts.commons.utils import JsCode


# 散点图
# 1、Scatter-基本示例
def scatter_base():
    s = (Scatter()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例")))
    return s

# scatter_base().render(r'Scatter-基本示例.html')


# 2、Scatter-显示分割线
def scatter_spliteline():
    s = (Scatter()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-显示分割线"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True))))
    return s

# scatter_spliteline().render(r'Scatter-显示分割线.html')


# 3、Scatter-VisualMap(Color)
def scatter_visualmap_color():
    s = (Scatter()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-VisualMap(Color)"),
            visualmap_opts=opts.VisualMapOpts(max_=150)))
    return s

# scatter_visualmap_color().render(r'Scatter-VisualMap(Color).html')


# 4、Scatter-VisualMap(Size)
def scatter_visualmap_size():
    s = (Scatter()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20)))
    return s

# scatter_visualmap_size().render(r'Scatter-VisualMap(Size).html')


# 5、Scatter-多维度数据
def scatter_muti_dimension_data():
    s = (Scatter()
         .add_xaxis(Faker.choose())
         .add_yaxis(
            "商家A",
            [list(z) for z in zip(Faker.values(), Faker.choose())],
            label_opts=opts.LabelOpts(
                formatter=JsCode(
                    "function(params){return params.value[1] +' : '+ params.value[2];}")))
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-多维度数据"),
            tooltip_opts=opts.TooltipOpts(
                formatter=JsCode(
                    "function (params) {return params.name + ' : ' + params.value[2];}")),
            visualmap_opts=opts.VisualMapOpts(type_="color", max_=150, min_=20, dimension=1)))
    return s

scatter_muti_dimension_data().render(r'Scatter-多维度数据.html')


