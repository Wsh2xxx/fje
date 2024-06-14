import visitor
import iterator as iter


# 成分接口，包含draw()和add_child()方法
class Component:
    def draw(self, index, islast):
        raise NotImplementedError

    def add_child(self, child):
        raise NotImplementedError

    # 接受访问者
    def accept(self, visitor, index, is_last):
        raise NotImplementedError


class Leaf(Component):
    def __init__(self, name, icon, level, data=None):
        self.name = name
        self.data = data
        self.icon = icon
        self.level = level
        self.prefix = None
        self.suffix = ''

    def draw(self, indent, is_last=True):
        # print(indent, is_last, self.level)
        indent = "   " * self.level
        if self.level > 1:
            self.prefix = '│' + indent + ("└─ " if is_last else "├─ ") + self.icon
        else:
            self.prefix = indent + ("└─ " if is_last else "├─ ") + self.icon
        self.suffix = f": {self.data}" if self.data else ""

    def accept(self, visitor, index, is_last):
        visitor.visit_leaf(self, index, is_last)


class Container(Component):
    def __init__(self, name, level=0, icon=None):
        self.name = name
        self.icon = icon
        self.level = level
        self.children = []
        self.prefix = None
        self.suffix = ''

    def add_child(self, child):
        self.children.append(child)

    def draw(self, indent, is_last=True):
        #print(indent, is_last, self.level)
        indent = "│  " * self.level
        self.prefix = indent + ("└─ " if is_last else "├─ ") + self.icon

    def accept(self, visitor, index, is_last):
        iterator = iter.Iterator(self)
        if not self.name == "Root":
            visitor.visit_container(self, index, is_last)
        # print(iterator)
        while iterator.has_next():
            child = iterator.next()
            child.accept(visitor, iterator.index, not iterator.has_next())


class RecLeaf(Component):
    def __init__(self, name, icon, level, data=None):
        self.name = name
        self.data = data
        self.icon = icon
        self.level = level
        self.prefix = None
        self.suffix = None

    def draw(self, index, is_last=False):
        prefix = "│  " * self.level
        prefix += "┴─ " if is_last and self.level == 0 else "├─ "
        self.prefix = prefix + self.icon
        self.data = f": {self.data} " if self.data else ' '
        self.suffix = self.data + '─' * (50 - len(self.prefix) - len(self.name) - len(self.data)) + '│'

    def accept(self, visitor, index, is_last):
        visitor.visit_leaf(self, index, is_last)


class RecContainer(Component):
    def __init__(self, name, level=0, icon=None):
        self.name = name
        self.level = level
        self.icon = icon
        self.children = []
        self.prefix = None
        self.suffix = None

    def add_child(self, child):
        self.children.append(child)

    def draw(self, index, is_last=False):
        # print(self.level, index, end=' ')
        if index == 1 and self.level == 0:
            self.prefix = "┌─ "
        else:
            header_prefix = "│  " * self.level
            prefix = "├─ "
            self.prefix = header_prefix + prefix
        self.prefix = self.prefix + self.icon
        if index == 1 and self.level == 0:
            self.suffix = '─' * (50 - len(self.prefix) - len(self.name)) + "┐"
        else:
            self.suffix = '─' * (50 - len(self.prefix) - len(self.name)) + "┤"

    def accept(self, visitor, index, is_last):
        iterator = iter.Iterator(self)
        if not self.name == "Root":
            visitor.visit_container(self, index, is_last)
        # print(iterator)
        while iterator.has_next():
            child = iterator.next()
            #print(iterator.index)
            child.accept(visitor, iterator.index, not iterator.has_next())
        if index == 0:
            print("└" + '─' * 49 + "┘")


'''# Factory class definitions
class ContainerFactory:
    def create(self, name):
        return Container(name, icon, level=1)

class LeafFactory:
    def create(self, name):
        return Leaf(name)
    '''