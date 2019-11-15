import xlrd
import xlwt
from xlrd import xldate_as_tuple
from datetime import datetime, date


# xlrd 读取excel数据
"""
备注：不同的excel格式，创建的储存对象写法也不同
    获取xlsx格式的合并单元格 data = xlrd.open_workbook("test.xlsx")
    获取xls格式的合并单元格 data = xlrd.open_workbook("test.xls", formatting_info=True)
"""
data = xlrd.open_workbook(r'test_excel.xls', formatting_info=True)    # 打开excel表，并创建对象存储

# 通过对象可以得到各个sheet对象（excel文件可以有多个sheet，每个sheet就是一张表格）
sheet1 = data.sheet_by_index(0)         # 通过索引顺序获取表里的行列内容
sheet2 = data.sheet_by_name(u'2018年数据表')       # 通过名称获取表里的行列内容
sheet3 = data.sheets()[0]       # 通过索引顺序获取表里的行列内容
num = data.nsheets          # 获取sheet的数量
list = data.sheets()        # 获取所有sheet对象行列内容的列表
list1 = data.sheet_names()      # 获取所有sheet对象名称的列表

# print(sheet2)
# print(num)
# print(list)
# print(list1)

# 通过sheet对象可以获取各个单元格，每个单元格是一个cell对象
# 获取工作表的名称、行数、列数
name = sheet1.name
nrows = sheet1.nrows
ncols = sheet1.ncols
# print(name)
# print(nrows)
# print(ncols)

# 获取单元格的数据类型，3 种方法
"""
xlrd的数据类型：0--empty, 1--string, 2--number, 3--date, 4--boolean, 5--error
"""
a = sheet1.cell_type(2, 2)
b = type(sheet1.cell_value(2, 2))
c = sheet1.cell(2, 2).ctype
# print(a, b, c)


"""
1、默认从excel中取出的数据:数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，因此需做处理转换成想要的数据类型
2、date的ctype=3，这时需要使用xlrd的xldate_as_tuple来处理为date格式，先判断表格的ctype=3时xldate才能开始操作
"""
# 方法一
d1 = sheet1.cell_value(1, 4)
# print(d1)
date_value = xlrd.xldate_as_tuple(d1, data.datemode)
# print(date_value)
# print(date(*date_value[:3]))
# print(datetime(*date_value))
# print(datetime(*date_value).strftime('%Y/%m/%d %H-%M-%S'))

# 方法二
date_v = datetime(*xldate_as_tuple(d1, 0))
# print(date_v)
# print(date_v.strftime('%Y.%m.%d %H-%M-%S'))


# 获取单元格内容的 3 种方式
v1 = sheet1.cell(1, 1).value
v2 = sheet1.cell_value(1, 1)
v3 = sheet1.row(1)[1].value
# print(v1, v2, v3)

# 获取行的列表
r1 = sheet1.row(1)
r2 = sheet1.row_slice(1)
r3 = sheet1.row_values(1)
r4 = sheet1.row_types(1)    # 获取该行中所有单元格的数据类型组成的列表
r5 = sheet1.row_len(1)      # 获取该行的有效单元格长度
# print(r1)
# print(r2)
# print(r3)
# print(r4)
# print(r5)

# 获取列的列表
c1 = sheet1.col(1)
c2 = sheet1.col_slice(1)
c3 = sheet1.col_values(1)
c4 = sheet1.col_types(1)
# print(c1)
# print(c2)
# print(c3)
# print(c4)


# 读取合并单元格的数据 merged_cells()
"""
merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range),
其中[row,row_range)包括row,不包括row_range,col也是一样，
即(1, 3, 4, 5)的含义是：第1到2行（不包括3）合并，(7, 8, 2, 5)的含义是：第2到4列合并。
"""
# print(sheet1.merged_cells)
# print(sheet1.cell_value(5, 1))
# print(sheet1.cell_value(7, 1))
# print(sheet1.cell_value(2, 3))
# print(sheet1.cell_value(3, 1))
# 总结：写入最小的row和col低位索引即可获得合并单元格数据
# 简化代码
# merge = []
# for (rlow, rligh, clow, chigh) in sheet1.merged_cells:
#     merge.append([rlow, clow])
# for index in merge:
#     print(sheet1.cell_value(index[0], index[1]))



