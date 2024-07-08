import csv
import glob

def make_sql(file_name):
    output_file = file_name.split('.')[0]+'.sql' # create an sql output file with same name as input csv file
    with open(file_name) as csvf:
        next(csvf)
        csvreader = csv.reader(csvf)
        file = open(output_file,'w')
        for keys,values in csvreader:
            filedata = '--'+keys+'\n'+values
            file.write('\n'+filedata)
        file.close()


filepath = input("Enter folder location : ")
csvlist = glob.glob('*.csv')
for item in csvlist:
    make_sql(item)