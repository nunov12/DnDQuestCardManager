import xml.etree.ElementTree as ET

Class Spell():
    def __init__(self, text):
        self.Description = text

def import_spells(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()

    for child in root:
        print(child.tag, child.attrib)

file = "Utils/Data/Spells/PHBSpells.xml"
import_spells(file)
