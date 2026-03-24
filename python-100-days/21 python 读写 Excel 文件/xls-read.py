import xlrd
import os

print(os.path.abspath(__file__))

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '阿里巴巴2020年股票数据.xls')

# 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象（工作簿）
wb = xlrd.open_workbook(file_path)
# 通过Book对象的sheet_names方法可以获取所有表单名称
sheet_names = wb.sheet_names()

print(sheet_names)

sheet = wb.sheet_by_name(sheet_names[0])

print(sheet.nrows)
print(sheet.ncols)

for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell(row, col).value

        if row > 0:
            if col == 0:
                value = xlrd.xldate_as_tuple(value, 0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            else:
                value = f'{value:.2f}'

        print(value, end='\t')
    print()

# 获取最后一个单元格的数据类型
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
print(last_cell_type)

# 获取第一行的值（列表）
print(sheet.row_values(0))

# 获取指定行指定列范围的数据（列表）
# 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
print(sheet.row_slice(3, 0, 5))