from pyecharts.charts import Line, Bar
from pyecharts import options as opts
from example.commons import Faker


# 层叠多图
# 1、Overlap-层叠多图
def overlap_bar_line():
    x = Faker.choose()
    bar = (Bar()
           .add_xaxis(x)
           .add_yaxis('商家A', Faker.values())
           .add_yaxis('商家B', Faker.values())
           .set_global_opts(title_opts=opts.TitleOpts(title='Overlap-bar-line')))
    line = (Line()
            .add_xaxis(x)
            .add_yaxis('商家A', Faker.values())
            .add_yaxis('商家B', Faker.values()))
    bar.overlap(line)
    return bar

# overlap_bar_line().render(r'Overlap-层叠多图.html')


# 2、Overlap-bar+line（双 Y 轴）
zengfaliang =  [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
jiangshuiliang = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
average_wendu = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
def overlap_bar_line_double_y():
    bar = (Bar()
           .add_xaxis(Faker.months)
           .add_yaxis('蒸发量', zengfaliang)
           .add_yaxis('降水量', jiangshuiliang)
           .extend_axis(
                yaxis=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} °C"), interval=5))
           .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
           .set_global_opts(
                title_opts=opts.TitleOpts(title='Overlap-bar+line(双 Y 轴)'),
                yaxis_opts=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(formatter="{value} ml"))))
    line = Line().add_xaxis(Faker.months).add_yaxis('平均温度', average_wendu, yaxis_index=1)
    bar.overlap(line)
    return bar

overlap_bar_line_double_y().render(r'Overlap-bar+line(双 Y 轴).html')


