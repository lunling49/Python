from pyecharts.charts import EffectScatter, Grid
from pyecharts import options as opts
from example.commons import Faker
from pyecharts.globals import SymbolType


# 涟漪特效散点图
# 1、EffectScatter-基本示例
def effectscatter_base():
    e = (EffectScatter()
         .add_xaxis(Faker.choose())
         .add_yaxis("", Faker.values())
         .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-基本示例")))
    return e

# effectscatter_base().render(r'EffectScatter-基本示例.html')


# 2、EffectScatter-显示分割线
def effectscatter_splitline():
    e = (EffectScatter()
         .add_xaxis(Faker.choose())
         .add_yaxis("", Faker.values())
         .set_global_opts(
            title_opts=opts.TitleOpts(title="EffectScatter-显示分割线"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True))))
    return e

# effectscatter_splitline().render(r'EffectScatter-显示分割线.html')


# 3、EffectScatter-不同Symbol
def effectscatter_symbol():
    e = (EffectScatter()
         .add_xaxis(Faker.choose())
         .add_yaxis("", Faker.values(), symbol=SymbolType.DIAMOND)
         .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-不同Symbol")))
    return e

effectscatter_symbol().render(r'EffectScatter-不同Symbol.html')

