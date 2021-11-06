
def readCSV(file_path, column_delimeter=','):
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()
    obj = {}
    headers = lines[0].replace('\n','').split(column_delimeter)
    for line in lines[1:]:
        line = line.split(column_delimeter)
        obj[line[0]] = {}
        for header,i  in zip(headers[1:],range(1,len(headers))):
            obj[line[0]][header] = line[i].replace('\n','')
    return obj