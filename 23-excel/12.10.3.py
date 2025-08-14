import openpyxl
wb = openpyxl.load_workbook('../produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'a2'
wb.save('../produceSales.xlsx')