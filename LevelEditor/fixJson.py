from tools import *

data = ImportLevel('level5')

for i in range(len(data)):
    data[i][4] = 1

with open('level5.json', 'w') as f:
    json.dump(data, f)
