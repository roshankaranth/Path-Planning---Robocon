import sys
import heapq
from MapNode import MapNode


class PlannerNode:
    
    def __init__(self):
        self.current_obj=MapNode()
        # Since we know that the first step the bot will take will be down, we can simply do it here
        self.current_obj.direction_callback("down")  # example 1

        print(self.wall_callback())

    @staticmethod
    def RetracePath(start_node,end_node):
         #Method to Retrace the path back to the start from the end
         current_node = end_node
         path=[]
         while(current_node.coords!=start_node.coords):
               coords_change = [current_node.coords[0]-current_node.parent.coords[0],current_node.coords[1]-current_node.parent.coords[1]]
               
               if(coords_change[0]==1):
                   path.append(1)
               if(coords_change[0]==-1):
                   path.append(0)
               if(coords_change[1]==1):
                   path.append(3)
               if(coords_change[1]==-1):
                   path.append(2)

               current_node=current_node.parent

         return list(reversed(path))
    
    def node_neighbors(self,node):
        #Method to create neighbor nodes
        if(node.value<=7): 
             #Top wall absent
             node.neighbors.append(Node((node.coords[0]-1,node.coords[1]),self.current_obj._MapNode__map.array[node.coords[0]-1][node.coords[1]]))
             
        if(node.value%2==0):
             #Bottom wall absent
             node.neighbors.append(Node((node.coords[0]+1,node.coords[1]),self.current_obj._MapNode__map.array[node.coords[0]+1][node.coords[1]]))
             
        if(node.value!=12 and node.value!=6 and node.value!=5 and node.value!=4 and node.value!=14 and node.value!=7 and node.value!=13 ):
             #Left wall absent
             node.neighbors.append(Node((node.coords[0],node.coords[1]-1),self.current_obj._MapNode__map.array[node.coords[0]][node.coords[1]-1]))
             
        if(node.value!=2 and node.value!=3 and node.value!=10 and node.value!=6 and node.value!=14 and node.value!=7 and node.value!=11 ):
             #Right wall absent
             node.neighbors.append(Node((node.coords[0],node.coords[1]+1),self.current_obj._MapNode__map.array[node.coords[0]][node.coords[1]+1]))


    def heuristic_cost(self,node_coords):
         #Determines the Manhattan distance between the current node and the end node
         return abs(node_coords[0]-self.current_obj._MapNode__map.end[0])+abs(node_coords[1]-self.current_obj._MapNode__map.end[1])
       
         #Euclidean distance
         #return pow(pow(node_coords[0]-self.current_obj._MapNode__map.end[0],2) + pow(node_coords[1]-self.current_obj._MapNode__map.end[1],2),0.5)


    def wall_callback(self):
            
            Open_Set = []
            Close_set = []
            start = Node(self.current_obj.current,self.current_obj._MapNode__map.array[self.current_obj.current[0]][self.current_obj.current[1]],0,self.heuristic_cost(self.current_obj.current))
            end = Node(self.current_obj._MapNode__map.end,self.current_obj._MapNode__map.array[self.current_obj._MapNode__map.end[0]][self.current_obj._MapNode__map.end[1]],float('inf'),0)
            count = 0
            
            heapq.heapify(Open_Set)
            heapq.heappush(Open_Set,(start.fscore,count,start))
           
            while(len(Open_Set)!=0):
                 
                 current_Node = heapq.heappop(Open_Set)[2]
                 Close_set.append(current_Node.coords)
                 
                 if(current_Node.coords==end.coords):
                      return self.RetracePath(start,current_Node)
                 self.node_neighbors(current_Node)
                 
                 for neighbor in current_Node.neighbors:
                      if(neighbor.coords in Close_set):
                           continue
                      
                      temp_gscore = current_Node.gscore + 1

                      if(temp_gscore<neighbor.gscore):
                           t=0
                           neighbor.parent = current_Node
                           neighbor.gscore = temp_gscore
                           neighbor.fscore = temp_gscore+ self.heuristic_cost(neighbor.coords)
                           #To check weather neighbor node is already present in Open_Set
                           for i in range(len(Open_Set)):
                              if(neighbor.coords == Open_Set[i][2].coords):
                                   t=1
                           if(t==0):
                                count+=1
                                heapq.heappush(Open_Set,(neighbor.fscore,count,neighbor))

            return "No path Found"


class Node:
    
    def __init__(self,coords,value,gscore=float('inf'),fscore=float('inf'),parent=None):
        self.coords = coords
        self.gscore = gscore
        self.fscore = fscore
        self.parent = parent
        self.value = value
        self.neighbors = []
        
        
        
if __name__ == '__main__':
    start_obj=PlannerNode()
    start_obj.current_obj.print_root.mainloop()
 