import networkx as nx
import matplotlib.pyplot as plt


def clear_marks(G):
    for node in G.nodes:
        G.nodes[node]['marked'] = False
    for edge in G.edges:
        G.edges[edge]['marked'] = False

def draw_graph(G, with_labels=True, with_tree=True, ax=None):
    
    marked_nodes = [node for node, attrs in G.nodes.items() if attrs.get('marked', False) == True]
    unmarked_nodes = list(set(G.nodes) - set(marked_nodes))
            
    marked_edges = [e for e, attrs in G.edges.items() if attrs.get('marked', False) == True]    
    unmarked_edges = list(set(G.edges) - set(marked_edges))
    
    pos = nx.spring_layout(G) # positions for all nodes
    if with_tree:
        nx.draw_networkx_nodes(G, pos,
                           nodelist=marked_nodes,
                           node_color='#FF00FF',
                           node_size=400,
                           ax=ax)

        nx.draw_networkx_edges(G, pos,
                            edgelist=marked_edges,
                            edge_color='#FF00FF',
                            width=2,
                            ax=ax)
    
        nx.draw_networkx_nodes(G, pos,
                           nodelist=unmarked_nodes,
                           node_color='#7EFF67',
                           node_size=400,
                           ax=ax)

        nx.draw_networkx_edges(G, pos,
                               edgelist=unmarked_edges,
                               edge_color='k',
                               width=1,
                               ax=ax)
    else:
        nx.draw_networkx_nodes(G, pos,
                           nodelist=unmarked_nodes + marked_nodes,
                           node_color='#7EFF67',
                           node_size=400,
                           ax=ax)
        
        nx.draw_networkx_edges(G, pos,
                               edgelist=unmarked_edges + marked_edges,
                               edge_color='k',
                               width=1,
                               ax=ax)
    
    if with_labels:
        labels = {n: n for n in G.nodes}
        nx.draw_networkx_labels(G, pos, labels, font_size=14, ax=ax)
    
    if ax:
        ax.axis('off')
    plt.axis('off')
    