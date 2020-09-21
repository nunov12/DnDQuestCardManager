" Imports XML files into Spells DB "

import os
import xml.etree.ElementTree as ET
from collections import deque, defaultdict


def import_spells(dir_name):
    """Import all spells from Utils/Data/Spells/*
    To import:
        _name=None,
        _level=None,
        _school=None,
        _time=None,
        _range=None,
        _components=None,
        _duration=None,
        _classes=None,
        _text=None,
        _roll=None,
        _ritual=None,
    """
    spellbook = deque()

    for file_name in os.listdir(dir_name):
        print(file_name)
        compendium = ET.parse(os.path.join(dir_name, file_name)).getroot()
        for spell in compendium:
            _stats = defaultdict(str)
            text = []
            for stat in spell:
                if "text" in stat.tag:
                    text.append(stat.text)
                else:
                    _stats[stat.tag] = stat.text
            _stats["text"] = "\n\n".join(filter(None, text))
            spellbook.append(_stats)
    return spellbook


def import_monsters(dir_name):
    """Import all monsters from Utils/Data/Zoo/*
    To import:
    """
    zookeeper = deque()
    for file_name in os.listdir(dir_name):
        print(file_name)
        compendium = ET.parse(os.path.join(dir_name, file_name)).getroot()
        for monster in compendium:
            _stats = defaultdict(str)
            text = []
            for stat in monster:
                if "text" in stat.tag:
                    text.append(stat.text)
                else:
                    _stats[stat.tag] = stat.text
            _stats["text"] = "\n\n".join(filter(None, text))
            zookeeper.append(_stats)
    return zookeeper


FILE = "Utils/Data/Spells/"
SPELL_BOOK = import_spells(FILE)
print(len(SPELL_BOOK))

FILE = "Utils/Data/Zoo/"
MONSTERNOMICON = import_monsters(FILE)
print(len(MONSTERNOMICON))
