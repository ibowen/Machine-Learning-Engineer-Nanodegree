
"""
Question: Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. 
Your function should take in and return an adjacency list

Design Choice: Greedy Algorithm was used to solve Minimum Spanning tree. 
Since the graph is undirectly connected, there is at least one path to chhoose. 
So Greey algorithm choosing local minimum at each iteration can obtain global minimum in the end.

Implementation: a priority queue was used to store each adjacent list. Then edges weights were summed up for each vertice step by step. 
The vertice with the least weight will be in the head of the queue and be stored into output dictionary. 
Meanwhile, the edge of the head vertice is pushed into the queue. 
The iteration stops when the output dict equals the input adjacent list in length.

Complexity: 
	worst case: O(nlog(n)), to connect n vertices need n - 1 sorting. And the priority queue insert costs log(n-1), so totally O(nlogn)
	best case: O(n), only if vertices are along one line.
	average: O(nlog(n))

"""	

from Queue import PriorityQueue

def question3(G):
	"""
	Definition: function to calulates the minimum spanning tree(mst) from adjacent lists
	Parameters: G: a dictionary containing adjacency lists
	Returns: mst, a dictionary containing adjacency lists with the least weight
	"""
	if G is None:
		return

	mst = {} # initiate a minimum spanning tree
	queue = PriorityQueue() # initiate a priority queue to store each vertice and its edge
	
	vertice, edge_list = G.popitem() # pop one item to start
	for e in edge_list: # break the first adjacent list into the format "(priority, vetice, edge)"
		queue.put((0 + e[1], vertice, e))
	
	while len(mst) <= len(G) and not queue.empty():
		head = queue.get() # dequeue the head, the same as "(priority, vetice, edge)"
		if head[1] in mst:
			continue
		mst[head[1]] = [head[2]] # put head into mst, note: the head is always the adjacent list with the least weight

		# put the edge of the head into the queue
		next_vertice = head[2][0]
		if next_vertice in mst: # if the vertice in the edge already in mst, continue
			continue
		for edge in G[next_vertice]:
				if edge[0] in mst: # if vertice in the edge already in mst, continue
					continue

				# construct the new adjacent list and put into the queue
				priority = head[0] + edge[1]
				queue.put((priority, next_vertice, edge))

	return mst

def main():
	# test case
	# should print {'A': [('B', 2)]}
	G = {'A': [('B', 2)],
		 'B': [('A', 2)]}
	print question3(G)

	# should print {'A': [('B', 2)], 'B': [('C', 5)]}
	G = {'A': [('B', 2)],
		 'B': [('A', 2), ('C', 5)], 
		 'C': [('B', 5)]}
	print question3(G)
	
	# should print {'A': [('E', 1)], 'C': [('B', 5)], 'B': [('D', 4)], 'E': [('C', 3)]}
	G = {'A': [('B', 2), ('E', 1)],
		 'B': [('A', 2), ('C', 5), ('D', 4)], 
		 'C': [('B', 5), ('D', 6), ('E', 3)],
		 'D': [('B', 4), ('C', 6)],
		 'E': [('A', 1), ('C', 3)]}
	print question3(G)	 

	G = None
	# should print None
	print question3(G)

if __name__ == "__main__":
    main()




