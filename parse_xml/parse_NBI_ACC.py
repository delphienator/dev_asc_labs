import xml.etree.ElementTree as ET
import re

xml = ET.parse("/home/devasc/dev_asc_labs/NBI_ACC.xml")
root = xml.getroot()
#print('root name: ', root)
root_tag = re.match('{.*}', root.tag).group(0)
#print('root tag: ',root_tag)
body = root.find('{}Body'.format(root_tag))
#print('Body name:',body)
#print('Body tag: ',body.tag)


for child in body:
    create_appclass_tag = re.match('{.*}', child.tag).group(0)
    app_class = child.find('applicationClassification')
    table = app_class.find('fwdLinkIPv4ApplicationClassificationTable')
  
  # for each table instance need to find a specific element
    for instance in table:
        stopSourceIpAddress = instance.find('stopSourceIpAddress')
        print(stopSourceIpAddress.text)
        

 
    
    
