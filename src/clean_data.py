import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Folder to clean')
parser.add_argument('--variable', type=str, help='Variable to download',
                    choices=['SG_Total', 'SG_T2G', 'Birdie_Bogey_Ratio', 'Birdies', 'Bogeys', 'Driving_Distance',
                             'Driving_Accuracy', 'Tournament_Results'], default='SG_Total')
args = parser.parse_args()
FOLDER = args.variable

data = pd.read_csv(f'data/{FOLDER}/{FOLDER.lower()}.csv', encoding='utf-8')
try:
    data.drop(columns = 'Unnamed: 1', inplace = True)
except:
    pass
data.dropna(subset=['RANK', 'PLAYER'], inplace=True)
data.drop(data[data['RANK'] == 'RANK'].index, inplace=True)
data.replace('-', 0, inplace=True)
data.replace({'%': ''}, inplace=True, regex=True)
data.to_csv(f'data/{FOLDER}/{FOLDER.lower()}.csv', index=False)