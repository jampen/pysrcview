import networkx as nx
import matplotlib.pyplot as plt
import myclass as myclass
from pprint import pprint

def gather(root, thing, cache = set()):
  dirs = dir(thing)
  dirs = [d for d in dirs if not d.startswith('__')]
  tree = [root]

  for d in dirs:
    try:
      evaluation = eval(f'{root}.{d}')
    except AttributeError as ae:
      continue
    except SyntaxError as se:
      continue
    
    if not hasattr(evaluation, '__name__'):
      continue

    name = evaluation.__name__

    if name.startswith('_'):
      continue

    uniquename = root


    print(uniquename)

    if uniquename in cache:
      continue

    cache.add(uniquename)
    result = gather(
      f'{root}.{name}',
      evaluation)
      
    tree.append(result)

  return tree

def add(data, graph: nx.Graph):
  name = data[0]
  graph.add_node(name)

  if len(data) >= 2:
    rest = data[1:]
    rest = [item for item in rest if item not in graph]

    for item in rest:
      add(item, graph)
      graph.add_edge(name, item[0])

data = gather('myclass', myclass)
graph = nx.Graph()
add(data, graph)

nx.draw(graph, with_labels=True)
plt.show()

#graph = nx.DiGraph(edges)
#nx.draw(graph, with_labels=True)
#plt.show()