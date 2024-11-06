#Implement Depth first search algorithm and Breadth First Search algorithm, Use 
an undirected graph and develop a recursive algorithm for searching all the vertices 
of a graph or tree data structure.  
  
  

def dfs(visited,G,node): 
    if(node not in visited): 
        visited.append(node) 
        for neighbour in G[node]: 
                dfs(visited,G,neighbour) 
                 
def bfs(queue,G,node): 
    if(node not in visited2): 
        print(node) 
        visited2.append(node) 
    for neighbour in G[node]: 
        if(neighbour not in visited2): 
            print(neighbour) 
            queue.append(neighbour) 
            visited2.append(neighbour) 
    if(len(queue)==0): 
        return 
    else: 
        x=queue.pop(0) 
        bfs(queue,G,x) 
         
             
#MAIN PROGRAM 
visited=[] 
queue=[] 
G=dict() 
visited2=[] 
G={ 
     '0':['1','2','3'], 
     '1':['0','4'], 
     '2':['0','5'], 
     '3':['0','5'], 
     '4':['1'], 
     '5':['2','3'] 
 } 
print("MENU:") 
print("1.DFS") 
print("2.BFS") 
choice=int(input("Please enter your choice of action: ")) 
if(choice==1): 
    n=input("Please enter starting node: ") 
    dfs(visited,G,n) 
    print(visited) 
elif(choice==2): 
    n=input("Please enter starting node: ") 
    bfs(queue,G,n)
