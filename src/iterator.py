class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def has_next(self):
        return self.index < len(self.container.children)

    def next(self):
        if self.has_next():
            result = self.container.children[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
