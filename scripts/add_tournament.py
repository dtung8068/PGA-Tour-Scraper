from datetime import datetime
from dateutil import parser
import pandas as pd
import os

TABLE = 'Driving_Distance'
FILE_DIRECTORY = f'data/{TABLE}/'

files = [i for i in os.listdir(FILE_DIRECTORY)]
files.sort(key=lambda x: os.path.getctime(os.path.join(FILE_DIRECTORY, x)))

current_year = '2004'

for i in files:
    df = pd.read_csv(FILE_DIRECTORY + i, encoding='unicode-escape')
    tournament = i.split(f'_{TABLE}')[0].split('_')
    if '-' in tournament[0]:
        years = tournament[0].split('-')
        if 'Jan' in tournament[1]:
            current_year = years[1]
    else:
        current_year = tournament[0]
    df['TOURNAMENT_DATE'] = datetime.strftime(parser.parse(current_year + ' ' + tournament[1]), "%Y-%m-%d")
    df['TOURNAMENT_NAME'] = tournament[2]
    df.to_csv(FILE_DIRECTORY + i, index=False)