import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(G):
    
    marked_nodes = []
    unmarked_nodes = []
    for node, attrs in G.nodes.items():
        print(node, attrs)
        if attrs.get('marked', False) == True:
            marked_nodes.append(node)
        else:
            unmarked_nodes.append(node)
            
    print(marked_nodes)
            
    marked_edges = [e for e, attrs in G.edges.items() if attrs.get('marked', False) == True]    
    unmarked_edges = [e for e, attrs in G.edges.items() if not attrs.get('marked', False) == True]
    
    pos = nx.spring_layout(G) # positions for all nodes

    nx.draw_networkx_nodes(G, pos,
                       nodelist=marked_nodes,
                       node_color='g',
                       node_size=500)
    
    nx.draw_networkx_nodes(G, pos,
                       nodelist=unmarked_nodes,
                       node_color='b',
                       node_size=500)

    # edges
    nx.draw_networkx_edges(G, pos,
                           edgelist=marked_edges,
                           edge_color='g',
                           width=2)
    
    nx.draw_networkx_edges(G, pos,
                           edgelist=unmarked_edges,
                           edge_color='k',
                           width=1)
    
    labels = {n: n for n in G.nodes}
    nx.draw_networkx_labels(G,pos,labels,font_size=16)

    plt.axis('off')
    plt.show()