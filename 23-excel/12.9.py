import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet['a1'] = 21
sheet['a2'] = 32
sheet['a3'] ='=sum(a1:a2)'
wb.save('formula.xlsx')