import os
import glob
import pandas as pd
#write the directory where you want to combine the csv files
os.chdir('')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#rename the first column
combined_csv = combined_csv.rename(columns={combined_csv.columns[0]:'COLUMN_NAME_COMBINE'})
#export to csv
combined_csv.to_csv('OUTPUT_FILENAME'+'.csv', index=False, encoding='utf-8-sig')
