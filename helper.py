import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(G):
    
    marked_nodes = [node for node, attrs in G.nodes.items() if attrs.get('marked', False) == True]
    unmarked_nodes = list(set(G.nodes) - set(marked_nodes))
            
    marked_edges = [e for e, attrs in G.edges.items() if attrs.get('marked', False) == True]    
    unmarked_edges = list(set(G.edges) - set(marked_edges))
    print(unmarked_edges)
    
    pos = nx.spring_layout(G) # positions for all nodes

    nx.draw_networkx_nodes(G, pos,
                       nodelist=marked_nodes,
                       node_color='#FF00FF',
                       node_size=500)
    
    nx.draw_networkx_nodes(G, pos,
                       nodelist=unmarked_nodes,
                       node_color='#7EFF67',
                       node_size=500)

    # edges
    nx.draw_networkx_edges(G, pos,
                           edgelist=marked_edges,
                           edge_color='#FF00FF',
                           width=2)
    
    nx.draw_networkx_edges(G, pos,
                           edgelist=unmarked_edges,
                           edge_color='k',
                           width=1)
    
    labels = {n: n for n in G.nodes}
    nx.draw_networkx_labels(G,pos,labels,font_size=16)

    plt.axis('off')
    plt.show()
    
def clear_marks(G):
    for node in G.nodes:
        G.nodes[node]['marked'] = False
    for edge in G.edges:
        G.edges[edge]['marked'] = False
    