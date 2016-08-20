
"""
Question 2: Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.

Design Choice: The natural method is brutal force, finding the longest palindromic. That would give a complexity of O(n^3).
Another way is to use dynamic programming. 

Implementation: Whether a longer substring is parlindromic depends on the previous shorter substring.
For dynamic programming, we need a 2d matrix to record if each substring is parlindromic.

Time Complexity: O(n^2), it loops the length of substring from 1 to n. In each loop, we move a window-like frame to check each substring,
That's n, n-1, ... 1. So it's O(n^2) in total

Space Complexity: O(n^2) 2D matrix is needed with half of them(one side of diaganal) unused.
"""	

def question2(s):
	"""
	Definition: return the longest parlindromic string
	Parameters: s: a target string
	Returns: a string
	"""
	if s is None or s == '':
		return ''

	length = len(s)
	# init a dp matrix
	parl_matrix = [[False for col in range(length)] for row in range(length)] 
	# init the start status
	for i in xrange(length):
		parl_matrix[i][i] = True

	# index tags to record the longest substring
	max_start = 0
	max_end = 0
	max_length = 1

	# state update
	for inv in xrange(1, length + 1): # increase the length interval from 1 to string length
		start = 0
		end = start + inv - 1
		while (end < length):
			if (start + 1) <= (end - 1): # base case
				parl_matrix[start][end] = parl_matrix[start + 1][end - 1] and s[start] == s[end]
			else: # case for two adjacent characters
				parl_matrix[start][end] = s[start] == s[end]

			if parl_matrix[start][end] == True: # if true, compare with the max length and update the maximum start and end index
				if max_length < inv:
					max_length = inv
					max_start = start
					max_end = end
			start += 1
			end = start + inv - 1

	return s[max_start:max_end+1]



def main():
	# test cases
	# should return radar
	print question2('radar')
	# should return abba
	print question2('abbac')
	# should return a
	print question2('a')

if __name__ == "__main__":
    main()




