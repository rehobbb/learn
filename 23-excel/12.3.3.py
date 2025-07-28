import openpyxl  # 导入 openpyxl 库，用于操作 Excel 文件
wb = openpyxl.load_workbook('./doc/example.xlsx')  # 加载指定路径下的 Excel 文件
sheet = wb['Sheet1']  # 获取名为 'Sheet1' 的工作表
print(sheet['a1'])
print(sheet['a1'].value)
c = sheet['b1']  # 获取工作表中 B1 单元格对象
print(c.value)
str = f'row {c.row},column {c.column} is {c.value}'  # 格式化字符串，包含单元格的行号、列号和值
print(str)
str2 = f'cell {c.coordinate} is {c.value}'  # 格式化字符串，包含单元格的坐标和值
print(str2)
print(sheet['c1'].value)
