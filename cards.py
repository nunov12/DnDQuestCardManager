""" Classes And Main Actions
Card : represented structure
    Spell :
            "name", "level", "school",
            "time", "range", "components",
            "duration", "classes", "text",
            "roll", "ritual",
    Monster :
            "name", "size", "type",
            "alignment", "ac", "hp",
            "speed", "str", "dex",
            "con", "int", "wis",
            "cha", "skill", "senses",
            "passive", "languages",
            "cr", "trait", "action",
            "spells", "slots",
            "reaction", "resist",
            "immune", "conditionImmune",
            "vulnerable", "save",
            "legendary", "description",
    Quest :
            Compilation of settings
    Setting :
            "Place", "Description"
            "Monster", "Items"
            "Maps", "CR"

Actions
    Attack_Roll
    Damage_Roll
"""
# pylint: disable=too-many-instance-attributes

from random import randrange


def roll_dmg(dice):
    """Roll for Damage"""
    num, ran = dice.split("d")
    return sum(randrange(int(ran)) + 1 for _ in range(int(num)))


class Card:
    "Class that represents a Card"

    def __init__(self, name, taipe):
        self._name = name
        self._type = taipe

    def write_card(self):
        "Write to Flask"

    def update_card(self):
        "Change Card"
