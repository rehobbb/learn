import openpyxl  # 导入 openpyxl 库，用于操作 Excel 文件
wb = openpyxl.Workbook()  # 创建一个新的 Excel 工作簿对象
print(wb.sheetnames)  # 打印工作簿中所有工作表的名称
sheet = wb['Sheet']  # 获取工作簿中名为 'Sheet' 的工作表
sheet['a1'] = 'hello world'  # 在工作表的 A1 单元格中写入 'hello world'
print(sheet['a1'].value)  # 打印工作表 A1 单元格的值
wb.save('example4.xlsx')