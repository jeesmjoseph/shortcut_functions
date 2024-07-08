import json
import os

def make_json(file_name,files):
    output_file = file_name+'.json'
    data = {k:v for (k,v) in zip(['key'],files)}
    print(data)
    with open(output_file,'w',encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data,indent=4))


file_name = input("Enter name you want to give for output file :")
filepath = input("Enter the folder path :")
files = os.listdir(filepath)
make_json(file_name,files)
