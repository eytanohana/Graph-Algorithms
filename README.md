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

In graph theory, vertices can accessed by computing a graph traversal. A graph traversal is an algorithm that "visits" each vertex in the graph. All types of traversal gives a specific order in which each vertex is visited. Two simple types of traversals in a graph are paths and cycles. A path is sequence of non-repeating vertices connected by unique edges. 

<img src="static/path-graph.png" width="30%"/>

A cycle is a path where the start and end vertices are the same.

An important property of graphs to discuss before further discussing traversals is the concept of graph connectivity. Two vertices *u* and *v* are connected if there exists a path between them.


* Basic Traversals - Topological Sort
* Trees - explanation
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
