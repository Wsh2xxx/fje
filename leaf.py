class Leaf:
    def __init__(self, name):
        self.name = name

    def draw(self, indent=0):
        print(' ' * indent + f"- {self.name}")

class Container:
    def __init__(self, name, icon="default_icon", level=0):
        self.name = name
        self.icon = icon
        self.level = level
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def draw(self, indent=0):
        print(' ' * indent + f"{self.icon} {self.name} (Level {self.level})")
        for child in self.children:
            child.draw(indent + 4)

# Factory class definitions
class ContainerFactory:
    def create(self, name):
        return Container(name, icon="folder_icon.png", level=1)

class LeafFactory:
    def create(self, name):
        return Leaf(name)