from collections import defaultdict

class DFS:
		
	def __init__( self ):
		
		self.graph = defaultdict( list )
	
	def addEdge( self,u, v ):
		

		self.graph[u].append(v)
		self.graph[v].append(u)
	
	def _dfs_Call( self, u, visited,path,v):
		
		visited[u] = True;
		path.append(u)
		if u == v:
			print(path)
		
		else:
			for i in self.graph[u]:
				if visited[i] == False:
					self._dfs_Call( i, visited,path,v )
	
		path.remove(u)
		visited[u] = False
			
	def dfs( self, u, visited,path,v):
	
		for key,val in visited.items():
			visited[key] = False
			
		path = list()	
		self._dfs_Call( u, visited,path,v)
		
def main():
	
	dfs_obj = DFS()
	visited = dict()
	path = list()
	while(1):
		choice = raw_input("\nCreate Edge - 1\nDFS - 2\nExit-3\n")
		if choice == '1':
			n = int( raw_input("Enter number of edges\n") )
			while n!=0:
				u = (raw_input("First vertex:\t"))
				v = (raw_input("Second vertex:\t"))
				visited[u] = False
				visited[v] = False			
				dfs_obj.addEdge( u, v )
				n=n-1
		elif choice == '2':
			u = (raw_input("Enter source node:\t"))
			v = (raw_input("Enter destination node:\t"))
						
			print("\n")
			dfs_obj.dfs(u, visited,path,v)
		elif choice == '3':
			break
		else:
			print("Enter valid input")
			
if __name__ == '__main__':
	main()	
		
	
