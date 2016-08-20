
"""

Question 4: Find the least common ancestor between two nodes on a binary search tree.

Design Choice: I only thought of divid and conquer to find the ancestor recursively

Implementation: First, the tree is divided into left and right node recursively till the bottom of tree. 
Then, the target child nodes are searched from bottom to the top. Finally, the node with left and right child nodes found as the target nodes will be returned.

Time Complexity: O(n^2), we need to traverse all nodes, so it starts with n. For each divide, we need to loop the whole adjacent list, that'n. So the final complexity is O(n^2)
Space Complexity: no extra space needed, it's O(1)
"""	

def question4(T, r, n1, n2):
	"""
	Definition: function to return the node row number of the least common ancester
	Parameters: 
		T: 2D list
		r: int, a root node row number
		n1,n2: int, row numbers
	Returns: int, node row number
	"""
	if T is None:
		return -1
	if r == n1 or r == n2:
		return r

	length = len(T) # the number of tree nodes
	# out of range check
	if r >= length or n1 >= length or n2 >= length:
		return -1

	left_idx = find_idx(T[r], 0, r) # find the left node index
	right_idx = find_idx(T[r], r, len(T[r])) # find the right node index

	left_node = -1
	right_node = -1
	if left_idx >= 0: # go to the left child node
		left_node = question4(T, left_idx, n1, n2)
	if right_idx >= 0: # go to the right child node
		right_node = question4(T, right_idx, n1, n2)

	if left_node >= 0 and right_node >= 0:
		return r
	if left_node >= 0:
		return left_node
	if right_node >= 0:
		return right_node
	else:
		return -1

def find_idx(l, start, end): # function to find the index of value '1' between the range of index
	for i in xrange(start, end):
		if l[i] == 1:
			return i

	return -1
	

def main():
	# test cases
	test = [[0, 1, 0, 0, 0],
	       [0, 0, 0, 0, 0],
	       [0, 0, 0, 0, 0],
	       [1, 0, 0, 0, 1],
	       [0, 0, 0, 0, 0]]
	# should be 3
	print question4(test, 3, 1, 4)

	# should be -1
	print question4(None, 3, 1, 4)

	# should be -1
	print question4(test, 6, 1, 4)


if __name__ == "__main__":
    main()




