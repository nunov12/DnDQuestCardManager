""" Imports XML files into Spells DB
"""
import xml.etree.ElementTree as ET


class Spell:
    """ Spell class characterizes a spell with stat, roll and description"""

    def __init__(self, text):
        """Stats:
        *   Description :: String
        """
        self.description = text

    def roll(self):
        """Placeholder to roll for Damage"""

    def get_stats(self):
        """Placeholder to return Spells stats"""


def import_spells(file_name):
    """Import all spells from Utils/Data/Spells/*"""
    tree = ET.parse(file_name)
    root = tree.getroot()

    for child in root:
        print(child.tag, child.attrib)


FILE = "Utils/Data/Spells/PHBSpells.xml"
import_spells(FILE)
