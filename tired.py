import pandas as pd
datas = pd.read_csv("drugs.tsv", sep='\t')ñ
column_name = datas.rename(columns = {0:"old"})
print(column_name)
print(datas.info())
print(datas)