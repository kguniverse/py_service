from sanic import Sanic 
from sanic.response import json
from sanic.response import text
from sanic.response import file
from sanic import request
import csv
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

import Dao


app = Sanic("Myapp")
data = []

def Dao():
    with open("asset/test.txt", "r") as f:
        line = f.readline()
        while line:
            if line[0] == '#':
                line = f.readline()
                continue
            items = line.strip().split()
            dic_items = {'Year': int(items[0]), 'Temperature': float(items[1])}
            data.append(dic_items)
            line = f.readline()
    pass

@app.get('/data')
def handler(request):
    # return text('hello world')
    key = request.args.get('key', 'Year')
    form = request.args.get('form', 'json')
    sub_data = []
    if request.args.get('reverse') == 'true':
        sub_data = sorted(data[int(request.args.get('beginYear', 1880)) - 1880: int(request.args.get('endYear', 2010)) - 1879],\
                    key=lambda x:x[key], reverse=True)
    else:
        sub_data = sorted(data[int(request.args.get('beginYear', 1880)) - 1880: int(request.args.get('endYear', 2010)) - 1879],\
                    key=lambda x:x[key])
    
    if form == 'json':
        return json(sub_data)
    elif form == 'xml':
        return text(parseString(dicttoxml(sub_data).decode('utf-8')).toprettyxml(indent=' '))
    elif form == 'csv':
        fileName = 'data_csv.csv'
        fieldnames=sub_data[0].keys() 
        with open(fileName,"w") as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow(fieldnames)
            for dict in sub_data:
                writer.writerow(dict.values())
        return file(fileName)
    return text("parse failed")

def test_dao(beginYear: int, endYear: int):
    sub_data = sorted(data[beginYear - 1880: endYear - 1880], key=lambda x:x['Lowess'], reverse=True) 
    print(sub_data.__str__())


if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=1337)
    # test_dao(2001, 2005)
