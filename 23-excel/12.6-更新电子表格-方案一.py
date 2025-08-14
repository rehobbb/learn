import openpyxl  # 导入 openpyxl 库，用于操作 Excel 文件
wb = openpyxl.load_workbook('../produceSales.xlsx')  # 加载指定路径的 Excel 文件
sheet = wb['Sheet']  # 获取名为 'Sheet' 的工作表
for row in range(2, sheet.max_row+1):  # 遍历工作表中的每一行，从第 2 行开始
    name = sheet['a'+str(row)].value  # 获取当前行 A 列单元格的值
    if name == 'Garlic':  # 如果当前行 A 列的值为 'Garlic'
        sheet['b'+str(row)] = 100  # 将当前行 B 列的值设置为 100
    elif name == 'Celery':  # 如果当前行 A 列的值为 'Celery'
        sheet['b'+str(row)] = 200  # 将当前行 B 列的值设置为 200
    elif name == 'Lemon':  # 如果当前行 A 列的值为 'Lemon'
        sheet['b'+str(row)] = 300  # 将当前行 B 列的值设置为 300
    else:  # 如果不满足以上条件
        continue  # 跳过当前循环，继续下一次循环
wb.save('../produceSales2.xlsx')  # 将修改后的工作簿保存到指定路径
