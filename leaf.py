import factory


class Leaf(factory.Component):
    def __init__(self, name, icon=None, data=None):
        self.name = name
        self.data = data
        self.icon = icon

    def draw(self, indent=0, is_last=True):
        if self.name == "None":
            pass
        else:
            prefix = "│  " * (indent - 1) + ("└─ " if is_last else "├─ ") + self.icon
            print(prefix + f"{self.name}",end='')
            if self.data is not None:
                print(": "+self.data)
            else:
                print("")

class Container(factory.Component):
    def __init__(self, name, level=0, icon=None):
        self.name = name
        self.icon = icon
        self.level = level
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def draw(self, indent=0, is_last=True):
        if self.name is None:
            pass
        else:
            prefix = "│  " * (indent - 1) + ("└─ " if indent > 0 else "")
            print(prefix + f"{self.icon}{self.name} "
                           #f"(Level {self.level})"
                  )
            for i, child in enumerate(self.children):
                child.draw(indent + 1, i == len(self.children) - 1)


class RecLeaf(factory.Component):
    def __init__(self, name, icon, data=None):
        self.name = name
        self.data = data
        self.icon = icon

    def draw(self, indent=0, is_last=True):
        prefix = "│  " * indent + ("└─" if is_last else "├─") + self.icon
        data_display = f": {self.data}" if self.data else ""
        line = prefix + self.name + data_display
        print(line + '─' * (50 - len(line)) + '│')


class RecContainer(factory.Component):
    def __init__(self, name, level=0, icon=None):
        self.name = name
        self.level = level
        self.icon = icon
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def draw(self, indent=0, is_last=True):
        header_prefix = "│  " * indent
        prefix = header_prefix + "┌─" + self.icon
        print(prefix + self.name + '─' * (50 - len(prefix) - len(self.name)) + "┐")

        # 打印每个子节点
        for i, child in enumerate(self.children):
            child.draw(indent + 1, i == len(self.children) - 1)
        if self.level == 0:
            print("└─" + '─' * 47 + "─┘")



'''# Factory class definitions
class ContainerFactory:
    def create(self, name):
        return Container(name, icon, level=1)

class LeafFactory:
    def create(self, name):
        return Leaf(name)
    '''