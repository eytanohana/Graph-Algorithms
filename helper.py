import os
import networkx as nx
import matplotlib.pyplot as plt
import imageio
from IPython.display import Image


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
                            connectionstyle='arc3, rad = 0.1',
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
                               connectionstyle='arc3, rad = 0.1',
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
                               connectionstyle='arc3, rad = 0.1',
                               ax=ax)
    
    if with_labels:
        labels = {n: n for n in G.nodes}
        nx.draw_networkx_labels(G, pos, labels, font_size=14, ax=ax)
    
    if ax:
        ax.axis('off')
    plt.axis('off')
    
    
def animate_euler(G, circ, name='euler'):
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()

    nx.draw_networkx_nodes(G, pos,
                           nodelist=G.nodes,
                           node_color='#00bbff',
                           ax=ax)
    
    nx.draw_networkx_edges(G, pos,
                           edgelist=G.edges,
                           connectionstyle='arc3, rad = 0.1',
                           ax=ax)
    labels = {n: n for n in G.nodes}
    nx.draw_networkx_labels(G, pos, labels, font_size=14, ax=ax)
    ax.axis('off')
    plt.savefig('.tmp0.png')
    tmp_files = ['.tmp0.png']
    marked_edges = []
    for i, edge in enumerate(zip(circ, circ[1:]), 1):
        marked_edges.append(edge)
        if isinstance(G, nx.DiGraph):
            unmarked_edges = set(G.edges) - set(marked_edges)
        else: 
             unmarked_edges = set(G.edges) - set(marked_edges) - set(e[::-1] for e in marked_edges)
        ax.clear()
        nx.draw_networkx_nodes(G, pos,
                               nodelist=G.nodes,
                               node_color='#00bbff',
                               ax=ax)
        nx.draw_networkx_edges(G, pos,
                               edgelist=marked_edges,
                               edge_color ='#b300f0',
                               connectionstyle='arc3, rad = 0.1',
                               ax=ax)
        nx.draw_networkx_edges(G, pos,
                               edgelist=unmarked_edges,
                               connectionstyle='arc3, rad = 0.1',
                               ax=ax)
        nx.draw_networkx_labels(G, pos, labels, font_size=14, ax=ax)
        ax.axis('off')
        tmp_files.append(f'.tmp{i}.png')
        plt.savefig(tmp_files[-1])
    ax.remove()
    with imageio.get_writer(f'static/euler-gifs/{name}.gif', mode='I') as writer:
        for file in tmp_files:
            image = imageio.imread(file)
            for _ in range(5):
                writer.append_data(image)
            os.remove(file)
        
    return Image(url=f'static/euler-gifs/{name}.gif')
