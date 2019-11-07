from pyecharts.charts import Bar, Grid
from example.commons import Faker
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

# 柱状图/条形图
# 1、Bar-基本示例
def bar_base():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis('商家A', Faker.values())
         .add_yaxis('商家B', Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title='Bar-基本示例', subtitle='副标题')))
    return b

# bar_base().render(r'Bar-基本示例.html')


# 2、Bar-渐变圆柱
def bar_border_radius():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis('商家A', Faker.values(), category_gap='60%')
         .set_series_opts(itemstyle_opts={
            "normal": {
                "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1,
                 [{offset: 0, color: 'rgba(0, 244, 255, 1)'},
                 {offset: 1, color: 'rgba(0, 77, 167, 1)'}], false)"""),
                "barBorderRadius": [30, 30, 30, 30],
                "shadowColor": 'rgb(0, 160, 221)'}})
         .set_global_opts(title_opts=opts.TitleOpts(title='Bar-渐变圆柱')))
    return b

# bar_border_radius().render(r'Bar-渐变圆柱.html')


# 3、Bar-动画配置基本示例
def bar_base_with_animation():
    b = (Bar(init_opts=opts.InitOpts(
                animation_opts=opts.AnimationOpts(
                    animation_delay=1000, animation_easing="elasticOut")))
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-动画配置基本示例", subtitle="我是副标题")))
    return b

# bar_base_with_animation().render(r'Bar-动画配置基本示例.html')


# 4、Bar-背景图基本示例
def bar_base_with_custom_background_image():
    b = (Bar(init_opts=opts.InitOpts(bg_color={"type": "pattern",
                                               "image": JsCode("img"),
                                               "repeat": "no-repeat"}))
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-背景图基本示例",
                                                    subtitle="我是副标题",
                                                    title_textstyle_opts=opts.TextStyleOpts(color="white"))))
    b.add_js_funcs(
        """
        var img = new Image(); img.src = 'http://pic23.nipic.com/20120921/8434536_083333219174_2.jpg';
        """)
    return b

# bar_base_with_custom_background_image().render(r'Bar-背景图基本示例.html')


# 5、Bar-通过 dict 进行配置
def bar_base_dict_config():
    b = (Bar({"theme": ThemeType.MACARONS})
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts={"text": "Bar-通过 dict 进行配置", "subtext": "我也是通过 dict 进行配置的"}))
    return b

# bar_base_dict_config().render(r'Bar-通过 dict 进行配置.html')


# 6、Bar-默认取消显示某 Series
def bar_is_selected():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values(), is_selected=False)
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-默认取消显示某 Series")))
    return b

# bar_is_selected().render(r'Bar-默认取消显示某 Series.html')


# 7、Bar-显示 ToolBox
def bar_toolbox():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-显示 ToolBox"),
                          toolbox_opts=opts.ToolboxOpts(),
                          legend_opts=opts.LegendOpts(is_show=False)))
    return b

# bar_toolbox().render(r'Bar-显示ToolBox.html')


# 8、Bar-单系列柱间距离
def bar_same_series_gap():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), category_gap="80%")
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-单系列柱间距离")))
    return b

# bar_same_series_gap().render(r'Bar-单系列柱间距离.html')


# 9、Bar-不同系列柱间距离
def bar_different_series_gap():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), gap="0%")
         .add_yaxis("商家B", Faker.values(), gap="0%")
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-不同系列柱间距离")))
    return b

# bar_different_series_gap().render(r'Bar-不同系列柱间距离.html')


# 10、Bar-Y 轴 formatter
def bar_yaxis_formatter():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-Y 轴 formatter"),
                         yaxis_opts=opts.AxisOpts(
                         axislabel_opts=opts.LabelOpts(formatter="{value} /月"))))
    return b

# bar_yaxis_formatter().render(r'Bar-Y 轴 formatter.html')


# 11、Bar-XY 轴名称
def bar_xyaxis_name():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-XY 轴名称"),
                          yaxis_opts=opts.AxisOpts(name="我是 Y 轴"),
                          xaxis_opts=opts.AxisOpts(name="我是 X 轴")))
    return b

# bar_xyaxis_name().render(r'Bar-XY 轴名称.html')


# 12、Bar-翻转 XY 轴
def bar_reversal_axis():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .reversal_axis()
         .set_series_opts(label_opts=opts.LabelOpts(position="right"))
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-翻转 XY 轴")))
    return b

# bar_reversal_axis().render(r'Bar-翻转 XY 轴.html')


# 13、Bar-堆叠数据（全部）
def bar_stack0():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), stack="stack1")
         .add_yaxis("商家B", Faker.values(), stack="stack1")
         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）")))
    return b

# bar_stack0().render(r'Bar-堆叠数据（全部）.html')

# 14、Bar-堆叠数据（部分）
def bar_stack1():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), stack="stack1")
         .add_yaxis("商家B", Faker.values(), stack="stack1")
         .add_yaxis('商家C', Faker.values())
         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（部分）")))
    return b

# bar_stack1().render(r'Bar-堆叠数据（部分）.html')


# 15、Bar-MarkPoint（指定类型）
def bar_markpoint_type():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（指定类型）"))
         .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                          markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值"),
                                                                  opts.MarkPointItem(type_="min", name="最小值"),
                                                                  opts.MarkPointItem(type_="average", name="平均值")])))
    return b

# bar_markpoint_type().render(r'Bar-MarkPoint（指定类型）.html')


# 16、Bar-MarkPoint（自定义）
def bar_markpoint_custom():
    x, y = Faker.choose(), Faker.values()
    b = (Bar()
         .add_xaxis(x)
         .add_yaxis("商家A", y, markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(name="自定义标记点",
                                                                                           coord=[x[2], y[2]],
                                                                                           value=y[2])]))
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（自定义）"))
         .set_series_opts(label_opts=opts.LabelOpts(is_show=False)))
    return b

# bar_markpoint_custom().render(r'Bar-MarkPoint（自定义）.html')


# 17、Bar-MarkLine（指定类型）
def bar_markline_type():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkLine（指定类型）"))
         .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="min", name="最小值"),
                      opts.MarkLineItem(type_="max", name="最大值"),
                      opts.MarkLineItem(type_="average", name="平均值")])))
    return b

# bar_markline_type().render(r'Bar-MarkLine（指定类型）.html')


# 18、Bar-MarkLine（自定义）
def bar_markline_custom():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkLine（自定义）"))
         .set_series_opts(
                label_opts=opts.LabelOpts(is_show=False),
                markline_opts=opts.MarkLineOpts(
                    data=[opts.MarkLineItem(y=50, name="yAxis=50")])))
    return b

# bar_markline_custom().render(r'Bar-MarkLine（自定义）.html')


# 19、Bar-DataZoom（slider-水平）
def bar_datazoom_slider():
    b = (Bar()
         .add_xaxis(Faker.days_attrs)
         .add_yaxis("商家A", Faker.days_values)
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
                          datazoom_opts=opts.DataZoomOpts()))
    return b

# bar_datazoom_slider().render(r'Bar-DataZoom（slider-水平）.html')


# 20、Bar-DataZoom（slider-垂直）
def bar_datazoom_slider_vertical():
    b = (Bar()
         .add_xaxis(Faker.days_attrs)
         .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-垂直）"),
            datazoom_opts=opts.DataZoomOpts(orient="vertical")))
    return b

# bar_datazoom_slider_vertical().render(r'Bar-DataZoom（slider-垂直）.html')


# 21、Bar-DataZoom（inside）
def bar_datazoom_inside():
    b = (Bar()
         .add_xaxis(Faker.days_attrs)
         .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（inside）"),
            datazoom_opts=opts.DataZoomOpts(type_="inside")))
    return b

# bar_datazoom_inside().render(r'Bar-DataZoom（inside）.html')


# 22、Bar-DataZoom（slider+inside）
def bar_datazoom_both():
    b = (Bar()
         .add_xaxis(Faker.days_attrs)
         .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider+inside）"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]))
    return b

# bar_datazoom_both().render(r'Bar-DataZoom（slider+inside）.html')


# 23、Bar-直方图
def bar_histogram():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), category_gap=0, color=Faker.rand_color())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-直方图")))
    return b

# bar_histogram().render('Bar-直方图.html')


# 24、Bar-直方图（颜色区分）
def bar_histogram_color():
    x = Faker.dogs + Faker.animal
    xlen = len(x)
    y = []
    for idx, item in enumerate(x):
        if idx <= xlen / 2:
            y.append(
                opts.BarItem(
                    name=item,
                    value=(idx + 1) * 10,
                    itemstyle_opts=opts.ItemStyleOpts(color="#749f83")))
        else:
            y.append(
                opts.BarItem(
                    name=item,
                    value=(xlen + 1 - idx) * 10,
                    itemstyle_opts=opts.ItemStyleOpts(color="#d48265")))
    b = (Bar()
         .add_xaxis(x)
         .add_yaxis("series0", y, category_gap=0, color=Faker.rand_color())
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-直方图（颜色区分）")))
    return b

# bar_histogram_color().render(r'Bar-直方图（颜色区分）.html')


# 25、Bar-旋转 X 轴标签
def bar_rorate_xaxis_label():
    b = (Bar()
         .add_xaxis(["名字很长的X轴标签1",
                     "名字很长的X轴标签2",
                     "名字很长的X轴标签3",
                     "名字很长的X轴标签4",
                     "名字很长的X轴标签5",
                     "名字很长的X轴标签6"])
         .add_yaxis("商家A", [10, 20, 30, 40, 50, 40])
         .add_yaxis("商家B", [20, 10, 40, 30, 40, 50])
         .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title="Bar-旋转X轴标签", subtitle="解决标签名字过长的问题")))
    return b

# bar_rorate_xaxis_label().render(r'Bar-旋转X轴标签.html')


# 26、Bar-Graphic 组件示例
def bar_graphic_component():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Graphic 组件示例"),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=110,
                        bottom=110,
                        z=100),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_shape_opts=opts.GraphicShapeOpts(width=400, height=50),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="rgba(0,0,0,0.3)")),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text="pyecharts bar chart",
                                font="bold 26px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="#fff")))])]))
    return b

# bar_graphic_component().render(r'Bar-Graphic组件示例.html')


# 27、Bar-Graphic (Rect + Text) 组件示例 1
def bar_graphic_rect_text_one_component():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Graphic Rect+Text 1 组件示例"),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=110,
                        bottom=110,
                        z=100),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_shape_opts=opts.GraphicShapeOpts(width=400, height=50),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="rgba(0,0,0,0.3)")),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(left="center", top="center", z=100),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text="pyecharts bar chart",
                                font="bold 26px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="#fff")))])]))
    return b

# bar_graphic_rect_text_one_component().render(r'Bar-Graphic(Rect + Text)组件示例1.html')        # 跟上一个组件的代码是一样的


# 28、Bar-Graphic (Rect + Text) 组件示例 2
def bar_graphic_rect_text_two_component():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Graphic Rect+Text 2 组件示例"),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(left="50%", top="15%"),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(z=100, left="center", top="middle"),
                            graphic_shape_opts=opts.GraphicShapeOpts(width=190, height=90),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="#fff",
                                stroke="#555",
                                line_width=2,
                                shadow_blur=8,
                                shadow_offset_x=3,
                                shadow_offset_y=3,
                                shadow_color="rgba(0,0,0,0.3)")),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(left="center", top="middle", z=100),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text=JsCode(
                                    "['横轴表示数据类别',"
                                    "'纵轴表示数值的值',"
                                    "'这个文本块可以放在图中各',"
                                    "'种位置'].join('\\n')"),
                                font="14px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="#333")))])]))

    return b

# bar_graphic_rect_text_two_component().render(r'Bar-Graphic(Rect + Text)组件示例2.html')


# 29、Bar-Graphic (Image) 组件示例
def bar_graphic_image_component():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Graphic Image 组件示例"),
            graphic_opts=[
                opts.GraphicImage(
                    graphic_item=opts.GraphicItem(
                        id_="logo", right=20, top=20, z=-10, bounding="raw", origin=[75, 75]),
                    graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                        image="https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3498742115,1467852641&fm=26&gp=0.jpg",
                        width=150, height=150, opacity=0.4))]))
    return b

# bar_graphic_image_component().render(r'Bar-Graphic(Image)组件示例.html')


# 30、Bar-Graphic (Image-Rotate) 组件示例
def bar_graphic_image_with_js_component():
    bar = (
        Bar(init_opts=opts.InitOpts(chart_id="1234"))
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Graphic Image（旋转功能）组件示例"),
            graphic_opts=[
                opts.GraphicImage(
                    graphic_item=opts.GraphicItem(
                        id_="logo", right=20, top=20, z=-10, bounding="raw", origin=[75, 75]),
                    graphic_imagestyle_opts=opts.GraphicImageStyleOpts(
                        image="https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3498742115,1467852641&fm=26&gp=0.jpg",
                        width=150, height=150, opacity=0.4))]))
    b = (Grid(init_opts=opts.InitOpts(chart_id="1234"))
         .add(chart=bar, grid_opts=opts.GridOpts(pos_left="5%", pos_right="4%", pos_bottom="5%"))
         .add_js_funcs("""
            var rotation = 0;
            setInterval(function () {
                chart_1234.setOption({
                    graphic: {id: 'logo',
                              rotation: (rotation += Math.PI / 360) % (Math.PI * 2)}});
                              },30);
        """))
    return b

# bar_graphic_image_with_js_component().render(r'Bar-Graphic(Image-Rotate)组件示例.html')


# 31、Bar-Brush 示例
def bar_with_brush():
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values())
         .add_yaxis("商家B", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-Brush 示例", subtitle="我是副标题"),
            brush_opts=opts.BrushOpts()))
    return b

# bar_with_brush().render(r'Bar-Brush示例.html')


# 32、Bar-自定义柱状颜色
def bar_custom_bar_color():
    color_function = """
        function (params) {
            if (params.value > 0 && params.value < 50) {
                return 'red';
            } else if (params.value > 50 && params.value < 100) {
                return 'blue';
            }
            return 'green';
        }
        """
    b = (Bar()
         .add_xaxis(Faker.choose())
         .add_yaxis("商家A", Faker.values(), itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))
         .add_yaxis("商家B", Faker.values(), itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))
         .add_yaxis("商家C", Faker.values(), itemstyle_opts=opts.ItemStyleOpts(color=JsCode(color_function)))
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-自定义柱状颜色")))
    return b

# bar_custom_bar_color().render(r'Bar-自定义柱状颜色.html')



