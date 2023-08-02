import inspect
import myfile
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint


def evaluate(string):
    try:
        evaluation = eval(string)
    except AttributeError as ae:
        return None
    except SyntaxError as se:
        return None
    except ModuleNotFoundError as mfne:
        return None

    if not hasattr(evaluation, '__name__'):
        return None

    return evaluation


class Node:
    def __init__(self, name, id, item):
        self.name = name
        self.id = id
        self.item = item

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return self.name

    def color(self):
        if inspect.ismethod(self.item):
            return 'red'
        elif inspect.isfunction(self.item) or inspect.isroutine(self.item):
            return 'yellow'
        elif inspect.ismodule(self.item):
            return 'orange'
        elif inspect.isclass(self.item):
            return 'green'
        else:
            return 'blue'

    def weight(self):
        if inspect.ismethod(self.item):
            return 1.0
        elif inspect.isfunction(self.item) or inspect.isroutine(self.item):
            return 1.0
        elif inspect.ismodule(self.item):
            return 1.0
        elif inspect.isclass(self.item):
            return 1.0
        else:
            return 1.0


def gather(root, cache=set()):
    item = evaluate(root)
    dirs = dir(item)
    dirs = [d for d in dirs if not d.startswith('__')]

    name = root.split('.')[-1]
    tree = [Node(name, root, item)]

    for d in dirs:
        evalstr = f'{root}.{d}'

        result = gather(
            evalstr,
            cache
        )

        if result != None:
            tree.append(result)

    return tree


def add(data, graph: nx.DiGraph):
    node = data[0]
    graph.add_node(node, color=node.color())

    if len(data) >= 2:
        rest = data[1:]

        for item in rest:
            add(item, graph)
            graph.add_edge(node, item[0])


if __name__ == '__main__':
    data = gather('myfile')
    graph = nx.Graph()
    add(data, graph)

    color_map = [node.color() for node in graph]
    weight_map = [node.weight() for node in graph]

    nx.draw(graph, with_labels=True, node_color=color_map)
    plt.show()

    # graph = nx.DiGraph(edges)
    # nx.draw(graph, with_labels=True)
    # plt.show()
