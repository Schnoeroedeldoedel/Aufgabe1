# Validate XML using xmlschema and ElementTree

# Requires: pip3 install xmlschema

import xmlschema, xml.etree.ElementTree as ET

xml = ET.parse("Kurse_snippet.xml")
xsd = xmlschema.XMLSchema("test.xsd")


def is_valid():
    valid = xsd.is_valid(xml)
    print(valid)


def get_courses():
    list = []
    for child in xml.getroot():
        guid = child.find("guid").text
        name = child.find("name").text
        list.append((guid, name))
    return list


if __name__ == '__main__':
    print(is_valid())
    print(get_courses())
