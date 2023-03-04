# Path Planning

I have implemented A* algorithm to solve the maze.

Every grid on the map, is represented using an object of the class Node. The Node class has the following properties :

1. coords : Coordinates of the node on the map.
2. gscore : The cost of moving from the start to that node. In this case, cost is represcent by the distance between each node, which is equal to 1. Default value for each node is infinity.
3. fscore : It is the sum of gscore and hscore. Hscore is the estimated distance between the current node and the end node. In this case I have used manhattan distance.
4. parent : It represent from which node did we arrive on the current node. Keeping track of this, helps us retrace our path from the goal to the start.
5. value : It is the integer value 0-15 given to each node, representing the walls adjacent to the node.
6. neighbors : List of neighbors of the node.

Basically, there are two sets Open set and close set. The Open set contains all the nodes which need to be examined and the close set contains all the nodes which have been examined. We start with starting node in the open set. There is a main loop which finds the node in the open set with the least fscore, and pops it out. It then adds it to the closed set. Now, it checks weather the coordinates of the given node is equal to the coordinates of the end node. If it is, then it returns a function call to retracepath function, which retraces a path from the end node to the start node and returns a list of integers. If it is not equal to the end node, it caluclates all it's neighbors using the node_neighbors function. There is another loop inside the main loop which goes through all the neighbors and checks weather the (gcost(of the current node) + 1), which is the total distance from the start node along the path till the neighbor node, is less than gcost of the neighbor node. If it is, then the neighbor node is added into the open set for evaluation. The main loop runs until the open set is empty.
