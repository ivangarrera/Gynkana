
class NodeElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_key(self, key):
        self.key = key

    def set_value(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, NodeElement):
            return self.key == other.key
        return NotImplemented

    def __str__(self):
        return self.value.__str__()

