from collections import defaultdict

class Graph:

    def __init__( self ):

        self.graph = defaultdict( list )

    def addEdge( self, u, v, weight ):

        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    @staticmethod
    def _sortTuple( tup ):
        tup.sort(key = lambda x:x[1])

    def bfs( self, source, dest, visited):

        for key, value in self.graph.items():
            self.graph[key] = Graph._sortTuple( self.graph[key] )

        queue = []
        queue.append(source)
        visited[source]=True

        while queue:

            s = queue.pop(0)
            s = s[0]

            print ("{} {}".format(s," "))
            if s==dest:
                break
            else:
                for i in self.graph[s]:
                    if visited[i[0]]==False:
                        queue.append(i)
                        queue.sort(key=lambda x:x[1])
                        visited[i[0]]=True

def main():

	bfs_obj = Graph()
	visited = dict()
	while(1):
		choice = raw_input("\nCreate Edge - 1\nBFS - 2\nExit-3\n")
		if choice == '1':
			n = int( raw_input("Enter number of edges\n") )
			while n!=0:
				u 	= (raw_input("First vertex:\t"))
				v 	= (raw_input("Second vertex:\t"))
				wt 	= int( raw_input("Enter edge weight:\t") )
				bfs_obj.addEdge( u, v, wt )
				visited[u] = False
				visited[v] = False
				n = n-1
		elif choice == '2':
			u = (raw_input("Enter source node:\t"))
			v = (raw_input("Enter destination node:\t"))
			print("\n")
			bfs_obj.bfs(u, v, visited)
		elif choice == '3':
			break
		else:
			print("Enter valid input")

if __name__ == '__main__':
	main()
