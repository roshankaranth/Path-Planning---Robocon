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
         current_node = end_node
         path=[]
         while(current_node!=start_node):
               coords_change = [current_node.coords[0]-current_node.parent.coords[0],current_node.coords[1]-current_node.parent.coords[1]]
               if(coords_change[0]==1):
                   path.append(3)
               if(coords_change[0]==-1):
                   path.append(2)
               if(coords_change[1]==1):
                   path.append(0)
               if(coords_change[1]==-1):
                   path.append(1)

               current_node=current_node.parent

         return reversed(path)
    
    
    def Hcost_calc(self,node):
         
         return ()
    
    
    def node_neighbors(self,node):
        
        if(node.value<=7): 
             #Top wall absent
             node.neighbors.append(Node([node.coords[0]-1,node.coords[1]],self.current_obj._MapNode__map.array[node.coords[0]-1][node.coords[1]]))
             
             
        if(node.value%2==0):
             #Bottom wall absent
             node.neighbors.append(Node([node.coords[0]+1,node.coords[1]],self.current_obj._MapNode__map.array[node.coords[0]+1][node.coords[1]]))
             
             
        
        if(node.value!=12 and node.value!=6 and node.value!=5 and node.value!=4 and node.value!=14 and node.value!=7 and node.value!=13 and node.value!=0):
             #Left wall absent
             node.neighbors.append(Node([node.coords[0],node.coords[1]-1],self.current_obj._MapNode__map.array[node.coords[0]][node.coords[1]-1]))
             
             

        if(node.value!=2 and node.value!=3 and node.value!=10 and node.value!=6 and node.value!=14 and node.value!=7 and node.value!=11 and node.value!=0):
             #Right wall absent
             
             node.neighbors.append(Node([node.coords[0],node.coords[1]+1],self.current_obj._MapNode__map.array[node.coords[0]][node.coords[1]+1]))

    def wall_callback(self):
            
            Open_Set = []
            start = Node(self.current_obj.current,self.current_obj._MapNode__map.array[self.current_obj.current[0]][self.current_obj.current[1]],0,abs(self.current_obj.current[0]-self.current_obj._MapNode__map.end[0])+abs(self.current_obj.current[1]-self.current_obj._MapNode__map.end[1]))
            end = Node(self.current_obj._MapNode__map.end,self.current_obj._MapNode__map.array[self.current_obj._MapNode__map.end[0]][self.current_obj._MapNode__map.end[1]],float('inf'),0)
            count = 0
            
           
            
            
            heapq.heapify(Open_Set)
            heapq.heappush(Open_Set,(start.fscore,count,start))
            
            
     
            while(len(Open_Set)!=0):
                 
                 
                 current_Node = heapq.heappop(Open_Set)[2]
                 current_Node.evaluated = True
                 print(current_Node.coords)
                 
                 
                 if(current_Node.coords==end.coords):
                      return self.RetracePath(start,end)
                 

                 self.node_neighbors(current_Node)
                 
                 
                      

                 for neighbor in current_Node.neighbors:
                     
                      temp_gscore = current_Node.gscore + 1
                      if(temp_gscore<neighbor.gscore):
                           neighbor.parent = current_Node
                           neighbor.gscore = temp_gscore
                           neighbor.fscore = temp_gscore+ abs(neighbor.coords[0]-self.current_obj._MapNode__map.end[0])+abs(neighbor.coords[1]-self.current_obj._MapNode__map.end[1])
                           if(neighbor not in Open_Set):
                                count+=1
                                heapq.heappush(Open_Set,(neighbor.fscore,count,neighbor))
                                

                   
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
 