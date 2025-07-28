import openpyxl  # 导入 openpyxl 库，用于操作 Excel 文件
wb = openpyxl.load_workbook('./doc/example.xlsx')  # 加载指定路径下的 Excel 文件
sheet = wb['Sheet1']  # 获取名为 'Sheet1' 的工作表
whole = sheet['A1':'C3']  # 获取工作表中 A1 到 C3 区域的所有单元格
print(whole)  # 打印获取到的单元格区域对象

for row in whole:  # 遍历单元格区域中的每一行
    for cell in row:  # 遍历当前行中的每一个单元格
        print(cell.coordinate, cell.value)  # 打印单元格的坐标和值
    print('-'*5 + 'end of row' + '-'*5)  # 打印分隔线，表示一行结束
column1 = list(sheet.columns)[1]
for cellcol in column1:
    print(cellcol.value)