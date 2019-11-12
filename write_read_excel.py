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
print(sheet1.merged_cells)
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




