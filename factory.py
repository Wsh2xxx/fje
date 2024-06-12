
import leaf

# 抽象工厂接口，提供 createLeaf() 和 createContainer() 方法。
class AbstractFactory():
    def __init__(self, icon=None):
        self.icon = self.set_icon(icon)

    def create_container(self, name, level):
        raise NotImplementedError

    def create_leaf(self, name, data):
        raise NotImplementedError

    def set_icon(self, icon):
        default_icon = {'container': '', 'leaf': ''}
        if icon is None or icon == "default":
            return default_icon
        elif icon == "poker":
            return {'container': '♢', 'leaf': '♤'}
        else:
            icon = icon.strip("()").split(",")
            return {'container': icon[0], 'leaf': icon[1]}

# 成分接口，包含draw()和add_child()方法
class Component:
    def __init__(self, a, b, c):
        raise  NotImplementedError

    def draw(self, ):
        raise NotImplementedError

    def add_child(self, child):
        raise NotImplementedError

# 实现具体工厂方法，创建树的具体container 和leaf
class TreeFactory(AbstractFactory):
    def create_container(self, name, level):
        return leaf.Container(name, level, self.icon["container"])

    def create_leaf(self, name, data):
        return leaf.Leaf(name, self.icon["leaf"], data)

class RectangleFactory(AbstractFactory):
    def create_container(self, name, level):
        return leaf.RecContainer(name, level, self.icon["container"])

    def create_leaf(self, name, data):
        return leaf.RecLeaf(name, self.icon["leaf"], data)
