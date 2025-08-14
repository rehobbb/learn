import openpyxl  # 导入 openpyxl 库，用于操作 Excel 文件
wb = openpyxl.load_workbook('example1.xlsx')  # 加载名为 example1.xlsx 的 Excel 文件
sheet = wb.active  # 获取当前活动工作表
print(sheet.title)  # 打印当前活动工作表的标题
sheet.title = 'hahahahaha'  # 将当前活动工作表的标题修改为 'hahahahaha'
print(sheet.title)  # 打印修改后当前活动工作表的标题
wb.save('example2.xlsx')  # 将修改后的工作簿保存为 example2.xlsx 文件
