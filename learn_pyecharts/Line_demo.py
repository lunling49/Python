from pyecharts.charts import Line, Grid
from pyecharts import options as opts
from example.commons import Faker


# 线性图
# 1、Line-基本示例
def line_base():
    l = (Line()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例")))
    return l

# line_base().render(r'Line-基本示例.html')


# 2、Line-数值 X 轴
def line_xaxis_type():
    l = (Line()
         .add_xaxis(Faker.values())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Line-数值 X 轴"),
            xaxis_opts=opts.AxisOpts(type_="value")))
    return l

# line_xaxis_type().render(r'Line-数值 X 轴.html')


# 3、Line-连接空数据（相当于过滤空数据，直接与下个不为空数据相连）
def line_connect_null():
    y = Faker.values()
    y[3], y[5] = None, None
    l = (Line()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", y, is_connect_nones=True)
         .set_global_opts(title_opts=opts.TitleOpts(title="Line-连接空数据")))
    return l

# line_connect_null().render(r'Line-连接空数据.html')


# 4、Line-平滑曲线
def line_smooth():
    l = (Line()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), is_smooth=True)
         .add_yaxis("商家B", Faker.values(), is_smooth=True)
         .set_global_opts(title_opts=opts.TitleOpts(title="Line-smooth")))
    return l

# line_smooth().render(r'Line-平滑曲线.html')


# 5、Line-面积图
def line_areastyle():
    l = (Line()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
         .add_yaxis("商家B", Faker.values(), areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
         .set_global_opts(title_opts=opts.TitleOpts(title="Line-面积图")))
    return l

# line_areastyle().render(r'Line-面积图.html')


# 6、Line-面积图（紧贴 Y 轴）
def line_areastyle_boundary_gap():
    l = (Line()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), is_smooth=True)
         .add_yaxis("商家B", Faker.values(), is_smooth=True)
         .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False))
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Line-面积图（紧贴 Y 轴）"),
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False)))
    return l

# line_areastyle_boundary_gap().render(r'Line-面积图（紧贴 Y 轴）.html')


# 7、Line-对数轴示例
def line_yaxis_log():
    l = (Line()
         .add_xaxis(xaxis_data=["一", "二", "三", "四", "五", "六", "七", "八", "九"])
         .add_yaxis(
            "2 的指数",
            y_axis=[1, 2, 4, 8, 16, 32, 64, 128, 256],
            linestyle_opts=opts.LineStyleOpts(width=2))
         .add_yaxis(
            "3 的指数",
            y_axis=[1, 3, 9, 27, 81, 247, 741, 2223, 6669],
            linestyle_opts=opts.LineStyleOpts(width=2))
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Line-对数轴示例"),
            xaxis_opts=opts.AxisOpts(name="x"),
            yaxis_opts=opts.AxisOpts(
                type_="log",
                name="y",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True)))
    return l

# line_yaxis_log().render(r'Line-对数轴示例.html')


# 8、Line-MarkPoint
def line_markpoint():
    l = (Line()
         .add_xaxis(Faker.choose())
         .add_yaxis(
            "商家A",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]))
         .add_yaxis(
            "商家B",
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]))
         .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint")))
    return l

# line_markpoint().render(r'Line-MarkPoint.html')


# 9、Line-MarkPoint（自定义）
def line_markpoint_custom():
    x, y = Faker.choose(), Faker.values()
    l = (Line()
         .add_xaxis(x)
         .add_yaxis(
            "商家A",
            y,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(name="自定义标记点", coord=[x[2], y[2]], value=y[2])]))
         .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint（自定义）")))
    return l

# line_markpoint_custom().render(r'Line-MarkPoint（自定义）.html')


# 10、Line-MarkLine
def line_markline():
    l = (Line()
         .add_xaxis(Faker.choose())
         .add_yaxis(
            "商家A",
            Faker.values(),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]))
         .add_yaxis(
            "商家B",
            Faker.values(),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]))
         .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkLine")))
    return l

# line_markline().render(r'Line-MarkLine.html')


# 11、Line-阶梯图
def line_step():
    l = (Line()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), is_step=True)
         .set_global_opts(title_opts=opts.TitleOpts(title="Line-阶梯图")))
    return l

# line_step().render(r'Line-阶梯图.html')


# 12、Line-ItemStyle
def line_itemstyle():
    l = (Line()
         .add_xaxis(xaxis_data=Faker.choose())
         .add_yaxis(
            "商家A",
            Faker.values(),
            symbol="circle",
            symbol_size=20,
            linestyle_opts=opts.LineStyleOpts(color="pink", width=4, type_="dashed"),
            label_opts=opts.LabelOpts(is_show=False),
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=3, border_color="yellow", color="red"))
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Line-ItemStyle"),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True)),
            tooltip_opts=opts.TooltipOpts(is_show=False)))
    return l

line_itemstyle().render(r'Line-ItemStyle.html')


