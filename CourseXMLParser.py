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
    ret = xml.find(f"./veranstaltung/[guid='{guid}']")
    return ET.tostring(ret, encoding="utf-8", method="xml", short_empty_elements=True).decode("utf-8")


def get_courses_for_user(username):
    ret = {}
    i = 1
    elements = xml.findall(f"./veranstaltung/buchung/[kunde='{username}']")
    for child in elements:
        guid = child.find("guid").text
        name = child.find("name").text
        ret.update({f"Kurs-{i}": {"GUID": guid, "Name": name}})
        i += 1
    return json.dumps(ret)


def book_course(guid, username):
    course = xml.find(f"./veranstaltung/[guid='{guid}']")
    b = course.find("buchung")
    if not b:
        b= ET.SubElement(course, "buchung")
    k = b.find(f"[kunde = '{username}']")
    if not k:
        k = ET.SubElement(b,"kunde")
        k.text = username
    save()


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
    global xml
    xml.write(SOURCE)
    xml = ET.parse(SOURCE)


def parse_xml():
    save()
    with open(SOURCE) as f:
        return f


def parse_schema():
    with open("schemaKurse.xsd") as f:
        return f.read()


if __name__ == '__main__':
    book_course(617524, "Hans-Peter")
    pass
