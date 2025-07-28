import alldata  # 导入 alldata 模块
state = input('please input the state:')  # 提示用户输入州名，并将输入内容赋值给 state 变量
county = input('please input the county:')  # 提示用户输入县名，并将输入内容赋值给 county 变量
tracks1 = alldata.alldata[state][county]['tracks']  # 根据用户输入的州名和县名，从 alldata 中获取对应的轨道数量
pop1 = alldata.alldata[state][county]['pop']  # 根据用户输入的州名和县名，从 alldata 中获取对应的人口数量
print(f'the {county} has {tracks1} tracks' )  # 打印指定县的轨道数量
print(f'the {county} has {pop1} people' )  # 打印指定县的人口数量
for state in alldata.alldata:  # 遍历 alldata 中的所有州
    for county in alldata.alldata[state]:  # 遍历当前州下的所有县
        print(state,county,alldata.alldata[state][county]['tracks'],alldata.alldata[state][county]['pop'])  # 打印每个州、县的轨道数量和人口数量
