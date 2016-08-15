
"""
Question 2: Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.

Design Choice:
Complexity:
"""	
def is_parlindromic(substring):
	"""
	Definition: check if one string is parlindromic
	Parameters: substring: a string
	Returns: True or False: bool
	"""
	if substring is None or substring == '':
		return False
	length = len(substring)
	start = 0
	end = length - 1
	while start <= end:
		if substring[start] == substring[end]:
			start += 1
			end -= 1
			continue
		return False
	return True

def question2(s):
	"""
	Definition: return the longest parlindromic string
	Parameters: s: a target string
	Returns: a string
	"""
	if s is None or s == '':
		return ''
	length = len(s)
	if length == 1:
		return s
	for win_size in xrange(length, 0, -1):
		start = 0
		while start + win_size <= length:
			end = start + win_size
			if is_parlindromic(s[start:end]):
				return s[start:end]
			start += 1


def main():
	# test cases
	print "'radar' has the longest parlindromic string: {}".format(question2('radar'))
	print "'redivider' has the longest parlindromic string: {}".format(question2('redivider'))
	print "'ab' has the longest parlindromic string: {}".format(question2('aa'))
	print "'a' has the longest parlindromic string: {}".format(question2('a'))

if __name__ == "__main__":
    main()




