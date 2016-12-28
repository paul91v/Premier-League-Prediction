# -*- coding: utf-8 -*-

import os
import settings
import pandas as pd

INPUT_HEADERS = ["Club_Name", "Total_Value", "Average_Value"]
OUTPUT_HEADERS = ['Club_Name', 'Average_Value']
current_dir = os.path.dirname(os.path.realpath('__file__'))

full_squad_path = str(current_dir + '\\' + settings.DATA_DIR + '\\' + settings.SQUAD_DATA_FILE)
#Importing Squad Data
squad_data = pd.read_csv(full_squad_path, encoding = "ISO-8859-1", header = None, index_col = False, names = INPUT_HEADERS)
squad_data['Average_Value'] = squad_data['Average_Value'].str[:5]
squad_data['Average_Value'] = squad_data['Average_Value'].str.replace(',','.').astype(float)
squad_data = squad_data.drop('Total_Value', 1)
squad_data.to_csv(os.path.join(current_dir,settings.PROCESSED_DIR,settings.SQUAD_DATA_FILE), sep = ',', header = OUTPUT_HEADERS, index = False)
print(squad_data)

#Importing Fixture & Results
results_data_path = str(current_dir + '\\' + settings.DATA_DIR + '\\' + settings.RESULTS_DATA_FILE)
results_data = pd.read_csv(results_data_path)
RESULTS_HEADERS = ["HomeTeam","AwayTeam","FTR"]
results_data = results_data[RESULTS_HEADERS]

def ReturnAvgValue(TeamName):
    bool = TeamName == squad_data.Club_Name
    return float(squad_data.Average_Value[bool])
    
results_data['HomeValue']=""
results_data['AwayValue']=""
for i in range(len(results_data)):
    results_data.HomeValue[i] = ReturnAvgValue(results_data.HomeTeam[i])
    results_data.AwayValue[i] = ReturnAvgValue(results_data.AwayTeam[i])
    
results_data.to_csv(os.path.join(current_dir, settings.PROCESSED_DIR, settings.RESULTS_DATA_FILE), sep =',', header = results_data.columns, index = False )

#Creating Test Data set
Test_Data = pd.read_csv(os.path.join(current_dir, settings.PROCESSED_DIR, settings.RESULTS_DATA_FILE))
Test_Data['Result'] = Test_Data['FTR']
Test_Data.drop(['HomeTeam','AwayTeam','FTR'], axis = 1, inplace = True)
Test_Data.to_csv(os.path.join(current_dir, settings.PROCESSED_DIR, 'train.csv'), sep = ',', header = Test_Data.columns, index = False)