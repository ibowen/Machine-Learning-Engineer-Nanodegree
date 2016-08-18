
"""
Question5: Find the element in a singly linked list that's m elements from the end. 


Design Choice: In a single list, we have to tranverse the whole list to get the mth element from the end. 
So a m-length array is needed to record m nodes of the list in each iteration. 
In the end, the first element of the array will be the mth element from the end of the list

Time Complexity: the complexity starts with n(the length of the list ll) for tranversing the while list.
At each iteration, we are moving the nodes in the array from end to beginning. It's m movements. Hence:
	Worst case: O(n^2), if it happens to return the nth element from the end
	Best case: O(n), if it only return the last node of the list
	Average case: O(n*m), given a average m

Space Complexity: a m-length array is needed as a window frame to move along the list
"""	

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
	"""
	Definition: 
	Parameters: 
	Returns: 
	"""
	# None check
	if ll is None:
		return
	# initiate a m-length array as the window frame
	window = [None] * m
	# traverse the list ll till the tail
	while ll.next:
		for idx, val in enumerate(window): # move the whole window from the end to the beginning
			if idx == m - 1:	# insert the new node from ll into the end position of window m
				window[idx] = ll.next.data
				break
			window[idx] = window[idx + 1]
		ll = ll.next
	return window[0] # the first element of m will be the mth element from the end of the list ll

def main():
	# test cases
	head = Node(3)
	head.next = Node(6)
	head.next.next = Node(7)
	head.next.next.next = Node(2)

	# it should be 6
	print question5(head, 3)


if __name__ == "__main__":
    main()




