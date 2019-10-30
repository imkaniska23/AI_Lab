from collections import defaultdict

class Graph:

    def __init__( self ):

        self.graph = defaultdict( list )

    def addEdge( self, u, v):

        self.graph[u].append(v)

    def BFS( self, v ):

        visited     = [False]*(len( self.graph ))
        queue       = []
        visited[v]  = True
        queue.append(v)

        while queue:

            v = queue.pop(0)
            print(v, end=" ")

            for i in self.graph[v]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

def main():

    vert    = int(input( "Enter no. of vertices: "))
    edges   = int(input( "Enter no. of edges: "))
    g       = Graph()
    while(edges):
        u = int(input())
        v = int(input())
        g.addEdge( u, v)
        edges = edges-1

    vstart = int(input( "Enter vertex to start BFS:" ))
    g.BFS( vstart )

if __name__=="__main__":
    main()
