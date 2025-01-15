import pandas as pd

FOLDER = 'Tournament_Results'

data = pd.read_csv(f'data/{FOLDER}/{FOLDER.lower()}.csv', encoding='utf-8')
try:
    data.drop(columns = 'Unnamed: 1', inplace = True)
except:
    pass
data.dropna(subset=['RANK', 'PLAYER'], inplace=True)
data.drop(data[data['RANK'] == 'RANK'].index, inplace=True)
data.replace('-', 0, inplace=True)
data.to_csv(f'data/{FOLDER}/{FOLDER.lower()}.csv', index=False)