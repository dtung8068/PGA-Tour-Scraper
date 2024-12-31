import pandas as pd
import os

TABLE = 'SG_T2G'
FILE_DIRECTORY = f'data/{TABLE}/'

for i in os.listdir(FILE_DIRECTORY):
    df = pd.read_csv(FILE_DIRECTORY + i)
    tournament = i.split(f'_{TABLE}')[0].split('_')
    df['TOURNAMENT_DATE'] = tournament[0] + ' ' + tournament[1]
    df['TOURNAMENT_NAME'] = tournament[2]
    df.to_csv(FILE_DIRECTORY + i, index=False)