# Validate XML using xmlschema and ElementTree

# Requires: pip3 install xmlschema

import xmlschema, xml.etree.ElementTree as ET
xml = ET.parse("Kurse_snippet.xml")
xsd = xmlschema.XMLSchema("test.xsd")

valid = xsd.is_valid(xml)
print(valid)

