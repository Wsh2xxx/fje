import json
import argparse
import os
import leaf
import factory as fc
import FunnyJsonExplorer as FJE

def parse_args():
    parser = argparse.ArgumentParser(description="Visualize JSON files in a tree-like structure.")
    parser.add_argument('-f', '--file', required=True, help="Path to the JSON file.")
    parser.add_argument('-s', '--style', choices=['tree', 'rectangle'], default='tree', help="Display style of the tree.")
    parser.add_argument('-i', '--icon_family', default='default', help="Icon family to use in the display.")
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Visualizing '{args.file}' with style '{args.style}' and icons from '{args.icon_family}':")
    if args.style == "tree":
        factory = fc.TreeFactory(args.icon_family)
    elif args.style == "rectangle":
        factory = fc.RectangleFactory(args.icon_family)
    fje = FJE.FunnyJsonExplorer(args.file, factory)
    fje.show()


if __name__ == "__main__":
    main()
