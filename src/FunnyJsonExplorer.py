import os
import json

from visitor import PrintVisitor


class FunnyJsonExplorer:
    def __init__(self, filename, factory):
        self.filename = filename
        self.factory = factory
        # self.visitor = visitor
        self.data = self._load()
        self.root = self.build_tree(self.data)

    def _load(self):
        if not os.path.exists(self.filename):
            print(f"Error: The file {self.filename} does not exist.")
            exit(1)
        with open(self.filename, 'r') as file:
            return json.load(file)

    def build_tree(self, data, parent_name="Root", level=-1):
        if isinstance(data, dict):
            # print(f"1, {data}, {parent_name} {level}")
            container = self.factory.create_container(parent_name, level)
            for key, value in data.items():
                child = self.build_tree(value, key, level + 1)
                container.add_child(child)
            return container
        else:
            # print(f"3, {data}, {parent_name}")
            return self.factory.create_leaf(parent_name, data, level)

    def show(self):
        if self.root:
            # self.root.draw()
            draw_visitor = PrintVisitor()
            self.root.accept(draw_visitor, 0, False)
