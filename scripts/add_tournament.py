from datetime import datetime
from dateutil import parser
import pandas as pd
import os

TABLE = 'SG_T2G'
FILE_DIRECTORY = f'data/{TABLE}/'

for i in os.listdir(FILE_DIRECTORY):
    df = pd.read_csv(FILE_DIRECTORY + i)
    tournament = i.split(f'_{TABLE}')[0].split('_')
    if '-' in tournament[0]: #Try to infer year
        years = tournament[0].split('-')
        if datetime.weekday(parser.parse(years[0] + ' ' + tournament[1])) > datetime.weekday(parser.parse(years[1] + ' ' + tournament[1])):
            tournament[0] = years[0]
        else:
            tournament[0] = years[1]
    df['TOURNAMENT_DATE'] = datetime.strftime(parser.parse(tournament[0] + ' ' + tournament[1]), "%Y-%m-%d")
    df['TOURNAMENT_NAME'] = tournament[2]
    df.to_csv(FILE_DIRECTORY + i, index=False)