# xlwt 写数据到excel
workbook = xlwt.Workbook(encoding='utf-8')      # 创建一个workbook并设置编码
worksheet = workbook.add_sheet('test')          # 创建一个worksheet
style = xlwt.XFStyle()          # 初始化样式
font = xlwt.Font()      # 为样式创建字体
font.name = 'Times New Roman'
font.underline = True       # 下划线
font.bold = True        # 黑体
font.italic = True      # 斜体
style.font = font       # 设定样式

# # 写入excel，参数对应行、列、值
# worksheet.write(1, 0, 'try to create a excel')      # 写入一个单元格数据，不带样式写入
#
rows = ['item', 'swim', 'run', 'ski', 'walk']       # 写入多个单元格数据，不带样式写入
cols = ['time', 'score', 'number']
for i in range(len(rows)):
    worksheet.write(i, 0, rows[i])
for j in range(1, len(cols)+1):
    worksheet.write(0, j, cols[j-1])
#
# worksheet.write_merge(3, 5, 1, 3, 'Second Merge', style)    # 带样式写入合并单元格，与读取合并单元格不同的是，单元格区间是左右闭合的，不是左开右闭
# workbook.save('create_excel.xls')       # 保存文件

# 设置单元格列宽度、行高度
# worksheet.col(0).width = 3333           # 列宽设置方法一
# worksheet.col(1).width = 256 * 20       # 列宽设置方法二：256为衡量单位，20表示20个字符宽度
# 行高度，行宽是在单元格的样式中设置的，可以通过自动换行、通过输入文字的多少来确定行高
# row_height_style = xlwt.easyxf('font:height 720')
# worksheet.row(0).set_style(row_height_style)
# 行高设置方法二，行高的基本单位为20
# worksheet.row(0).height_mismatch = True
# worksheet.row(0).height = 20*40

# 写入日期到单元格
style.num_format_str = 'YYYY/M/D'       # 日期样式设置
worksheet.write(1, 1, datetime.now(), style)    # style必须写，不然是时间是一串数字

# 添加公式--Formula()
# worksheet.write(2, 2, 3)
# worksheet.write(3, 2, 4)
# worksheet.write(4, 2, xlwt.Formula('C3*C4'))
# worksheet.write(4, 3, xlwt.Formula('SUM(C3,C4)'))

# 添加超链接
# worksheet.write(4, 4, xlwt.Formula('HYPERLINK("https://www.baidu.com";"百度")'))

# 设置单元格内容的对齐方式
# alignment = xlwt.Alignment()
# alignment.horz = xlwt.Alignment.HORZ_CENTER
# alignment.vert = xlwt.Alignment.VERT_CENTER
# style.alignment = alignment
# worksheet.write(4, 4, 'I don\'t know', style)

# 添加边框
# borders = xlwt.Borders()
# borders.left = xlwt.Borders.DASHED      # DASHED-虚线，NO_LINE-没有，THIN-实线
# borders.right = xlwt.Borders.THIN
# borders.top = xlwt.Borders.NO_LINE
# borders.bottom = xlwt.Borders.MEDIUM
# borders.left_colour = 0*40
# style.borders = borders
# worksheet.write(4, 5, 'python', style)

# 设置单元格背景色
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# pattern.pattern_fore_colour = 5       # 设置背景色方法一
pattern.pattern_fore_colour = xlwt.Style.colour_map['dark_blue']        # 设置背景色方法二
style.pattern = pattern
worksheet.write(4, 6, 'success', style)

workbook.save('create_excel.xls')

