# Fill in this file with the code from parsing JSON exercise


import json
import yaml


with open('nms.json','r') as json_file:
    ourjson = json.load(json_file)

#print("\n\n---")
#print(yaml.dump(ourjson))

#print(ourjson['result'])
#del ourjson['result']

ourjson['result']['test'] = 123
print(ourjson)

with open('nms_changed.json','w') as file:
    json.dump(ourjson,file,indent=2)
