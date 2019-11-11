class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def dfs(self, unrary_fun):
        if unrary_fun(self.data):
            return self
        for child in self.children:
            res = child.dfs(unrary_fun)
            if res is not None:
                return res
        return None


def print_tree(node, tab=0):
    to_print = " " * tab + f"-{node.data}"
    print(to_print)
    if len(node.children) > 0:
        print(" " * tab + "\\")
        for c_node in node.children:
            print_tree(c_node, tab+1)


def include_path(tree, include_file, current_path=[]):
    #TODO
    pass
