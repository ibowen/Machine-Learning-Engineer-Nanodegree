
"""
Question 1: Given two strings s and t, determine whether some anagram of t is a substring of s.

Design Choice: We have loop s to check if each substring has the same character. There is no choice but looping the string. 
We chould choose intersection or equation of two strings to check anagram. The first will take O(n^2), and the latter will take O(nlogn). 
So I choose the second one.

Time Complexity: O(n-k)*(klogk), suppose t has the length of k, and s has the length of n. 
Breaking string into list will take O(k). Python sort() using timsort algorithm which is a hybrid of merg sort and insertion sort. The timsort has the complexity of O(nlogn).
So, the is_anagram has the complexity of O(k + klogk). In question1 function, we move s along the index of t to check the anagram.
It will take (n-k). Therefore, the complexity is O(n-k)*(k + klogk)

Space Complexity: O(1), we don't need extra space
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
	if s is None or t is None:
		return False

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
	# should return true
	print question1('udacity', 'ad')
	# should return false
	print question1('udacity', 'jm')
	# should false
	print question1('udacity', '')
	# should false
	print question1('', 'd')
	# should false
	print question1('', None)
	# should false
	print question1(None, None)

if __name__ == "__main__":
    main()




