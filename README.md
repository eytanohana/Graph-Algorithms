# Graph-Algorithms

This is a collaboration between [Eytan Ohana](https://github.com/eytan-ohana/Graph-Algorithms) and [Osher Boudara](https://github.com/osherboudara99/Graph-Algorithms) to implement and visualize various graph algorithms.

---

## Table of Contents
- [BFS](BFS.ipynb)
- [DFS](DFS.ipynb)

A graph is a type of data structure that is represented by a set of nodes/vertices and edges.  
<img src="static/graph.png" width="60%"/>

Graphs can be used to model many complex things like social networks where individuals are the nodes and connections between friends are the edges. 

Graphs and Graph algorithms are also widely used in navigation systems like google maps. The nodes can be intersections or popular destinations and the edges can be roads or highways connecting them. 

Additionally edges can be weighted which in the case of nav systems can be represent some sort of measure for how long the road (edge) from point a to point b is, which can take in to account physical distance, traffic conditions, and other factors.

In graph theory, vertices can accessed by computing a graph traversal. A graph traversal is an algorithm that "visits" each vertex in the graph. All types of traversal gives a specific order in which each vertex is visited. Two simple types of traversals in a graph are paths and cycles. A path is sequence of non-repeating vertices connected by unique edges. A cycle is a path where the start and end vertices are the same.

<p float="left">
 <img src="static/path-graph.png" width="30%"/>
 <img src="static/cycle-graph.png" width="30%"/>
</p>


An important property of graphs to discuss before further discussing traversals is the concept of graph connectivity. Two vertices *u* and *v* are connected if there exists a path between them.

A graph is called a connected graph if vertex has a path to every other vertex.

A graph is called completely connected if every vertex is connected to every other vertex by a single edge.

<img src="static/complete-graph.png" width="30%"/>

Another important topic in graph theory are trees. A tree is an undirected connecte graph that doesn't contain any cycles. Trees have a few characteristic properties. A graph is a tree if it has the following properties:

1. It is connected and has no cycles.
1. If any edge is added to the graph, a cycle will be formed.
1. For every two vertices there is a unique path (composed of unique edges) between them.
1. If any edge is removed from the graph, then the graph won't be connected anymore.

<img src="static/simple-tree.png" width="30%"/>

In graph theory an important topic is finding spanning trees of graphs. A spanning tree for a graph is just the set of edges in the graph that form a tree and contains every node in the graph.

<img src="static/tree-graph.png" width="30%"/>

The graph above consists of all the nodes and edges both pink and black. The spanning tree consists only of the nodes and pink edges.


* Basic Traversals - Topological Sort
* Spanning Trees i.e. BFS and DFS Traversals
 - single shortest path
* Dijkstras Algo
* Graph Connectivity
* Connected Components
* Common Graph
* Euler Trails and Circuit - Fleury's Algo
* Hamiltonian Cycles 
 -  maybe Planarity
* Graph Coloring

Graphs are applicable in so many situations that thousands of algorithms have been developed for them. Algorithms like shortest path, spanning trees, graph traversals, topological sorts and more. 
