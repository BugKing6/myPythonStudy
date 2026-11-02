import pandas as pd
import xgboost as xgb
import sklearn as sk

# 读取 Excel 文件
excel_file = pd.read_excel('C:\\Users\\杨粤\\Documents\\资料\\春.xlsx')
df = excel_file.parse('300')

# 查看数据的基本信息和前几行
print('数据基本信息：')
df.info()

# 查看数据集行数和列数
rows, columns = df.shape

if rows < 100 and columns < 20:
    # 短表数据（行数少于100且列数少于20）查看全量数据信息
    print('数据全部内容信息：')
    print(df.to_csv(sep='\t', na_rep='nan'))
else:
    # 长表数据查看数据前几行信息
    print('数据前几行内容信息：')
    print(df.head().to_csv(sep='\t', na_rep='nan'))

