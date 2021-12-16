from pandas import *
import random
xls = ExcelFile('crop-dataset.xls')
df = xls.parse(xls.sheet_names[0])

TOLERANCE = {
    'Temp' : 0.05,
    'SM': 0.1,
    'Rain': 0.075,
    'Nitrogen': 0.01
}

for i in range(20):
    for index, row in df.iterrows():
        new_row = {}
        new_row['Temp-S'] = random.uniform(-1, 1) * TOLERANCE['Temp'] * row['Temp-S']
        new_row['Temp-G'] = random.uniform(-1, 1) * TOLERANCE['Temp'] * row['Temp-G']
        new_row['Temp-M'] = random.uniform(-1, 1) * TOLERANCE['Temp'] * row['Temp-M']
        new_row['Temp-Avg'] = random.uniform(-1, 1) * TOLERANCE['Temp'] * row['Temp-Avg']
        new_row['Rain-Avg'] = random.uniform(-1, 1) * TOLERANCE['Rain'] * row['Rain-Avg']
        new_row['SM-S'] = random.uniform(-1, 1) * TOLERANCE['SM'] * row['SM-S']
        new_row['SM-G'] = random.uniform(-1, 1) * TOLERANCE['SM'] * row['SM-G']
        new_row['SM-M'] = random.uniform(-1, 1) * TOLERANCE['SM'] * row['SM-M']
        new_row['SM-Avg'] = random.uniform(-1, 1) * TOLERANCE['SM'] * row['SM-Avg']
        new_row['Nitrogen'] = random.uniform(-1, 1) * TOLERANCE['Nitrogen'] * row['Nitrogen']
        new_row['Suitability'] = row['Suitability']
        df = df.append(new_row, ignore_index = True)
        
display(df)