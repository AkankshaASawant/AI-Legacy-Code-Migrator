import networkx as nx

def build_dependency_graph(documents):
    g = nx.DiGraph()
    for doc in documents:
        g.add_node(doc["file"])
    return g
