from pyecharts.charts import Pie
from pyecharts import options as opts
from example.commons import Faker
from pyecharts.commons.utils import JsCode


# 饼状图
# 1、Pie-基本示例
def pie_base():
    p = (Pie()
         .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
         .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
    return p

# pie_base().render(r'Pie-基本示例.html')


# 2、Pie-设置颜色
def pie_set_colors():
    p = (Pie()
         .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
         .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
         .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
    return p

# pie_set_colors().render(r'Pie-设置颜色.html')


# 3、Pie-调整位置
def pie_position():
    p = (Pie()
         .add(
            "",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            center=["35%", "50%"])      # 饼图的位置
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-调整位置"),
            legend_opts=opts.LegendOpts(pos_left="50%"))    # 标签的位置
         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
    return p

# pie_position().render(r'Pie-调整位置.html')


# 4、Pie-Radius
def pie_radius():
    p = (Pie()
         .add(
            "",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["40%", "75%"])
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-Radius"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"))
         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
    return p

# pie_radius().render(r'Pie-Radius.html')


# 5、Pie-玫瑰图示例
def pie_rosetype():
    v = Faker.choose()
    p = (Pie()
         .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False))
         .add(
            "",
            [list(z) for z in zip(v, Faker.values())],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area")
         .set_global_opts(title_opts=opts.TitleOpts(title="Pie-玫瑰图示例")))
    return p

# pie_rosetype().render(r'Pie-玫瑰图示例.html')


# 6、Pie-Legend 滚动   --标签多的时候可以滚动或点击翻页
def pie_scroll_legend():
    p = (Pie()
         .add(
            "",
            [list(z) for z in zip(
                    Faker.choose() + Faker.choose() + Faker.choose(),
                    Faker.values() + Faker.values() + Faker.values())],
            center=["40%", "50%"])
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-Legend 滚动"),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"))
         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")))
    return p

# pie_scroll_legend().render(r'Pie-Legend滚动.html')


# 7、Pie-富文本示例
def pie_rich_label():
    p = (Pie()
         .add(
            "",
            [list(z) for z in zip(Faker.choose(), Faker.values())],
            radius=["40%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0]},
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0},
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {"color": "#eee",
                            "backgroundColor": "#334455",
                            "padding": [2, 4],
                            "borderRadius": 2}}))
         .set_global_opts(title_opts=opts.TitleOpts(title="Pie-富文本示例")))
    return p

# pie_rich_label().render(r'Pie-富文本示例.html')


# 8、Pie-多饼图基本示例
def pie_multiple_base():
    fn = """
    function(params) {
        if(params.name == '其他')
            return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
        return params.name + ' : ' + params.value + '%';
    }
    """

    def new_label_opts():
        return opts.LabelOpts(formatter=JsCode(fn), position="center")

    p = (Pie()
         .add(
            "",
            [list(z) for z in zip(["剧情", "其他"], [25, 75])],
            center=["20%", "30%"],
            radius=[60, 80],
            label_opts=new_label_opts())
         .add(
            "",
            [list(z) for z in zip(["奇幻", "其他"], [24, 76])],
            center=["55%", "30%"],
            radius=[60, 80],
            label_opts=new_label_opts())
         .add(
            "",
            [list(z) for z in zip(["爱情", "其他"], [14, 86])],
            center=["20%", "70%"],
            radius=[60, 80],
            label_opts=new_label_opts())
         .add(
            "",
            [list(z) for z in zip(["惊悚", "其他"], [11, 89])],
            center=["55%", "70%"],
            radius=[60, 80],
            label_opts=new_label_opts())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Pie-多饼图基本示例"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="20%", pos_left="80%", orient="vertical")))
    return p

pie_multiple_base().render(r'Pie-多饼图基本示例.html')

