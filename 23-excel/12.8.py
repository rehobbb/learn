import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb.active
fontObj1 = Font(name='Times New Roman',bold=True)
sheet['a1'].font = fontObj1
sheet['a1'] = 'Bold Times New Roman'
fontObj2 = Font(size = 24,italic=True)
sheet['b2'].font = fontObj2
sheet['b2'] = '24 pt Italic'
wb.save('styles.xlsx')