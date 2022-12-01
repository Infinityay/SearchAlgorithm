class Node:
    def __init__(self):
        self.name = ''
        self.point = (0, 0)
        self.next = []
        self.prev = None
        self.fn = 0
        self.gn = 0

    # def setNode(self, name, point, next, prev=None, fn=0, gn=0):
    #     self.name = name
    #     self.point = point
    #     self.next = next
    #     self.prev = prev
    #     self.fn = fn
    #     self.gn = gn


class Graph:
    def __init__(self):
        # 所有结点构成图
        self.nodes = []
