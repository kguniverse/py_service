
class Data:

    def getdata():
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
