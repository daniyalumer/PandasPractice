#Getting all the column names

import csv

with open('sample_grpr_input.csv', 'r') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    column_names_list=[]
    for row in csv_reader:
        column_names_list.append(row)
        break

print(column_names_list)
        
class Node:
    index=None
    keyword=None
    country=None
    difficulty=None
    volume=None
    cpc=None
    cps=None
    parentkeyword=None
    lastupdate=None
    serpfeatures=None
    globalvolume=None
    trafficpotential=None

    

nodes_list=[]
with open('sample_grpr_input.csv', 'r') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        obj=Node()
        obj.index=row[0]
        obj.keyword=row[1]
        obj.country=row[2]
        obj.difficulty=row[3]
        obj.volume=row[4]
        obj.cpc=row[5]
        obj.cps=row[6]
        obj.parentkeyword=row[7]
        obj.lastupdate=row[8]
        obj.serpfeatures=row[9]
        obj.globalvolume=row[10]
        obj.trafficpotential=row[11]
        nodes_list.append(obj)

for row in nodes_list:
    print(row.index + ',' + row.keyword + ',' + row.country + ',' + row.difficulty + ',' + row.volume + ',' + row.cpc + ',' + row.cps + ',' + row.parentkeyword + ',' + row.lastupdate + ',' + row.serpfeatures + ',' + row.globalvolume + ',' + row.trafficpotential)
