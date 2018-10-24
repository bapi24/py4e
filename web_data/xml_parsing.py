import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>Margo</name>
        </user>
</stuff>'''

try:
    stuff = ET.fromstring(input)
except ET.ParseError as e:
    print("XML file is invalid\n\n")
    print(e)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name: ', item.find('name').text)
    print('Id: ', item.find('id').text)
    print('Attribute: ', item.get("x"))