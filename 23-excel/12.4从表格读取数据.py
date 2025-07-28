import pprint  # 导入pprint模块，用于美观地打印数据结构
import openpyxl  # 导入openpyxl模块，用于处理Excel文件
wb = openpyxl.load_workbook("censuspopdata.xlsx")  # 加载名为censuspopdata.xlsx的Excel工作簿
sheet = wb.active  # 获取当前活动工作表
censusdata = {}  # 初始化一个空字典，用于存储人口普查数据
for row in range(2, sheet.max_row + 1):  # 遍历工作表中从第2行到最后一行的数据
    state = sheet['B' + str(row)].value  # 获取当前行B列的值，作为州名
    county = sheet['C' + str(row)].value  # 获取当前行C列的值，作为县名
    pop = sheet['D' + str(row)].value  # 获取当前行D列的值，作为人口数量
    censusdata.setdefault(state, {})  # 如果州名不在字典中，则添加该州名并初始化为空字典
    censusdata[state].setdefault(county, {'tracks': 0, 'pop': 0})  # 如果县名不在对应州的字典中，则添加该县名并初始化统计信息
    censusdata[state][county]['tracks'] += 1  # 对应县的统计记录数加1
    censusdata[state][county]['pop'] += int(pop)  # 对应县的人口总数加上当前行的人口数量
with open('./learn/23-excel/alldata.py', 'w') as alldata:  # 以写入模式打开alldata.py文件
    alldata.write('alldata = ' + pprint.pformat(censusdata))  # 将处理好的人口普查数据格式化后写入文件，并添加变量名alldata

