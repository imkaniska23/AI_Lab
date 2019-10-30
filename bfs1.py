from collections import defaultdict

class BFS:
		
	def __init__( self ):
		
		self.graph = defaultdict( list )
	
	def addEdge( self,u, v ):
		
		self.graph[u].append(v)
		self.graph[v].append(u)
	
	def bfs(self, s, visited): 

		queue = [] 

		queue.append(s) 
		visited[s] = True

		while queue: 

			s = queue.pop(0) 
			print ("{} {}".format(s," ")) 

			for i in self.graph[s]: 
				if visited[i] == False: 
					queue.append(i) 
					visited[i] = True
		
def main():
	
	bfs_obj = BFS()
	visited = dict()
	while(1):
		choice = raw_input("\nCreate Edge - 1\nBFS - 2\nExit-3\n")
		if choice == '1':
			n = int( raw_input("Enter number of edges\n") )
			while n!=0:
				u = raw_input("First vertex:\t")
				v = raw_input("Second vertex:\t")
				visited[u] = False
				visited[v] = False			
				bfs_obj.addEdge( u, v )
				n=n-1
		elif choice == '2':
			u = raw_input("Enter source node:\t")
			print("\n")
			bfs_obj.bfs(u, visited)
		elif choice == '3':
			break
		else:
			print("Enter valid input")
			
if __name__ == '__main__':
	main()	
