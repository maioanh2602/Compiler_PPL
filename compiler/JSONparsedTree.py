import json


class Node:
    def __init__(self, node_name, child_name=None):
        self.text = {"name": node_name}
        # self.image = "../treant-js-master/background.jpg"
        if child_name is not None:
            self.children = child_name
        else:
            self.children = []


class ParsedTreeConfig:
    def __init__(self, root: Node):
        self.chart = {
            "container": "#compiler-parse-tree",
            "connectors": {
                "type": "straight",
                "style": {
                    "stroke": 'red',
                    "stroke-width": 3,
                    "arrow-end": ">",
                },
            },
            "levelSeparation": 60
        }
        self.nodeStructure = root


class Wrapper:
    def __init__(self, arg):
        self.JSONParsedTree = arg


def serialize(obj):
    try:
        return obj.__dict__
    except AttributeError:
        return None


def write(root: Node, filename: str):
    json_data = json.dumps(ParsedTreeConfig(root), default=serialize)
    with open('../treant-js-master/%s.json' % filename, 'w') as f:
        f.write("JSONParsedTree = ")
        f.write(json_data)
