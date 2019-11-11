# import json

# with open('datajson.json', 'r') as x:
#     out = json.load(x)

# print(type(out))
# print(type(out[0]))
# print(out)

import json

#baca
with open('datajson.json', 'r') as x:
    out = json.load(x)

#nulis
with open('datahaha.json', 'w') as y:
    json.dump(out,y)


##manual / pakai package csv json:
# 1. csv=> json
# 2. json=>csv