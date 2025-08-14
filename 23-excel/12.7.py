import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb.active
ft = Font(size=24,italic=True)
sheet['a1'].font = ft
sheet['A1'] = 'Hello World'
wb.save('example5.xlsx')