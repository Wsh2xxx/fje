import leaf as node
import os
import json

class FunnyJsonExplorer:
    def __init__(self, filename, factory):
        self.filename = filename
        self.factory = factory
        self.data = self._load()
        self.root = self.build_tree(self.data)

    def _load(self):
        if not os.path.exists(self.filename):
            print(f"Error: The file {self.filename} does not exist.")
            exit(1)
        with open(self.filename, 'r') as file:
            return json.load(file)

    def build_tree(self, data, parent_name="Root", level=0):
        if isinstance(data, dict):
            # print(f"1, {data}, {parent_name} {level}")
            container = self.factory.create_container(parent_name, level)
            for key, value in data.items():
                child = self.build_tree(value, key, level + 1)
                container.add_child(child)
            return container
        elif isinstance(data, list):
            # print(f"2, {data}, {parent_name} {level}")
            container = self.factory.create_container(parent_name, level)
            for item in data:
                child = self.build_tree(item, "List Item", level + 1)
                container.add_child(child)
            return container
        else:
            # print(f"3, {data}, {parent_name}")
            return self.factory.create_leaf(parent_name, data)

    def show(self):
        if self.root:
            self.root.draw()

