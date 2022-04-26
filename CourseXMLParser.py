# Validate XML using xmlschema and ElementTree

# Requires: pip3 install xmlschema

import xmlschema, xml.etree.ElementTree as ET
import json

SOURCE = "Kurse.xml"

xml = ET.parse(SOURCE)
xsd = xmlschema.XMLSchema("schemaKurse.xsd")


def is_valid():
    valid = xsd.is_valid(xml)
    print(valid)

def parse_course(guid):
    ret = xml.find(f"veranstaltung[@GUID={guid}]")
    return ret


def parse_all_courses():
    ret = {}
    i = 1
    for child in xml.getroot():
        guid = child.find("guid").text
        name = child.find("name").text
        ret.update({f"Kurs-{i}": {"GUID": guid, "Name": name}})
        i += 1
    return json.dumps(ret)


def save():
    with open(SOURCE) as f:
        xml.write(f)


def parse_xml():
    save()
    with open(SOURCE) as f:
        return f


def parse_schema():
    with open("schemaKurse.xsd") as f:
        return f.read()
