class Visitor:
    def visit_leaf(self, leaf, index, ck):
        pass

    def visit_container(self, container, index, ck):
        pass


class PrintVisitor(Visitor):
    def visit_leaf(self, leaf, index, is_last):
        # print(f"Leaf: {leaf.name}, Data: {leaf.data}")
        leaf.draw(index, is_last)
        print(leaf.prefix + leaf.name + leaf.suffix)

    def visit_container(self, container, index, is_last):
        # container.draw(container.level)
        container.draw(index, is_last)
        print(container.prefix + container.name + container.suffix)

