from collections import defaultdict

class Graph:

    def __init__( self ):

        self.graph = defaultdict( list )

    def addEdge( self, u, v ):

        self.graph[u].append(v)

    def DFSUtil( self, v, visited ):

        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil( i, visited )

    def DFS( self, v ):

        visited = [False]*(len( self.graph ))
        self.DFSUtil( v, visited)

def main():

    vert    = int(input( "Enter no. of vertices: "))
    edges   = int(input( "Enter no. of edges: "))
    g       = Graph()
    while(edges):
        u = int(input())
        v = int(input())
        g.addEdge( u, v)
        edges = edges-1

    vstart = int(input( "Enter vertex to start DFS:" ))
    g.DFS( vstart )

if __name__=="__main__":
    main()
