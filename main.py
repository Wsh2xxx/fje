import json
import argparse
import os
import main as fc

def parse_args():
    parser = argparse.ArgumentParser(description="Visualize JSON files in a tree-like structure.")
    parser.add_argument('-f', '--file', required=True, help="Path to the JSON file.")
    parser.add_argument('-s', '--style', choices=['compact', 'extended'], default='compact', help="Display style of the tree.")
    parser.add_argument('-i', '--icon_family', default='default', help="Icon family to use in the display.")
    return parser.parse_args()


class FunnyJsonExplorer:
    def __init__(self, filename, factory):
        self.factory = factory
        self.filename = filename
        self.style = None
        self.data = self._load()
        self.root = self.build_tree(self.data)

    def _load(self):
        if not os.path.exists(self.filename):
            print(f"Error: The file {self.filename} does not exist.")
            exit(1)
        with open(self.filename, 'r') as file:
            return json.load(file)

    def build_tree(self, data, parent_name="Root"):
        if isinstance(data, dict):
            container = self.factory.create(parent_name)
            for key, value in data.items():
                print(f"11{key}: {value}")
                child = self.build_tree(value, key)
                container.add_child(child)
            return container
        elif isinstance(data, list):
            container = self.factory.create(parent_name)
            for item in data:
                print(f"22{item}")
                child = self.build_tree(item, "List Item")
                container.add_child(child)
            return container
        else:
            return fc.Leaf(str(data))
    def show(self):
        if self.root:
            self.root.draw()


def main():
    args = parse_args()
    if args.style == 'compact':
        factory = fc.LeafFactory()
    else:
        factory = fc.ContainerFactory()
    print(f"Visualizing '{args.file}' with style '{args.style}' and icons from '{args.icon_family}':")
    fje = FunnyJsonExplorer(args.file, factory)
    fje.show()

if __name__ == "__main__":
    main()
