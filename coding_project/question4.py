
"""

Question 4: Find the least common ancestor between two nodes on a binary search tree.
Design Choice: The question was solved by divid and conquer. First, the tree is divided into left and right node recursively till the bottom of tree. 
Then, the target child nodes are searched from bottom to the top. Finally, the node with left and right child nodes found as the target nodes will be returned.

Time Complexity: O(n^2), we need to traverse all nodes, so it starts with n. For each divide, we need to loop the whole adjacent list, that'n. So the final complexity is O(n^2)
Space Complexity: no extra space needed, it's O(1)
"""	

def question4(T, r, n1, n2):
	"""
	Definition: 
	Parameters: 
	Returns: 
	"""
	if T is None:
		return -1
	if r == n1 or r == n2:
		return r

	left_idx = find_idx(T[r], 0, r) # find the left node index
	right_idx = find_idx(T[r], r, len(T[r])) # find the right node index

	left_node = -1
	right_node = -1
	if left_idx >= 0:
		left_node = question4(T, left_idx, n1, n2)
	if right_idx >= 0:
		right_node = question4(T, right_idx, n1, n2)

	if left_node >= 0 and right_node >= 0:
		return r
	if left_node >= 0:
		return left_node
	if right_node >= 0:
		return right_node
	else:
		return -1

def find_idx(matrix, start, end):
	for i in xrange(start, end):
		if matrix[i] == 1:
			return i

	return -1
	

def main():
	# test cases
	test = [[0, 1, 0, 0, 0],
	       [0, 0, 0, 0, 0],
	       [0, 0, 0, 0, 0],
	       [1, 0, 0, 0, 1],
	       [0, 0, 0, 0, 0]]

	print question4(test, 3, 1, 4)


if __name__ == "__main__":
    main()




