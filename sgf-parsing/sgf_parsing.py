import re
from typing import List, Dict


class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string: str):
    if not input_string.startswith("(") or not input_string.endswith(")"):
        raise ValueError("Invalid format")
    input_string = input_string[1:-1]
    if input_string == ";":
        return SgfTree()
    input_string = re.sub("\\\\\\]", "*", input_string)
    maintree_props, *children = re.findall(
        r"(?<!\();\w(?:[\[\s\w*\\\]]+)+(?!\))", input_string
    )

    subtrees_props = re.findall(r"(?<=\()[^\)]+(?=\))", input_string) + children

    subtrees = None
    if subtrees_props:
        subtrees = [
            SgfTree(properties=_extract_node_info(prop)) for prop in subtrees_props
        ]

    maintrees = SgfTree(
        properties=_extract_node_info(maintree_props), children=subtrees or None
    )
    return maintrees


def _extract_node_info(node: str) -> Dict[str, List[str]]:
    node_info = {}
    properties = re.findall(r"(\w(?:\[[^][]+\])+)", node)
    for prop in properties:
        values = re.findall(r"\[([^][]+)\]", prop)
        [key] = re.findall(r"^(\w)", prop)
        if key.islower():
            raise ValueError(f"Lowercase property: {key}")
        values = [value.replace("*", "]").replace("\t", " ") for value in values]
        node_info[key] = values
    return node_info
