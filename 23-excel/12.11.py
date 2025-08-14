import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1,11):
    sheet['a'+ str(i)] = i
refObj = openpyxl.chart.Reference(sheet,1,1,1,10)
seriObj = openpyxl.chart.Series(refObj,title='first series')
chartObj = openpyxl.chart.BarChart()
chartObj.title = 'my chart'
chartObj.append(seriObj)
sheet.add_chart(chartObj,'c5')
wb.save('samplechart.xlsx')