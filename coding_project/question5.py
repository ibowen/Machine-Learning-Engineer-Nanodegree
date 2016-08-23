
"""
Question5: Find the element in a singly linked list that's m elements from the end. 


Design Choice: On way is to tranverse the list and record the m elements along the way.
Another better way is to use cursor node to record the mth node along the tranverse. 

Implementation: In the second choice, we use a position variable to record the number of steps when tranversing the list.
Plus, a cursor node is needed to update the node from the head when the postion adds up from mth step. 
Finally, we return the cursor node as the tranversing ends at the tail.

Time Complexity: the complexity is always n(the length of the list ll) for tranversing the whole list.
Space Complexity: O(1), a node cursor and a position variable are needed
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
	# initiate a cursor
	cursor = ll
	position = 1
	# traverse the list ll till the tail
	while ll:
		if ll.next:
			ll = ll.next
			position += 1
		else:
			break

		if position > m: # cursor moves when postion > m
				cursor = cursor.next

	return cursor.data if position >= m else None # only return cursor when ll is longer than m, otherwise return None

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




