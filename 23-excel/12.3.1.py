import openpyxl
wb = openpyxl.load_workbook('./doc/example.xlsx')
stname = wb.sheetnames
print(stname)
sheet = wb['Sheet3']
print(sheet.title)
another = wb.active
print(another)