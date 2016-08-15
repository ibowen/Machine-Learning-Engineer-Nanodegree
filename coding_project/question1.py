
"""
Design Choice:
Complexity: Python sort() using timsort algorithm which is a hybrid of merg sort and insertion sort. The timsort has the complexity of O(nlogn)
	Then the is_anagram has the complexity of O(nlogn)
"""
def is_anagram(str1, str2):
	"""
	Definition: helper function to check if two strings with the same length are anagram
	Parameters: str1, str2: string to be compaired
	Returns: True or False: boolean
	"""
	s1 = [i for i in str1] # break the string into an array
	s2 = [j for j in str2] 
	s1.sort() # sort the array
	s2.sort()
	return ''.join(s1) == ''.join(s2) # join the array back into string and compare two strings

def question1(s, t):
	"""
	Definition: function to check if one substring is the anagram of one string
	Parameters: s, t: string, substring
	Returns: True or False: boolean
	"""
	if len(s) < len(t): # longer substring is definitely not an anagram
		return False
	flag = False # set a flag to return
	for i in xrange(len(s) - len(t) + 1): # loop through each substring to compare with the target substring
		flag = is_anagram(s[i:i + len(t)], t)
		if flag:
			return flag
	return flag

def main():
	# test cases
	print "'udacity' and 'ad'(should be True) : {}".format(question1('udacity', 'ad'))
	print "'udacity' and 'jm'(should be False) : {}".format(question1('udacity', 'jm'))

if __name__ == "__main__":
    main()




