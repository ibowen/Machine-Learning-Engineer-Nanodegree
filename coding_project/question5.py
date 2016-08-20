
"""
Question5: Find the element in a singly linked list that's m elements from the end. 


Design Choice: Simply tranverse the list and record the m elements along the way.

Implementation: In a single list, we have to tranverse the whole list to get the mth element from the end. 
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
	Definition: function to return the mth element from the end of a list
	Parameters: ll, a linked list; m, an int number
	Returns: an int number
	"""
	# None check
	if ll is None or m <= 0:
		return
	# initiate a m-length array as the window frame
	window = [None] * m
	# traverse the list ll till the tail
	while ll:
		for idx, val in enumerate(window):
			if idx == m - 1:	# insert the new node from ll into the end position of window m
				window[idx] = ll.data
				break
			window[idx] = window[idx + 1]
		if ll.next:
			ll = ll.next
		else:
			break

	return window[0] # the first element of m will be the mth element from the end of the list ll

def main():
	# test cases
	head = Node(3)
	head.next = Node(6)
	head.next.next = Node(7)
	head.next.next.next = Node(2)

	# it should be None
	print question5(None, 2)
	# it should be None
	print question5(head, -1)
	# it should be 2
	print question5(head, 1)
	# it should be 7
	print question5(head, 2)
	# it should be 6
	print question5(head, 3)
	# it should be 3
	print question5(head, 4)


if __name__ == "__main__":
    main()




